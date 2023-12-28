from flask import render_template, Blueprint, request
from myblogposts.models import BlogPost
core = Blueprint("core",__name__)

@core.route("/")
def home():
    page = request.args.get('page',1,type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    return render_template("home.html", blog_post=blog_posts)

@core.route("/info")
def about():
    return render_template("about.html")