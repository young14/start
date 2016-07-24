# Create your views here.
#from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.template import loader, Context
"""
class Person(object):
    def _init_(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def say(self):
        return "I'm" + self.name

def index(request, pars):
    user = {'name':'tom', 'age': 23, 'sex': 'male'}
    book_list = {'python', 'jave', 'php', 'web'}

    return render_to_response('index.html',{'title':'my page', 'book_list': book_list, 'user': user, 'id':pars})
"""
"""
def index(request):
    t = loader.get_template('index.html')
    c = Context({})

    return HttpResponse(t.render(c))
"""

class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        return "WTF are you doing, " + self.name


def index(request):
    user = {'name':'boo', 'age': 23, 'sex': 'male'}
    #user = Person('tom',23,'male')
    book_list = ["python", "php", "java", "web"]
    return render_to_response('index.html',{'title':'my pkq', 'user':user, 'book_list': book_list})
