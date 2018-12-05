from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer
from .pagination import LanguageLimitOffsetPagination, LanguagePageNumberPagination


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    pagination_class = LanguagePageNumberPagination
