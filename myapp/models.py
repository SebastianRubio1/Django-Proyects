from django.db import models

class project(models.Model):
    '''
    Modelo que representa un proyecto
    '''

    name = models.CharField(max_length=50,help_text='Ingrese el nombre del proyecto.')
    
    def _str_(self):
        return self.name

class Task(models.Model):
    '''
    Modelo que representa una tarea de un proyecto
    '''
    title = models.CharField(max_length=200,help_text='Ingrese el título de la tarea.')
    description=models.TextField(help_text='Ingrese la descripción de la tarea.')
    project=models.ForeignKey(project, on_delete=models.CASCADE)

    def _str_(self) -> str:
        return self.title + ' - ' + str(self.project)
