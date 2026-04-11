# Setup Hosting - Dokumentasi

## Perubahan yang Dilakukan

Website sekarang menggunakan **SQLite Database** untuk menyimpan data form kontak, sehingga data akan tersimpan secara permanent di hosting.

### Fitur Baru:
- ✅ Form kontak disimpan ke database `madrasah.db`
- ✅ Data pesan tidak hilang saat restart server
- ✅ Berfungsi sempurna di berbagai platform hosting
- ✅ Notifikasi sukses dan error pada form

## Langkah-Langkah Setup di Hosting

### 1. **Update Dependencies**
Pastikan requirements.txt sudah ter-update dengan Flask-SQLAlchemy:
```
Flask==3.1.2
Flask-SQLAlchemy==3.1.1
```

Jalankan di hosting:
```bash
pip install -r requirements.txt
```

### 2. **Folder Structure**
Pastikan folder structure seperti ini:
```
web_mdta/
├── app.py
├── requirements.txt
├── SETUP_HOSTING.md
├── static/
│   ├── css/
│   ├── images/
│   └── js/
├── templates/
│   ├── base.html
│   ├── contact.html
│   └── ... (template lainnya)
└── madrasah.db (akan dibuat otomatis saat pertama kali run)
```

### 3. **Environment Variables** (Opsional)
Jika hosting memungkinkan, set environment variable:
```bash
FLASK_ENV=production
FLASK_DEBUG=False
```

### 4. **Database Initialization**
Database `madrasah.db` akan **dibuat otomatis** saat aplikasi pertama kali dijalankan. Tidak perlu membuat secara manual.

### 5. **Verifikasi**
Setelah deploy:
1. Buka halaman `/contact`
2. Isi form dengan test data
3. Klik "Kirim Pesan"
4. Jika muncul pesan "Pesan Anda berhasil dikirim!", berarti berhasil ✅

## File yang Diubah

### app.py
- Menambahkan `Flask-SQLAlchemy` untuk database
- Model `Message` untuk menyimpan pesan kontak
- Route `/contact` yang menangani POST request
- Auto-create tables dengan `db.create_all()`

### requirements.txt
- Menambahkan `Flask-SQLAlchemy==3.1.1`

### templates/contact.html
- Menambahkan error message notification
- Form tetap sama, hanya penambahan pesan feedback

## Troubleshooting

### Problem: Form tidak menyimpan data
**Solusi:**
- Pastikan file memiliki permission write (chmod 755)
- Cek bahwa Flask-SQLAlchemy terinstall: `pip install Flask-SQLAlchemy`
- Lihat error log di server hosting

### Problem: Database corrupted
**Solusi:**
- Hapus file `madrasah.db`
- Restart aplikasi, database akan dibuat ulang otomatis

### Problem: Error "ModuleNotFoundError: No module named 'flask_sqlalchemy'"
**Solusi:**
```bash
pip install -r requirements.txt
pip install Flask-SQLAlchemy==3.1.1
```

## Hosting Recommendations

Aplikasi ini bisa di-deploy ke:
- ✅ Heroku
- ✅ PythonAnywhere
- ✅ Replit
- ✅ Railway
- ✅ Render
- ✅ DigitalOcean
- ✅ VPS (Linode, Vultr, etc)
- ✅ Shared Hosting dengan Python support

## Backup Data

Untuk backup data form yang sudah disimpan:
1. Download file `madrasah.db` dari server hosting
2. Simpan di lokasi aman
3. Jika perlu restore, upload kembali file tersebut

## Support

Jika ada masalah dengan database atau form submission, hubungi developer untuk bantuan setup database lebih lanjut.
