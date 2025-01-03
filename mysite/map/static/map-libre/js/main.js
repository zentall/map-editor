const protocol = new pmtiles.Protocol();
maplibregl.addProtocol("pmtiles", protocol.tile);

const map_options = JSON.parse(document.getElementById('map_options').textContent);
const map = new maplibregl.Map(map_options);