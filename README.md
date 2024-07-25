# Aria-CoverSong

🌍 [한국어](docs/README.kor.md) ∙ [English](docs/README.eng.md) ∙ [日本語](docs/README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/aria-coversong)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/aria-coversong)](https://github.com/abus-aikorea/aria-coversong/releases)

The best gradio web-ui for creating cover song that uses mdx-net and rvc. Easy one click installation. Fully portable.


## Introduction
* Easily create **AI Cover** with Aria-CoverSong.
* Make a Trump version of IU's 'Cupid', Kim Kwang-seok's 'I Miss You', and 'Private's Letter'.
* Equipped with **Vocal Remover** provided by UVR5 and **RVC** engine.
* Aria-CoverSong can be easily installed with **one click** and provides Gradio Web-UI.
* Experience the highest level of **AI voice modulation** technology.


## main function

* `AI Cover` tab
  - YouTube downloader, vocal separation, and voice modulation provided in an integrated environment
  - Supports audio effects such as Pitch, Gain, Reverb, Room, Damping, etc.


<p align="center">
  <img style="width: 90%; height: 90%" src="docs/images/main_page.eng.png?raw=true" alt=""/>
</p>  


* `Demixing` tab
  - Vocal separation, Reverb/Echo removal
  - MDX-Net, Demucs model support
  - Selectable audio format (wav, flac, mp3)



## Key-Features
* You can download YouTube videos (mp4, webm) and save them as audio files (mp3, wav, flac).
* Provides vocal remover. Uses **MDX-Net** and **Demucs**.
* Provides voice modulation function. **RVC v2** is used.
* AI Voice can be downloaded from **Discord AI Hub** or, if necessary, **production request (abus.aikorea@gmail.com)**.
* **One-click installation**. Once installed, you can use it **permanently** at no additional cost. (※ Free version has **30 minute limit** on usage time)
* Provides **Web-UI**. Google Chrome browser is recommended.


## Running Environment
* OS : Windows 10/11 (64bits) **※ Linux, Mac OS is not supported.**
* CPU: Intel Processor 2GHz or faster (or equivalent compatible)
* RAM: 4GB or greater
* HDD: At least 10GB of free space during installation
* GPU: NVIDIA graphics card supporting CUDA 11.8 is recommended. VRAM 4GB or more.
* Internet connection required (installation)


## Installing and running

### step 1. Package preparation
* A. Paid version
    + Unzip the compressed file (**aria-coversong-x.zip**) included in the USB to an appropriate location on your computer.
    + Or, copy the already unzipped folder (**aria-coversong-x**) to an appropriate location on your computer.

* B. Free version
  + Download and unzip the latest release ( **Source code (zip)** ) from [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/aria-coversong)](https://github.com/abus-aikorea/aria-coversong/releases) 
  + Or, download source code with git clone

```bash
git clone https://github.com/abus-aikorea/aria-coversong.git
```

### step 2. Install and run the program
1. Run `configure.bat`
   - Install ffmpeg and CUDA (if using NVIDIA GPU) on Windows.
   - You only need to run it the first time.
2. Run `start.bat`
   - Start Aria-CoverSong. Web-UI will run automatically.
   - When running for the first time, install Aria-CoverSong first.
   - Aria-CoverSong installation requires an Internet connection, and depending on the system, installation may take more than an hour.
   - Never close the Windows-Command window during installation.
   - If a problem occurs during installation, delete the installer_files folder and run start.bat again.
#### If Browser does not run automatically
- Close the Windows-Commnad window and run start.bat again.
- Run the browser directly and enter the address displayed in the Windows-Command window (e.g. **http://127.0.0.1:7892**) in the address bar.


### Run screen

https://github.com/abus-aikorea/abus-code/assets/161691694/2379fc0d-6b23-4b83-99eb-94ba003bebe9


### step 3. Uninstall program
* Run `uninstall.bat`:
  - Remove the installer_files folder.
  - Remove ffmepg and CUDA packages installed on Windows (if selected)

* Aria-CoverSong has **portable** installation as standard. To uninstall the program, deleting the installation folder is sufficient.


## caution
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
* RVC-Project: <https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI>
* UVR5: <https://github.com/Anjok07/ultimatevocalremovergui>
* FacebookResearch Demucs: <https://github.com/facebookresearch/demucs>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>


## Copyright
<img src="docs/images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://slashpage.com/abus)
