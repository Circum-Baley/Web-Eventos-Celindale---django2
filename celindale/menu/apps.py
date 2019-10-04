from django.apps import AppConfig


# Configuramos esta clase para poder tener acceso directo en la plataforma admin
class MenuConfig(AppConfig):
    name = 'menu'
    verbose_name='Menu'
