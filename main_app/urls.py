from django.urls import path

from .views import Greeting,GetUserAnswers,RegisterNewUser,TestHistory,TestMark
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('greeting/',Greeting.as_view(),name='greeting'),
    path('GetRating/',GetUserAnswers.as_view(),name='GetRating'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
    path('register-user/',RegisterNewUser.as_view(),name='register-user'),
    path('dbaccess/get-total-marks/',TestHistory.as_view(),name='get-total-marks'),
    path('dbaccess/get-test-mark/',TestMark.as_view(),name='get-total-marks'),
]

