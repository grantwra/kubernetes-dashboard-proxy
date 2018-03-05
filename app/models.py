# -*- coding: utf-8 -*-
from django.db import models


class PROXY_users(models.Model):
    password = models.CharField(max_length=128, null=False)
    username = models.CharField(max_length=32, null=False)
    salt = models.CharField(max_length=54, null=False)
    session_token = models.CharField(max_length=54, null=True)
    
    def __str__(self):
        return self.username
