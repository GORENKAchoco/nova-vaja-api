import requests

koordinate = [
    {"ime": "Ljubljana", "lat": 46.05, "lon": 14.51},
    {"ime": "London", "lat": 51.51, "lon": -0.13},
    {"ime": "New York", "lat": 40.71, "lon": -74.01},
    {"ime": "Tokyo", "lat": 35.68, "lon": 139.69},
    {"ime": "Sydney", "lat": -33.87, "lon": 151.21},
    {"ime": "Kairo", "lat": 30.04, "lon": 31.24},
    {"ime": "São Paulo", "lat": -23.55, "lon": -46.63},
    {"ime": "Mumbai", "lat": 19.08, "lon": 72.88}
]


# 1: Poišči mesto z najvišjo maksimalno temperaturo v naslednjih 7 dneh
# Namig: Uporabi max() na ["daily"]["temperature_2m_max"]

max_tmp=0
max_tmp_mesto=""
for k in koordinate:
    lat=k["lat"]
    lon=k["lon"]
    url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max&timezone=Europe%2FBerlin"
    call=requests.get(url).json()
    max_temp=max(call["daily"]["temperature_2m_max"])
    if max_temp>max_tmp:
        max_tmp=max_temp
        max_tmp_mesto=k["ime"]
#print(max_tmp_mesto,max_tmp)

# 2: Katero mesto bo imelo največ padavin skupaj v naslednjih 7 dneh?
# Namig: Seštej vse vrednosti v ["daily"]["precipitation_sum"]

max_padavine=0
max_padavine_mesto=""
for k in koordinate:
    lat=k["lat"]
    lon=k["lon"]
    url=f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=rain_sum&timezone=Europe%2FBerlin"
    call=requests.get(url).json()
    max_pada=sum(call["daily"]["rain_sum"])
    if max_pada>max_padavine:
        max_padavine=max_pada
        max_padavine_mesto=k["ime"]
print(max_padavine_mesto,max_padavine)

# 3: Najdi najhladneje mesto v naslednjih 7 dneh
# Namig: Nekatera mesta lahko nimajo podatkov, preveri dolžino seznama!



# 4: Poišči mesto z največjim temperaturnim razponom (max - min) za prvi dan
# Namig: Uporabi indeks [0] za prvi dan napovedi

# 5: Izpiši vsa mesta, kjer bo jutri padalo (precipitation_sum[1] > 0)
# Namig: Jutri je na indeksu [1], danes je [0]

# 6: Koliko mest bo imelo jutri maksimalno temperaturo nad 20°C?
# Namig: Preštej mesta, kjer je temperature_2m_max[1] > 20

# 7: Katero mesto ima najhitrejši veter v naslednjih 7 dneh? Izpiši tudi hitrost vetra.
# Namig: Preveri max() vrednost v ["daily"]["wind_speed_10m_max"]

# 8: V katerem mestu je najdaljši dan (razlika med zahodom in vzhodom sonca)?
# Namig: Uporabi DateTime https://www.w3schools.com/python/python_datetime.asp

# 9: Ugotovi, koliko mest bo  v naslednjih 7 dneh brez padavin
# Namig: Preveri, če ima mesto vsaj eno ničlo v precipitation_sum