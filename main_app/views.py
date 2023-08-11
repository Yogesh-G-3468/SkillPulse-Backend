from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
import openai
# Create your views here.


class Greeting(APIView):

    def get(self,request):
        return Response({"message":"end point working fine"})
    
class GetUserAnswers(APIView):

    def post(self,request):
        subject = request.data.get("UserAnswer")
        print(type(subject))
        chatgptsend = "theese are the question i need answer for \n subject:DBMS "

        print(subject[0])

        for x in subject[0]:
            topic = "\n topic: " + x + "\n"
            chatgptsend += topic
            print(x)

        for y in subject[0][x]:
            for questions in y:
                question = "topic: " + questions + "\n"
                chatgptsend += question
                
                for z in y[questions]:
                    print(z)
                    chatgptsend += z + "\n"

        openai.my_api_key = 'YOUR_API_KEY'
        response = openai.ChatCompletion.create(model="get-3.5-turbo",messages=chatgptsend)


        print(chatgptsend)
        return Response({"query":chatgptsend})

class NewYogesh(APIView):

    def get(self,request):
        return Response({"message":"I am yogesh"})

