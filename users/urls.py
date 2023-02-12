from .views import UserCreateView, LoginView, UserRetriveView, UserDeactiveView, UserUpdatedView
from django.urls import path

urlpatterns = [
    path("login/", LoginView.as_view()),
    path("users/", UserCreateView.as_view()),
    path("users/<pk>/", UserRetriveView.as_view()),
    path("users/<pk>/update", UserUpdatedView.as_view()),
    path("users/<pk>/deactive", UserDeactiveView.as_view()),
]   
