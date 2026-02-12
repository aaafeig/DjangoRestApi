import re
from rest_framework import serializers


class LinkValidator:

    def __init__(self, field):
        self.field = field

    def __caLL__(self, link):
        if not re.match(r"^https?://youtu.be", link):
            raise serializers.ValidationError("Ссылки могут быть только с youtube")