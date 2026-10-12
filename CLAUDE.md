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
7. TikTok profil sayıları: `tiktok.com/@handle` HTML içinde followerCount, heartCount, videoCount. Hashtag ve discover sayfaları çalışmıyor.
8. **TikTok organik radar** (`araclar/tiktok-radar-*.py`): Kategori top free listeleri (ABD, GB) → genç uygulamalar → TikTok hesabı → kalp/video oranı. Oran 5k'dan büyükse organik trend adayıdır. Listede üst sırada olup TikTok'ta boş olan uygulamalar ücretli edinimle büyüyordur. App Store yorumlarında 'tiktok' aramak işe yaramıyor. Creative Center ve Ad Library sadece tarayıcıda, elle kullanılabiliyor. Detay: `arastirma/tiktok-trend-uygulama-bulma-yontemleri.md`
9. **İzlenme satış demek değil.** Dönüşüm kontrolü: top grossing sırasını top free sırasıyla karşılaştır, kalp/değerlendirme oranına bak, yorumlarda niyet oranını ölç. Kazanan = kalp/video > 5k **ve** grossing sırası free sırasından en fazla 10 basamak kötü. Karşı örnek: WayShot (çok viral, zayıf gelir).
10. **Apify** (kullanıcının sorduğu anahtar buydu): clockworks/tiktok-scraper ve profile/comments scraper'ları. Video başına ~$0,0037. Ücretsiz plan ayda $5 kredi veriyor. Token, ortam ayarlarına `APIFY_TOKEN` olarak eklenir. Anahtar kelime araması, video izlenmesi ve yorumlar için gerekir.
11. Anthropic API anahtarı: Araştırma için gerekmez. Otomatik radar için Claude Code rutini yeterli. Kendi sunucunda LLM kullanacaksan `ANTHROPIC_API_KEY` gerekir.

## Ek kullanıcı kısıtları (12 Eki 2026)
- Yüzünü göstermeyecek. AI ile UGC tarzı içerik (AI etiketi açık, sahte müşteri tanıklığı yok).
- **Pazarlama kanalı: TikTok + Instagram organik** (12 Eki 2026'da teyit edildi). AI içerik ve karusel/slayt gösterisi serbest.
- **Reklam bütçesi yok, sadece organik.** Pazarı veri seçecek, format serbest.
- **Creator ve influencer ile ÇALIŞMAYACAK** (gelir paylaşımlı dahil). Tüm içeriği kendisi üretecek. Bunu bir daha önerme.

## Birleşik doğrulama hattı (FINAL turunda kullanıldı)
Evren (5 ülke × 22 kategori en çok kazandıranlar) → genç kazananlar → büyüme hızı → site üzerinden TikTok takipçisi → Screensdesign geliri → coğrafi boşluk → otomatik tamamlama talebi → AB rakip araması → vaka ve kanal doğrulaması → veri ve hukuk.

## Mevcut karar (12 Eki 2026, FINAL)
- **Seçilen: Avrupa'nın MenuFit'i** (restoranda hedefe göre ne sipariş edilir, İngiltere öncelikli). Bakınız `arastirma/FINAL-dogrulanmis-fikir.md`.
- Yedek 1: AI Değer Tarayıcı. Yedek 2: Hobi AI koçu.
- Sıradaki adım: 14 günlük yüzsüz içerik testi.
- **Son karar: GO (koşullu).** Kapsam İngiltere restoran + meal deal + GLP-1 modu. Bakınız `arastirma/FINAL-derin-analiz-ve-karar.md`. Kritik açık konular: veritabanı hakkı için avukat görüşü, yüzsüz içerik dönüşümü (test). Creator programı kapsam dışı (kullanıcı reddetti). MenuFit strateji analizi: `arastirma/menufit-icerik-ve-strateji-analizi.md`.

## Güncel karar (12 Eki 2026, sadece kendi organik içeriği)
- Yeniden skorlama (`arastirma/yeniden-skorlama-sadece-organik.md`): Değer Tarayıcı 73, Boothie tipi 72, Avrupa MenuFit 70. Başa baş.
- Sıradaki adım: **14 günlük paralel kodsuz içerik testi**: Avrupa MenuFit (İngiltere) ve Değer Tarayıcı. Kazanana geç. İkisi de geçemezse Boothie tipi (kanalı kanıtlı) devreye girer.
- Test paketi hazır: `icerik/test-paketi-14-gun.md` (A: @ukmacromenu, @mealdealmacros. B: @whatsitworth.uk, @worthscanuk). Rakip içerik verisi: `arastirma/rakip-icerik-analizi.md`. Tüm kcal ve fiyat değerleri resmi kaynaktan doldurulacak, uydurma sayı yok.

## Karar ölçütü (kullanıcı, 12 Eki 2026)
- Ancak hem ben hem de şeytanın avukatı alt agent'ı "gerçekten büyük fırsat" diyebilirsek durulur.

## TikTok trend radarı (12 Eki 2026)
- Trend = dağıtım filtresi. Sonrasında gelir, talep ve boşluk filtreleri yine uygulanır.
- İlk bulgu: Yemek planlama ve tarif kategorisi şu an TikTok'ta organik çalışıyor. Herbi (GB Food #13, 2026-06, ~$15k/ay tahmini Screensdesign, @herbi.app 41k takipçi). NeatEat (ABD Food #9, 2026-07).
- Dönüşüm de kanıtlı: Herbi **GB Food grossing #3**, NeatEat **ABD Food grossing #5** (Apple RSS, 12 Eki).
- Kendi hesabıyla büyüme için referans Herbi ve NeatEat. MenuFit creator'larla büyüdü, kalp/video oranı 630.
