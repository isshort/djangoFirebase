from django.shortcuts import render
from account.firebase_config import firebase

auth = firebase.auth()
database = firebase.database()


def index(request):
    return render(request, "index.html")


def login(request):
    print("your request mehtod is ", request.method)
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get("password")
        user = auth.sign_in_with_email_and_password(email, password)
        id_token=user['idToken']
        print("id_token",id_token)
        account=auth.get_account_info(id_token)
        print("your account is ",account)
        return render(request, "index.html", {"user": user})
    return render(request, "login.html")


def sign_up(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get("password")

        user = auth.create_user_with_email_and_password(email, password)
        uid = user['localId']
        data = {'name': username, 'status': '1'}
        database.child('users').child(uid).child('details').set(data)
        return render(request, 'index.html', {'user': user})
    return render(request, 'signup.html')

