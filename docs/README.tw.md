# Kara-Audio

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/kara-audio)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases)

最佳的人聲分離網頁界面，使用 demucs 和 mdx-net。
使用 faster whisper 自動生成字幕。簡單一鍵安裝。完全可攜式。

### 運行示例

https://github.com/abus-aikorea/kara-audio/assets/161691694/40bdc7d6-6924-4711-b3aa-b0af3ea29c38

## 簡介
Kara-Audio 是 AI Studio 的新名稱，從 2024-04-10 開始。

* Kara-Audio 可以將 YouTube 視頻轉換為您自己的**卡拉OK音樂視頻**。
* 您可以創建**文字稿**、**會議記錄**以及電影、電視劇和新聞的**字幕**。
* 配備了 UVR5 提供的**人聲分離**功能和使用 OpenAI Whisper 的**自動字幕**功能。
* Kara-Audio 可以**一鍵安裝**，並提供 Gradio 網頁界面。

# 主要功能

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

## 主要特點
* 您可以下載 YouTube 視頻（mp4、webm）並將其保存為音頻文件（mp3、wav、flac）。
* 我們提供人聲分離功能，使用 **MDX-Net** 和 **Demucs**。
* 通過 AI 語音識別可以自動創建字幕。使用 OpenAI 的高性能語音識別引擎 **Whisper**。
* Whisper 支援超過 90 種語言，包括日語、韓語、英語、中文、法語和西班牙語。
* **一鍵安裝**。安裝後，您可以**永久**使用，無需額外費用。（※ 免費版本使用時間限制為 **30 分鐘**）
* 提供**網頁界面**。推薦使用 Google Chrome 瀏覽器。

## 運行環境
* 作業系統：Windows 10/11（64位）**※ 不支援 Linux、Mac OS**
* CPU：Intel 處理器 2GHz 或更快（或相容等效處理器）
* 內存：16GB 或以上
* 硬碟：安裝時至少需要 20GB 可用空間
* 顯卡：建議使用支援 CUDA 12.3 的 NVIDIA 顯卡，VRAM 6GB 或以上
* 需要網際網路連接（安裝時）

## 安裝和運行

### 步驟 1. 軟件包準備
* A. 付費版本
    + 將 USB 中包含的壓縮文件（**kara-audio-x.zip**）解壓到電腦適當位置。
    + 或者，將已解壓的文件夾（**kara-audio-x**）複製到電腦適當位置。

* B. 免費版本
  + 從 [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases) 下載並解壓最新版本（**Source code (zip)**）
  + 或者，使用 git clone 下載源代碼

```bash
git clone https://github.com/abus-aikorea/kara-audio.git
```

### 步驟 2. 安裝和運行方法

0. 安裝前準備
   - 運行 Windows Update 將系統更新到最新狀態。
   - 將 NVIDIA 顯卡驅動更新到最新狀態。

1. 運行 `configure.bat`
     * 在 Windows 上安裝 ffmpeg、CUDA（如果使用 NVIDIA 顯卡）和 Windows SDK。
     * 安裝需要網際網路連接，根據電腦配置可能需要超過一小時。
     * 安裝過程中切勿關閉 Windows 命令窗口。（如果操作似乎停止，請偶爾按空格鍵）
     * 如果安裝過程中出現錯誤，建議運行 uninstall.bat 後從頭開始。
     * configure.bat 只需運行一次。

2. 運行 `start.bat`
     * 啟動 Kara-Audio。網頁界面將自動運行。
     * 首次運行時，先安裝 Kara-Audio。
     * 安裝需要網際網路連接，根據電腦配置可能需要超過一小時。
     * 安裝過程中切勿關閉 Windows 命令窗口。（如果操作似乎停止，請偶爾按空格鍵）
     * 如果安裝過程中出現錯誤，請刪除 installer_files 文件夾後重新運行 start.bat。

    #### 瀏覽器未自動運行時
     * 關閉 Windows 命令窗口並重新運行 start.bat，或
     * 直接運行瀏覽器並在地址欄輸入 Windows 命令窗口中顯示的地址（例如 **http://127.0.0.1:7894**）。

