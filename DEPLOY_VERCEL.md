# Panduan Deploy ke Vercel

Karena file `vercel.json` sudah ada di project, berikut adalah panduan lengkap deploy ke Vercel.

## Step 1: Install Vercel CLI

```bash
npm install -g vercel
```

## Step 2: Login ke Vercel

```bash
vercel login
```

## Step 3: Konfigurasi Vercel

File `vercel.json` sudah ada, pastikan konfigurasinya seperti ini:

```json
{
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

## Step 4: Update WSGI untuk Vercel

Buat file `wsgi.py` di root project:

```python
from app import app

if __name__ == "__main__":
    app.run()
```

## Step 5: Deploy

```bash
vercel
```

## PENTING: Database untuk Vercel

Vercel menggunakan ephemeral filesystem, artinya file akan hilang setiap kali deploy ulang.

### Solusi 1: Gunakan PostgreSQL (Recommended untuk Production)
1. Setup database eksternal di Supabase atau Railway
2. Update connection string di app.py
3. Ganti SQLite dengan PostgreSQL

### Solusi 2: Gunakan Serverless Database
- Supabase (PostgreSQL)
- Railway
- MongoDB Atlas

### Solusi 3: Gunakan File Storage Service
- AWS S3 untuk backup database
- Cloudinary untuk file storage

## Rekomendasi untuk Production

**Gunakan PostgreSQL + Railway:**

1. Setup di https://railway.app
2. Dapatkan DATABASE_URL
3. Update app.py:

```python
import os
from urllib.parse import quote_plus

# Production Database
if os.getenv('DATABASE_URL'):
    # Railway/Production
    db_url = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
else:
    # Development
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///madrasah.db'
```

4. Update requirements.txt untuk PostgreSQL:

```
Flask==3.1.2
Flask-SQLAlchemy==3.1.1
psycopg2-binary==2.9.9
```

## Testing Sebelum Deploy

```bash
# Local test
python app.py

# Buka http://localhost:5000
# Test form submission
# Cek apakah data tersimpan
```

## Monitoring Logs

```bash
# Lihat logs deployment
vercel logs

# Real-time logs
vercel logs --follow
```

## Troubleshooting

### Database error saat deploy
- Pastikan DATABASE_URL sudah di-set di Vercel environment
- Update requirements.txt dengan driver PostgreSQL

### Module not found
- Pastikan requirements.txt ter-update
- Run: `pip freeze > requirements.txt`

### Import error
- Pastikan file wsgi.py dibuat dengan benar
- Check file permissions

## Health Check URL

Setelah deploy, test dengan:
```
https://your-domain.vercel.app/
```

Harus menampilkan halaman beranda tanpa error.
