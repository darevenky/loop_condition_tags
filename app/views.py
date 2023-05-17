from django.shortcuts import render

# Create your views here.

def loop(request):
    d={'name':'venkydare'}
    return render(request,'loop.html',d)

def conditional(request):
    d={'a':10 ,'b':20 ,'c':30}
    return render(request,'conditional.html',d)

def mul_cond(request):
    d={'a':50 ,'b':20 ,'c':30, 'd':40}
    return render(request,'mul_cond.html',d)