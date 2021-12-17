from django.urls import path
from . import views

urlpatterns = [
    path("", views.TodoList.as_view(), name="list"),
    path("detail/<int:pk>", views.TodoDetail.as_view(), name="detail")
]
