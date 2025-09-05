

**Portal**, metin tabanlı bir sosyal medya mikroblog platformudur ve Kamu Portal, Memur Portal, Öğrenci Portal gibi farklı temalar için özelleştirilebilir. Kullanıcıların gönderi paylaşabileceği, mesajlaşabileceği, trendleri takip edebileceği ve yöneticilerin platformu denetleyebileceği bir sistem sunar.

## Özellikler
- Kullanıcı Arayüzü: Anasayfa, profil, arama, mesajlaşma, keşfet, bildirimler, ayarlar, özel içerikler.
- Yönetim Panelleri: Admin, moderatör ve süper üye panelleri.
- Reklam Yönetimi: Üye türüne göre özelleştirilmiş reklamlar.
- İstatistikler: Kullanıcı ve gönderi analitikleri.

## Kurulum
1. Depoyu klonlayın: `git clone https://github.com/kullaniciadi/portal.git`
2. Sanal ortam oluşturun: `python -m venv venv`
3. Sanal ortamı etkinleştirin: `venv\Scripts\activate` (Windows) veya `source venv/bin/activate` (Linux/Mac)
4. Gereksinimleri yükleyin: `pip install -r requirements.txt`
5. Migrasyonları çalıştırın: `python manage.py makemigrations && python manage.py migrate`
6. Süper kullanıcı oluşturun: `python manage.py createsuperuser`
7. Statik dosyaları toplayın: `python manage.py collectstatic`
8. Sunucuyu başlatın: `python manage.py runserver`
9. Siteye erişin: `http://localhost:8000/` (Kullanıcı arayüzü) ve `http://localhost:8000/admin-panel/dashboard/` (Admin paneli)

## Gereksinimler
- Python 3.8+
- Django 4.2+
- PostgreSQL (veya başka bir Django destekli veritabanı)

## Katkıda Bulunma
Katkılarınızı bekliyoruz! Lütfen bir issue açın veya pull request gönderin.

## Lisans
MIT Lisansı
