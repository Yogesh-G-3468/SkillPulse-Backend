from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .eval_module import Evaluate
from .DATA import TestModulesHistory,TestTotalMarks
from .mongo import MongoInsertTest,MongoInsertTotalMark,MongoRetirveTest,MongoRetirveTotalMarks
# Create your views here.



class RegisterNewUser(APIView):
    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")

        if password is None or email is None:
            return Response({"message":"Please provide all the details"})
        
        try:
            user = User.objects.create_user(username=email,password=password)
            user.save()

            new_user_test_modeule = {
                "user_id":email,
                "scores":TestModulesHistory,
            }

            new_user_total_marks = {
                "user_id":email,
                "scores":TestTotalMarks,
            }

            MongoInsertTest(new_user_test_modeule)
            MongoInsertTotalMark(new_user_total_marks)
            print("new_user_test_modeule:",new_user_test_modeule)
            print("new_user_total_marks:",new_user_total_marks)

            return Response({"message":"User Created Successfully"})
        except Exception as e:
            print(e)
            return Response({"message":"User Already Exists"})
        

class Greeting(APIView):
    permission_classes = ( IsAuthenticated, )
    def get(self,request):
        user = request.user.username

        new_user_test_modeule = {
            "user_id":user,
            "scores":TestModulesHistory,
        }

        new_user_total_marks = {
            "user_id":user,
            "scores":TestTotalMarks,
        }

        print("new_user_test_modeule:",new_user_test_modeule)
        print("new_user_total_marks:",new_user_total_marks)
        return Response({"message":"HI {}".format(user)})
    

class TestHistory(APIView):
    permission_classes = ( IsAuthenticated, )
    def get(self,request):
        user = request.user.username
        output = MongoRetirveTest(user)
        return Response(output["scores"])
    

class TestMark(APIView):
    permission_classes = ( IsAuthenticated, )
    def get(self,request):
        user = request.user.username
        output = MongoRetirveTotalMarks(user)
        return Response(output["scores"])
    

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
        
        try:
            prompt=ai.generate_prompt(user_res)
            print(prompt)
            scores=ai.extraction(x:=ai.generate_chat_response(prompt))
            return Response({"scores":ai.jsonify(scores)})

        except Exception as e:
            print("error:",e)
            return Response({"message":"server is busy"})
        
        # print(x)
        # except Exception as e:
        #     print(e)
        #     print("server busy")
        #     return Response({"message":"Server is busy please wait"})
        # # return Response(ai.generate_prompt("DBMS",subject))
        # return Response({"message":"HI"})

