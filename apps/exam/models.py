from __future__ import unicode_literals
import datetime
from django.db import models

class UserManager (models.Manager):
    def validate_register(self, postData):
        errors = []
        if len(postData['name'])<1:
            errors.append('Name field cannot be blank!')
        if len(postData['alias'])<1:
            errors.append('Alias field cannot be blank!')
        if len(postData['email'])<1:
            errors.append('Email field cannot be blank!')
        if len(postData['password'])<1:
            errors.append('Password field cannot be blank!')
        if postData['password'] != postData['confirm_password']:
            errors.append("Passwords do not match.")
        if len(postData['dob']) < 1:
            errors.append('Date of Birth field cannot be blank!')

        return errors

    def validate_login(self, postData):
        errors = []
        if not self.filter(email = postData['email']):
            errors.append('Email not found. Please try again.')
        #if not self.filter(password = postData['PW']):
           # errors.append ('Password is incorrect. Please try again.')
        if len(postData['email'])<1:
            errors.append('Email must not be blank!')
        if len(postData['PW'])<1:
            errors.append('Password must not be blank!')  
        return errors

class QuoteManager (models.Manager):
    def validate_quote(self, postData):
        errors = []
        if len(postData['quoted_by'])<4:
            errors.append('Quoter field must be greater than four characters!')
        if len(postData['message'])<11:
            errors.append('Message must be greater than ten characters!')  
        return errors

class User (models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    dob = models.DateField(null = True)
    favorite_quotes = models.ManyToManyField('Quote', related_name = 'favorite_quotes', default = None)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Quote (models.Model):
    quoted_by = models.CharField(max_length = 255 , null = True)
    message = models.CharField(max_length = 255)
    posted_by  = models.ForeignKey(User, related_name = 'posted_quotes', null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()

