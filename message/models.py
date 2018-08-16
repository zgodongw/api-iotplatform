from django.db import models

# Create your models here.
class Message(models.Model):
    message = models.CharField(max_length=512)
    username = models.CharField(max_length=256)
    timestamp = models.DateTimeField()

    def __str__(self):
        return "Message from {}".format(self.username)