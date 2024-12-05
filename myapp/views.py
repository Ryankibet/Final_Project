
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from .forms import AppointmentForm
from django.contrib.auth.decorators import login_required
from . models import Appointment
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def index(request):
    return render(request, "index.html")
    
def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")


def testimonial(request):
    return render(request, "testimonial.html")

def blog(request):
    return render(request, "blog.html")


@login_required(login_url='accounts:login')
def appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            
        else:
            print(form.errors)  # Debugging: Outputs validation errors
            messages.error(request, "There was an error submitting the form. Please try again.")
    else:
        form = AppointmentForm()

    return render(request, 'appointment.html', {'form': form})

def team(request):
    return render(request, "mine.html")


@login_required
def appointment(request):
    if request.method == 'POST':
        contact = Appointment(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            Message = request.POST.get('Message'),
        )
        contact.save()
        # Redirect to a page after saving
        return redirect('myapp:index')  # Adjust the redirect to your desired page
    else:
        return render(request, 'appointment.html')
  