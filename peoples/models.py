from django.db import models


class People(models.Model):
    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    mother = models.ForeignKey('self', on_delete=models.SET_NULL,
                               null=True, blank=True, verbose_name='Мать',
                               related_name='children_mother')
    father = models.ForeignKey('self', on_delete=models.SET_NULL,
                               null=True, blank=True, verbose_name='Отец',
                               related_name='children_father')

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.pk})'
