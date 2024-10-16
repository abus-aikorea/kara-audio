# Kara-Audio: The best Whisper Web UI for subtitle production.

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [中文简体](README.zh.md) ∙ [中文繁體](README.tw.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/kara-audio)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases)

**Kara-Audio는 자막 제작을 위한 최고의 Whisper Web UI입니다.** 원클릭으로 쉽게 설치할 수 있습니다. Miniconda를 사용하여 가상 환경을 만들고, Windows 시스템과 완전히 독립적으로 실행됩니다 (fully portable).

- **YouTube 다운로더**: YouTube 비디오를 다운로드하고 오디오(mp3, wav, flac)를 추출할 수 있습니다.
- **보컬 제거**: UVR5에서 지원되는 MDX-Net과 Meta에서 개발한 Demucs 엔진을 사용하여 음성을 분리합니다.
- **STT**: Whisper, Faster-Whisper 및 whisper-timestamped를 사용한 음성-텍스트 변환을 지원합니다.
- more...

Kara-Audio는 YouTube 비디오를 당신만의 노래방 뮤비로 만들어 줍니다. 
영화, 드라마, 뉴스의 녹취록, 회의록, 자막을 생성할 수 있습니다.


### 🚄 실행 화면

https://github.com/abus-aikorea/kara-audio/assets/161691694/d085cebf-a1b9-4428-a7f3-a43610a5ab87



## ⭐ 주요 기능

* `Kara Audio` 탭
  - YouTube 다운로더, 보컬 분리, 자동자막을 통합환경으로 제공
  
<p align="center">
  <img style="width: 90%; height: 90%" src="images/main_page.kor.png?raw=true" alt=""/>
</p>  


* `Demixing` 탭
  - 보컬 분리, Reverb/Echo 제거
  - MDX-Net, Demucs 모델 지원
  - 오디오 포맷(wav, flac, mp3) 선택가능


* `자막` 탭
  - 음성인식, 자동자막 제작(srt, vtt, txt)
  - 90여 언어 지원 (English, Japanese, French, German, Chinese, 한국어)


## 💻 Execution environment
* OS : Windows 10/11 (64bits) **※ Linux, Mac OS는 지원하지 않습니다.**
* GPU: CUDA 12.1을 지원하는 **NVIDIA** 그래픽 카드 권장. 
* VRAM: 4GB 이상. 8GB이상 권장.
* RAM: 4GB 이상
* HDD: 설치 중 최소 20GB의 여유 공간
* 인터넷 연결 필요(설치 및 번역 작업)

## 📀 설치 와 실행

Kara-Audio는 one click으로 손쉽게 설치 가능합니다. 🚀**configure.bat** 와 🚀**start.bat** 을 실행하기만 하면 됩니다.

### step 1. 패키지 준비
* A. 유료버전
    + USB에 포함된 압축파일(**kara-audio-x.zip**)을 컴퓨터의 적당한 위치에 압축해제
    + 혹은, 이미 압축이 해제된 폴더(**kara-audio-x**)를 컴퓨터의 적당한 위치에 복사
* B. 무료버전
  + Clone or download the latest release (**Source code (zip)**) from  [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/)

### step 2. 프로그램 설치 및 실행
1. 🚀 `configure.bat` 실행
   - Windows에 ffmpeg, git 과 CUDA(NVIDIA GPU를 사용하는 경우)를 설치합니다. 
   - 최초 1회만 실행하면 됩니다.
   - 인터넷 연결을 필요로하며, 시스템에 따라 설치에 1시간 이상 소요될 수 있음.
   - 설치 중에는 절대 Windows-Command 창을 종료하지 마세요.
2. 🚀 `start.bat` 실행
   - Kara-Audio 를 시작합니다. Web-UI가 자동으로 실행됩니다. 
   - 최초 실행시에는 Kara-Audio 설치 작업을 먼저 진행합니다. 
   - Kara-Audio 설치는 인터넷 연결을 필요로 하며, 시스템에 따라 설치에 1시간 이상이 소요될 수 있습니다. 
   - 설치 중에는 절대 Windows-Command 창을 종료하지 마세요.
   - 설치중 문제가 발생한 경우, installer_files 폴더를 삭제하고 start.bat를 다시 실행하세요.


### step 3. 프로그램 제거
* `uninstall.bat` 실행: 
  - installer_files 폴더를 제거합니다. 
  - Windows 에 설치한 ffmepg, CUDA 패키지를 제거합니다(선택할 경우)
* Kara-Audio는 **포터블** 설치가 기본입니다. 프로그램의 제거는 설치 폴더를 삭제하는 것으로 충분합니다.



## ❓사용팁

