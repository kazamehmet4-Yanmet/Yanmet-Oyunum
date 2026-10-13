import random
import tkinter as tk
from tkinter import messagebox
import os

try:
    import winsound
    SES_DESTEGI = True
except ImportError:
    SES_DESTEGI = False

pencere = tk.Tk()
pencere.title("🚀 YANMET: CYBER SHOCK 2026 Ultimate RPG")
pencere.geometry("560x980")
pencere.configure(bg="#0f172a")

# --- GLOBAL OYUN VERİLERİ ---
gizli_sayi = random.randint(1, 100)
tahmin_hakki = 10
hamle_sayisi = 0
hacker_adi = "ANONYMOUS"  
secili_sinif = "Netrunner"
siber_para = 500  

# Gelişmiş Combat Sistemleri
oyuncu_hp = 100
ai_hp = 100
ai_adi = "CHROME_CORRUPTOR"

cpu_seviyesi = 1  
ram_seviyesi = 1  
cyberware_seviyesi = 1
yancoin_fiyat = 100
yancoin_cuzdan = 0

goz_implanti_alindi = False
kalp_implanti_alindi = False
gunluk_odul_alindi = False

# ENVANTER VE GÖREV DEĞİŞKENLERİ
siber_iksir_sayisi = 1
reboot_kart_sayisi = 0
alinan_ganimetler = []
gorev1_tamamlandi = False
gorev2_tamamlandi = False
su_anki_tema = "Mavi"

LIDERLER_DOSYASI = "yanmet_liderler_v6.txt"
SKOR_DOSYASI = "skor_verisi_v6.txt"
def ses_cal(efekt_tipi):
    if not SES_DESTEGI: return
    try:
        if efekt_tipi == "tus": winsound.Beep(1000, 50)
        elif efekt_tipi == "yanlis": winsound.Beep(400, 150)
        elif efekt_tipi == "basari": winsound.Beep(1200, 200)
        elif efekt_tipi == "kritik": winsound.Beep(1500, 100)
        elif efekt_tipi == "yetenek": winsound.Beep(1800, 80)
    except: pass

def siber_giris_muzigi():
    if not SES_DESTEGI: return
    try:
        notalar = [
            (440, 150), (554, 150), (659, 150), (880, 300),
            (0, 100),   
            (659, 150), (880, 450)
        ]
        for frekans, sure in notalar:
            if frekans == 0: pencere.after(sure)
            else: winsound.Beep(frekans, sure)
    except: pass

def konsol_yaz(mesaj, tip="OK"):
    try:
        if 'txt_konsol' in globals() and txt_konsol.winfo_exists():
            txt_konsol.config(state=tk.NORMAL)
            simge = "[+] " if tip == "OK" else "[!] " if tip == "WARN" else "[*] "
            txt_konsol.insert(tk.END, f"{simge}{mesaj}\n")
            txt_konsol.see(tk.END)
            txt_konsol.config(state=tk.DISABLED)
    except: pass

def ekrani_temizle_ve_ac(hedef_frame):
    # Sabit üst başlık hariç tüm sahneleri gizler, böylece YANMET yazısı hep kalır!
    for frame in [frame_giris_ekrani, frame_ana_menu, frame_ana_oyun, frame_magaza_ekrani, 
                  frame_borsa_ekrani, frame_lider_ekrani, frame_destek_ekrani, 
                  frame_envanter_ekrani, frame_gorev_ekrani, frame_tema_ekrani]:
        if 'frame' in locals() and frame.winfo_exists(): frame.pack_forget()
    hedef_frame.pack(fill=tk.BOTH, expand=True)
def skoru_kaydet():
    try:
        with open(SKOR_DOSYASI, "w", encoding="utf-8") as f:
            f.write(f"{siber_para}\n{cpu_seviyesi}\n{ram_seviyesi}\n{cyberware_seviyesi}\n"
                    f"{yancoin_cuzdan}\n{hacker_adi}\n{secili_sinif}\n"
                    f"{int(goz_implanti_alindi)}\n{int(kalp_implanti_alindi)}\n"
                    f"{siber_iksir_sayisi}\n{reboot_kart_sayisi}\n"
                    f"{int(gorev1_tamamlandi)}\n{int(gorev2_tamamlandi)}\n{su_anki_tema}")
        konsol_yaz("Gelişmiş siber ilerleme ve envanter veritabanına kaydedildi.", "OK")
    except: pass

def skoru_yukle():
    global siber_para, cpu_seviyesi, ram_seviyesi, cyberware_seviyesi, yancoin_cuzdan, hacker_adi, secili_sinif, goz_implanti_alindi, kalp_implanti_alindi, siber_iksir_sayisi, reboot_kart_sayisi, gorev1_tamamlandi, gorev2_tamamlandi, su_anki_tema
    if os.path.exists(SKOR_DOSYASI):
        try:
            with open(SKOR_DOSYASI, "r", encoding="utf-8") as f:
                satirlar = f.read().splitlines()
                if len(satirlar) >= 7:
                    siber_para = int(satirlar[0])
                    cpu_seviyesi = int(satirlar[1])
                    ram_seviyesi = int(satirlar[2])
                    cyberware_seviyesi = int(satirlar[3])
                    yancoin_cuzdan = int(satirlar[4])
                    hacker_adi = satirlar[5]
                    secili_sinif = satirlar[6]
                if len(satirlar) >= 9:
                    goz_implanti_alindi = bool(int(satirlar[7]))
                    kalp_implanti_alindi = bool(int(satirlar[8]))
                if len(satirlar) >= 14:
                    siber_iksir_sayisi = int(satirlar[9])
                    reboot_kart_sayisi = int(satirlar[10])
                    gorev1_tamamlandi = bool(int(satirlar[11]))
                    gorev2_tamamlandi = bool(int(satirlar[12]))
                    su_anki_tema = satirlar[13]
            return True
        except: pass
    return False

