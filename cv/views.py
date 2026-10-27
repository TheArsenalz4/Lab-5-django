from django.shortcuts import render


def home(request):
    integrantes = [
        {'nombre': 'Maicol Aracena', 'url': '/cv/maicol/'},
        {'nombre': 'Christian Salazar', 'url': '/cv/christian/'},
        {'nombre': 'Joaquin Michea', 'url': '/cv/joaquin/'},
    ]
    return render(request, 'home.html', {'integrantes': integrantes})


def cv_ejemplo(request):
    contexto = {
        'nombre': 'Ana Pérez',
        'titulo': 'Ingeniera en Informática',
        'contacto': {
            'email': 'ana.perez@ejemplo.cl',
            'telefono': '+56 9 1234 5678',
            'github': 'github.com/anaperez',
        },
        'habilidades': ['Python', 'Django', 'HTML y CSS', 'Git y GitHub', 'SQL'],
        'experiencia': [
            {
                'cargo': 'Desarrolladora web',
                'lugar': 'Empresa Ejemplo S.A.',
                'periodo': '2024 - 2025',
                'descripcion': 'Desarrollo de un sistema web para la gestión de turnos de atención.',
            },
            {
                'cargo': 'Practicante de desarrollo',
                'lugar': 'Universidad Ejemplo',
                'periodo': '2023',
                'descripcion': 'Apoyo en el mantenimiento del sitio web institucional.',
            },
        ],
    }
    return render(request, 'cv/cv_ejemplo.html', contexto)
