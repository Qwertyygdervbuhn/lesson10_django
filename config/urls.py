from django.urls import path
from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hello/', views.hello, name='hello'),
    path("articles/<int:pk>/", views.article, name="article"),
    path('greet/', views.greet, name='greet'),
    path("api/echo/", views.echo_json, name="echo"),
    path("status/", views.status_demo, name="status"),
    path("go/", views.go_home,name="go",),
    path("feedback/success/", views.feedback_success, name="feedback_success"),
    path("feedback/", views.feedback, name="feedback"),
]