import requests


headers1 = {
    "Content-Type": "application/json",
}

URL_SERVICE = "https://d231ce07-625d-4500-ae26-25e4a5068e73.serverhub.praktikum-services.ru/"

HEADER_CREATE = "api/v1/orders"

BODY_CREATE = {

    "firstName": "Абдурахмангаджи",
    "lastName": "Убдурахмангаджи",
    "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
    "metroStation": 204,
    "phone": "+34916123458",
    "rentTime": 5,
    "deliveryDate": "2023-03-19",
    "comment": "Не звони"
}
# создание заказа

def post_new_create(body):
    return requests.post(URL_SERVICE + HEADER_CREATE, json=body, headers=headers1)

response = post_new_create(BODY_CREATE);
trackno = response.json()["track"]
assert response.status_code == 201
print(response.status_code)
print(response.json())
print(trackno)

trackstr = str(trackno)

RECEIVE_ORDER = "v1/orders/track?t= " + trackstr
# Нахождение заказа по трек-номеру

def get_track_no():
    return requests.get(URL_SERVICE + RECEIVE_ORDER)

get_response = get_track_no();
assert  get_response.status_code == 200
print(get_response.status_code)
