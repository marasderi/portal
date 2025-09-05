Portal
Portal, metin tabanlı bir sosyal medya mikroblog platformudur. Kamu Portal, Memur Portal ve Öğrenci Portal gibi farklı temalar için özelleştirilebilir. Kullanıcıların gönderi paylaşabileceği, mesajlaşabileceği, trendleri takip edebileceği ve yöneticilerin platformu etkin bir şekilde denetleyebileceği bir sistem sunar. Kullanıcı dostu arayüzü ve güçlü yönetim araçlarıyla bireysel ve kurumsal ihtiyaçlara hitap eder.
Özellikler

Kullanıcı Arayüzü: Anasayfa, profil, arama, mesajlaşma, keşfet, bildirimler, ayarlar ve özel içerikler.
Yönetim Panelleri: Admin, moderatör ve süper üye panelleri ile platform yönetimi.
Reklam Yönetimi: Üye türüne göre özelleştirilmiş reklamlar.
İstatistikler: Kullanıcı ve gönderi analitikleri ile detaylı raporlama.

Proje Yapısı

/portal: Ana Django proje dosyaları
/core: Uygulama mantığı ve modeller
/templates: HTML şablonları
/static: CSS, JS ve diğer statik dosyalar
/requirements.txt: Proje bağımlılıkları
/manage.py: Django yönetim komutları

Kurulum
Aşağıdaki adımları takip ederek Portal'ı yerel makinenizde kurabilirsiniz:

Depoyu klonlayın:git clone https://github.com/marasderi/portal.git


Sanal ortam oluşturun:python -m venv venv


Sanal ortamı etkinleştirin:
Windows: venv\Scripts\activate
Linux/Mac: source venv/bin/activate


Gereksinimleri yükleyin:pip install -r requirements.txt


Veritabanını yapılandırın:
PostgreSQL kullanıyorsanız, settings.py dosyasındaki DATABASES ayarını güncelleyin:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portal_db',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


Ortam değişkenlerini bir .env dosyasında tanımlayın:SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://your_username:your_password@localhost:5432/portal_db




Migrasyonları çalıştırın:python manage.py makemigrations && python manage.py migrate


Süper kullanıcı oluşturun:python manage.py createsuperuser


Statik dosyaları toplayın:python manage.py collectstatic


Sunucuyu başlatın:python manage.py runserver


Siteye erişin:
Kullanıcı arayüzü: http://localhost:8000/
Admin paneli: http://localhost:8000/admin-panel/dashboard/



Gereksinimler

Python 3.8+
Django 4.2+
PostgreSQL (veya Django destekli başka bir veritabanı)
Örnek bağımlılıklar:
Django==4.2
psycopg2-binary==2.9.6
django-crispy-forms==2.0



Tam bağımlılık listesi için requirements.txt dosyasını inceleyin.
Testler
Projeyi test etmek için aşağıdaki komutu kullanabilirsiniz:
python manage.py test

Ekran Görüntüleri

Anasayfa: Kullanıcıların gönderileri görüntülediği ana sayfa.
Admin Paneli: Yönetim ve denetim araçları.

Not: Ekran görüntüleri için screenshots/ dizinine ilgili dosyaları ekleyin.
Katkıda Bulunma
Katkılarınızı memnuniyetle karşılıyoruz! Lütfen aşağıdaki adımları takip edin:

Depoyu fork edin.
Yeni bir branch oluşturun: git checkout -b feature/your-feature-name
Değişikliklerinizi yapın ve commit edin: git commit -m "Açıklayıcı mesaj"
Değişikliklerinizi push edin: git push origin feature/your-feature-name
Bir pull request gönderin ve inceleme için bekleyin.

Kod stili için PEP 8 kurallarına uyun. Pull request'lerde net bir açıklama ve test sonuçları ekleyin.
Destek
Sorularınız veya hatalar için lütfen bir GitHub Issue açın veya [marasderi@gmail.com] adresine yazın.
Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.
