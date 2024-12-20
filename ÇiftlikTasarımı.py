import tkinter as tk
from tkinter import messagebox
import numpy as np

# Arazi Optimizasyonu Fonksiyonu
def arazi_optimizasyonu(toprak_tipi, urunler):
    urun_uygunluk = {
        "kumlu": ["mısır", "buğday"],
        "killi": ["pirinç", "soya"],
        "tınlı": ["domates", "biber"]
    }
    ekonomik_getiri = {
        "mısır": 1500,
        "buğday": 1000,
        "pirinç": 2000,
        "soya": 1200,
        "domates": 2500,
        "biber": 1800
    }
    uygun_urunler = urun_uygunluk.get(toprak_tipi, [])
    uygun_urunler = [(urun, ekonomik_getiri[urun]) for urun in urunler if urun in uygun_urunler]
    uygun_urunler.sort(key=lambda x: x[1], reverse=True)  # Ekonomik getirisine göre sıralama
    return uygun_urunler

# Su Tüketimi Hesaplama Fonksiyonu
def su_tuketimi(bitki_tipi, alan, su_ihtiyaci_m2):
    toplam_su_ihtiyaci = alan * su_ihtiyaci_m2
    return f"{bitki_tipi} için toplam su ihtiyacı: {toplam_su_ihtiyaci:.2f} litre"

# Enerji Optimizasyonu Fonksiyonu
def enerji_optimizasyonu(gunluk_tuketim, enerji_kaynaklari):
    yenilenebilir = {"güneş": 5, "rüzgar": 7}  # kWh
    karbon_ayak_izi = {"güneş": 0, "rüzgar": 0}  # kg CO2
    toplam = sum([yenilenebilir.get(kaynak, 0) for kaynak in enerji_kaynaklari])
    toplam_karbon = sum([karbon_ayak_izi.get(kaynak, 0) for kaynak in enerji_kaynaklari])
    tasarruf = max(0, toplam - gunluk_tuketim)
    return f"Yenilenebilir enerji toplamı: {toplam} kWh, Tasarruf: {tasarruf} kWh, Karbon Ayak İzi: {toplam_karbon} kg CO2"

# Gübre Kullanımı Hesaplama Fonksiyonu (Yeni Özellik)
def gubre_hesaplama(bitki_tipi, alan, organik=True):
    gubre_miktarlari = {
        "mısır": 1.2,  # kg/m²
        "buğday": 0.8,
        "pirinç": 1.0,
        "domates": 1.5,
        "soya": 0.7
    }
    cevresel_etki = "Organik Gübre" if organik else "Kimyasal Gübre"
    gubre_ihtiyaci = gubre_miktarlari.get(bitki_tipi, 0) * alan
    return f"{bitki_tipi} için toplam gübre ihtiyacı: {gubre_ihtiyaci:.2f} kg ({cevresel_etki})"

# Tkinter GUI
def hesapla_arazi():
    toprak_tipi = entry_toprak.get()
    urunler = entry_urunler.get().split(",")  # Ürünler virgülle ayırılacak
    uygun_urunler = arazi_optimizasyonu(toprak_tipi, urunler)
    uygun_urunler_str = ", ".join([f"{urun} ({getiri} TL)" for urun, getiri in uygun_urunler])
    messagebox.showinfo("Arazi Optimizasyonu", f"Uygun Ürünler: {uygun_urunler_str}")

def hesapla_su():
    try:
        bitki_tipi = entry_bitki.get() # type: ignore
        alan = float(entry_alan.get()) # type: ignore
        su_ihtiyaci = float(entry_su.get()) # type: ignore
        sonuc = su_tuketimi(bitki_tipi, alan, su_ihtiyaci)
        messagebox.showinfo("Su Yönetimi", sonuc)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayısal değerler girin.")

def hesapla_enerji():
    try:
        gunluk_tuketim = float(entry_enerji.get())
        enerji_kaynaklari = entry_kaynaklar.get().split(",")  # Kaynaklar virgül ile ayrılacak
        sonuc = enerji_optimizasyonu(gunluk_tuketim, enerji_kaynaklari)
        messagebox.showinfo("Enerji Yönetimi", sonuc)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayısal bir tüketim değeri girin.")

