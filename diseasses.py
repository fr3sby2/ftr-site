import google.generativeai as genai
import os
import re
import time
import unicodedata

# --- Ayarlar ---
# --- API Anahtarınızı Buraya Yapıştırın ---
API_KEY = "AIzaSyCYWRcRiTRE5T91I7Kyo25TLt0GenrcZuw" # <--- KENDİ GEMINI API ANAHTARINIZI BURAYA YAPIŞTIRIN
# -----------------------------------------

if API_KEY == "YOUR_API_KEY_HERE" or not API_KEY:
     raise ValueError("Lütfen betik içerisindeki API_KEY değişkenine geçerli Gemini API anahtarınızı girin.")

MODEL_NAME = "gemini-2.0-flash"
OUTPUT_DIR = "_diseases"  # Hastalık dosyalarının kaydedileceği klasör adı
# --- Ayarlar Sonu ---

# --- Hastalık Listesi (Genişletilmiş FTR Odaklı) ---
DISEASE_LIST = [
    # Nörolojik Durumlar
    "Stroke", # İnme (Genel)
    "Ischemic Stroke", # İskemik İnme
    "Hemorrhagic Stroke", # Hemorajik İnme
    "Transient Ischemic Attack", # Geçici İskemik Atak (TIA)
    "Parkinson's Disease", # Parkinson Hastalığı
    "Multiple Sclerosis", # Multiple Skleroz (MS)
    "Spinal Cord Injury", # Omurilik Yaralanması (Genel)
    "Traumatic Spinal Cord Injury", # Travmatik Omurilik Yaralanması
    "Non-Traumatic Spinal Cord Injury", # Travmatik Olmayan Omurilik Yaralanması
    "Traumatic Brain Injury", # Travmatik Beyin Yaralanması (TBI)
    "Acquired Brain Injury", # Edinilmiş Beyin Yaralanması (Genel)
    "Cerebral Palsy", # Serebral Palsi (SP)
    "Amyotrophic Lateral Sclerosis", # Amyotrofik Lateral Skleroz (ALS)
    "Guillain-Barre Syndrome", # Guillain-Barre Sendromu
    "Myasthenia Gravis", # Myastenia Gravis
    "Peripheral Neuropathy", # Periferik Nöropati (Genel)
    "Diabetic Neuropathy", # Diyabetik Nöropati
    "Charcot-Marie-Tooth Disease", # Charcot-Marie-Tooth Hastalığı
    "Vestibular Disorders", # Vestibüler Bozukluklar (Genel)
    "Benign Paroxysmal Positional Vertigo", # Benign Paroksismal Pozisyonel Vertigo (BPPV)
    "Meniere's Disease", # Meniere Hastalığı
    "Vestibular Neuritis", # Vestibüler Nörit
    "Labyrinthitis", # Labirentit
    "Alzheimer's Disease", # Alzheimer Hastalığı
    "Dementia", # Demans (Genel)
    "Vascular Dementia", # Vasküler Demans
    "Lewy Body Dementia", # Lewy Cisimcikli Demans
    "Huntington's Disease", # Huntington Hastalığı
    "Ataxia", # Ataksi (Genel)
    "Friedreich's Ataxia", # Friedreich Ataksisi
    "Spinocerebellar Ataxia", # Spinoserebellar Ataksi
    "Dystonia", # Distoni
    "Essential Tremor", # Esansiyel Tremor
    "Transverse Myelitis", # Transvers Miyelit
    "Epilepsy", # Epilepsi (Fiziksel etkileri olan durumlar)
    "Normal Pressure Hydrocephalus", # Normal Basınçlı Hidrosefali
    "Post-Polio Syndrome", # Post-Polio Sendromu
    "Bell's Palsy", # Bell Paralizisi (Yüz Felci)
    "Trigeminal Neuralgia", # Trigeminal Nevralji
    "Complex Regional Pain Syndrome", # Kompleks Bölgesel Ağrı Sendromu (CRPS)
    "Hydrocephalus", # Hidrosefali

    # Kas-İskelet Sistemi Durumları
    "Osteoarthritis", # Osteoartrit (Genel)
    "Knee Osteoarthritis", # Diz Osteoartriti
    "Hip Osteoarthritis", # Kalça Osteoartriti
    "Hand Osteoarthritis", # El Osteoartriti
    "Rheumatoid Arthritis", # Romatoid Artrit
    "Ankylosing Spondylitis", # Ankilozan Spondilit
    "Low Back Pain", # Bel Ağrısı (Genel)
    "Chronic Low Back Pain", # Kronik Bel Ağrısı
    "Lumbar Disc Herniation", # Lomber Disk Hernisi
    "Lumbar Spinal Stenosis", # Lomber Spinal Stenoz
    "Spondylolisthesis", # Spondilolistezis
    "Neck Pain", # Boyun Ağrısı (Genel)
    "Cervical Disc Herniation", # Servikal Disk Hernisi
    "Cervical Spondylosis", # Servikal Spondiloz
    "Whiplash Associated Disorders", # Whiplash İlişkili Bozukluklar
    "Shoulder Impingement Syndrome", # Omuz Sıkışma Sendromu
    "Rotator Cuff Tear", # Rotator Manşet Yırtığı
    "Adhesive Capsulitis", # Adeziv Kapsülit (Donuk Omuz)
    "Shoulder Instability", # Omuz İnstabilitesi
    "Tennis Elbow", # Tenisçi Dirseği (Lateral Epikondilit)
    "Golfer's Elbow", # Golfçü Dirseği (Medial Epikondilit)
    "Carpal Tunnel Syndrome", # Karpal Tünel Sendromu
    "Hip Fracture", # Kalça Kırığı
    "Femur Fracture", # Femur Kırığı
    "Tibial Fracture", # Tibia Kırığı
    "Ankle Fracture", # Ayak Bileği Kırığı
    "Wrist Fracture", # El Bileği Kırığı (örn. Colles)
    "Vertebral Compression Fracture", # Vertebra Kompresyon Kırığı
    "Total Hip Arthroplasty", # Total Kalça Artroplastisi (Rehabilitasyon)
    "Total Knee Arthroplasty", # Total Diz Artroplastisi (Rehabilitasyon)
    "Shoulder Arthroplasty", # Omuz Artroplastisi (Rehabilitasyon)
    "Achilles Tendinopathy", # Aşil Tendinopatisi
    "Patellar Tendinopathy", # Patellar Tendinopati
    "Plantar Fasciitis", # Plantar Fasiit
    "Fibromyalgia", # Fibromiyalji
    "Osteoporosis", # Osteoporoz
    "Scoliosis", # Skolyoz
    "Patellofemoral Pain Syndrome", # Patellofemoral Ağrı Sendromu
    "Meniscus Tear", # Menisküs Yırtığı
    "ACL Reconstruction", # Ön Çapraz Bağ (ACL) Rekonstrüksiyonu (Rehabilitasyon)
    "Temporomandibular Joint Dysfunction", # Temporomandibular Eklem Disfonksiyonu (TME)

    # Kardiyopulmoner Durumlar
    "Heart Failure", # Kalp Yetmezliği
    "Chronic Obstructive Pulmonary Disease", # Kronik Obstrüktif Akciğer Hastalığı (KOAH)
    "Myocardial Infarction", # Miyokard Enfarktüsü (Kalp Krizi sonrası rehabilitasyon)
    "Coronary Artery Bypass Graft Surgery", # Koroner Arter Bypass Greft Cerrahisi (CABG sonrası rehabilitasyon)
    "Asthma", # Astım
    "Cystic Fibrosis", # Kistik Fibroz
    "Pulmonary Fibrosis", # Pulmoner Fibroz
    "Pulmonary Hypertension", # Pulmoner Hipertansiyon

    # Pediatrik Durumlar
    # "Cerebral Palsy", # Yukarıda nörolojik altında da var
    "Spina Bifida", # Spina Bifida
    "Muscular Dystrophy", # Müsküler Distrofi (örn. Duchenne, Becker)
    "Developmental Coordination Disorder", # Gelişimsel Koordinasyon Bozukluğu
    "Developmental Delay", # Gelişimsel Gecikme
    "Torticollis", # Tortikolis
    "Juvenile Idiopathic Arthritis", # Juvenil İdiyopatik Artrit
    "Autism Spectrum Disorder", # Otizm Spektrum Bozukluğu (Motor ve duyusal yönleri)
    "Down Syndrome", # Down Sendromu

    # Geriatrik Durumlar
    "Falls in Older Adults", # Yaşlılarda Düşmeler
    "Frailty", # Kırılganlık
    "Sarcopenia", # Sarkopeni
    "General Deconditioning", # Genel Kondisyon Kaybı

    # Diğer Durumlar
    "Lower Limb Amputation", # Alt Ekstremite Amputasyonu (Genel)
    "Transfemoral Amputation", # Transfemoral Amputasyon
    "Transtibial Amputation", # Transtibial Amputasyon
    "Upper Limb Amputation", # Üst Ekstremite Amputasyonu
    "Burns", # Yanıklar (Rehabilitasyon)
    "Cancer Rehabilitation", # Kanser Rehabilitasyonu (Genel)
    "Breast Cancer Rehabilitation", # Meme Kanseri Rehabilitasyonu
    "Head and Neck Cancer Rehabilitation", # Baş Boyun Kanseri Rehabilitasyonu
    "Lymphedema", # Lenfödem
    "Chronic Pain", # Kronik Ağrı (Genel)
    "Obesity", # Obezite (FTR ile ilişkili)
    "HIV/AIDS", # HIV/AIDS (Fonksiyonel kısıtlılıklarla ilişkili)
    "Organ Transplantation", # Organ Transplantasyonu (Rehabilitasyon)
    "Critical Illness Myopathy and Neuropathy", # Kritik Hastalık Miyopatisi ve Nöropatisi
    "Post Intensive Care Syndrome" # Yoğun Bakım Sonrası Sendromu (PICS)

]
# --- Hastalık Listesi Sonu ---


