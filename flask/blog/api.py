from flask import Blueprint, render_template, request, redirect, url_for

from blog.db import PostDB

blog_router = Blueprint('blog', __name__)
db = PostDB()

@blog_router.route('/')
def index():
    return render_template('index.html')

@blog_router.route('/posts')
def get_posts():
    posts = db.get_all()
    return render_template('posts.html', posts=posts)

@blog_router.route('/posts/<int:id_>')
def get_post(id_):
    post = db.get_one(id_)
    return render_template('post.html', post=post)

@blog_router.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if request.method =='GET':
        return render_template('post_form.html')
    title = request.form.get('title')
    text = request.form.get('text')

    new_post = db.create(title, text)
    return redirect(url_for('blog.get_post', id_=new_post['id']))


@blog_router.route('/update_post/<int:id_>', methods=['GET', 'POST'])
def update_post(id_):
    if request.method =='GET':
        post = db.get_one(id_)
        return render_template('post_form.html', post=post)
    title = request.form.get('title')
    text = request.form.get('text')

    new_post = db.update(id_,title, text)
    return redirect(url_for('blog.get_post', id_=new_post['id']))

@blog_router.route('/delete_post/<int:id_>', methods=['GET', 'POST'])
def delete_post(id_):
  db.delete(id_)
  return redirect(url_for("blog.get_posts"))
