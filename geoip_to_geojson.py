import geoip2.database
from geojson import Point, Feature, FeatureCollection, dump

import data.ip_data as data

features = []

with geoip2.database.Reader('./db/GeoLite2-City_20220419/GeoLite2-City.mmdb') as reader:

    # for ip in data.more_ip_addresses:
    for ip in data.ip_address_pair:
        ip_obj = reader.city(ip)
        print(f'City Name: {ip_obj.city.name}')
        print(
            f'Lat/Lng: {ip_obj.location.latitude, ip_obj.location.longitude}')
        print(f'Accuracy: {ip_obj.location.accuracy_radius} km\n')

        # write geojson feature obj
        features.append(Feature(geometry=Point((ip_obj.location.longitude, ip_obj.location.latitude)), properties={
                        "geoip_accuracy_radius": ip_obj.location.accuracy_radius, "city_name": ip_obj.city.name}))

# outside of the db file reading loop, create a geojson FeatureCollection
feature_collection = FeatureCollection(features)

# write the feature collection to a .geojson file
with open('./geojson/geoip_results.geojson', 'w') as geojson_file:
    dump(feature_collection, geojson_file)
