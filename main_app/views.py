from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response

# Create your views here.


class Greeting(APIView):

    def get(self, request):
        return Response({"message":"end point working fine"})


