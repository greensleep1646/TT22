import requests
from bs4 import BeautifulSoup

def tiktok_ev_adresi_bul(username):
    # TikTok profil URL'sini oluştur
    url = f"https://www.tiktok.com/@{username}"

    # URL'yi getir
    response = requests.get(url)

    # Hedefin TikTok sayfasını kontrol et
    if response.status_code == 200:
        # BeautifulSoup kullanarak sayfayı analiz et
        soup = BeautifulSoup(response.text, 'html.parser')

        # Profil sayfasında metin içeriğini ara
        profile_info = soup.find('meta', attrs={'property': 'og:description'})

        # Profil bilgisini al
        profile_content = profile_info['content']

        # Adresi içeren kısımları bul
        adresler = [i for i in profile_content.split() if i.startswith("Adres:")]

        if adresler:
            # Eğer adres varsa, ilk adresi döndür
            return adresler[0][7:]
        else:
            return "Üzgünüm, adres bulunamadı. Ya da senin yeteneksizliğini mi sorgulayayım?"

    else:
        return "Hedefin TikTok profili bulunamadı. Daha iyi bir hedef seçmelisin."

# Kullanıcı adını gir
username = input("TikTok kullanıcı adını gir: ")

# Fonksiyonu çağır ve sonucu yazdır
print(tiktok_ev_adresi_bul(username))
