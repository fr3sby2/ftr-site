---
# _assessments/braden-scale.md

# --- Front Matter Başlangıcı ---
layout: assessment
title: "Braden Skalası (Bası Yarası Riski)" # Türkçe'ye çevrilmiş başlık
original_title: "Braden Scale for Predicting Pressure Sore Risk"
abbreviation: "Braden Skalası"
purpose: "Bası yarası (dekübit ülseri) gelişme olasılığını/riskini değerlendirir."
population: "Bası yarası riski taşıyan tüm hastalar (Yoğun Bakım, Yatan Hasta, Evde Bakım, Uzun Süreli Bakım, Omurilik Yaralanması, İnme, Beyin Hasarı, Yaşlı Yetişkinler)."
scoring: "6 alt ölçek (Duyusal Algı, Nemlilik, Aktivite, Mobilite, Beslenme, Sürtünme/Yırtılma) üzerinden puanlanır. Toplam skor 6 ile 23 arasında değişir. Düşük skorlar daha yüksek bası yarası riskini gösterir."

# Filtreleme için etiketler (_data/filters.yml dosyasındaki 'id' değerleri kullanılacak)
filter_tags:
  alan:
    - risk-degerlendirme # Yeni etiket?
    - deri-butunlugu # Yeni etiket?
    - duyu           # Sensory perception
    - mobilite       # Activity, Mobility
    - beslenme       # Nutrition
  populasyon:
    - yogun-bakim    # Critical Care (Yeni etiket?)
    - yatan-hasta    # Inpatient (Yeni etiket?)
    - evde-bakim     # Home Health (Yeni etiket?)
    - uzun-sureli-bakim # Skilled Nursing Facility (Yeni etiket?)
    - omurilik-yaralanmasi
    - inme
    - beyin-hasari
    - geriatri
    - non-spesifik   # Mixed Populations
  arac-tipi:
    - gozlemsel      # Observer rated risk assessment

source_url: "http://www.bradenscale.com/" # Metindeki link
original_reference: "Bergstrom, N., Braden, B. J., Laguzza, A., & Holman, V. (1987). The Braden Scale for Predicting Pressure Sore Risk. Nursing Research, 36(4), 205–210." # Orijinal makale

# İsteğe Bağlı Ek Alanlar:
# translation_date: {% now 'local: %Y-%m-%d' %}
# translator: <Oluşturan: Yapay Zeka>
# --- Front Matter Sonu ---

# --- Markdown İçerik Başlangıcı ---

## Açıklama

Braden Skalası, bireylerin bası yarası (yatak yarası, dekübit ülseri) geliştirme riskini değerlendirmek için yaygın olarak kullanılan, kanıta dayalı bir risk değerlendirme aracıdır. Altı faktörü göz önünde bulundurarak riski belirler:

1.  **Duyusal Algı:** Hastanın basınçla ilgili rahatsızlığı hissedebilme ve buna yanıt verebilme yeteneği.
2.  **Nemlilik:** Cildin ne ölçüde sürekli neme maruz kaldığı (ter, idrar, dışkı vb.).
3.  **Aktivite:** Hastanın fiziksel aktivite düzeyi (yatağa bağımlı, sandalyeye bağımlı, ara sıra/sık yürüyor).
4.  **Mobilite:** Hastanın vücut pozisyonunu kendi başına değiştirebilme yeteneği.
5.  **Beslenme:** Hastanın genel beslenme alışkanlığı ve durumu.
6.  **Sürtünme ve Yırtılma:** Hastanın hareket ederken cildinin yatak veya sandalye yüzeylerine sürtünme veya bu yüzeylere yapışıp yırtılma potansiyeli.

Her alt ölçek, risk düzeyine göre genellikle 1 (en yüksek risk) ile 3 veya 4 (en düşük risk) arasında puanlanır. Bu altı alt ölçekten alınan puanlar toplanarak 6 ile 23 arasında değişen bir toplam skor elde edilir. Daha düşük toplam skorlar, daha yüksek bası yarası geliştirme riski anlamına gelir.

Braden Skalası, risk altındaki hastaları belirleyerek uygun önleyici müdahalelerin (pozisyon değiştirme, özel yatak kullanımı, cilt bakımı, beslenme desteği vb.) planlanmasına yardımcı olur.

## Gerekli Malzemeler

*   Braden Skalası formu ve puanlama kriterleri.
*   Hastayı gözlemleme ve gerekirse bilgi alma yeteneği.

## Uygulama Talimatları

1.  Hastanın durumu, tıbbi kayıtları ve bakımıyla ilgili bilgiler gözden geçirilir.
2.  Hasta gözlemlenir ve gerekirse hastaya veya bakıcısına sorular sorulur.
3.  Braden Skalası'ndaki 6 alt ölçeğin her biri için hastanın durumuna en uygun tanım seçilir ve karşılık gelen puan (1-4 veya 1-3) verilir.
    *   **Duyusal Algı:** Tamamen sınırlı (1) - Bozukluk yok (4)
    *   **Nemlilik:** Sürekli ıslak (1) - Nadiren ıslak (4)
    *   **Aktivite:** Yatağa bağımlı (1) - Düzenli yürür (4)
    *   **Mobilite:** Tamamen hareketsiz (1) - Sınırlama yok (4)
    *   **Beslenme:** Çok yetersiz (1) - Mükemmel (4)
    *   **Sürtünme ve Yırtılma:** Problem var (1) - Potansiyel problem yok (3)
