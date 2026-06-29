from . import views
from django.urls import path

urlpatterns = [
    path('build/web-development/', views.webdev, name='web_development'),
    path('build/qr-menu/', views.qrmenu, name='qr_menu'),
    path('build/chatbots/', views.chatbots, name='chatbots'),
    path('data/data-expert-consultancy/', views.dataexpertconsultancy, name='data_expert_consultancy'),
    path('data/training/', views.training, name='training'),
    path('data/business-analytics/', views.businessanalytics, name='business_analytics'),
    path('data/automation-ai/', views.automation_ai, name='automation_ai'),
]
