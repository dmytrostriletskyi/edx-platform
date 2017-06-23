"""
Django admin page for edX global analytics application.
"""

from django.contrib import admin

from .models import TokenStorage


class TokenStorageAdmin(admin.ModelAdmin):
    """
    Admin for access tokens storage.
    """
    fields = ['secret_token']

admin.site.register(TokenStorage, TokenStorageAdmin)
