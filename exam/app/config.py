import os

SECRET_KEY = 'secret'

params = {
    'username': 'std_2065_exam_py',
    'password': '12345678',
    'db_name': 'std_2065_exam_py'
}

# SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://std_1902_exam:12345678@std-mysql.ist.mospolytech.ru/std_1902_exam'

SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{params.get("username")}:{params.get("password")}@std-mysql.ist.mospolytech.ru/{params.get("db_name")}'
#SQLALCHEMY_TRACK_MODIFICATIONS = False
#SQLALCHEMY_ECHO = True

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media', 'images')