# Gemini İstemcisini Yapılandır
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL_NAME)

# --- Yardımcı Fonksiyon: Slugify ---
def slugify(value):
    turkish_map = {ord('ı'): 'i', ord('İ'): 'i', ord('ğ'): 'g', ord('Ğ'): 'g',
                   ord('ü'): 'u', ord('Ü'): 'u', ord('ş'): 's', ord('Ş'): 's',
                   ord('ö'): 'o', ord('Ö'): 'o', ord('ç'): 'c', ord('Ç'): 'c',
                   ord(' '): '-', ord('/'): '-', ord('\\'): '-'}
    value = unicodedata.normalize('NFKD', value.lower().translate(turkish_map))
    value = re.sub(r'[^\w\s-]', '', value).strip()
    value = re.sub(r'[-\s]+', '-', value)
    return value

# --- Hastalık Prompt Şablonu ---
DISEASE_PROMPT_TEMPLATE = """
Sen, fizik tedavi ve rehabilitasyon (FTR) alanında uzmanlaşmış, güvenilir ve güncel bilgilere sahip bir içerik üreticisisin. Görevin, "{disease_name}" hastalığı hakkında, aşağıda belirtilen yapıya **tam olarak uyan** bir Türkçe `.md` dosyası içeriği oluşturmak.

Çıktın **SADECE** `.md` formatında olmalı. Başka hiçbir açıklama, giriş veya sonuç cümlesi eklememelisin. Çıktı birebir kopyalanıp bir .md dosyasına kaydedilebilecek şekilde olmalıdır.

Çıktının yapısı şu şekilde olmalıdır (Parantez içindeki açıklamalar sadece bilgilendirme amaçlıdır, çıktıya dahil edilmemelidir):

---
# _diseases/[dosya-adı].md (Bu satırı çıktıya EKLEME)

# --- Front Matter Başlangıcı ---
layout: disease
title: "[Hastalığın Türkçe Adı - '{disease_name}' adını Türkçe'ye çevir]"
english_title: "{disease_name}" # İngilizce adı aynen yaz
common_name: "[Hastalığın yaygın adı veya kısaltması (varsa, AI tahmin etsin, yoksa boş bırak)]"
summary: "[Hastalığın 1-2 cümlelik kısa, öz ve anlaşılır Türkçe özeti]"
image: "/assets/images/diseases/{disease_tag_placeholder}.jpg" # Bu satırı aynen ekle, sadece disease_tag_placeholder kısmını aşağıda belirtilen etiketle değiştir
disease_tag: "{disease_tag_placeholder}" # Bu satırı aynen ekle, aşağıda belirtilen etiketi kullan

# İsteğe Bağlı Ek Alanlar:
# related_assessments_info: "[Hastalıkla ilgili sık kullanılan değerlendirme türleri hakkında kısa not (örn: 'Genellikle denge, yürüme ve GYA değerlendirmeleri yapılır.')]" # AI uygun görürse eklesin
# --- Front Matter Sonu ---

# --- Markdown İçerik Başlangıcı ---

## Tanım / Genel Bakış

[{disease_name} hastalığının ne olduğu, temel özellikleri hakkında genel, güvenilir ve anlaşılır Türkçe bilgi. Bu bilgiyi kendi bilgi tabanından veya güvenilir kaynaklardan derle.]

## Nedenleri ve Risk Faktörleri

[{disease_name} hastalığının bilinen nedenleri, etiyolojisi ve risk faktörleri hakkında Türkçe bilgi. Bilgi mevcut ve güvenilirse ekle, yoksa bu bölümü başlığıyla birlikte ÇIKTIYA EKLEME.]

## Belirtiler ve Bulgular

[{disease_name} hastalığının yaygın klinik belirti ve bulguları hakkında Türkçe bilgi. Bilgi mevcut ve güvenilirse ekle.]

## Fizik Tedavi ve Rehabilitasyon (FTR) Yaklaşımları

[FTR profesyonelleri için önemli olacak şekilde, {disease_name} hastalığına sahip bireyler için tipik FTR hedefleri, sık kullanılan müdahaleler ve genel rehabilitasyon yaklaşımları hakkında Türkçe bilgi. Bu bölüm FTR odağında olmalı.]

## Prognoz

[{disease_name} hastalığının genel seyri ve prognozu hakkında kısa Türkçe bilgi. Bilgi mevcut ve güvenilirse ekle, yoksa bu bölümü başlığıyla birlikte ÇIKTIYA EKLEME.]

## Kaynakça / Daha Fazla Bilgi

[Okuyucuların daha fazla bilgi edinebileceği 1-2 adet güvenilir Türkçe veya İngilizce kaynak (örn. sağlık bakanlığı, hasta dernekleri, Mayo Clinic, WHO gibi tanınmış kuruluşlar) web sitesi linki veya temel bir derleme makale referansı. Link formatında ver (örn: '[Kaynak Adı](URL)'). Eğer güvenilir ve uygun kaynak bulamazsan bu bölümü başlığıyla birlikte ÇIKTIYA EKLEME.]

# --- Markdown İçerik Sonu --- (Bu satırı çıktıya EKLEME)

---

Tüm çıktı **Türkçe** olmalıdır. Bilgilerin **doğru, güncel ve güvenilir** olmasına özen göster. Tıbbi tavsiye niteliğinde olmayan, genel bilgilendirme amaçlı bir dil kullan. Eğer belirli bir bölüm (Nedenler, Prognoz, Kaynakça) için yeterli ve güvenilir bilgi bulamazsan, o bölümü başlığıyla birlikte çıktıya **ekleme**. YAML Front Matter'daki `title` alanını mutlaka Türkçe olarak doldur. `disease_tag` ve `image` alanlarındaki yer tutucuları `{disease_tag_placeholder}` ile değiştirilmesi gerektiğini unutma (bu, Python betiği tarafından yapılacak).
"""

