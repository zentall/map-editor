from django.db import models
import uuid


class MapSource(models.Model):
    name = models.CharField(max_length=255, unique=True, default=uuid.uuid4)
    description = models.CharField(max_length=255, null=True, blank=True)
    options = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


class MapLayer(models.Model):
    name = models.CharField(max_length=255, unique=True, default=uuid.uuid4)
    description = models.CharField(max_length=255, null=True, blank=True)
    options = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name


class MapPage(models.Model):
    id = models.UUIDField(
        primary_key=True,  # 主キーとして使用
        default=uuid.uuid4,  # デフォルトでUUIDを生成
    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)
    options = models.JSONField()
    sources = models.ManyToManyField(MapSource, related_name="maps")
    layers = models.ManyToManyField(MapLayer, related_name="maps")

    def __str__(self):
        return self.name
