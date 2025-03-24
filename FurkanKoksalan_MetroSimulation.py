from collections import defaultdict, deque
from typing import Dict, List, Optional, Tuple
import matplotlib.pyplot as plt
import networkx as nx
import time
import heapq
import math

# Her istasyonu temsil eden sınıf
class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str, x: float = 0, y: float = 0):
        self.idx = idx        # İstasyonun benzersiz ID'si
        self.ad = ad          # İstasyonun adı
        self.hat = hat        # İstasyonun ait olduğu metro hattı
        self.x = x            # Haritadaki X koordinatı (görselleştirme için)
        self.y = y            # Haritadaki Y koordinatı (görselleştirme için)
        self.komsular: List[Tuple['Istasyon', int]] = []  # Komşu istasyonlar ve aradaki süre

    # İstasyona komşu ekleyen fonksiyon
    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

    # A* algoritması için kullanılacak sezgisel (heuristic) fonksiyon (öklidyen mesafe)
    def heuristic(self, hedef: 'Istasyon') -> float:
        return math.sqrt((self.x - hedef.x) ** 2 + (self.y - hedef.y) ** 2)

    def __hash__(self):
        return hash(self.idx)

    def __eq__(self, other):
        return isinstance(other, Istasyon) and self.idx == other.idx

# Metro ağı sınıfı
class MetroAgi:
    def __init__(self):
        self.istasyonlar: Dict[str, Istasyon] = {}  # ID ile istasyonlara erişim
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)  # Hat bazında istasyon gruplaması

    # Yeni istasyon ekleme fonksiyonu
    def istasyon_ekle(self, idx: str, ad: str, hat: str, x: float = 0, y: float = 0) -> None:
        if idx not in self.istasyonlar:
            istasyon = Istasyon(idx, ad, hat, x, y)
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    # İki istasyon arasında çift yönlü bağlantı ekleyen fonksiyon
    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None:
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)

    # Güzergahı matplotlib ile görselleştirir
    def gorsellestir_rota(self, rota: List[Istasyon]):
        G = nx.Graph()
        # Tüm kenarları grafa ekle
        for istasyon in self.istasyonlar.values():
            for komsu, sure in istasyon.komsular:
                G.add_edge(istasyon.ad, komsu.ad, weight=sure)

        # İstasyonların koordinatlarını pozisyon olarak ayarla
        pos = {ist.ad: (ist.x, ist.y) for ist in self.istasyonlar.values()}
        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_size=800, node_color='lightgray', font_weight='bold')

        # Belirtilen güzergahı kırmızı ile çiz
        rota_adlari = [ist.ad for ist in rota]
        yol_ciftleri = list(zip(rota_adlari, rota_adlari[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=yol_ciftleri, edge_color='red', width=2)

        plt.title("Rota Görselleştirme")
        plt.show()

    # BFS ile en az aktarma yapan rotayı bulur
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        kuyruk = deque([(baslangic, [baslangic], 0)])  # BFS kuyruğu: (istasyon, rota, aktarma sayısı)
        ziyaret_edildi = set([(baslangic, baslangic.hat)])  # Aynı istasyon ve hat kombinasyonu bir kez ziyaret edilir

        while kuyruk:
            guncel_istasyon, rota, aktarma = kuyruk.popleft()

            if guncel_istasyon == hedef:
                print(f"Rota bulundu! Toplam aktarma: {aktarma}")
                return rota

            for komsu, _ in guncel_istasyon.komsular:
                yeni_aktarma = aktarma + (1 if komsu.hat != guncel_istasyon.hat else 0)
                ziyaret_kriter = (komsu, komsu.hat)

                if ziyaret_kriter not in ziyaret_edildi:
                    ziyaret_edildi.add(ziyaret_kriter)
                    kuyruk.append((komsu, rota + [komsu], yeni_aktarma))

        print("Uygun rota bulunamadı.")
        return None

    # A* algoritması ile en hızlı rotayı bulur
    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]:
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None

        baslangic = self.istasyonlar[baslangic_id]
        hedef = self.istasyonlar[hedef_id]

        baslama_zamani = time.time()
        oncelik_kuyrugu = [(0, id(baslangic), baslangic, [baslangic])]  # (toplam_sure + heuristic, id, istasyon, rota)
        ziyaret_edildi = set()

        while oncelik_kuyrugu:
            toplam_sure, _, guncel_istasyon, rota = heapq.heappop(oncelik_kuyrugu)

            if guncel_istasyon == hedef:
                bitis_zamani = time.time()
                print(f"Rota bulundu! Toplam süre: {toplam_sure} dakika")
                print(f"Çalışma süresi: {bitis_zamani - baslama_zamani:.4f} saniye")
                return rota, toplam_sure

            if guncel_istasyon in ziyaret_edildi:
                continue

            ziyaret_edildi.add(guncel_istasyon)

            for komsu, sure in guncel_istasyon.komsular:
                if komsu not in ziyaret_edildi:
                    tahmini_toplam = toplam_sure + sure + komsu.heuristic(hedef)
                    heapq.heappush(oncelik_kuyrugu, (tahmini_toplam, id(komsu), komsu, rota + [komsu]))

        print("Rota bulunamadı.")
        return None

# Ana çalışma bloğu: örnek metro ağı oluşturulur ve testler yapılır
if __name__ == "__main__":
    metro = MetroAgi()

    # Kırmızı Hat istasyonları
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat", 0, 0)
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat", 1, 2)
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat", 3, 3)
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat", 5, 3)

    # Mavi Hat istasyonları
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat", -3, -1)
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat", 0, 0)
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat", 1, -1)
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat", 3, -2)

    # Turuncu Hat istasyonları
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat", -1, 4)
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat", 3, 3)
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat", 3, -2)
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat", 5, 5)

    # Bağlantılar
    metro.baglanti_ekle("K1", "K2", 4)
    metro.baglanti_ekle("K2", "K3", 6)
    metro.baglanti_ekle("K3", "K4", 8)

    metro.baglanti_ekle("M1", "M2", 5)
    metro.baglanti_ekle("M2", "M3", 3)
    metro.baglanti_ekle("M3", "M4", 4)

    metro.baglanti_ekle("T1", "T2", 7)
    metro.baglanti_ekle("T2", "T3", 9)
    metro.baglanti_ekle("T3", "T4", 5)

    # Hatlar arası bağlantılar
    metro.baglanti_ekle("K1", "M2", 2)
    metro.baglanti_ekle("K3", "T2", 3)
    metro.baglanti_ekle("M4", "T3", 2)

    # Test senaryoları
    print("\n=== Ek Test Senaryoları ===")

    print("\n4. Sıhhiye'den Kızılay'a:")
    rota = metro.en_az_aktarma_bul("M3", "M2")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
        metro.gorsellestir_rota(rota)

    sonuc = metro.en_hizli_rota_bul("M3", "M2")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        metro.gorsellestir_rota(rota)

    print("\n5. Dikimevi'nden OSB'ye:")
    # Dikimevi tanımlı değil, bu kısım çalışmayacak, A1 yok
    rota = metro.en_az_aktarma_bul("A1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
        metro.gorsellestir_rota(rota)

    sonuc = metro.en_hizli_rota_bul("A1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        metro.gorsellestir_rota(rota)

    print("\n6. OSB'den Batıkent'e:")
    rota = metro.en_az_aktarma_bul("K4", "T1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
        metro.gorsellestir_rota(rota)

    sonuc = metro.en_hizli_rota_bul("K4", "T1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
        metro.gorsellestir_rota(rota)
