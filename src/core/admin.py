from django.contrib import admin

from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'next_question']


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'question', 'is_correct']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
