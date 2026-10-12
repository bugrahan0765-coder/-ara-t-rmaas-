# Rakip Analizi: AI Değer Tarayıcı ("Bu kaç para eder?")

_Tarih: 12 Ekim 2026_

> **Veri güvenilirliği:** Gelir rakamları üçüncü taraf **tahminleridir** (Screensdesign, Appllama, Sensor Tower'a atıf yapan bloglar), doğrulanmış değildir. Hiçbir rakip TrustMRR'da yok. Değerlendirme sayıları App Store'un açık API'sinden (12 Ekim 2026), fiyatlar App Store sayfalarından, TikTok sayıları profil sayfalarından alındı.

## 1. Özet karar

- **Kategori para kazandırıyor. Bu kanıtlandı.** Tek uygulamalık bağımsız geliştiriciler bile tahminen ayda $60-100k'ya çıkmış. Uygulama stüdyoları ayda $350-550k.
- **Ama alan 2025-2026'da çok kalabalıklaştı.** 40'tan fazla klon var. Almanca ve Fransızca sürümler, Vinted'e özel ilan yardımcıları da mevcut. "Avrupa'da rakip yok" varsayımı **yanlıştı.**
- **Ücretsiz platform araçları tehdit oluşturuyor.** Meta "Seller" (Temmuz 2026) ve eBay Magical Listing, fotoğraftan ilan ve **fiyat önerisini** bedavaya veriyor.
- **Asıl boşluk ürün değil, dağıtım.** Rakiplerin markalı TikTok hesapları neredeyse boş (en büyüğü SellRaze, 16k takipçi). Stüdyolar büyümeyi ücretli reklam ve ASO ile alıyor. **Organik içerik kanalı boş.**
- **Sonuç:** "Para kazandırır mı?" sorusuna dürüst cevap: **Kategori kazandırıyor, ama biz sadece ürünle değil, dağıtımla kazanırız.** Ürün, rakiplerle eşit seviyede olmalı, yani asgari şart. Avantaj içerik makinesinden gelmeli. Kod yazmadan önce 1-2 haftalık içerik testi şart.

## 2. Gelir ve büyüme tablosu

| Uygulama | Kim | Çıkış | Kategori | Tahmini gelir | Tahmini indirme | App Store değerlendirme | Not |
|---|---|---|---|---|---|---|---|
| **CoinSnap** | Next Vision (Hong Kong stüdyosu) | 2022 | Madeni para | **~$550k/ay** (bir blog Sensor Tower'a dayanarak $700k/ay diyor) | — | 306k (ABD) | Stüdyonun 24+ "Snap" uygulaması var |
| **Lens Scan** | **EvenEdge (Türk şirketi)** | Eyl 2024 | Her şeyi tanı | **~$450k/ay** | 150k | 19k | Genel tanıyıcı, değer de söylüyor |
| **AntiqSnap** | Next Vision | **Eki 2025** | Antika | **~$350k/ay** | **200k/ay** | 31k | **8 ayda** bu seviyeye geldi |
| **Curio** | Dionysus Labs (ABD, küçük) | Tem 2024 | Antika | ~$100k/ay | 30k | 16k | "750k+ kullanıcı" iddiası |
| **ThriftAI** | smallstack ApS (Danimarka, tek geliştirici) | **Haz 2025** | **Thrift/flip değeri** | **~$60k/ay** | **~20k/ay** | **20.6k ABD** (sitede "32k+") | Google Play'de Alışveriş kategorisinde #4 en çok kazanan (Mart 2026), 100k+ kurulum. **En doğrudan rakip** |
| **Zophi** | 326 LAB (Dubai stüdyosu) | Haz 2025 | Antika | ~$60k/ay | <5k | 11k | Aynı stüdyonun Gemli'si var |
| **SellRaze** | YC F25, $0.5-1.1M yatırım | Eyl 2023 | Fotoğraftan ilan + çapraz listeleme | Bilinmiyor | — | **41k ABD** | "500.000+ satıcı" iddiası |
| **Hero** | $1.5M seed (FJ Labs) | Eyl 2024 | Fotoğraftan ilan, eBay/FB | Bilinmiyor | — | 2k | "85.000+ satıcı" iddiası |
| **Gemli** | 326 LAB | Eki 2025 | Thrift/flip değeri | Bilinmiyor | — | 4.4k | — |
| **Flippr** | — | Ağu 2025 | Toplu tarama + eBay | Bilinmiyor | — | 1.7k | — |
| **Cluzy** | — | — | Tarama + eBay listeleme | Bilinmiyor | — | — | "50k+ reseller, 2.4M tarama" iddiası, Vinted verisi de var |
| **CollX** | — | 2022 | Spor kartları | Bilinmiyor | — | 49k | — |
| RePick, ThriftWise, Value AI, ResalePal, What is it Worth, Worthiva, Valuify, ThriftValue AI, Thrift Pal, Price Snap… | Çoğu tek kişi ya da stüdyo | 2025-26 | Thrift/değer | Küçük | — | 100-500 | **Klon dalgası** |

### Avrupa'ya özel rakipler

- **Yerelleştirilmiş tarayıcılar:** "ThriftAI: Détecteur de profit" (FR), "ThriftAI: Wiederverkaufshelfer" (DE, ayrı geliştirici), "Thrift AI: Wiederverkaufswert" (DE), Valuify (FR), AntiqSnap DE/FR.
- **Vinted ilan yardımcıları:** Vintapp (FR, 34k Vinted satışıyla kalibre edilmiş fiyat), FlipFlow (DE/AT/CH, 25+ marka için piyasa fiyatı), VintRapid, AutoLister, VintyLook, Fripio, Describ.it.
- **Dolaylı alternatifler:** Sellpy ("biz senin yerine satarız", DE), Momox, Faircado (fotoğrafla ikinci el arama).
- **Platformların kendisi:** Vinted'in Pro satıcılara yazım yardımı araçları getirdiği bildiriliyor (tek kaynak).

### Platformların ücretsiz araçları (en büyük tehdit)

- **Meta Seller** (24 Temmuz 2026, ABD, ücretsiz): Fotoğraftan başlık, açıklama, **fiyat önerisi** ve kategori. Toplu listeleme, birleşik gelen kutusu, performans istatistikleri. Çıkışından bu yana 12k değerlendirme.
- **eBay Magical Listing:** Fotoğraftan ilan ve fiyat önerisi. 2023'ten beri yayında.
- **Google Lens:** Ücretsiz görsel arama, benzer ürünlerin fiyatlarını gösteriyor.

## 3. Rakipler kullanıcılara ne sunuyor?

| Özellik | ThriftAI | SellRaze | Hero | Cluzy | Curio/AntiqSnap |
|---|---|---|---|---|---|
| Fotoğraftan tanıma (marka, durum, malzeme) | ✅ (3 fotoğraf: ön, arka, etiket) | ✅ (+barkod, metin) | ✅ (+video, ses) | ✅ | ✅ |
| Satılmış ürün verisiyle değer | ✅ eBay, Poshmark, FB, Depop, Mercari, Grailed | ✅ | ✅ | ✅ eBay, Poshmark, Depop (+Vinted iddiası) | İlan verisinden aralık |
| Satış hızı (sell-through rate) | ✅ (ek ücretli) | — | — | — | — |
| "Bu bir fırsat mı?" kararı | ✅ | — | — | ✅ (kâr marjı) | — |
| Hazır ilan ve tek dokunuşla yayınlama | ✅ | ✅ çapraz listeleme | ✅ eBay+FB | ✅ eBay | — |
| Envanter, kargo, mesaj yönetimi | — | ✅ | ✅ | — | Koleksiyon |
| Mağaza bulucu ve topluluk | ✅ | — | — | — | — |
| AI sohbet asistanı | — | — | — | — | ✅ |

## 4. Fiyatlandırma

| Uygulama | Haftalık | Aylık | Yıllık | Not |
|---|---|---|---|---|
| ThriftAI | $4.99 | $9.99 | $19.99-49.99 | 3 gün deneme. Satış hızı verisi ayrıca $19.99-39.99, "Multi Mode" $4.99 |
| Gemli / Zophi (326 LAB) | $3.99-4.99 | — | $19.99-34.99 | Stüdyo şablonu |
| AntiqSnap | $3.99 | — | $29.99-39.99 | — |
| Curio | $4.99-9.99 | — | $19.99-49.99 | — |
| RePick | $7.99-9.99 | — | $29.99-59.99 | "Canlı satış modu" premium |
| ThriftWise | — | $7.99 | $39.99 | — |
| SellRaze | — | $9.99-44.99 | $29.99-191.99 | Profesyonel satıcıya yönelik |
| Hero | — | $9.99-49.99 | — | Kademeli |
| Lens Scan | $8.99-9.99 | $14.99 | $79.99-89.99 | — |
| CollX | — | $9.99-24.99 | $99.99-249 | — |

**Kategori standardı:** Haftalık $3.99-4.99, yıllık $19.99-39.99, 3 günlük deneme, uygulama açılır açılmaz ödeme duvarı. ThriftAI'nin karşılama akışı **27 adımlık anket** içeriyor (deneyim, hedef, yaş, cinsiyet, "kişiselleştirilmiş kâr tahmini"). Cal AI tarzı yüksek dönüşümlü karşılama akışı kategoride standart.

## 5. Sosyal medya varlığı

| Marka | TikTok | Diğer |
|---|---|---|
| **SellRaze** | **@sellraze: 16k takipçi, 175k beğeni, 475 video** | Instagram, X, Discord |
| ThriftAI | Markalı hesap bulunamadı | Site: "Guides" (SEO blog), "Compare" sayfaları |
| Hero | @herostuff: 246 takipçi, 3 video | Product Hunt, App Store ağırlıklı |
| Gemli | @gemli.app: 230 takipçi, 1 video | — |
| Cluzy | @cluzy.app: 19 takipçi, **128 video** (tutmamış) | Blog, ücretsiz araçlar (SEO) |
| Curio | @curio.app: 59 takipçi | Facebook, Instagram (reklam pikseli var) |
| FlipTip | @fliptip.ai: 3 takipçi | Instagram |
| Underpriced AI | — | X, Facebook, Pinterest, YouTube |

**Yorum:**
- Rakipler **ücretli reklam (Meta/TikTok Ads), Apple Search Ads ve ASO** ile büyüyor. Stüdyolar (Next Vision, 326 LAB, EvenEdge) bunu sanayi ölçeğinde yapıyor.
- **Organik TikTok marka varlığı yok denecek kadar az.** Bu, içerik makinesiyle büyüyecek bir oyuncu için boşluk.
- Cluzy'nin 128 videoya rağmen 19 takipçide kalması uyarı: **Sadece video basmak yetmiyor, format ve hikâye anlatımı belirleyici.**
- Talep tarafında #thriftflip/#thrifthaul içerikleri milyarlarca izlenmeye ulaşmış (doğrulanmamış rakamlar). Format sevilen bir format.

## 6. Bizim için anlamı: farklılaşma seçenekleri

1. **Dağıtım farkı (ana strateji):** Rakiplerin boş bıraktığı organik TikTok/Reels/Shorts. Sabit içerik makinesi + şeffaf marka hesapları. Ürün rakiplerle eşit, avantaj içerikte.
2. **Kitle farkı:** Rakipler "thrifter/reseller"a, yani alıcı tarafına odaklı. **"Evimdeki eşyalar kaç para eder?"** satıcı tarafı (sade yaşam, taşınma, miras) daha geniş bir kitle ve TikTok'ta daha kolay viral oluyor. Curio "parent's house" ile buna kısmen değiniyor.
3. **Pazar farkı:** Avrupa yerel pazaryerleri (Kleinanzeigen, Leboncoin, Wallapop, Marktplaats, Vinted) **bir arada** ve yerel dilde içerikle. Kısmen dolu ama birleşik değer + "nerede satmalı?" karşılaştırması zayıf.
4. **Dikey niş (stüdyo stratejisi):** Next Vision'ın "Snap" serisi gibi tek kategoriye odaklı uygulamalar. Boş niş bulmak ayrı araştırma ister.

**Kaçınılması gerekenler:**
- Satılmış veri olmadan "kesin fiyat" iddiası. Curio ve CoinSnap'e doğruluk eleştirisi var.
- Agresif abonelik tuzağı. Değerlendirmelerde "abonelik şeffaflığı" şikâyeti var.
- Platformların zaten bedavaya verdiği "sadece ilan yazma" özelliğine bel bağlamak.

## 7. "Para kazandırır mı?" doğrulama planı (kod yazmadan, 14 gün)

1. **İçerik testi:** 3 şeffaf marka hesabı (EN: "evindeki eşyalar kaç para?", EN: thrift flip, DE: "Was ist das wert?"). Günde 2-3 gönderi, gerçek eşyalar ve dürüst değerlemeler.
2. **Ölçüm:** İzlenme dağılımı, kaydetme oranı, "benimkini de yap" yorumları, bekleme listesine dönüşüm.
3. **Ödeme isteği testi:** Bekleme listesine "erken erişim yıllık €19.99 ön sipariş" ya da $1 depozito seçeneği.
4. **Devam ölçütü:**
   - En az 3 gönderi 50k+ izlenme almış olmalı.
   - Bekleme listesi 500+ olmalı.
   - Ön sipariş/depozito oranı %3+ olmalı.

   Tutmazsa: formatı değiştir ya da dikey nişe geç. Ürün yazmadan kaybedilen tek şey 2 hafta olur.

## Kaynaklar

- App Store açık API (itunes.apple.com/search, US/GB/DE/FR, 12 Eki 2026) ve App Store sayfaları: [ThriftAI](https://apps.apple.com/us/app/thriftai-profit-identifier/id6746565278) · [SellRaze](https://apps.apple.com/gb/app/sellraze-list-sell-earn/id6455042085) · [Hero](https://apps.apple.com/us/app/hero-ai-listing-for-resellers/id6479718293) · [Gemli](https://apps.apple.com/us/app/thrift-profit-finder-gemli/id6753282566) · [Flippr](https://apps.apple.com/gb/app/flippr-complete-reselling-app/id6746770511) · [AntiqSnap](https://apps.apple.com/gb/app/antiqsnap-antique-identifier/id6752929120) · [Curio](https://apps.apple.com/gb/app/curio-antique-identifier/id6520380757) · [Zophi](https://apps.apple.com/gb/app/antique-identifier-zophi/id6745821219) · [Lens Scan](https://apps.apple.com/us/app/lens-scan-identify-anything/id6560107458) · [RePick](https://apps.apple.com/us/app/repick-thrift-item-value/id6755334675) · [ThriftWise](https://apps.apple.com/us/app/thriftwise-value-scanner/id6743677520) · [Meta Seller](https://apps.apple.com/us/app/seller-a-facebook-app/id6766382815) · [CollX](https://apps.apple.com/us/app/collx-sports-card-scanner/id1581164444)
- Gelir ve indirme tahminleri: [Screensdesign – ThriftAI](https://screensdesign.com/apps/thriftai-profit-identifier/) · [AntiqSnap](https://screensdesign.com/apps/antiqsnap-antique-id-value/) · [Curio](https://screensdesign.com/apps/curio-antique-identifier/) · [Zophi](https://screensdesign.com/apps/antique-identifier-zophi/) · [Lens Scan](https://screensdesign.com/apps/lens-scan-identify-anything/) · [CoinSnap](https://screensdesign.com/apps/coinsnap-coin-identifier/) · [Appllama – ThriftAI](https://appllama.io/apps/6746565278/thriftai-profit-identifier) · [App Pricing Lab – ThriftAI (Google Play)](https://www.apppricinglab.com/app/google_play/com.fulcra.thriftai) · [Sterling Currency – CoinSnap/Sensor Tower](https://www.sterlingcurrency.com.au/blog/news-research/the-fine-art-of-numismatics/coinsnap-a-fantastic-app-thats-not-fit-for-purpose/)
- Şirket ve yatırım bilgileri: [SellRaze – YC](https://www.ycombinator.com/companies/sellraze) · [SellRaze – LinkedIn](https://www.linkedin.com/company/sellraze) · [SellRaze – TechSquare ATL](https://www.techsquareatl.com/tech-square-news/2025/4/16/4b0p32evu99ch1mrry7nwgvbbbjo9e) · [Hero – Caplight](https://www.caplight.com/company/herostuff) · [Hero – Product Hunt](https://www.producthunt.com/products/hero-9/launches)
- Rakip siteleri: [thriftai.io](https://thriftai.io) · [sellraze.com](https://sellraze.com) · [herostuff.com](https://herostuff.com) · [cluzy.app](https://cluzy.app) · [curio.app](https://curio.app) · [fliptip.ai](https://fliptip.ai)
- Platform araçları: [Meta Seller – TechRepublic](https://www.techrepublic.com/article/news-meta-facebook-marketplace-seller-app/) · [Meta Seller – The Next Web](https://thenextweb.com/news/meta-seller-app-facebook-marketplace-ai-listing) · [eBay Magical Listing](https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/)
- Avrupa Vinted araçları: [Fripio – Vinted için AI araçları 2026](https://fripio.app/blog/ia-description-vinted-outils-2026) · [Vintapp](https://hunted.space/product/vintapp) · [FlipFlow](https://hunted.space/product/flip-flow)
- TikTok trendi: [Glossy – thrift flip](https://www.glossy.co/fashion/gen-z-is-trading-in-fast-fashion-clothing-hauls-for-thriftflips/) · [Daily Dot – thrift flip](https://www.dailydot.com/culture/thrift-flip-tiktok-trend) · [Corq Studio](https://corq.studio/?p=1641)
