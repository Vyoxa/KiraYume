# Copyright (C) 2024 Yousef A. (Vyoxa).
# Licensed under the GPL-3.0 License.
# Created for KiraYume: https://github.com/Vyoxa/KiraYume

from PyQt6.QtCore import Qt

PROGRAM_VERSION = '0.6.76'

ITEM_PATH_ROLE = Qt.ItemDataRole.UserRole + 1  # Role to store the item path of a model item
TRANSLATED_ITEM_PATH_ROLE = Qt.ItemDataRole.UserRole + 2  # Role to store the translated item path of a model item

COLOR_FOLDER = 'e8bf4d'  # Golden Yellow
COLOR_INFO = '1aafd0'  # Sky Blue
COLOR_SUCCESS = '3be8b0'  # Turquoise
COLOR_ERROR = 'fc636b'  # Coral Red
COLOR_DEFAULT_TEXT = 'dcddde'  # Light Gray

RATIO_MODES = {'Maintain Aspect Ratio, Expand to Fit': 'Qt.AspectRatioMode.KeepAspectRatioByExpanding', 'Maintain Aspect Ratio': 'Qt.AspectRatioMode.KeepAspectRatio', 'Ignore Aspect Ratio, Resize to Fit': 'Qt.AspectRatioMode.IgnoreAspectRatio'}

LANGUAGES_FROM = [
    'Auto', "English", "Arabic", "Croatian", "Filipino", "French", "German",
    "Hebrew", "Hindi", "Indonesian", "Italian", "Japanese", "Korean", "Russian", "Spanish", "Thai"
]

LANGUAGES_TO = [
    "English", "Arabic", "Croatian", "Filipino", "French", "German",
    "Hebrew", "Hindi", "Indonesian", "Italian", "Japanese", "Korean", "Russian", "Spanish", "Thai"
]

LANGUAGE_CODES = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
                  'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu',
                  'belarusian': 'be', 'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs',
                  'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny',
                  'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co',
                  'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi',
                  'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee',
                  'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl',
                  'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn', 'gujarati': 'gu',
                  'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi',
                  'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo',
                  'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw',
                  'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom',
                  'korean': 'ko', 'krio': 'kri', 'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb',
                  'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lingala': 'ln',
                  'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk',
                  'maithili': 'mai', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt',
                  'maori': 'mi', 'marathi': 'mr', 'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus',
                  'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no',
                  'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl',
                  'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru',
                  'samoan': 'sm', 'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr',
                  'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk',
                  'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw',
                  'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te',
                  'thai': 'th', 'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk',
                  'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz',
                  'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo',
                  'zulu': 'zu'}

DEEPL_LANGUAGES = [
    "auto", "ar", "bg", "zh", "cs", "da", "nl", "en", "et", "fi",
    "fr", "de", "el", "hu", "id", "it", "ja", "ko", "lv", "lt", "nb", "pl",
    "pt", "ro", "ru", "sk", "sl", "es", "sv", "tr", "uk"]

SCANNER_BUTTON_OFF_STYLE_SHEET = """
QPushButton {
	color: #d7d7d7;
    background-color: qlineargradient(spread:reflect, x1:0, y1:0.420318, x2:0.955224, y2:0.966, stop:0.25 #101f32, stop:1 #148fa3);
    border: 1px solid rgba(0, 0, 0, 0);
    padding: 6px 2px;
    text-align: center;
    text-decoration: none;
    font-size: 15px;
    font-weight: bold;
    border-radius: 14px;
    border-width: 2px;
}

QPushButton:hover {    
	background-color: qlineargradient(spread:reflect, x1:0, y1:0.420318, x2:0.955224, y2:0.966, stop:0.1 #101f32, stop:1 #148fa3);
}

QPushButton:pressed {
	background-color: #148fa3;
}

QPushButton:disabled {
	color: #91abb9;
}

"""

