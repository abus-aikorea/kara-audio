# Kara-Audio: The best Whisper Web UI for subtitle production.

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/kara-audio)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases)


**Kara-Audioは字幕制作のための最高のWhisper Web UIです。** ワンクリックで簡単にインストールできます。Minicondaを使用して仮想環境を作成し、Windowsシステムとは完全に独立して動作します（完全にポータブル）。

- **YouTubeダウンローダー**: YouTube動画をダウンロードし、音声（mp3、wav、flac）を抽出できます。
- **ボーカルリムーバー**: UVR5でサポートされているMDX-Netと、Metaによって開発されたDemucsエンジンを使用して声を分離します。
- **STT**: Whisper、Faster-Whisper、およびwhisper-timestampedによる音声からテキストへの変換をサポートします。
- もっと...

Kara-AudioはYouTube動画を自分のカラオケミュージックビデオに変えます。
映画、ドラマ、ニュースのトランスクリプト、議事録、字幕を作成できます。


### 🚄 実行画面

* `Kara Audio` タブ
<video src="https://github.com/abus-aikorea/kara-audio/assets/161691694/40bdc7d6-6924-4711-b3aa-b0af3ea29c38" width="100%" style="max-width: 720px;" controls="controls" muted="muted"></video>




## ⭐ 主な機能

* `Kara Audio` タブ
  - YouTubeダウンローダ、ボーカル削除、自動字幕統合環境

<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.jpn.png?raw=true" alt=""/>
</p>  


* `Demixing` タブ
  - ボーカル除去、リバーブ/エコーの除去。 MR制作。 
  - MDX-Net、Demucsモデルのサポート
  - 3つのオーディオ出力（wav、flac、mp3）をサポート
  
* `字幕` タブ
  - 音声認識、自動字幕（srt、vtt、txt）
  - 90以上の言語をサポート



## 💻 実行環境
* OS: Windows 10/11（64ビット）**※ LinuxとMac OSはサポートされていません。**
* GPU: CUDA 12.1をサポートする**NVIDIA**グラフィックカードを推奨。
* VRAM: 4GB以上。8GB以上を推奨。
* RAM: 4GB以上
* HDD: インストール時に少なくとも20GBの空き容量が必要
* インターネット接続が必要（インストールと翻訳作業）


## 📀 インストール

Kara-Audioはワンクリックで簡単にインストールできます。🚀**configure.bat**と🚀**start.bat**を実行するだけです。

### ステップ1. パッケージの準備
* A. 有料版
    + USBに含まれる圧縮ファイル（**kara-audio-x.zip**）をコンピューターの適切な場所に解凍します。
    + または、すでに解凍されているフォルダ（**kara-audio-x**）をコンピューターの適切な場所にコピーします。
* B. 無料版
  + [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/)から最新リリース（**Source code (zip)**）をクローンまたはダウンロードします。

### ステップ2. プログラムのインストールと実行
1. 🚀 `configure.bat`を実行
   - Windows上にgit、ffmpeg、CUDA（NVIDIAのGPUを使用する場合）をインストールします。
   - 初回のみ実行する必要があります。
   - インターネット接続が必要で、システムによっては1時間以上かかる場合があります。
   - インストール中はWindows-Commandウィンドウを絶対に閉じないでください。
2. 🚀 `start.bat`を実行
   - Kara-Audioを起動します。Web-UIが自動的に実行されます。
   - 初回実行時は、まずKara-Audioがインストールされます。
   - インターネット接続が必要で、システムによっては1時間以上かかる場合があります。
   - インストール中はWindows-Commandウィンドウを絶対に閉じないでください。
   - インストール中に問題が発生した場合は、**installer_files**フォルダを削除し、start.batを再度実行してください。

### ステップ3. プログラムのアンインストール
* `uninstall.bat`を実行:
  - **installer_files**フォルダを削除します。
  - Windows上にインストールされたffmpeg、git、CUDAパッケージを削除します（選択した場合）。
* Kara-Audioは標準で**ポータブル**インストールです。プログラムをアンインストールするには、インストールフォルダを削除するだけで十分です。

## step 3. アンインストールする方法
* `uninstall.bat`の実行
  - installer_files フォルダを削除します。 
  - Windowsにインストールしたffmepg、CUDAパッケージ、Windows SDKを削除します（選択した場合）

* Kara-Audioは**ポータブル**インストールがデフォルトです。 プログラムの削除は、インストールフォルダを削除するだけで十分です。


## ❓ヒントとコツ

#### ブラウザが自動的に起動しない場合
- Windows-Commandウィンドウを閉じて、start.batを再度実行してください。
- ブラウザを直接起動し、Windows-Commandウィンドウに表示されているアドレス（例：**http://127.0.0.1:7892**）をアドレスバーに入力してください。

#### CUDA Out-Of-Memoryエラーが発生した場合
- WindowsタスクマネージャーのパフォーマンスタブでGPUメモリの状態を確認してください。
- ノイズ除去レベルを0または1に設定してください。ノイズ除去レベル2には少なくとも8GBのGPUメモリが必要です。
- Compute Typeをintタイプに設定してください。floatタイプは品質が良いですが、より多くのGPUメモリを必要とします。

