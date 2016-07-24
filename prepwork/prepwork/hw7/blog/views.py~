# Create your views here.
from django import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response


class UserForm(forms.Form):
    name = forms.CharField()


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            return HttpResponse('OK')
    else:
        form = UserForm()
        return render_to_response('register.html',{'form':form})

