from django.shortcuts import render, redirect
from .forms import ParticipantForm, VehicleForm


def participant_registration(request):
    if request.method == 'POST':
        participant_form = ParticipantForm(request.POST)

        if participant_form.is_valid():
            participant = participant_form.save()
            return redirect('vehicles_form')  # Redirect to a success page or home page

    else:
        participant_form = ParticipantForm()

    return render(request, 'validation/participant_registration.html', {'participant_form': participant_form})




def success(request):
    return render(request, 'validation/success.html')






def vehicle_list(request):
    if request.method == 'POST':
        vehicles_form = VehicleForm(request.POST)

        if vehicles_form.is_valid():
            vehicle = vehicles_form.save()
            return redirect('success')  # Redirect to a success page or home page

    else:
        vehicles_form = VehicleForm()

    return render(request, 'validation/vehicles_form.html', {'vehicles_form': vehicles_form})












