# Lab-5-django · Sitio de CVs del grupo

Laboratorio 5 de **Programación de Aplicaciones** (Unidad III, Backend).

Es un sitio Django monolítico en el que el servidor renderiza las páginas HTML con vistas y templates. Tiene una página de inicio y un CV por integrante. No usa base de datos: los datos de cada persona están en su propia vista y llegan al template a través del contexto.

## Integrantes

| Integrante        | Ruta              |
|-------------------|-------------------|
| Maicol Aracena    | `/cv/maicol/`     |
| Christian Salazar | `/cv/christian/`  |
| Joaquín Michea    | `/cv/joaquin/`    |

También está `/cv/ejemplo/`, un CV con datos ficticios que hicimos entre todos para dejar definido el patrón que siguió cada integrante.

## Qué se hizo

1. **Proyecto base:** creamos el proyecto `sitio_cv` y la app `cv`, que quedó registrada en `INSTALLED_APPS`.
2. **Plantilla base compartida:** `templates/base.html` tiene el encabezado, la navegación y el pie de página, con un `{% block content %}` para el contenido de cada página. Todas las páginas extienden esta plantilla, así que el sitio se ve igual en todas partes.
3. **Inicio:** la vista `home` le pasa la lista de integrantes a `home.html`, que muestra un enlace al CV de cada uno.
4. **CV de ejemplo:** la vista `cv_ejemplo` arma un diccionario con nombre, título, contacto, habilidades y experiencia. El template muestra los datos simples con `{{ }}` y recorre las listas con `{% for %}`.
5. **CV por integrante:** cada integrante trabajó en su propia rama (`cv-nombre`), con su vista, su template y su ruta. Después se integró a `main` mediante un Pull Request.

## Estructura

```
sitio_cv/          # Configuración del proyecto (settings, urls raíz)
cv/
  views.py         # home + una vista por CV, con los datos en el contexto
  urls.py          # Rutas de la app
templates/
  base.html        # Plantilla base compartida
  home.html        # Página de inicio
  cv/              # Un template por CV (extienden base.html)
```

## Cómo ejecutarlo

Requisitos: Python 3.12 o superior (Django 6.1).

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Luego abre http://127.0.0.1:8000/.

## Decisiones técnicas

- **Datos en el contexto, no en el HTML:** los templates solo muestran los datos. Toda la información viene de la vista, que es lo que pide la pauta.
- **Un template por integrante:** así cada persona trabaja en sus propios archivos y hay menos conflictos de merge. El único archivo compartido que cambiaron todos es `home.html`.
- **Sin modelos por ahora:** el objetivo es practicar el paso de datos de la vista al template. Pasar los datos a modelos y a la base de datos sería el siguiente paso natural.
