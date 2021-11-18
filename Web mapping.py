import folium
import pandas
f=pandas.read_csv("tor.txt")
l1=list(f["LAT"])
l2=list(f["LON"])
l3=list(f["NAME"])
l4=list(f["LOCATION"])
l5=list(f["TYPE"])
d=pandas.read_json("kadu.json")
print(d)
def color(rate):

    if 4 < co >=5:
        return "green"
    elif 2< co >=3:
        return "orange"
    else:
        return "red"

mp =folium.Map(location=[21.068084974573743,81.37345526251033],zoom_start=11,min_zoom=8,max_zoom=20)
f=folium.FeatureGroup("Tourist Map")
for lan,lon,name,loc,co in zip(l1,l2,l3,l4,l5):
    f.add_child(folium.Marker(location=[lan,lon],popup=str(name),tooltip=str(loc),icon=folium.Icon(color=color(co),icon="car")))
mp.add_child(f)
mp.save("c1.html")
