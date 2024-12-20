document.addEventListener("DOMContentLoaded", () => {
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const mobileSidebar = document.getElementById('mobileSidebar');
    const closeSidebarBtn = document.getElementById('closeSidebarBtn');
    const sidebarOverlay = document.getElementById('sidebarOverlay');
    const dropdownContainer = document.querySelector('.dropdown-container');
    const dropdownButton = document.getElementById("dropdownButton");
    const dropdownMenu = document.getElementById("dropdownMenu");
    const expandIcon = document.getElementById("expandIcon");
    let isDropdownOpen = false;
    let isClickToggled = false;

    // Fungsi untuk membuka dropdown
    function showDropdown() {
        if (!isClickToggled) {
            dropdownMenu.classList.remove('hidden');
            expandIcon.style.transform = 'rotate(180deg)';
        }
    }

    // Fungsi untuk menutup dropdown
    function hideDropdown() {
        if (!isDropdownOpen && !dropdownContainer.matches(':hover')) {
            dropdownMenu.classList.add('hidden');
            expandIcon.style.transform = 'rotate(0deg)';
            isClickToggled = false;
        }
    }

    if (dropdownContainer) {
        dropdownContainer.addEventListener('mouseenter', showDropdown);
        dropdownContainer.addEventListener('mouseleave', hideDropdown);
    }

    function openSidebar() {
        mobileSidebar.classList.remove('-translate-x-full');
        sidebarOverlay.classList.remove('hidden');
        document.body.style.overflow = 'hidden';
    }

    function closeSidebar() {
        mobileSidebar.classList.add('-translate-x-full');
        sidebarOverlay.classList.add('hidden');
        document.body.style.overflow = '';
    }

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', openSidebar);
    }
    
    if (closeSidebarBtn) {
        closeSidebarBtn.addEventListener('click', closeSidebar);
    }
    
    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', closeSidebar);
    }
    
    if (dropdownContainer) {
        dropdownButton.addEventListener('click', function(e) {
            e.stopPropagation();
            isDropdownOpen = !isDropdownOpen;
        isClickToggled = !isDropdownOpen;
        if (isDropdownOpen) {
            dropdownMenu.classList.remove('hidden');    
            expandIcon.style.transform = 'rotate(180deg)';
        } else {
            dropdownMenu.classList.add('hidden');
                expandIcon.style.transform = 'rotate(0deg)';
            }
        });
    }

    // Menutup dropdown ketika mengklik di luar
    document.addEventListener('click', function(e) {
        if(dropdownContainer){
            if (!dropdownContainer.contains(e.target)) {
                isDropdownOpen = false;
                isClickToggled = false;
                hideDropdown();
            }
        }
    });
});