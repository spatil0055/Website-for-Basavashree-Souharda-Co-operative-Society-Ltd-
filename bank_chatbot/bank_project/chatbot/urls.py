from django.urls import path
from .views import chatbot_api, chatbot_page

urlpatterns = [
    path("", chatbot_page, name="chatbot_page"),
    path("chatbot-api/", chatbot_api, name="chatbot_api"),
]