def liderleri_yukle():
    liderler = []
    if os.path.exists(LIDERLER_DOSYASI):
        try:
            with open(LIDERLER_DOSYASI, "r", encoding="utf-8") as f:
                for satir in f:
                    if "," in satir:
                        isim, hamle = satir.strip().split(",")
                        liderler.append((isim, int(hamle)))
        except: pass
    liderler.sort(key=lambda x: x if len(x) > 1 else 99)
    return liderler[:3]

def rekor_kontrol_ve_kaydet(hamle):
    liderler = liderleri_yukle()
    liderler.append((hacker_adi, hamle))
    liderler.sort(key=lambda x: x if len(x) > 1 else 99)
    liderler = liderler[:3]
    try:
        with open(LIDERLER_DOSYASI, "w", encoding="utf-8") as f:
            for isim, h in liderler: f.write(f"{isim},{h}\n")
    except: pass

def sinif_sec(sinif_adi):
    ses_cal("tus")
    global secili_sinif
    secili_sinif = sinif_adi
    if 'lbl_secili_sinif_gosterge' in globals() and lbl_secili_sinif_gosterge.winfo_exists():
        lbl_secili_sinif_gosterge.config(text=f"🚩 Sınıf: {secili_sinif}", fg="#38bdf8" if sinif_adi == "Netrunner" else "#eab308" if sinif_adi == "Fixer" else "#ef4444")
    konsol_yaz(f"Hacker rolü güncellendi: {sinif_adi} aktif.", "SYS")
    skoru_kaydet()
def dukkan_guncelle():
    if 'lbl_m_cuzdan' in globals() and lbl_m_cuzdan.winfo_exists():
        lbl_m_cuzdan.config(text=f"💰 Bakiyeniz: {siber_para} ₵")
    if 'lbl_durum' in globals() and lbl_durum.winfo_exists():
        lbl_durum.config(text=f"Hacker: {hacker_adi} | Sınıf: {secili_sinif} | Para: {siber_para} ₵")
    if 'btn_m_cpu' in globals() and btn_m_cpu.winfo_exists():
        btn_m_cpu.config(text=f"💻 CPU Geliştir (Lvl {cpu_seviyesi}) -> {cpu_seviyesi * 80} ₵")
    if 'btn_m_ram' in globals() and btn_m_ram.winfo_exists():
        btn_m_ram.config(text=f"🧠 RAM Geliştir (Lvl {ram_seviyesi}) -> {ram_seviyesi * 70} ₵")
    if 'btn_m_cyber' in globals() and btn_m_cyber.winfo_exists():
        btn_m_cyber.config(text=f"🦾 Cyberware Kur (Lvl {cyberware_seviyesi}) -> {cyberware_seviyesi * 100} ₵")
    if 'btn_m_goz' in globals() and btn_m_goz.winfo_exists():
        btn_m_goz.config(text="👁️ Kiroshi Gözü (ALINDI)" if goz_implanti_alindi else "👁️ Kiroshi Optik Al -> 250 ₵")
    if 'btn_m_kalp' in globals() and btn_m_kalp.winfo_exists():
        btn_m_kalp.config(text="❤️ Bio-Monitor (ALINDI)" if kalp_implanti_alindi else "❤️ Bio-Monitor Kalp Al -> 300 ₵")
    if 'btn_m_iksir' in globals() and btn_m_iksir.winfo_exists():
        btn_m_iksir.config(text=f"🧪 Siber Sağlık İksiri Al -> 50 ₵ (Sahip: {siber_iksir_sayisi})")
    if 'btn_m_kart' in globals() and btn_m_kart.winfo_exists():
        btn_m_kart.config(text=f"🃏 Sistem Reboot Kartı Al -> 120 ₵ (Sahip: {reboot_kart_sayisi})")
    skoru_kaydet()

def satinal(tip):
    global siber_para, cpu_seviyesi, ram_seviyesi, cyberware_seviyesi, goz_implanti_alindi, kalp_implanti_alindi, siber_iksir_sayisi, reboot_kart_sayisi
    if tip == "cpu" and siber_para >= cpu_seviyesi * 80:
        siber_para -= cpu_seviyesi * 80
        cpu_seviyesi += 1
    elif tip == "ram" and siber_para >= ram_seviyesi * 70:
        siber_para -= ram_seviyesi * 70
        ram_seviyesi += 1
    elif tip == "cyber" and siber_para >= cyberware_seviyesi * 100:
        siber_para -= cyberware_seviyesi * 100
        cyberware_seviyesi += 1
    elif tip == "goz" and not goz_implanti_alindi and siber_para >= 250:
        siber_para -= 250
        goz_implanti_alindi = True
    elif tip == "kalp" and not kalp_implanti_alindi and siber_para >= 300:
        siber_para -= 300
        kalp_implanti_alindi = True
    elif tip == "iksir" and siber_para >= 50:
        siber_para -= 50
        siber_iksir_sayisi += 1
    elif tip == "kart" and siber_para >= 120:
        siber_para -= 120
        reboot_kart_sayisi += 1
    else:
        messagebox.showerror("Hata", "İşlem başarısız! Yetersiz bakiye veya zaten alınmış.")
        return
    ses_cal("basari")
    dukkan_guncelle()
