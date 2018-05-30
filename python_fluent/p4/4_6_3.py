# -*- coding:utf-8 -*-
import unicodedata
import string

def shave_marks(txt):
    norm_txt = unicodedata.normalize('NFD', txt) # 使用NFC没有作用？
    shave = ''.join(c for c in norm_txt
                    if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shave)

def shave_mark_latin(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue
        keepers.append(c)
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shave = ''.join(keepers)
    return unicodedata.normalize('NFC', shave)


order = '“Herr Voß: • 1⁄2 cup of OEtkerTM caffè latte • bowl of açaí.”'
print(shave_marks(order))
print(shave_mark_latin(order))
Greek = 'Zέφupoς, Zéfiro'
print(shave_marks(Greek))