from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('question', views.question, name='question_index'),
    path('question/<str:question_pk>', views.question, name='question'),
    path('question/<str:question_pk>/<int:answer_pk>', views.question, name='question_answer'),
]
