from django.contrib import admin

from .forms import SignUpForm
from .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
    list_display=['__str__','timestamp','updated']
    '''Replaced Admin Model Form with custom FORM from form.py'''
    form = SignUpForm
    #class Meta:
        #model = SignUp

admin.site.register(SignUp,SignUpAdmin)

