from django.db import models
from django.conf import settings
from django.db.models.signals import post_save

User=settings.AUTH_USER_MODEL

# Create your models here.
class Profile(models.Model):
    user        =models.OneToOneField(User)
    followers   =models.ManyToManyField(User,related_name='is_following',blank=True)
    #followings  =models.ManyToManyField(User,related_name='followings',blank=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    activated   =models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

def post_save_user_receiver(sender,instance,created,*args,**kwargs):
    if created:
        profile, is_created= Profile.objects.get_or_create(user=instance)
        default_user_profile= Profile.objects.get_or_create(user__id=1)[0]
        default_user_profile.followers.add(instance)

        profile.followers.add(default_user_profile.user)
        profile.followers.add(2)

post_save.connect(post_save_user_receiver,sender=User)