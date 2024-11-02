from django.urls import path
from .views import *

urlpatterns = [
    path('category-list/', category_list, name='category-list'),
    path('category-add/', category_create, name='category-add'),
    path('category/<int:pk>/edit/', category_update, name='category-update'),
    path('category/<int:pk>/delete/', category_delete, name='category-delete'),

    path('user-list/', user_list, name='user-list'),
    path('user-add/', user_create, name='user-add'),
    path('user/<int:pk>/edit/', user_update, name='user-update'),
    path('user/<int:pk>/delete/', user_delete, name='user-delete'),

    path('questions/', question_list, name='question-list'),
    path('questions/<int:pk>/', question_list, name='question-detail'),
    path('questions/add/', question_create, name='question-add'),
    path('questions/<int:pk>/edit/', question_update, name='question-update'),  
    path('questions/<int:pk>/delete/', question_delete, name='question-delete'),
    
    path('answer-list/', answer_list, name='answer-list'),
    path('answer-add/', answer_create, name='answer-add'),
    path('answer/<int:pk>/edit/', answer_update, name='answer-update'),
    path('answer/<int:pk>/delete/', answer_delete, name='answer-delete'),
]
