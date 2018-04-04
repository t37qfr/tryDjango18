from django.db import models

'''
blank: Form
null: DB
auto_now: updated
auto_now_add: created
'''
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=200,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.email