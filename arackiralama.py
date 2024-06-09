from tkinter import *
from tkinter import messagebox
from datetime import datetime


class AracKiralamaSistemi:
    def __init__(self,ekran):
        self.ekran=ekran
        self.ekran.title("Arac Kiralama Sistemi")
        
        self.araclar=[]
        self.musteriler=[]
        self.kiralamalar=[]
        
        self.ekrani_olustur()
        
    def ekrani_olustur(self):
        Label(self.ekran,text="Arac Ekle").grid(row=0,column=0,pady=10)
        
        Label(self.ekran,text="Marka").grid(row=1,column=0)
        self.arac_marka=Entry(self.ekran)
        self.arac_marka.grid(row=1,column=1)
        
        Label(self.ekran,text="Model").grid(row=2,column=0)
        self.arac_model=Entry(self.ekran)
        self.arac_model.grid(row=2,column=1)
        
        Label(self.ekran,text="Plaka").grid(row=3,column=0)
        self.arac_plaka=Entry(self.ekran)
        self.arac_plaka.grid(row=3,column=1)
        
        Label(self.ekran,text="Kiralama Ücreti").grid(row=4,column=0)
        self.arac_ucret=Entry(self.ekran)
        self.arac_ucret.grid(row=4,column=1)
        
        Button(self.ekran,text="Arac Ekle",command=self.aracEkle).grid(row=5,column=1,pady=10)
        
        
        Label(self.ekran, text="Müşteri Ekle").grid(row=0,column=2,pady=10)
        
        Label(self.ekran, text="Ad").grid(row=1, column=2)
        self.musteri_ad = Entry(self.ekran)
        self.musteri_ad.grid(row=1, column=3)
        
        Label(self.ekran, text="Soyad").grid(row=2, column=2)
        self.musteri_soyad =Entry(self.ekran)
        self.musteri_soyad.grid(row=2, column=3)
        
        Label(self.ekran, text="Müşteri No").grid(row=3, column=2)
        self.musteri_no = Entry(self.ekran)
        self.musteri_no.grid(row=3, column=3)
        
        Label(self.ekran, text="Ehliyet Bilgileri").grid(row=4, column=2)
        self.musteri_ehliyet = Entry(self.ekran)
        self.musteri_ehliyet.grid(row=4, column=3)
        
        Button(self.ekran,text="Müsteri Ekle",command=self.musteriEkle).grid(row=5,column=3,pady=10)
        
        
        Label(self.ekran, text="Kiralama İşlemi").grid(row=6, column=0, pady=10)
        Label(self.ekran, text="Araç Plakası").grid(row=7, column=0)
        self.kiralama_arac = Entry(self.ekran)
        self.kiralama_arac.grid(row=7, column=1)
        
        Label(self.ekran, text="Müşteri No").grid(row=8, column=0)
        self.kiralama_musteri = Entry(self.ekran)
        self.kiralama_musteri.grid(row=8, column=1)
        
        Label(self.ekran, text="Kiralama Tarihi (YYYY-MM-DD)").grid(row=9, column=0)
        self.kiralama_tarih = Entry(self.ekran)
        self.kiralama_tarih.grid(row=9, column=1)
        
        Label(self.ekran, text="İade Tarihi (YYYY-MM-DD)").grid(row=10, column=0)
        self.iade_tarih = Entry(self.ekran)
        self.iade_tarih.grid(row=10, column=1)
        
        Button(self.ekran,text="Kiralama Yap").grid(row=11,column=1,pady=10)
        
        self.aracResmi=PhotoImage(file="pngwing.com.png")
        Label(self.ekran,image=self.aracResmi).grid(row=12,column=0,columnspan=4)
        
    def aracEkle(self):
           marka=self.arac_marka.get()
           model=self.arac_model.get()
           plaka=self.arac_plaka.get()
           ucret=self.arac_ucret.get()
           
           yeniArac=Arac(marka,model,plaka,ucret)
           self.araclar.append(yeniArac)
           messagebox.showinfo("Islem basarili","Araciniz basariyla kaydedildi")
    
    def musteriEkle(self):
         ad=self.musteri_ad.get()
         soyad=self.musteri_soyad.get()
         musteriNo=self.musteri_no.get()
         ehliyetInfo=self.musteri_ehliyet.get()
        
         yeniMusteri=Musteri(ad,soyad,musteriNo,ehliyetInfo)
         self.musteriler.append(yeniMusteri)
         messagebox.showinfo("Islem basarili","Bilgileriniz basariyla kaydedildi")
         
    def Kiralama(self):
        kiralanacakArac=self.kiralama_arac.get()
        kiralayacakMusteri=self.kiralama_musteri.get()
        alinanTarih=self.kiralama_tarih.get()
        teslimTarih=self.iade_tarih.get()
        
        for Arac in self.araclar:
            if arac.plaka==kiralanacakArac:
                for Musteri in self.musteriler:
                    if Musteri==kiralayacakMusteri:
                        messagebox.showinfo("Islem basarili","Kiralama islemi basariyla gerceklesti")
        
        
        
        
class Arac:
    def __init__(self,marka,model,plaka,ucret):
        self.marka=marka
        self.model=model
        self.plaka=plaka
        self.ucret=ucret
        
class Musteri:
    def __init__(self,ad,soyad,musteriNo,ehliyetInfo):
        self.ad=ad
        self.soyad=soyad
        self.musteriNo=musteriNo
        self.ehliyetInfo=ehliyetInfo
        
class Kiralama:
    def __init__(self,arac,musteri,tarih,iadeTarihi):
        self.arac=arac
        self.musteri=musteri
        self.tarih=tarih
        self.iadetarihi=iadeTarihi
        
ekran=Tk()
app=AracKiralamaSistemi(ekran)

ekran.mainloop()