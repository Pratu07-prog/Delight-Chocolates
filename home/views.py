from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        'variable':'Pratu',
    }
    return render(request, 'index.html', context)
    # return HttpResponse("This is Homepage")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is Aboutpage")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("This is servicespage")

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Your Form has been send!')
    return render(request, 'contact.html')
    #return HttpResponse("This is contactpage")
