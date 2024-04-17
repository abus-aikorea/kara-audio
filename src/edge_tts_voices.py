import iso639
from src.iso_country_codes import *

import structlog
logger = structlog.get_logger()



# 'af-ZA-AdriNeural' : LangCode - CountryCode - Character 

class MS_Voice():
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        
    def __str__(self):
        return f'MS_Voice(name={self.name}, gender={self.gender})'
    
    def getDisplayName(self):
        return f'{self.getCharacterName()},{self.gender}'
    
    def getLanguageCode(self):
        words = self.name.split('-')
        code = words[0]
        return code
    
    def getLanguageName(self):
        try:
            code = self.getLanguageCode()
            if len(code) == 2:
                lang = iso639.Language.from_part1(code)
            elif len(code) == 3:
                lang = iso639.Language.from_part2b(code)
            return lang.name
        except iso639.LanguageNotFoundError:
            return 'English'

    def getCountryCode(self):
        words = self.name.split('-')
        code = words[1]
        return code
    
    def getCountryName(self):
        country = CC[self.getCountryCode()]
        return country
    
    def getCharacterName(self):
        words = self.name.split('-')
        code = words[2]
        name = code.replace('Neural', '')
        return name
            


class MS_VoiceManager():
    def __init__(self) -> None:
        self.selectedLanguageName: str = ''
        pass
    
    def get_all_language_names(self):
        unique_languages = list(set(voice.getLanguageName() for voice in MS_VOICES))
        sorted_languages = sorted(unique_languages)
        return sorted_languages
    
    def select_language(self, languageName: str):
        self.selectedLanguageName = languageName
        
    # def get_all_voices(self, languageName: str) -> list:
    #     if languageName == '':
    #         return []
        
    #     lang = iso639.Language.from_name(languageName)
    #     logger.debug(f'get_all_voices: lang={lang}')        
    #     voices = [voice for voice in MS_VOICES if voice.getLanguageCode() == lang.part1]
    #     return voices        
        
    
    def get_language_voices(self, languageName: str) -> list:
        if languageName is None or len(languageName) <= 0:
            return [] 
        
        lang = iso639.Language.from_name(languageName)
        voices = [voice for voice in MS_VOICES if voice.getLanguageCode() == lang.part1]
        return voices
    
    def get_voice(self, displayName: str) -> MS_Voice:
        words = displayName.split(',')
        name = words[0]
        gender = words[1]
        for voice in MS_VOICES:
            if voice.gender == gender and name in voice.name:
                return voice
            
        return MS_VOICES[0]


                
    
