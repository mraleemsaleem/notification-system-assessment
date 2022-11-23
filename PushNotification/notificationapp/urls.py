from django.urls import path, include
from .import views



urlpatterns = [
    path('submit-form/', views.SubmitForm.as_view(), name='submit-form'),
    path('get-logs/', views.GetLogs.as_view(), name='get-logs'),
    path('get-logs/<int:id>', views.GetLogs.as_view(), name='get-logs'),
]