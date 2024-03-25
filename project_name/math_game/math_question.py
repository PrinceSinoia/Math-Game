from django.shortcuts import render
from django.http import HttpResponseServerError
from .math_question import generate_math_question

def math_game(request):
    try:
        level = int(request.GET.get('level', 1))
        if level not in [1, 2, 3]:
            raise ValueError('Invalid level')
        question = generate_math_question(level)
    except ValueError as e:
        return HttpResponseServerError(str(e))
    return render(request, 'math_game.html', {'question': question})