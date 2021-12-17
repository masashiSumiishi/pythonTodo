from django.urls import path
from . import views

urlpatterns = [
    path("", views.TodoList.as_view(), name="list"),
    path("detail/<int:pk>", views.TodoDetail.as_view(), name="detail"),
    path("create/", views.TodoCreate.as_view(), name="create"),
    path("update/<int:pk>", views.TodoUpdate.as_view(), name="update")
]
