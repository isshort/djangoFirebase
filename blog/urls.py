from django.urls import path

from blog.views import *

app_name = "blog"
urlpatterns = [
    path('index/', index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name="signup"),
]
