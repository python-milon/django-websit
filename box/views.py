from django.shortcuts import render
from datetime import datetime
from box.models import Contact

# Create your views here.
def Home(request):
    return render( request,'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):

    if request.method == "POST":
       name = request.POST.get('name')
       surname = request.POST.get('surname')
       email = request.POST.get('email')
       subject = request.POST.get('subject')
       message = request.POST.get('message')
       contact= Contact(name=name,email=email,surname=surname,subject=subject,message=message,date=datetime.today())
       contact.save()
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')