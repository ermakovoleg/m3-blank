# coding: utf-8

# from django.core.exceptions import ValidationError
from spyne import srpc, Integer, Unicode, Iterable, Boolean, rpc, Date
from spyne.model import ComplexModel

from models import Institution, Person


class InstitutionComplexModel(ComplexModel):
    id_ = Integer
    name = Unicode


@srpc(_returns=Iterable(InstitutionComplexModel))
def get_institution():
    return Institution.objects.values_list('id', 'name').all()\


# class PersonComplexModel(ComplexModel):
#     name = Unicode
#     surname = Unicode
#     patronymic = Unicode
#     date_of_birth = Date
#     institution_id = Integer


@rpc(Unicode, Unicode, Unicode, Date, Integer, _returns=Boolean)
def add_person(ctx, name, surname, patronymic, date_of_birth, institution_id):
    if name and surname and patronymic and date_of_birth and institution_id:
        try:
            institution = Institution.objects.get(pk=institution_id)
        except Institution.DoesNotExist:
            pass
        else:
            person = Person()
            person.name = name
            person.surname = surname
            person.patronymic = patronymic
            person.date_of_birth = date_of_birth
            person.institution_id = institution_id
            person.save()
            return True
    return False