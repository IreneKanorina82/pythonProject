import requests
import pytest_check as check

def test_api_users_page ():
    r = requests.get('https://reqres.in//api/users/23')
    status_code = r.status_code

    check.equal(status_code,404,f'Статус код не равен 200. Статус код равен {status_code}')



 def test_api_users_page():
     r = requests.post('https://reqres.in//api/register')
     status_code = r.status_code

     check.equal(status_code, 200, f'Статус код не равен 200. Статус код равен {status_code}')

     data = r.json()

     for user in data['data']:
          if 'email, password' in user and user['email, password'] == "'eve.holt@reqres.in', 'pistol'":
              print ('OK')
          else:
              print ('ERROR')

