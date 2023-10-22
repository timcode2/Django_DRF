from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Course(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название курса')
    image = models.ImageField(upload_to='courses/', verbose_name='превью курса', **NULLABLE)
    description = models.TextField(verbose_name='описание курса')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название урока')
    image = models.ImageField(upload_to='lessons/', verbose_name='Превью курса', **NULLABLE)
    description = models.TextField(verbose_name='описание урока')
    video_link = models.URLField(verbose_name='ссылка на видео')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

