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
        user_res = request.data.get("UserAnswer")
        print(user_res)
        for x in user_res:
            subject = x
        print(subject)
        ai = Evaluate(subject)




        # # for i in subject["DBMS"]:
        # #     print(subject["DBMS"][i])

        prompt=ai.generate_prompt(user_res)
        print(prompt)
        # scores=ai.extraction(x:=ai.generate_chat_response(prompt))
        # print(x)
        # print(ai.jsonify(scores))

        # return Response({"scores":ai.jsonify(scores)})
        # return Response(ai.generate_prompt("DBMS",subject))
        return Response({"message":"HI"})

