# Son Karar ve Derin Analiz: İngiltere Öncelikli "Dışarıda ve Market Yemeği Makro Rehberi"

_Tarih: 12 Ekim 2026. [FINAL-dogrulanmis-fikir.md](FINAL-dogrulanmis-fikir.md) dosyasının derinleştirilmiş hâli._

## KARAR: GO (koşullu)

**Ürün:** İngiltere'de yaşayan, kilo vermek, protein almak ya da GLP-1 ilacı (Mounjaro/Wegovy) kullanmak isteyenlere, **gittiği zincir restoranda ve aldığı market "meal deal" paketinde tam olarak ne seçmesi ve siparişi nasıl değiştirmesi gerektiğini** söyleyen AI uygulaması. Önce İngiltere, sonra Almanya (döner dahil).

**Koşul:** 14 günlük yüzsüz içerik testi ölçütleri geçmeden kod yazılmayacak.

## 1. Lider ürün: MenuFit, güncel durum (12 Eki 2026)

| Gösterge | Değer | Kaynak |
|---|---|---|
| ABD Health en çok kazandıranlar | **#47** (önceki gün #44) / ücretsizler #21 | Apple RSS (objektif, istikrarlı) |
| Değerlendirme | 54.491 (ABD, 4.77), 343 (GB, 4.44), 53 (DE, 3.79) | Apple API |
| Tahmini gelir | ~$850k/ay | Screensdesign (tahmin) |
| Kanal | Kurucunun fast food hack içerikleri + influencer'lar (GB yorumu: "promoting yourself online with influencers") | SGE, kullanıcı yorumu |
| Fiyat | Haftalık deneme sonrası ~$50/yıl, $9.99/ay | Yorumlar, App Store |

### Kullanıcı yorumlarından çıkan ürün boşlukları

**ABD yorumları:**
1. "**Inaccurate Calorie Counts**": Kaloriler gerçek değerlerden çok farklı.
2. "Önerdiği ürünler **menüde yok**." AI uydurma (halüsinasyon).
3. "Makro hedeflerini **özelleştiremiyorsun**."
4. "Yüksek protein seçince **saçma, uygulanamaz** öneriler veriyor."
5. "**Siparişi nasıl değiştireceğini söylemiyor**." Hangi malzemeyi çıkarmalı?
6. "Müşteri desteği yok." "Ücret kurulumun sonunda söyleniyor."

**İngiltere yorumları (doğrudan pazar boşluğu):**
- "**Not made for Europe**… McDonald's'ta McGriddle öneriyor, burada yok."
- "Ülkemde olmayan ürünleri öneriyor, kullanılamaz."
- "Not relevant to anywhere outside of America."
- "Kebap dürüm + patates 400 küsur kalori diyor, çok düşük."
- "**Can't wait for an app to be released which actually cares about its users.**"

**Sonuç:** Pazar lideri İngiltere'de **yanlış ülke verisi ve yanlış kalori** yüzünden başarısız. Bizim temel vaadimiz bunun tersi: **"İngiltere'ye özel, resmi kaloriler, uydurma yok."**

## 2. Rakip haritası (Avrupa)

| Rakip | Konum | Durum |
|---|---|---|
| MenuFit | ABD odaklı AI tahmini | GB'de zayıf ve şikâyetli, DE'de 3.79 |
| Macrotarian | "Resmi veri, 240k restoran" | GB'de 31 değerlendirme, TikTok 1.1k |
| LeanBites | ABD zincirleri, resmi veri | GB'de 25 değerlendirme |
| Scranly, MenuMacros, NutriFinder, LeanPick, TasteLens, Menu AI, What2Eat, CleanMenu (Paris), Order Fit (FR) | 2025-26 klonları | 0-4 değerlendirme |
| MyFitnessPal, MacroFactor | Kayıt tutma | "Ne sipariş edeyim?" sorusunu yanıtlamıyor |
| Fitness Chef uygulaması (GB) | Kalori sayacı | 473 değerlendirme, farklı iş |

**Kimse İngiltere'ye özel ve resmi veriyle bu işi yapmıyor.** Meal deal + restoran + GLP-1 birleşimi hiç yok.

## 3. Talep kanıtı (Google otomatik tamamlama, GB ve DE, 12 Eki 2026)

