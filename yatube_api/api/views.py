"""
Модуль, содержащий viewsets для работы с моделями постов, групп,
комментариев и подписок.

Этот модуль определяет viewsets, которые обрабатывают запросы API для
моделей Post, Group, Comment и Follow.
"""

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins, filters, permissions
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, FollowSerializer, \
    CommentSerializer, GroupSerializer
from posts.models import Post, Comment, Follow, Group


class PostViewSet(viewsets.ModelViewSet):
    """
    Представление для модели Post.

    Поддерживает все операции CRUD. Доступ к созданию и редактированию постов
    ограничен автором поста.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Сохраняет новый пост с текущим пользователем в качестве автора."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Представление для модели Group.

    Поддерживает только операции чтения. Доступ к группам ограничен анонимными
    и аутентифицированными пользователями.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    """
    Представление для модели Comment.

    Поддерживает все операции CRUD. Доступ к созданию и редактированию
    комментариев ограничен автором комментария. Комментарии связаны
    с конкретным постом.
    """
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        new_queryset = Comment.objects.filter(post=post)
        return new_queryset

    def perform_create(self, serializer):
        """Сохраняет новый комментарий с текущим пользователем
        и связывает его с постом."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    """
    Представление для модели Follow.

    Поддерживает создание и получение подписок. Доступ к созданию подписок
    ограничен аутентифицированными пользователями.
    """
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        new_queryset = Follow.objects.filter(user=self.request.user)
        return new_queryset

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
