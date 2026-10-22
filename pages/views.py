import json
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseBadRequest
from .forms import FeedbackForm
# Create your views here.

def home(request):
    return HttpResponse("Hello World")

def hello(request):
    context = {
        "student_name": "Олена",
        "technologies": ["Python", "Django", "NumPy"],
        "comment": "<script>alert(1)</script>",
    }
    return render(request, "pages/hello.html", context)

def article(request, pk):
    if pk not in {1, 2, 5}:
        raise Http404("Статтю не знайдено")
    return HttpResponse(f"Стаття #{pk}")

def greet(request):
    name = request.GET.get("name", "гость")
    return HttpResponse(f"Салам, {name}!")

@require_POST
def echo_json(request):
    try:
        data = json.loads(request.body)
    except (ValueError, UnicodeDecodeError):
        return HttpResponseBadRequest("Некоректний JSON")

    if not isinstance(data, dict):
        return HttpResponseBadRequest("Очікується JSON-об'єкт")

    return JsonResponse({"received": data})

def status_demo(request):
    response = JsonResponse({"ok": True, "count": 3}, status=200)
    response["X-Lesson"] = "11"
    return response

def go_home(request):
    return redirect("hello")

def feedback_success(request):
    return HttpResponse("<h1>Дякуємо! Повідомлення успішно надіслано.</h1>")
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            return redirect("feedback_success")
    else:
        form = FeedbackForm()
    return render(request, "pages/feedback.html", {"form": form})