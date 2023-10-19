
# Подключение библиотеки flask
from flask import Flask, render_template, session, request, redirect, url_for, flash
# Подключение бибилотеки flask_login
from flask_login import LoginManager, current_user, UserMixin, login_user, logout_user, login_required
# Полключение MySQL connector
import mysql.connector
# Подключение модуля для валидации данных
from modules.validation import checkLogin, checkPassword, checkLastName, checkFirstName
from mysql_db import MySQL

# Параметры, которые можно извлекать из формы запроса при создании пользователя
PERMITED_PARAMS = ['login', 'password', 'last_name',
                   'first_name', 'middle_name', 'role_id']
# Параметры, которые можно извлекать из формы запроса при редактировании пользователя
EDIT_PARAMS = ['last_name', 'first_name', 'middle_name', 'role_id']

MESSAGE_CHECK_FIELDS = 'Проверьте, пожалуйста, корректность введенных данных.'

app = Flask(__name__)
application = app

# Импортирование конфигурации из файла config.py
app.config.from_pyfile('config.py')

db = MySQL(app)

# LoginManager - это класс, через который осуществляетяс настройка
# аутентификации
login_manager = LoginManager()
# Передаем менеджеру экземляр Flask (приложение),
# чтобы иметь возможность проверять учетные данные пользователей.
login_manager.init_app(app)
# Если пользователь не вошел в систему, но пытается получиь доступ
# к странице, для которой установлен декоратор login_required,
# то происходит перенаправление на endpoint указанный в login_view
# в случае остутствия login_view приложение вернет 401 ошибку
login_manager.login_view = 'login'
# Login_message и login_message_category используется flash,
# когда пользователь перенаправляется на страницу аутентификации
# Сообщение выводимое пользователю, при попытке доступа к страницам,
# требующим авторизации
login_manager.login_message = 'Для доступа к этой странице нужно авторизироваться.'
# Категория отображаемого сообщения
login_manager.login_message_category = 'warning'


# Требования Flask login к User Class
# is_authenticated - return True, если пользователь аутентифицирован
# is_active - return True, если это активный пользователь.
# помимо того, что он прошел проверку, пользователь также
# активировал свою учетную запись, не был заблокирован и т.д.
# Неактивные пользователи не могут войти в систему.
# is_anonymous - return True, если текущий пользователь
# не аутентифицирован, то есть выполняется анонимный доступ
# get_id() - этот метод возвращает уникальный идентификатор
# пользователя и может исопльзоваться для загрузки пользователя из
# обратного вызова user_loader. Идентифкатор должен иметь тип str

class User(UserMixin):
    '''Класс пользователя с наследованием от UserMixin,
    который предоставляет реализацию определенных методов и свойств.'''

    def __init__(self, user_id, user_login):
        self.id = user_id
        self.login = user_login


# Главная страница
@app.route('/')
def index():
    return render_template('index.html')


# Используя объект request, извлекаем значения переданные в форме
# login и password и проверяем пользователя на существование в "БД"
# login_user(UserClass, remember) - обновляет данные сессии и при
# необходимости запоминает пользователя
# redirect(url) - используется для перенаправления на страницу
# с url, переданным в качестве параметра
@app.route('/login', methods=['GET', 'POST'])
def login():
    '''Функция для аутентификации пользователя'''
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        print(f'При аутентифкации пароль {password}')
        remember = request.form.get('remember_me') == 'on'

        query = 'SELECT * FROM users WHERE login = %s and password_hash = SHA2(%s, 256);'
        user = False  # Заглушка от ошибки доступа к переменной
        with db.connection().cursor(named_tuple=True) as cursor:
            cursor.execute(query, (login, password))
            user = cursor.fetchone()
        # Если пользователь был найден
        if user:
            # Аутентифицируем пользователя
            login_user(User(user.id, user.login), remember=remember)
            # Создание уведомления
            flash('Вы успешно прошли аутентификацию!', 'success')
            # Извлечение параметра next из url
            param_url = request.args.get('next')
            # Перенаправление на страницу, указанную в url или на index
            return redirect(param_url or url_for('index'))
        # Создание уведомления
        flash('Введён неправильный логин или пароль.', 'danger')
    return render_template('login.html')


@app.route('/users')
def users():
    # LEFT JOIN - объединение таблиц по таблице слева.
    # Сохраняются все записи из таблицы слева, даже если
    # у правой таблицы нет нужной записи.
    query = ('SELECT users.*, roles.name AS role_name FROM users '
             'LEFT JOIN roles ON roles.id = users.role_id')
    with db.connection().cursor(named_tuple=True) as cursor:
        cursor.execute(query)
        users_list = cursor.fetchall()

    return render_template('users/index.html', users_list=users_list)


