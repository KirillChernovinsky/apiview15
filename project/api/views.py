from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MealSerializer
from .models import Meal, Ingredients
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView


class MealGetList(ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MealOne(RetrieveUpdateDestroyAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer





class MealGet(APIView):
    def get(self, request):
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        # new_meal = Meal.objects.create(
        #     title = request.data['title'],
        #     description = request.data['description'],
        #     price = request.data['price'],
        # )
        # serializer = MealSerializer(new_meal)
        # return Response('My post request')

        serializer = MealSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data':serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')

        try:
            meal = Meal.objects.get(pk=pk)

        except:
            return Response('Meal is no exist')

        serializer = MealSerializer(data=request.data, instance=meal)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})

    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk', None)
    #     if pk is None:
    #         return Response('Not pk')
    #
    #     try:
    #