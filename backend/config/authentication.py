import jwt
from django.conf import settings
from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from members.models import Member


class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):

        try:
            token = request.META.get('HTTP_AUTHORIZATION')

            if token is None:
                return None
            
            decoded = jwt.decode(
                token, settings.SECRET_KEY)

            pk = decoded.get("pk")
            user = Member.objects.get(pk=pk)
            return (user, None)
        except ValueError:
            return None
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed(detail="JWT Format Invalid")