@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    '''Функция для смены пароля текущего пользователя.
    ID текущего пользователя извлекается из данных сессии (session) из current_user.id

    error_list={
        'current_password': set(...),
        'new_password': set(...),
        'new_password2': set(...),
        }'''

    error_list = {}

    if request.method == 'GET':
        return render_template('users/change_password.html', error_list=error_list)

    current_password = request.form.get('oldPassword') or None
    new_password = request.form.get('newPassword') or None
    new_password2 = request.form.get('newPassword2') or None

    # Валидация параметров
    if checkPassword(current_password):
        error_list['current_password'] = checkPassword(current_password)
    if checkPassword(new_password):
        error_list['new_password'] = checkPassword(new_password)
    if checkPassword(new_password2):
        error_list['new_password2'] = checkPassword(new_password2)
    # Если были параметры не валидны, то вывод ошибок пользователю
    if error_list:
        flash('Проверьте введенные данные', 'danger')
        return render_template('users/change_password.html', error_list=error_list)

    with db.connection().cursor(named_tuple=True) as cursor:
        query = 'SELECT password_hash FROM users WHERE id=%s'
        cursor.execute(query, (current_user.id,))
        user = cursor.fetchone()

    with db.connection().cursor(named_tuple=True) as cursor:
        query = 'SELECT SHA2(%s, 256) as current_password;'
        cursor.execute(query, (current_password,))
        calculated_hash = cursor.fetchone().current_password

    if user:
        if user.password_hash == calculated_hash:
            if new_password == new_password2:
                query = (
                    'UPDATE users SET password_hash=SHA2(%(new_password)s, 256) WHERE id=%(id)s;')
                dict_for_query = {
                    'new_password': new_password,
                    'id': current_user.id,
                }
                try:
                    with db.connection().cursor(named_tuple=True) as cursor:
                        cursor.execute(query, dict_for_query)
                        db.connection().commit()
                        flash(
                            'Пароль успешно изменен', 'success')
                        return redirect(url_for('index'))
                except mysql.connector.errors.DatabaseError:
                    db.connection().rollback()
                    flash('Во время обновления пароля произошел сбой', 'danger')
                    return render_template('users/change_password.html', error_list=error_list)
            else:
                flash('Введенные пароли не совпадают', 'danger')
                error_list['new_password2'] = {'Пароли должны совпадать'}
                return render_template('users/change_password.html', error_list=error_list)
        else:
            flash('Текущий пароль не совпадает с паролем введенным в поле "Введите старый пароль"', 'danger')
            return render_template('users/change_password.html', error_list=error_list)
    return render_template('users/change_password.html', error_list=error_list)


# @login_required - декоратор для ограничения доступа для
# неавторизованных пользователей
@app.route('/users/new')
@login_required
def users_new():
    return render_template('users/new.html', roles_list=load_roles(), user={}, error_list={})


def load_roles():
    '''Функция для загрузки существующих ролей из БД.
    Возвращает список кортежей'''
    with db.connection().cursor(named_tuple=True) as cursor:
        query = 'SELECT * FROM roles;'
        cursor.execute(query)
        roles = cursor.fetchall()
    return roles


def extract_params(params_list):
    '''Функция для извлечения параметров из запроса.
    Возвращает словарь значений извлеченных из формы.
    Если значения нет, то ключу проставляется None'''
    params_dict = {}
    for param in params_list:
        # get для избежания ошибки при извлечении параметра
        params_dict[param] = request.form.get(param) or None
    return params_dict


@app.route('/users/create', methods=['POST'])
@login_required
def create_user():
    '''Создание нового пользователя

    error_list={
        'login': set(...),
        'password': set(...),
        'last_name': set(...),
        'first_name': set(...),
        }'''
    error_list = {}

    # Извлечение допустимых параметров
    params = extract_params(PERMITED_PARAMS)
    # Валидация параметров
    if checkLogin(params.get('login')):
        error_list['login'] = checkLogin(params.get('login'))
    if checkPassword(params.get('password')):
        error_list['password'] = checkPassword(params.get('password'))
    if checkLastName(params.get('last_name')):
        error_list['last_name'] = checkPassword(params.get('last_name'))
    if checkFirstName(params.get('first_name')):
        error_list['first_name'] = checkPassword(params.get('first_name'))
    # Если были параметры не валидны, то вывод ошибок пользователю
    if error_list:
        return render_template('users/new.html', user=params, roles_list=load_roles(), error_list=error_list)

    query = ('INSERT INTO users(login, password_hash, last_name, '
             'first_name, middle_name, role_id) '
             'VALUES ( %(login)s, SHA2(%(password)s, 256), '
             '%(last_name)s, %(first_name)s, %(middle_name)s, %(role_id)s);')
    try:
        # Пробуем вставить запись о пользователе в БД
        with db.connection().cursor(named_tuple=True) as cursor:
            # params - словарь значений, извлеченных из формы
            cursor.execute(query, params)
            db.connection().commit()
            flash(
                f"Успешно! Создан пользователь @{params.get('login')}", 'success')
    # Если получена ошибка, то выводим ошибку
    except mysql.connector.errors.DatabaseError as error:
        db.connection().rollback()
        flash(MESSAGE_CHECK_FIELDS, 'danger')

        return render_template('users/new.html', user=params, roles_list=load_roles(), error_list=error_list)

    return redirect(url_for('users'))