def envanter_guncelle():
    metin = f"🎒 {hacker_adi} - MEVCUT SİBER ÇANTA 🎒\n\n"
    metin += f"🧪 Siber Sağlık İksiri: {siber_iksir_sayisi} Adet\n"
    metin += f"🃏 Sistem Reboot Kartı: {reboot_kart_sayisi} Adet\n\n"
    metin += f"💻 CPU Seviyesi: Lvl {cpu_seviyesi}\n"
    metin += f"🧠 RAM Seviyesi: Lvl {ram_seviyesi}\n"
    metin += f"🦾 Cyberware Seviyesi: Lvl {cyberware_seviyesi}\n\n"
    metin += "👁️ Kiroshi Gözü: " + ("[KURULU]" if goz_implanti_alindi else "[YOK]") + "\n"
    metin += "❤️ Bio-Monitor Kalp: " + ("[KURULU]" if kalp_implanti_alindi else "[YOK]") + "\n\n"
    metin += "🏆 ELE GEÇİRİLEN BOSS GANİMETLERİ:\n"
    if alinan_ganimetler:
        for g in alinan_ganimetler: metin += f" - {g}\n"
    else: metin += " - Henüz boss ganimeti yok.\n"
    if 'lbl_e_liste' in globals() and lbl_e_liste.winfo_exists():
        lbl_e_liste.config(text=metin)

def iksir_kullan():
    global siber_iksir_sayisi, oyuncu_hp
    if siber_iksir_sayisi > 0:
        if oyuncu_hp >= 100:
            messagebox.showinfo("Sağlık Tam", "Canınız zaten maksimum seviyede!")
            return
        siber_iksir_sayisi -= 1
        oyuncu_hp = min(100, oyuncu_hp + 40)
        ses_cal("basari")
        envanter_guncelle()
        konsol_yaz(f"🧪 Çantadan Sağlık İksiri tıklandı. Can +40 yenilendi! Yeni HP: {oyuncu_hp}", "OK")
    else: messagebox.showwarning("Çanta Boş", "Hiç Sağlık İksiriniz kalmadı!")

def reboot_kart_kullan():
    global reboot_kart_sayisi, tahmin_hakki
    if reboot_kart_sayisi > 0:
        reboot_kart_sayisi -= 1
        tahmin_hakki = 10
        ses_cal("basari")
        envanter_guncelle()
        konsol_yaz("🃏 Çantadan Reboot Kartı tetiklendi! ICE şifreleme hakları yenilendi. (+10 Hak)", "OK")
    else: messagebox.showwarning("Çanta Boş", "Hiç Reboot Kartınız kalmadı!")

def borsa_ekrani_guncelle():
    if 'lbl_b_durum' in globals() and lbl_b_durum.winfo_exists():
        lbl_b_durum.config(text=f"🪙 YanCoin Fiyatı: {yancoin_fiyat} ₵\nPortföy: {yancoin_cuzdan} YNC")

def b_islem(islem_tipi):
    global siber_para, yancoin_cuzdan, yancoin_fiyat
    if islem_tipi == "al" and siber_para >= yancoin_fiyat:
        siber_para -= yancoin_fiyat
        yancoin_cuzdan += 1
    elif islem_tipi == "sat" and yancoin_cuzdan > 0:
        yancoin_cuzdan -= 1
        siber_para += yancoin_fiyat
    else:
        messagebox.showerror("Hata", "İşlem reddedildi!")
        return
    ses_cal("basari")
    yancoin_fiyat = max(20, yancoin_fiyat + random.randint(-40, 50))
    borsa_ekrani_guncelle()
    if 'lbl_durum' in globals() and lbl_durum.winfo_exists():
        lbl_durum.config(text=f"Hacker: {hacker_adi} | Sınıf: {secili_sinif} | Para: {siber_para} ₵")
    skoru_kaydet()

def gorev_paneli_guncelle():
    if 'btn_g1' in globals() and btn_g1.winfo_exists():
        btn_g1.config(text="🏢 Şirket Verisi Çal (Tamamlandı)" if gorev1_tamamlandi else "🏢 Şirket Verisi Çal (+150 ₵ Ödül)")
    if 'btn_g2' in globals() and btn_g2.winfo_exists():
        btn_g2.config(text="🔐 ICE Korumasını Erit (Tamamlandı)" if gorev2_tamamlandi else "🔐 ICE Korumasını Erit (+250 ₵ Ödül)")

