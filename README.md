# 🌑 Karanlik-Dort-Gun-Mimarisi: Ay Güney Kutbu Mikroşebeke ve Kütle Fırlatma Altyapısı

![TUA Astrohackathon](https://img.shields.io/badge/Etkinlik-TUA_Astrohackathon-0052cc?style=flat-square)
![Milli Uzay Programı](https://img.shields.io/badge/Hedef-Ay_Güney_Kutbu_Kolonisi-e60000?style=flat-square)
![Sürüm](https://img.shields.io/badge/Sürüm-v1.1.0-orange?style=flat-square)
![Teknoloji](https://img.shields.io/badge/Teknoloji-Akıllı_Şebeke_%7C_Kütle_Fırlatıcı_%7C_Termal_Depolama-2ea44f?style=flat-square)

## 🚀 Yüksek Düzey Özet
**Karanlik-Dort-Gun-Mimarisi**, Ay'ın Güney Kutbu'nda (Shackleton Krateri bölgesi) kurulacak kalıcı bir üssün karşılaştığı en büyük hayatta kalma ve lojistik testini otonom olarak çözen entegre bir endüstriyel sistem tasarımıdır. 

Sistem iki ana omurgadan oluşur:
1. **Yapay Zeka Destekli Mikroşebeke (Microgrid):** Kutup bölgesindeki dondurucu 4 günlük karanlık periyotları (termal ölüm riskini) atlatmak için, güneş enerjisini devasa lityum bataryalar yerine **Regolit Termal Enerji Depolama (TES)** sistemlerinde hapseden ve Stirling motorlarıyla kesintisiz elektriğe çeviren kapalı döngü enerji ağı.
2. **Kütle Fırlatıcı (Mass Driver / Katapult):** Ay yüzeyinde üretilen su buzunu ve değerli madenleri kimyasal roket kullanmadan, Lineer Senkron Motorlar (LSM) ile elektromanyetik olarak doğrudan Ay yörüngesine fırlatan otonom lojistik sistemi.

---

## 🏗️ Teknik Derinlik ve Sistem Modelleme

### 1. Mikroşebeke Karar Mekanizması (AI Load Shedding)
Karanlık dönemde hayatta kalabilmek için sistem enerji tüketimini 3 ana kategoriye ayırır:
- **Kritik (ECLSS):** Yaşam destek, sürekli aktif.
- **Esnek (Termal):** Regolit depodan Stirling motoruna aktarılan ısı akışı, ayarlanabilir.
- **Kesintili (Endüstriyel):** Katapult şarjı ve maden işleme, sadece enerji fazlası varsa aktif.

Yapay zeka, regolit sıcaklığı ($T_{reg}$) ve batarya doluluk oranına ($SOC$) bakarak anlık güç tahsisatı ($P_{alloc}$) yapar:
$$P_{alloc} = f(T_{reg}, SOC, \Delta t_{karanlik})$$

### 2. Termal Enerji Depolama (TES) Fizigi
Regolit bloklarından elde edilen enerji, blokların kütlesi ($m$), özgül ısı sığası ($c$) ve sıcaklık farkı ($\Delta T$) ile doğrudan orantılıdır:
$$Q = m \cdot c \cdot \Delta T$$
Soğuma eğrisi, Stefan-Boltzmann yasasına göre radyasyon kayıplarıyla modellenir. Vakum ortamında iletim (conduction) sadece temas noktalarında olduğu için regolit mükemmel bir yalıtkan görevi görür.

### 3. Katapult (Mass Driver) Ray Tasarımı
Fırlatılacak kargonun maruz kalacağı ivme ($a$) ve gereken ray uzunluğu ($L$) arasındaki ilişki:
$$L = \frac{v_e^2}{2a}$$
Örneğin, kargonun parçalanmaması için 50G (**$490 m/s^2$**) sınırı konulursa, **1.7 km/s** yörünge hızı için yaklaşık **2.95 km** ray uzunluğuna ihtiyaç duyulur.

---

## 🕹️ Operasyonel Senaryolar

### 🔴 Senaryo A: Nominal Ay Günü (Yükleme & Depolama)
- Güneş panelleri %100 kapasite çalışır.
- Regolit TES blokları 1000°C'ye ısıtılır.
- Kargo kapsülleri elektromanyetik raylara yerleştirilir ve süperkapasitörler kademeli şarj edilir.

### 🌑 Senaryo B: 4 Günlük Karanlık (Hayatta Kalma)
- AI modülü "L-MODE" (Legacy Mode) aktifleşir.
- Endüstriyel işlemler (madencilik, arıtma) durdurulur.
- Enerji sadece Stirling motoru üzerinden TES'ten çekilir.

### ⚡ Senaryo C: Acil Durum Fırlatması (Düşük Güç)
- Eğer ana şebeke hasar görürse, bataryadaki son enerji tek bir "Mass Driver Pulse" için optimize edilir.
- Kargo emniyeti yerine "yörüngeye ulaşma" önceliği alınır.

---

## 📂 Uygulama Modülleri (Source Modules)

### `mikrokarar_ai/grid_manager.py`
Bu modül, güneş panelleri, TES ve batarya bankası arasındaki enerji akışını yönetir. Doğrusal programlama (Linear Programming) kullanarak 4 günlük karanlık boyu hayatta kalma senaryolarını simüle eder.

### `termal_simülatör/cooling_model.py`
Isı depolama bloklarının yüzey alanı ve kütlesine bağlı olarak ne kadar sürede enerji üretim eşiğinin altına düşeceğini hesaplar.

### `katapult_kontrol/firlatma_simülatörü.py`
Elektromanyetik bobinlerin tetikleme zamanlamasını ve anlık güç çekimini optimize eder.

---

## 🛠️ Kurulum ve Yazılım Simülasyonu

Yapay zekanın karanlık periyotta enerjiyi nasıl optimize ettiğini veya elektromanyetik fırlatma profilini bilgisayarınızda test etmek için:

```bash
# Depoyu klonlayın
git clone https://github.com/arch-yunus/Karanlik-Dort-Gun-Mimarisi.git
cd Karanlik-Dort-Gun-Mimarisi

# Gerekli bilimsel hesaplama kütüphanelerini yükleyin
pip install -r requirements.txt

# Gelişmiş fırlatma simülasyonunu başlatın (örnek: 250kg kargo, 30G ivme)
python src/katapult_kontrol/firlatma_simülatörü.py --kargo_kg 250 --accel_g 30
```

---

## 🔮 Gelecek Vizyonu
- [ ] **Yörünge Yakalama (Orbital Catching):** Fırlatılan kargo paketlerinin Ay yörüngesindeki istasyonda elektromanyetik ağlar veya otonom uzay römorkörleriyle (Tug) yakalanmasını sağlayan yörünge mekaniği algoritmaları.
- [ ] **Modüler Ray Genişletmesi:** Otonom rover'ların fırlatma rayını Ay yüzeyinde 3D baskı (Sinterleme) ile sürekli uzatarak daha ağır kargoların daha düşük G-kuvvetiyle fırlatılmasını sağlaması.

---

## 👨‍🔬 Sistem Mimarı
Bu proje, **TUA Astrohackathon** etkinliği kapsamında gezegenler arası lojistiği ve enerji altyapılarını endüstriyel optimizasyon prensipleriyle çözmek amacıyla tasarlanmıştır.

**Tasarım ve Optimizasyon:** Multi-Disciplinary Systems Designer | Solopreneur | AI & Endüstriyel Optimizasyon