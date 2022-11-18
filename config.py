'''
Конфинурация приложения
'''

import os

'''
Класс конфигурации приложения
'''

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    host = "127.0.0.1"
    user = "sav"
    password = "kotikiandsobachki"
    db_name = "medical_service"