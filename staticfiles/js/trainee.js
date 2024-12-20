document.addEventListener('DOMContentLoaded', function() {
    // Tambahkan event listener untuk tombol favorite
    const favoriteButtons = document.querySelectorAll('.favorite-btn');
    favoriteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.stopPropagation(); // Mencegah event bubble ke parent
            const traineeId = this.dataset.traineeId;
            const unfavoriteIcon = this.querySelector('.unfavorite-icon');
            const favoriteIcon = this.querySelector('.favorite-icon');

            // Toggle icon
            unfavoriteIcon.classList.toggle('hidden');
            favoriteIcon.classList.toggle('hidden');

            // Di sini bisa ditambahkan AJAX request ke backend untuk menyimpan status favorite
        });
    });
});