# --- Ana İşlem ---
def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        print(f"Klasör oluşturuldu: {OUTPUT_DIR}")

    for disease_name in DISEASE_LIST:
        print(f"\nİşleniyor: {disease_name}")

        # Dosya adını ve disease_tag'ı oluştur
        disease_slug = slugify(disease_name)
        filename = disease_slug + ".md"
        output_filepath = os.path.join(OUTPUT_DIR, filename)

        # Gemini'ye gönderilecek prompt'u oluştur
        # Yer tutucuları Python tarafında dolduruyoruz
        try:
            prompt = DISEASE_PROMPT_TEMPLATE.format(
                disease_name=disease_name,
                disease_tag_placeholder=disease_slug # Python'da oluşturulan slug'ı prompt'a ekliyoruz
            )
        except Exception as e:
            print(f"Hata: Prompt formatlanırken hata - {e}")
            continue # Bu hastalığı atla

        # Gemini API'yi çağır
        try:
            print("Gemini API çağrılıyor...")
            safety_settings = [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
            ]
            response = model.generate_content(prompt, safety_settings=safety_settings)

            if response.parts:
                 md_content = response.text
                 # Küçük bir temizlik: Bazı modeller başta/sonda ```md ... ``` ekleyebilir.
                 md_content = re.sub(r"^```markdown\s*", "", md_content, flags=re.IGNORECASE)
                 md_content = re.sub(r"\s*```$", "", md_content)
            elif response.prompt_feedback and response.prompt_feedback.block_reason:
                 print(f"Hata: İçerik engellendi. Sebep: {response.prompt_feedback.block_reason}")
                 md_content = f"# {disease_name}\n\nİÇERİK ÜRETİLEMEDİ - ENGELLEME SEBEBİ: {response.prompt_feedback.block_reason}"
            else:
                 try:
                    md_content = "".join(part.text for part in response.parts)
                    if not md_content:
                       print("Uyarı: Gemini API'den boş metin yanıtı alındı.")
                       md_content = f"# {disease_name}\n\nİÇERİK ÜRETİLEMEDİ - BOŞ YANIT"
                 except Exception as ex:
                    print(f"Hata: Yanıt içeriği alınamadı veya işlenemedi - {ex}")
                    print(f"Alınan yanıt: {response}")
                    md_content = f"# {disease_name}\n\nİÇERİK ÜRETİLEMEDİ - YANIT İŞLEME HATASI"

            print("Yanıt alındı (veya hata oluştu).")

            # Gelen içeriği dosyaya yaz (UTF-8 olarak)
            try:
                with open(output_filepath, 'w', encoding='utf-8') as md_file:
                    md_file.write(md_content.strip()) # Başta/sonda olası boşlukları temizle
                print(f"Başarılı: '{output_filepath}' dosyası oluşturuldu.")
            except IOError as e:
                print(f"Hata: '{output_filepath}' dosyası yazılamadı - {e}")
            except Exception as e:
                 print(f"Dosya yazma sırasında beklenmedik hata ({output_filepath}): {e}")

        except Exception as e:
            print(f"Hata: '{disease_name}' için Gemini API çağrısı başarısız oldu - {e}")

        # API hız limitlerine takılmamak için bekleme
        time.sleep(1) # 1 saniye bekle

    print(f"\nİşlem tamamlandı. Toplam {len(DISEASE_LIST)} hastalık için .md dosyası oluşturma denendi.")

if __name__ == "__main__":
    main()