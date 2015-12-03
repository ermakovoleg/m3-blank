# coding: utf-8
"""
Модели
"""
import datetime
import mptt
from django.core.exceptions import ValidationError
from django.db import models


# =============================================================================
# Institutions
# =============================================================================


class Institution(models.Model):
    """
    Учреждение
    """
    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(u'Наименование', max_length=100)
    inn = models.CharField(u'ИНН', max_length=12)
    kpp = models.CharField(u'КПП', max_length=9)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.parent and self.parent.level > 0:
            raise ValidationError(u'Максимальный уровень вложенности')
        super(Institution, self).save(*args, **kwargs)

    class Meta:
        verbose_name = u"Учреждение"
        verbose_name_plural = u"Учреждениея"

mptt.register(Institution, order_insertion_by=['name'])


# =============================================================================
# Person
# =============================================================================
class Person(models.Model):
    """
    Физическое лицо
    """
    GENDERS = (
        (0, u'Женский'),
        (1, u'Мужской')
    )

    name = models.CharField(u'Имя', max_length=50)
    surname = models.CharField(u'Фамилия', max_length=50)
    patronymic = models.CharField(u'Отчество', max_length=50)
    date_of_birth = models.DateField(u'Дата рождения', null=True, default=datetime.date.today)
    gender = models.SmallIntegerField(u'Пол', choices=GENDERS, default=GENDERS[1][0])
    institution = models.ForeignKey(Institution, verbose_name=u'Учреждение')

    @property
    def fullname(self):
        return u' '.join((self.name, self.surname, self.patronymic))

    def __unicode__(self):
        return self.fullname

    class Meta:
        verbose_name = u'Физическое лицо'
        verbose_name_plural = u'Физические лица'
