from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import ClientSerializer,UserSerializer,AdminSerializer
from rest_framework.authtoken.models import Token

# Create your views here.
class AdminSignUpView(generics.GenericAPIView):
    serializer_class=AdminSerializer
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        context = {
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'message':'account made successfully'
        }
        return Response(context)

class ClientSignUpView(generics.GenericAPIView):
    serializer_class=ClientSerializer
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        context = {
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'message':'account made successfully'
        }
        return Response(context)