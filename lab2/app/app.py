from flask import Flask, render_template, request
from flask import make_response
# Подключение модуля для проверки номера телефона
from modules.check_phone_number import check_number

app = Flask(__name__)
# Fixing 503 error для хостинга Московского Политеха
application = app


'''
Значение request определяется текущим контекстом запроса,
для каждого потока он свой, можем получить доступ к данным,
которые доступны в запросе.
Обратиться к объекту request можно только контексте запроса
В шаблоне доступен по умолчанию (его не нужно передавать)
'''


@app.route('/')
def index():
    '''Функция-обработчик для главной страницы'''
    return render_template('index.html')


@app.route('/headers')
def headers():
    '''Функция-обработчик для страницы "заголовки запроса"'''
    return render_template('headers.html')


@app.route('/args')
def args():
    '''Функция-обработчик для страницы "Параметры URL"'''
    return render_template('args.html')


'''
Кроме тела ответа может передаваться служебная информация с помощью cookies

Чтобы сделать новое значение cookies - у ответа есть заголовки в которых
можно что-то передать. Чтобы установить свой заголовок нужен объект
ответа. Чтобы его получить используем make_response и затем
вместо render_template возвращаем make_response

cookies - словарь
Путь по умолчанию проставляется для всего домена.
Чтобы задать конкретный путь используется path.
Чтобы cookies не были доступны для скрипта, используется httponly
(доступ только у сервера)
Чтобы установить будет ли доступен cookie, через защищенное
соединение или нет используется secure
Отправление cookies, если запрос был с другого домена
определяется samesite.
Чтобы определить для какого поддомена будут доступны cookies
используется domain.
'''


@app.route('/cookies')
def cookies():
    '''Функция-обработчик для страницы "Cookie"'''

    # Создается тело ответа
    resp = make_response(render_template('cookies.html'))
    # Если в запросе есть cookie с именем name
    if "name" in request.cookies:
        # Удаление cookie
        resp.delete_cookie("name")
    else:
        # Добавление cookie
        resp.set_cookie("name", "value")
    return resp


'''
При помощи параметра methods можно добавить методы.
Flask по умолчанию обрабатывает GET запросы.
Свой набор методов передается как список строк.

Запрос GET передает данные в URL в виде пар `ключ=значение`
Запрос POST передает данные в теле запроса.
'''


@app.route('/form', methods=['GET', 'POST'])
def form():
    '''Функция-обработчик для страницы "Параметры формы"'''

    return render_template('form.html')


@app.route('/check-tel-number', methods=['GET', 'POST'])
def check_tel_number():
    '''Функция-обработчик для страницы "Форма с обработкой ошибок"'''

    # Если метод запроса POST
    if request.method == 'POST':
        # Получение номера телефона из формы
        tel = request.form['number']
        # Проверка номера телефона при помощи функции модуля
        result_check = check_number(tel)
        # Если номер прошел проверку
        if (result_check['result']):
            # Возвращается шаблон с результатом number
            return render_template('check-tel-number.html',
                            number=result_check['message'])
        else:
            # Если ошибка описана, то возвращается шаблон с типом ошибки
            if result_check['message']:
                return render_template('check-tel-number.html',
                                error=result_check['message'])
            # Иначе возвращается шаблон с типом ошибки по умолчанию
            else:
                return render_template('check-tel-number.html', error='Другой тип ошибки')
    # Если метод GET (по умолчанию), то возвращается шаблон без параметров
    return render_template('check-tel-number.html')


@app.route('/calc', methods=['GET', 'POST'])
def calc():
    '''Функция-обработчик для страницы "Калькулятор"'''
    answer = ''
    error_text = ''
    if request.method == 'POST':
        try:
            first_num = int(request.form['firstnumber'])
            second_num = int(request.form['secondnumber'])
        except ValueError:
            error_text = 'Был передан текст. Введите, пожалуйста, число.'
            return render_template('calc.html', answer=answer, error_text=error_text)
        operation = request.form['operation']
        if operation == '+':
            answer = first_num + second_num
        elif operation == '-':
            answer = first_num - second_num
        elif operation == '*':
            answer = first_num * second_num
        elif operation == '/':
            try:
                answer = first_num / second_num
            except ZeroDivisionError:
                error_text = 'На ноль делить нельзя'
    return render_template('calc.html', answer=answer, error_text=error_text)


@app.errorhandler(404)
def page_not_found(error):
    '''Функция-обработчик для страницы "Страница не найдена"'''
    return render_template('page_not_found.html'), 404
