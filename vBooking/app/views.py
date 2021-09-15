from django.shortcuts import render
from django.http import HttpResponse

from app.models import Post, Event, Reservation
from app.forms import EventForm, ReservationForm

import qrcode

from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, "index.html")

def event(request):
    if request.method == "GET":
        form = EventForm()
        return render(request, "event.html", {"form": form})
    elif request.method == "POST":
        event = Event.objects.get(name=request.POST.get('name'))
        if event:
            form = EventForm(request.POST, instance=event)
            form.save()
            return HttpResponse("Success. Existing Event updated.")
        else:
            form = EventForm(request.POST)
            form.save()
            return HttpResponse("Success. New Event created.")
        

def events(request):
    if request.method == "GET":
        id = request.GET.get('id', '')
        if id == '':
            events = Event.objects.all()
            return render(request, "events.html", {"events": events})
        else:
            event = Event.objects.get(id=id)
            form = EventForm(instance=event)
            return render(request, "event.html", {"form": form, "edit":True})

@csrf_exempt
def reservation(request):
    if request.method == "GET":
        form = ReservationForm()
        return render(request, "reservation.html", {"form": form})
    elif request.method == "POST":
        event = Event.objects.get(id=request.POST.get('event'))
        reservation = Reservation.objects.filter(email=request.POST.get('email'), event=event)
        if reservation:
            form = ReservationForm(request.POST, instance=reservation[0])
            form.save()
            return HttpResponse("Success. Existing Reservation updated.")
        else:
            form = ReservationForm(request.POST)
            reservation = form.save()

            url = f'http://192.168.2.108:8000/reservations/?id={reservation.id}'
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save(f'qrcode{reservation.id}.png')

            return HttpResponse("Success. New Reservation created.")

def reservations(request):
    if request.method == "GET":
        id = request.GET.get('id', '')
        if id == '':
            reservations = Reservation.objects.all()
            return render(request, "reservations.html", {"reservations": reservations})
        else:
            reservation = Reservation.objects.get(id=id)
            form = ReservationForm(instance=reservation)
            return render(request, "reservation.html", {"form": form, "edit": True})

def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        print(request.POST.body)

def posts(request):
    search_term = request.GET.get('searchTerm', '')
    posts = Post.objects.filter(title__contains=search_term)
    return render(request, "posts.html", {"search_term": search_term, "posts": posts})

def post(request):
    id = request.GET.get('id', '')
    post = Post.objects.get(id=id)
    return render(request, "post.html", {"post": post})