#### Browser가 자동으로 실행되지 않는 경우
- Windows-Commnad 창을 종료하고, start.bat 을 다시 실행하거나
- Browser를 직접 실행하고, Windows-Command 창에 표시된 주소(예, **http://127.0.0.1:7892** )를 주소창에 입력합니다.

#### CUDA Out-Of-Memory 오류가 발생하는 경우
- 윈도우 작업관리자 - 성능 탭에서 GPU 메모리 상태를 확인하세요. 
- Denoise 레벨을 0 또는 1 로 설정하세요. Denoise 레벨 2 는 8GB 이상의 GPU 메모리를 필요로 합니다.
- Compute Type 을 int 타입으로 설정하세요. float 타입의 품질이 더 좋지만 더 많은 GPU 메모리를 요구합니다.

#### 자막의 품질을 높이려면?
- 자막의 품질은 더 큰 Whisper 모델을 사용할 수록 좋아지는 경향은 있지만, 꼭 그런것은 아닙니다. large >  medium > small > base > tiny 
- Compute Type 중에서는 float 타입의 성능이 좋습니다. int 타입은 모델 양자화를 통해 GPU사용량을 낮추고 속도를 높인 모델입니다. 반면, 성능은 떨어집니다. 
- Denoise 레벨을 높이면 배경음을 더 많이 제거하고, 남아있는 보이스만 음성인식에 사용하게 됩니다. 항상 좋은 결과를 보장하지는 않습니다.

#### Demixer 사용
- Facebook Research 의 Demucs 모델(htdemucs, htdemucs_6s, htdemucs_ft, mdx_extra)들은 모두 좋은 성능을 보여줍니다. 
- Demucs 는 저사양 PC (RAM 8GB)에서도 그럭저럭 잘 동작합니다.
- MDX-Net에서는 UVR-MDX-NET-Voc_FT, Kim_Vocal_2, UVR_MDXNET_KARA_2 등이 좋은 성능을 보여줍니다.
- MDX-Net 모델은 고사양 PC (RAM 16GB 이상)에서만 동작합니다.
- 모델들을 하나씩 사용해 보고, 목적에 맞는 것을 찾으시길 바랍니다.
- NVIDIA 최신 GPU (VRAM 6GB 이상) 사용을 권장합니다. VRAM 부족시 Out-Of-Memory 에러가 발생할 수 있습니다.

#### Whisper 사용
- Large-V2 모델이 가장 좋습니다. 나머지는 인식률이 나쁩니다.
- 오디오의 언어가 '한국어'인 경우, Whisper 언어 설정도 '한국어'로 하는 것이 가장 좋습니다.
- 오디오의 언어가 '한국어'일 때, Whisper 언어 설정을 '일본어'로 하면 '일본어' 를 출력하긴 합니다만, 정확도는 떨어집니다. (차라리 구글 번역기가 낫습니다.)
- **Denoise** 옵션을 사용하면 MDX-Net 모델을 이용하여 노이즈를 제거합니다. 음성 인식 결과가 좋아 질 수 있습니다. (고사양 PC에서만 사용하세요)



## 📢 주의사항

Windows Defender가 신뢰할 수 없는 애플리케이션에 대한 경고를 표시하고 Kara-Audio의 추가 실행을 허용하지 않을 수 있습니다.
SmartScreen 보안 수준이 "경고"로 설정되어 있다면 "More info"를 클릭한 후 "어쨌든 실행"을 클릭하세요.
SmartScreen이 "차단" 수준으로 설정되어 있으면 설치를 실행할 수 있는 버튼이 없습니다. 이 경우, start.bat 파일의 속성을 열고 "차단 해제"를 체크한 후 변경 사항을 적용하고 다시 start.bat 파일을 실행하세요.

<p align="center">
  <img style="width: 60%; height: 60%" src="images/windows_smartscreen_warning.png?raw=true" alt=""/>
</p>  


Windows Defender가 실수로 batch 파일을 트로이 목마로 인식하는 경우, 이는 종종 'False Positive'라고 불립니다. 이런 문제를 해결하기 위해서는 다음과 같은 과정을 거칠 수 있습니다.

1. 파일 예외 처리: Windows Defender에서 특정 파일이나 프로세스가 보안 검사를 건너뛰도록 설정할 수 있습니다. 이를 위해 아래의 단계를 따르세요.
   * '시작' 버튼을 클릭하고 '설정'으로 이동하세요.
   * '업데이트 및 보안'을 클릭하세요.
   * 'Windows 보안'을 선택하고 '바이러스 및 위협 보호'로 이동하세요.
   * '바이러스 및 위협 보호 설정 관리'를 클릭하세요.
   * '바이러스 및 위협 보호 설정'에서 '예외 추가'를 선택하세요.
   * '파일 또는 폴더'를 선택하고, 문제의 batch 파일을 찾아 예외로 추가하세요.
2. Windows Defender를 잠시 비활성화: 이 방법은 임시적인 해결책이 될 수 있습니다. 하지만 이 방법을 사용할 경우, 컴퓨터가 다른 위협에 노출될 수 있으므로 주의가 필요합니다.
3. 백신 소프트웨어에 문제 제보: 만약 파일이 트로이 목마가 아니라는 확신이 있다면, Microsoft에 False Positive로 제보할 수 있습니다. Microsoft는 이를 검토한 후 필요한 조치를 취할 것입니다.



## 📬 제품 문의
* e-mail: <abus.aikorea@gmail.com>
* homepage(Korean): <https://abuskorea.imweb.me>
* Amazon(USA): <https://www.amazon.com/dp/B0CTQQDPXT>
* Amazon(Japan): <https://www.amazon.co.jp/dp/B0CTHT2JH3>
* Amazon(Singapore): <https://www.amazon.sg/dp/B0DCGKMMG3>
* Amazon(UAE): <https://www.amazon.ae/dp/B0DCGQ1FGC>
* 네이버 스마트스토어(korean): <https://smartstore.naver.com/abus/category/ALL?cp=1>


## 👍 YouTube
* 제품 설명: <https://youtube.com/playlist?list=PLwx5dnMDVC9Y7dAjm9r26CZUw1uU5VIeq&si=873MgzUtu4POE9jO>
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


## ©️ 저작권 정보
  <img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://abuskorea.imweb.me)

