import requests
from bs4 import BeautifulSoup

def tiktok_ev_adresi_bul(username):
    url = f"https://www.tiktok.com/@{username}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        user_info = soup.find('div', class_='share-sub-title')
        if user_info:
            user_id = user_info['data-user-id']
            address_url = f"https://www.tiktok.com/node/share/user/@{user_id}?lang=en"
            address_response = requests.get(address_url)
            if address_response.status_code == 200:
                address_data = address_response.json()
                if 'address' in address_data:
                    ev_adresi = address_data['address']
                    print(f"{username} adlı kullanıcının ev adresi: {ev_adresi}")
                else:
                    print(f"{username} adlı kullanıcının ev adresi bulunamadı.")
            else:
                print("Adres bilgisine ulaşırken bir hata oluştu.")
        else:
            print("Kullanıcı bilgileri bulunamadı.")
    else:
        print("Kullanıcı profili bulunamadı.")

# Kullanıcı adını gir ve işini bitir.
tiktok_ev_adresi_bul("kullanıcı_adı")
