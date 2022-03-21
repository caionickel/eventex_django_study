from django.test import TestCase
from django.core import mail
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Caio Nickel', cpf='12345678901',
                    email='caio.nickel@gmail.com', phone='43-99682-5355')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de Inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'caio.nickel@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Caio Nickel',
            '12345678901',
            'caio.nickel@gmail.com',
            '43-99682-5355',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)

