from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)

class LanguageLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 5

class LanguagePageNumberPagination(PageNumberPagination):
    page_size = 2