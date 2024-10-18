from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer


@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data) # всех юзеров вернет


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def set_language_level(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    level = request.data.get('level')
    if level is not None and 1 <= level <= 5:
        user.language_level = level
        user.save()
        return Response({'message': 'Language level updated', 'new_level': user.language_level}) #обновляет уровень языка
    return Response({'error': 'not correct level'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def set_energy(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    energy = request.data.get('energy')
    if energy is not None and energy >= 0:
        user.energy = energy
        user.save()
        return Response({'message': 'Energy updated', 'new_energy': user.energy}) #обновляет количество энергии у нашего чела
    return Response({'error': 'not correct energy'}, status=status.HTTP_400_BAD_REQUEST)
