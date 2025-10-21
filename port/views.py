from django.shortcuts import render,redirect
from .models import ProfilePic,Project,Contact

# Create your views here.
def home(request):
    profile = ProfilePic.objects.first()
    return render(request,'home.html',{'profile':profile})
def about(request):
    return render(request,'about.html')
def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})
def contact_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Save the data
        Contact.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            message=message
        )

        return redirect('contact')  # or show a thank you message

    return render(request, 'contact.html')
