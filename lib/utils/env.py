import os


def is_dev():
    return os.getenv("DJANGO_ENV", "development") == "development"


def is_prod():
    return os.getenv("DJANGO_ENV") == "production"
