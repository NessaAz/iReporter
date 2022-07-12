from rest_framework import generics
from .serializers import ClientSerializer, UserSerializer, AdminSerializer
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import RedFlag, Intervention
from .serializers import RedFlagSerializer, InterventionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework import viewsets
from . import models
import cloudinary.uploader


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/users',
        'api/admin',
        'api/client',
        'api/token',
        'api/token/refresh/',
        'api/redflags',
        'api/interventions',
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


class RedFlagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows redflags to be viewed or edited.
    """
    queryset = RedFlag.objects.all()
    serializer_class = RedFlagSerializer
    parser_classes = (
        MultiPartParser,
        JSONParser,
        FormParser
    )

    # permission_classes = [permissions.IsAuthenticated]
    def post(self,request, *args, **kwargs):
        image = request.data('image')
        title = request.data('title')
        info = request.data('title')
        user = request.user
        stages = request.data('stages')
        created = request.data('created')
        location = request.data('location')
        upload_data = cloudinary.uploader.upload(image)
        RedFlag.objects.create(image=image,title=title,info=info, user=user, stages=stages, created=created,location=location)
        return Response({
            'status': 'success',
            'data': upload_data,
        }, status=201)


class InterventionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows interventions to be viewed or edited.
    """
    queryset = Intervention.objects.all()
    serializer_class = InterventionSerializer
    parser_classes = (
        MultiPartParser,
        JSONParser,
        FormParser
    )

    # permission_classes = [permissions.IsAuthenticated]
    def list(self, request, *args, **kwargs):
        interventions = Intervention.objects.all()
        serializer = InterventionSerializer(interventions, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
