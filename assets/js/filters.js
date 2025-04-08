// assets/js/filters.js
console.log("filters.js yüklendi.");

// Filtreleme mantığı buraya eklenecek.
// 1. Filtre elemanlarını (checkbox'lar vb.) seç.
// 2. Filtre elemanlarındaki değişiklikleri dinle.
// 3. Seçili filtrelere göre gösterilecek/gizlenecek içerik öğelerini belirle.
// 4. İçerik öğelerinin görünürlüğünü ayarla.

document.addEventListener('DOMContentLoaded', function() {
    const filterCheckboxes = document.querySelectorAll('.filter-checkbox');
    const clearFiltersBtn = document.getElementById('clear-filters-btn');
    let activeFilters = {}; // Aktif filtreleri tutacak nesne

    filterCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            applyFilters();
            updateClearButtonVisibility();
        });
    });

    if (clearFiltersBtn) {
        clearFiltersBtn.addEventListener('click', function() {
            filterCheckboxes.forEach(cb => cb.checked = false);
            applyFilters();
            updateClearButtonVisibility();
        });
    }

    function applyFilters() {
        activeFilters = {};
        filterCheckboxes.forEach(checkbox => {
            if (checkbox.checked) {
                const group = checkbox.dataset.filterGroup;
                const value = checkbox.value;
                if (!activeFilters[group]) {
                    activeFilters[group] = [];
                }
                activeFilters[group].push(value);
            }
        });
        console.log('Aktif Filtreler:', activeFilters);
        // Buraya filtrelemeyi uygulayacak asıl kod gelecek
        // Örnek: Tüm .assessment-card'ları döngüye alıp data-filter-tags ile karşılaştır
        // ve display: none/block ayarla.
         alert("Filtreleme özelliği yakında eklenecek!");
    }

     function updateClearButtonVisibility() {
        if (clearFiltersBtn) {
            const anyChecked = Array.from(filterCheckboxes).some(cb => cb.checked);
            clearFiltersBtn.classList.toggle('d-none', !anyChecked); // Bootstrap class'ı
        }
    }
});