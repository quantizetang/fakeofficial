from django.db import models

class silverusers(models.Model):
    user_name  = models.CharField('username', max_length=200)
    user_description  = models.CharField('userdesc', max_length=100)
    user_bd = models.DateField('birthday')
    
    def __str__(self):
        return '%s' % (self.user_name)
    
    class Admin:
        pass