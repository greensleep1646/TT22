import requests
from bs4 import BeautifulSoup

def tiktok_adres_bul(username):
    url = f"https://www.tiktok.com/@{username}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        address_element = soup.find('span', {'class': 'user-address'})
        if address_element:
            address = address_element.text.strip()
            print(f"{username}'ın adresi: {address}")
        else:
            print("Adres bulunamadı.")
    else:
        print("TikTok profili bulunamadı.")

username = input("Hedefin TikTok kullanıcı adını gir: ")
tiktok_adres_bul(username)
