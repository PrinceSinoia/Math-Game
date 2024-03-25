from django.http import JsonResponse
import random

def math_question_view(request, level=None):
    if level is None:
        # Handle the case when level is not provided
        return JsonResponse({'error': 'Level not specified'})

    # Generate a random math question based on the level
    if level == 1:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        question = f"What is {num1} + {num2}?"
        answer = num1 + num2
    elif level == 2:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, num1)
        question = f"What is {num1} - {num2}?"
        answer = num1 - num2
    else:
        return JsonResponse({'error': 'Invalid level'})

    # Return the question and possible answers as a JSON response
    return JsonResponse({
        'question': question,
        'answers': [answer],
        'fetchedAnswer': str(answer).strip('.'),
    })

