---
# _assessments/6-minute-walk-test.md

# --- Front Matter Başlangıcı ---
layout: assessment
title: "6 Dakika Yürüme Testi" # Türkçe'ye çevrilmiş başlık
original_title: "6 Minute Walk Test"
abbreviation: "6MWT"
purpose: "Submaksimal aerobik/fonksiyonel yürüme kapasitesini, toplum içinde yürüme potansiyelini değerlendirir ve kardiyak hastalarda morbidite/mortalite için bir öngörücü olarak hizmet eder."
population: "Geniş bir popülasyon: İnme, Omurilik Yaralanması, Pulmoner Hastalıklar (KOAH vb.), Parkinson Hastalığı, Osteoartrit, Yaşlı Yetişkinler, Multiple Sclerosis (MS), Alzheimer Hastalığı, Beyin Hasarı (TBI), Artrit, Kronik Kalp Yetmezliği, Alt Ekstremite Amputasyonu, Çocuklar (modifiye)."
scoring: "Tek bir skor: 6 dakika içinde yürünen toplam mesafe (genellikle metre cinsinden)."

# Filtreleme için etiketler (_data/filters.yml dosyasındaki 'id' değerleri kullanılacak)
filter_tags:
  alan:
    - yurume         # Gait
    - endurans       # Aerobic Capacity
    - fonksiyonel-mobilite # Functional Mobility
    - yasam-katilimi # Life Participation (Community walking prediction)
  populasyon:
    - inme
    - omurilik-yaralanmasi
    - pulmoner
    - parkinson
    - osteoartrit    # Yeni etiket?
    - geriatri
    - ms
    - alzheimer
    - non-spesifik   # Mixed Populations
    - beyin-hasari
    - artrit
    - kardiyak       # Yeni etiket?
    - amputasyon
    - pediatri
  arac-tipi:
    - performans     # Observer rated performance

source_url: "" # Spesifik link yok, ATS kılavuzuna atıf var.
original_reference: "ATS Committee on Proficiency Standards for Clinical Pulmonary Function Laboratories. (2002). ATS statement: guidelines for the six-minute walk test. Am J Respir Crit Care Med, 166(1), 111-117." # Ana kılavuz.

# İsteğe Bağlı Ek Alanlar:
# translation_date: {% now 'local: %Y-%m-%d' %}
# translator: <Oluşturan: Yapay Zeka>
# --- Front Matter Sonu ---

# --- Markdown İçerik Başlangıcı ---

## Açıklama

6 Dakika Yürüme Testi (6MWT), bireyin kendi belirlediği hızda 6 dakika boyunca düz bir zeminde kat edebildiği maksimum mesafeyi ölçen, yaygın olarak kullanılan submaksimal bir egzersiz tolerans testidir. Fonksiyonel egzersiz kapasitesini, yürüme enduransını ve genel fiziksel fonksiyonu değerlendirmek amacıyla kullanılır.

Test, çeşitli kardiyopulmoner, nörolojik ve kas-iskelet sistemi rahatsızlıklarında hastanın durumunu değerlendirmek, tedaviye yanıtını izlemek ve prognozu tahmin etmek için kullanılır. Örneğin, kalp yetmezliği, KOAH, pulmoner hipertansiyon gibi durumlarda morbidite ve mortalite ile ilişkisi gösterilmiştir. Aynı zamanda inme, MS, Parkinson, SCI gibi nörolojik durumlarda yürüme kapasitesini ve toplum içinde yürüme potansiyelini değerlendirmede de değerli bir araçtır.

Test sırasında hastanın kendi hızını ayarlamasına izin verilir ve ihtiyaç duyduğunda durup dinlenebilir (ancak süre işlemeye devam eder). Yardımcı cihaz kullanımına izin verilir ancak kaydedilmelidir.

## Gerekli Malzemeler

