from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from habit.models import Habit, Reflex
from habit.paginations import ReflexPagination
from habit.serializers import HabitSerializers, ReflexSerializers, ReflexDetailSerializer


class HabitCreateApiView(generics.CreateAPIView):
    serializer_class = HabitSerializers

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitListApiView(generics.ListAPIView):
    serializer_class = HabitSerializers
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated]


class ReflexCreateApiView(generics.CreateAPIView):
    serializer_class = ReflexSerializers

    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class ReflexListApiView(generics.ListAPIView):
    serializer_class = ReflexDetailSerializer
    queryset = Reflex.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reflex.objects.filter(user=self.request.user)


class ReflexAPIView(generics.ListAPIView):
    serializer_class = ReflexDetailSerializer
    queryset = Reflex.objects.filter(is_published=True)
    pagination_class = ReflexPagination


class ReflexUpdateApiView(generics.UpdateAPIView):
    serializer_class = ReflexSerializers
    permission_classes = [IsAuthenticated]
    queryset = Reflex.objects.all()

    def get_queryset(self):
        return Reflex.objects.filter(user=self.request.user)


class ReflexDestroyApiView(generics.DestroyAPIView):
    serializer_class = ReflexSerializers
    queryset = Reflex.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reflex.objects.filter(user=self.request.user)