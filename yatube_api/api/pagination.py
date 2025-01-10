from rest_framework.pagination import PageNumberPagination

from django.conf import settings


class PostPagination(PageNumberPagination):
    page_size = settings.PAGE_SIZE