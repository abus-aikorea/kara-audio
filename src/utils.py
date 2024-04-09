import textwrap
import unicodedata
import re

import zlib
from typing import Iterator, TextIO, Union
import tqdm

import urllib3


def exact_div(x, y):
    assert x % y == 0
    return x // y


def str2bool(string):
    str2val = {"True": True, "False": False}
    if string in str2val:
        return str2val[string]
    else:
        raise ValueError(f"Expected one of {set(str2val.keys())}, got {string}")


def optional_int(string):
    return None if string == "None" else int(string)


def optional_float(string):
    return None if string == "None" else float(string)


def compression_ratio(text) -> float:
    return len(text) / len(zlib.compress(text.encode("utf-8")))


def format_timestamp(seconds: float, always_include_hours: bool = False, fractionalSeperator: str = '.'):
    assert seconds >= 0, "non-negative timestamp expected"
    milliseconds = round(seconds * 1000.0)

    hours = milliseconds // 3_600_000
    milliseconds -= hours * 3_600_000

    minutes = milliseconds // 60_000
    milliseconds -= minutes * 60_000

    seconds = milliseconds // 1_000
    milliseconds -= seconds * 1_000

    hours_marker = f"{hours:02d}:" if always_include_hours or hours > 0 else ""
    return f"{hours_marker}{minutes:02d}:{seconds:02d}{fractionalSeperator}{milliseconds:03d}"


def write_txt(transcript: Iterator[dict], file: TextIO):
    for segment in transcript:
        print(segment['text'].strip(), file=file, flush=True)


def write_vtt(transcript: Iterator[dict], file: TextIO, 
              maxLineWidth=None, highlight_words: bool = False):
    iterator  = __subtitle_preprocessor_iterator(transcript, maxLineWidth, highlight_words)

    print("WEBVTT\n", file=file)

    for segment in iterator:
        text = segment['text'].replace('-->', '->')

        print(
            f"{format_timestamp(segment['start'])} --> {format_timestamp(segment['end'])}\n"
            f"{text}\n",
            file=file,
            flush=True,
        )

def write_srt(transcript: Iterator[dict], file: TextIO, 
              maxLineWidth=None, highlight_words: bool = False):
    """
    Write a transcript to a file in SRT format.
    Example usage:
        from pathlib import Path
        from whisper.utils import write_srt
        result = transcribe(model, audio_path, temperature=temperature, **args)
        # save SRT
        audio_basename = Path(audio_path).stem
        with open(Path(output_dir) / (audio_basename + ".srt"), "w", encoding="utf-8") as srt:
            write_srt(result["segments"], file=srt)
    """
    iterator  = __subtitle_preprocessor_iterator(transcript, maxLineWidth, highlight_words)

    for i, segment in enumerate(iterator, start=1):
        text = segment['text'].replace('-->', '->')

        # write srt lines
        print(
            f"{i}\n"
            f"{format_timestamp(segment['start'], always_include_hours=True, fractionalSeperator=',')} --> "
            f"{format_timestamp(segment['end'], always_include_hours=True, fractionalSeperator=',')}\n"
            f"{text}\n",
            file=file,
            flush=True,
        )

def __subtitle_preprocessor_iterator(transcript: Iterator[dict], maxLineWidth: int = None, highlight_words: bool = False): 
    for segment in transcript:
        words = segment.get('words', [])

        if len(words) == 0:
            # Yield the segment as-is or processed
            if maxLineWidth is None or maxLineWidth < 0:
                yield segment
            else:
                yield {
                    'start': segment['start'],
                    'end': segment['end'],
                    'text': process_text(segment['text'].strip(), maxLineWidth)
                }
            # We are done
            continue

        subtitle_start = segment['start']
        subtitle_end = segment['end']

        text_words = [ this_word["word"] for this_word in words ]
        subtitle_text = __join_words(text_words, maxLineWidth)
        
        # Iterate over the words in the segment
        if highlight_words:
            last = subtitle_start

            for i, this_word in enumerate(words):
                start = this_word['start']
                end = this_word['end']

                if last != start:
                    # Display the text up to this point
                    yield {
                        'start': last,
                        'end': start,
                        'text': subtitle_text
                    }
                
                # Display the text with the current word highlighted
                yield {
                    'start': start,
                    'end': end,
                    'text': __join_words(
                        [
                            {
                                "word": re.sub(r"^(\s*)(.*)$", r"\1<font color=\"#0e556a\"><b><u>\2</u></b></font>", word)
                                        if j == i
                                        else word,
                                # The HTML tags <u> and </u> are not displayed, 
                                # # so they should not be counted in the word length
                                "length": len(word)
                            } for j, word in enumerate(text_words)
                        ], maxLineWidth)
                }
                last = end

            if last != subtitle_end:
                # Display the last part of the text
                yield {
                    'start': last,
                    'end': subtitle_end,
                    'text': subtitle_text
                }

        # Just return the subtitle text
        else:
            yield {
                'start': subtitle_start,
                'end': subtitle_end,
                'text': subtitle_text
            }

def __join_words(words: Iterator[Union[str, dict]], maxLineWidth: int = None):
    if maxLineWidth is None or maxLineWidth < 0:
        return " ".join(words)
    
    lines = []
    current_line = ""
    current_length = 0

    for entry in words:
        # Either accept a string or a dict with a 'word' and 'length' field
        if isinstance(entry, dict):
            word = entry['word']
            word_length = entry['length']
        else:
            word = entry
            word_length = len(word)

        if current_length > 0 and current_length + word_length > maxLineWidth:
            lines.append(current_line)
            current_line = ""
            current_length = 0
        
        current_length += word_length
        # The word will be prefixed with a space by Whisper, so we don't need to add one here
        current_line += word

    if len(current_line) > 0:
        lines.append(current_line)

    return "\n".join(lines)

def process_text(text: str, maxLineWidth=None):
    if (maxLineWidth is None or maxLineWidth < 0):
        return text

    lines = textwrap.wrap(text, width=maxLineWidth, tabsize=4)
    return '\n'.join(lines)

def slugify(value, allow_unicode=False):
    """
    Taken from https://github.com/django/django/blob/master/django/utils/text.py
    Convert to ASCII if 'allow_unicode' is False. Convert spaces or repeated
    dashes to single dashes. Remove characters that aren't alphanumerics,
    underscores, or hyphens. Convert to lowercase. Also strip leading and
    trailing whitespace, dashes, and underscores.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value.lower())
    return re.sub(r'[-\s]+', '-', value).strip('-_')

def download_file(url: str, destination: str):
        with urllib3.request.urlopen(url) as source, open(destination, "wb") as output:
            with tqdm(
                total=int(source.info().get("Content-Length")),
                ncols=80,
                unit="iB",
                unit_scale=True,
                unit_divisor=1024,
            ) as loop:
                while True:
                    buffer = source.read(8192)
                    if not buffer:
                        break

                    output.write(buffer)
                    loop.update(len(buffer))