MS_VOICES = [
    MS_Voice('af-ZA-AdriNeural', 'Female'),
    MS_Voice('af-ZA-WillemNeural', 'Male'),
    MS_Voice('af-ZA-AdriNeural', 'Female'),
    MS_Voice('af-ZA-WillemNeural', 'Male'),
    MS_Voice('am-ET-AmehaNeural', 'Male'),
    MS_Voice('am-ET-MekdesNeural', 'Female'),
    MS_Voice('ar-AE-FatimaNeural', 'Female'),
    MS_Voice('ar-AE-HamdanNeural', 'Male'),
    MS_Voice('ar-BH-AliNeural', 'Male'),
    MS_Voice('ar-BH-LailaNeural', 'Female'),
    MS_Voice('ar-DZ-AminaNeural', 'Female'),
    MS_Voice('ar-DZ-IsmaelNeural', 'Male'),
    MS_Voice('ar-EG-SalmaNeural', 'Female'),
    MS_Voice('ar-EG-ShakirNeural', 'Male'),
    MS_Voice('ar-IQ-BasselNeural', 'Male'),
    MS_Voice('ar-IQ-RanaNeural', 'Female'),
    MS_Voice('ar-JO-SanaNeural', 'Female'),
    MS_Voice('ar-JO-TaimNeural', 'Male'),
    MS_Voice('ar-KW-FahedNeural', 'Male'),
    MS_Voice('ar-KW-NouraNeural', 'Female'),
    MS_Voice('ar-LB-LaylaNeural', 'Female'),
    MS_Voice('ar-LB-RamiNeural', 'Male'),
    MS_Voice('ar-LY-ImanNeural', 'Female'),
    MS_Voice('ar-LY-OmarNeural', 'Male'),
    MS_Voice('ar-MA-JamalNeural', 'Male'),
    MS_Voice('ar-MA-MounaNeural', 'Female'),
    MS_Voice('ar-OM-AbdullahNeural', 'Male'),
    MS_Voice('ar-OM-AyshaNeural', 'Female'),
    MS_Voice('ar-QA-AmalNeural', 'Female'),
    MS_Voice('ar-QA-MoazNeural', 'Male'),
    MS_Voice('ar-SA-HamedNeural', 'Male'),
    MS_Voice('ar-SA-ZariyahNeural', 'Female'),
    MS_Voice('ar-SY-AmanyNeural', 'Female'),
    MS_Voice('ar-SY-LaithNeural', 'Male'),
    MS_Voice('ar-TN-HediNeural', 'Male'),
    MS_Voice('ar-TN-ReemNeural', 'Female'),
    MS_Voice('ar-YE-MaryamNeural', 'Female'),
    MS_Voice('ar-YE-SalehNeural', 'Male'),
    MS_Voice('az-AZ-BabekNeural', 'Male'),
    MS_Voice('az-AZ-BanuNeural', 'Female'),
    MS_Voice('bg-BG-BorislavNeural', 'Male'),
    MS_Voice('bg-BG-KalinaNeural', 'Female'),
    MS_Voice('bn-BD-NabanitaNeural', 'Female'),
    MS_Voice('bn-BD-PradeepNeural', 'Male'),
    MS_Voice('bn-IN-BashkarNeural', 'Male'),
    MS_Voice('bn-IN-TanishaaNeural', 'Female'),
    MS_Voice('bs-BA-GoranNeural', 'Male'),
    MS_Voice('bs-BA-VesnaNeural', 'Female'),
    MS_Voice('ca-ES-EnricNeural', 'Male'),
    MS_Voice('ca-ES-JoanaNeural', 'Female'),
    MS_Voice('cs-CZ-AntoninNeural', 'Male'),
    MS_Voice('cs-CZ-VlastaNeural', 'Female'),
    MS_Voice('cy-GB-AledNeural', 'Male'),
    MS_Voice('cy-GB-NiaNeural', 'Female'),
    MS_Voice('da-DK-ChristelNeural', 'Female'),
    MS_Voice('da-DK-JeppeNeural', 'Male'),
    MS_Voice('de-AT-IngridNeural', 'Female'),
    MS_Voice('de-AT-JonasNeural', 'Male'),
    MS_Voice('de-CH-JanNeural', 'Male'),
    MS_Voice('de-CH-LeniNeural', 'Female'),
    MS_Voice('de-DE-AmalaNeural', 'Female'),
    MS_Voice('de-DE-ConradNeural', 'Male'),
    MS_Voice('de-DE-FlorianMultilingualNeural', 'Male'),
    MS_Voice('de-DE-KatjaNeural', 'Female'),
    MS_Voice('de-DE-KillianNeural', 'Male'),
    MS_Voice('de-DE-SeraphinaMultilingualNeural', 'Female'),
    MS_Voice('el-GR-AthinaNeural', 'Female'),
    MS_Voice('el-GR-NestorasNeural', 'Male'),
    MS_Voice('en-AU-NatashaNeural', 'Female'),
    MS_Voice('en-AU-WilliamNeural', 'Male'),
    MS_Voice('en-CA-ClaraNeural', 'Female'),
    MS_Voice('en-CA-LiamNeural', 'Male'),
    MS_Voice('en-GB-LibbyNeural', 'Female'),
    MS_Voice('en-GB-MaisieNeural', 'Female'),
    MS_Voice('en-GB-RyanNeural', 'Male'),
    MS_Voice('en-GB-SoniaNeural', 'Female'),
    MS_Voice('en-GB-ThomasNeural', 'Male'),
    MS_Voice('en-HK-SamNeural', 'Male'),
    MS_Voice('en-HK-YanNeural', 'Female'),
    MS_Voice('en-IE-ConnorNeural', 'Male'),
    MS_Voice('en-IE-EmilyNeural', 'Female'),
    MS_Voice('en-IN-NeerjaExpressiveNeural', 'Female'),
    MS_Voice('en-IN-NeerjaNeural', 'Female'),
    MS_Voice('en-IN-PrabhatNeural', 'Male'),
    MS_Voice('en-KE-AsiliaNeural', 'Female'),
    MS_Voice('en-KE-ChilembaNeural', 'Male'),
    MS_Voice('en-NG-AbeoNeural', 'Male'),
    MS_Voice('en-NG-EzinneNeural', 'Female'),
    MS_Voice('en-NZ-MitchellNeural', 'Male'),
    MS_Voice('en-NZ-MollyNeural', 'Female'),
    MS_Voice('en-PH-JamesNeural', 'Male'),
    MS_Voice('en-PH-RosaNeural', 'Female'),
    MS_Voice('en-SG-LunaNeural', 'Female'),
    MS_Voice('en-SG-WayneNeural', 'Male'),
    MS_Voice('en-TZ-ElimuNeural', 'Male'),
    MS_Voice('en-TZ-ImaniNeural', 'Female'),
    MS_Voice('en-US-AnaNeural', 'Female'),
    MS_Voice('en-US-AndrewMultilingualNeural', 'Male'),
    MS_Voice('en-US-AndrewNeural', 'Male'),
    MS_Voice('en-US-AriaNeural', 'Female'),
    MS_Voice('en-US-AvaMultilingualNeural', 'Female'),
    MS_Voice('en-US-AvaNeural', 'Female'),
    MS_Voice('en-US-BrianMultilingualNeural', 'Male'),
    MS_Voice('en-US-BrianNeural', 'Male'),
    MS_Voice('en-US-ChristopherNeural', 'Male'),
    MS_Voice('en-US-EmmaMultilingualNeural', 'Female'),
    MS_Voice('en-US-EmmaNeural', 'Female'),
    MS_Voice('en-US-EricNeural', 'Male'),
    MS_Voice('en-US-GuyNeural', 'Male'),
    MS_Voice('en-US-JennyNeural', 'Female'),
    MS_Voice('en-US-MichelleNeural', 'Female'),
    MS_Voice('en-US-RogerNeural', 'Male'),
    MS_Voice('en-US-SteffanNeural', 'Male'),
    MS_Voice('en-ZA-LeahNeural', 'Female'),
    MS_Voice('en-ZA-LukeNeural', 'Male'),
    MS_Voice('es-AR-ElenaNeural', 'Female'),
    MS_Voice('es-AR-TomasNeural', 'Male'),
    MS_Voice('es-BO-MarceloNeural', 'Male'),
    MS_Voice('es-BO-SofiaNeural', 'Female'),
    MS_Voice('es-CL-CatalinaNeural', 'Female'),
    MS_Voice('es-CL-LorenzoNeural', 'Male'),
    MS_Voice('es-CO-GonzaloNeural', 'Male'),
    MS_Voice('es-CO-SalomeNeural', 'Female'),
    MS_Voice('es-CR-JuanNeural', 'Male'),
    MS_Voice('es-CR-MariaNeural', 'Female'),
    MS_Voice('es-CU-BelkysNeural', 'Female'),
    MS_Voice('es-CU-ManuelNeural', 'Male'),
    MS_Voice('es-DO-EmilioNeural', 'Male'),
    MS_Voice('es-DO-RamonaNeural', 'Female'),
    MS_Voice('es-EC-AndreaNeural', 'Female'),
    MS_Voice('es-EC-LuisNeural', 'Male'),
    MS_Voice('es-ES-AlvaroNeural', 'Male'),
    MS_Voice('es-ES-ElviraNeural', 'Female'),
    MS_Voice('es-ES-XimenaNeural', 'Female'),
    MS_Voice('es-GQ-JavierNeural', 'Male'),
    MS_Voice('es-GQ-TeresaNeural', 'Female'),
    MS_Voice('es-GT-AndresNeural', 'Male'),
    MS_Voice('es-GT-MartaNeural', 'Female'),
    MS_Voice('es-HN-CarlosNeural', 'Male'),
    MS_Voice('es-HN-KarlaNeural', 'Female'),
    MS_Voice('es-MX-DaliaNeural', 'Female'),
    MS_Voice('es-MX-JorgeNeural', 'Male'),
    MS_Voice('es-NI-FedericoNeural', 'Male'),
    MS_Voice('es-NI-YolandaNeural', 'Female'),
    MS_Voice('es-PA-MargaritaNeural', 'Female'),
    MS_Voice('es-PA-RobertoNeural', 'Male'),
    MS_Voice('es-PE-AlexNeural', 'Male'),
    MS_Voice('es-PE-CamilaNeural', 'Female'),
    MS_Voice('es-PR-KarinaNeural', 'Female'),
    MS_Voice('es-PR-VictorNeural', 'Male'),
    MS_Voice('es-PY-MarioNeural', 'Male'),
    MS_Voice('es-PY-TaniaNeural', 'Female'),
    MS_Voice('es-SV-LorenaNeural', 'Female'),
    MS_Voice('es-SV-RodrigoNeural', 'Male'),
    MS_Voice('es-US-AlonsoNeural', 'Male'),
    MS_Voice('es-US-PalomaNeural', 'Female'),
    MS_Voice('es-UY-MateoNeural', 'Male'),
    MS_Voice('es-UY-ValentinaNeural', 'Female'),
    MS_Voice('es-VE-PaolaNeural', 'Female'),
    MS_Voice('es-VE-SebastianNeural', 'Male'),
    MS_Voice('et-EE-AnuNeural', 'Female'),
    MS_Voice('et-EE-KertNeural', 'Male'),
    MS_Voice('fa-IR-DilaraNeural', 'Female'),
    MS_Voice('fa-IR-FaridNeural', 'Male'),
    MS_Voice('fi-FI-HarriNeural', 'Male'),
    MS_Voice('fi-FI-NooraNeural', 'Female'),
    MS_Voice('fil-PH-AngeloNeural', 'Male'),
    MS_Voice('fil-PH-BlessicaNeural', 'Female'),
    MS_Voice('fr-BE-CharlineNeural', 'Female'),
    MS_Voice('fr-BE-GerardNeural', 'Male'),
    MS_Voice('fr-CA-AntoineNeural', 'Male'),
    MS_Voice('fr-CA-JeanNeural', 'Male'),
    MS_Voice('fr-CA-SylvieNeural', 'Female'),
    MS_Voice('fr-CA-ThierryNeural', 'Male'),
    MS_Voice('fr-CH-ArianeNeural', 'Female'),
    MS_Voice('fr-CH-FabriceNeural', 'Male'),
    MS_Voice('fr-FR-DeniseNeural', 'Female'),
    MS_Voice('fr-FR-EloiseNeural', 'Female'),
    MS_Voice('fr-FR-HenriNeural', 'Male'),
    MS_Voice('fr-FR-RemyMultilingualNeural', 'Male'),
    MS_Voice('fr-FR-VivienneMultilingualNeural', 'Female'),
    MS_Voice('ga-IE-ColmNeural', 'Male'),
    MS_Voice('ga-IE-OrlaNeural', 'Female'),
    MS_Voice('gl-ES-RoiNeural', 'Male'),
    MS_Voice('gl-ES-SabelaNeural', 'Female'),
    MS_Voice('gu-IN-DhwaniNeural', 'Female'),
    MS_Voice('gu-IN-NiranjanNeural', 'Male'),
    MS_Voice('he-IL-AvriNeural', 'Male'),
    MS_Voice('he-IL-HilaNeural', 'Female'),
    MS_Voice('hi-IN-MadhurNeural', 'Male'),
    MS_Voice('hi-IN-SwaraNeural', 'Female'),
    MS_Voice('hr-HR-GabrijelaNeural', 'Female'),
    MS_Voice('hr-HR-SreckoNeural', 'Male'),
    MS_Voice('hu-HU-NoemiNeural', 'Female'),
    MS_Voice('hu-HU-TamasNeural', 'Male'),
    MS_Voice('id-ID-ArdiNeural', 'Male'),
    MS_Voice('id-ID-GadisNeural', 'Female'),
    MS_Voice('is-IS-GudrunNeural', 'Female'),
    MS_Voice('is-IS-GunnarNeural', 'Male'),
    MS_Voice('it-IT-DiegoNeural', 'Male'),
    MS_Voice('it-IT-ElsaNeural', 'Female'),
    MS_Voice('it-IT-GiuseppeNeural', 'Male'),
    MS_Voice('it-IT-IsabellaNeural', 'Female'),
    MS_Voice('ja-JP-KeitaNeural', 'Male'),
    MS_Voice('ja-JP-NanamiNeural', 'Female'),
    MS_Voice('jv-ID-DimasNeural', 'Male'),
    MS_Voice('jv-ID-SitiNeural', 'Female'),
    MS_Voice('ka-GE-EkaNeural', 'Female'),
    MS_Voice('ka-GE-GiorgiNeural', 'Male'),
    MS_Voice('kk-KZ-AigulNeural', 'Female'),
    MS_Voice('kk-KZ-DauletNeural', 'Male'),
    MS_Voice('km-KH-PisethNeural', 'Male'),
    MS_Voice('km-KH-SreymomNeural', 'Female'),
    MS_Voice('kn-IN-GaganNeural', 'Male'),
    MS_Voice('kn-IN-SapnaNeural', 'Female'),
    MS_Voice('ko-KR-HyunsuNeural', 'Male'),
    MS_Voice('ko-KR-InJoonNeural', 'Male'),
    MS_Voice('ko-KR-SunHiNeural', 'Female'),
    MS_Voice('lo-LA-ChanthavongNeural', 'Male'),
    MS_Voice('lo-LA-KeomanyNeural', 'Female'),
    MS_Voice('lt-LT-LeonasNeural', 'Male'),
    MS_Voice('lt-LT-OnaNeural', 'Female'),
    MS_Voice('lv-LV-EveritaNeural', 'Female'),
    MS_Voice('lv-LV-NilsNeural', 'Male'),
    MS_Voice('mk-MK-AleksandarNeural', 'Male'),
    MS_Voice('mk-MK-MarijaNeural', 'Female'),
    MS_Voice('ml-IN-MidhunNeural', 'Male'),
    MS_Voice('ml-IN-SobhanaNeural', 'Female'),
    MS_Voice('mn-MN-BataaNeural', 'Male'),
    MS_Voice('mn-MN-YesuiNeural', 'Female'),
    MS_Voice('mr-IN-AarohiNeural', 'Female'),
    MS_Voice('mr-IN-ManoharNeural', 'Male'),
    MS_Voice('ms-MY-OsmanNeural', 'Male'),
    MS_Voice('ms-MY-YasminNeural', 'Female'),
    MS_Voice('mt-MT-GraceNeural', 'Female'),
    MS_Voice('mt-MT-JosephNeural', 'Male'),
    MS_Voice('my-MM-NilarNeural', 'Female'),
    MS_Voice('my-MM-ThihaNeural', 'Male'),
    MS_Voice('nb-NO-FinnNeural', 'Male'),
    MS_Voice('nb-NO-PernilleNeural', 'Female'),
    MS_Voice('ne-NP-HemkalaNeural', 'Female'),
    MS_Voice('ne-NP-SagarNeural', 'Male'),
    MS_Voice('nl-BE-ArnaudNeural', 'Male'),
    MS_Voice('nl-BE-DenaNeural', 'Female'),
    MS_Voice('nl-NL-ColetteNeural', 'Female'),
    MS_Voice('nl-NL-FennaNeural', 'Female'),
    MS_Voice('nl-NL-MaartenNeural', 'Male'),
    MS_Voice('pl-PL-MarekNeural', 'Male'),
    MS_Voice('pl-PL-ZofiaNeural', 'Female'),
    MS_Voice('ps-AF-GulNawazNeural', 'Male'),
    MS_Voice('ps-AF-LatifaNeural', 'Female'),
    MS_Voice('pt-BR-AntonioNeural', 'Male'),
    MS_Voice('pt-BR-FranciscaNeural', 'Female'),
    MS_Voice('pt-BR-ThalitaNeural', 'Female'),
    MS_Voice('pt-PT-DuarteNeural', 'Male'),
    MS_Voice('pt-PT-RaquelNeural', 'Female'),
    MS_Voice('ro-RO-AlinaNeural', 'Female'),
    MS_Voice('ro-RO-EmilNeural', 'Male'),
    MS_Voice('ru-RU-DmitryNeural', 'Male'),
    MS_Voice('ru-RU-SvetlanaNeural', 'Female'),
    MS_Voice('si-LK-SameeraNeural', 'Male'),
    MS_Voice('si-LK-ThiliniNeural', 'Female'),
    MS_Voice('sk-SK-LukasNeural', 'Male'),
    MS_Voice('sk-SK-ViktoriaNeural', 'Female'),
    MS_Voice('sl-SI-PetraNeural', 'Female'),
    MS_Voice('sl-SI-RokNeural', 'Male'),
    MS_Voice('so-SO-MuuseNeural', 'Male'),
    MS_Voice('so-SO-UbaxNeural', 'Female'),
    MS_Voice('sq-AL-AnilaNeural', 'Female'),
    MS_Voice('sq-AL-IlirNeural', 'Male'),
    MS_Voice('sr-RS-NicholasNeural', 'Male'),
    MS_Voice('sr-RS-SophieNeural', 'Female'),
    MS_Voice('su-ID-JajangNeural', 'Male'),
    MS_Voice('su-ID-TutiNeural', 'Female'),
    MS_Voice('sv-SE-MattiasNeural', 'Male'),
    MS_Voice('sv-SE-SofieNeural', 'Female'),
    MS_Voice('sw-KE-RafikiNeural', 'Male'),
    MS_Voice('sw-KE-ZuriNeural', 'Female'),
    MS_Voice('sw-TZ-DaudiNeural', 'Male'),
    MS_Voice('sw-TZ-RehemaNeural', 'Female'),
    MS_Voice('ta-IN-PallaviNeural', 'Female'),
    MS_Voice('ta-IN-ValluvarNeural', 'Male'),
    MS_Voice('ta-LK-KumarNeural', 'Male'),
    MS_Voice('ta-LK-SaranyaNeural', 'Female'),
    MS_Voice('ta-MY-KaniNeural', 'Female'),
    MS_Voice('ta-MY-SuryaNeural', 'Male'),
    MS_Voice('ta-SG-AnbuNeural', 'Male'),
    MS_Voice('ta-SG-VenbaNeural', 'Female'),
    MS_Voice('te-IN-MohanNeural', 'Male'),
    MS_Voice('te-IN-ShrutiNeural', 'Female'),
    MS_Voice('th-TH-NiwatNeural', 'Male'),
    MS_Voice('th-TH-PremwadeeNeural', 'Female'),
    MS_Voice('tr-TR-AhmetNeural', 'Male'),
    MS_Voice('tr-TR-EmelNeural', 'Female'),
    MS_Voice('uk-UA-OstapNeural', 'Male'),
    MS_Voice('uk-UA-PolinaNeural', 'Female'),
    MS_Voice('ur-IN-GulNeural', 'Female'),
    MS_Voice('ur-IN-SalmanNeural', 'Male'),
    MS_Voice('ur-PK-AsadNeural', 'Male'),
    MS_Voice('ur-PK-UzmaNeural', 'Female'),
    MS_Voice('uz-UZ-MadinaNeural', 'Female'),
    MS_Voice('uz-UZ-SardorNeural', 'Male'),
    MS_Voice('vi-VN-HoaiMyNeural', 'Female'),
    MS_Voice('vi-VN-NamMinhNeural', 'Male'),
    MS_Voice('zh-CN-XiaoxiaoNeural', 'Female'),
    MS_Voice('zh-CN-XiaoyiNeural', 'Female'),
    MS_Voice('zh-CN-YunjianNeural', 'Male'),
    MS_Voice('zh-CN-YunxiNeural', 'Male'),
    MS_Voice('zh-CN-YunxiaNeural', 'Male'),
    MS_Voice('zh-CN-YunyangNeural', 'Male'),
    MS_Voice('zh-CN-liaoning-XiaobeiNeural', 'Female'),
    MS_Voice('zh-CN-shaanxi-XiaoniNeural', 'Female'),
    MS_Voice('zh-HK-HiuGaaiNeural', 'Female'),
    MS_Voice('zh-HK-HiuMaanNeural', 'Female'),
    MS_Voice('zh-HK-WanLungNeural', 'Male'),
    MS_Voice('zh-TW-HsiaoChenNeural', 'Female'),
    MS_Voice('zh-TW-HsiaoYuNeural', 'Female'),
    MS_Voice('zh-TW-YunJheNeural', 'Male'),
    MS_Voice('zu-ZA-ThandoNeural', 'Female'),
    MS_Voice('zu-ZA-ThembaNeural', 'Male')        
]



    