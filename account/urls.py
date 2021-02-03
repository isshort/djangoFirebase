from django.urls import path

from account import views

app_name = "account"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('signup/', views.sign_up, name="signup"),
]
