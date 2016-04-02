from django.shortcuts import render

def show(request):
    products=product.objects.all()
    return render(request,'index.html',locals())
