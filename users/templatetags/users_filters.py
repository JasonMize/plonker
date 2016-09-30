from django import template
import hashlib


register = template.Library()


def hashify (value):
    lowercase_value = value.lower()
    no_whitespace_value = "".join(lowercase_value.split())
    
    m = hashlib.md5()
    m.update(no_whitespace_value.encode('utf-8'))

    return m.hexdigest()

register.filter('hashify', hashify)

