from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import KazakhTest
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
