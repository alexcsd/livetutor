from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createquestion', views.create_question, name='createquestion'),
    path('question/<int:pk>', views.question_view, name='question'),
    path('questions', views.questions_view, name='questions'),
    path('question/<int:pk>/answer', views.answer, name='answer'),
    path('question/reply/<int:pk>', views.reply, name='reply'),
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name='logout'),
]
