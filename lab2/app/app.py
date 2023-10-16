from flask import Flask, render_template, url_for, request, make_response, redirect
import re


app = Flask(__name__)
application = app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/args')
def args():
    return render_template('args.html')


@app.route('/headers')
def headers():
    return render_template('headers.html')


@app.route('/cookies', methods=['GET', 'POST'])
def cookies():
    n_resp = make_response(render_template('cookies.html'))
    if request.method == 'POST':
        n_resp.set_cookie(request.form.get('key'),
                          request.form.get('value'))
    return n_resp


@app.route('/cookies/clear', methods=['GET', 'POST'])
def clear():
    n_resp = make_response(render_template('cookies.html'))
    for cookie in iter(request.cookies):
        print(cookie)
        n_resp.set_cookie(cookie, expires=0)
    return n_resp


# Создаем маршрут '/tel_check', который обрабатывает GET и POST запросы
@app.route('/tel_check', methods=['GET', 'POST'])
def tel_check():
    # Если метод запроса равен 'POST', то обрабатываем данные формы
    if request.method == 'POST':
        # Получаем значение поля 'tel' из формы запроса
        tel = request.form.get('tel')
        # Проверяем, что номер телефона содержит только цифры и несколько разделительных символов (пробелы, скобки, дефисы, точки и знак плюса)
        if not re.search(r'[^\d\s\(\)\-\.\+]', tel):
            # Удаляем все символы из номера, кроме цифр
            d_tel = list(filter(lambda num: num.isdigit(), tel))
            # Если в номере осталось ровно 10 цифр, то добавляем цифру '8' в начало номера и разбиваем его на блоки по 3 цифры
            if len(d_tel) == 10:
                d_tel.insert(0, '8')
            # Если в номере осталось 11 цифр, то заменяем первую цифру на '8' и разбиваем номер на блоки по 3 цифры
            elif len(d_tel) == 11:
                d_tel[0] = '8'
            # Если в номере недостаточно или слишком много цифр, то генерируем сообщение об ошибке
            else:
                tel_error = "Недопустимый ввод. Неверное количество цифр."
                return render_template('tel_check.html', tel=tel, tel_error=tel_error)
            # Соединяем цифры обратно в строку и разбиваем номер на блоки по 3 цифры с помощью дефисов
            tel = ''.join(d_tel)
            tel = f"8-{tel[1:4]}-{tel[4:7]}-{tel[7:9]}-{tel[9:]}"
        # Если в номере телефона содержатся недопустимые символы, то генерируем сообщение об ошибке
        else:
            tel_error = "Недопустимый ввод. В номере телефона встречаются недопустимые символы."
            return render_template('tel_check.html', tel=tel, tel_error=tel_error)
        # Возвращаем страницу 'tel_check.html' с отформатированным номером телефона
        return render_template('tel_check.html', tel=tel)
    # Возвращаем страницу 'tel_check.html' для GET-запросов
    return render_template('tel_check.html')