#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re
char_mappings = {
    "٥": "5",
    "А": "a",
    "В": "b",
    "Е": "e",
    "Н": "h",
    "Р": "P",
    "С": "C",
    "Т": "T",
    "а": "a",
    "г": "r",
    "е": "e",
    "к": "k",
    "м": "m",
    "о": "o",
    "р": "p",
    "ڈ": "د",
    "ڇ": "چ",
    # Persian numbers (will be raplaced by english one)
    "۰": "0",
    "۱": "1",
    "۲": "2",
    "۳": "3",
    "۴": "4",
    "۵": "5",
    "۶": "6",
    "۷": "7",
    "۸": "8",
    "۹": "9",
    ".": ".",
    # Arabic numbers (will be raplaced by english one)
    "٠": "0",
    "١": "1",
    "٢": "2",
    "٣": "3",
    "٤": "4",
    "٥": "5",
    "٦": "6",
    "٧": "7",
    "٨": "8",
    "٩": "9",
    # Special Arabic Characters (will be replaced by persian one)
    "ك": "ک",
    "ى": "ی",
    "ي": "ی",
    "ؤ": "و",
    "ئ": "ی",
    "إ": "ا",
    "أ": "ا",
    "آ": "ا",
    "ة": "ه",
    "ء": "ی",
    # French alphabet (will be raplaced by english one)
    "à": "a",
    "ä": "a",
    "ç": "c",
    "é": "e",
    "è": "e",
    "ê": "e",
    "ë": "e",
    "î": "i",
    "ï": "i",
    "ô": "o",
    "ù": "u",
    "û": "u",
    "ü": "u",
    # Camma (will be replaced by dots for floating point numbers)
    ",": ".",
    # And (will be replaced by dots for floating point numbers)
    "&": " and ",
    # Vowels (will be removed)
    "ّ": "",  # tashdid
    "َ": "",  # a
    "ِ": "",  # e
    "ُ": "",  # o
    "ـ": "",  # tatvil
    # Spaces
    "‍": "",  # 0x9E -> ZERO WIDTH JOINER
    "‌": " ",  # 0x9D -> ZERO WIDTH NON-JOINER
    # Arabic Presentation Forms-A (will be replaced by persian one)
    "ﭐ": "ا",
    "ﭑ": "ا",
    "ﭖ": "پ",
    "ﭗ": "پ",
    "ﭘ": "پ",
    "ﭙ": "پ",
    "ﭞ": "ت",
    "ﭟ": "ت",
    "ﭠ": "ت",
    "ﭡ": "ت",
    "ﭺ": "چ",
    "ﭻ": "چ",
    "ﭼ": "چ",
    "ﭽ": "چ",
    "ﮊ": "ژ",
    "ﮋ": "ژ",
    "ﮎ": "ک",
    "ﮏ": "ک",
    "ﮐ": "ک",
    "ﮑ": "ک",
    "ﮒ": "گ",
    "ﮓ": "گ",
    "ﮔ": "گ",
    "ﮕ": "گ",
    "ﮤ": "ه",
    "ﮥ": "ه",
    "ﮦ": "ه",
    "ﮪ": "ه",
    "ﮫ": "ه",
    "ﮬ": "ه",
    "ﮭ": "ه",
    "ﮮ": "ی",
    "ﮯ": "ی",
    "ﮰ": "ی",
    "ﮱ": "ی",
    "ﯼ": "ی",
    "ﯽ": "ی",
    "ﯾ": "ی",
    "ﯿ": "ی",
    # Arabic Presentation Forms-B (will be removed)
    "ﹰ": "",
    "ﹱ": "",
    "ﹲ": "",
    "ﹳ": "",
    "ﹴ": "",
    "﹵": "",
    "ﹶ": "",
    "ﹷ": "",
    "ﹸ": "",
    "ﹹ": "",
    "ﹺ": "",
    "ﹻ": "",
    "ﹼ": "",
    "ﹽ": "",
    "ﹾ": "",
    "ﹿ": "",
    # Arabic Presentation Forms-B (will be replaced by persian one)
    "ﺀ": "ی",
    "ﺁ": "ا",
    "ﺂ": "ا",
    "ﺃ": "ا",
    "ﺄ": "ا",
    "ﺅ": "و",
    "ﺆ": "و",
    "ﺇ": "ا",
    "ﺈ": "ا",
    "ﺉ": "ی",
    "ﺊ": "ی",
    "ﺋ": "ی",
    "ﺌ": "ی",
    "ﺍ": "ا",
    "ﺎ": "ا",
    "ﺏ": "ب",
    "ﺐ": "ب",
    "ﺑ": "ب",
    "ﺒ": "ب",
    "ﺓ": "ه",
    "ﺔ": "ه",
    "ﺕ": "ت",
    "ﺖ": "ت",
    "ﺗ": "ت",
    "ﺘ": "ت",
    "ﺙ": "ث",
    "ﺚ": "ث",
    "ﺛ": "ث",
    "ﺜ": "ث",
    "ﺝ": "ج",
    "ﺞ": "ج",
    "ﺟ": "ج",
    "ﺠ": "ج",
    "ﺡ": "ح",
    "ﺢ": "ح",
    "ﺣ": "ح",
    "ﺤ": "ح",
    "ﺥ": "خ",
    "ﺦ": "خ",
    "ﺧ": "خ",
    "ﺨ": "خ",
    "ﺩ": "د",
    "ﺪ": "د",
    "ﺫ": "ذ",
    "ﺬ": "ذ",
    "ﺭ": "ر",
    "ﺮ": "ر",
    "ﺯ": "ز",
    "ﺰ": "ز",
    "ﺱ": "س",
    "ﺲ": "س",
    "ﺳ": "س",
    "ﺴ": "س",
    "ﺵ": "ش",
    "ﺶ": "ش",
    "ﺷ": "ش",
    "ﺸ": "ش",
    "ﺹ": "ص",
    "ﺺ": "ص",
    "ﺻ": "ص",
    "ﺼ": "ص",
    "ﺽ": "ض",
    "ﺾ": "ض",
    "ﺿ": "ض",
    "ﻀ": "ض",
    "ﻁ": "ط",
    "ﻂ": "ط",
    "ﻃ": "ط",
    "ﻄ": "ط",
    "ﻅ": "ظ",
    "ﻆ": "ظ",
    "ﻇ": "ظ",
    "ﻈ": "ظ",
    "ﻉ": "ع",
    "ﻊ": "ع",
    "ﻋ": "ع",
    "ﻌ": "ع",
    "ﻍ": "غ",
    "ﻎ": "غ",
    "ﻏ": "غ",
    "ﻐ": "غ",
    "ﻑ": "ف",
    "ﻒ": "ف",
    "ﻓ": "ف",
    "ﻔ": "ف",
    "ﻕ": "ق",
    "ﻖ": "ق",
    "ﻗ": "ق",
    "ﻘ": "ق",
    "ﻙ": "ک",
    "ﻚ": "ک",
    "ﻛ": "ک",
    "ﻜ": "ک",
    "ﻝ": "ل",
    "ﻞ": "ل",
    "ﻟ": "ل",
    "ﻠ": "ل",
    "ﻡ": "م",
    "ﻢ": "م",
    "ﻣ": "م",
    "ﻤ": "م",
    "ﻥ": "ن",
    "ﻦ": "ن",
    "ﻧ": "ن",
    "ﻨ": "ن",
    "ﻩ": "ه",
    "ﻪ": "ه",
    "ﻫ": "ه",
    "ﻬ": "ه",
    "ﻭ": "و",
    "ﻮ": "و",
    "ﻯ": "ی",
    "ﻰ": "ی",
    "ﻱ": "ی",
    "ﻲ": "ی",
    "ﻳ": "ی",
    "ﻴ": "ی",
    "ﻵ": "لا",
    "ﻶ": "لا",
    "ﻷ": "لا",
    "ﻸ": "لا",
    "ﻹ": "لا",
    "ﻺ": "لا",
    "ﻻ": "لا",
    "ﻼ": "لا",
}

