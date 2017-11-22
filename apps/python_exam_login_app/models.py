# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re  ##import Regular Expressions for email validation
import bcrypt

# Create your models here.

class UserManager(models.Manager):

    def validate(self, postData):
        results = {'status': True, 'errors':[]}
        ##########Validation for name
        if len (postData ['name']) < 3:
            results['errors'].append('Your name is too short.')
            results['status'] = False
        ##########Validating name only contains characters
        if not re.match("[A-Za-z]", postData['name']):
            results['errors'].append('Name must only contain characters.')
            results['status'] = False
        ##########Validation for username
        if len (postData ['user_name']) < 3:
            results['errors'].append('Your username is too short.')
            results['status'] = False
        ##########Validating username only contains characters
        if not re.match("[A-Za-z]", postData['user_name']):
            results['errors'].append('Username must only contain characters.')
            results['status'] = False
        ##########Validation for email        
        #if not re.match("[^@]+@[^@]+\.[^@]+", postData['email']):
            #results['errors'].append('Email is not valid.')
            #results['status'] = False
        ##########Validation for password equals password confirmation
        if postData['pw'] != postData['pwcon']:
            results['errors'].append('Passwords do not match.')
            results['status'] = False 
        ##########Validation length of password
        if len(postData['pw']) < 5:
            results['errors'].append('Password needs to be 5 characters long at least.')
            results['status'] = False
        ##########Validating if username already exists in database 
        if len(self.filter(user_name = postData ['user_name'])) > 0:
            results['errors'].append('User already exists.')
            results['status'] = False
        return results

        ##########Putting new form data in database
    def creator(self, postData):
        user = self.create(name = postData['name'], user_name = postData['user_name'], password = bcrypt.hashpw(postData['pw'].encode(), bcrypt.gensalt()), hiredate = postData['hiredate'])
        return user

        ##########Checking login info to see if user exsists
    def loginVal(self, postData):
        results = {'status': True, 'errors':[], 'user': None}
        users = self.filter(user_name = postData['user_name'])

        if len(users) < 1:
            results['status'] = False
        else:
            if bcrypt.checkpw(postData['pw'].encode(), users[0].password.encode()):
                results['user'] = users[0]
            else:
                results['status'] = False 
        return results


class User(models.Model):
    name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    hiredate = models.DateField(auto_now=False, auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    def __repr__(self):
        return "<User object: {} {} {} {}>".format(self.name, self.user_name, self.password, self.hiredate)

    objects = UserManager()