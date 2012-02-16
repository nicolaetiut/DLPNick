from questionnaires.models import Questionnaire
from questionnaires.models import Page
from questionnaires.models import Question
from questionnaires.models import Answer
from questionnaires.models import Result
from django.contrib import admin


class QuestionnaireAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        ('Date information', {
            'fields': ['creation_date', 'description'],
            'classes': ['collapse']
        }),
    ]

admin.site.register(Questionnaire, QuestionnaireAdmin)

admin.site.register(Page)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Result)
