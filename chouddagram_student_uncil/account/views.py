from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html',)



def registration(request):
    return render(request,'Registration.html',)




def login(request):
    return render(request,'Login.html',)

def services(request):
    return render(request,'service.html',)

def about(request):
    return render(request,'about.html',)