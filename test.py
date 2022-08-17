import streamlit as st
import geopandas as gpd
import pydeck as pdk

def map_3D(value="current-energy-efficiency"):
    PATH = "C:/Users/lilia/Downloads/wmca_download_2022-07-29_10-07-36/files/wmca_prj/project/unzip_files/output/SJ9000.geojson"
    df = gpd.read_file(PATH, driver='GeoJSON')
    df["lng"] = df.geometry.centroid.x
    df["lat"] = df.geometry.centroid.y

    xMax, xMin = df.lng.max(), df.lng.min()
    yMax, yMin = df.lat.max(), df.lat.min()
    LAND_COVER = [[[xMin, yMin], [xMin, yMax], [xMax, yMax], [xMax, yMin]]]

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=df['lat'].mean(),
            longitude=df['lng'].mean(),
            zoom=12,
            max_zoom=15,
            min_zoom=10,
            pitch=50,
            get_color='[200, 30, 0, 160]',
        ),
        layers=[
            pdk.Layer(
                "ColumnLayer",
                data=df,
                opacity=0.8,
                extruded=True,
                flatShading=True,
                get_elevation="AbsHMax",
                get_position=['lng','lat'],
                elevation_scale=1,
                elevation_range=[0, 1000],
                radius=5,
                get_fill_color=f"[{value}/20 *255, 255, {value} / 100 * 255]",
                get_line_color=[255, 255, 255],
            ),
            pdk.Layer(
                "PolygonLayer",
                LAND_COVER,
                stroked=False,
                # processes the data as a flat longitude-latitude pair
                get_polygon="-",
                get_fill_color=[0, 0, 0, 20],
            )
        ],
    ))

map_3D('calculatedAreaValue')