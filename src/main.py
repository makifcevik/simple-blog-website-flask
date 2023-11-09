import requests
from flask import Flask, render_template

BLOG_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)
response = requests.get(BLOG_ENDPOINT)
blogs = response.json()


@app.route('/')
def home():
    return render_template("./index.html", blogs=blogs)


@app.route("/post/blog/<blog_id>")
def get_blog(blog_id):
    return render_template("./post.html", blog=blogs[int(blog_id) - 1])


if __name__ == "__main__":
    app.run(debug=True)
