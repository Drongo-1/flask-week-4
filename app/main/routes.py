from flask import render_template, request, Blueprint
from app.models import Post
import random

main = Blueprint("main",__name__)


@main.route('/')
@main.route("/home")
def home():
    posts = Post.query.all()
    return render_template("index.html", posts=posts, title="Home page")
    return quote()


@main.route("/about")
def about():
    return render_template("about.html", name="namess")

@main.route("/")
def quote():
    dict1 = {1: {'author':'Ngugidavid', 'title':'authords'},
            2: {'author':'Ngugidavid2', 'title':'authords2'}}
    res=key, val=random.choice(list(dict1.items()))
    author=str(val['author'])
    title1=str(val['title'])
    return render_template("index.html", author="author", title1=title1)
    