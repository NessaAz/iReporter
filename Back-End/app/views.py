from django.http import HttpResponse, JsonResponse
from .models import RedFlag, Intervention
from .serializers import RedFlagSerializer, InterventionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the iReporter')


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
