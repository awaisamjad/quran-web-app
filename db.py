import sqlite3
from typing import List

"""
helper functions needed
    get_chapter(id)
    get_chapters([id])

"""
#TODO is check same thread false safe/needed?
db = sqlite3.connect("quran.sqlite", check_same_thread=False)
cursor = db.cursor()

id = db.execute("SELECT id FROM chapters").fetchall()
name_arabic = db.execute("SELECT name_ar FROM chapters").fetchall()
name_english = db.execute("SELECT name_pron_en FROM chapters").fetchall()
city_of_revelation = db.execute("SELECT class FROM chapters").fetchall()
number_of_verses_per_chapter = db.execute("SELECT verses_number FROM chapters").fetchall()
verses = db.execute("SELECT content FROM chapters").fetchall()

# print(verses)

def get_info_by_surah_name(id : int):
    result =  cursor.execute("SELECT * FROM chapters WHERE id = ?", (id,)).fetchone()
    return result

def get_verses_by_surah_num(id : int):
    result =  cursor.execute("SELECT content FROM chapters WHERE id = ?", (id,)).fetchall()
    return result

def get_verses_by_juz_num(id : int):
    result =  cursor.execute("SELECT content FROM chapters WHERE id = ?", (id,)).fetchall()
    return result

def get_verses_by_hizb_num(id : int):
    result =  cursor.execute("SELECT content FROM chapters WHERE id = ?", (id,)).fetchall()
    return result

def get_verses_by_page_num(id : int):
    result =  cursor.execute("SELECT content FROM chapters WHERE id = ?", (id,)).fetchall()
    return result

def get_chapters(ids : List[int]):
    pass