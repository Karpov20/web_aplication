import mysql.connector
# Импортирование глобального объекта
from flask import g


class MySQL:
    '''Класс для работы с базой данных
    __init__(app) - инициализация класса
    config() - генерация конфигурации, необходимой для подключения к базе данных
    connection() - установление соединения с базой данных
    close_connection() - закрытие соединения
    '''
    def __init__(self, app):
        self.app = app
        self.app.teardown_appcontext(self.close_connection)
    
    def config(self):
        return {
            "user": self.app.config['MYSQL_USER'], 
            "password": self.app.config['MYSQL_PASSWORD'],
            "host": self.app.config['MYSQL_HOST'],
            "database": self.app.config['MYSQL_DATABASE']
        }

    def close_connection(self, e=None):
        # g - глобальный объект
        db = g.pop('db', None)

        if db is not None:
            db.close()

    def connection(self):
        # Если соединения нет в глобальном объекте (g)
        if 'db' not in g:
            # Установление соединения
            g.db = mysql.connector.connect(**self.config())
        # Иначе возврат существующего соединения
        return g.db