def gorev_yap(numara):
    global siber_para, gorev1_tamamlandi, gorev2_tamamlandi
    if numara == 1:
        if gorev1_tamamlandi: return
        if cpu_seviyesi >= 2:
            siber_para += 150
            gorev1_tamamlandi = True
            ses_cal("basari")
            konsol_yaz("🏢 Şirket sunucularına sızıldı! Ödül: +150 ₵", "OK")
            gorev_paneli_guncelle()
            skoru_kaydet()
        else: messagebox.showwarning("Yetersiz Donanım", "Bu işlem için en az CPU Seviye 2 gerekiyor!")
    elif numara == 2:
        if gorev2_tamamlandi: return
        if ram_seviyesi >= 2 and cyberware_seviyesi >= 2:
            siber_para += 250
            gorev2_tamamlandi = True
            ses_cal("basari")
            konsol_yaz("🔐 Ağ korumaları çökertildi! Ödül: +250 ₵", "OK")
            gorev_paneli_guncelle()
            skoru_kaydet()
        else: messagebox.showwarning("Yetersiz Donanım", "Bu işlem için en az RAM Seviye 2 ve Cyberware Seviye 2 gerekiyor!")
def tahmin_et():
    global tahmin_hakki, gizli_sayi, siber_para, hamle_sayisi
    try: tahmin = int(ent_tahmin.get())
    except ValueError:
        messagebox.showwarning("Uyan Hacker!", "Sadece sayı girin!")
        return
    hamle_sayisi += 1
    tahmin_hakki -= 1
    ses_cal("tus")
    if tahmin == gizli_sayi:
        ses_cal("basari")
        odul = 200 + (tahmin_hakki * 25)
        if secili_sinif == "Fixer": odul = int(odul * 1.3)
        siber_para += odul
        konsol_yaz(f"MAINFRAME HACKLENDİ! {gizli_sayi} doğruydu. +{odul} ₵", "OK")
        rekor_kontrol_ve_kaydet(hamle_sayisi)
        oyunu_sifirla()
    elif tahmin_hakki <= 0:
        ses_cal("yanlis")
        konsol_yaz(f"Sistem kilitlendi! Doğru şifre: {gizli_sayi}", "WARN")
        oyunu_sifirla()
    else:
        ses_cal("yanlis")
        yon = "YÜKSEK FREKANS" if tahmin > gizli_sayi else "DÜŞÜK FREKANS"
        konsol_yaz(f"Çok {yon}! Kalan Deneme: {tahmin_hakki}", "WARN")
    lbl_durum.config(text=f"Hacker: {hacker_adi} | Sınıf: {secili_sinif} | Para: {siber_para} ₵")
    skoru_kaydet()

def oyunu_sifirla():
    global gizli_sayi, tahmin_hakki, hamle_sayisi
    gizli_sayi = random.randint(1, 100)
    tahmin_hakki = 10
    hamle_sayisi = 0
    ent_tahmin.delete(0, tk.END)

def gunluk_odul_al_baamsiz():
    global siber_para, gunluk_odul_alindi
    if gunluk_odul_alindi:
        messagebox.showinfo("Matrix Kilitli", "Bugün zaten siber yardım paketi aldın!")
        return
    ses_cal("basari")
    hediye = random.randint(100, 300)
    siber_para += hediye
    gunluk_odul_alindi = True
    lbl_destek_baslik.config(text=f"🎁 ÖDÜL ALINDI!\nHesabınıza {hediye} ₵ aktarıldı.", fg="#10b981")
    if 'lbl_durum' in globals() and lbl_durum.winfo_exists():
        lbl_durum.config(text=f"Hacker: {hacker_adi} | Sınıf: {secili_sinif} | Para: {siber_para} ₵")
    skoru_kaydet()

def boss_saldir(aksiyon):
    global oyuncu_hp, ai_hp, siber_para, alinan_ganimetler
    ses_cal("tus")
    if aksiyon == "hack":
        hasar = random.randint(10, 25) + (cpu_seviyesi * 3)
        konsol_yaz(f"⚔️ {hacker_adi}, {ai_adi}'a siber virüs enjekte etti! {hasar} hasar!", "OK")
    elif aksiyon == "yetenek":
        ses_cal("yetenek")
        if secili_sinif == "Netrunner":
            hasar = random.randint(25, 45) + (ram_seviyesi * 4)
            konsol_yaz(f"✨ NETRUNNER YETENEĞİ: 'Siber Çökertme' uygulandı! {hasar} Ağ Hasarı!", "OK")
        elif secili_sinif == "Solo":
            hasar = random.randint(30, 50) + (cyberware_seviyesi * 5)
            konsol_yaz(f"🔥 SOLO YETENEĞİ: 'Kritik Sinyal Aşımı' tetiklendi! {hasar} Ağır Hasar!", "OK")
        else:
            hasar = random.randint(20, 35) + (cpu_seviyesi * 4)
            siber_para += 30
            konsol_yaz(f"💵 FIXER YETENEĞİ: 'Rüşvet Protokolü' çalıştı! {hasar} Hasar + 30 ₵ nakit!", "OK")
    elif aksiyon == "savunma":
        hasar = 0
        konsol_yaz("🛡️ Güvenlik duvarları maksimuma çıkarıldı!", "SYS")
        if kalp_implanti_alindi: oyuncu_hp = min(100, oyuncu_hp + 15)
    ai_hp -= hasar
    if ai_hp > 0:
        boss_hasar = max(2, random.randint(12, 28) - (cyberware_seviyesi * 2))
        if aksiyon == "savunma": boss_hasar = max(2, boss_hasar - 10)
        oyuncu_hp -= boss_hasar
        konsol_yaz(f"💥 {ai_adi} karşı taarruz yaptı! {boss_hasar} hasar aldın!", "WARN")
    if ai_hp <= 0:
        ses_cal("basari")
        siber_para += 500
        ganimet_ismi = random.choice(["Efsanevi Çip", "Kripto Anahtar", "Corruptor Veri Sürücüsü"])
        if ganimet_ismi not in alinan_ganimetler: alinan_ganimetler.append(ganimet_ismi)
        konsol_yaz(f"🏆 BOSS SİSTEMDEN SİLİNDİ! +500 ₵ ve [{ganimet_ismi}] kazanıldı!", "OK")
        oyuncu_hp, ai_hp = 100, 100
    elif oyuncu_hp <= 0:
        ses_cal("kritik")
        konsol_yaz("💀 Bağlantın koptu! Sistem yenildi.", "WARN")
        oyuncu_hp, ai_hp = 100, 100
    lbl_boss_durum.config(text=f"🤖 {ai_adi} HP: {ai_hp}% | 👤 Senin HP: {oyuncu_hp}%")
    lbl_durum.config(text=f"Hacker: {hacker_adi} | Sınıf: {secili_sinif} | Para: {siber_para} ₵")
    skoru_kaydet()