- **Meal deal:** "high protein meal deal **tesco / sainsbury's / asda / m&s / coop / morrisons**", "highest protein meal deal", "low calorie meal deal…"
- **Zincirler:**
  - "greggs high protein (low calorie / lunch / breakfast / items)"
  - "wetherspoons low calorie (meals / menu / breakfast / high protein)"
  - "nandos high protein (order / low calorie options / sides)"
  - "what to order at mcdonalds on a calorie deficit / for high protein"
- **GLP-1:** "what to eat on mounjaro (uk / to avoid nausea / injection day)", "**what to eat at mcdonald's on mounjaro**", "…on glp-1"
- **Genel:** "calorie deficit app uk", "calorie deficit meals uk"
- **Almanya:** "kalorienarm bei burger king/mcdonalds/subway/kfc/nordsee/backwerk", "**dönerbox kalorien** (mit pommes / ohne soße / hähnchen / klein)"

## 4. Pazar büyüklüğü (İngiltere)

- İngilizlerin **%27'si** ayda en az bir kez dışarıda yiyor, ~%10'u haftalık. En sık gidenler 18-34 yaş (erkek %39, kadın %35). (YouGov, Tem 2024 – Tem 2025)
- Sık gelenlerin gittiği yerler: McDonald's %45, Wetherspoon %34, Costa %28, KFC %20, Nando's %15. (YouGov)
- Halkın ~%12'si haftalık fast food alıyor. (Statista özeti)
- **GLP-1:** Tahminen 1.5-1.6 milyon yetişkin kullanıyor. Tek bir ayda 2.49M kutu satılmış (IQVIA). Kaynaklar ticari, dikkatli okunmalı.
- **Hedef için gereken pay:** $10k MRR ≈ **~3.000-3.500 aktif abone** (net ~$3/abone/ay varsayımı). Bu, haftalık fast food alan ~6 milyon İngiliz'in **%0.05'i**.

## 5. Veri stratejisi (en kritik teknik ve hukuki konu)

