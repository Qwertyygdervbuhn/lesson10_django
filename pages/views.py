from django.http import HttpResponse, Http404
import json
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST
# Create your views here.

def home(request):
    return HttpResponse("Hello World")

def hello(request):
    return HttpResponse("Hello")

def article(request, pk):
    if pk not in {1, 2, 5}:
        raise Http404("Статтю не знайдено")
    return HttpResponse(f"Стаття #{pk}")

def greet(request):
    name = request.GET.get("name", "гость")
    return  HttpResponse(f"Салам, {name}!")


@require_POST
def echo_json(request):
    try:
        data = json.loads(request.body)
    except (ValueError, UnicodeDecodeError):
        return HttpResponseBadRequest("Некоректний JSON")

    if not isinstance(data, dict):
        return HttpResponseBadRequest("Очікується JSON-об'єкт")

    return JsonResponse({"received": data})
from django.http import JsonResponse
from django.shortcuts import redirect
def status_demo(request):
    response = JsonResponse({"ok": True, "count": 3}, status=200)
    response["X-Lesson"] = "11"
    return response
def go_home(request):
    return redirect("pages:hello")