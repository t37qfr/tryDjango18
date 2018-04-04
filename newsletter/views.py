from django.shortcuts import render

from .forms import ContactForm,SignUpForm

# Create your views here.
def home(request):
    title = 'Welcome'
    if request.user.is_authenticated():
        title = 'hello {}'.format(request.user)

    #Form
    form = SignUpForm(request.POST or None)
    #Context
    context = {
        'template_title': title,
        'form': form,
        'showForm': True
    }

    #Form Validation
    if form.is_valid():
        instance = form.save(commit=False)
        if instance.full_name=='':
            instance.full_name = 'Nobody'
        instance.save()
        #recontext
        context = {
            'template_title': 'Thank You!',
            'showForm': False
        }


    return render(request,'home.html',context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        full_name = form.cleaned_data.get('full_name')
        print(email,message,full_name)
    context={
        'form':form,
    }
    return render(request,'forms.html',context)