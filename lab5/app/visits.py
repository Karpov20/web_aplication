
from flask import send_file, render_template, Blueprint, request, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from app import db
from math import ceil
from auth import check_rights
import io
PER_PAGE = 10

bp = Blueprint('visits', __name__, url_prefix='/visits')


# Экспорт данных в CSV
def generate_report_file(records, fields):
    csv_content = '№,' + ','.join(fields) + '\n'
    for i, record in enumerate(records):
        values = [str(getattr(record, f, '')) for f in fields]
        csv_content += f'{i+1},' + ','.join(values) + '\n'
    f = io.BytesIO()
    f.write(csv_content.encode('utf-8'))
    f.seek(0)
    return f


@bp.route('/')
@login_required
def logging():
    page = request.args.get('page', 1, type=int)
    # Запрос для любого пользователя
    query = ('SELECT visit_logs.*, CONCAT_WS(" ",users.last_name, users.first_name, users.middle_name) as FIO '
             'FROM users RIGHT JOIN visit_logs ON visit_logs.user_id = users.id WHERE users.id = %(user_id)s '
             'ORDER BY created_at DESC LIMIT %(per_page)s OFFSET %(param_offset)s')
    params = {
        'per_page': PER_PAGE,
        'param_offset': (page-1)*PER_PAGE,
        'user_id': current_user.id,
    }
    # Запрос для тех, кто может читать все логи (например, администратор)
    if current_user.can('read_full_logs', current_user):
        query = ('SELECT visit_logs.*, CONCAT_WS(" ",users.last_name, users.first_name, users.middle_name) as FIO '
                 'FROM users RIGHT JOIN visit_logs ON visit_logs.user_id = users.id '
                 'ORDER BY created_at DESC LIMIT %(per_page)s OFFSET %(param_offset)s')
        del params['user_id']

    with db.connection().cursor(named_tuple=True) as cursor:
        cursor.execute(query, (params))
        print(params)
        logs = cursor.fetchall()

    with db.connection().cursor(named_tuple=True) as cursor:
        if current_user.can('read_full_logs', current_user):
            query_count_page = 'SELECT COUNT(*) AS count FROM visit_logs'
            cursor.execute(query_count_page)
        else:
            # Для пользователя должно учитываться только его количество записей
            query_count_page = 'SELECT COUNT(*) AS count FROM visit_logs WHERE visit_logs.user_id = %s'
            cursor.execute(query_count_page, (current_user.id,))
        count = cursor.fetchone().count

    last_page = ceil(count/PER_PAGE)

    return render_template('visits/logs.html', logs=logs, last_page=last_page, current_page=page)


@bp.route('/stats/pages')
@login_required
@check_rights('read_full_logs')
def pages_stat():
    query = ('SELECT visit_logs.path, COUNT(*) AS count FROM visit_logs GROUP BY visit_logs.path ORDER BY count DESC;')
    with db.connection().cursor(named_tuple=True) as cursor:
        cursor.execute(query)
        logs = cursor.fetchall()
    if request.args.get('download_csv'):
        f = generate_report_file(logs, ['path', 'count'])
        return send_file(f, mimetype='text/csv', as_attachment=True, download_name='pages_stat.csv')
    return render_template('visits/pages_stat.html', logs=logs)


@bp.route('/stats/users')
@login_required
@check_rights('read_full_logs')
def users_stat():
    query = ('SELECT CONCAT_WS(" ", users.last_name, users.first_name, users.middle_name) as FIO, COUNT(*) AS count '
            'FROM users RIGHT JOIN visit_logs ON visit_logs.user_id = users.id '
            'GROUP BY visit_logs.user_id '
            'ORDER BY count DESC;')
    with db.connection().cursor(named_tuple=True) as cursor:
        cursor.execute(query)
        logs = cursor.fetchall()
    if request.args.get('download_csv'):
        f = generate_report_file(logs, ['FIO', 'count'])
        return send_file(f, mimetype='text/csv', as_attachment=True, download_name='users_stat.csv')
    return render_template('visits/users_stat.html', logs=logs)


