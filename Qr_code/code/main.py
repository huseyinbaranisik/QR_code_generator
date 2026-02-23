import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk, ImageFilter
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

ctk.set_appearance_mode("Dark")

class QRCodeApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pencereyi eski boyutuna getirdik (340x520)
        self.title("QR")
        self.geometry("340x520") 
        self.configure(fg_color="#121212")
        self.resizable(False, False)
        
        # İkon Ayarla
        icon_path = resource_path("icon/icon.png")
        if os.path.exists(icon_path):
            try:
                img = Image.open(icon_path)
                photo = ImageTk.PhotoImage(img)
                self.wm_iconphoto(True, photo)
            except: pass

        # Pencereyi merkeze al
        self.update_idletasks()
        width, height = 340, 520
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')

        # Başlık
        self.title_label = ctk.CTkLabel(self, text="QR OLUŞTURUCU", font=("Segoe UI", 16, "bold"), text_color="#bb86fc")
        self.title_label.pack(pady=(20, 10))

        # QR Konteynırı (Eski Boyut: 320x320)
        self.container = ctk.CTkFrame(self, width=320, height=320, fg_color="#1e1e1e", corner_radius=5)
        self.container.pack(pady=10)
        self.container.pack_propagate(False)

        # Ana QR Label (Eski Boyut: 280x280)
        self.qr_display = tk.Label(self.container, bg="#1e1e1e", cursor="hand2")
        self.qr_display.place(relx=0.5, rely=0.5, anchor="center", width=280, height=280)
        
        # Yer tutucu
        self.placeholder = ctk.CTkLabel(self.container, text="QR Hazır Değil", text_color="#444444", font=("Segoe UI", 11))
        self.placeholder.place(relx=0.5, rely=0.5, anchor="center")

        # İndir Butonu
        self.download_btn = ctk.CTkButton(self.container, text="⬇ İNDİR", command=self.save_qr, 
                                         fg_color="#4a148c", hover_color="#7b1fa2", 
                                         width=100, height=35, corner_radius=5, font=("Segoe UI", 12, "bold"))

        # Giriş Alanı
        self.url_entry = ctk.CTkEntry(self, width=320, height=42, corner_radius=5, 
                                     fg_color="#2c2c2c", border_color="#333333", 
                                     placeholder_text="Link veya metin gir...", border_width=1)
        self.url_entry.pack(pady=(15, 5))
        
        # Oluştur Butonu
        self.generate_btn = ctk.CTkButton(self, text="Oluştur", command=self.generate_qr, 
                                          fg_color="#4a148c", hover_color="#7b1fa2", 
                                          width=320, height=48, corner_radius=5, font=("Segoe UI", 14, "bold"))
        self.generate_btn.pack(pady=10)
        
        # Mouse Olayları
        self.qr_display.bind("<Enter>", self.on_hover_enter)
        self.qr_display.bind("<Leave>", self.on_hover_leave)
        self.container.bind("<Leave>", self.on_hover_leave)
        self.download_btn.bind("<Enter>", self.on_hover_enter)

        self.current_qr_img = None
        self.blurred_qr_tk = None
        self.normal_qr_tk = None

    def generate_qr(self):
        data = self.url_entry.get().strip()
        if not data:
            messagebox.showwarning("Uyarı", "Lütfen bir şeyler yazın!")
            return
            
        try:
            qr = qrcode.QRCode(version=1, box_size=10, border=1)
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
            
            self.current_qr_img = img
            
            # Eski boyuta geri dönüldü: 280x280
            display_img = img.resize((280, 280), Image.Resampling.LANCZOS)
            self.normal_qr_tk = ImageTk.PhotoImage(display_img)
            
            # Blur versiyon
            blur_img = display_img.filter(ImageFilter.GaussianBlur(radius=8))
            self.blurred_qr_tk = ImageTk.PhotoImage(blur_img)
            
            self.qr_display.config(image=self.normal_qr_tk)
            self.placeholder.place_forget()
            self.download_btn.place_forget()
            
        except Exception as e:
            messagebox.showerror("Hata", f"Hata: {e}")

    def on_hover_enter(self, event):
        if self.current_qr_img:
            self.qr_display.config(image=self.blurred_qr_tk)
            self.download_btn.place(relx=0.5, rely=0.5, anchor="center")

    def on_hover_leave(self, event):
        # Fare gerçekten konteynırın dışına çıktı mı kontrol et
        x, y = self.winfo_pointerxy()
        widget = self.winfo_containing(x, y)
        
        if widget not in [self.qr_display, self.download_btn]:
            self.download_btn.place_forget()
            if self.normal_qr_tk:
                self.qr_display.config(image=self.normal_qr_tk)

    def save_qr(self):
        if self.current_qr_img:
            path = filedialog.asksaveasfilename(defaultextension=".png", 
                                               filetypes=[("PNG", "*.png")],
                                               parent=self) # Diyaloğu ortala
            if path:
                self.current_qr_img.save(path)
                messagebox.showinfo("Başarılı", "PNG olarak kaydedildi!", parent=self) # Uyarıyı ortala

if __name__ == "__main__":
    app = QRCodeApp()
    app.mainloop()
