
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
            appointment = form.save(commit=False)
            appointment.user = request.user

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
            phone = request.POST.get('phone'),
            message = request.POST.get('message'),
        )
        contact.save()
        # Redirect to a page after saving
        return redirect('myapp:appointment')  # Adjust the redirect to your desired page
    else:
        return render(request, 'appointment.html')
@login_required
def retrieve_appointments(request):
    appointments = Appointment.objects.all()
    context = {'appointments':appointments}
    return render(request, 'show_appointments.html', context)
 

def delete_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    return redirect("myapp:show_appointments")

def update_appointment(request, appointment_id):
    appointment =get_object_or_404(Appointment, id=appointment_id )
    if request.method == 'POST':
        appointment.name = request.POST.get('name')
        appointment.email = request.POST.get('email')
        appointment.message = request.POST.get('message')
        appointment.save()
        return redirect("myapp:show_appointments")
     
    context = {'appointment': appointment}
    return render(request, "update_appointment.html", context)

