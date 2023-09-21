from django.urls import path

from .views import Greeting,GetUserAnswers,RegisterNewUser,TestHistory,TestMark,RatingRetrive,ResourcesRetreive,SeniorData,GetScoreboard,GetUserAnswersmcq
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('greeting/',Greeting.as_view(),name='greeting'),
    path('GetRating/',GetUserAnswers.as_view(),name='GetRating'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register-user/',RegisterNewUser.as_view(),name='register-user'),
    path('dbaccess/get-total-marks/',TestHistory.as_view(),name='get-total-marks'),
    path('dbaccess/get-test-mark/',TestMark.as_view(),name='get-test-marks'),
    path('dbaccess/get-test-rating/',RatingRetrive.as_view(),name='get-test-rating'),
    path('dbaccess/get-resources/',ResourcesRetreive.as_view(),name='get-resources'),
    path('dbaccess/get-seniordata/',SeniorData.as_view(),name='get-seniordata'),
    path('dbaccess/get-scoreboard/',GetScoreboard.as_view(),name='get-scoreboard'),
    path('GetMcqRating/',GetUserAnswersmcq.as_view(),name='GetMcqRating'),
]


