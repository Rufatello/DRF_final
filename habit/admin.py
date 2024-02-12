from django.contrib import admin

from habit.models import Habit, Reflex


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Reflex)
class ReflexAdmin(admin.ModelAdmin):
    list_display = ('id',)