*   Kronometre
*   Standart bir sandalye (başlangıç/bitiş ve dinlenme için)
*   İşaretlenmiş, düz, sert yüzeyli bir yürüme parkuru (ATS kılavuzu 30 metre/100 feet önerir, ancak 12-34 metre arası parkurlar da kullanılır). Parkur üzerinde her 3 metrede bir işaret olması önerilir.
*   Dönüş noktalarını işaretlemek için 2 adet koni.
*   Mesafe ölçüm aracı (ölçüm tekerleği veya işaretli parkur).
*   Kayıt formu ve kalem/kurşun kalem.
*   (Önerilen) Borg RPE (Algılanan Zorluk Düzeyi) skalası.
*   (Önerilen) Tansiyon aleti (sfigmomanometre) ve stetoskop (test öncesi/sonrası ölçüm için).
*   (Önerilen) Pulse oksimetre (test öncesi/sonrası veya sırasında ölçüm için).
*   Acil durum ekipmanı (oksijen, telefon vb.).

## Uygulama Talimatları

Amerikan Toraks Derneği (ATS) kılavuzları gibi standart protokoller takip edilmelidir:

1.  Test öncesi hastanın dinlenmesi sağlanır (gerekirse 10 dk). Kontraendikasyonlar (örn. son 1 ayda stabil olmayan anjina veya MI) kontrol edilir.
2.  Başlangıç vital bulguları (Nabız, KB, SpO2) ve Borg skalası skorları alınır.
3.  Hastaya test açıklanır: "Bu testte amacımız 6 dakika içinde ne kadar uzağa yürüyebileceğinizi ölçmektir. Hızlı yürümeniz önemlidir, ancak koşmayın. Yorulursanız yavaşlayabilir veya durup dinlenebilirsiniz. Dinlenmeniz gerekirse sürenin devam edeceğini unutmayın."
4.  Hasta başlangıç çizgisine getirilir. "Başla" komutuyla kronometre başlatılır.
5.  Değerlendirici hastanın yanında veya biraz gerisinde yürür, hastayı hızlandırmaz.
6.  Standart teşvik cümleleri belirli aralıklarla söylenir (örn. "İyi gidiyorsunuz", "Zamanın yarısı bitti", "Hızınızı koruyun"). Başka konuşma yapılmaz.
7.  Hasta durursa dinlenmeye teşvik edilir ve hazır olduğunda devam etmesi söylenir. Durma sayısı ve süresi kaydedilir.
8.  6 dakika sonunda "Dur" komutu verilir. Hasta durduğu yer işaretlenir ve yürünen toplam mesafe ölçülür.
9.  Test sonrası vital bulgular ve Borg skorları tekrar alınır.

## Puanlama Detayları

*   Ana skor: 6 dakika içinde yürünen **toplam mesafe** (metre cinsinden).
*   Ek olarak kaydedilebilecekler: Durma sayısı, toplam dinlenme süresi, test sırasındaki en düşük oksijen satürasyonu, test sonu Borg skorları.

## Yorumlama

Yürünen mesafe, hastanın fonksiyonel kapasitesi hakkında bilgi verir. Sonuçlar, beklenen normal değerlerle (yaş, cinsiyet, boy, kiloya göre hesaplanan referans denklemleri ile) veya hastanın önceki test sonuçlarıyla karşılaştırılır.
*   **Normatif Değerler:** Sağlıklı yetişkinler için referans denklemleri mevcuttur (Enright et al., 1998). Çocuklar ve farklı hasta gruarı için de normatif veriler bulunmaktadır.
*   **Prognoz:** Özellikle KOAH ve kalp yetmezliği gibi durumlarda düşük 6MWT mesafeleri (<200-300 m) artmış mortalite ve morbidite riski ile ilişkilidir.
*   **Toplum Ambulasyonu:** İnme sonrası toplum içinde yürüyebilme düzeyi ile 6MWT mesafesi arasında ilişki kurulmuştur (Fulk et al., 2017). Örneğin, sınırsız toplum ambulatörü olmak için genellikle 300 metrenin üzerinde bir mesafe gerekebilir.
*   **Klinik Anlamlı Fark:** Farklı popülasyonlar için Minimal Klinik Olarak Anlamlı Fark (MCID) değerleri belirlenmiştir. Örneğin, KOAH için 54m, geriatri/inme için 50m, MS için ~20m iyileşme/ ~7m kötüleşme gibi değerler önerilmiştir. Minimal Saptanabilir Değişim (MDC) değerleri de raporlanmıştır (örn. OA için 61m, Parkinsonizm için 82m, inme için 34-61m).

