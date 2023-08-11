from django.urls import path

from .views import Greeting,GetUserAnswers

urlpatterns = [
    path('greeting/',Greeting.as_view(),name='greeting'),
    path('GetRating/',GetUserAnswers.as_view(),name='GetRating'),
]

