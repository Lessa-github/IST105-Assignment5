from django.shortcuts import render
from .forms import PuzzleForm
import math
import random

def puzzle_view(request):
    if request.method == 'POST':
        form = PuzzleForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            text = form.cleaned_data['text']

            if number % 2 == 0:
                num_type = "even"
                num_value = math.sqrt(number)
            else:
                num_type = "odd"
                num_value = number ** 3

            number_result = f"The number {number} is {num_type}. Its {'square root' if num_type == 'even' else 'cube'} is {num_value:.2f}."

            binary_text = ' '.join(format(ord(c), '08b') for c in text)
            vowel_count = sum(1 for c in text.lower() if c in 'aeiou')

            secret_number = random.randint(1, 100)
            attempts = []
            found = False
            for i in range(1, 6):
                guess = random.randint(1, 100)
                if guess > secret_number:
                    attempts.append(f"Attempt {i}: {guess} (Too high!)")
                elif guess < secret_number:
                    attempts.append(f"Attempt {i}: {guess} (Too low!)")
                else:
                    attempts.append(f"Attempt {i}: {guess} (Correct!)")
                    found = True
                    break

            treasure_result = f"You found the treasure in {i} attempts!" if found else "Failed to find the treasure in 5 attempts."

            context = {
                'form': form,
                'results': {
                    'number_puzzle': number_result,
                    'binary_text': binary_text,
                    'vowel_count': vowel_count,
                    'treasure_hunt_secret': f"The secret number is {secret_number}.",
                    'treasure_hunt_log': attempts,
                    'treasure_hunt_result': treasure_result,
                }
            }
            return render(request, 'puzzle/puzzle_form.html', context)
    else:
        form = PuzzleForm()
    return render(request, 'puzzle/puzzle_form.html', {'form': form})
