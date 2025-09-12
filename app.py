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
    'gallery_images': [
        {'src': 'gallery/foto11.jpg', 'alt': 'Santri Belajar Di Kelas'},
        {'src': 'gallery/foto1.jpg', 'alt': 'Santri Mengikuti Ujian Akhir Madrasah'},
        {'src': 'gallery/foto2.jpg', 'alt': 'Kegiatan PERSADA (Perkemahan Santri Diniyah)'},
        {'src': 'gallery/foto3.jpg', 'alt': 'Ziarah Jawa Tengah Bersama Santriwan dan Santriwati'},
        {'src': 'gallery/foto4.jpg', 'alt': 'Juara Kegiatan PORSADIN (Pekan Olahraga dan Seni Antar Diniyah) Tingkat Kecamatan'},
        {'src': 'gallery/foto5.jpg', 'alt': 'Juara Kegiatan PORSADIN (Pekan Olahraga dan Seni Antar Diniyah) Tingkat Kecamatan'},
        {'src': 'gallery/foto6.jpg', 'alt': 'Pawai Taaruf Santri'},
        {'src': 'gallery/foto9.jpg', 'alt': 'Haflah Penampilan Santri'},
        {'src': 'gallery/foto7.jpg', 'alt': 'Pembagian Kenang-Kenangan Santri Kelas 4'},
        {'src': 'gallery/foto8.jpg', 'alt': 'Pembagian Ta’jil Pada Bulan Ramadhan'},
        {'src': 'gallery/foto10.jpg', 'alt': 'Mengikuti Kegiatan Upacara Dalam Rangka Hari Santri Nasional'},
        {'src': 'gallery/foto12.jpg', 'alt': 'Santri Kelas 4'},
    ],
    # Data khusus untuk halaman PSDB
    'psdb_info': {
        'title': 'Penerimaan Santri Didik Baru',
        'subtitle': 'Bergabunglah dengan keluarga besar Madrasah Nurul Huda!',
        'description': 'Kami membuka kesempatan bagi calon santri berprestasi untuk menempuh pendidikan terbaik dengan kurikulum terpadu dan lingkungan Islami yang kondusif. Raih masa depan cerah bersama kami!',
        'image': 'psdb-banner.jpg', # Pastikan gambar ini ada di static/images/
        'whatsapp_number': '6282323939692', # Ganti dengan nomor WhatsApp Anda
        'whatsapp_message': 'Assalamualaikum, saya ingin mendaftar Penerimaan Santri Didik Baru di Madrasah Nurul Huda. Mohon informasinya.'
    },
    # Tambahkan informasi kontak di sini agar lebih dinamis
    'contact_info_data': {
        'address': 'Jl. Brawijaya No. 168, Muarareja, Kota Tegal, Jawa Tengah, Indonesia',
        'phone': '+62 823-1393-1437',
        'email': 'mdtanurulhudamuarareja@gmail.com',
        'hours': 'Senin - Sabtu, 15:00 - 17:00',
        'instagram_url': 'https://www.instagram.com/mdtanurulhudamj?igsh=eHpvY21laXRtOXM=',
        'google_maps_embed_url': 'https://www.google.com/maps/embed?pb=!4v1757684514102!6m8!1m7!1sZxB6jrXqgoKzA31o7zCVZg!2m2!1d-6.847288180137246!2d109.1093265261672!3f336!4f0!5f0.7820865974627469'
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
    # Kirim data kontak ke template
    return render_template('contact.html', data=madrasah_data)

if __name__ == '__main__':
    app.run(debug=True)