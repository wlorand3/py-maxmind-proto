import geoip2.database
import json

import data.ip_data as data

geo_data = []

with geoip2.database.Reader('./db/GeoLite2-City_20220301/GeoLite2-City.mmdb') as reader:

    # for ip in data.more_ip_addresses:
    for ip in data.ip_address_pair:
        ip_obj = reader.city(ip)
        # print(f'City Name: {ip_obj.city.name}')
        # print(f'Lat/Lng: {ip_obj.location.latitude, ip_obj.location.longitude}')
        # print(f'Accuracy: {ip_obj.location.accuracy_radius} km\n')

        # manually create a dict of the data and push to the geo_data list
        geo_data.append(
            {"City": ip_obj.city.name,
             "coordinates": [ip_obj.location.latitude,
                             ip_obj.location.longitude],
             "accuracy": ip_obj.location.accuracy_radius})

# convert to json
json_data = json.dumps(geo_data, indent=2)
print(json_data)
