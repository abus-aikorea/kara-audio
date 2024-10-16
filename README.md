# Kara-Audio: The best Whisper Web UI for subtitle production.

🌍 [한국어](docs/README.kor.md) ∙ [English](docs/README.eng.md) ∙ [中文简体](docs/README.zh.md) ∙ [中文繁體](docs/README.tw.md) ∙ [日本語](docs/README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/kara-audio)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases)


**Kara-Audio is The best Whisper Web UI for subtitle production.** It can be easily installed with one click. Create a virtual environment using Miniconda, running completely separate from the Windows system (fully portable).

- **YouTube Downloader**: You can download YouTube videos and extract the audio (mp3, wav, flac).
- **Vocal Remover**: Use MDX-Net supported in UVR5 and the Demucs engine developed by Meta for voice separation.
- **STT**: Supports speech-to-text conversion with Whisper, Faster-Whisper, and whisper-timestamped.
- more...

Kara-Audio turns YouTube videos into your own karaoke music videos.
You can create transcripts, meeting minutes, as well as subtitles for movies, dramas, and news.



### 🚄 Run screen

https://github.com/abus-aikorea/kara-audio/assets/161691694/40bdc7d6-6924-4711-b3aa-b0af3ea29c38


## ⭐ Key Features

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


## 💻 Execution environment
* OS: Windows 10/11 (64bits) **※ Linux and Mac OS are not supported.**
* GPU: **NVIDIA** graphics card supporting CUDA 12.1 recommended. 
* VRAM: 4GB or more. 8GB or more recommended.
* RAM: 4GB or more
* HDD: At least 20GB of free space during installation
* Internet connection required (installation and translation work)



## 📀 Installation

Kara-Audio can be easily installed with one click. Just run 🚀**configure.bat** and 🚀**start.bat**


### step 1. Package preparation
* A. Paid version
    + Unzip the compressed file (**kara-audio-x.zip**) included in the USB to an appropriate location on your computer.
    + Or, copy the already unzipped folder (**kara-audio-x**) to an appropriate location on your computer.
* B. Free version
  + Clone or download the latest release (**Source code (zip)**) from  [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/)
  

### step 2. Install and run the program
1. 🚀 Run `configure.bat`
   - Install git, ffmpeg and CUDA (if using NVIDIA GPU) on Windows. 
   - You only need to run it the first time.
   - An internet connection is required, and it may take over an hour depending on the system.
   - Never close the Windows-Command window during installation.
2. 🚀 Run `start.bat`
   - Start Kara-Audio. Web-UI will run automatically. 
   - When running for the first time, Kara-Audio is installed first. 
   - An internet connection is required, and it may take over an hour depending on the system. 
   - Never close the Windows-Command window during installation.
   - If a problem occurs during installation, delete the **installer_files** folder and run start.bat again.

### step 3. Uninstall program
* Run `uninstall.bat`:
  - Remove the **installer_files** folder.
  - Remove ffmepg, git and CUDA packages installed on Windows (if selected)
* Kara-Audio has **portable** installation as standard. To uninstall the program, deleting the installation folder is sufficient.



## ❓Tips & Tricks

#### If Browser does not run automatically
- Close the Windows-Commnad window and run start.bat again.
- Run the browser directly and enter the address displayed in the Windows-Command window (e.g. **http://127.0.0.1:7892**) in the address bar.

#### If a CUDA Out-Of-Memory error occurs
- Check the GPU memory status in Windows Task Manager - Performance tab. 
- Set the Denoise level to 0 or 1. Denoise level 2 requires at least 8GB of GPU memory.
- Set Compute Type to int type. The float type has better quality, but requires more GPU memory.

#### How to improve the quality of subtitles?
- The quality of subtitles tends to improve with larger Whisper models, but this is not necessarily the case. large > medium > small > base > tiny 
- Among compute types, float type has good performance. The int type is a model that reduces GPU usage and increases speed through model quantization. On the other hand, performance decreases. 
- If you increase the denoise level, more background sounds will be removed, and only the remaining voice will be used for voice recognition. It does not always guarantee good results.
  

#### About Demixer
- Facebook Research's Demucs models (htdemucs, htdemucs_6s, htdemucs_ft, mdx_extra) all show good performance.
- Demucs runs quite well even on low-end PCs (8GB of RAM).
- In MDX-Net, UVR-MDX-NET-Voc_FT, Kim_Vocal_2, UVR_MDXNET_KARA_2, etc. show good performance.
- MDX-Net models only operate on high-end PCs (RAM 16GB or more).
- Try using the models one by one and find one that suits your purpose.
- We recommend using the latest NVIDIA GPU (VRAM 6GB or higher). Out-of-memory errors may occur if VRAM is insufficient.

#### About Whisper
- Large-V2 model is best. The rest have poor recognition rates.
- If the audio language is 'Korean', it is best to set the Whisper language to 'Korean' as well.
- When the audio language is 'Korean', if you set the Whisper language to 'Japanese', 'Japanese' will be output, but the accuracy will be low. (Google Translator is better.)
- The **Denoise** option removes noise using the MDX-Net model. Voice recognition results may improve. (Use only on high-end PC)



## 📢 caution

Windows Defender may give a warning about untrusted application and disallow further execution of Kara-Audio.
If SmartScreen security level is set to "Warn", just click "More info" and then click "Run anyway". 
If SmartScreen is set to level "Block" there will be no button to run the installation. In this case, open the properties of the start.bat file, and check "Unblock", apply the change and run the start.bat again.

<p align="center">
  <img style="width: 60%; height: 60%" src="docs/images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  


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


## 📬 Contact us
* e-mail: <abus.aikorea@gmail.com>
* homepage(Korean): <https://abuskorea.imweb.me>
* Amazon(USA): <https://www.amazon.com/dp/B0CTQQDPXT>
* Amazon(Japan): <https://www.amazon.co.jp/dp/B0CTHT2JH3>
* Amazon(Singapore): <https://www.amazon.sg/dp/B0DCGKMMG3>
* Amazon(UAE): <https://www.amazon.ae/dp/B0DCGQ1FGC>
* 네이버 스마트스토어(korean): <https://smartstore.naver.com/abus/category/ALL?cp=1>



## 👍 YouTube
* Product Information: <https://youtube.com/playlist?list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq&si=873MgzUtu4POE9jO>
* Home Karaoke (Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6&si=aWRDfF8TxFp2oAR0>
* Home Karaoke (K-Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8&si=1_-9p722rd_JXpzv>
* Home Karaoke (J-Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9apyxrP9LE9PiT821G7lJXk&si=0a474CP7ZIjMoGN9>
  

## 🙏 Credits
* UVR5: <https://github.com/Anjok07/ultimatevocalremovergui>
* FacebookResearch Demucs: <https://github.com/facebookresearch/demucs>
* OpenAI Whisper: <https://github.com/openai/whisper>
* Faster-Whisper: <https://github.com/SYSTRAN/faster-whisper>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>



## ©️ Copyright
  <img src="docs/images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)

