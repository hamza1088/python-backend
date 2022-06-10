from django.urls import path
from cars.views import CategoryView, CarView

urlpatterns = [
    path('add_category/', CategoryView.as_view(), name='add_category'),
    path('get_category/', CategoryView.as_view(), name='get_category'),
    path('update_category/', CategoryView.as_view(), name='update_category'),
    path('delete_category/', CategoryView.as_view(), name='delete_category'),
    path('add_car/', CarView.as_view(), name='add_car'),
    path('get_car/', CarView.as_view(), name='get_car'),
    path('update_car/', CarView.as_view(), name='update_car'),
    path('delete_car/', CarView.as_view(), name='delete_car')
]