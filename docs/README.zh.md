# Kara-Audio: The best Whisper Web UI for subtitle production.

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/kara-audio)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases)

**Kara-Audio是最佳的Whisper Web UI，用于字幕制作。** 它可以通过一键轻松安装。使用Miniconda创建虚拟环境，与Windows系统完全独立运行（完全可携）。

- **YouTube下载器**: 您可以下载YouTube视频并提取音频（mp3、wav、flac）。
- **人声去除器**: 使用UVR5中支持的MDX-Net和Meta开发的Demucs引擎进行声音分离。
- **STT**: 支持使用Whisper、Faster-Whisper和whisper-timestamped的语音转文本。
- 更多...

Kara-Audio将YouTube视频转换为您自己的卡拉OK音乐视频。
您可以创建电影、剧集和新闻的逐字稿、会议记录以及字幕。



### 🚄 运行画面

  * `Kara Audio` 标签页
<video src="https://github.com/abus-aikorea/kara-audio/assets/161691694/40bdc7d6-6924-4711-b3aa-b0af3ea29c38" width="100%" style="max-width: 720px;" controls="controls" muted="muted"></video>



## ⭐ 主要功能

  * `Kara Audio` 标签页
      - YouTube下载器、人声移除、自动字幕集成环境

<p align="center">
<img style="width: 90%; height: 90%" src="images/main_page.eng.png?raw=true" alt=""/>
</p>  

  * `Demixing` 标签页
    - 人声分离、混响/回音去除
    - 支持MDX-Net、Demucs模型
    - 支持3种音频输出格式（wav、flac、mp3）

  * `Subtitle` 标签页
    - 语音识别、自动字幕（srt、vtt、txt）
    - 支持90多种语言（英语、日语、法语、德语、中文、韩语）


## 💻 执行环境
* 操作系统：Windows 10/11（64位）**※不支持Linux和Mac OS。**
* GPU：推荐支持CUDA 12.1的**NVIDIA**显卡。
* VRAM：4GB或以上。推荐8GB或以上。
* RAM：4GB或以上
* 硬盘：安装时至少需要20GB的可用空间
* 需要网络连接（安装和翻译工作）

## 📀 安装

Kara-Audio可以轻松地一键安装。只需运行🚀**configure.bat**和🚀**start.bat**即可。

### 步骤1. 准备包
* A. 付费版
    + 将USB中包含的压缩文件（**kara-audio-x.zip**）解压到计算机的适当位置。
    + 或者，将已解压的文件夹（**kara-audio-x**）复制到计算机的适当位置。
* B. 免费版
  + 从[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/)克隆或下载最新版本（**Source code (zip)**）。

### 步骤2. 安装和运行程序
1. 🚀 运行`configure.bat`
   - 在Windows上安装git、ffmpeg和CUDA（如果使用NVIDIA GPU）。
   - 只需要在第一次运行时执行。
   - 需要网络连接，根据系统情况可能需要一个多小时。
   - 安装过程中切勿关闭Windows命令窗口。
2. 🚀 运行`start.bat`
   - 启动Kara-Audio。网页界面将自动运行。
   - 首次运行时，会先安装Kara-Audio。
   - 需要网络连接，根据系统情况可能需要一个多小时。
   - 安装过程中切勿关闭Windows命令窗口。
   - 如果安装过程中出现问题，请删除**installer_files**文件夹并再次运行start.bat。

### 步骤3. 卸载程序
* 运行`uninstall.bat`：
  - 删除**installer_files**文件夹。
  - 删除安装在Windows上的ffmpeg、git和CUDA包（如果选择）。
* Kara-Audio默认为**便携式**安装。要卸载程序，只需删除安装文件夹即可。

## ❓ 提示和技巧

#### 如果浏览器没有自动运行
- 关闭Windows命令窗口并再次运行start.bat。
- 直接运行浏览器并在地址栏输入Windows命令窗口中显示的地址（例如**http://127.0.0.1:7892**）。

#### 如果出现CUDA内存不足错误
- 在Windows任务管理器的性能选项卡中检查GPU内存状态。
- 将降噪级别设置为0或1。降噪级别2至少需要8GB的GPU内存。
- 将计算类型设置为int类型。float类型质量更好，但需要更多GPU内存。

#### 如何提高字幕质量？
- 字幕质量通常随着更大的Whisper模型而提高，但并非总是如此。large > medium > small > base > tiny
- 在计算类型中，float类型性能较好。int类型是通过模型量化减少GPU使用并提高速度的模型。另一方面，性能会下降。
- 如果增加降噪级别，将会去除更多背景声音，只使用剩余的声音进行语音识别。这并不总是保证好的结果。

