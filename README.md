# Kara-Audio

🌍 [한국어](docs/README.kor.md) ∙ [English](docs/README.eng.md) ∙ [中文简体](docs/README.zh.md) ∙ [中文繁體](docs/README.tw.md) ∙ [日本語](docs/README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/kara-audio)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases)

The best gradio web-ui for vocal remover that uses demucs and mdx-net. 
Automatic subtitle creation using faster whisper. Easy one click installation. Fully portable.


### Running example

https://github.com/abus-aikorea/kara-audio/assets/161691694/40bdc7d6-6924-4711-b3aa-b0af3ea29c38




## Introduction
Kara-Audio is the new name of AI Studio. from 2024-04-10

* Kara-Audio turns YouTube videos into your own **karaoke music videos**.
* You can create **transcripts**, **meeting minutes**, as well as **subtitles** for movies, dramas, and news.
* It is equipped with **Vocal Remover** provided by UVR5 and **Automatic Subtitles** function using OpenAI Whisper.
* Kara-Audio can be easily installed with **one click** and provides Gradio Web-UI.



# main function

  * `Kara Audio` Tab
      - YouTube downloader, vocal removal, automatic subtitle integrated environment

<p align="center">
  <img style="width: 90%; height: 90%" src="docs/images/main_page.eng.png?raw=true" alt=""/>
</p>  

  * `Demixing` Tab
    - Vocal separation, Reverb/Echo removal
    - MDX-Net, Demucs model support
    - Supports 3 audio outputs (wav, flac, mp3)

  * `Subtitle` Tab
    - Voice recognition, Automatic subtitles (srt, vtt, txt)
    - Supports over 90 languages (English, Japanese, French, German, Chinese, 한국어)



## Key-Features
* You can download YouTube videos (mp4, webm) and save them as audio files (mp3, wav, flac).
* We provide vocal remover. Uses **MDX-Net** and **Demucs**.
* Automatic subtitle creation is possible through AI voice recognition. It uses OpenAI’s high-performance voice recognition engine, **Whisper**.
* Whisper supports over 90 languages, including Japanese, Korean, English, Chinese, French, and Spanish.
* **One-click installation**. Once installed, you can use it **permanently** at no additional cost. (※ Free version has **30 minute limit** on usage time)
* Provides **Web-UI**. Google Chrome browser is recommended.


## Running Environment
* OS : Windows 10/11 (64bits) **※ Linux, Mac OS is not supported.**
* CPU: Intel Processor 2GHz or faster (or equivalent compatible)
* RAM: 16GB or more
* HDD: At least 20GB of free space during installation
* GPU: NVIDIA graphics card supporting CUDA 12.3 is recommended. VRAM 6GB or more.
* Internet connection required (installation)


## Installing and running

### step 1. Package preparation
* A. Paid version
    + Unzip the compressed file (**kara-audio-x.zip**) included in the USB to an appropriate location on your computer.
    + Or, copy the already unzipped folder (**kara-audio-x**) to an appropriate location on your computer.

* B. Free version
  + Download and unzip the latest release ( **Source code (zip)** ) from [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases)
  + Or, download source code with git clone

```bash
git clone https://github.com/abus-aikorea/kara-audio.git
```

### step 2. How to install and run

0. Before installation
   - Run Windows Update to update the system to the latest status.
   - Update the NVIDIA Graphic Driver to the latest status.

1. Run `configure.bat`
     * Install ffmpeg and CUDA (if using an NVIDIA GPU) and the Windows SDK on Windows.
     * Installation requires an Internet connection and may take more than an hour depending on your computer specifications.
     * Never close the Windows-Command window during installation. (If the operation appears to have stopped, press the space bar occasionally)
     * If an error occurs during installation, we recommend running uninstall.bat and starting again from the beginning.
     * configure.bat only needs to be run once.

