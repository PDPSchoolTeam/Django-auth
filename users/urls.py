from django.urls import path
from users.views import RegisterView, LoginView, IndexView

urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('', IndexView.as_view(), name="index")
]
