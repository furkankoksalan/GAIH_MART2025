# GAIH_MART2025

#  Metro Ağı Simülasyonu

Bu proje, bir şehir metrosunun istasyon ve hat yapısını simüle eder. A* algoritması ile en hızlı rotayı, BFS algoritması ile en az aktarma yapılan rotayı bulur. Ayrıca bulunan rota grafiksel olarak görselleştirilir.

---

## 🛠 Kullanılan Teknolojiler ve Kütüphaneler

Python 3 ile geliştirilmiştir. Kullanılan kütüphaneler:

- `collections`: deque veri yapısı ile BFS kuyruğu için
- `heapq`: öncelikli kuyruk (A* algoritması) için
- `math`: koordinatlar arası uzaklık (heuristic)
- `networkx`: graf yapısını oluşturmak ve analiz etmek için
- `matplotlib`: grafikleri çizmek ve görselleştirme yapmak için
- `time`: algoritma çalışma süresini ölçmek için

---

## 📌 Algoritmaların Çalışma Mantığı

### 🔹 1. BFS (Breadth-First Search) – En Az Aktarma

- Her istasyonu ziyaret ederek hedefe giden en kısa aktarma sayılı rotayı bulur.
- Aktarma, iki istasyon farklı hatlardaysa sayılır.
- BFS sırası `deque` ile takip edilir.
- Her istasyon-hat çifti ayrı ziyaret kontrolü ile optimize edilmiştir.

### 🔹 2. A* Algoritması – En Hızlı Rota

- Gelişmiş öncelikli kuyruk algoritmasıdır.
- Her adımda: `g(n) + h(n)` hesaplanır.
  - `g(n)`: o ana kadar olan toplam süre
  - `h(n)`: kalan tahmini süre (heuristic olarak koordinat uzaklığı)
- En kısa sürede hedefe ulaşan rotayı bulur.
- Öncelikli kuyruk `heapq` ile uygulanır.

### 🔸 Neden Bu Algoritmalar?

- **BFS**, en kısa adım sayısını (dolayısıyla aktarma sayısını) garantiler.
- **A\***, süre bazlı tahminle daha hızlı çözümler üretir.
- Her iki algoritma metro yolculuğunun farklı ihtiyaçlarına hitap eder.

---

## 🧪 Örnek Kullanım ve Test Sonuçları

### 🛤️ Örnek İstasyonlar

- **Kırmızı Hat**: Kızılay → Ulus → Demetevler → OSB  
- **Mavi Hat**: AŞTİ → Kızılay → Sıhhiye → Gar  
- **Turuncu Hat**: Batıkent → Demetevler → Gar → Keçiören

### 🔁 Örnek Test Senaryoları

**1. AŞTİ → OSB**
- En az aktarma: `AŞTİ -> Kızılay -> Ulus -> Demetevler -> OSB`
- En hızlı rota: (süre ve adım sayısı gösterilir)

**2. Batıkent → Keçiören**
- Direkt turuncu hat üzerinde
- En az aktarma: 0
- En hızlı rota: rota ve süre yazdırılır

**3. Keçiören → AŞTİ**
- 2 aktarma noktası içerir (Gar ve Kızılay)
- A* rotası süre bazında daha verimli olabilir

### 📈 Görselleştirme

Rotayı grafik olarak çizen fonksiyon kullanılmıştır. İstasyonlar düğüm, geçişler kenar olarak gösterilir. Rota kırmızı renkle vurgulanır.

---

## 🚀 Projeyi Geliştirme Fikirleri

- Gerçek şehir metrolarıyla (İstanbul, Ankara) veri tabanı bağlantısı
- Web arayüzü (Streamlit/Flask) ile kullanıcı dostu yapı
- Kullanıcıdan kalkış-varış alma
- JSON/CSV veri ile dış veri aktarımı
- Aktarma sürelerini daha detaylı modelleme (bekleme süreleri gibi)
- Metro kart entegrasyonu (sanal bilet ücreti hesaplama)

---

**Hazırlayan:** [Furkan Köksalan]  