4.  6 alt ölçek puanı toplanarak toplam Braden skoru elde edilir (6-23 arası).

## Puanlama Detayları

*   Alt Ölçekler: 1 (yüksek risk) - 3 veya 4 (düşük risk) arası puanlanır.
*   Toplam Skor: 6 (çok yüksek risk) - 23 (risk yok) arası.

## Yorumlama

Toplam skora dayalı olarak risk seviyesi belirlenir. Kesme noktaları (cut-off scores) kuruma veya çalışılan popülasyona göre değişebilir, ancak genel olarak kabul gören risk kategorileri şunlardır:

*   **≤ 9:** Çok Yüksek Risk
*   **10-12:** Yüksek Risk
*   **13-14:** Orta Risk
*   **15-18:** Hafif Risk (Bazı kaynaklarda 16 veya 18'e kadar olan skorlar riskli kabul edilir)
*   **19-23:** Risk Yok

Belirlenen risk düzeyine göre önleyici bakım planı oluşturulur. Örneğin, yüksek riskli hastalarda daha sık pozisyon değişimi, basınç azaltıcı yüzeyler ve yoğun cilt bakımı gerekebilir.

Farklı popülasyonlar (yoğun bakım, evde bakım, uzun süreli bakım) ve durumlar için farklı kesme noktalarının daha uygun olabileceği gösterilmiştir. Örneğin, yoğun bakım hastaları için 12-13 gibi daha düşük kesme noktaları önerilebilirken, evde bakım hastaları için 18-19 gibi daha yüksek kesme noktaları kullanılabilir.

**Sınırlılık:** Bazı çalışmalar, deneyimli hemşirelerin klinik yargısının Braden Skalası kadar veya daha iyi risk öngörüsü sağlayabildiğini öne sürmüştür (Salvadalena et al, 1992). Teknolojili eğitimlerin, skalanın güvenilirliğini artırabileceği belirtilmiştir (Magnan et al, 2009).

## Psikometrik Özellikler (Özet)

Braden Skalası, bası yarası riskini değerlendirmede yaygın olarak kullanılan ve genellikle iyi psikometrik özelliklere sahip bir araçtır.

*   **Güvenilirlik:**
    *   **Değerlendiriciler Arası:** Yoğun bakım ve evde bakım ortamlarında yapılan çalışmalarda toplam skor için **Yeterli** ile **İyi** arasında bulunmuştur (ICC = 0.72 - 0.90). Ancak bazı alt ölçeklerde (örn. Aktivite, Nemlilik) güvenilirlik daha düşük olabilir (ICC = 0.08 - 0.81).
    *   **Değerlendirici İçi:** Yatan hastalarda **Mükemmel** (ICC = 0.83).
*   **Geçerlilik:**
    *   **Kriter Geçerliliği (Öngörücü):** Bası yarası gelişimini öngörmedeki doğruluğu (duyarlılık ve özgüllük) kullanılan kesme noktasına ve popülasyona göre değişir. Genel olarak duyarlılık %83-100, özgüllük %64-90 aralıklarında rapor edilmiştir (Bergstrom et al, 1987). Farklı kesme noktaları (örn. 18, 16, 12) farklı duyarlılık/özgüllük dengeleri sunar.
    *   **Yapı Geçerliliği:** Yoğun bakım hastalarında VAS (Görsel Analog Skala) ve Waterlow Skalası gibi diğer risk değerlendirme araçlarıyla **Mükemmel** korelasyon göstermiştir (r = -0.60 ila -0.77, negatif korelasyon beklenir). Omurilik yaralanmalı hastalarda Norton Skalası ile **Yeterli** (r=0.48), Waterlow Skalası ile **Zayıf** (r=-0.06) korelasyon bulunmuştur.
*   **Yanıt Verebilirlik / Duyarlılık & Özgüllük:** Farklı kesme noktaları için duyarlılık ve özgüllük değerleri raporlanmıştır. Genellikle daha düşük kesme noktaları (örn. 10-12) yüksek özgüllük ama düşük duyarlılık sağlarken, daha yüksek kesme noktaları (örn. 18-19) yüksek duyarlılık ama düşük özgüllük sağlar. Kullanım amacına (tarama vs. kesin risk belirleme) göre uygun kesme noktası seçilmelidir.

## Kaynakça

(Metinde listelenen tüm bibliyografya buraya eklenebilir.)
Baldwin, K. M. and Ziegler, S. M. (1998). "Pressure ulcer risk following critical traumatic injury." Adv Wound Care 11(4): 168-173.
... (diğer tüm referanslar) ...
VandenBosch, T.; Montoye, C.; Satwicz, M.; Durkee-Leonard, K.; Boylan-Lewis, B. (1996). "Predictive validity of the Braden Scale and nurse perception in identifying pressure ulcer risk." Applied Nursing Research 9(2): 80-86.

---
# --- Markdown İçerik Sonu ---