2. Run `start.bat`
     * Start Kara-Audio. Web-UI will run automatically.
     * When running for the first time, install Kara-Audio first.
     * Installation requires an Internet connection and may take more than an hour depending on your computer specifications.
     * Never close the Windows-Command window during installation. (If the operation appears to have stopped, press the space bar occasionally)
     * If an error occurs during installation, delete the installer_files folder and run start.bat again.

    #### When the browser does not run automatically
     * Close the Windows-Commnad window and run start.bat again or
     * Run the browser directly and enter the address displayed in the Windows-Command window (e.g. **http://127.0.0.1:7894** ) into the address bar.


### step 3. How to uninstall
* Run `uninstall.bat`
  * Remove installer_files . 
  * Remove the ffmepg, CUDA packages and Windows SDK installed on Windows (if selected)

* Kara-Audio has a **portable** installation as standard. To uninstall the program, deleting the installation folder is sufficient.


## Tips for use

1. About Demixer
   - Facebook Research's Demucs models (htdemucs, htdemucs_6s, htdemucs_ft, mdx_extra) all show good performance.
   - Demucs runs quite well even on low-end PCs (8GB of RAM).
   - In MDX-Net, UVR-MDX-NET-Voc_FT, Kim_Vocal_2, UVR_MDXNET_KARA_2, etc. show good performance.
   - MDX-Net models only operate on high-end PCs (RAM 16GB or more).
   - Try using the models one by one and find one that suits your purpose.
   - We recommend using the latest NVIDIA GPU (VRAM 6GB or higher). Out-of-memory errors may occur if VRAM is insufficient.

2. About Whisper
   - Large-V2 model is best. The rest have poor recognition rates.
   - If the audio language is 'Korean', it is best to set the Whisper language to 'Korean' as well.
   - When the audio language is 'Korean', if you set the Whisper language to 'Japanese', 'Japanese' will be output, but the accuracy will be low. (Google Translator is better.)
   - The **Denoise** option removes noise using the MDX-Net model. Voice recognition results may improve. (Use only on high-end PC)
   - 

## Caution!!
When Windows Defender mistakenly recognizes a batch file as a Trojan, this is often called a 'False Positive'. To solve this problem, you can go through the following steps:

1. File exception handling: In Windows Defender, you can set certain files or processes to skip security scanning. To do this, follow the steps below:
   * Click the ‘Start’ button and go to ‘Settings’.
   * Click ‘Update & Security’.
   * Select ‘Windows Security’ and go to ‘Virus & threat protection’.
   * Click ‘Manage Virus & Threat Protection Settings’.
   * Select 'Add exception' in 'Virus & threat protection settings'.
   * Select 'File or Folder', find the batch file in question and add it as an exception.
2. Temporarily disable Windows Defender: This may be a temporary solution. However, you must be careful when using this method as it may expose your computer to other threats.
3. Report the problem to anti-virus software: If you are sure that the file is not a Trojan horse, you can report it to Microsoft as a False Positive. Microsoft will review this and take any necessary action.


## Contact us
* e-mail: <abus.aikorea@gmail.com>
* homepage(Korean): <https://slashpage.com/abus>
* 네이버 스마트스토어(korean): <https://smartstore.naver.com/abus/category/ALL?cp=1>
* Coupang(Korean): <https://www.coupang.com/vp/products/7875503674>
* Amazon(US): <https://www.amazon.com/dp/B0CTQQDPXT>
* Amazon(Japan): <https://www.amazon.co.jp/dp/B0CTHT2JH3>


## YouTube
* Product Information: <https://youtu.be/heEN4UIQLjc>
* Automatic Subtitle∙Translation: <https://youtu.be/uQ14hoEiI4c?si=Io9K_vIDYyeu9Z8_>
* Home Karaoke: <https://youtube.com/playlist?list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6&si=TZBh5AFjcr7_dyiI>
  

## Credits
* UVR5: <https://github.com/Anjok07/ultimatevocalremovergui>
* FacebookResearch Demucs: <https://github.com/facebookresearch/demucs>
* OpenAI Whisper: <https://github.com/openai/whisper>
* Faster-Whisper: <https://github.com/SYSTRAN/faster-whisper>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>


## Copyright
<img src="docs/images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://slashpage.com/abus)