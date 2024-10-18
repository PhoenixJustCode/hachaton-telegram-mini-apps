from .models import User, KazakhTest  # Импортируем необходимые модели
# Импортируем сериализаторы
from .serializer import UserProfileSerializer, KazakhTestSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import KazakhTestSerializer


@api_view(['POST'])
def create_kazakh_test(request):
    """Создание нового теста"""
    serializer = KazakhTestSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_kazakh_tests(request, user_id):
    """Получение всех тестов для конкретного пользователя"""
    tests = KazakhTest.objects.filter(user_id=user_id)
    if not tests.exists():
        return Response({'error': 'No tests found for this user'}, status=status.HTTP_404_NOT_FOUND)

    serializer = KazakhTestSerializer(tests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializer = UserProfileSerializer(users, many=True)
    return Response(serializer.data)  # Возвращает всех пользователей


@api_view(['POST'])
def create_user(request):
    serializer = UserProfileSerializer(data=request.data)
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
        # Обновляет уровень языка
        return Response({'message': 'Language level updated', 'new_level': user.language_level})
    return Response({'error': 'Not a correct level'}, status=status.HTTP_400_BAD_REQUEST)


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
        # Обновляет количество энергии
        return Response({'message': 'Energy updated', 'new_energy': user.energy})
    return Response({'error': 'Not a correct energy'}, status=status.HTTP_400_BAD_REQUEST)