def tema_uygula(tema_adi):
    global su_anki_tema
    su_anki_tema = tema_adi
    ses_cal("tus")
    renkler = {
        "Mavi":  {"bg": "#0f172a", "fg": "#38bdf8"},
        "Matrix":{"bg": "#022c22", "fg": "#10b981"},
        "Neon":  {"bg": "#2e1065", "fg": "#f472b6"}
    }
    r = renkler.get(tema_adi, renkler["Mavi"])
    for f in [pencere, frame_ust_sabit_baslik, frame_giris_ekrani, frame_ana_menu, frame_ana_oyun, frame_magaza_ekrani, 
              frame_borsa_ekrani, frame_destek_ekrani, frame_lider_ekrani, frame_envanter_ekrani, 
              frame_gorev_ekrani, frame_tema_ekrani]:
        if 'f' in locals() and f.winfo_exists(): f.configure(bg=r["bg"])
    lbl_tema_durum.config(text=f"🎨 Aktif Tema: Neon {tema_adi}", fg=r["fg"])
    messagebox.showinfo("Tema Senkronizasyonu", f"{tema_adi} Görsel Arayüzü Başarıyla Senkronize Edildi!")
    skoru_kaydet()
def oyunu_baslat():
    global hacker_adi
    yeni_ad = ent_giris_adi.get().strip().upper()
    if not yeni_ad:
        messagebox.showwarning("Erişim Engellendi", "Siber ağa isimsiz giriş yapamazsınız!")
        return
    ses_cal("tus")
    hacker_adi = yeni_ad
    skoru_kaydet()
    ekrani_temizle_ve_ac(frame_ana_menu)

# --- TÜM SİSTEMDE EN ÜSTTE SABİT KALACAK BAŞLIK PROTOKOLÜ ---
frame_ust_sabit_baslik = tk.Frame(pencere, bg="#0f172a")
frame_ust_sabit_baslik.pack(fill=tk.X, pady=15)

frame_merkez_logo = tk.Frame(frame_ust_sabit_baslik, bg="#0f172a")
frame_merkez_logo.pack()
tk.Label(frame_merkez_logo, text="YAN", font=("Courier New", 32, "bold"), bg="#0f172a", fg="#ef4444").pack(side=tk.LEFT)
tk.Label(frame_merkez_logo, text="MET", font=("Courier New", 32, "bold"), bg="#0f172a", fg="#facc15").pack(side=tk.LEFT)

# --- TÜM EKRANLARIN ÖNDEN TANIMLANMASI (HATALARI ÖNLER) ---
frame_giris_ekrani = tk.Frame(pencere, bg="#0f172a")
frame_ana_menu = tk.Frame(pencere, bg="#0f172a")
frame_ana_oyun = tk.Frame(pencere, bg="#0f172a")
frame_envanter_ekrani = tk.Frame(pencere, bg="#0f172a")
frame_magaza_ekrani = tk.Frame(pencere, bg="#1e293b")
frame_borsa_ekrani = tk.Frame(pencere, bg="#0f172a")
frame_gorev_ekrani = tk.Frame(pencere, bg="#0f172a")
frame_tema_ekrani = tk.Frame(pencere, bg="#0f172a")
frame_destek_ekrani = tk.Frame(pencere, bg="#0f172a")
frame_lider_ekrani = tk.Frame(pencere, bg="#0f172a")

# --- 1. SAHNE: GİRİŞ EKRANI ARAYÜZÜ ---
frame_giris_ekrani.pack(fill=tk.BOTH, expand=True)
tk.Label(frame_giris_ekrani, text="🔒 MERKEZİ VERİ TABANI GİRİŞİ", font=("Courier New", 11, "bold"), bg="#0f172a", fg="#38bdf8").pack(pady=(20, 5))
tk.Label(frame_giris_ekrani, text="HACKER KOD ADINIZI SEÇİN:", font=("Courier New", 10, "bold"), bg="#0f172a", fg="#38bdf8").pack(pady=(0, 20))

ent_giris_adi = tk.Entry(frame_giris_ekrani, font=("Courier New", 14, "bold"), justify="center", bg="#1e293b", fg="#38bdf8", insertbackground="white", width=20)
ent_giris_adi.insert(0, "ANONYMOUS")
ent_giris_adi.pack(pady=20)

