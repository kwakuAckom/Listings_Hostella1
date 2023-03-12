from urllib import request
from .serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import permissions, status

User = get_user_model()

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = data.request
            name = data['name']
            email = data['email']
            email = email.lower()
            password = data['password']
            confirm_password = data['confirm_password']
            is_realtor = data['is_realtor']

            if is_realtor == 'True':
                is_realtor = True
            else:
                is_realtor = False

            if password == confirm_password:
                if password >= 8:
                    if not User.objects.filter(email=email).exists():
                        if not is_realtor:
                            User.objects.create_user(name= name, email=email, password=password)
                            return Response(
                                {'success':'User created successfully'},
                                status=status.HTTP_201_CREATED,
                            )
                        else:
                            User.objects.create_realtor(name= name, email=email, password=password)
                            return Response(
                                {'success':'Realtor account created successfully'},
                                status=status.HTTP_201_CREATED,
                            )
                    else:

                        return Response(
                            {'error':'User with this email already exists'},
                            status=status.HTTP_400_BAD_REQUEST,
                        )

                else:
                    return Response(
                        {'error':'Password must be at least 8 characters in lenght'},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                        {'error':'Passwords do not match'},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

        except:
            return Response(
                {'error': 'Something went wrong'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)
            return Response(
                {'error': 'Something went wrong when retrieving user details'},
                status=status.HTTP_200_OK

            )

        except:
            return Response(
                {'error': 'Something went wrong when retrieving user details'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
