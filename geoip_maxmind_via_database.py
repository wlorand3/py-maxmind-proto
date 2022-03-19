import geoip2.database
import data.ip_data as data

with geoip2.database.Reader('./db/GeoLite2-City_20220301/GeoLite2-City.mmdb') as reader:

    for ip in data.more_ip_addresses:
        ip_obj = reader.city(ip)
        print(f'City Name: {ip_obj.city.name}')
        print(
            f'Lat/Lng: {ip_obj.location.latitude, ip_obj.location.longitude}')
        print(f'Accuracy: {ip_obj.location.accuracy_radius} km\n')
