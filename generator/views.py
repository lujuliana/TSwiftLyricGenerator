from django.shortcuts import render
from .lyric_generator import Generator
from .models import Lyric

def generate_lyric(request):
    if request.method == 'POST':
        if 'all' in request.POST:
            Lyric.objects.create(content=str(Generator('lyrics/all_lyrics.txt')))
        elif '1989' in request.POST:
            Lyric.objects.create(content=str(Generator('lyrics/1989_lyrics.txt')))
        elif 'evermore' in request.POST:
            Lyric.objects.create(content=str(Generator('lyrics/evermore_lyrics.txt')))
        elif 'fearless' in request.POST:
            Lyric.objects.create(content=str(Generator('lyrics/fearless_lyrics.txt')))
        elif 'folklore' in request.POST:
            Lyric.objects.create(content=str(Generator('lyrics/folklore_lyrics.txt')))
        elif 'lover' in request.POST:
            Lyric.objects.create(content=str(Generator('lyrics/lover_lyrics.txt')))
        elif 'red' in request.POST:
            Lyric.objects.create(content=str(Generator('lyrics/red_lyrics.txt')))
        elif 'reputation' in request.POST:
            Lyric.objects.create(content=str(Generator('lyrics/reputation_lyrics.txt')))
        elif 'speak_now' in request.POST:
            Lyric.objects.create(content=str(Generator('lyrics/speak_now_lyrics.txt')))
        elif 'taylor_swift' in request.POST:
            Lyric.objects.create(content=str(Generator('lyrics/taylor_swift_lyrics.txt')))
    return render(request, "home.html", {"lyric": Lyric.objects.last()})
