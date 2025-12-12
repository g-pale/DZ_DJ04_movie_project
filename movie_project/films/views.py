from django.shortcuts import render, redirect
from .models import Film


def home(request):
    return redirect('films_list')


def add_film(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        review = request.POST.get('review')
        
        if title and description and review:
            Film.objects.create(
                title=title,
                description=description,
                review=review
            )
            return redirect('films_list')
    
    return render(request, 'films/add_films.html')


def films_list(request):
    films = Film.objects.all()
    return render(request, 'films/films.html', {'films': films})
