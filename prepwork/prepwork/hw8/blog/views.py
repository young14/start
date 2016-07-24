# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django import forms
from blog.models import User

class UserForm(forms.Form):
    username = forms.CharField()
    headImage = forms.FileField()


def register(request):
    if  request.method == 'POST':
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            #print uf.cleaned_data['username']
            #print request.FILES
            #fp = file('upload/' + uf.cleaned_data['headImage'].name, 'wb')
            #s = uf.cleaned_data['headImage'].read()
            #fp.write(s)
            #fp.close()
            username = uf.cleaned_data['username']
            headImage = uf.cleaned_data['headImage']
            user = User()
            user.usename = username
            user.headImage = headImage
            user.save()
            return HttpResponse('ok')
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf': uf})
