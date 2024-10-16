# Kara-Audio: The best Whisper Web UI for subtitle production.

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/kara-audio)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases)


**Kara-Audio是最佳的Whisper Web UI，用於字幕製作。** 它可以通過一鍵輕鬆安裝。使用Miniconda創建虛擬環境，與Windows系統完全獨立運行（完全可攜）。

- **YouTube下載器**: 您可以下載YouTube視頻並提取音頻（mp3、wav、flac）。
- **人聲去除器**: 使用UVR5中支持的MDX-Net和Meta開發的Demucs引擎進行聲音分離。
- **STT**: 支持使用Whisper、Faster-Whisper和whisper-timestamped的語音轉文本。
- 更多...

Kara-Audio將YouTube視頻轉換為您自己的卡拉OK音樂視頻。
您可以創建電影、劇集和新聞的逐字稿、會議記錄以及字幕。


### 🚄 運行畫面

https://github.com/abus-aikorea/kara-audio/assets/161691694/40bdc7d6-6924-4711-b3aa-b0af3ea29c38


## ⭐ 主要功能

  * `Kara Audio` 標籤頁
      - YouTube 下載器、人聲分離、自動字幕集成環境

<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.eng.png?raw=true" alt=""/>
</p>  

  * `Demixing` 標籤頁
    - 人聲分離、混響/回音消除
    - 支援 MDX-Net、Demucs 模型
    - 支援 3 種音頻輸出格式（wav、flac、mp3）

  * `Subtitle` 標籤頁
    - 語音識別、自動字幕（srt、vtt、txt）
    - 支援超過 90 種語言（英語、日語、法語、德語、中文、韓語）


## 💻 執行環境
* 操作系統：Windows 10/11（64位）**※不支持Linux和Mac OS。**
* GPU：推薦支持CUDA 12.1的**NVIDIA**顯卡。
* VRAM：4GB或以上。推薦8GB或以上。
* RAM：4GB或以上
* 硬碟：安裝時至少需要20GB的可用空間
* 需要網絡連接（安裝和翻譯工作）

## 📀 安裝

Kara-Audio可以輕鬆地一鍵安裝。只需運行🚀**configure.bat**和🚀**start.bat**即可。

### 步驟1. 準備包
* A. 付費版
    + 將USB中包含的壓縮文件（**kara-audio-x.zip**）解壓到電腦的適當位置。
    + 或者，將已解壓的文件夾（**kara-audio-x**）複製到電腦的適當位置。
* B. 免費版
  + 從[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/)克隆或下載最新版本（**Source code (zip)**）。

### 步驟2. 安裝和運行程序
1. 🚀 運行`configure.bat`
   - 在Windows上安裝git、ffmpeg和CUDA（如果使用NVIDIA GPU）。
   - 只需要在第一次運行時執行。
   - 需要網絡連接，根據系統情況可能需要一個多小時。
   - 安裝過程中切勿關閉Windows命令窗口。
2. 🚀 運行`start.bat`
   - 啟動Kara-Audio。網頁界面將自動運行。
   - 首次運行時，會先安裝Kara-Audio。
   - 需要網絡連接，根據系統情況可能需要一個多小時。
   - 安裝過程中切勿關閉Windows命令窗口。
   - 如果安裝過程中出現問題，請刪除**installer_files**文件夾並再次運行start.bat。

### 步驟3. 卸載程序
* 運行`uninstall.bat`：
  - 刪除**installer_files**文件夾。
  - 刪除安裝在Windows上的ffmpeg、git和CUDA包（如果選擇）。
* Kara-Audio默認為**便攜式**安裝。要卸載程序，只需刪除安裝文件夾即可。

## ❓ 提示和技巧

#### 如果瀏覽器沒有自動運行
- 關閉Windows命令窗口並再次運行start.bat。
- 直接運行瀏覽器並在地址欄輸入Windows命令窗口中顯示的地址（例如**http://127.0.0.1:7892**）。

#### 如果出現CUDA內存不足錯誤
- 在Windows任務管理器的性能選項卡中檢查GPU內存狀態。
- 將降噪級別設置為0或1。降噪級別2至少需要8GB的GPU內存。
- 將計算類型設置為int類型。float類型質量更好，但需要更多GPU內存。

#### 如何提高字幕質量？
- 字幕質量通常隨著更大的Whisper模型而提高，但並非總是如此。large > medium > small > base > tiny
- 在計算類型中，float類型性能較好。int類型是通過模型量化減少GPU使用並提高速度的模型。另一方面，性能會下降。
- 如果增加降噪級別，將會去除更多背景聲音，只使用剩餘的聲音進行語音識別。這並不總是保證好的結果。

