from django.db import models


class Questionnaire(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    creation_date = models.DateTimeField('date created')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Page(models.Model):
    ordering = ['order_index']
    questionnaire = models.ForeignKey(Questionnaire)
    title = models.CharField(max_length=50)
    order_index = models.IntegerField()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Question(models.Model):
    ordering = ['order_index']
    page = models.ForeignKey(Page)
    question_text = models.CharField(max_length=200)
    order_index = models.IntegerField()

    def __unicode__(self):
        return self.question_text

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question)
    answer_text = models.CharField(max_length=50)
    score = models.IntegerField()

    def __unicode__(self):
        return self.answer_text + "with score" + str(self.score)

    def __str__(self):
        return self.answer_text + "with score" + str(self.score)


class Result(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    result_text = models.CharField(max_length=300)
    upper_limit = models.IntegerField()

    def __unicode__(self):
        return self.result_text + "with limit" + str(self.upper_limit)

    def __str__(self):
        return self.result_text + "with limit" + str(self.upper_limit)
