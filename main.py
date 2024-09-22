from flask import Flask, render_template
# from api import get_juz, jprint
from db import get_verses_by_surah_num, get_verses_by_juz_num, get_verses_by_hizb_num, get_verses_by_page_num

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

"""
    category_num: int
        this is the number that the respective category is
        example: if the catergory_num is 1, it is about the first juz

    category: str
        this is the category that the number is about
        example: if the category is "juz", then the category_num is about the juz

    @reason
        this data is sent to the html file to display the respective category
        example: if the category is "juz" and the category_num is 1, then the first juz will be displayed
"""    
#! juz, hizb and page columns dont exist in the database
@app.route("/juz/<int:juz_num>")
def juz(juz_num):
    return render_template("categories/juz.html", category_num=juz_num, category="juz", verses = get_verses_by_juz_num(juz_num))


@app.route("/surah/<int:surah_num>")
def surah(surah_num):
    return render_template("categories/surah.html", category_num=surah_num, category="surah", verses = get_verses_by_surah_num(surah_num))


@app.route("/hizb/<int:hizb_num>")
def hizb(hizb_num):
    return render_template("categories/hizb.html", category_num=hizb_num, category="hizb", verses = get_verses_by_hizb_num(hizb_num))


@app.route("/page/<int:page_num>")
def page(page_num):
    return render_template("categories/page.html", category_num=page_num, category="page", verses = get_verses_by_page_num(page_num))


if __name__ == "__main__":
    app.run(debug=True)
