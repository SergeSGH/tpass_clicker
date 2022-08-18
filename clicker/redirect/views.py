from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.utils import timezone as tz

from .models import Link


def RedirectLink(request, short_link):
    link = get_object_or_404(Link, short_link=short_link)
    if tz.now() < link.expires:
        return redirect(link.original_link)
    else:
        return HttpResponse('Cрок действия ссылки закончился', status=400)
