from django.contrib import messages
from django.shortcuts import render, redirect
from reservations.models import Appartment
from reservations.forms import ReservationForm


def appartment_detail(request, slug):
    appartment = Appartment.objects.get(slug=slug)

    return render(request, "appartment_detail.html", {"appartment": appartment})


def reservation_create(request, slug):
    appartment = Appartment.objects.get(slug=slug)

    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.appartment = appartment
            reservation.save()
            messages.success(request, "Your demand has been sent to the landlord")
            return redirect('appartment-detail', slug=appartment.slug)
    else:
        form = ReservationForm()

    return render(request, "reservation_create.html", {"appartment": appartment, "form": form})
