from django.urls import path
from .views import homework_querysets

urlpatterns = [
    path('homework/querysets/', homework_querysets),
]