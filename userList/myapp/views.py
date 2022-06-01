from django.shortcuts import render

# Create your views here.

import requests

def users(request):
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    print(users)
    return render(request, "index.html",{'users': users})