from django.db import models

# Create your models here.
class Profile(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='profiles', on_delete=models.CASCADE)

    avatar_img = models.URLField()
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    ethnic = models.CharField(max_length=40,default='汉族')
    real_name = models.CharField(max_length=40)

    class Meta:
        ordering = ('created',)