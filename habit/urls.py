from django.urls import path

from habit.apps import HabitConfig
from habit.views import HabitCreateApiView, ReflexCreateApiView, ReflexListApiView, ReflexAPIView, ReflexUpdateApiView, \
    ReflexDestroyApiView, HabitListApiView

app_name = HabitConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateApiView.as_view(), name='habit-create'),
    path('habit/list/',  HabitListApiView.as_view(), name='habit-list'),
    path('reflex/create/', ReflexCreateApiView.as_view(), name='reflex-create'),
    path('reflex/list/', ReflexListApiView.as_view(), name='reflex-list'),
    path('reflex/published/', ReflexAPIView.as_view(), name='published-list'),
    path('reflex/<int:pk>/update/', ReflexUpdateApiView.as_view(), name='reflex-update'),
    path('reflex/<int:pk>/delete/', ReflexDestroyApiView.as_view(), name='reflex-delete')
]