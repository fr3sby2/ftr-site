---
layout: default
title: Hastalıklar ve Durumlar
permalink: /hastaliklar-genel/
body_class: disease-list-page
---

<div class="container mt-4">
  <h1>{{ page.title }}</h1>

  <p class="lead text-center mb-4">
    FTR alanında sık karşılaşılan ve rehabilitasyon gerektiren hastalıklar ve durumlar hakkında bilgiler:
    (Hastalıklara ait görseller eklenmemiştir. Bu yüzden görüntülemede bozukluklar oluşabilir.)
  </p>

  <!-- 🔍 Arama Kutusu -->
  <div class="mb-4">
    <input type="text" id="searchInputDiseases" class="form-control" placeholder="Hastalık arayın...">
  </div>

  <div class="disease-list grid-container mt-4">
    {% assign sorted_diseases = site.diseases | sort: 'title' %}
    {% if sorted_diseases.size > 0 %}
      {% for disease in sorted_diseases %}
        <div class="card disease-card h-100"
             id="disease-{{ disease.title | slugify }}"
             data-disease-tag="{{ disease.disease_tag }}"
             data-title="{{ disease.title | downcase }}"
             data-summary="{{ disease.summary | downcase }}">

          {% if disease.image %}
            <a href="{{ disease.url | relative_url }}">
              <img src="{{ disease.image | relative_url }}" alt="{{ disease.title }}" class="card-img-top">
            </a>
          {% else %}
            <div style="height: 150px; background-color: #eee;" class="card-img-top"></div>
          {% endif %}

          <div class="card-body d-flex flex-column">
            <h3 class="card-title mb-2">
              <a href="{{ disease.url | relative_url }}">{{ disease.title }}</a>
            </h3>
            {% if disease.common_name %}
              <p class="text-muted small mb-2"><em>({{ disease.common_name }})</em></p>
            {% endif %}
            {% if disease.summary %}
              <p class="card-text flex-grow-1">{{ disease.summary | strip_html | truncatewords: 25 }}</p>
            {% else %}
              <p class="card-text flex-grow-1">&nbsp;</p>
            {% endif %}
          </div>
        </div>
      {% endfor %}
    {% else %}
      <div class="alert alert-info">Henüz hastalık bilgisi eklenmemiş.</div>
    {% endif %}
  </div>
</div>

<!-- 🔧 JavaScript: Canlı Arama -->
<script>
  document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("searchInputDiseases");
    const items = document.querySelectorAll(".disease-card");

    input.addEventListener("input", function () {
      const query = input.value.toLowerCase();

      items.forEach((item) => {
        const title = item.getAttribute("data-title");
        const summary = item.getAttribute("data-summary");

        if (title.includes(query) || summary.includes(query)) {
          item.style.display = "block";
        } else {
          item.style.display = "none";
        }
      });
    });
  });
</script>
