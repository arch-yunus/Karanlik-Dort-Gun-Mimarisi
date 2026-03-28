# 🌡️ Termal Kapasite ve Regolit Isı Sığası Analizi

Ay yüzeyindeki Regolit Termal Enerji Depolama (TES) sisteminin verimliliği, malzemenin ısıl özelliklerine doğrudan bağlıdır.

## 📊 Regolit Termal Özellikleri

Ay regoliti, vakum altında olağanüstü düşük ısıl iletkenliğe sahip olsa da, katılaştırılmış (sinterlenmiş) bloklar yüksek ısı depolama kapasitesi sunar.

### 1. Özgül Isı Sığası ($C_p$) Model
Regolitin özgül ısısı sıcaklığa bağlı olarak değişir:
$$C_p(T) = A + B \cdot T + C \cdot T^2$$

Tipik değerler (300K - 1000K aralığı):
- **300K:** ~700 J/kg·K
- **1000K:** ~1200 J/kg·K

### 2. Enerji Depolama Yoğunluğu
1 m³ regolit blok ($\rho \approx 2000 \, \text{kg/m}^3$) için depolanan enerji:
$$Q = \int_{T_{min}}^{T_{max}} m \cdot C_p(T) \, dT$$

**Örnek Hesaplama:**
1000°C'den 200°C'ye soğuyan 1 tonluk blok yaklaşık **0.8 - 1.2 GJ** enerji sağlar. Bu, mikroşebeke için kritik gece baz yükünü karşılamak için yeterlidir.

---

## 🏗️ TES Ünite Tasarımı
Her bir TES ünitesi, radyasyon kaybını minimize etmek için çok katmanlı yalıtım (MLI) ile çevrili regolit çekirdek ve ortasında bir Stirling motoru ısı değiştiricisi barındırır.

- **Çekirdek Malzeme:** Sinterlenmiş Ay Regoliti
- **Çalışma Aralığı:** 250°C - 1100°C
- **Tahmini Verimlilik:** %40 (Stirling çevrimi dahil)
