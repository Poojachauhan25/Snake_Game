from django.shortcuts import render

# Create your views here.
from .models import HighScore

def snake_game(request):
    return render(request, 'game/snake_game.html')

def save_score(request):
    if request.method == 'POST':
        player_name = request.POST.get('player_name')
        score = int(request.POST.get('score'))
        HighScore.objects.create(player_name=player_name, score=score)
        return JsonResponse({'message': 'Score saved successfully!'})
