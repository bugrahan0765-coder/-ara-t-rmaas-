# Pazaryeri Satıcıları İçin SaaS Adayları — Kopyala + Geliştir Analizi

_Tarih: 12 Ekim 2026_

**Hedef:** Düşük pazarlama maliyetiyle ayda ~$10k gelir. Model B2C ya da bireysel satıcılara yönelik, kendi kendine abone olunan (self-serve) bir ürün. Satış toplantısı yok.
**Avantaj:** Kurucu tüm büyük pazaryerlerinde satış yapmış, kod yazabiliyor ve İngilizcesi iyi.

> Not: Gelir ve kullanıcı rakamlarının çoğu kurucuların veya şirketlerin kendi beyanı ya da tahmin. Kesin veri olarak değil, sinyal olarak okunmalı.

---

## 1. Ana bulgu: üç katman var

| Katman | Örnek | Kanıtlanmış para | Rekabet | Platform kuralı (ToS) riski |
|---|---|---|---|---|
| **A. Platformun içinde otomasyon** (paylaş, yeniden yayınla, otomatik teklif) | Closet Tools, Vinted botları, FB Marketplace relister'ları | **Yüksek.** Closet Tools ~$40k/ay | Çok yüksek | **Çok yüksek** |
| **B. Çapraz listeleme** (bir ilanı birden fazla platforma kopyalama) | Vendoo, List Perfectly, Crosslist, Closo | Yüksek (ABD) | ABD'de doymuş | Orta-yüksek. Vinted'in açık API'si yok, Leboncoin otomasyona izin vermiyor |
| **C. Platformun yanında araç** (stok, kâr, vergi, fiyat araştırması, ilan taslağı) | Margeo (Fransa), Flipwise, Underpriced AI, Ludex | Orta, büyüyor | Ülkeye ve nişe göre düşük-orta | **Düşük** |

