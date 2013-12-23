#!/usr/bin/python
#-*- coding: UTF-8 -*-

from www.models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User

def create_profile(sender, **kwargs):
    user = kwargs['instance']
    if not kwargs['created']:
        try: Profile(user=user).save()
        except: pass

post_save.connect(create_profile, sender=User)

