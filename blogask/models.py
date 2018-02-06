from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    likes = models.IntegerField()
    def __str__(self):
        return self.content + ' ' + self.likes

    # class Meta:
    #     db_table = ''
    #     managed = True
    #     verbose_name = 'Question'
    #     verbose_name_plural = 'Questions'