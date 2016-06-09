#!/usr/bin/python
#-*- coding: UTF-8 -*-

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    from www.models import Profile
    user = kwargs['instance']
    if not kwargs['created']:
        try: Profile(user=user).save()
        except: pass

