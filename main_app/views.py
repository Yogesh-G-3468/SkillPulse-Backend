from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .eval_module import Evaluate
import openai
# Create your views here.


class Greeting(APIView):

    def get(self,request):
        user = request.user.id
        return Response({"message":"HI {}".format(user)})
    
class GetUserAnswers(APIView):

    def post(self,request):
        subject = request.data.get("UserAnswer")
        print(subject)
        ai = Evaluate()

        # for i in subject["DBMS"]:
        #     print(subject["DBMS"][i])

        prompt=ai.generate_prompt("DBMS",subject)
        scores=ai.extraction(x:=ai.generate_chat_response(prompt))
        print(x)
        print(ai.jsonify(scores))

        print(prompt)
        return Response({"scores":ai.jsonify(scores)})
        #return Response(ai.generate_prompt("DBMS",subject))

