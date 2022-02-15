'''
Django SECRET_KEY generator.
'''

from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvexyz0123456789!@#$%^&*(-_=+)'
print(get_random_string(50, chars))
