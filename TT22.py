import requests

def tiktok_adres_bul(kullanici_adi):
    # TikTok API'sine istek yap
    url = f"https://api.tiktok.com/api/user/detail/?uniqueId={kullanici_adi}"
    response = requests.get(url)
    
    # Yanıtı kontrol et
    if response.status_code == 200:
        veri = response.json()
        if 'userInfo' in veri:
            kullanici_bilgisi = veri['userInfo']
            if 'city' in kullanici_bilgisi and 'country' in kullanici_bilgisi:
                adres = kullanici_bilgisi['city'] + ", " + kullanici_bilgisi['country']
                print("Kullanıcının adresi:", adres)
            else:
                print("Kullanıcının adresi bulunamadı.")
        else:
            print("Kullanıcı bilgileri alınamadı.")
    else:
        print("TikTok API'ye bağlanırken bir hata oluştu.")

# Kullanıcı adını buraya gir
tiktok_kullanici_adi = input("TikTok kullanıcı adını gir: ")
tiktok_adres_bul(tiktok_kullanici_adi)
