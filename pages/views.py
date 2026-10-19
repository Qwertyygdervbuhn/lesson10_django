from django.http import HttpResponse

def about(request):
    return HttpResponse("<h1>Курс: Python та Django</h1>")