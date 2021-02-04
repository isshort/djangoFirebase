from django.urls import path

from account.views import *

app_name = "account"
urlpatterns = [
    path('index/', index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('signup/', SignUpView.as_view(), name="signup"),
]
