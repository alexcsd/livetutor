from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.content + ' ' + str(self.likes) + ' ' + self.user.username

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.content + ' ' + str(self.likes)+ ' ' + self.user.username

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    likes = models.IntegerField(default=0)
    def __str__(self):
        return self.content + ' ' + str(self.likes)+ ' ' + self.user.username
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Reply'
        verbose_name_plural = 'Replys'