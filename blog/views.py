from django.contrib.auth import login
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from blog.firebase_config import firebase
from blog.form import UserForm
from blog.models import User

auth = firebase.auth()
database = firebase.database()


def index(request):
    info = [
        {'name': "Namatullah", 'surname': "Wahidi"},
        {'name': "Rahim", 'surname': "R"},
        {'name': "Nawid", 'surname': "akhtar"},
        {'name': "Enayet", 'surname': "Sayeed"},
        {'name': "Hadi", 'surname': "Ekrami"},
    ]
    cities = [
        {'name': "Bishkek", 'populations': '2000000', 'country': "Kyrgyzstan"},
        {'name': "Batken", 'populations': '1000000', 'country': "Kyrgyzstan"},
        {'name': "Ankara", 'populations': '5000000', 'country': "Turkey"},
        {'name': "Kabul", 'populations': '6000000', 'country': "Afghanistan"},
        {'name': "Tashkent", 'populations': '5000000', 'country': "Uzbekistan"},
    ]
    return render(request, "index.html", {'info': info,'cities':cities})


class LoginView(TemplateView):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get("password")
        user = auth.sign_in_with_email_and_password(email, password)
        id_token = user['idToken']
        request.session['uid'] = id_token
        # print("id_token", id_token)
        # account = auth.get_account_info(id_token)
        # login(request, user)
        return render(request, "index.html", {'user': user})


class SignUpView(CreateView):
    template_name = "signup.html"
    model = User
    form_class = UserForm

    def form_valid(self, form):
        data = form.data.dict()
        user = auth.create_user_with_email_and_password(email=data['email'], password=data['password'])
        uid = user['localId']
        database.child('account_users').child(uid).child('details').set(data)

        return render(self.request, 'index.html', {'user': user, 'data': data})


"""
This is testing1 branch

Namatullah Wahidi

favorite color is green

children
pull request 
"""