def hesapla_gubre():
    try:
        bitki_tipi = entry_gubre_bitki.get()
        alan = float(entry_gubre_alan.get())
        organik = var_organik.get() == 1
        sonuc = gubre_hesaplama(bitki_tipi, alan, organik)
        messagebox.showinfo("Gübre Hesaplama", sonuc)
    except ValueError:
        messagebox.showerror("Hata", "Lütfen geçerli sayısal değerler girin.")

# Ana Pencere
pencere = tk.Tk()
pencere.title("Sürdürülebilir Çiftlik Tasarım Yazılımı")
pencere.geometry("800x600")
pencere.configure(bg="#d9f7d4")  # Açık yeşil arka plan

# Arazi Yönetimi Bölümü
tk.Label(pencere, text="Arazi Yönetimi", font=("Arial", 14), bg="#d9f7d4").pack(pady=5)
tk.Label(pencere, text="Toprak Tipi (kumlu/killi/tınlı):", bg="#d9f7d4").pack()
entry_toprak = tk.Entry(pencere)
entry_toprak.pack()

tk.Label(pencere, text="Ürünler (virgülle ayırın):", bg="#d9f7d4").pack()
entry_urunler = tk.Entry(pencere)
entry_urunler.pack()

frame_buttons_1 = tk.Frame(pencere, bg="#d9f7d4")
frame_buttons_1.pack(pady=10)

btn_arazi = tk.Button(frame_buttons_1, text="Arazi Optimizasyonu", command=hesapla_arazi, bg="#8bc34a", fg="white")
btn_arazi.pack(side=tk.LEFT, padx=10)

btn_su = tk.Button(frame_buttons_1, text="Su Tüketimi Hesapla", command=hesapla_su, bg="#8bc34a", fg="white")
btn_su.pack(side=tk.LEFT, padx=10)

# Enerji Yönetimi Bölümü
tk.Label(pencere, text="Enerji Yönetimi", font=("Arial", 14), bg="#d9f7d4").pack(pady=5)
tk.Label(pencere, text="Günlük Tüketim (kWh):", bg="#d9f7d4").pack()
entry_enerji = tk.Entry(pencere)
entry_enerji.pack()

tk.Label(pencere, text="Enerji Kaynakları (güneş,rüzgar):", bg="#d9f7d4").pack()
entry_kaynaklar = tk.Entry(pencere)
entry_kaynaklar.pack()

frame_buttons_2 = tk.Frame(pencere, bg="#d9f7d4")
frame_buttons_2.pack(pady=10)

btn_enerji = tk.Button(frame_buttons_2, text="Enerji Optimizasyonu", command=hesapla_enerji, bg="#8bc34a", fg="white")
btn_enerji.pack(side=tk.LEFT, padx=10)

btn_gubre = tk.Button(frame_buttons_2, text="Gübre İhtiyacı Hesapla", command=hesapla_gubre, bg="#8bc34a", fg="white")
btn_gubre.pack(side=tk.LEFT, padx=10)

# Gübre Yönetimi Bölümü
tk.Label(pencere, text="Gübre Yönetimi", font=("Arial", 14), bg="#d9f7d4").pack(pady=5)
tk.Label(pencere, text="Bitki Tipi:", bg="#d9f7d4").pack()
entry_gubre_bitki = tk.Entry(pencere)
entry_gubre_bitki.pack()

tk.Label(pencere, text="Alan (m2):", bg="#d9f7d4").pack()
entry_gubre_alan = tk.Entry(pencere)
entry_gubre_alan.pack()

frame_gubre = tk.Frame(pencere, bg="#d9f7d4")
frame_gubre.pack(pady=10)

var_organik = tk.IntVar()
tk.Checkbutton(frame_gubre, text="Organik Gübre Kullan", variable=var_organik, bg="#d9f7d4").pack(side=tk.LEFT, padx=10)

# Pencereyi Başlat
pencere.mainloop()
