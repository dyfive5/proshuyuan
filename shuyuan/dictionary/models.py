from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class WordType(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    typename = models.CharField(max_length=10)

class Word(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey('WordType',related_name='type',on_delete=models.CASCADE,null=True)
    owner = models.ForeignKey('auth.User', related_name='words', on_delete=models.CASCADE,null=True)
    content = models.CharField(max_length=300)
    img_url = models.URLField(default=None)
    like_count = models.IntegerField(default=0)
    dislike_count = models.IntegerField(default=0)
    STATUES_CHOICE = (
        ('EP','Examine Passed'),
        ('WE','Wait Examine')
    )
    status = models.CharField(max_length=2,choices=STATUES_CHOICE,default='WE')