@ app.route('/users/<int:user_id>/update', methods=['POST'])
@ login_required
def update_user(user_id):
    params = extract_params(EDIT_PARAMS)
    params['id'] = user_id
    error_list = {}
    # Валидация параметров
    if checkLastName(params.get('last_name')):
        error_list['last_name'] = checkPassword(params.get('last_name'))
    if checkFirstName(params.get('first_name')):
        error_list['first_name'] = checkPassword(params.get('first_name'))
    # Если были параметры не валидны, то вывод ошибок пользователю
    if error_list:
        return render_template('users/edit.html', user=params, roles_list=load_roles(), error_list=error_list)

    query = ('UPDATE users SET last_name=%(last_name)s, first_name=%(first_name)s, '
             'middle_name=%(middle_name)s, role_id=%(role_id)s WHERE id=%(id)s;')
    try:
        with db.connection().cursor(named_tuple=True) as cursor:
            cursor.execute(query, params)
            db.connection().commit()
            flash('Успешно! Данные о пользователе были обновлены', 'success')
    except mysql.connector.errors.DatabaseError:
        db.connection().rollback()
        flash(MESSAGE_CHECK_FIELDS, 'danger')
        return render_template('users/edit.html', user=params, roles_list=load_roles(), error_list=error_list)

    return redirect(url_for('users'))


@ app.route('/users/<int:user_id>/edit')
@ login_required
def edit_user(user_id):
    query = 'SELECT * FROM users WHERE users.id = %s;'
    cursor = db.connection().cursor(named_tuple=True)
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return render_template('users/edit.html', user=user, roles_list=load_roles(), error_list={})


@ app.route('/users/<int:user_id>/delete', methods=['POST'])
@ login_required
def delete_user(user_id):
    query = 'DELETE FROM users WHERE users.id=%s;'
    try:
        cursor = db.connection().cursor(named_tuple=True)
        cursor.execute(query, (user_id,))
        db.connection().commit()
        cursor.close()
        flash('Пользователь успешно удален', 'success')
    except mysql.connector.errors.DatabaseError:
        db.connection().rollback()
        flash('При удалении пользователя возникла ошибка.', 'danger')
    return redirect(url_for('users'))


# Всегда GET запрос
@ app.route('/user/<int:user_id>')
def show_user(user_id):
    '''Отображение информации о всех пользователях'''
    query = ('SELECT users.*, roles.name AS role_name FROM users '
             'LEFT JOIN roles ON roles.id = users.role_id '
             'WHERE users.id = %s;')
    cursor = db.connection().cursor(named_tuple=True)
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close()
    return render_template('users/show.html', user=user)


# Используется для удаления из сессии данных о текущем пользователе
@ app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('index'))


# user_loader - декоратор.
# Внутри объекта login_manager запоминается функция
# Функция позволяет по идентификатору пользователя, который
# хранится в сессии, вернуть объект соответствующий пользователю
# или если такого пользователя нет, то вернуть None
# Функция load_user используется для обработки запроса, в ходе которой
# необходимо проверить наличие пользователя
# При помощи декоратора функция записывается в login_manager и
# вызывается, при получении доступа к current_user

# query - запрос, где вместо %s подставляются значения полученные
# при выполнении запроса (cursor.execute).
# db.connection - вернет объект содинения
# .cursor(named_tuple=True) - создаст курсор,
# который возвращает именованный кортеж
# .execute(query, tuple_of_params) - выполнения запроса с подстановкой
# параметров (с экранированием)
# Результат выполнения запроса будет доступен через cursor
# fetchone() - вернет единственную запись в виде tuple, если результата
# нет вернет None
# fetchall() - вернет все записи запроса в виде списка
# fetchmany(size=1) - определенное количество записей (size)
@ login_manager.user_loader
def load_user(user_id):
    '''Класс для загрузки пользователя для login_manager.
    Если пользователь был найден, то возвращается класс User.
    Иначе возвращается None'''
    query = 'SELECT * FROM users WHERE users.id = %s;'
    cursor = db.connection().cursor(named_tuple=True)
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close()
    # Если пользователь был найден, то возвращается класс Польлзователь
    if user:
        return User(user.id, user.login)
    # Иначе возвращается None
    return None


@app.errorhandler(404)
def page_not_found(error):
    '''Функция-обработчик для страницы "Страница не найдена"'''
    return render_template('errors/page_not_found.html', description=error), 404


@app.errorhandler(405)
def method_not_allowed(error):
    '''Функция-обработчик для страницы "Метод не разрешен"'''
    return render_template('errors/method_not_allowed.html', description=error), 405
