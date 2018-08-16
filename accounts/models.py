from django.db import models
from api.models import Organisation
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    defaultSite = models.CharField(max_length=256)
    color = models.CharField(max_length=7)

    def enable(self):
        self.user.is_active = True
        self.user.save() 

    def disable(self):
        self.user.is_active = False
        self.user.save() 
    
    def __str__(self):
        return "Profile for {}".format(self.user)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
    