valid_chars = [
    " ",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "ا",
    "ب",
    "ت",
    "ث",
    "ج",
    "ح",
    "خ",
    "د",
    "ذ",
    "ر",
    "ز",
    "س",
    "ش",
    "ص",
    "ض",
    "ط",
    "ظ",
    "ع",
    "غ",
    "ف",
    "ق",
    "ل",
    "م",
    "ن",
    "ه",
    "و",
    "پ",
    "چ",
    "ژ",
    "ک",
    "گ",
    "ی",
]

translation_table = dict((ord(a), b) for a, b in char_mappings.items())

# Create a regex for recognizing invalid characters.
nonvalid_reg_text = ' '.format("".join(valid_chars))
nonvalid_reg = re.compile(nonvalid_reg_text)


def normalize_text(text, to_lower=True, remove_invalid=True):
    # Map invalid characters with replacement to valid characters.
    text = text.translate(translation_table)
    if to_lower:
        text = text.lower()
    if remove_invalid:
        text = nonvalid_reg.sub(' ', text)
    # Replace consecutive whitespaces with a single space character.
#    text = re.sub(r"\s+", " ", text)
    return text

import re
def clean_text2(text):
    pattern5='\.|؟|!|؛'
    pattern8='[،|:|«|»|-|(|)|*|=|"|"|}|{|-|…]+'
    pattern9='[\d]+'
    pattern10='\.'+'\.'+'\.'
    file2='edit_text.txt'
    file3='new_text4.txt'
    
    stripped = re.sub('\u200c', ' ', text)
  
    stripped = re.sub(pattern10, ' ', stripped)
    regex=re.findall(pattern5, stripped)
    for r in regex:
        for d in r:
            stripped=stripped.replace(d," "+d+" ")
    stripped=normalize_text(stripped)
    stripped=re.sub(r'\d+(.*?)(?:\u263a|\U0001f645)', ' ', stripped)
    stripped = re.sub(pattern8, ' ', stripped)
    stripped=re.sub(r" +", " ", stripped)
    stripped=re.sub(r"\t+", " ", stripped)                                            
    sentences2=re.findall(pattern5, stripped)              
    for s in sentences2:
        for m in s:
            stripped=stripped.replace(m,m+"\n")
    lines = stripped.split("\n")

    non_empty_lines = [line for line in lines if line.strip() != ""]


    stripped2= ""

    for line in non_empty_lines:

          stripped2+= line + "\n"
    return stripped2

