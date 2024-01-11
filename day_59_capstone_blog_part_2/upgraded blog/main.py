from flask import Flask, render_template
import requests
import json

data = {}
response = requests.get("https://api.npoint.io/b0148efe999d10d24b3f")
if response.status_code == 200:
    data = json.loads(response.text)
else:
    print(f"Error: {response.status_code}\n{response.text}")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", data=data)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def get_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)