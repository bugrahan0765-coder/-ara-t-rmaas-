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

## Mevcut karar (12 Eki 2026)
- Seçilen: **AI Değer Tarayıcı** (67/80). Yedek: Hobi AI koçu (60/80). Sıradaki adım: 14 günlük içerik testi.
