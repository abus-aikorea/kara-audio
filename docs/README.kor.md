# Kara-Audio

🌍 [한국어](README.kor.md) ∙ [English](README.eng.md) ∙ [日本語](README.jpn.md)

[![GitHub License](https://img.shields.io/github/license/abus-aikorea/kara-audio)](LICENSE)
[![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases)

The best gradio web-ui for vocal remover that uses demucs and mdx-net. 
Automatic subtitle creation using faster whisper. Easy one click installation. Fully portable.


### 실행 화면

https://github.com/abus-aikorea/kara-audio/assets/161691694/d085cebf-a1b9-4428-a7f3-a43610a5ab87



## 소개
Kara-Audio는 AI Studio의 새이름입니다. from 2024-04-10 

* Kara-Audio는 유튜브 동영상을 당신만의 **노래방 뮤비**로 만들어 드립니다.
* **녹취록**, **회의록**은 물론, 영화, 드라마, 뉴스의 **자막**을 만들수 있습니다.
* UVR5에서 제공하는 **보컬 리무버**와 OpenAI Whisper를 이용한 **자동자막** 기능을 탑재하고 있습니다. 
* Kara-Audio는 **원클릭**으로 손쉽게 설치할 수 있으며, Gradio Web-UI 를 제공합니다. 


## 주요 기능

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




## 특징
* YouTube 동영상(mp4, webm)을 다운로드하고, 오디오 파일(mp3, wav, flac)로 저장할 수 있습니다.
* 보컬 리무버를 제공합니다. **MDX-Net** 과 **Demucs**를 이용합니다.
* AI 음성인식을 통한 자동 자막생성이 가능합니다. OpenAI의 고성능 음성인식 엔진, **Whisper**를 이용합니다.
* Whisper는 일본어, 한국어, 영어, 중국어, 프랑스어, 스페인어 등 90개 이상의 언어를 지원합니다.
* **원클릭 설치**. 한 번 설치하면 추가 비용 없이 **영구적**으로 사용할 수 있습니다. ( ※ Free버전은 이용시간 **30분제한** 있음)
* **Web-UI**를 제공합니다. Google Chrome 브라우저를 권장합니다.



## 실행 환경
* OS : Windows 10/11 (64bits) **※ Linux, Mac OS는 지원하지 않습니다.**
* CPU: Intel 프로세서 2GHz 이상(또는 동급 호환)
* RAM: 16GB 이상
* HDD: 설치 중 최소 20GB의 여유 공간
* GPU: CUDA 12.3을 지원하는 **NVIDIA** 그래픽 카드 권장. VRAM 6GB 이상.
* 인터넷 연결 필요(설치시)


## 설치 와 실행

### step 1. 패키지 준비
* A. 유료버전
    + USB에 포함된 압축파일(**kara-audio-x.zip**)을 컴퓨터의 적당한 위치에 압축해제
    + 혹은, 이미 압축이 해제된 폴더(**kara-audio-x**)를 컴퓨터의 적당한 위치에 복사

* B. 무료버전
  + [![GitHub Release](https://img.shields.io/github/v/release/abus-aikorea/kara-audio)](https://github.com/abus-aikorea/kara-audio/releases) 로부터 최신 릴리즈 (**Source code (zip)**) 다운로드 후 압축 해제 
  + 혹은, git clone 으로 소스코드 다운로드
    
```bash
git clone https://github.com/abus-aikorea/kara-audio.git
```

### step 2. 프로그램 설치 및 실행

0. 설치전
   - Windows Update 를 실행하여 시스템을 최신 상태로 업데이트 합니다.
   - NVIDIA Graphic Driver 를 최신 상태로 업데이트 합니다.


1. `configure.bat` 실행
   - Windows에 ffmpeg 과 CUDA(NVIDIA GPU를 사용하는 경우) 및 Windows SDK를 설치합니다. 
   - 설치를 위해서는 인터넷에 연결되어 있어야 하고, 컴퓨터 사양에 따라 1시간 이상 소요될 수 있습니다.
   - 설치 중에는 절대 Windows-Command 창을 종료하지 마세요. (작업이 멈춘것 처럼 보인다면 스페이스바를 가끔씩 눌러보세요)
   - 설치중 오류가 발생한 경우, uninstall.bat를 실행한 후 처음부터 다시 시작하는 것을 권장합니다.
   - configure.bat 는 최초 1회만 실행하면 됩니다.


2. `start.bat` 실행
   - Kara-Audio 를 시작합니다. Web-UI가 자동으로 실행됩니다. 
   - 최초 실행시에는 Kara-Audio 설치 작업을 먼저 진행합니다. 
   - 설치를 위해서는 인터넷에 연결되어 있어야 하고, 시스템에 따라 1시간 이상 소요될 수 있습니다. 
   - 설치 중에는 절대 Windows-Command 창을 종료하지 마세요. (작업이 멈춘것 처럼 보인다면 스페이스바를 가끔씩 눌러보세요)
   - 설치중 오류가 발생한 경우, installer_files 폴더를 삭제하고 start.bat를 다시 실행하세요.

#### Browser가 자동으로 실행되지 않는 경우
- Windows-Commnad 창을 종료하고, start.bat 을 다시 실행하거나
- Browser를 직접 실행하고, Windows-Command 창에 표시된 주소(예, **http://127.0.0.1:7894** )를 주소창에 입력합니다.


### step 3. 프로그램 제거
* `uninstall.bat` 실행: 
  - installer_files 폴더를 제거합니다. 
  - Windows 에 설치한 ffmepg, CUDA 패키지, Windows SDK를 제거합니다(선택할 경우)

* Kara-Audio는 **포터블** 설치가 기본입니다. 프로그램의 제거는 설치 폴더를 삭제하는 것으로 충분합니다.


## 이용팁

1. Demixer 사용
   - Facebook Research 의 Demucs 모델(htdemucs, htdemucs_6s, htdemucs_ft, mdx_extra)들은 모두 좋은 성능을 보여줍니다. 
   - Demucs 는 저사양 PC (RAM 8GB)에서도 그럭저럭 잘 동작합니다.
   - MDX-Net에서는 UVR-MDX-NET-Voc_FT, Kim_Vocal_2, UVR_MDXNET_KARA_2 등이 좋은 성능을 보여줍니다.
   - MDX-Net 모델은 고사양 PC (RAM 16GB 이상)에서만 동작합니다.
   - 모델들을 하나씩 사용해 보고, 목적에 맞는 것을 찾으시길 바랍니다.
   - NVIDIA 최신 GPU (VRAM 6GB 이상) 사용을 권장합니다. VRAM 부족시 Out-Of-Memory 에러가 발생할 수 있습니다.
2. Whisper 사용
   - Large-V2 모델이 가장 좋습니다. 나머지는 인식률이 나쁩니다.
   - 오디오의 언어가 '한국어'인 경우, Whisper 언어 설정도 '한국어'로 하는 것이 가장 좋습니다.
   - 오디오의 언어가 '한국어'일 때, Whisper 언어 설정을 '일본어'로 하면 '일본어' 를 출력하긴 합니다만, 정확도는 떨어집니다. (차라리 구글 번역기가 낫습니다.)
   - **Denoise** 옵션을 사용하면 MDX-Net 모델을 이용하여 노이즈를 제거합니다. 음성 인식 결과가 좋아 질 수 있습니다. (고사양 PC에서만 사용하세요)


## 주의사항
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


## 제품 문의
* 이메일 문의: <abus.aikorea@gmail.com>
* 홈페이지: <https://slashpage.com/abus>
* 네이버 스마트스토어: <https://smartstore.naver.com/abus/category/ALL?cp=1>
* 쿠팡: <https://www.coupang.com/vp/products/7875503674>
* 아마존(미국): <https://www.amazon.com/dp/B0CTQQDPXT>
* 아마존(일본): <https://www.amazon.co.jp/dp/B0CTHT2JH3>


## YouTube
* 제품 설명: <https://youtu.be/heEN4UIQLjc>
* 자동 자막∙번역: <https://youtu.be/uQ14hoEiI4c?si=Io9K_vIDYyeu9Z8_>
* 홈 가라오케: <https://youtube.com/playlist?list=PLwx5dnMDVC9Z8kB01tQKfzTysaCCxC3C8&si=v_GLA6Edwj_AWgHg>
  

## Credits
* UVR5: <https://github.com/Anjok07/ultimatevocalremovergui>
* FacebookResearch Demucs: <https://github.com/facebookresearch/demucs>
* OpenAI Whisper: <https://github.com/openai/whisper>
* Faster-Whisper: <https://github.com/SYSTRAN/faster-whisper>
* yt-dlp: <https://github.com/yt-dlp/yt-dlp>
* gradio: <https://github.com/gradio-app/gradio>


## 저작권 정보
<img src="images/ABUS-logo.jpg" width="100" height="100"> by [ABUS](https://slashpage.com/abus)
