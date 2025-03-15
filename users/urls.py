from django.urls import path
from users.views import RegisterView, LoginView, IndexView,send_mail_page

urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('login', LoginView.as_view(), name="login"),
    path('email',send_mail_page,name='email'),
    path('', IndexView.as_view(), name="index"),
]
