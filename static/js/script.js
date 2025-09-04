document.addEventListener('DOMContentLoaded', () => {
    // Fungsi untuk memicu animasi saat elemen masuk ke viewport
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Hentikan pengamatan setelah animasi berjalan
                observer.unobserve(entry.target);
            }
        });
    }, {
        // threshold 0.2 = animasi akan dimulai saat 20% bagian dari elemen terlihat
        threshold: 0.2
    });

    // Ambil semua elemen yang memiliki kelas 'animate-on-scroll'
    const elementsToAnimate = document.querySelectorAll('.animate-on-scroll');

    // Mulai pengamatan untuk setiap elemen
    elementsToAnimate.forEach(element => {
        observer.observe(element);
    });

    // --- Kode untuk Slideshow Hero Section ---
    let slideIndex = 0;
    const slides = document.querySelectorAll('.slideshow-container .slide');

    function showSlides() {
        if (slides.length === 0) return; // Tidak ada slide, keluar

        // Sembunyikan semua slide
        slides.forEach(slide => {
            slide.classList.remove('active');
        });

        // Pindah ke slide berikutnya
        slideIndex++;
        if (slideIndex > slides.length) {
            slideIndex = 1; // Kembali ke slide pertama
        }

        // Tampilkan slide saat ini
        slides[slideIndex - 1].classList.add('active');

        // Ganti slide setiap 5 detik (5000 milidetik)
        setTimeout(showSlides, 5000);
    }

    // Jalankan slideshow jika ada slide
    if (slides.length > 0) {
        // Panggil showSlides pertama kali setelah DOMContentLoaded untuk menampilkan slide awal
        showSlides();
    }

    // --- Kode untuk Hamburger Menu (Mobile Navigation) ---
    const hamburger = document.querySelector('.hamburger');
    const navLinks = document.querySelector('.nav-links');

    if (hamburger && navLinks) {
        hamburger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            hamburger.innerHTML = navLinks.classList.contains('active') ? '&times;' : '&#9776;'; // Ganti ikon
        });

        // Tutup menu saat link diklik (opsional, untuk UX yang lebih baik)
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navLinks.classList.remove('active');
                hamburger.innerHTML = '&#9776;';
            });
        });
    }

    // --- Kode untuk menandai link navigasi yang aktif ---
    const currentPath = window.location.pathname;
    const navLinksList = document.querySelectorAll('.nav-links a');

    navLinksList.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        } else if (currentPath === '/' && link.getAttribute('href') === '/') {
            link.classList.add('active'); // Pastikan Beranda aktif di root path
        }
    });
});