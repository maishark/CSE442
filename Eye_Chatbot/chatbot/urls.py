from django.urls import path
from . import views

urlpatterns = [
    path("chatbot", views.chat, name="chat"),
    path("", views.index, name="index"),
    path("ask_question/", views.ask_question, name="ask_question"),
    path('login/', views.custom_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup')
]