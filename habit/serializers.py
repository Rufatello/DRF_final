from rest_framework import serializers
from habit.models import Habit, Reflex
from habit.validators import TimeValidator, ReflexPleasantValidator, ReflexFeeValidator


class HabitSerializers(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'


class ReflexSerializers(serializers.ModelSerializer):

    class Meta:
        model = Reflex
        fields = '__all__'
        validators = [TimeValidator("time_to_complete"),
                      ReflexPleasantValidator("is_pleasant", "habit", "fee"),
                      ReflexFeeValidator('habit', 'fee')
                      ]


class ReflexDetailSerializer(serializers.ModelSerializer):
    habit = HabitSerializers(read_only=True)

    class Meta:
        model = Reflex
        fields = '__all__'




