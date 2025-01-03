from django.core.management.base import BaseCommand
from django.db import transaction

from map.models import (
    MapSource,
    MapLayer,
    MapPage,
)


class Command(BaseCommand):
    help = "Load sample data into the database."

    def handle(self, *args, **kwargs):
        with transaction.atomic(using="default"):
            sources = [
                MapSource.objects.get_or_create(
                    name="shibuya-geojson-sample",
                    options={
                        "type": "geojson",
                        "data": "/static/example/shibuya.geojson",
                    },
                ),
                MapSource.objects.get_or_create(
                    name="osm-raster",
                    options={
                        "type": "raster",
                        "tiles": [
                            "https://tile.openstreetmap.jp/styles/osm-bright-ja/{z}/{x}/{y}.png"
                        ],
                        "tileSize": 256,
                        "attribution": "<a href='https://www.openstreetmap.org/copyright' target='_blank'>© OpenStreetMap contributors</a>",
                    },
                ),
            ]

            layers = [
                MapLayer.objects.get_or_create(
                    name="background-osm-raster",
                    options={
                        "id": "background-osm-raster",
                        "source": "osm-raster",
                        "type": "raster",
                    },
                ),
                MapLayer.objects.get_or_create(
                    name="geojson-shibuya-polygon",
                    options={
                        "id": "maine",
                        "source": "shibuya-geojson-sample",
                        "type": "fill",
                        "paint": {"fill-color": "#088", "fill-opacity": 0.8},
                    },
                ),
                MapLayer.objects.get_or_create(
                    name="geojson-shibuya-point",
                    options={
                        "id": "geojson-shibuya-point",
                        "source": "shibuya-geojson-sample",
                        "type": "circle",
                        "paint": {"circle-color": "#F0F"},
                    },
                ),
            ]

            map_page, _ = MapPage.objects.get_or_create(
                name="sample-map",
                options={"container": "map", "center": [139.7024, 35.6598], "zoom": 16},
            )

            map_page.sources.set([source for (source, _) in sources])
            map_page.layers.set([layer for (layer, _) in layers])
            map_page.save()

        print("Successfully map created.")
        print("1. Run deveropment server: python manage.py runserver 0.0.0.0:8000")
        print(f"2. Open your map: http://localhost:8000/map/{map_page.id}")
