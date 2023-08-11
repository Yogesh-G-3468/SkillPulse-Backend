from django.urls import path

from .views import Greeting,GetUserAnswers,NewYogesh

urlpatterns = [
    path('greeting/',Greeting.as_view(),name='greeting'),
    path('GetRating/',GetUserAnswers.as_view(),name='GetRating'),
    path('NewYogesh/',NewYogesh.as_view(),name='NewYogesh'),
]

