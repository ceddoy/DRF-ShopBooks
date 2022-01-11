from django.db import models

from djangoRF.models import TrackableUpdateCreateModel
from djangoRF.settings import BASE_URL
from userapp.models import User


class Project(TrackableUpdateCreateModel):
    name = models.CharField(max_length=128, verbose_name='Название проекта')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец проекта')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{BASE_URL}/project/{self.id}/'


class WorkGroup(TrackableUpdateCreateModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    user = models.ManyToManyField(User, verbose_name='Рабочая группа')

    class Meta:
        verbose_name = 'Рабочая группа'
        verbose_name_plural = 'Рабочие группы'

    def __str__(self):
        return self.project.name


class ToDo(TrackableUpdateCreateModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    title = models.CharField(max_length=128, verbose_name='Заголовок заметки')
    description = models.TextField(verbose_name='Описание заметки')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор заметки')
    is_activ = models.BooleanField(default=True, verbose_name='Активная заметка')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.title