### 步驟 3. 卸載方法
* 運行 `uninstall.bat`
  * 移除 installer_files。
  * 移除在 Windows 上安裝的 ffmpeg、CUDA 包和 Windows SDK（如果選擇）

* Kara-Audio 採用**可攜式**安裝。要卸載程序，刪除安裝文件夾即可。

## 使用技巧

1. 關於 Demixer
   - Facebook Research 的 Demucs 模型（htdemucs、htdemucs_6s、htdemucs_ft、mdx_extra）都表現出色。
   - Demucs 在低配置電腦上（8GB 內存）也能運行良好。
   - 在 MDX-Net 中，UVR-MDX-NET-Voc_FT、Kim_Vocal_2、UVR_MDXNET_KARA_2 等表現出色。
   - MDX-Net 模型只能在高配置電腦上運行（內存 16GB 或以上）。
   - 建議逐一嘗試模型，找到適合您目的的模型。
   - 建議使用最新的 NVIDIA 顯卡（VRAM 6GB 或以上）。如果 VRAM 不足，可能會出現內存不足錯誤。

2. 關於 Whisper
   - Large-V2 模型最佳。其他模型識別率較差。
   - 如果音頻語言是"韓語"，將 Whisper 語言也設置為"韓語"效果最佳。
   - 當音頻語言是"韓語"時，如果將 Whisper 語言設置為"日語"，會輸出"日語"，但準確率會較低。（Google 翻譯更好）
   - **降噪**選項使用 MDX-Net 模型消除噪音。可能會改善語音識別結果。（僅在高配置電腦上使用）

## 注意事項
當 Windows Defender 錯誤地將批處理文件識別為特洛伊木馬時，這通常稱為"誤報"。要解決此問題，您可以按照以下步驟操作：

1. 文件例外處理：在 Windows Defender 中，您可以設置某些文件或進程跳過安全掃描。操作步驟如下：
   * 點擊"開始"按鈕，進入"設置"。
   * 點擊"更新和安全"。
   * 選擇"Windows 安全中心"並進入"病毒和威脅防護"。
   * 點擊"管理病毒和威脅防護設置"。
   * 在"病毒和威脅防護設置"中選擇"添加排除項"。
   * 選擇"文件或文件夾"，找到相關批處理文件並將其添加為例外。

2. 暫時禁用 Windows Defender：這可能是臨時解決方案。但使用此方法時必須小心，因為可能會使您的電腦暴露於其他威脅之下。

3. 向防病毒軟件報告問題：如果您確定該文件不是特洛伊木馬，可以向 Microsoft 報告為誤報。Microsoft 將審查並採取必要措施。

## 聯繫我們
* 電子郵件：<abus.aikorea@gmail.com>
* 主頁（韓語）：<https://abuskorea.imweb.me>
* Amazon(USA): <https://www.amazon.com/dp/B0CTQQDPXT>
* Amazon(Japan): <https://www.amazon.co.jp/dp/B0CTHT2JH3>
* Amazon(Singapore): <https://www.amazon.sg/dp/B0DCGKMMG3>
* Amazon(UAE): <https://www.amazon.ae/dp/B0DCGQ1FGC>
* 韓國 Naver 智能商店：<https://smartstore.naver.com/abus/category/ALL?cp=1>


## YouTube
* 產品資訊：<https://youtube.com/playlist?list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq&si=873MgzUtu4POE9jO>
* 家庭卡拉OK(Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6&si=aWRDfF8TxFp2oAR0>
* 家庭卡拉OK(K-Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8&si=1_-9p722rd_JXpzv>
* 家庭卡拉OK(J-Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9apyxrP9LE9PiT821G7lJXk&si=0a474CP7ZIjMoGN9>
  

## 致謝
* UVR5：<https://github.com/Anjok07/ultimatevocalremovergui>
* FacebookResearch Demucs：<https://github.com/facebookresearch/demucs>
* OpenAI Whisper：<https://github.com/openai/whisper>
* Faster-Whisper：<https://github.com/SYSTRAN/faster-whisper>
* yt-dlp：<https://github.com/yt-dlp/yt-dlp>
* gradio：<https://github.com/gradio-app/gradio>

## 版權
<img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://slashpage.com/abus)