| Kaynak | Ne için | Hukuki durum | Karar |
|---|---|---|---|
| **Kullanıcının çektiği menü fotoğrafı** (İngiltere'de 250+ çalışanlı zincirlerin menüde kcal göstermesi zorunlu) | Restoranda anlık doğru kcal (OCR) + AI ile makro tahmini (etiketli) | Kullanıcı kendi gördüğünü tarar. Toplu veri çekme yok | **Ana mekanizma**: "uydurma yok" vaadinin dayanağı |
| Zincirlerin web sitelerindeki besin tabloları (Wetherspoon, Wagamama vb. yayınlıyor) | En popüler ~30 zincirin seçili ürünleri | **İngiltere veritabanı hakkı (database right):** büyük kısmı toplu çekmek risk taşıyabilir. Tekil gerçekler telif dışı ama derleme korunabilir | Sınırlı ve seçici kürasyon. **İngiliz fikri mülkiyet avukatından görüş alınmalı.** İzin ya da lisans talebi |
| **Open Food Facts** (ODbL açık veritabanı) | Market meal deal ürünleri (paketli ürünlerde besin etiketi zorunlu) | Ticari kullanıma izin var. Atıf ve paylaşım koşulu var | Meal deal optimize edici için **ana kaynak** |
| MenuTracker (Cambridge MRC) | — | **Sadece ticari olmayan kullanım** | Kullanılmayacak |

## 6. Ürün tasarımı (MVP, rakip zayıflıklarına göre)

1. **Sadece İngiltere'de var olan ürünler.** McGriddle yok, Greggs, Nando's, Spoons, Pret, Tesco meal deal var.
2. **Menüyü tara:** Basılı kcal'yi okur. Hedefe göre sıralar: kalori açığı, yüksek protein, **GLP-1 modu** (küçük porsiyon, önce protein, mide hassasiyeti).
3. **Tam sipariş talimatı:** "Mayonezsiz iste: −150 kcal", "Küçük patates al".
4. **Meal deal optimize edici:** "Tesco'da en yüksek proteinli meal deal kombinasyonu: …"
5. **Özelleştirilebilir makro hedefleri.**
6. **Şeffaf fiyat:** Ücretsiz katman (ör. haftada 5 tarama) + deneme. Fiyat baştan gösterilir. İngiltere'nin DMCC Act 2024 abonelik kurallarına uyum (yürürlük takvimi kontrol edilmeli).
7. Tahmini değerler her zaman "**tahmini**" etiketli. Tıbbi tavsiye yok.

**Fiyat taslağı:** £3.99/hafta, £24.99/yıl.
**AI maliyeti:** OCR + LLM, tarama başına yaklaşık birkaç sent.

## 7. İçerik ve dağıtım (yüzsüz, reklamsız)

**Kanıtlar:**
- Bir uygulama **725 TikTok slayt gösterisiyle ~700k kullanıcıya** ulaştı. En iyi paylaşımların %98'i slayt gösterisi. (SGE)
- Gerçek ürün fotoğraflarından yapılan slayt gösterileri genelde AI etiketi gerektirmez.
- İngiltere'de kalori karşılaştırma içeriğine iştah büyük: The Fitness Chef TikTok'ta 835k takipçi.

**Formatlar (MenuFit kancaları + İngiltere'ye uyarlama):**
1. "Greggs'te 400 kcal altı, 30g+ protein: 5 seçenek" (liste slayt gösterisi)
2. "Onlar vs. biz": "Bu Nando's siparişi 1.450 kcal, bu 620 kcal ve aynı doyuruculukta"
3. "En yüksek proteinli Tesco meal deal (2026)", her market için ayrı seri
4. "Mounjaro'dayken Spoons'ta ne sipariş edilir?" Reklamda reçeteli ilaç markası kullanılmaz. Bakınız Risk 5
5. Şok kalori: "Bu 'salata' 1.100 kcal"

**Çağrı:** "Yorum'a 'MENU' yaz" → otomatik DM ile link.

**Üretim:** Agent ile zincir × hedef × ürün kombinasyonlarından günlük 3-5 içerik.

**Kural:** AI sunucu ya da gerçekçi AI görsel varsa AI etiketi açık. Sahte "müşteri" tanıklığı yok.

## 8. Birim ekonomisi ve senaryolar (varsayımlar açık)

| Senaryo | Varsayım | 6. ay | 12. ay |
|---|---|---|---|
| Kötümser | İçerik tutmaz (14 gün testinde elenir) | — (sıfıra yakın kayıpla dur) | — |
| Temel | Ayda 15-25k kurulum, %3 ödeyen, net ~$3/ay, churn sonrası | ~$3-6k MRR | **~$10k MRR** |
| İyimser | Birkaç viral seri, ayda 50k+ kurulum | ~$10-15k MRR | $25k+ (+ Almanya) |

> Bu rakamlar hesaplama varsayımıdır, kanıt değildir. Asıl kanıt 14 günlük testten gelecek.

**Sabit maliyetler:** Apple Developer $99/yıl, sunucu ve AI ~$50-300/ay (kullanıcıyla artar), avukat görüşü ~£500-1.500 (tek seferlik tahmin).

## 9. Riskler ve azaltma

| # | Risk | Olasılık | Azaltma |
|---|---|---|---|
| 1 | Yüzsüz içerik, kurucu yüzlü içerik kadar dönüşmez | Orta | 14 günlük test. Slayt gösterisi kanıtı (SGE) |
| 2 | Veritabanı hakkı ve site kullanım şartları | Orta | Menü tarama + Open Food Facts + seçici kürasyon + avukat |
| 3 | Kalori doğruluğu hatası, güven kaybı | Orta | Resmi kcal öncelikli, tahminlerin etiketlenmesi |
| 4 | MenuFit İngiltere'ye yerelleşir | Orta | Hız, İngiltere'ye özel içerik markası, meal deal + GLP-1 farkı |
| 5 | Reklam kuralları (ASA/CAP: kilo kaybı oranı vaadi yasak; reçeteli ilaçların halka reklamı yasak) | Düşük-orta | "X kg ver" yok. İçerikte "GLP-1 kullanıcıları" gibi genel ifade, ilaç markası reklamı yok, tıbbi tavsiye yok |
| 6 | Sağlık verisi (GDPR'da özel kategori) | Düşük | Asgari veri, açık rıza, cihazda saklama tercihi |

## 10. Son karar ve takvim

**GO: İngiltere öncelikli. Önce içerik, sonra kod.**

| Hafta | İş |
|---|---|
| 1-2 | **Test:** 2 TikTok hesabı (GB İngilizce + yedek GB meal deal hesabı), günde 3 slayt gösterisi (resmi kcal verisiyle), bekleme listesi sayfası, "MENU" DM akışı, £24.99/yıl ön sipariş seçeneği |
| 2. haftanın sonu | **Karar kapısı:** 3+ içerik 50k+ izlenme, 500+ bekleme listesi, %3+ ön sipariş. Geçmezse format değişikliği. İkinci kez geçmezse yedek fikre (Değer Tarayıcı) dönüş |
| 3-6 | MVP (Expo/React Native + OCR + LLM + RevenueCat), 30 zincir + 6 market meal deal, avukat görüşü |
| 7-12 | TestFlight, bekleme listesine açılış, günlük içerik, App Store optimizasyonu (İngilizce anahtar kelimeler: "high protein meal deal", "low calorie greggs"…) |
| 4-6. ay | Almanya (Almanca içerik, "kalorienarm bei…", **Dönerbox** serisi) |

## Kaynaklar

- MenuFit: [App Store](https://apps.apple.com/us/app/menufit-healthy-eating-out/id6746144481) · [İngiltere yorumları](https://apps.apple.com/gb/app/menufit-healthy-eating-out/id6746144481?see-all=reviews) · [Screensdesign](https://screensdesign.com/apps/menufit-healthy-eating-out/) · [SGE vaka çalışması](https://www.socialgrowthengineers.com/fast-food-swaps-to-60k-mrr-in-two-months)
- Rakipler: [Macrotarian](https://macrotarian.com) · [LeanBites](https://leanbites.app) · [LeanBites incelemesi](https://leanbites.app/blog/best-restaurant-nutrition-rating-apps-2026-reviewed)
- Pazar: [YouGov – Britain's frequent diners (2025)](https://yougov.com/en-gb/articles/52573-whos-driving-britains-restaurant-economy-a-closer-look-at-frequent-diners) · [Lumina Intelligence](https://www.lumina-intelligence.com/wp-content/uploads/2021/06/131.Consumers-Dine-Out-Less-Often-but-Spend-More-per-Visit-Reveals-Lumina-Intelligence-1.docx) · [Understanding Society](https://www.understandingsociety.ac.uk/documentation/innovation-panel/variables/trffdwk/)
- Veri: [MenuTracker (JMIR / PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC9501650) · [Wetherspoon besin bilgisi](https://jdwetherspoon.com/wp-content/uploads/2025/03/ESG0010ALL-V4-0325-Fact-sheet-responsible-retailing.pdf) · [Wagamama kalorileri](https://www.thedonutwhole.com/does-wagamama-show-calories/)
- Hukuk: İngiltere kalori yasası ([Birketts](https://www.birketts.co.uk/legal-update/food-for-thought-the-introduction-of-calorie-labelling), [Citation](https://www.citation.co.uk/calorie-labelling-law-to-come-into-force-from-6-april/)) · ASA/CAP ([Osborne Clarke – CAP kilo kaybı](https://marketinglaw.osborneclarke.com/advertising-regulation/cap-note-weight-loss-claims/), [CMS](https://cms.law/en/gbr/legal-updates/big-facts-no-figures-weight-management-food-supplement-ad-gets-a-grilling-from-the-asa)) · TikTok AI etiketi ([Cinerads](https://www.cinerads.com/blog/tiktok-ai-content-policy), [Storrito](https://storrito.com/resources/tiktoks-2026-ai-labeling-rules-and-what-they-signal-for-platform-governance))
- İçerik kanıtı: [SGE – 725 slayt gösterisiyle 700k kullanıcı](https://www.socialgrowthengineers.com/700k-users-from-725-tiktok-slideshows) · [SGE – Soundmap slayt formatı](https://www.socialgrowthengineers.com/soundmaps-tiktok-slideshow-format-to-18m-views)
- GLP-1: [Second Nature](https://www.secondnature.io/guides/glp1s/mounjaro-private-prescriptions-uk) · [Irish News / IQVIA](https://www.irishnews.com/news/uk/almost-25-million-purchased-weight-loss-jabs-in-july-estimates-suggest-G2AEXRYAZ5JD7JAIH5C4RM6F3Y)
