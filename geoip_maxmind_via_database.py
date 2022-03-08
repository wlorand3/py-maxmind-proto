import geoip2.database
test_ip = '90.90.90.90'  # Paris

with geoip2.database.Reader('./db/GeoLite2-City_20220301/GeoLite2-City.mmdb') as reader:
    response = reader.city(test_ip)
    print(f'City Name: {response.city.name}')
    print(
        f'Lat/Lng: {response.location.latitude, response.location.longitude}')
    print(f'Accuracy: {response.location.accuracy_radius} km')
