from django.urls import path
from .views import TovarGet, TovarRetrieve

urlpatterns = [
    path('', TovarGet.as_view(), name='home'),
    path('tovar/<int:pk>/', TovarRetrieve.as_view(), name='home'),
    path('del/<int:pk>/', TovarRetrieve.as_view(), name='home')
]
