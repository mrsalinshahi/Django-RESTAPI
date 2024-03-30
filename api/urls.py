from django.urls import path
from .views import *
urlpatterns = [
 path('student', StudentAPI.as_view()),
 # path('student', get_student),
 # path('student/create', create_student),
 # path('student/update/<id>', update_student),
 # path('student/delete/<id>', delete_student),
 path('book', get_book),
]
