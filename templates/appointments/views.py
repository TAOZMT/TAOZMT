from django.shortcuts import render, redirect
from . forms import AppointmentForm
from . models import Doctor
from django.core.mail import send_mail

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            reason = form.cleaned_data['reason']
            fullname = form.cleaned_data['fullname']
            phonenumber = form.cleaned_data['phonenumber']
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']
            appointment.save()
            doctors = Doctor.objects.filter(field=reason)
            for doctor in doctors:
                subject = f'New Appointment from {fullname}'
                message = f'Greetings Dr. {doctor.name.first_name} {doctor.name.last_name}, \n\nYou have received new appointment from {fullname}. \n\nPhone Number: {phonenumber}\n\nEmail: {email}\n\n {description} \n\n Your {reason} services are required.\n\nRegards\n Group1Telehealth'
                from_email = 'sainhope16@gmail.com'
                to_email = doctor.name.email
                send_mail(
                    subject,
                    message,
                    from_email,
                    [to_email,],
                    fail_silently=False,
                )
            return redirect('homepage')
        
    form = AppointmentForm()
    context = {
        'form': form,
    }
    return render (request, 'appointments/book_appointment.html', context)