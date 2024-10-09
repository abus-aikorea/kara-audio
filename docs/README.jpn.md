# Kara-Audio

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/kara-audio)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases)


The best gradio web-ui for vocal remover that uses demucs and mdx-net. Automatic subtitle creation using faster whisper. Easy one click installation. Fully portable.


### 実行画面

https://github.com/abus-aikorea/kara-audio/assets/161691694/1255ca26-4454-4224-9558-921dc72295ef



## はじめに
Kara-AudioはAI Studioの新しい名前です。from 2024-04-10

* Kara-AudioはYouTubeの動画をあなただけの**カラオケムービー**にしています。
* **録音録**、**会議録**はもちろん、映画、ドラマ、ニュースの**字幕**を作ることができます。
* UVR5が提供する**ボーカルリムーバー**とOpenAI Whisperを利用した**自動字幕**機能を搭載しています。
* Kara-Audioは**ワンクリック**で簡単にインストールでき、Gradio Web-UIを提供します。


## 主な機能

* `スタジオ` タブ
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



## 特徴
* YouTubeビデオのダウンロードには**yt-dlp**を使用してください。
* YouTube動画（mp4、webm）をダウンロードし、オーディオファイル（mp3、wav、flac）として保存することもできます。
* Facebook Researchの音源分離(music source separation)システムのDemucsを提供します。
* OpenAIの高性能文字起こしAI「Whisper」を提供します。
* 一度設置すれば、追加費用なしで**永続的**に使用することができます。 ( ※ Free版は利用時間**30分制限**あり)
* **Gradio Web-UI**を提供します。 Google Chrome ブラウザをお勧めします。
* 日本語、韓国語、英語、中国語、フランス語、スペイン語など90余りの言語に対応しています。


## 実行要件
* OS : Windows 10/11 (64bits) **※ Linux, Mac OSには対応しておりません。**
* CPU: Intelプロセッサ 2GHz以上(または同等の互換プロセッサ)
* RAM: 16GB 以上
* HDD: 20GB以上の空き容量(インストール時)
* GPU: :CUDA 12.3に対応するNVIDIAグラフィックカードを推奨。VRAM 6GB以上。
* インターネット接続環境必須(インストール時)


## インストールと実行

### step 1. パッケージの準備
* A.有料バージョン
    + USBに含まれる圧縮ファイル（**kara-audio-x.zip**）をコンピュータの適切な場所に解凍する
    + またはすでに解凍されているフォルダ（**kara-audio-x**）をコンピュータの適切な場所にコピーする

* B. 無料版
  + [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases) から最新リリース (**Source code (zip)**) ダウンロード後に解凍
  + または、git cloneでソースコードをダウンロードする

```bash
git clone https://github.com/abus-aikorea/kara-audio.git
```

## step 2. インストールして実行する方法

0. 設置前
   - Windows Updateを実行してシステムを最新の状態に更新します。
   - NVIDIA Graphic Driverを最新の状態に更新します。

1. `configure.bat`の実行
     * WindowsにffmpegとCUDA（NVIDIA GPUを使用している場合）とWindows SDKをインストールします。
     * インストールにはインターネットに接続する必要があり、コンピュータの仕様によっては1時間以上かかることがあります。
     * インストール中は絶対にWindowsコマンドウィンドウを終了しないでください。 （作業が止まったように見える場合は、スペースバーをたまに押してください）
     * インストール中にエラーが発生した場合は、uninstall.batを実行してから最初から再起動することをお勧めします。
     * configure.batは最初の1回だけ実行できます。

2. `start.bat`の実行
     - Kara-Audioを起動します。 Web-UIが自動的に起動します。 
     - 初回実行時には、Kara-Audioのインストール作業を先に進めます。
     - インストールにはインターネットに接続する必要があり、システムによっては1時間以上かかることがあります。
     - インストール中は絶対にWindowsコマンドウィンドウを終了しないでください。 （作業が止まったように見える場合は、スペースバーをたまに押してください）
     - インストール中にエラーが発生した場合は、installer_filesフォルダを削除してstart.batを再実行してください。

    #### Browserが自動的に実行されない場合
    - Windows-Commnadウィンドウを終了し、start.batを再実行するか、
    - Browserを直接実行し、Windows-Commnadウィンドウに表示されたアドレス（例：**http://127.0.0.1:7894** ）をアドレスウィンドウに入力します。



