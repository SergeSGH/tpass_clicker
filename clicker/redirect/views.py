from django.shortcuts import redirect, get_object_or_404
from .models import Link
from django.views.generic.base import RedirectView 


def RedirectLink(request, short_link):
    link = get_object_or_404(Link, short_link=short_link)
    print(link.expires)
    print(link.original_link)
    return redirect(link.original_link)
    #return RedirectView.as_view(url=link.original_link)