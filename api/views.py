from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import User, Meal, Food
from . serializers import UserSerializer, MealSerializer, FoodSerializer
from rest_framework import status
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def users(request):
    if (request.method == 'GET'):
        id = request.query_params.get('id')

        if id is not None:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    elif (request.method == 'POST'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def meals(request, meal_id=None):
    if request.method == 'GET':
        id = request.query_params.get('user_id')
        if id is not None:
            meals = Meal.objects.filter(user_id=id)
        else:
            meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MealSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'PUT':
        try:
            meal = Meal.objects.get(id=meal_id)
        except Meal.DoesNotExist:
            return Response(status=404)

    elif request.method == 'DELETE':
        try:
            meal = Meal.objects.get(id=meal_id)
            meal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Meal.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = MealSerializer(meal, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def foods(request, food_id=None):
    if request.method == 'GET':
        id = request.query_params.get('user_id')
        if id is not None:
            foods = Food.objects.filter(user_id=id)
            serializer = FoodSerializer(foods, many=True)
        else:
            foods = Food.objects.all()
            serializer = FoodSerializer(foods, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    elif request.method == 'PUT':
        try:
            food = Food.objects.get(id=food_id)
        except Food.DoesNotExist:
            return Response(status=404)

        serializer = FoodSerializer(food, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        try:
            food = Food.objects.get(id=food_id)
        except Food.DoesNotExist:
            return Response(status=404)

        food.delete()
        return Response(status=204)
