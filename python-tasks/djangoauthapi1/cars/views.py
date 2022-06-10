from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from cars.serializers import CategoriesAddSerializer, CarAddSerializer
from account.renderers import UserRenderer
from django.http import HttpRequest, HttpResponse, JsonResponse
from cars.models import Category, Car
from rest_framework.parsers import JSONParser


class CategoryView(APIView):

    def post(self, request, format=None):
        serializer = CategoriesAddSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return HttpResponse("Record added successfully", status=200)
        return HttpResponse(serializer.errors, status=400)

    def get(self, request, format=None):
        categories = Category.objects.all().order_by('date')
        serializer = CategoriesAddSerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request):
        cat_id = request.data.get("id")
        cat = Category.objects.filter(id=cat_id)

        if cat.exists():
            if len(request.data.get("name")):
                Category.objects.filter(id=cat_id).update(name=request.data.get("name"))
                return HttpResponse("Record added successfully", status=200)
            else:
                return HttpResponse("Name must not be empty", status=402)

        else:
            return HttpResponse("No category found", status=401)

    def delete(self, request):
        cat_id = request.data.get("id")
        cat = Category.objects.filter(id=cat_id)
        if cat.exists():
            if request.data.get("id"):
                Category.objects.filter(id=cat_id).delete()
                return HttpResponse("Record deleted successfully", status=200)
            else:
                return HttpResponse("id must not be empty", status=402)

        else:
            return HttpResponse("No category found", status=401)


class CarView(APIView):

    def post(self, request, format=None):
        cat = Category.objects.filter(id=request.data.get("cat_id"))
        if cat.exists():
            serializer = CarAddSerializer(data=request.data)
        else:
            return HttpResponse("Category not found", status=401)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return HttpResponse("Record added successfully", status=200)
        return HttpResponse(serializer.errors, status=400)

    def get(self, request, format=None):
        cars = Car.objects.all().order_by('date')
        serializer = CarAddSerializer(cars, many=True)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request):
        cat_id = request.data.get("id")
        cat = Category.objects.filter(id=cat_id)

        if cat.exists():
            Car.objects.filter(id=request.data.get("id")).update(color=request.data.get("color"),
                                                                 model=request.data.get("model"),
                                                                 cat_id=request.data.get("cat_id"),
                                                                 registration_no=request.data.get("registration_no"))
            return HttpResponse("Record updated successfully", status=200)
        else:
            return HttpResponse("No car found", status=401)

    def delete(self, request):
        car_id = request.data.get("id")
        car = Car.objects.filter(id=car_id)
        if car.exists():
            if request.data.get("id"):
                Car.objects.filter(id=car_id).delete()
                return HttpResponse("Record deleted successfully", status=200)
            else:
                return HttpResponse("id must not be empty", status=402)

        else:
            return HttpResponse("No car found", status=401)
