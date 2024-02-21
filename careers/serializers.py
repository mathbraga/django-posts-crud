from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def update(self, instance, validated_data):
        patch_fields_allowed = ['title', 'content']
        for field, value in validated_data.items():
            if field in patch_fields_allowed:
                setattr(instance, field, value)
        instance.save()
        return instance
