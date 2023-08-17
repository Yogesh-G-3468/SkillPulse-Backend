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
        

        avilable_answers = []
        for i in user_res[subject]:
            if user_res[subject][i] == "":
                continue
            else:
                avilable_answers.append(i)
        print(avilable_answers)

        ai = Evaluate(subject,avilable_answers)

        



        # # for i in subject["DBMS"]:
        # #     print(subject["DBMS"][i])

        no_scores = True
        while(no_scores):
            prompt=ai.generate_prompt(user_res)
            print(prompt)
            scores=ai.extraction(x:=ai.generate_chat_response(prompt))
            if scores:
                no_scores = False
        
        # print(x)

        return Response({"scores":ai.jsonify(scores)})
        
        # except Exception as e:
        #     print(e)
        #     print("server busy")
        #     return Response({"message":"Server is busy please wait"})
        # # return Response(ai.generate_prompt("DBMS",subject))
        # return Response({"message":"HI"})