## step 3. アンインストールする方法
* `uninstall.bat`の実行
  - installer_files フォルダを削除します。 
  - Windowsにインストールしたffmepg、CUDAパッケージ、Windows SDKを削除します（選択した場合）

* Kara-Audioは**ポータブル**インストールがデフォルトです。 プログラムの削除は、インストールフォルダを削除するだけで十分です。


## 使用のヒント

1. Demixerの使用
   - Facebook ResearchのDemucsモデル（htdemucs、htdemucs_6s、htdemucs_ft、mdx_extra）はすべて良いパフォーマンスを示しています。
   - Demucsは低仕様PC（RAM 8GB）でも非常にうまく動作します。
   - MDX-Netでは、UVR-MDX-NET-Voc_FT、Kim_Vocal_2、UVR_MDXNET_KARA_2などが良いパフォーマンスを示しています。
   - MDX-Netモデルは、高仕様PC（RAM 16GB以上）でのみ動作します。
   - モデルを一つずつ使ってみて、目的に合ったものを探してください。
   - NVIDIA 最新のGPU(6GB以上のVRAM)の使用を推奨します. VRAMが不足すると、Out-Of-Memoryエラーが発生する可能性があります。

2. Whisperの使用
   - Large-V2モデルが最適です。残りは認識率が悪い。
   - オーディオの言語が「韓国語」の場合、Whisperの言語設定も「韓国語」にするのが最善です。
   - オーディオの言語が「韓国語」のとき、Whisperの言語設定を「日本語」にすると「日本語」を出力しますが、精度は低下します。 （むしろグーグル翻訳者は良いです。）
   - **Denoise**オプションを使用すると、MDX-Netモデルを使用してノイズを除去します。音声認識結果が良くなることがあります。 （高仕様PCでのみお使いください）

## 注意事項
Windows Defenderが誤ってバッチファイルをトロイの木馬として認識している場合、これはしばしば「False Positive」と呼ばれます。この問題を解決するには、次の手順を実行できます。

1. ファイル例外処理：Windows Defenderでは、特定のファイルまたはプロセスがセキュリティチェックをスキップするように設定できます。これを行うには、以下の手順に従ってください

   * 「スタート」ボタンをクリックして「設定」に進みます。
   * [アップデートとセキュリティ]をクリックしてください。
   * 「Windowsセキュリティ」を選択し、「ウイルスと脅威の保護」に進みます。
   * [ウイルスと脅威の保護設定の管理]をクリックしてください。
   * 「ウイルスと脅威の保護設定」で「例外を追加」を選択してください。
   * 「ファイルまたはフォルダ」を選択し、問題のバッチファイルを見つけて例外として追加します。
2.  Windows Defender をしばらく無効にする: この方法は一時的な解決策になります。ただし、この方法を使用すると、コンピュータが他の脅威にさらされる可能性があるため、注意が必要です。

3. ワクチンソフトウェアに問題を提起: ファイルがトロイの木馬ではないという確信があれば、マイクロソフトに False Positive として情報を提供できます。マイクロソフトはこれを確認した後、必要な措置を講じます。


## 製品お問い合わせ
* メール: <abus.aikorea@gmail.com>
* ホームページ(韓国語): <https://slashpage.com/abus>
* 네이버 스마트스토어(韓国語): <https://smartstore.naver.com/abus/category/ALL?cp=1>
* Coupang(韓国語): <https://www.coupang.com/vp/products/7875503674>
* Amazon(英語): <https://www.amazon.com/dp/B0CTQQDPXT>
* Amazon(日本語): <https://www.amazon.co.jp/dp/B0CTHT2JH3>


## YouTube
* 商品説明: <https://youtu.be/heEN4UIQLjc>
* 自動字幕・翻訳: <https://youtu.be/uQ14hoEiI4c?si=Io9K_vIDYyeu9Z8_>
* ホームカラオケ: <https://youtube.com/playlist?list=PLwx5dnMDVC9bd6y3wXs-bOas2cXIi-GAq&si=B4S8HJr8gmeAw8hw>


## Credits
* UVR5: <https://github.com/Anjok07/ultimatevocalremovergui>
* FacebookResearch Demucs: <https://github.com/facebookresearch/demucs>
* OpenAI Whisper: <https://github.com/openai/whisper>
* Faster-Whisper: <https://github.com/SYSTRAN/faster-whisper>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>


## 著作権
<img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://slashpage.com/abus)
