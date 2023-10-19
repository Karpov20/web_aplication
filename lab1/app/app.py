
from random import randint
from flask import Flask, render_template
from faker import Faker

fake = Faker()

app = Flask(__name__)
application = app

images_ids = ['avatar',
              'библиотека',
              'горы',
              'картина',
              'кофейня',
              'ночная москва']
def generate_comments(reply=True):
    comments = []
    if not(reply): 
        max_quantity = randint(0, 3)
    else: 
        max_quantity = randint(1, 4)
    
    for i in range(max_quantity):
        comment = {
            'author': fake.name(),
            'text': fake.text(),
            'date': fake.date_time_between(
                start_date='-2y',
                end_date='now'
            )}
        if reply:
            comment['reply'] = generate_comments(reply=False)
        comments.append(comment)
    comments = sorted(comments, key=lambda comment: comment['date'], reverse=True)
    return comments


def generate_post(index):
    '''Функция для статичной генерации постов
    Возвращает словарь с ключами:
    * title - название поста
    * img_id - изображение поста
    * text - текст поста
    * author - автор поста
    * date - дата публикации поста
    * comments - комментарии к посту
    '''
    return {
        'index': index,
        'title': fake.text(max_nb_chars=15).rstrip('.'),
        'img_id': images_ids[index],
        'text': fake.paragraph(nb_sentences=50),
        'author': fake.name(),
        'date': fake.date_time_between(start_date='-2y', end_date='now'),
        'comments': generate_comments()
    }


posts_list = [generate_post(i) for i in range(5)]
posts_list = sorted(posts_list, key=lambda post: post['date'], reverse=True)


@ app.route('/')
def index():
    return render_template('index.html', msg='qq')



@ app.route('/posts')
def posts():
    return render_template('posts.html', title='Посты', posts_list=posts_list)



@ app.route('/post/<int:post_id>')
def post(post_id):
    for post_item in posts_list:
        if post_item['index'] == post_id:
            desired_post = post_item
            break
    return render_template('post.html', post=desired_post, title=desired_post['title'])



@ app.route('/about')
def about():
    return render_template('about.html', title='Об авторе')