btn_sisteme_gir = tk.Button(frame_giris_ekrani, text="⚡ SİSTEME ENJEKTE OL", font=("Courier New", 11, "bold"), bg="#10b981", fg="white", padx=10, pady=10, command=oyunu_baslat)
btn_sisteme_gir.pack(pady=20)

# --- 2. SAHNE: OYUN ANA MENÜSÜ ARAYÜZÜ ---
tk.Label(frame_ana_menu, text="💻 CORE MAINFRAME MENU", font=("Courier New", 18, "bold"), bg="#0f172a", fg="#38bdf8").pack(pady=30)
tk.Button(frame_ana_menu, text="🎮 OYUNA BAŞLA (HACKFIELD)", font=("Courier New", 12, "bold"), bg="#10b981", fg="white", width=30, height=1, command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_ana_oyun), dukkan_guncelle()]).pack(pady=10)
tk.Button(frame_ana_menu, text="💼 SİBER ÇANTA (ENVANTER)", font=("Courier New", 12, "bold"), bg="#eab308", fg="white", width=30, height=1, command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_envanter_ekrani), envanter_guncelle()]).pack(pady=10)
tk.Button(frame_ana_menu, text="🏪 MİLİTER DONANIM BORSASI", font=("Courier New", 12, "bold"), bg="#6366f1", fg="white", width=30, height=1, command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_magaza_ekrani), dukkan_guncelle()]).pack(pady=10)
tk.Button(frame_ana_menu, text="📈 KRİPTO BORSA SİSTEMİ", font=("Courier New", 12, "bold"), bg="#8b5cf6", fg="white", width=30, height=1, command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_borsa_ekrani), borsa_ekrani_guncelle()]).pack(pady=10)
tk.Button(frame_ana_menu, text="🌌 ÖDÜLLÜ SİBER GÖREVLER", font=("Courier New", 12, "bold"), bg="#f43f5e", fg="white", width=30, height=1, command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_gorev_ekrani), gorev_paneli_guncelle()]).pack(pady=10)
tk.Button(frame_ana_menu, text="🎨 NEON TEMA SEÇİCİ", font=("Courier New", 12, "bold"), bg="#ec4899", fg="white", width=30, height=1, command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_tema_ekrani)]).pack(pady=10)
tk.Button(frame_ana_menu, text="🎁 GÜNLÜK DESTEK PAKETİ", font=("Courier New", 12, "bold"), bg="#06b6d4", fg="white", width=30, height=1, command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_destek_ekrani)]).pack(pady=10)
tk.Button(frame_ana_menu, text="🏆 EN İYİ OYUNCULAR LİSTESİ", font=("Courier New", 12, "bold"), bg="#14b8a6", fg="white", width=30, height=1, command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_lider_ekrani), l_guncelle()]).pack(pady=10)

# --- 3. SAHNE: ANA OYUN EKRANI ARAYÜZÜ ---
lbl_durum = tk.Label(frame_ana_oyun, text="", font=("Courier New", 11, "bold"), bg="#1e293b", fg="#38bdf8", bd=2, relief="groove")
lbl_durum.pack(pady=10, fill=tk.X, padx=10)
frame_siniflar = tk.Frame(frame_ana_oyun, bg="#0f172a")
frame_siniflar.pack(pady=8)
tk.Button(frame_siniflar, text="💻 Netrunner", bg="#0284c7", fg="white", font=("Courier New", 9, "bold"), command=lambda: [ses_cal("tus"), sinif_sec("Netrunner")]).pack(side=tk.LEFT, padx=3)
tk.Button(frame_siniflar, text="🤝 Fixer", bg="#d97706", fg="white", font=("Courier New", 9, "bold"), command=lambda: [ses_cal("tus"), sinif_sec("Fixer")]).pack(side=tk.LEFT, padx=3)
tk.Button(frame_siniflar, text="🦾 Solo", bg="#dc2626", fg="white", font=("Courier New", 9, "bold"), command=lambda: [ses_cal("tus"), sinif_sec("Solo")]).pack(side=tk.LEFT, padx=3)

lbl_secili_sinif_gosterge = tk.Label(frame_ana_oyun, text=f"🚩 Sınıf: {secili_sinif}", font=("Courier New", 10, "bold"), bg="#0f172a", fg="#38bdf8")
lbl_secili_sinif_gosterge.pack()

frame_hack = tk.LabelFrame(frame_ana_oyun, text=" 🔐 MAINFRAME ENCRYPTION CRACKER ", font=("Courier New", 10, "bold"), bg="#0f172a", fg="#facc15", padx=10, width=20)
frame_hack.pack(pady=10, fill=tk.X, padx=10)
ent_tahmin = tk.Entry(frame_hack, font=("Courier New", 14, "bold"), justify="center", width=10, bg="#1e293b", fg="#10b981", insertbackground="white")
ent_tahmin.pack(pady=5)
tk.Button(frame_hack, text="🚀 ENJEKTE ET", font=("Courier New", 11, "bold"), bg="#10b981", fg="white", width=20, command=tahmin_et).pack(pady=2)

