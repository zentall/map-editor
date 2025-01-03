from django import forms
from django_admin_json_editor import JSONEditorWidget
from .models import *


class MapPageAdminForm(forms.ModelForm):
    class Meta:
        model = MapPage
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.dynamic_schema(None))
        self.fields["options"].widget = JSONEditorWidget(self.dynamic_schema, False)

    def dynamic_schema(self, widget):
        return {
            "type": "object",
            "properties": {
                "container": {
                    "type": "string",
                    "template": "map",
                },
                # "style": {
                #     "type": "object",
                #     "properties": {
                #         "layers": {
                #             "type": "array",
                #             "uniqueItems": True,
                #             "items": {
                #                 "title": "Layer",
                #                 "type": "object",
                #                 "enum": [layer.options for layer in layers],
                #                 "options": {
                #                     "enum_titles": [layer.name for layer in layers],
                #                 },
                #             },
                #         },
                #         "sources": {
                #             "type": "object",
                #             "default": {
                #                 source.name: source.options for source in sources
                #             },
                #             "options": {"collapsed": True},
                #         },
                #     },
                #     "required": ["layers", "sources"],
                # },
            },
            "required": ["container"],
        }


class MapSourceAdminForm(forms.ModelForm):
    class Meta:
        """
        https://maplibre.org/maplibre-style-spec/sources/
        """

        model = MapSource
        DATA_SCHEMA = {
            "title": "MapSource",
            "oneOf": [
                {
                    "title": "None",
                    "type": "object",
                    "properties": {
                        "type": {
                            "type": "string",
                            "enum": ["none"],
                            "options": {"hidden": True},
                        }
                    },
                    "required": ["type"],
                },
                {
                    "title": "vector",
                    "type": "object",
                    "format": "grid",
                    "properties": {
                        "type": {
                            "type": "string",
                            "enum": ["vector"],
                            "options": {"hidden": True},
                        },
                        "url": {"type": "string"},
                        "tiles": {"type": "array", "items": {"type": "string"}},
                        "bounds": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "scheme": {
                            "type": "string",
                            "enum": ["xyz", "tms"],
                        },
                        "minzoom": {"type": "number"},
                        "maxzoom": {"type": "number"},
                        "attribution": {"type": "string"},
                        "promoteId": {"type": "string"},
                        "volatile": {"type": "boolean"},
                    },
                    "required": [
                        "type",
                    ],
                    "options": {
                        "disable_collapse": True,
                    },
                },
                {
                    "title": "raster",
                    "type": "object",
                    "format": "grid",
                    "properties": {
                        "type": {
                            "type": "string",
                            "enum": ["raster"],
                            "options": {"hidden": True},
                        },
                        "url": {"type": "string"},
                        "tiles": {"type": "array", "items": {"type": "string"}},
                        "bounds": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "minzoom": {"type": "number"},
                        "maxzoom": {"type": "number"},
                        "tileSize": {"type": "number"},
                        "scheme": {
                            "type": "string",
                            "enum": ["xyz", "tms"],
                        },
                        "attribution": {"type": "string"},
                        "volatile": {"type": "boolean"},
                    },
                    "required": [
                        "type",
                    ],
                    "options": {
                        "disable_collapse": True,
                    },
                },
            ],
        }
        widgets = {
            "options": JSONEditorWidget(DATA_SCHEMA, collapsed=False),
        }
        fields = "__all__"


class MapLayerAdminForm(forms.ModelForm):
    class Meta:
        model = MapLayer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["options"].widget = JSONEditorWidget(self.dynamic_schema, False)

    def dynamic_schema(self, widget):
        return {
            "type": "object",
            "properties": {
                "id": {
                    "title": "id",
                    "type": "string",
                },
                "source": {
                    "type": "string",
                    "enum": [
                        source
                        for source in MapSource.objects.values_list("name", flat=True)
                    ],
                },
            },
            "required": ["id", "source"],
        }
