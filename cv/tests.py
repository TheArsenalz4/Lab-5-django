from django.test import TestCase
from django.urls import reverse


class CvMaicolTests(TestCase):
    def test_pagina_responde_y_usa_las_plantillas(self):
        respuesta = self.client.get(reverse('cv_maicol'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertTemplateUsed(respuesta, 'cv/cv_maicol.html')
        self.assertTemplateUsed(respuesta, 'base.html')

    def test_contexto_trae_los_datos_del_cv(self):
        respuesta = self.client.get(reverse('cv_maicol'))
        for clave in ('nombre', 'titulo', 'contacto', 'habilidades', 'experiencia'):
            self.assertIn(clave, respuesta.context)
        self.assertEqual(respuesta.context['nombre'], 'Maicol Aracena')

    def test_pagina_muestra_habilidades_y_experiencia(self):
        respuesta = self.client.get(reverse('cv_maicol'))
        for habilidad in respuesta.context['habilidades']:
            self.assertContains(respuesta, habilidad)
        for item in respuesta.context['experiencia']:
            self.assertContains(respuesta, item['cargo'])

    def test_inicio_enlaza_al_cv(self):
        respuesta = self.client.get(reverse('home'))
        self.assertContains(respuesta, reverse('cv_maicol'))