frame_boss = tk.LabelFrame(frame_ana_oyun, text=" ⚔️ ENDGAME PROTOCOL: BOSS RAID ", font=("Courier New", 10, "bold"), bg="#0f172a", fg="#ef4444", padx=10, pady=5)
frame_boss.pack(pady=5, fill=tk.X, padx=10)
lbl_boss_durum = tk.Label(frame_boss, text=f"👁‍🗨 {ai_adi} HP: 100% | 👤 Senin HP: 100%", font=("Courier New", 10, "bold"), bg="#0f172a", fg="#f87171")
lbl_boss_durum.pack(pady=3)
tk.Button(frame_boss, text="💥 Atak", bg="#b91c1c", fg="white", font=("Courier New", 9, "bold"), command=lambda: boss_saldir("hack")).pack(side=tk.LEFT, expand=True, padx=2)
tk.Button(frame_boss, text="✨ Sınıf Yeteneği", bg="#a855f7", fg="white", font=("Courier New", 9, "bold"), command=lambda: boss_saldir("yetenek")).pack(side=tk.LEFT, expand=True, padx=2)
tk.Button(frame_boss, text="🛡️ Defans", bg="#475569", fg="white", font=("Courier New", 9, "bold"), command=lambda: boss_saldir("savunma")).pack(side=tk.LEFT, expand=True, padx=2)

txt_konsol = tk.Text(frame_ana_oyun, height=8, bg="#020617", fg="#10b981", font=("Courier New", 9), state=tk.DISABLED)
txt_konsol.pack(pady=5, fill=tk.X, padx=15)
tk.Button(frame_ana_oyun, text="⬅️ ANA MENÜYE DÖN", bg="#475569", fg="white", font=("Courier New", 11, "bold"), command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_ana_menu)]).pack(pady=10)
# --- 4. SAHNE: BAĞIMSIZ ENVANTER (ÇANTA) ARAYÜZÜ ---
lbl_e_liste = tk.Label(frame_envanter_ekrani, text="", font=("Courier New", 12, "bold"), bg="#0f172a", fg="#facc15", justify="left")
lbl_e_liste.pack(pady=50)
tk.Button(frame_envanter_ekrani, text="🧪 Siber Sağlık İksiri Tüket (+40 HP)", bg="#10b981", fg="white", font=("Courier New", 11, "bold"), width=35, command=iksir_kullan).pack(pady=8)
tk.Button(frame_envanter_ekrani, text="🃏 Sistem Reboot Kartı Kullan (10 Hak)", bg="#3b82f6", fg="white", font=("Courier New", 11, "bold"), width=35, command=reboot_kart_kullan).pack(pady=8)
tk.Button(frame_envanter_ekrani, text="⬅️ ANA MENÜYE DÖN", bg="#475569", fg="white", font=("Courier New", 11, "bold"), command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_ana_menu)]).pack(pady=40)

# --- 5. SAHNE: BAĞIMSIZ MAĞAZA ARAYÜZÜ ---
lbl_m_cuzdan = tk.Label(frame_magaza_ekrani, text="", font=("Courier New", 14, "bold"), bg="#1e293b", fg="#facc15")
lbl_m_cuzdan.pack(pady=20)
btn_m_cpu = tk.Button(frame_magaza_ekrani, text="", bg="#10b981", fg="white", font=("Courier New", 10, "bold"), command=lambda: satinal("cpu"))
btn_m_cpu.pack(pady=8, fill=tk.X, padx=50)
btn_m_ram = tk.Button(frame_magaza_ekrani, text="", bg="#10b981", fg="white", font=("Courier New", 10, "bold"), command=lambda: satinal("ram"))
btn_m_ram.pack(pady=8, fill=tk.X, padx=50)
btn_m_cyber = tk.Button(frame_magaza_ekrani, text="", bg="#10b981", fg="white", font=("Courier New", 10, "bold"), command=lambda: satinal("cyber"))
btn_m_cyber.pack(pady=8, fill=tk.X, padx=50)
btn_m_goz = tk.Button(frame_magaza_ekrani, text="", bg="#3b82f6", fg="white", font=("Courier New", 10, "bold"), command=lambda: satinal("goz"))
btn_m_goz.pack(pady=8, fill=tk.X, padx=50)
btn_m_kalp = tk.Button(frame_magaza_ekrani, text="", bg="#ef4444", fg="white", font=("Courier New", 10, "bold"), command=lambda: satinal("kalp"))
btn_m_kalp.pack(pady=8, fill=tk.X, padx=50)
btn_m_iksir = tk.Button(frame_magaza_ekrani, text="", bg="#a855f7", fg="white", font=("Courier New", 10, "bold"), command=lambda: satinal("iksir"))
btn_m_iksir.pack(pady=8, fill=tk.X, padx=50)
btn_m_kart = tk.Button(frame_magaza_ekrani, text="", bg="#ec4899", fg="white", font=("Courier New", 10, "bold"), command=lambda: satinal("kart"))
btn_m_kart.pack(pady=8, fill=tk.X, padx=50)
tk.Button(frame_magaza_ekrani, text="⬅️ ANA MENÜYE DÖN", bg="#475569", fg="white", font=("Courier New", 11, "bold"), command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_ana_menu)]).pack(pady=30)

# --- 6. SAHNE: BAĞIMSIZ KRİPTO BARSASI ---
lbl_b_durum = tk.Label(frame_borsa_ekrani, text="", font=("Courier New", 14, "bold"), bg="#0f172a", fg="#a855f7")
lbl_b_durum.pack(pady=50)
tk.Button(frame_borsa_ekrani, text="🪙 YanCoin Satın Al", bg="#8b5cf6", fg="white", font=("Courier New", 11, "bold"), width=25, command=lambda: b_islem("al")).pack(pady=10)
tk.Button(frame_borsa_ekrani, text="💸 YanCoin Sat", bg="#a855f7", fg="white", font=("Courier New", 11, "bold"), width=25, command=lambda: b_islem("sat")).pack(pady=10)
tk.Button(frame_borsa_ekrani, text="⬅️ ANA MENÜYE DÖN", bg="#475569", fg="white", font=("Courier New", 11, "bold"), command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_ana_menu)]).pack(pady=60)

