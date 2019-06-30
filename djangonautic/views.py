from django.http import HttpResponse

def home(request):
    return HttpResponse('response')
def about(request):
    return HttpResponse("about")
