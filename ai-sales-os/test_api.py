import requests
import json
import sqlite3

# Login to get session cookie
res = requests.post("http://127.0.0.1:8000/login", json={"username": "admin", "password": "admin123"})
if res.status_code != 200:
    print(f"Login failed: {res.text}")
    
cookies = res.cookies

# Try to update admin profile
data = {
    "name": "Sarah Connor",
    "email": "sarah@test.com",
    "phone": "123",
    "company_name": "Test Company",
    "business_address": "Test Address"
}

res2 = requests.put("http://127.0.0.1:8000/admin/profile", json=data, cookies=cookies)
print("Admin Profile Update Response:")
print(res2.status_code)
print(res2.text)

# Try to update settings
data3 = {
    "company_name": "Test Company",
    "business_name": "Test Company",
    "business_address": "Test Address",
    "business_phone": "123",
    "business_email": "hello@test.com",
    "website_url": "https://test.com",
    "social_media_links": "foo",
    "working_hours": "9-5",
    "timezone": "UTC",
    "language": "English",
    "currency": "USD"
}

res3 = requests.put("http://127.0.0.1:8000/settings", json=data3, cookies=cookies)
print("Settings Update Response:")
print(res3.status_code)
print(res3.text)
