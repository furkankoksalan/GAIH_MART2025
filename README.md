# 🚇 Akıllı Metro Ağı Simülasyonu

### 🔍 En Verimli Güzergahı Bulan, En Az Aktarma Yapan Ulaşım Rehberi

Bu proje, bir şehir metrosunun istasyon ve hat yapısını simüle eder. A* algoritması ile **en hızlı rotayı**, BFS algoritması ile **en az aktarma yapılan** rotayı bulur. Gelişmiş görselleştirme ve kullanıcıya yönelik rota analiziyle fark yaratır.

---

## 🎯 Proje Amacı

Gerçek bir metro kullanıcısı gibi düşün:  
🧍‍♂️ “Aktarma az olsun”  
⏱️ “Zaman kaybetmeyeyim”  
🧭 “Rota net ve görsel olsun”

Bu projede amaç, bu üç kullanıcı beklentisini **yapay zeka destekli algoritmalarla** karşılamaktır.

---

## 🧠 Fark Yaratan Özellikler

- 🚦 Hem **en az aktarma** hem de **en kısa sürede ulaşım**
- 📊 **Grafik destekli güzergah haritası**
- ♻️ Genişletilebilir veri yapısı
- 🧩 Gelecekte gerçek şehir verileriyle entegre edilebilir

---

## 🛠️ Kullanılan Teknolojiler

| Kütüphane | Açıklama |
|----------|----------|
| `collections.deque` | BFS kuyruğu için |
| `heapq` | A* öncelikli kuyruk için |
| `math` | Koordinat bazlı heuristic hesaplama |
| `networkx` | Metro ağı graf yapısı |
| `matplotlib` | Rota görselleştirmesi |
| `time` | Algoritma süresi ölçümü |

---

## ⚙️ Algoritmalar

### 🔹 BFS (Breadth-First Search) – En Az Aktarma

- İstasyon-hat çiftleri ayrı düğüm gibi ele alınır.
- Hat değişimi olduğunda **aktarma sayılır**.
- `deque` ile seviyeli tarama yapılır.
- En az aktarma sayısıyla hedefe ulaşılır.

### 🔸 A* Algoritması – En Hızlı Rota

- Her adımda `g(n) + h(n)` değeri hesaplanır:
  - `g(n)`: O ana kadar geçen süre
  - `h(n)`: Kalan tahmini süre (heuristic)
- `heapq` ile öncelikli kuyruk üzerinde çalışır.
- Gerçek zamanlı en hızlı rota bulunur.

---

## 🧪 Örnek Senaryolar

| Başlangıç | Varış | En Az Aktarma | A* Süresi | A* Rota |
|-----------|-------|----------------|-----------|---------|
| AŞTİ | OSB | AŞTİ → Kızılay → Ulus → Demetevler → OSB | 12 dk | Aynı rota veya varyant |
| Batıkent | Keçiören | Direkt Turuncu Hat (0 aktarma) | 6 dk | Batıkent → Gar → Keçiören |
| Keçiören | AŞTİ | 2 aktarma (Gar, Kızılay) | 14 dk | Keçiören → Gar → Sıhhiye → Kızılay → AŞTİ |

> 📌 Testler sonucunda, A* algoritması süre bakımından avantaj sağlar. Ancak hat sayısı arttıkça aktarma oranı artabilir.

> ![image](https://github.com/user-attachments/assets/b92b62fc-5cb3-474b-94a5-1598f2acd05b)

> ![image](https://github.com/user-attachments/assets/5b3b66d1-32a5-4242-afcc-1b5bf43a830c)

> ![image](https://github.com/user-attachments/assets/26c5e931-223d-4dcd-a3c0-6e1274124542)

> ![image](https://github.com/user-attachments/assets/dae2ae30-20f0-462d-b3ff-84e05cbc79e6)

---

## 📈 Görselleştirme

`NetworkX` ve `Matplotlib` ile metro ağı görselleştirilir:

- 🟢 İstasyonlar: düğüm
- 🔵 Hatlar: kenar
- 🔴 Seçilen rota: vurgulu kırmızı çizgi

Grafikler sayesinde yolcunun rota üzerindeki geçişleri **anlaması ve güven duyması** sağlanır.

---

## 🚀 Geliştirme Fikirleri

- 🌐 Web arayüz (Streamlit, Flask)  
- 🗺️ İstanbul, Ankara metrolarının entegrasyonu  
- ⌛ Aktarma gecikme sürelerinin modellenmesi  
- 📁 JSON / CSV dış veri kaynağı  
- 🧮 Metro ücreti hesaplama (bakiye simulasyonu)  
- 📱 Mobil uygulama ile konum bazlı kullanım  

---

## 🧩 Projenin Farkı

> Bu proje yalnızca bir “algoritma gösterisi” değil.  
Gerçek hayattaki yolcu davranışlarını, **mühendislik zekası** ve **optimizasyon prensipleri** ile birleştirerek sunar.

---
