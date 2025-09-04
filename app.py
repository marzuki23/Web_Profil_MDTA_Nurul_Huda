from flask import Flask, render_template

app = Flask(__name__)

madrasah_data = {
    'nama': 'Madrasah Hebat Bermartabat',
    'visi': 'Mencetak generasi muslim unggul, cerdas, berakhlak mulia, dan berwawasan global.',
    'misi': [
        'Menciptakan santri yang Qur’ani dan mampu mengamalkannya dalam kehidupan sehari-hari.',
        'Menciptakan santri yang terampil dalam berbagai kegiatan keagamaan.',
        'Menumbuhkan santri yang berjiwa sosial, peduli, dan bermanfaat bagi masyarakat.',
        'Membentuk santri yang cinta ilmu serta memiliki semangat belajar sepanjang hayat.'
    ],
    'programs': [
        {'title': 'Tahfidz Al-Qur\'an', 'desc': 'Program unggulan menghafal Al-Qur\'an dengan metode cepat dan efektif.'},
        {'title': 'Bahasa Arab dan Inggris', 'desc': 'Fokus pada kemampuan komunikasi aktif dalam bahasa Arab dan Inggris.'},
        {'title': 'Robotik dan Sains', 'desc': 'Mengembangkan kreativitas dan nalar ilmiah melalui kegiatan praktikum dan lomba.'},
    ],
    'about_cards': [
        {'image': 'about1.jpg', 'text': 'Lingkungan madrasah yang kondusif dan nyaman untuk belajar.'},
        {'image': 'about2.jpg', 'text': 'Fasilitas modern mendukung kegiatan akademik dan non-akademik.'},
        {'image': 'about3.jpg', 'text': 'Kegiatan ekstrakurikuler yang beragam untuk mengembangkan bakat dan minat.'},
    ],
    'gallery_images': [
        {'src': 'gallery/foto1.jpg', 'alt': 'Santri Belajar Di Kelas'},
        {'src': 'gallery/foto2.jpg', 'alt': 'Kegiatan PERSADA (Perkemahan Santri Diniyah)'},
        {'src': 'gallery/foto3.jpg', 'alt': 'Ziarah Jawa Tengah Bersama Santriwan dan Santriwati'},
        {'src': 'gallery/foto4.jpg', 'alt': 'Juara Kegiatan PORSADIN (Pekan Olahraga dan Seni Antar Diniyah) Tingkat Kecamatan'},
        {'src': 'gallery/foto5.jpg', 'alt': 'Studi lapangan siswa'},
        {'src': 'gallery/foto6.jpg', 'alt': 'Pawai Taaruf Santri'},
    ],
    # Data khusus untuk halaman PSDB
    'psdb_info': {
        'title': 'Penerimaan Santri Didik Baru',
        'subtitle': 'Bergabunglah dengan keluarga besar Madrasah Nurul Huda!',
        'description': 'Kami membuka kesempatan bagi calon santri berprestasi untuk menempuh pendidikan terbaik dengan kurikulum terpadu dan lingkungan Islami yang kondusif. Raih masa depan cerah bersama kami!',
        'image': 'psdb-banner.jpg', # Pastikan gambar ini ada di static/images/
        'whatsapp_number': '6282323939692', # Ganti dengan nomor WhatsApp Anda
        'whatsapp_message': 'Assalamualaikum, saya ingin mendaftar Penerimaan Santri Didik Baru di Madrasah Nurul Huda. Mohon informasinya.'
    }
}

@app.route('/')
def home():
    """Halaman Beranda"""
    return render_template('index.html', data=madrasah_data)

@app.route('/about')
def about():
    """Halaman Tentang Kami"""
    return render_template('about.html', data=madrasah_data)

@app.route('/programs')
def programs():
    """Halaman Program Unggulan"""
    return render_template('programs.html', data=madrasah_data)

@app.route('/gallery')
def gallery():
    """Halaman Galeri"""
    return render_template('gallery.html', data=madrasah_data)

@app.route('/psdb')
def psdb():
    """Halaman Penerimaan Santri Didik Baru"""
    return render_template('psdb.html', data=madrasah_data)

@app.route('/contact')
def contact():
    """Halaman Kontak"""
    return render_template('contact.html', data=madrasah_data)

if __name__ == '__main__':
    app.run(debug=True)