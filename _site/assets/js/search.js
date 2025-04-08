// assets/js/search.js
console.log("search.js yüklendi.");

(function () {
  const searchInput = document.getElementById("search-input");
  const resultsContainer = document.getElementById("search-results-container");
  let lunrIndex, documentsData;
  let isIndexBuilt = false;

  // Türkçe için Lunr ayarları
  const lunrTr = lunr.tr;
  lunr.Pipeline.registerFunction(lunrTr.stemmer, "stemmer-tr");
  lunr.Pipeline.registerFunction(lunrTr.stopWordFilter, "stopWordFilter-tr");

  function displaySearchResults(results) {
    if (!resultsContainer) return;
    resultsContainer.innerHTML = "";

    if (results.length === 0) {
      resultsContainer.innerHTML =
        '<p class="list-group-item">Aramanızla eşleşen sonuç bulunamadı.</p>';
      return;
    }

    const ul = document.createElement("ul");
    ul.classList.add("list-group", "search-results-list");

    results.slice(0, 10).forEach((result) => {
      const doc = documentsData.find((d) => d.id === result.ref);
      if (doc) {
        const li = document.createElement("li");
        li.classList.add("list-group-item", "search-result-item");

        const link = document.createElement("a");
        const baseurl = "{{ site.baseurl }}"; // Jekyll tarafından derlenirken işlenecek
        link.href = baseurl + doc.id;
        link.textContent = doc.title;
        li.appendChild(link);

        if (doc.purpose || doc.summary) {
          const snippet = document.createElement("p");
          snippet.classList.add(
            "search-result-snippet",
            "text-muted",
            "small",
            "mb-0",
            "mt-1"
          );
          snippet.textContent =
            (doc.purpose || doc.summary).substring(0, 120) + "...";
          li.appendChild(snippet);
        }

        ul.appendChild(li);
      }
    });

    resultsContainer.appendChild(ul);
  }

  function buildLunrIndex(data) {
    lunrIndex = lunr(function () {
      this.use(lunrTr);
      this.ref("id");
      this.field("title", { boost: 10 });
      this.field("original_title", { boost: 5 });
      this.field("abbreviation", { boost: 8 });
      this.field("purpose");
      this.field("summary");
      this.field("tags", { boost: 7 });
      this.field("content");

      data.forEach(function (doc) {
        if (doc.id && !doc.id.startsWith("/")) {
          doc.id = "/" + doc.id;
        }
        this.add(doc);
      }, this);
    });
    isIndexBuilt = true;
    console.log("Lunr.js indeksi oluşturuldu.");

    if (searchInput && searchInput.value) {
      performSearch(searchInput.value);
    }
  }

  function performSearch(query) {
    if (!isIndexBuilt || !lunrIndex) {
      console.warn("Arama indeksi henüz hazır değil.");
      if (resultsContainer)
        resultsContainer.innerHTML =
          '<p class="list-group-item">Arama indeksi yükleniyor...</p>';
      return;
    }

    if (!query || query.trim().length < 2) {
      if (resultsContainer) resultsContainer.innerHTML = "";
      return;
    }

    const searchQuery = query
      .trim()
      .toLowerCase()
      .split(/\s+/)
      .map((term) => term + "*")
      .join(" ");

    try {
      const results = lunrIndex.search(searchQuery);
      displaySearchResults(results);
    } catch (e) {
      console.error("Lunr arama hatası:", e);
      if (resultsContainer)
        resultsContainer.innerHTML =
          '<p class="list-group-item">Arama sırasında bir hata oluştu.</p>';
    }
  }

  // --- Başlangıç ---
  const searchDataUrl = "{{ '/search-data.json' | relative_url }}";
  fetch(searchDataUrl)
    .then((response) => {
      if (!response.ok) {
        throw new Error(
          `HTTP error! status: ${response.status} when fetching ${searchDataUrl}`
        );
      }
      return response.json();
    })
    .then((data) => {
      documentsData = data;
      buildLunrIndex(data);
    })
    .catch((error) => {
      console.error("Arama verisi yüklenemedi:", error);
      if (resultsContainer)
        resultsContainer.innerHTML =
          '<p class="list-group-item">Arama verisi yüklenemedi. Lütfen sayfayı yenileyin.</p>';
    });

  if (searchInput) {
    let debounceTimer;
    searchInput.addEventListener("input", function (event) {
      const query = event.target.value;
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        performSearch(query);
      }, 300);
    });
  }

  const searchForm = document.getElementById("site-search-form");
  if (searchForm) {
    searchForm.addEventListener("submit", function (event) {
      event.preventDefault();
      performSearch(searchInput.value);
    });
  }
})();
