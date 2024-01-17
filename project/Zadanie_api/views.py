from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tovar, Category, Maker
from .serializers import TovarSerializer


# Create your views here.



class TovarGet(APIView):
    def get(self, request):
        tovars = Tovar.objects.all()
        serializer = TovarSerializer(tovars, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        # new_meal = Meal.objects.create(
        #     title = request.data['title'],
        #     description = request.data['description'],
        #     price = request.data['price'],
        # )
        # serializer = MealSerializer(new_meal)
        # return Response('My post request')

        serializer = TovarSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data':serializer.data})



class TovarRetrieve(APIView):

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')

        try:
            tovar = Tovar.objects.get(pk=pk)

        except:
            return Response('Meal is no exist')
        serializer = TovarSerializer(tovar)
        return Response({'data': serializer.data})


    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')
        try:
            tovar = Tovar.objects.get(pk=pk)

        except:
            return Response('Meal is no exist')

        serializer = TovarSerializer(data=request.data, instance=tovar)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')

        try:
            tovar = Tovar.objects.get(pk=pk)

        except:
            return Response('Meal is no exist')
        tovar.delete()
        return Response('Tovar deleted')