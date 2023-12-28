'''Blog site using Flask'''
from flask import Flask, render_template
import requests
from post import Post

# aggregate blog post objects into list
post_objects = []
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
all_posts_data = response.json()
for post in all_posts_data:
    post_object = Post(post["id"], post["title"],
                       post["subtitle"], post["body"])
    post_objects.append(post_object)

# flask framework
app = Flask(__name__)

@app.route('/')
def posts_preview():
    return render_template("index.html", posts=post_objects)

@app.route('/post/<int:post_id>')
def get_post(post_id):
    post_to_display = None
    for object in post_objects:
        if object.id == post_id:
            post_to_display = object
    return render_template("post.html", post=post_to_display)

if __name__ == "__main__":
    app.run(debug=True)
