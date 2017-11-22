# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from ..python_exam_login_app.models import User

from django.db import models

# Create your models here.

class ItemManager(models.Manager):
    pass

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    liked_user = models.ManyToManyField(User, related_name="liked_item")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<Item object: {} {} {}>".format(self.item_name, self.liked_user, self.created_at)

    objects = ItemManager()
