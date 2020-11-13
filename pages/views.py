from django.http import HttpResponse

# Create your views here.
def homePageView(req):
    return HttpResponse('hello, world')
