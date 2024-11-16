from django.shortcuts import render, redirect, get_object_or_404
from appointments.models import Doctor
from users.models import CustomUser
from . models import Message
from django.contrib.auth.decorators import login_required

@login_required()
def chat(request):
    user = request.user
    is_doctor = Doctor.objects.filter(name=user).exists()
    patients = None
    doctor_details = None
    if is_doctor:
        doctor_details = Doctor.objects.get(name=user)
        patients = CustomUser.objects.filter(message__receiver=doctor_details).distinct()
    doctors = Doctor.objects.all()
    context = {
        'is_doctor': is_doctor,
        'doctor_details': doctor_details,
        'doctors': doctors,
        'user': user,
        'patients': patients,

        }
    return render (request, 'chat/chat.html', context)

@login_required()
def conversation(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        text = request.POST.get('text')
        sender = request.user
        message = Message.objects.create(sender=sender, receiver=doctor, text=text)
        return redirect('conversation', doctor_id=doctor_id)
    else:
        patient = request.user
        messages_sent_by_patient = Message.objects.filter(sender=patient, receiver=doctor)
        messages = messages_sent_by_patient.order_by('timestamp')
        context = {
            'doctor': doctor,
            'messages': messages
        }
        return render(request, 'chat/conversation.html', context)