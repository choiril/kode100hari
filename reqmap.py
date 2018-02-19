# import request
import requests
# target alamat googlemaps
base_url = 'http://maps.googleapis.com/maps/api/geocode/json'
# alamat yang akan dicari titik geolokasinya, disini saya menggunakan Kabupaten saya 
my_params = {'address': 'Bojonegoro, East Java, ID, Indonesia', 
             'language': 'id'}
response = requests.get(base_url, params = my_params)
results = response.json()['results']
x_geo = results[0]['geometry']['location']
# menampilkan longitude dan latitude alamat
print(x_geo['lng'], x_geo['lat'])