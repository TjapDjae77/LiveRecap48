let player;

// Fungsi untuk mengkonversi detik ke format timestamp [HH:MM:SS]
function formatTimestamp(seconds) {
    
    // Memastikan seconds adalah angka
    seconds = parseFloat(seconds);
    
    // Menghitung jam, menit, dan detik
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    
    // Format dengan leading zeros
    const formatted = [
        hours.toString().padStart(2, '0'),
        minutes.toString().padStart(2, '0'),
        remainingSeconds.toString().padStart(2, '0')
    ].join(':');
    
    return `[${formatted}]`;
}

// Fungsi untuk memformat semua timestamp saat halaman dimuat
function formatAllTimestamps() { 
    const elements = document.querySelectorAll('[data-timestamp]');
    
    elements.forEach(element => {
        const timestamp = element.getAttribute('data-timestamp');
        element.textContent = formatTimestamp(timestamp);
    });
}

// Panggil fungsi format saat halaman dimuat
document.addEventListener('DOMContentLoaded', () => {
    formatAllTimestamps();
});

// Inisialisasi YouTube Player
function onYouTubeIframeAPIReady() {
    player = new YT.Player('youtubePlayer', {
        events: {
            'onReady': onPlayerReady
        }
    });
}

function onPlayerReady(event) {
   
}

function seekToTimestamp(timestamp) {
    if (player && player.seekTo) {
        player.seekTo(timestamp);
        // Scroll halus ke bagian atas halaman
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }
}