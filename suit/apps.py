"""Django Application configuration."""
from django.apps import AppConfig

__all__ = ['SuitConfig']


class SuitConfig(AppConfig):
    """Default configuration for django-suit app."""

    name = 'suit'
    label = 'suit'
    verbose_name = 'suit'
