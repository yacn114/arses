from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255,blank=False,null=False)
    phone = models.IntegerField(blank=False,null=False)
    last_seen_site = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.phone
