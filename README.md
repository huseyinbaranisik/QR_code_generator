<img src="docs/hero.png" alt="QR Code Generator: type a link or text, get a QR code. Left: the title and its stack, Python, CustomTkinter, Pillow and qrcode. Right: the app icon, a hand holding a phone that shows a QR code." width="100%">

<p align="center">
  <a href="#what-it-does">What it does</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#run-it">Run it</a> ·
  <a href="#türkçe">Türkçe</a>
</p>

**QR Code Generator** is a small desktop app. Type a link or any text, press the button, and save the QR code as a PNG. The interface is in Turkish.

**Built with:** Python · CustomTkinter · Pillow · qrcode.

## What it does

<table>
  <tr><td><b>Create</b></td><td>Turns a link or text into a QR code, and the code size grows to fit the content.</td></tr>
  <tr><td><b>Preview</b></td><td>Shows the code right away in a compact 340×520 dark window.</td></tr>
  <tr><td><b>Hover to save</b></td><td>Moving the mouse over the code blurs it and reveals the download button.</td></tr>
  <tr><td><b>Export</b></td><td>Saves the code as a PNG wherever you choose.</td></tr>
  <tr><td><b>Input check</b></td><td>Warns you if the field is empty.</td></tr>
</table>

## How it works

The whole app is one file, [`Qr_code/code/main.py`](Qr_code/code/main.py). `qrcode` builds the matrix and Pillow creates the normal and blurred previews. The saved PNG comes from the original image, not the resized preview.

## Run it

```bash
git clone https://github.com/huseyinbaranisik/QR_code_generator.git
cd QR_code_generator/Qr_code
pip install customtkinter pillow qrcode
python code/main.py
```

> [!NOTE]
> Run it from the `Qr_code` folder so the app can find its window icon.

## License

[MIT](LICENSE)

---

## Türkçe

**QR Code Generator**, küçük bir masaüstü uygulaması. Bir bağlantı ya da metin yaz, butona bas, QR kodu PNG olarak kaydet.

**Teknoloji:** Python · CustomTkinter · Pillow · qrcode.

### Neler yapıyor

- **Oluşturma:** Bağlantıyı ya da metni QR koda çevirir, kod boyutu içeriğe göre büyür.
- **Önizleme:** Kodu 340×520 boyutundaki koyu pencerede hemen gösterir.
- **Üzerine gelince kaydet:** Fare kodun üzerine gelince kod bulanıklaşır ve indirme butonu çıkar.
- **Dışa aktarma:** Kodu istediğin yere PNG olarak kaydeder.
- **Girdi kontrolü:** Alan boşsa uyarı verir.

### Nasıl çalışıyor

Uygulamanın tamamı tek dosyada: [`Qr_code/code/main.py`](Qr_code/code/main.py). `qrcode` matrisi üretir, Pillow normal ve bulanık önizlemeleri hazırlar. Kaydedilen PNG, küçültülmüş önizlemeden değil özgün görüntüden alınır.

### Çalıştır

```bash
git clone https://github.com/huseyinbaranisik/QR_code_generator.git
cd QR_code_generator/Qr_code
pip install customtkinter pillow qrcode
python code/main.py
```

> [!NOTE]
> Pencere ikonunun bulunması için uygulamayı `Qr_code` klasöründen çalıştır.

### Lisans

[MIT](LICENSE)