#### 字幕の品質を向上させるには？
- 字幕の品質は、より大きなWhisperモデルで向上する傾向がありますが、必ずしもそうではありません。large > medium > small > base > tiny
- Compute Typeの中では、floatタイプのパフォーマンスが良いです。intタイプはモデル量子化によってGPU使用量を減らし、速度を上げるモデルです。一方で、パフォーマンスは低下します。
- ノイズ除去レベルを上げると、より多くのバックグラウンドサウンドが除去され、残った音声のみが音声認識に使用されます。必ずしも良い結果を保証するものではありません。

#### Demixerの使用
- Facebook ResearchのDemucsモデル（htdemucs、htdemucs_6s、htdemucs_ft、mdx_extra）はすべて良いパフォーマンスを示しています。
- Demucsは低仕様PC（RAM 8GB）でも非常にうまく動作します。
- MDX-Netでは、UVR-MDX-NET-Voc_FT、Kim_Vocal_2、UVR_MDXNET_KARA_2などが良いパフォーマンスを示しています。
- MDX-Netモデルは、高仕様PC（RAM 16GB以上）でのみ動作します。
- モデルを一つずつ使ってみて、目的に合ったものを探してください。
- NVIDIA 最新のGPU(6GB以上のVRAM)の使用を推奨します. VRAMが不足すると、Out-Of-Memoryエラーが発生する可能性があります。

#### Whisperの使用
- Large-V2モデルが最適です。残りは認識率が悪い。
- オーディオの言語が「韓国語」の場合、Whisperの言語設定も「韓国語」にするのが最善です。
- オーディオの言語が「韓国語」のとき、Whisperの言語設定を「日本語」にすると「日本語」を出力しますが、精度は低下します。 （むしろグーグル翻訳者は良いです。）
- **Denoise**オプションを使用すると、MDX-Netモデルを使用してノイズを除去します。音声認識結果が良くなることがあります。 （高仕様PCでのみお使いください）




## 📢 注意

Windows Defenderは信頼できないアプリケーションに関する警告を表示し、Kara-Audioのさらなる実行を許可しない場合があります。
SmartScreenのセキュリティレベルが「警告」に設定されている場合は、「詳細情報」をクリックし、その後「続行」をクリックしてください。
SmartScreenが「ブロック」に設定されている場合、インストールを実行するボタンは表示されません。この場合、start.batファイルのプロパティを開き、「ブロック解除」をチェックし、変更を適用してからstart.batを再度実行してください。

<p align="center">
  <img style="width: 60%; height: 60%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  

Windows Defenderがバッチファイルを誤ってトロイの木馬と認識した場合、これは「誤検出」と呼ばれることがよくあります。この問題を解決するには、以下の手順を行うことができます：

1. ファイルの例外処理：Windows Defenderで、特定のファイルやプロセスをセキュリティスキャンの対象から除外するように設定できます。そのためには、以下の手順に従ってください：
   * 「スタート」ボタンをクリックし、「設定」に進みます。
   * 「更新とセキュリティ」をクリックします。
   * 「Windowsセキュリティ」を選択し、「ウイルスと脅威の防止」に進みます。
   * 「ウイルスと脅威の防止の設定を管理する」をクリックします。
   * 「ウイルスと脅威の防止の設定」で「除外を追加または削除」を選択します。
   * 「ファイルまたはフォルダー」を選択し、問題のバッチファイルを見つけて例外として追加します。
2. Windows Defenderを一時的に無効にする：これは一時的な解決策かもしれません。ただし、この方法を使用する場合は、コンピューターが他の脅威にさらされる可能性があるため、注意が必要です。
3. 問題をアンチウイルスソフトウェアに報告する：ファイルがトロイの木馬でないことが確実な場合、誤検出としてMicrosoftに報告することができます。Microsoftはこれをレビューし、必要な対応を取ります。


## 📬 製品お問い合わせ
* メール: <abus.aikorea@gmail.com>
* ホームページ(韓国語): <https://abuskorea.imweb.me>
* Amazon(USA): <https://www.amazon.com/dp/B0CTQQDPXT>
* Amazon(日本): <https://www.amazon.co.jp/dp/B0CTHT2JH3>
* Amazon(Singapore): <https://www.amazon.sg/dp/B0DCGKMMG3>
* Amazon(UAE): <https://www.amazon.ae/dp/B0DCGQ1FGC>
* 네이버 스마트스토어(韓国語): <https://smartstore.naver.com/abus/category/ALL?cp=1>

## 👍 YouTube
* 商品説明: <https://youtube.com/playlist?list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq&si=873MgzUtu4POE9jO>
* ホームカラオケ (Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9bVxfGo58U-R-w3fUHqwiD6&si=aWRDfF8TxFp2oAR0>
* ホームカラオケ (K-Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8&si=1_-9p722rd_JXpzv>
* ホームカラオケ (J-Pop): <https://youtube.com/playlist?list=PLwx5dnMDVC9apyxrP9LE9PiT821G7lJXk&si=0a474CP7ZIjMoGN9>

## 🙏 Credits
* UVR5: <https://github.com/Anjok07/ultimatevocalremovergui>
* FacebookResearch Demucs: <https://github.com/facebookresearch/demucs>
* OpenAI Whisper: <https://github.com/openai/whisper>
* Faster-Whisper: <https://github.com/SYSTRAN/faster-whisper>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>


## ©️ 著作権
<img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)