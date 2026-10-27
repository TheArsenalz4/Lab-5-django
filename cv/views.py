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


def cv_joaquin(request):
    contexto = {
        'nombre': 'Joaquín Michea Michea',
        'titulo': 'Por completar: título profesional',
        'contacto': {
            'email': 'Por completar: correo',
            'telefono': 'Por completar: teléfono',
            'github': 'github.com/jimm-96',
        },
        'habilidades': ['Python', 'CustomTkinter', 'TensorFlow'],
        'experiencia': [
            {
                'cargo': 'AgenteInteligente_LentesGravitacionales',
                'descripcion': (
                    'Lens Sentinel AI es un software de escritorio diseñado para optimizar '
                    'la detección y validación de lentes gravitacionales (anillos de Einstein) '
                    'en grandes volúmenes de datos astronómicos.'
                ),
                'enlace': 'https://github.com/jimm-96/AgenteInteligente_LentesGravitacionales',
            },
        ],
    }
    return render(request, 'cv/cv_joaquin.html', contexto)
