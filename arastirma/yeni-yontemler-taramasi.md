# Yeni Yöntemlerle Fikir Taraması (Tur 2)

_Tarih: 12 Ekim 2026_

## Kullanılan yeni yöntemler

| # | Yöntem | Veri kaynağı | Neyi kanıtlar |
|---|---|---|---|
| F | **Coğrafi arbitraj (ABD → AB/TR):** ABD'de kazanan genç uygulamalar DE, GB, FR ve TR'de de kazanıyor mu? | App Store en çok kazandıranlar, 5 ülke × 15 kategori × ilk 200 | Talebin ülkeler arası taşınabilirliği, boş pazarlar |
| G | **Ters arbitraj (AB/TR → ABD):** Yerelde kazanan ama ABD'de olmayan genç uygulamalar | Aynı veri | Yerel nişler, rakip yoğunluğu |
| H | **Arama talebi:** Google otomatik tamamlama, "bunu yapan bir uygulama var mı?" kalıpları (EN, DE, TR, FR; ~2.650 sorgu) | suggestqueries.google.com | Kullanıcıların aradığı ama bulamadığı şeyler |
| I | **Niş rekabet kontrolü:** Talep çıkan nişlerde App Store araması | iTunes Search API | Boşluk var mı? |

> Not: Google Trends API erişimi engellendi (HTTP 429). Bu yüzden arama talebi için otomatik tamamlama kullanıldı. Otomatik tamamlama hacim vermez, **popülerlik sırası** verir.

## F. Coğrafi arbitraj bulguları

- **Avrupa'da da kazananlar:** ThriftAI (DE Shopping #9, GB #7, FR #13), mise (DE Food **#2**, GB #4, FR #15), AntiqSnap, HoloDex, FoilSnap, WoodSense, Sewpal, BibleScroll (DE #22, GB #26).
  **Sonuç:** Değer tarayıcı ve yemek planlayıcı kategorilerinde Avrupalı kullanıcı da ödüyor. Ama rakipler Avrupa'ya zaten girmiş.
- **Sadece ABD'de kalanlar** (ABD hukukuna veya kültürüne bağlı): Toplu dava tazminatı bulucuları (Settlemate, Payout, PayMe), indirim/clearance bulucuları (DealHawk, Drop, Penny), GLP-1 takibi (MeAgain), Bible Widgets, TapCook, Whipp, Potto, Airclub.

## G. Ters arbitraj bulguları (Avrupa ve Türkiye'nin kendi kazananları)

| Alan | Uygulamalar (ülke, kategori ve sıra) | Yorum |
|---|---|---|
| **Vinted AI ilan** | Vendly (FR Shopping #4, Tem 2026), PreLoved AI (DE #16, GB #21), Vintly (DE #19, GB #26, Eyl 2026), DealUp AI (FR #15), Listed AI (FR) | **Fikir #1'in Avrupa versiyonunda talep kanıtlandı, rakipler de var** |
| **Yemek ve tarif (AB)** | Was kann ich essen? (DE Food #3, sosyal medya tariflerini süpermarket indirimleriyle birleştiriyor), Yuma (FR #4), Miso (DE #6), Choosy (DE #9), Basta (FR #6), Jow (FR #3), Disha, Yedeni, GoomY, Citron, Cookimag | **Almanya için yemek planlayıcı boşluğu YOK. Önceki varsayım yanlıştı** |
| **İslami (TR)** | Nurlu (#2), Quran Widgets (#4), Ruhun Gıdası (#6), Muslim Quotes (#11), Rahman (#16), Esma, Rahle, Nizam, Safar, Hüccet, Nuraly, Nur, Sereni, Elif… | Türkiye pazarı **doymuş** |
| **İslami (FR)** | CoranFacile (Books #8), Ihsan (#31), SalahScreen (#33, uygulama engelleyici), Maarifa (#34, AI), Noorly (#35) | Fransa aktif |
| **Stok ve beden alarmı (TR)** | StokDrop (Shopping #5), Simlek (#6, "Zara'da beden geldi") | Türkiye'de kanıtlanmış, gelir TL |
| **Vize (TR)** | VizeAsistan (Travel **#1**, Haz 2026, tek geliştirici) | Önceki vize fikri Türkiye'de kanıtlandı |
| **Hobi** | Catch ve Fisher AI (balıkçılık), Crumb ve BakeSide (ekşi maya), Crafly (el işi) | Hobi koçu kümesini destekliyor |

> **Ayar notu:** Bazı kategorilerde üst sıralar düşük gelirle alınabiliyor. Herbi İngiltere Food #5'te ama tahmini ~$15k/ay. PreLoved AI, Almanya Shopping #16'da sadece 26 değerlendirmeyle. Türkiye sıralamaları ABD'ye göre çok daha düşük gelirle oluşuyor.

## H. Arama talebi bulguları (otomatik tamamlama, 4 dil)

| Tema | EN | DE | FR | TR |
|---|---|---|---|---|
| **Tanıma ve tarama** (identify/scan/erkennt) | **417** | **111** | 18 | 0 |
| Çeviri ve sesli okuma | 67 | 38 | 11 | 1 |
| Değer, fiyat ve satış | 74 | 12 | 12 | 0 |
| Yemek ve market | 61 | 21 | 6 | 3 |
| Reels/Shorts engelleme | 17 | 12 | 13 | 2 |
| Para kazandıran uygulama | 9 | 0 | 7 | 5 |

**Tanınmak ya da değerlenmek istenenler:** İngilizcede madeni para (10), Pokémon (9), spor kartları (8), eşyalar/objeler (15), **LEGO (10)**, plak, antika, mücevher, pul. Almancada bitki, kuş sesi, **madeni para (5)**, böcek, **pul/Briefmarken (3)**, kene. Fransızcada "**application qui donne le prix des objets**" (eşyaların fiyatını söyleyen uygulama).

**Sonuç:** "Fotoğraftan tanı ve değerini söyle" talebi, App Store verisinden **bağımsız bir yöntemle** de doğrulandı.

## I. Niş rekabet kontrolü

- **Pul:** Uygulama stüdyoları (Next Vision PhilSnap, NineG, 326 LAB) ve klonlar var ama hepsi küçük (en büyüğü 3.5k değerlendirme). Almanca pul uygulaması bulunamadı. Ama kitle yaşlı olduğu için TikTok'a uyumu düşük, katalog verisi (Michel) de lisanslı.
- **LEGO:** Brickit (22k), Brickify (5.9k), Minifig Scan var. LEGO'nun kendi uygulamaları çok güçlü.
- **Vinted AI ilan:** Listed AI (FR, 535), PreLoved AI, VintSnap, Sell AI. Hepsi küçük ama listede.

## Kaynaklar

- App Store en çok kazandıranlar RSS: `itunes.apple.com/{us,de,gb,fr,tr}/rss/topgrossingapplications/limit=200/genre={id}/json` (12 Eki 2026)
- iTunes Lookup ve Search API
- Google otomatik tamamlama: `suggestqueries.google.com/complete/search?client=firefox`
- Gelir tahminleri: Screensdesign ([Herbi](https://screensdesign.com/apps/herbi-meal-planner-recipes/), [ReciMe](https://screensdesign.com/apps/recime-recipes-meal-planner/), [mise](https://screensdesign.com/apps/mise-meal-planner/))
