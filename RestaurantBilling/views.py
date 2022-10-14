from django.shortcuts import render



def index(request):
    return render(request,"index.html",{})
def AdminLogin(request):
    return render(request,'AdminLogin.html',{})

def logout(request):
    return render(request, 'index.html', {})