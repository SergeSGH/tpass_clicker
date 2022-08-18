from rest_framework.decorators import api_view
from rest_framework.response import Response
import hashlib
from rest_framework import status


@api_view(['POST'])
def GetLink(request):
    print(dict(request))
    link = 'aaa'
    blink = link.encode('utf-8')
    hash_object = hashlib.sha224(blink)
    hex_dig = hash_object.hexdigest()
    return Response(status=status.HTTP_200_OK, data={'short_link': hex_dig})





