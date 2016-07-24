# Create your views here.
from django.template import loader, Context
from django.http import HttpResponse

def index(request):
    t = loader.get_template('index.html')
    c = Context({'uname': 'alen'})
    html = t.render(c)
    return HttpResponse(html)