**Dikkat Edilmesi Gerekenler:**
*   Parkur uzunluğu test sonuçlarını etkileyebilir; daha kısa parkurlarda (daha fazla dönüş gerektiren) daha kısa mesafeler yürünebilir. Standardizasyon önemlidir.
*   Öğrenme etkisi olabilir; bazı protokoller ilk testin atılmasını veya pratik testi yapılmasını önerir.
*   Test performansı motivasyon, anksiyete ve günün saatinden etkilenebilir.

## Psikometrik Özellikler (Özet)

6MWT, birçok farklı popülasyonda yaygın olarak kullanılan ve genellikle iyi psikometrik özelliklere sahip bir testtir.

*   **Güvenilirlik:**
    *   **Test-Tekrar Test:** Çoğu popülasyonda (Yaşlılar, OA, Parkinsonizm, TBI, İnme, Alzheimer) **Mükemmel** bulunmuştur (ICC veya r = 0.86 - 0.99).
    *   **Değerlendiriciler Arası:** İnme ve Alzheimer hastalarında **İyi** ile **Mükemmel** arasında bulunmuştur (ICC = 0.78 - 0.99).
    *   **Değerlendirici İçi:** İnme ve Alzheimer hastalarında **Yeterli** ile **Mükemmel** arasında bulunmuştur (ICC = 0.74 - 0.96).
*   **Geçerlilik:**
    *   **Kriter Geçerliliği (Eş Zamanlı/Öngörücü):**
        *   VO2 max (maksimal oksijen tüketimi) ile çeşitli popülasyonlarda **Yeterli** ile **Mükemmel** arasında korelasyon gösterir (r = 0.41 - 0.82), bu da aerobik kapasiteyi yansıttığını gösterir.
        *   2 Dakika Yürüme Testi (2MWT) ile **Mükemmel** korelasyon (r > 0.93).
        *   10 Metre Yürüme Testi (10MWT) ve Zamanlı Kalk Yürü Testi (TUG) gibi diğer yürüme ve mobilite testleri ile **Mükemmel** korelasyon (r veya rho = 0.80 - 0.95 veya -0.80 - -0.89).
        *   Berg Denge Skalası (BBS) gibi denge ölçümleri ile **Yeterli** ile **Mükemmel** arasında korelasyon.
        *   SF-36 Fiziksel Fonksiyon alt ölçeği gibi yaşam kalitesi ölçümleriyle **Yeterli** korelasyon.
        *   Kardiyopulmoner hastalıklarda ve bazı nörolojik durumlarda mortalite, morbidite ve fonksiyonel sonucu öngörmede kullanılır.
    *   **Yapı Geçerliliği:** Yaş, cinsiyet, boy, kilo gibi faktörlerle ilişkisi gösterilmiştir. Hastalık şiddeti (örn. NYHA sınıfı, EDSS skoru) ile ters korelasyon gösterir.
*   **Yanıt Verebilirlik (Değişime Duyarlılık):** Çeşitli müdahaleler (örn. pulmoner rehabilitasyon, egzersiz programları) sonrası değişimi saptamada duyarlı olduğu gösterilmiştir. Farklı popülasyonlar için MCID ve MDC değerleri belirlenmiştir.

## Kaynakça

(Metinde listelenen tüm bibliyografya buraya eklenebilir.)
ATS Committee on Proficiency Standards for Clinical Pulmonary Function Laboratories. (2002). ATS statement: guidelines for the six-minute walk test. Am J Respir Crit Care Med, 166(1), 111-117.
... (diğer tüm referanslar) ...
Woodward JL, Connolly M, Hennessy PW, Holleran CL, Mahtani GB, Brazg G, Fahey M, Maganti K, Hornby TG. (2019, Jan 1). Cardiopulmonary Responses During Clinical and Laboratory Gait Assessments in People With Chronic Stroke. Phys Ther., 99(1):86-97.

---
# --- Markdown İçerik Sonu ---