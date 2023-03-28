from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.chat, name="chat"),
    path("process_message/", views.process_message, name="process_message"),
]