---
layout: assessment
title: "Akut Bakım Sonrası Aktivite Ölçümü" # Türkçe'ye çevrilmiş başlık
original_title: "Activity Measure for Post Acute Care"
abbreviation: "AM-PAC"
purpose: "DSÖ'nün ICF modeline dayanarak aktivite sınırlılıklarını değerlendirir. Farklı alanlardaki (örn. Temel Mobilite, Günlük Aktivite, Uygulamalı Biliş) fonksiyonel durumu ölçer."
population: "Çeşitli tanılara sahip akut bakım sonrası hastalar (İnme, Ortopedik durumlar - kalça kırığı vb., TBI, Medikal kompleks hastalar, Kanser, Parkinson, SCI, Artrit)."
scoring: "Hasta veya klinisyen bildirimine dayalıdır. Genellikle Bilgisayarlı Adaptif Test (CAT) veya kısa formlar (Inpatient Short Forms - '6 Clicks', Outpatient Short Forms) kullanılır. Farklı aktivite domainleri (Temel Mobilite, Günlük Aktivite, Uygulamalı Biliş vb.) için ayrı skorlar üretir. Skorlar genellikle ortalaması 50, standart sapması 10 olan T-skorlarına dönüştürülür."

filter_tags:
  alan:
    - gya            # Daily Activity, Personal Care, Instrumental
    - fonksiyonel-mobilite # Basic Mobility, Ambulation, Transfers, WC Skills
    - kognisyon      # Applied Cognitive, New Learning
    - iletisim       # Communication
    - sosyal         # Social
  populasyon:
    - inme
    - ortopedik      # Joint Pain and Fractures
    - artrit
    - kanser
    - parkinson
    - omurilik-yaralanmasi
    - beyin-hasari
    - non-spesifik   # Mixed Populations, Medically Complex
  arac-tipi:
    - anket          # Patient Reported Outcomes (veya Clinician Reported)
    - bilgisayarli-test # Computer Adaptive Test (CAT) version

source_url: "" # Spesifik link yok.
original_reference: "Haley, S. M., Coster, W. J., et al. (2004). \"Activity outcome measurement for postacute care.\" Med Care 42(1 Suppl): I49-61." # Geliştirme makalesi.
---




Akut Bakım Sonrası Aktivite Ölçümü (AM-PAC), hastaların akut bakım sonrası dönemdeki (rehabilitasyon, evde bakım, ayaktan tedavi vb.) fonksiyonel durumunu ve aktivite sınırlılıklarını değerlendirmek için geliştirilmiş bir ölçektir. Dünya Sağlık Örgütü'nün İşlevsellik, Yetiyitimi ve Sağlığın Uluslararası Sınıflandırması (ICF) modelini temel alır.

AM-PAC, hastanın farklı aktivite alanlarındaki (domain) yeteneğini ölçer. En sık kullanılan domainler şunlardır:
*   **Temel Mobilite (Basic Mobility):** Yatak hareketleri, transferler, yürüme gibi temel hareket becerileri.
*   **Günlük Aktivite (Daily Activity):** Kişisel bakım (giyinme, hijyen), enstrümantal aktiviteler (yemek hazırlama, ev işleri).
*   **Uygulamalı Biliş (Applied Cognitive):** Problem çözme, yeni şeyler öğrenme, talimatları takip etme gibi günlük yaşamda bilişsel becerilerin kullanımı.

Değerlendirme, hastanın kendi bildirimine veya klinisyenin gözlemine/değerlendirmesine dayanabilir. AM-PAC'in en önemli özelliği, **Bilgisayarlı Adaptif Test (CAT)** formatında uygulanabilmesidir. CAT formatında, hastanın yanıtlarına göre bilgisayar algoritması bir sonraki soruyu seçer, böylece hastanın yetenek düzeyine en uygun sorular sorularak daha az sayıda soruyla (genellikle 5-8 soru/domain) hassas bir ölçüm yapılır.

