# pip install leafmap folium

from leafmap import leafmap
import json
import folium

# Carrega o GeoJSON externamente
geojson_file_path = "temp.geojson"

with open(geojson_file_path, "r") as f:
    geojson_data = json.load(f)

# Cria um objeto de mapa centrado nas coordenadas do Brasil e com um zoom maior
m = folium.Map(location=[-14, -55], zoom_start=4, height="100%")

# Cria um grupo de camadas para adicionar os dados do GEDI
gedi_layer = folium.FeatureGroup(name='GEDI Observations')

# Adiciona a geometria do GeoJSON ao grupo de camadas com informações de tooltip
for feature in geojson_data["features"]:
    properties = feature["properties"]

    tooltip_info = (
        f"<strong>ID:</strong> {properties['id']}<br>"
        f"<strong>Título:</strong> {properties['title']}<br>"
        f"<strong>Início do Tempo:</strong> {properties['time_start']}<br>"
        f"<strong>Fim do Tempo:</strong> {properties['time_end']}<br>"
        f"<strong>Granule Size:</strong> {properties['granule_size']}<br>"
        f"<strong>Granule URL:</strong> <a href='{properties['granule_url']}' target='_blank'>Link</a>"
    )

    folium.GeoJson(
        feature,
        tooltip=tooltip_info
    ).add_to(gedi_layer)

# Adiciona o grupo de camadas ao mapa
m.add_child(gedi_layer)

# Adiciona controle de camada ao mapa para permitir que os usuários escolham visualizar ou ocultar os dados do GEDI
folium.LayerControl().add_to(m)

# Salva o mapa como um arquivo HTML com o título desejado
map_filename = "mapa_leafmap_interativo.html"
m.save(map_filename)

# Abre o arquivo HTML em um navegador padrão
import webbrowser
webbrowser.open(map_filename, new=2)  # "new=2" abre em uma nova janela/tab

