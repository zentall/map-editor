from django.shortcuts import render
from .models import MapPage


# Create your views here.
def map(request):
    context = {}
    return render(request, "map/index.html", context)


def libre(request, map_id):
    map = MapPage.objects.get(id=map_id)
    map_options = {
        "style": {
            "version": 8,
            "sources": {source.name: source.options for source in map.sources.all()},
            "layers": list(map.layers.values_list("options", flat=True)),
        },
        **map.options,
    }

    context = {"map": map, "map_options": map_options}
    return render(request, "map-libre/index.html", context)


def bo(request):
    context = {"request": "ok"}
    return render(request, "bo/index.html", context)
