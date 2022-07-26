from dataclasses import dataclass
from unittest import TestCase
from django.test import SimpleTestCase
from django.test.client import Client
from django.urls import reverse


class CalculatorTestCase(SimpleTestCase):
    """
    

    Args:
        TestCase (_type_): _description_
    """
    
    def setUp(self):
        self.client = Client()
        self.url = reverse('calculator:calculator')

    
    def test_view_success(self):
       
        
        data = {
            'first_number':3,
            'operation': '+',
            'second_number':4
        }
        resp = self.client.get(self.url, data=data)
        self.assertContains(resp, '<strong>7</strong>')
        self.assertContains(resp, 'El resultado es')
        
    def test_view_error(self):
        
        
        data = {
            'first_number':3,
            'operation': '/',
            'second_number':0
        }
        resp = self.client.get(self.url, data=data)
        self.assertContains(resp, '<strong>Inténtalo de nuevo.</strong>')
        
        