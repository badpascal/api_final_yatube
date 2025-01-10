from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth import get_user_model

from posts.models import Comment, Post, Group, Follow

User = get_user_model()


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following'),
                message='Вы уже подписаны'
            )
        ]

    def validate_following(self, following):
        request = self.context.get('request')
        user = request.user
        if user == following:
            raise serializers.ValidationError(
                {"detail": "Подписка на себя невозможна"}
            )
        return following


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
