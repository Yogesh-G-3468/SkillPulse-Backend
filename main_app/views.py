from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .eval_module import Evaluate
from .DATA import TestModulesHistory,TestTotalMarks
from .mongo import MongoInsertTest,MongoInsertTotalMark,MongoRetirveTest,MongoRetirveTotalMarks,InsertRating,RetriveRating
import logging
import inspect
# Create your views here.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',handlers=[
        logging.StreamHandler(),
        logging.FileHandler("logs.log"),
    ],)



class RegisterNewUser(APIView):
    def post(self,request):
        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
        email = request.data.get("email")
        password = request.data.get("password")

        if password is None or email is None:
            return Response({"message":"Please provide all the details"})
        
        try:
            user = User.objects.create_user(username=email,password=password)
            user.save()
            logger.info("User {} Created Successfully".format(email))

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

            return Response({"message":"User {} Created Successfully".format(email)})
        except Exception as e:
            logging.error("User {} Already Exists".format(email))
            print(e)
            return Response({"message":"User {} Already Exists".format(email)})
        

class Greeting(APIView):
    permission_classes = ( IsAuthenticated, )
    def get(self,request):
        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
        user = request.user.username

        logger.info("User {} came in".format(user))

        return Response({"message":"HI {}".format(user)})
    

class TestHistory(APIView):
    permission_classes = ( IsAuthenticated, )
    def get(self,request):
        
        user = request.user.username
        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
        logger.info("User {} came in".format(request.user.username))
        output = MongoRetirveTest(user)
        return Response(output["scores"])
    

class TestMark(APIView):
    permission_classes = ( IsAuthenticated, )
    def get(self,request):
        
        user = request.user.username
        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
        logger.info("User {} came in".format(request.user.username))
        output = MongoRetirveTotalMarks(user)
        return Response(output["scores"])
    
class RatingRetrive(APIView):
    permission_classes = ( IsAuthenticated, )
    def get(self,request):
        
        user = request.user.username
        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
        logger.info("User {} came in".format(request.user.username))
        subject = request.data.get("subject")
        output = RetriveRating(user,subject)
        print(output)
        return Response(output["ratings"])


class GetUserAnswers(APIView):
    permission_classes = ( IsAuthenticated, )
    def post(self,request):
        logger = logging.getLogger(inspect.currentframe().f_code.co_name)
        logger.info("User {} came in".format(request.user.username))
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

        prompt=ai.generate_prompt(user_res)
        print(prompt)
        scores=ai.extraction(x:=ai.generate_chat_response(prompt))

        print("gpt generated response:",x)
        print("scores of the user:",scores)
        
        rating = ai.jsonify(scores)
        
        Indirating = {
            "user_id":request.user.username,
            "subject":subject,
            "ratings":rating
        }
        InsertRating(Indirating)

        return Response({"scores":rating})