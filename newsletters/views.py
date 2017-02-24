# coding=utf-8
from django.contrib import messages
from django.shortcuts import render

from newsletters.forms import JoinForm
from .models import Join


def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
    except:
        ip = ""
    return ip


def join(request):
    form = JoinForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email = form.cleaned_data['email']
            new_join_old, created = Join.objects.get_or_create(email=email)
            if created:
                new_join_old.ip_address = get_ip(request)
                new_join_old.save()
                messages.success(request, "El correo se registro correctamente")
            else:
                messages.info(request, "El correo ya esta registrado")
        else:
            messages.error(request, "No se pudo registrar su correo")

    context = {
        "title": "Registrate a nuestro boletín de noticias",
        "form": form
    }
    return render(request, "newsletter/form.html", context)
