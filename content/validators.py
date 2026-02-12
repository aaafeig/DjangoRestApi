import re
from rest_framework import serializers


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, attrs):
        link = attrs.get(self.field)

        if link and "youtube.com" not in link and "youtu.be" not in link:
            raise serializers.ValidationError(
                {self.field: "Разрешены только ссылки на YouTube"}
            )