Ayrıca, yatan hasta ve ayaktan hasta ortamları için daha kısa, sabit maddeli **Kısa Formlar** (Short Forms) da mevcuttur. Özellikle yatan hasta ortamında kullanılan "6-Clicks" versiyonları (Temel Mobilite ve Günlük Aktivite için 6'şar madde) yaygınlaşmıştır.

Skorlar genellikle Madde Yanıt Teorisi (IRT) kullanılarak hesaplanır ve ortalaması 50, standart sapması 10 olan T-skorlarına dönüştürülür. Yüksek skorlar daha iyi fonksiyonel yeteneği gösterir. AM-PAC skorları, hastanın fonksiyonel durumunu izlemek, tedaviye yanıtı değerlendirmek, taburculuk yerini öngörmek ve bakım düzeyini belirlemek için kullanılır.


*   **CAT versiyonu için:** Bilgisayar ve internet bağlantısı.
*   **Kısa Formlar için:** Basılı form ve kalem/kurşun kalem.


*   **CAT:** Hasta veya klinisyen bilgisayar arayüzü üzerinden soruları yanıtlar. Sistem, yanıtlara göre sonraki soruları seçer ve domain skorunu hesaplar.
*   **Kısa Formlar:** Hasta veya klinisyen formdaki maddeleri yanıtlar. Puanlama kılavuzuna göre ham puanlar hesaplanır ve genellikle T-skorlarına dönüştürülür.


*   Maddeler genellikle "Yapamıyorum" ile "Zorluk Yok" arasında 4 veya 5 puanlık bir Likert skalası kullanır.
*   Ham puanlar, IRT modelleri kullanılarak bir yetenek tahminine (logit skoru) dönüştürülür.
*   Bu logit skorları daha sonra genellikle ortalaması 50, standart sapması 10 olan T-skorlarına çevrilir.
*   Her domain (Temel Mobilite, Günlük Aktivite, Uygulamalı Biliş vb.) için ayrı bir T-skoru elde edilir.
*   Yüksek T-skorları daha iyi fonksiyonel yeteneği gösterir.


AM-PAC skorları, hastanın belirli aktivite domainlerindeki fonksiyonel düzeyini gösterir.
*   **Normatif Veriler:** Farklı hasta gruarı (örn. ortopedik, medikal kompleks, nörolojik) ve bakım ortamları (yatan, ayaktan) için ortalama skorlar raporlanmıştır.
*   **Taburculuk Öngörüsü:** Özellikle yatan hasta "6-Clicks" skorlarının, hastanın eve mi yoksa kuruma mı taburcu olacağını öngörmede kullanılabileceği gösterilmiştir (Jette et al., 2014). Belirli kesme noktaları (örn. Temel Mobilite için 42.9, Günlük Aktivite için 39.4) eve taburculuk olasılığını belirlemede yardımcı olabilir.
*   **Değişim:** Zaman içindeki skor değişiklikleri fonksiyonel iyileşmeyi veya kötüleşmeyi gösterir. MDC değerleri (örn. Temel Mobilite için ~4-8 puan, Günlük Aktivite için ~5-8 puan) klinik olarak anlamlı değişimi yorumlamada kullanılır.

**Dikkat Edilmesi Gerekenler:** CAT versiyonu daha az madde ile daha hassas ölçüm sağlarken, kısa formlar daha pratiktir. Hasta bildirimi ile klinisyen bildirimi arasında farklılıklar olabilir.


AM-PAC (hem CAT hem de kısa formlar), çeşitli akut bakım sonrası popülasyonlarda güçlü psikometrik özellikler göstermiştir.

*   **Güvenilirlik:**
    *   **Test-Tekrar Test:** Postakut bakım hastalarında (çeşitli tanılar) tüm domainler için **Mükemmel** (ICC = 0.91 - 0.97). Nörolojik vakalarda da **Mükemmel** (ICC=0.96-0.97).
    *   **Değerlendiriciler Arası:** Postakut bakım hastalarında Temel Mobilite ve Günlük Aktivite için **Mükemmel** (ICC = 0.86 - 0.90), Uygulamalı Biliş için **Yeterli** (ICC = 0.68). Nörolojik vakalarda da **Mükemmel** (ICC=0.91-0.92). "6-Clicks" formları için de **Mükemmel** interrater güvenilirlik rapor edilmiştir.
*   **İç Tutarlılık:** "6-Clicks" formları ve diğer kısa formlar için **İyi** ile **Mükemmel** arasında (Cronbach's alpha = 0.86 - 0.97).
*   **Geçerlilik:**
    *   **Kriter Geçerliliği (Eş Zamanlı/Öngörücü):**
        *   Kalça kırığı hastalarında SF-36 PF, PFP-10, SPPB, Yürüme Hızı, 6MWT gibi diğer fiziksel fonksiyon ölçümleriyle **Yeterli** ile **Mükemmel** arasında korelasyonlar (r = 0.55 - 0.84).
        *   "6-Clicks" skorlarının akut hastaneden taburculuk yerini (ev vs kurum) öngörmede **iyi** olduğu gösterilmiştir (AUC değerleri ve kesme noktaları belirlenmiştir).
    *   **Yapı Geçerliliği:** Farklı tanı gruarı, cerrahi durum ve bakım ortamları arasında beklenen skor farklılıklarını gösterebilmiştir.
    *   **İçerik Geçerliliği:** ICF aktivite domainine dayalı olarak geliştirilmiş ve uzman görüşleri alınmıştır.
*   **Tavan/Tavan Etkisi:** Rehabilitasyon hastalarında zamanla (özellikle 12 ayda) Kişisel Bakım, Enstrümantal ve Uygulamalı Biliş domainlerinde artan **tavan etkileri** gözlemlenmiştir (%16-44). Temel Mobilite domaininde tavan etkisi düşüktür (<%5). Nörolojik vakalarda da Uygulamalı Biliş'te tavan etkisi (%11-24) diğer domainlerden daha yüksek bulunmuştur.
*   **Yanıt Verebilirlik (Değişime Duyarlılık):** Rehabilitasyon sürecindeki fonksiyonel değişiklikleri saptamada duyarlı olduğu gösterilmiştir. Ortopedik hastalarda (özellikle alt ekstremite) yanıt verebilirliği nörolojik veya medikal kompleks hastalara göre daha yüksek olabilir (ES ve SRM değerleri daha yüksek).


(Metinde listelenen tüm bibliyografya buraya eklenebilir.)
Andres, P. L., Haley, S. M., et al. (2003). "Is patient-reported function reliable for monitoring postacute outcomes?" Am J
... (diğer tüm referanslar) ...
Sandel, M. E., Jette, A. M., Appelman, J., Terdiman, J., TeSelle, M., Delmonico, R. L., ... & Chan, L. (2013). Designing and implementing a system for tracking functional status after stroke: A feasibility study. PM&R, 5(6), 481-490.

---