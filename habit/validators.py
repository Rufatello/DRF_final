import re
from rest_framework.serializers import ValidationError


class TimeValidator:

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value, *args, **kwargs):
        tmp_time = dict(value).get(self.fields)
        if tmp_time > 120:
            raise ValidationError('Время не может быть больше 120 секунд')


class ReflexPleasantValidator:
    def __init__(self, is_pleasant, habit, fee):
        self.field_habit = habit
        self.field_fee = fee
        self.field_is_pleasant = is_pleasant

    def __call__(self, value):
        tmp_habit = dict(value).get(self.field_habit)
        tmp_fee = dict(value).get(self.field_fee)
        tmp_is_pleasant = dict(value).get(self.field_is_pleasant)
        if tmp_is_pleasant and (tmp_habit or tmp_fee):
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


class ReflexFeeValidator:
    def __init__(self, habit, fee):
        self.field_habit = habit
        self.field_fee = fee

    def __call__(self, value):
        tmp_habit = dict(value).get(self.field_habit)
        tmp_fee = dict(value).get(self.field_fee)
        if tmp_habit and tmp_fee:
            raise ValidationError("Нельзя одновременно выборать связанную привычку и указать вознаграждение.")