#### 关于Demixer
- Facebook Research的Demucs模型（htdemucs、htdemucs_6s、htdemucs_ft、mdx_extra）都表现良好。
- Demucs即使在低端电脑（8GB内存）上也运行得相当好。
- 在MDX-Net中，UVR-MDX-NET-Voc_FT、Kim_Vocal_2、UVR_MDXNET_KARA_2等表现良好。
- MDX-Net模型只能在高端电脑（16GB或更高内存）上运行。
- 尝试一个个使用这些模型，找到适合您目的的模型。
- 我们建议使用最新的NVIDIA GPU（6GB或更高VRAM）。如果VRAM不足，可能会出现内存不足错误。

#### 关于Whisper
- Large-V2模型最佳。其他模型识别率较差。
- 如果音频语言是"韩语"，最好也将Whisper语言设置为"韩语"。
- 当音频语言是"韩语"时，如果将Whisper语言设置为"日语"，会输出"日语"，但准确度会很低。（Google翻译更好。）
- **Denoise**选项使用MDX-Net模型去除噪音。可能会改善语音识别结果。（仅在高端电脑上使用）

## 📢 注意

Windows Defender 可能会发出有关不受信任的应用程序的警告，并禁止进一步执行 Kara-Audio。
如果 SmartScreen 的安全级别设置为“警告”，只需点击“更多信息”，然后点击“仍然要运行”。
如果 SmartScreen 设置为“阻止”级别，则不会有按钮来运行安装。在这种情况下，打开 start.bat 文件的属性，检查“解除阻止”，应用更改后再次运行 start.bat。

<p align="center">
  <img style="width: 60%; height: 60%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  

当Windows Defender错误地将批处理文件识别为特洛伊木马时，这通常被称为"误报"。要解决这个问题，您可以按照以下步骤操作：

1. 文件例外处理：在Windows Defender中，您可以设置某些文件或进程跳过安全扫描。要做到这一点，请按照以下步骤：
   * 点击"开始"按钮并进入"设置"。
   * 点击"更新与安全"。
   * 选择"Windows安全中心"并进入"病毒和威胁防护"。
   * 点击"管理病毒和威胁防护设置"。
   * 在"病毒和威胁防护设置"中选择"添加或删除排除项"。
   * 选择"文件或文件夹"，找到相关的批处理文件并将其添加为例外。
2. 暂时禁用Windows Defender：这可能是一个临时解决方案。但是，使用此方法时必须小心，因为它可能会使您的计算机暴露于其他威胁中。
3. 向防病毒软件报告问题：如果您确定该文件不是特洛伊木马，可以将其作为误报向Microsoft报告。Microsoft将审查此问题并采取必要的行动。

## 📬 联系我们
* 电子邮件：<abus.aikorea@gmail.com>
* 主页（韩语）：<https://abuskorea.imweb.me>
* Amazon(USA): <https://www.amazon.com/dp/B0CTQQDPXT>
* Amazon(Japan): <https://www.amazon.co.jp/dp/B0CTHT2JH3>
* Amazon(Singapore): <https://www.amazon.sg/dp/B0DCGKMMG3>
* Amazon(UAE): <https://www.amazon.ae/dp/B0DCGQ1FGC>
* 네이버 스마트스토어（韩语）：<https://smartstore.naver.com/abus/category/ALL?cp=1>


## 👍 YouTube
* 产品信息：<https://youtube.com/playlist?list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq&si=873MgzUtu4POE9jO>
* 家庭卡拉OK(Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6&si=aWRDfF8TxFp2oAR0>
* 家庭卡拉OK(K-Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8&si=1_-9p722rd_JXpzv>
* 家庭卡拉OK(J-Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9apyxrP9LE9PiT821G7lJXk&si=0a474CP7ZIjMoGN9>

## 🙏 鸣谢
* UVR5：<https://github.com/Anjok07/ultimatevocalremovergui>
* FacebookResearch Demucs：<https://github.com/facebookresearch/demucs>
* OpenAI Whisper：<https://github.com/openai/whisper>
* Faster-Whisper：<https://github.com/SYSTRAN/faster-whisper>
* yt-dlp：<https://github.com/yt-dlp/yt-dlp>
* gradio：<https://github.com/gradio-app/gradio>

## ©️ 版权
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)
