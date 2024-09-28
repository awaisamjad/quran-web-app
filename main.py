from flask import Flask, render_template
from db import (
    get_verses_by_juz_num,
    get_verses_by_hizb_num,
    get_verses_by_page_num,
    get_surahs,
    get_surah_by_id,
)

app = Flask(__name__)


@app.route("/")
def main():
    surahs = get_surahs()
    # ? Displays the main page with the tabs for juz, surah, page and hizb
    return render_template("main.html", surahs=surahs)


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
def tab_juz(juz_num):
    return render_template(
        "tab_categories/juz.html",
        category_num=juz_num,
        category="juz",
        verses=get_verses_by_juz_num(juz_num),
    )


@app.route("/surah/<int:surah_num>")
def tab_surah(surah_num):
    # return render_template("tab_categories/surah.html", category_num=surah_num, category="surah", verses = get_verses_by_surah_num(surah_num))
    return render_template(
        "tab_categories/surah.html",
        category_num=surah_num,
        category="surah",
        verses=get_surah_by_id(surah_num),
    )


@app.route("/hizb/<int:hizb_num>")
def tab_hizb(hizb_num):
    return render_template(
        "tab_categories/hizb.html",
        category_num=hizb_num,
        category="hizb",
        verses=get_verses_by_hizb_num(hizb_num),
    )


@app.route("/page/<int:page_num>")
def tab_page(page_num):
    return render_template(
        "tab_categories/page.html",
        category_num=page_num,
        category="page",
        verses=get_verses_by_page_num(page_num),
    )


# * Pages
@app.route("/pages/juz.html")
def pages_juz():
    return render_template("pages/juz.html")


@app.route("/pages/surah.html")
def pages_surah():
    return render_template("pages/surah.html")


@app.route("/pages/page.html")
def pages_page():
    return render_template("pages/page.html")


@app.route("/pages/hizb.html")
def pages_hizb():
    return render_template("pages/hizb.html")

# ! In production, the debug mode should be turned off
if __name__ == "__main__":
    app.run()
