from django.contrib import admin
from .models import project,Task 

'''
Se importa project y task de models
'''

admin.site.register(project)
admin.site.register(Task)
'''
Se registran, en la pagina admin aún pedira user y contraseña por lo tanto se tendran que crear
'''