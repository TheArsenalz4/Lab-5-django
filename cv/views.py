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


def cv_christian(request):
    contexto = {
        'nombre': 'Christian Salazar',
        'titulo': 'Ingeniería Civil en Computación e Informática',
        'contacto': {
            'email': 'christian.salazars@alumnos.ucentral.cl',
            'telefono': '+56 9 8821 4469',
            'github': 'github.com/TheArsenalz4',
        },
        'habilidades': [
            'React',
            'TypeScript',
            'Desarrollo de software',
            'Metodología ágil',
            'Kotlin',
            'Python',
        ],
        'experiencia': [
            {
                'cargo': 'Reflexia',
                'descripcion': 'Potenciar el pensamiento en el aula con IA.',
            },
            {
                'cargo': 'Orquesta Prisma',
                'descripcion': 'Organizador de partituras de orquesta.',
            },
            {
                'cargo': 'Turnero UCEN',
                'descripcion': 'Remodelado del sistema de turnos de la UCEN para matrículas.',
            },
        ],
    }
    return render(request, 'cv/cv_christian.html', contexto)
def cv_maicol(request):
    contexto = {
        'nombre': 'Maicol Aracena',
        'titulo': 'Desarrollador web',
        'contacto': {
            'email': 'maicol.aracena@alumnos.ucentral.cl',
            'telefono': '+56 9 6503 1148',
            'github': 'github.com/bladingg',
        },
        'habilidades': [
            'PHP',
            'MySQL',
            'JavaScript',
            'HTML5 y CSS',
            'React y TypeScript',
            'Arquitectura MVC',
            'Git y GitHub',
        ],
        'experiencia': [
            {
                'cargo': 'Desarrollador del sistema Turnero Ucen',
                'lugar': 'Universidad Central (Sede Coquimbo)',
                'periodo': 'Práctica Operacional',
                'descripcion': 'Sistema web de gestión de filas, desarrollado junto a Christian Salazar '
                               'para controlar el flujo de personas en los procesos de Admisión y Matrículas.',
            },
            {
                'cargo': 'Desarrollador del Sistema de Gestión Académica',
                'lugar': 'Liceo José Santos Ossa',
                'periodo': '2024',
                'descripcion': 'Sistema web para administrar el ciclo escolar: matrícula, notas, asistencia '
                               'y apoderados. Base de datos MySQL de 15 tablas con vistas, triggers y auditoría.',
            },
        ],
    }
    return render(request, 'cv/cv_maicol.html', contexto)
