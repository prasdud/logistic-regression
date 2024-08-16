#!/usr/bin/env python3


import http.client

conn = http.client.HTTPSConnection("billboard-api2.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "Sign Up for Key",
    'x-rapidapi-host': "billboard-api2.p.rapidapi.com"
}

conn.request("GET", "/hot-100?date=2019-05-11&range=1-10", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))