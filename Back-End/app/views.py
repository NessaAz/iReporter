from rest_framework import generics
from .serializers import ClientSerializer, UserSerializer, AdminSerializer
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.http import HttpResponse, JsonResponse
from .models import RedFlag, Intervention, Admin, Client
from .serializers import RedFlagSerializer, InterventionSerializer, ClientProfileSerializer, AdminProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/admin',
        'api/adminprofile',
        'api/client',
        'api/clientprofile',
        'api/token',
        'api/token/refresh/',
        'api/flaglists',
        'api/interventions',
        'api/raiseflag/<int:id>/',
        'api/intervationrequest/<int:id>/',
        'api/adminprofiles',
        'api/clientsprofiles',
        'api/admins/<int:id>/',
        'api/clients/<int:id>/',
    ]
    return Response(routes)


class AdminSignUpView(generics.GenericAPIView):
    serializer_class = AdminSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        context = {
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'message': 'account made successfully'
        }
        return Response(context)


class ClientSignUpView(generics.GenericAPIView):
    serializer_class = ClientSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        context = {
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': Token.objects.get(user=user).key,
            'message': 'account made successfully'
        }
        return Response(context)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET', 'POST', 'DELETE'])
def flags_list(request, format=None):
    if request.method == 'GET':
        flags = RedFlag.objects.all()
        serializer = RedFlagSerializer(flags, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RedFlagSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201.CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def flag_detail(request, id, format=None):
    try:
        flag = RedFlag.objects.get(pk=id)
    except RedFlag.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RedFlagSerializer(flag)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RedFlagSerializer(flag, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        flag.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def interventions_list(request, format=None):
    if request.method == 'GET':
        interventions = Intervention.objects.all()
        serializer = InterventionSerializer(interventions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = InterventionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def intervention_detail(request, id, format=None):
    try:
        intervention = Intervention.objects.get(pk=id)
    except Intervention.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InterventionSerializer(intervention)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = InterventionSerializer(intervention, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        intervention.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def admins_list(request, format=None):
    if request.method == 'GET':
        admins = Admin.objects.all()
        serializer = AdminProfileSerializer(admins, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def admin_detail(request, id, format=None):
    try:
        admin = Admin.objects.get(pk=id)
    except Admin.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdminProfileSerializer(admin)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AdminProfileSerializer(admin, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        admin.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def clients_list(request, format=None):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientProfileSerializer(clients, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClientProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, id, format=None):
    try:
        client = Client.objects.get(pk=id)
    except Client.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientProfileSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ClientProfileSerializer(client, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        client.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
