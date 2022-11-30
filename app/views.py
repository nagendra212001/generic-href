from django.shortcuts import render

# Create your views here.
def dj(request):
    return render(request,'dj.html')

def tillu(request):
    return render(request,'tillu.html')