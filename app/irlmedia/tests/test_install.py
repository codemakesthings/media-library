from django.conf import settings


def test_django_settings_load():
    assert settings.configured
    assert settings.SECRET_KEY
