from django.urls import path

from .views import Greeting,GetUserAnswers
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('greeting/',Greeting.as_view(),name='greeting'),
    path('GetRating/',GetUserAnswers.as_view(),name='GetRating'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
]

