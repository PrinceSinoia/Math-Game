from django.urls import path
from math_game.views import math_question_view

urlpatterns = [
    path('', math_question_view, name='home'),
    path('Multiplication/', math_question_view, name='multiplication'),
    path('generate-math-question/<int:level>/', math_question_view, name='generate_math_question'),
]




# from django.urls import path
# from math_game.views import math_question_view

# urlpatterns = [
#     path('', math_question_view, name='home'),  # Remove the <int:level> part
#     path('Multiplication/', math_question_view, name='multiplication'),
#     path('generate-math-question/<int:level>/', math_question_view, name='generate_math_question'),
# ]








