**Sonuç:** A katmanı en çok para kazandıran ama artık hem kalabalık hem tehlikeli. Örneğin Vinted'in 8 Ekim 2026'da yürürlüğe girdiği bildirilen yeni şartlarının yetkisiz üçüncü taraf uygulamaları ve botları yasakladığı söyleniyor (tek kaynak, Vinted'in resmi metninden doğrulanmalı). Kullanıcılar da otomatik tespitle hesaplarının kapatıldığını bildiriyor.
**Kopyalanacak katman C:** Satıcının kendi verisiyle çalışır, platform hesabını tehlikeye atmaz, agent'ın avantajı burada en büyük.

---

## 2. Aday listesi

Puan 1-5 arası. Pazarlama maliyetinin düşüklüğü, ToS güvenliği, rekabet boşluğu ve agent avantajının toplamı.

| # | Kopyalanan model | Kanıt | Kopyalama açısı | Rekabet | ToS riski | Puan |
|---|---|---|---|---|---|---|
| 1 | **Margeo** (Fransa: Vinted/Leboncoin/eBay için stok, kâr ve vergi aracı) | Fransız pazarında konumlanmış, DAC7 içeriğiyle SEO yapıyor | **Almanya** (Kleinanzeigen + Vinted + eBay.de), sonra İtalya, İspanya, Hollanda, Polonya. Agent satış e-postalarını, CSV'leri ve ekran görüntülerini okuyup otomatik muhasebe çıkarır | Ülke bazında düşük | Düşük | ⭐⭐⭐⭐⭐ |
| 2 | **Closet Tools** (Poshmark otomasyonu, ~$40k/ay, 5 blog yazısıyla büyüdü) | Güçlü | Doğrudan kopyalamak yerine **SEO stratejisini** kopyala: belirli bir problemi hedefleyen birkaç blog yazısı + araç. Otomasyon kısmını alma | — | (Otomasyon kısmı yüksek) | Strateji olarak ⭐⭐⭐⭐ |
| 3 | **Underpriced AI / Thrift AI / Reliqe** (fotoğrafla fiyat ve satılmış ürün karşılaştırması, $5-10/ay) | Yeni, çok sayıda küçük rakip | **Avrupa'ya özel:** Vinted, Kleinanzeigen ve Leboncoin fiyatlarıyla, yerel dilde. Agent ürünü tanır, fiyat aralığı verir, "bu ürünü nerede satmalıyım?" sorusunu cevaplar | ABD'de orta, AB'de düşük | Orta. Satılmış ürün verisine erişim zor: eBay'in Insights API'si onaylı geliştiricilere kapalı | ⭐⭐⭐⭐ |
| 4 | **Ludex** (kart tarayıcı, $5-25/ay, $8M+ yatırım aldı) | Güçlü, Whatnot pazarı yıllık $8B satış hacmine ulaştı | **Az hizmet verilen bir koleksiyon nişi** (plak, LEGO, çizgi roman, saat vb.). Görüntü tanıma + fiyat + listeleme | Ana kategoriler dolu, nişler belirsiz | Düşük-orta | ⭐⭐⭐ (doğrulanmalı) |
| 5 | **Vendoo / List Perfectly** (çapraz listeleme, Vendoo 81k+ kullanıcı iddia ediyor, $9-150/ay) | Güçlü | AB'de API olmadığı için **tam otomasyon değil, "taslak + kopyala-yapıştır yardımcısı"** | ABD doymuş | Orta-yüksek | ⭐⭐ |
| 6 | **EverBee / eRank** (Etsy araştırma ve SEO; EverBee'nin kurucusu kendisi de Etsy satıcısı) | Orta-güçlü | Etsy dışındaki platformlar için benzer araç, ya da AI ile ilan optimizasyonu | Etsy'de kalabalık | Düşük | ⭐⭐ |
| 7 | **Flipwise / My Reseller Genie** (ABD'de satıcı muhasebesi) | Orta | 1 numaralı adayın ABD'deki karşılığı. Kalabalık | Orta-yüksek | Düşük | ⭐⭐ |
| 8 | **Vinted botları** (Dotb, Vinted Bot, Bleam, Vinz, VatBot, Vinkit; €6-20/ay) | Güçlü talep | **Kopyalama.** 7'den fazla rakip ve bildirilen ToS yasağı var | Çok yüksek | Çok yüksek | ⭐ |
| 9 | **FB Marketplace relister'ları** ($3-10/ay) | Talep var | **Kopyalama.** Çok sayıda ucuz klon var, Meta'nın kuralları belirsiz | Çok yüksek | Yüksek | ⭐ |
| 10 | **Trendyol satıcı panelleri** (Zunapro, BirFatura) | Var | Türkiye pazarı, gelir TL, müşteriler küçük işletme. $10k hedefi için zayıf | Orta | Düşük | ⭐⭐ |
| 11 | **Dolap / Gardrops araçları** | Araç bulunamadı | Pazar küçük, gelir TL | Yok | Bilinmiyor | ⭐ |
| 12 | **İlan taslağı oluşturucular** (fotoğraftan ilana: MyShopRender, QuickListAI, SellOut, ILoveListing) | Zayıf: kullanıcı sayıları küçük | Depop ve eBay bu özelliği **kendi içine ekledi**, platform rakibin oluyor | Yüksek | Orta | ⭐ |

---

## 3. En güçlü aday: "Almanya için Margeo" (ve sonra AB geneli)

**Neden:**
- **Düzenleme baskısı:** AB'nin DAC7 kuralına göre yılda 30 satış veya €2.000 ciroyu geçen satıcılar vergi dairesine raporlanıyor. Satıcılar endişeli ve "Vinted vergi", "Kleinanzeigen DAC7" gibi aramalar yapıyor. Bu, organik trafik demek.
- **Fransa'daki boşluk dolduruluyor (Margeo), diğer ülkeler açık görünüyor.** Bu doğrulanmalı.
- **Platform riski düşük:** Araç pazaryerine giriş yapıp işlem yapmıyor. Satıcının kendi verisini (satış bildirim e-postaları, dışa aktarılan dosyalar, ekran görüntüleri) okuyor.
- **Agent avantajı gerçek:** Vinted'in API'si olmadığı için veri dağınık. Agent e-posta kutusundaki "ürünün satıldı" mailleri ve fatura PDF'lerinden otomatik kayıt oluşturur, maliyetle eşleştirir, kâr ve vergi özeti üretir, "DAC7 eşiğine yaklaşıyorsun" uyarısı verir.
- **Kurucu avantajı:** Satıcı olarak bu derdi kendin yaşadın.

**Gelir matematiği:** Aylık €8-15 abonelikle $10k için ~700-1.200 ödeyen kullanıcı gerekir. Almanya + 2-3 AB ülkesiyle 12-24 ayda gerçekçi bir hedef. Garanti değil.

**Düşük maliyetli pazarlama:**
- Yerel dilde, sorun odaklı SEO yazıları. Closet Tools modeli: az sayıda ama çok isabetli yazı.
- Ücretsiz araçlar: DAC7 eşik hesaplayıcı, platform ücret karşılaştırıcı. Bunlar mıknatıs görevi görür.
- Satıcı Facebook grupları ve Reddit (r/Flipping, ülke subredditleri).
- Reseller YouTuber'lara affiliate (komisyon) programı.

**Riskler:**
- Vergi tavsiyesi kısıtlamaları var. Ürün "kayıt ve raporlama aracı" olarak konumlanmalı, vergi danışmanlığı olarak değil.
- Margeo veya benzerlerinin diğer AB ülkelerine genişlemesi.
- Gmail okuma izni gibi hassas OAuth kapsamları güvenlik incelemesi gerektirir. Alternatif: e-posta yönlendirme adresi.

---

## 4. Doğrulama adımları (kod yazmadan önce, 1-2 hafta)

1. Almanya, İtalya, İspanya ve Hollanda'da benzer bir ürün var mı? Yerel dilde Google + App Store + Chrome Web Store taraması.
2. Margeo'nun trafik ve kullanıcı sinyalleri: blog sayısı, App Store yorumları, sosyal medya.
3. Hedef ülkede "Vinted Steuer", "Kleinanzeigen DAC7", "Gewinn berechnen Wiederverkauf" gibi aramaların hacmi.
4. 3-5 satıcı grubunda problem odaklı gözlem: insanlar bu konuyu ne sıklıkla soruyor?
5. Tek sayfalık açılış sayfası + bekleme listesi + ücretsiz DAC7 hesaplayıcı. 2-4 haftada 100'den fazla kayıt gelirse yola devam.

---

## Kaynaklar

- [Closet Tools – Indie Hackers ($38k/ay)](https://www.indiehackers.com/post/how-the-winner-of-indie-hackers-built-a-38k-month-saas-business-with-a-dollar-a-day-product-aaad5b1ef1)
- [Closet Tools – Latka (tahmini)](https://getlatka.com/companies/closet-tools)
- [Vendoo](https://www.vendoo.co/cross-listing-app) · [Vendoo vs List Perfectly](https://www.vendoo.co/vendoo-vs-listperfectly) · [Crosslisting karşılaştırması 2026](https://www.voolist.com/blog/best-cross-listing-apps-2026)
- [Vinted Bot (Chrome Web Store)](https://chromewebstore.google.com/detail/vinted-bot/okoinghdkbgoppkcmnokjfeajkahjena?hl=en) · [Dotb](https://dotb.io/) · [Bleam](https://bleam.app/en) · [Vinted bot araçları – Souk](https://souk.to/en/blog/vinted-bot)
- [Vinted yeni kurallar – Crosslist](https://crosslist.com/blog/does-vinted-allow-resellers) · [Vinted hesap kapatmaları – Thred](https://thred.com/?p=22529) · [Selleraider değerlendirmesi](https://friptadium.com/blogs/actualites/selleraider-avis-prix-vinted)
- [Margeo – Fransa crosslisting karşılaştırması](https://margeoapp.com/blog/comparatif-applications-crosslisting-france-2026) · [Margeo – DAC7 açıklaması](https://margeoapp.com/en/blog/dac7-explained-online-sellers-europe/)
- [Kleinanzeigen DAC7 – mobiflip](https://www.mobiflip.de/shortnews/dac7-kleinanzeigen-erklaert-was-den-finanzbehoerden-gemeldet-wird/) · [Kleinanzeigen Tool – MyDealz](https://www.mydealz.de/deals/kleinanzeigen-enhanced-black-week-70-dauerhaft-auf-privaten-jahreslizenzen-17-21112025-2671887)
- [DAC7 – Cross-border magazine](https://cross-border-magazine.com/dac7-regulation-impact-and-tax-obligations/) · [DAC7 – VRT](https://www.vrt.be/vrtnws/nl/2023/03/23/vinted-geeft-gegevens-door-aan-fiscus/)
- [Underpriced AI](https://underpricedai.com/blog/best-thrift-store-apps) · [Reseller kâr kontrol uygulaması – Indie Hackers](https://www.indiehackers.com/post/built-a-profit-checker-app-for-resellers-that-solves-the-should-i-buy-this-problem-22fe82e6ca)
- [eBay Marketplace Insights API](https://developer.ebay.com/api-docs/buy/marketplace-insights/overview.html)
- [Ludex üyelik fiyatları](https://www.ludex.com/membership) · [Ludex yatırım – Built In](https://www.builtinchicago.org/articles/ludex-raises-8m-ai-trading-cards)
- [Whatnot – Modern Retail](https://www.modernretail.co/technology/live-shopping-platform-whatnot-taps-shopify-to-reach-millions-of-merchants-as-it-chases-growth/)
- [EverBee vs eRank](https://revenuegeeks.com/compare/erank-vs-everbee)
- [FB Marketplace relister](https://chromewebstore.google.com/detail/dfgockaiagdndpheemgihkchcdoekpki)
- [Depop AI açıklama aracı – Retail Dive](https://www.retaildive.com/news/depop-generative-artificial-intelligence-product-descriptions-photo/727860/)
- [Flipwise](https://flipwise.app/about)
- [Zunapro – Trendyol](https://www.zunapro.com/turkey/tr/pazaryeri/trendyol) · [BirFatura](https://birfatura.com/pazaryeri-entegrasyonu/)
- [Micro-SaaS gerçeklik kontrolü – futurion](https://futurion.blog/the-indie-hacker-reality-check-what-micro-saas-actually-looks-like-in-2026/) · [Bağımsız SaaS gelirleri 2026 – BigIdeasDB](https://bigideasdb.com/state-of-indie-saas-revenue-2026)
