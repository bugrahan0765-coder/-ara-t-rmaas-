# Proje Hafızası: AI Destekli Gelir Araştırması

Bu repo, kullanıcının agentic AI ile para kazanma araştırmasının kalıcı hafızasıdır. Her oturumda önce bu dosyayı, sonra `arastirma/FIKIR-HAVUZU.md` dosyasını oku.

## Kullanıcı profili
- Türkçe konuşur. İngilizcesi iyi, kod yazabiliyor, zamanı sınırsız, sermaye koyabiliyor.
- Tüm büyük pazaryerlerinde satış yapmış (reseller deneyimi var).
- **B2C istiyor.** B2B satış becerisi istemiyor (toplantı, soğuk arama yok).
- **TikTok'tan büyümek istiyor.** Sınırsız içerik üretebiliyor. Persona hesapları şeffaf marka hesabı olmalı, sahte kullanıcı tanıklığı yok (FTC ve AB kuralları).
- Hedef: Ayda $10k. Gerçekçi beklenti bekliyor. Doymuş işler (YouTube otomasyonu, dropshipping) istemiyor.
- Fikrin para kazandıracağından emin olmak istiyor. Kanıta dayalı ilerle.

## Çalışma kuralları
- Gelir verisi kaynağını her zaman belirt: doğrulanmış (TrustMRR) mı, tahmin mi (Screensdesign/Appllama/Sensor Tower)?
- Bulguları `arastirma/` altına yaz, commit et, `ccr-6aeca7f9-68vg43` branch'ine push et.
- Önceki bir varsayım yanlış çıkarsa açıkça düzelt.

## Kullanılan araştırma yöntemleri (tekrar kullanılabilir)
1. TrustMRR doğrulanmış gelir (kanal ve kategori sayfaları, `/startup/{slug}.md`, `/api/ai/discovery`). Toplu scraping yapma.
2. App Store en çok kazandıranlar RSS: `itunes.apple.com/{ülke}/rss/topgrossingapplications/limit=200/genre={id}/json`. Genç (2025+) uygulamaları filtrele.
3. iTunes Lookup ve Search API: çıkış tarihi, değerlendirme sayısı, rakip arama.
4. Gelir tahmini: `screensdesign.com/apps/{slug}/` (tahmin olduğunu belirt).
5. Coğrafi arbitraj (ABD ↔ DE/GB/FR/TR listeleri).
6. Arama talebi: `suggestqueries.google.com` otomatik tamamlama ("is there an app that…"). Google Trends 429 veriyor.
7. TikTok profil sayıları: `tiktok.com/@handle` HTML içinde followerCount. Hashtag sayfaları çalışmıyor.

## Ek kullanıcı kısıtları (12 Eki 2026)
- Yüzünü göstermeyecek. AI ile UGC tarzı içerik (AI etiketi açık, sahte müşteri tanıklığı yok).
- **Reklam bütçesi yok, sadece organik.** Pazarı veri seçecek, format serbest.

## Birleşik doğrulama hattı (FINAL turunda kullanıldı)
Evren (5 ülke × 22 kategori en çok kazandıranlar) → genç kazananlar → büyüme hızı → site üzerinden TikTok takipçisi → Screensdesign geliri → coğrafi boşluk → otomatik tamamlama talebi → AB rakip araması → vaka ve kanal doğrulaması → veri ve hukuk.

## Mevcut karar (12 Eki 2026, FINAL)
- **Seçilen: Avrupa'nın MenuFit'i** (restoranda hedefe göre ne sipariş edilir, İngiltere öncelikli). Bakınız `arastirma/FINAL-dogrulanmis-fikir.md`.
- Yedek 1: AI Değer Tarayıcı. Yedek 2: Hobi AI koçu.
- Sıradaki adım: 14 günlük yüzsüz içerik testi.
- **Son karar: GO (koşullu).** Kapsam İngiltere restoran + meal deal + GLP-1 modu. Bakınız `arastirma/FINAL-derin-analiz-ve-karar.md`. Kritik açık konular: veritabanı hakkı için avukat görüşü, yüzsüz içerik dönüşümü (test).