#### 關於 Demixer
- Facebook Research 的 Demucs 模型（htdemucs、htdemucs_6s、htdemucs_ft、mdx_extra）都表現出色。
- Demucs 在低配置電腦上（8GB 內存）也能運行良好。
- 在 MDX-Net 中，UVR-MDX-NET-Voc_FT、Kim_Vocal_2、UVR_MDXNET_KARA_2 等表現出色。
- MDX-Net 模型只能在高配置電腦上運行（內存 16GB 或以上）。
- 建議逐一嘗試模型，找到適合您目的的模型。
- 建議使用最新的 NVIDIA 顯卡（VRAM 6GB 或以上）。如果 VRAM 不足，可能會出現內存不足錯誤。

#### 關於 Whisper
- Large-V2 模型最佳。其他模型識別率較差。
- 如果音頻語言是"韓語"，將 Whisper 語言也設置為"韓語"效果最佳。
- 當音頻語言是"韓語"時，如果將 Whisper 語言設置為"日語"，會輸出"日語"，但準確率會較低。（Google 翻譯更好）
- **降噪**選項使用 MDX-Net 模型消除噪音。可能會改善語音識別結果。（僅在高配置電腦上使用）

## 📢 注意

Windows Defender 可能會發出有關不受信任的應用程式的警告，並禁止進一步執行 Kara-Audio。
如果 SmartScreen 的安全級別設置為「警告」，只需點擊「更多資訊」，然後點擊「仍然要執行」。
如果 SmartScreen 設置為「阻止」級別，則不會有按鈕來運行安裝。在這種情況下，打開 start.bat 文件的屬性，檢查「解除封鎖」，應用更改後再次運行 start.bat。

<p align="center">
  <img style="width: 60%; height: 60%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  

當Windows Defender錯誤地將批處理文件識別為特洛伊木馬時，這通常被稱為"誤報"。要解決這個問題，您可以按照以下步驟操作：

1. 文件例外處理：在Windows Defender中，您可以設置某些文件或進程跳過安全掃描。要做到這一點，請按照以下步驟：
   * 點擊"開始"按鈕並進入"設置"。
   * 點擊"更新與安全"。
   * 選擇"Windows安全中心"並進入"病毒和威脅防護"。
   * 點擊"管理病毒和威脅防護設置"。
   * 在"病毒和威脅防護設置"中選擇"添加或刪除排除項"。
   * 選擇"文件或文件夾"，找到相關的批處理文件並將其添加為例外。
2. 暫時禁用Windows Defender：這可能是一個臨時解決方案。但是，使用此方法時必須小心，因為它可能會使您的計算機暴露於其他威脅中。
3. 向防病毒軟件報告問題：如果您確定該文件不是特洛伊木馬，可以將其作為誤報向Microsoft報告。Microsoft將審查此問題並採取必要的行動。

## 📬 聯繫我們
* 電子郵件：<abus.aikorea@gmail.com>
* 主頁（韓語）：<https://abuskorea.imweb.me>
* Amazon(USA): <https://www.amazon.com/dp/B0CTQQDPXT>
* Amazon(Japan): <https://www.amazon.co.jp/dp/B0CTHT2JH3>
* Amazon(Singapore): <https://www.amazon.sg/dp/B0DCGKMMG3>
* Amazon(UAE): <https://www.amazon.ae/dp/B0DCGQ1FGC>
* 韓國 Naver 智能商店：<https://smartstore.naver.com/abus/category/ALL?cp=1>


## 👍 YouTube
* 產品資訊：<https://youtube.com/playlist?list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq&si=873MgzUtu4POE9jO>
* 家庭卡拉OK(Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6&si=aWRDfF8TxFp2oAR0>
* 家庭卡拉OK(K-Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8&si=1_-9p722rd_JXpzv>
* 家庭卡拉OK(J-Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9apyxrP9LE9PiT821G7lJXk&si=0a474CP7ZIjMoGN9>
  

## 🙏 鳴謝
* UVR5：<https://github.com/Anjok07/ultimatevocalremovergui>
* FacebookResearch Demucs：<https://github.com/facebookresearch/demucs>
* OpenAI Whisper：<https://github.com/openai/whisper>
* Faster-Whisper：<https://github.com/SYSTRAN/faster-whisper>
* yt-dlp：<https://github.com/yt-dlp/yt-dlp>
* gradio：<https://github.com/gradio-app/gradio>

## ©️ 版權
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)