SCANNER_BUTTON_ON_STYLE_SHEET = """
    QPushButton {
	    color: #d7d7d7;
        background-color: qlineargradient(spread:reflect, x1:0, y1:0.420318, x2:0.955224, y2:0.966, stop:0.25 #148fa3, stop:1 #101f32);
        border: 1px solid #101f32;
        padding: 6px 2px;
        text-align: center;
        text-decoration: none;
        font-size: 15px;
        font-weight: bold;
        border-radius: 6px;
        border-width: 2px;
}

    QPushButton:hover {    
	    background-color: qlineargradient(spread:reflect, x1:0, y1:0.420318, x2:0.955224, y2:0.966, stop:0.1 #148fa3, stop:1 #101f32);
}

    QPushButton:pressed {
	    background-color: #148fa3;
}

QPushButton:disabled {
	color: #91abb9;
}
"""

ERASER_BUTTON_OFF_STYLE_SHEET = """
QPushButton {
	color: #d7d7d7;
    background-color: qlineargradient(spread:reflect, x1:0, y1:0.466, x2:1, y2:0.801136, stop:0 #b0454b, stop:0.8 #101f32);
    border: 1px solid rgba(0, 0, 0, 0);
    padding: 6px 2px;
    text-align: center;
    text-decoration: none;
    font-size: 15px;
    font-weight: bold;
    border-radius: 14px;
    border-width: 2px;
}

QPushButton:hover {
    background-color: qlineargradient(spread:reflect, x1:0, y1:0.466, x2:1, y2:0.801136, stop:0 #b0454b, stop:1 #101f32);
}

QPushButton:pressed {
    background-color: #b0454b;
}

QPushButton:disabled {
	color: #c38e91;
}
"""

ERASER_BUTTON_ON_STYLE_SHEET = """
QPushButton {
	color: #d7d7d7;
    background-color: qlineargradient(spread:reflect, x1:0, y1:0.466, x2:1, y2:0.801136, stop:0 #101f32, stop:0.8 #b0454b);
    border: 1px solid #101f32;
    padding: 6px 2px;
    text-align: center;
    text-decoration: none;
    font-size: 15px;
    font-weight: bold;
    border-radius: 6px;
    border-width: 2px;
}

QPushButton:hover {
    background-color: qlineargradient(spread:reflect, x1:0, y1:0.466, x2:1, y2:0.801136, stop:0 #101f32, stop:1 #b0454b);
}

QPushButton:pressed {
    background-color: #b0454b;
}

QPushButton:disabled {
	color: #c38e91;
}
"""

TESSERACT_CONNECTED_STYLE_SHEET = """
QLabel {
	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0.149254 rgba(16, 31, 50, 206), stop:0.328358 rgba(16, 31, 50, 80), stop:0.442786 rgba(16, 31, 50, 80), stop:0.572139 rgba(20, 132, 132, 80), stop:0.686567 rgba(20, 132, 132, 250), stop:1 rgba(255, 255, 255, 0));
	border-radius: 20px;
	margin-top: 10px;
	margin-right: 10px;
}
"""
# QLabel {
# 	border: 6px solid #13a29a;
# 	border-radius: 20px;
# 	margin-top: 10px;
# 	margin-right: 10px;
# }

TESSERACT_DISCONNECTED_STYLE_SHEET = """
QLabel {
	background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(16, 31, 50, 255), stop:0.0995025 rgba(16, 31, 50, 255), stop:0.2 rgba(16, 31, 50, 167), stop:0.3 rgba(16, 31, 50, 92), stop:0.4 rgba(176, 69, 75, 51), stop:0.5 rgba(176, 69, 75, 205), stop:0.58209 rgba(255, 76, 76, 205), stop:0.671642 rgba(176, 69, 75, 84), stop:1 rgba(255, 255, 255, 0));
	border-radius: 20px;
	margin-top: 10px;
	margin-right: 10px;
}
"""
