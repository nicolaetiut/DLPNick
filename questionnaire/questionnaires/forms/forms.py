from django import forms

class AnsweredQuestionForm(forms.Form):
    class Meta:
        model = Question
        
class AnsweredPageForm(forms.Form):
    class Meta:
        model = Page
