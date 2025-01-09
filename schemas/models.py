from django.contrib.auth import get_user_model
from django.db import models


class TypeChoices(models.TextChoices):
    FULL_NAME = "full_name", "Full name"
    EMAIL = "email", "Email"
    DOMAIN_NAME = "domain_name", "Domain name"
    PHONE_NUMBER = "phone_number", "Phone number"
    COMPANY_NAME = "company_name", "Company name"
    TEXT = "text", "Text"
    INTEGER = "integer", "Integer value"
    ADDRESS = "address", "Address"
    DATE = "date", "Date"


class SeparatorChoices(models.TextChoices):
    COMMA = "comma", "Comma (,)"
    SEMICOLON = "semicolon", "Semicolon (;)"
    TAB = "tab", "Tab (\\t)"
    PIPE = "pipe", "Pipe (|)"
    SPACE = "space", "Space ( )"
    COLON = "colon", "Colon (:)"


class StringCharChoices(models.TextChoices):
    DOUBLE_QUOTE = "double_quote", "Double-quote (\")"
    SINGLE_QUOTE = "single_quote", "Single-quote(')"
    BACKTICK = "backtick", "Backtick (`)"
    SQUARE_BRACKET = "square_brackets", "Square brackets ([ ])"
    CURLY_BRACKET = "curly_brackets", "Curly brackets ({ })"
    ANGLE_BRACKET = "angle_brackets", "Angle brackets (< >)"
    PARENTHESES = "parentheses", "Parentheses (( ))"


class Schema(models.Model):
    name = models.CharField(
        max_length=255
    )
    separator = models.CharField(
        max_length=20,
        choices=SeparatorChoices,
        default=SeparatorChoices.COMMA
    )
    string_char = models.CharField(
        max_length=20,
        choices=StringCharChoices,
        default=StringCharChoices.DOUBLE_QUOTE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='schemas')
    updated_at = models.DateTimeField(auto_now=True)


class Column(models.Model):
    schema = models.ForeignKey(Schema, on_delete=models.CASCADE, related_name='columns')
    name = models.CharField(max_length=255)
    data_type = models.CharField(max_length=20, choices=TypeChoices.choices)
    order = models.IntegerField()
    extra_args = models.JSONField(blank=True, null=True)
