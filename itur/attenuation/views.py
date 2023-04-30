from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff, Product, Contact

# Create your views here.

def Home(request):
    #return HttpResponse('Hello World')
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'attenuation/home.html',context)

def About(request):
    return render(request, 'attenuation/about.html')

def Contacts(request):
    namelist = Staff.objects.all()
    context = {'namelist': namelist}

    if request.method == 'POST':
        data = request.POST.copy()
        print('data: ', data)
        name = data.get('name')
        title = data.get('title')
        detail = data.get('detail')
        mail = data.get('mail')

        new_post = Contact()
        new_post.name = name
        new_post.title = title
        new_post.detail = detail
        new_post.mail = mail
        new_post.save()
        context['alert'] = 'success'
        
    return render(request, 'attenuation/contact.html',context)

def Service(request):
    return render(request, 'attenuation/service.html')

def Products(request):
    return render(request, 'attenuation/product.html')