// assets/js/filters.js
// console.log("filters.js yüklendi."); // Çalıştığını biliyoruz, kaldırabiliriz

document.addEventListener('DOMContentLoaded', function() {
    const filterCheckboxes = document.querySelectorAll('.filter-checkbox');
    const clearFiltersBtn = document.getElementById('clear-filters-btn');
    const assessmentListContainer = document.querySelector('.assessment-list'); // Kartları içeren ana konteyner
    const noResultsMessage = document.getElementById('no-results-message');
    let assessmentCards = []; // Filtrelenecek kartları burada tutacağız

    // Kart listesi ve mesaj elementi yoksa fonksiyonu sonlandır
    if (!assessmentListContainer || !noResultsMessage) {
        // console.warn("Filtreleme için gerekli HTML elementleri (assessment-list veya no-results-message) bulunamadı.");
        return;
    }

    assessmentCards = Array.from(assessmentListContainer.querySelectorAll('.assessment-card')); // Tüm kartları seç

    // Eğer hiç kart yoksa işlem yapma
    if (assessmentCards.length === 0) {
        // console.log("Filtrelenecek değerlendirme kartı bulunamadı.");
        return;
    }

    let activeFilters = {}; // Aktif filtreleri tutacak nesne: { grupId: [deger1, deger2], ... }

    // Başlangıçta temizle butonunun görünürlüğünü ayarla
    updateClearButtonVisibility();

    // Checkbox değişikliklerini dinle
    filterCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', handleFilterChange);
    });

    // Filtreleri Temizle Butonu
    if (clearFiltersBtn) {
        clearFiltersBtn.addEventListener('click', clearAllFilters);
    }

    // Filtre değişikliğini yöneten fonksiyon
    function handleFilterChange() {
        updateActiveFilters();
        applyFilters();
        updateClearButtonVisibility();
    }

    // Tüm filtreleri temizleyen fonksiyon
    function clearAllFilters() {
        filterCheckboxes.forEach(cb => cb.checked = false);
        handleFilterChange(); // Değişikliği uygula
    }

    // Aktif filtreler nesnesini güncelleyen fonksiyon
    function updateActiveFilters() {
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
         // console.log('Aktif Filtreler:', activeFilters); // Debug
    }

    // Filtreleri kartlara uygulayan fonksiyon
    function applyFilters() {
        let visibleCount = 0;

        assessmentCards.forEach(card => {
            const cardTagsJson = card.dataset.filterTags;
            let cardTags = {};
            // data-filter-tags attribute'u yoksa veya boşsa hata vermemesi için kontrol
            if (!cardTagsJson || cardTagsJson.trim() === '{}' || cardTagsJson.trim() === '') {
                // Etiketi olmayan kartlar nasıl ele alınmalı?
                // Seçenek 1: Her zaman göster (filtre yoksa veya etiketleri yoksa)
                // cardTags = {};
                // Seçenek 2: Filtre uygulandığında gizle (varsayılan davranış aşağıda bunu yapar)
            } else {
                try {
                    cardTags = JSON.parse(cardTagsJson);
                    // JSON içinde null veya undefined değerler varsa temizle (örn. populasyon: null)
                    for (const key in cardTags) {
                        if (cardTags[key] === null || typeof cardTags[key] === 'undefined') {
                            delete cardTags[key];
                        }
                    }
                } catch (e) {
                    console.error('Geçersiz JSON data-filter-tags içinde:', cardTagsJson, card, e);
                    card.style.display = 'none'; // Hatalı kartı gizle
                    return; // Bu kartı atla
                }
            }


            let shouldShow = true; // Gösterilip gösterilmeyeceğini belirleyen bayrak

            // Her bir aktif filtre GRUBU için kontrol
            for (const group in activeFilters) {
                const requiredTagsInGroup = activeFilters[group]; // Seçili filtreler
                const cardTagsInGroup = cardTags[group] || []; // Kartın o gruptaki etiketleri

                // Bu grupta filtre seçiliyse ve kartın o grupta etiketi yoksa VEYA
                // kartın etiketlerinden HİÇBİRİ seçili filtrelerle eşleşmiyorsa GİZLE
                if (requiredTagsInGroup.length > 0) {
                    const matchFound = requiredTagsInGroup.some(reqTag => cardTagsInGroup.includes(reqTag));
                    if (!matchFound) {
                        shouldShow = false;
                        break; // Başka gruplara bakmaya gerek yok
                    }
                }
            }

            // Kartın görünürlüğünü ayarla
            // Not: 'display: grid' veya 'display: flex' gibi durumları
            // ele almak için class ekleyip çıkarmak daha iyi olabilir,
            // ancak şimdilik 'display' stilini kullanıyoruz.
            // Eğer '.grid-container' kullanıyorsanız, gizlemek için 'none',
            // göstermek için '' (boş string) genellikle çalışır.
            card.style.display = shouldShow ? '' : 'none';
            if (shouldShow) {
                visibleCount++;
            }
        });

        // "Sonuç yok" mesajını yönet
        const hasActiveFilters = Object.keys(activeFilters).length > 0;
        noResultsMessage.style.display = (visibleCount === 0 && hasActiveFilters) ? 'block' : 'none';

    } // applyFilters sonu

    // Temizle butonunun görünürlüğünü güncelleyen fonksiyon
    function updateClearButtonVisibility() {
        if (clearFiltersBtn) {
            const anyChecked = Object.keys(activeFilters).length > 0;
            clearFiltersBtn.classList.toggle('d-none', !anyChecked);
        }
    }

}); // DOMContentLoaded sonu