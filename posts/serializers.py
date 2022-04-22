# -*- coding: utf-8 -*-
from rest_framework.serializers import ModelSerializer



from posts.apps import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post
        read_only_fields = ('owner',)
        exclude = []
