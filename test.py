import json

class KaynakYoneticisi:
    def __init__(self, islem_sayisi, kaynak_sayisi, tahsis_matris, maksimum_matris, mevcut_kaynaklar):
        self.islem_sayisi = islem_sayisi
        self.kaynak_sayisi = kaynak_sayisi
        self.tahsis_matris = tahsis_matris
        self.maksimum_matris = maksimum_matris
        self.mevcut_kaynaklar = mevcut_kaynaklar

    def bilgi_goster(self):
        print("Islem Sayisi:", self.islem_sayisi)
        print("Kaynak Sayisi:", self.kaynak_sayisi)
        print("\nTahsis Matris:")
        for satir in self.tahsis_matris:
            print(satir)
        print("\nMaksimum Matris:")
        for satir in self.maksimum_matris:
            print(satir)
        print("\nMevcut Kaynaklar:")
        print(self.mevcut_kaynaklar)

    def guvenli_mi(self):
        calisma_kaynaklari = self.mevcut_kaynaklar[:]
        biten_islemler = [False] * self.islem_sayisi
        guvenli_sira = []
        while len(guvenli_sira) < self.islem_sayisi:
            ilerleme_yapildi = False
            for i in range(self.islem_sayisi):
                if not biten_islemler[i]:
                    
                    gerekli_kaynaklar = [self.maksimum_matris[i][j] - self.tahsis_matris[i][j] for j in range(self.kaynak_sayisi)]
                    if all(gerekli_kaynaklar[j] <= calisma_kaynaklari[j] for j in range(self.kaynak_sayisi)):
                        
                        calisma_kaynaklari = [calisma_kaynaklari[j] + self.tahsis_matris[i][j] for j in range(self.kaynak_sayisi)]
                        biten_islemler[i] = True
                        guvenli_sira.append(i)
                        ilerleme_yapildi = True
                        break
            if not ilerleme_yapildi:
                return False, []
        return True, guvenli_sira

    def cikti_kaydet(self, cikti_dosyasi, ogrenci_no, guvenli, sonuc):
        
        cikti_verisi = {
            "ogrenciNo": ogrenci_no,
            "guvenli": guvenli,
            "sonuc": sonuc
        }

        with open(cikti_dosyasi, "w") as dosya:
            json.dump(cikti_verisi, dosya, indent=4)

        print(f"Cikti {cikti_dosyasi} dosyasina kaydedildi")

with open("input.json", "r") as dosya:
    veriler = json.load(dosya)

kaynak_yoneticisi = KaynakYoneticisi(
    islem_sayisi=veriler["nproc"],
    kaynak_sayisi=veriler["nres"],
    tahsis_matris=veriler["allocationMatrix"],
    maksimum_matris=veriler["maximumMatrix"],
    mevcut_kaynaklar=veriler["availableResources"]
)

kaynak_yoneticisi.bilgi_goster()

ogrenci_no = 221213057

guvenli, sonuc = kaynak_yoneticisi.guvenli_mi()

kaynak_yoneticisi.cikti_kaydet("output.json", ogrenci_no, 1 if guvenli else 0, sonuc)
