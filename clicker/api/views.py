import datetime as dt
import hashlib

from django.utils import timezone as tz
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from redirect.models import Link


@api_view(['POST'])
def GetLink(request):
    link = request.data.get('link')
    expires_in = request.data.get('expires_in')
    if link:
        blink = link.encode('utf-8')
        hash_object = hashlib.sha224(blink)
        hex_dig = hash_object.hexdigest()
        length = 4
        new_unique = False
        exists_in_db = False
        while not new_unique and not exists_in_db:
            length += 1
            short_link = hex_dig[:length]
            link_in_db = Link.objects.filter(short_link=short_link).count()
            print(link_in_db)
            if not link_in_db:
                new_unique = True
                if expires_in:
                    link_time = dt.timedelta(hours=expires_in)
                else:
                    link_time = dt.timedelta(weeks=52 * 100)
                exp_time = tz.now() + link_time
                new_link = Link.objects.create(
                    short_link=short_link,
                    original_link=link,
                    expires=exp_time
                )
                new_link.save()
            else:
                link_from_db = Link.objects.filter(short_link=short_link)[0]
                if link_from_db.original_link == link:
                    exists_in_db = True
                    if expires_in is not None:
                        link_time = dt.timedelta(hours=expires_in)
                    else:
                        link_time = dt.timedelta(weeks=52 * 100)
                    exp_time = tz.now() + link_time
                    link_from_db.expires = exp_time
                    link_from_db.save()
        expires_str = exp_time.strftime("%d.%m.%Y %H:%M")
    return Response(
        status=status.HTTP_200_OK,
        data={'short_link': short_link, 'expires': expires_str}
    )