# --- 7. SAHNE: BAĞIMSIZ ÖDÜLLÜ GÖREVLER ---
tk.Label(frame_gorev_ekrani, text="🌌 ŞİRKET SİBER GÖREVLERİ 🌌\n\nGörevleri tamamlamak için donanım\nseviyelerinizi geliştirmelisiniz.", font=("Courier New", 12, "bold"), bg="#0f172a", fg="#f43f5e", justify="center").pack(pady=40)
btn_g1 = tk.Button(frame_gorev_ekrani, text="", bg="#4c1d95", fg="white", font=("Courier New", 11, "bold"), width=40, height=2, command=lambda: gorev_yap(1))
btn_g1.pack(pady=15)
btn_g2 = tk.Button(frame_gorev_ekrani, text="", bg="#4c1d95", fg="white", font=("Courier New", 11, "bold"), width=40, height=2, command=lambda: gorev_yap(2))
btn_g2.pack(pady=15)
tk.Button(frame_gorev_ekrani, text="⬅️ ANA MENÜYE DÖN", bg="#475569", fg="white", font=("Courier New", 11, "bold"), command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_ana_menu)]).pack(pady=50)

# --- 8. SAHNE: BAĞIMSIZ TEMA EKRANI ---
lbl_tema_durum = tk.Label(frame_tema_ekrani, text="🎨 NEON ARAYÜZ TEMA ÖZELLEŞTİRİCİ", font=("Courier New", 14, "bold"), bg="#0f172a", fg="#ec4899")
lbl_tema_durum.pack(pady=50)
tk.Button(frame_tema_ekrani, text="🔵 SİBER GECE MAVİSİ (VARSAYILAN)", bg="#1e3a8a", fg="white", font=("Courier New", 11, "bold"), width=35, command=lambda: tema_uygula("Mavi")).pack(pady=12)
tk.Button(frame_tema_ekrani, text="🟢 MATRIX MATRIX YEŞİLİ", bg="#065f46", fg="white", font=("Courier New", 11, "bold"), width=35, command=lambda: tema_uygula("Matrix")).pack(pady=12)
tk.Button(frame_tema_ekrani, text="🟣 CYBERPUNK FUŞYA NEON", bg="#701a75", fg="white", font=("Courier New", 11, "bold"), width=35, command=lambda: tema_uygula("Neon")).pack(pady=12)
tk.Button(frame_tema_ekrani, text="⬅️ ANA MENÜYE DÖN", bg="#475569", fg="white", font=("Courier New", 11, "bold"), command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_ana_menu)]).pack(pady=60)

# --- 9. SAHNE: BAĞIMSIZ GÜNLÜK DESTEK ARAYÜZÜ ---
lbl_destek_baslik = tk.Label(frame_destek_ekrani, text="🎁 SİBER DESTEK MERKEZİ\n\nGünlük siber yardım paketi protokolünü\nbaşlatmak için aşağıdaki butona tıklayın.", font=("Courier New", 12, "bold"), bg="#0f172a", fg="#06b6d4", justify="center")
lbl_destek_baslik.pack(pady=80)
tk.Button(frame_destek_ekrani, text="⚡ MATRİX BAĞLANTISI KUR (ÖDÜLÜ AL)", bg="#06b6d4", fg="white", font=("Courier New", 12, "bold"), padx=10, pady=10, command=gunluk_odul_al_baamsiz).pack(pady=20)
tk.Button(frame_destek_ekrani, text="⬅️ ANA MENÜYE DÖN", bg="#475569", fg="white", font=("Courier New", 11, "bold"), command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_ana_menu)]).pack(pady=40)

# --- 10. SAHNE: EN İYİ OYUNCULAR LİSTESİ ---
lbl_l_liste = tk.Label(frame_lider_ekrani, text="", font=("Courier New", 13, "bold"), bg="#0f172a", fg="#14b8a6", justify="left")
lbl_l_liste.pack(pady=60)
tk.Button(frame_lider_ekrani, text="⬅️ ANA MENÜYE DÖN", bg="#475569", fg="white", font=("Courier New", 11, "bold"), command=lambda: [ses_cal("tus"), ekrani_temizle_ve_ac(frame_ana_menu)]).pack(pady=40)
def l_guncelle():
    liderler = liderleri_yukle()
    metin = "🔥 EN İYİ OYUNCULAR LİSTESİ 🔥\n\n"
    madalyalar = ["🥇", "🥈", "🥉"]
    for i, (isim, hamle) in enumerate(liderler):
        metin += f"{madalyalar[i]} {i+1}. {isim} -> {hamle} Hamle\n"
    if not liderler: metin += "Veritabanı temiz. İlk rekoru sen kır!"
    lbl_l_liste.config(text=metin)

# --- SİSTEMİ ATEŞLE ---
skoru_yukle()
konsol_yaz("Yanmet OS v8.0 başarıyla yüklendi.", "SYS")
pencere.after(500, siber_giris_muzigi)
pencere.mainloop()
