from django.shortcuts import render


def home(request):
    integrantes = [
        {'nombre': 'Maicol Aracena', 'url': '/cv/maicol/'},
        {'nombre': 'Christian Salazar', 'url': '/cv/christian/'},
        {'nombre': 'Joaquin Michea', 'url': '/cv/joaquin/'},
    ]
    return render(request, 'home.html', {'integrantes': integrantes})
