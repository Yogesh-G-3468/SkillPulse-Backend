from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .chatgpt import AIresponse
import openai
# Create your views here.


class Greeting(APIView):

    def get(self,request):
        return Response({"message":"end point working fine"})
    
class GetUserAnswers(APIView):

    def post(self,request):
        subject = request.data.get("UserAnswer")
        print(subject[0])
        ai = AIresponse()

        prompt=ai.generate_prompt("DBMS",subject[0])
        scores=ai.extraction(ai.generate_chat_response(prompt))
        print(ai.jsonify(scores))

        print(prompt)
        return Response({"scores":ai.jsonify(scores)})