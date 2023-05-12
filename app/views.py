from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from app.models import RobotCategory, Manufacturer, Robot
from app.serializers import RobotCategorySerializer, ManufacturerSerializer, RobotSerializer
from rest_framework import generics


# class ApiRoot(generics.GenericAPIView):
#     name = 'api-root'
#     def get(self, request, *args, **kwargs):
#         return Response({
#             'robot-categories': reverse(RobotCategoryList.name, request=request),
#             'manufacturers': reverse(ManufacturerList.name, request=request),
#             'robots': reverse(RobotList.name, request=request),
#         })


class RobotCategoryList(generics.ListCreateAPIView):
    queryset = RobotCategory.objects.all()
    serializer_class = RobotCategorySerializer


class RobotCategoryUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = RobotCategory.objects.all()
    serializer_class = RobotCategorySerializer


class ManufacturerList(generics.ListCreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ManufacturerUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class RobotList(generics.ListCreateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer
