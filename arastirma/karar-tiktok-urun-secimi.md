# Karar: TikTok Büyüme Stratejisine En Uygun Ürün

_Tarih: 12 Ekim 2026_

## TikTok'a uygunluk kriterleri

Önceki taramalardaki (TrustMRR, Boothie, Nutria vb.) kazanan örüntüden türetildi:

1. **Ürünün çıktısı içeriğin kendisi mi?** Önce/sonra, "ortaya çıkma anı" var mı?
2. **Kitle geniş mi?** Herkes için mi, yoksa dar bir meslek grubu için mi?
3. **Telefonda anlık satın alma** yapılabiliyor mu? (Haftalık abonelik, kredi paketi)
4. **Kalıcı bir ihtiyaç mı?** Trend gibi 3-6 ayda sönmemeli.
5. **Kurucunun avantajı** var mı? Pazaryeri tecrübesi, içerik kapasitesi, kod.
6. **Teknik ve hukuki risk** düşük mü?

## Adayların puanlaması (1-5)

| Aday | Çıktı = içerik | Kitle | Anlık satın alma | Kalıcı | Kurucu avantajı | Risk düşüklüğü | Toplam |
|---|---|---|---|---|---|---|---|
| **AI değer tarayıcı** (fotoğraf → "bu kaç para eder?" → nerede satılır → hazır ilan) | 5 | 5 | 4 | 5 | 5 | 4 | **28** |
| Avrupa Flipify (fırsat alarmı) | 3 | 2 | 4 | 4 | 5 | 2 (scraping) | 20 |
| Kalori/diyet kamera uygulaması (Nutria tipi) | 4 | 5 | 5 | 5 | 1 | 4 | 24 (kalabalık) |
| Trend estetik fotoğraf (Boothie tipi) | 5 | 5 | 5 | 1 | 2 | 4 | 22 |
| Niş sınav hazırlığı | 1 | 1 | 2 | 4 | 2 | 5 | 15 |
| Almanya için Margeo | 1 | 2 | 2 | 4 | 4 | 4 | 17 |

## Seçim: AI değer tarayıcı

**Ne yapar:** Kullanıcı bir eşyanın (gardıroptaki bir ceket, bit pazarından bir lamba, çatıdaki eski bir oyun konsolu) fotoğrafını çeker. Uygulama:
1. Ürünü tanır (marka, model, dönem, durum).
2. **Tahmini satış fiyat aralığını** verir. Örnek: "Vinted'de €35-50, eBay'de €45-60."
3. Hangi platformda daha hızlı ve pahalı satılacağını söyler.
4. Başlık, açıklama ve fiyatıyla **hazır ilan** metni üretir. Kullanıcı kopyalayıp kendisi yapıştırır. Platform hesabında otomasyon yok, bu yüzden kullanım şartları riski düşük.

**Neden TikTok'a en uygun aday:**
- **Ortaya çıkma anı doğal olarak viral bir format.** "Gardırobumu taradım, €800 çıktı", "Bit pazarında €2'ya aldım, değeri €90" gibi. "Bu kaç para eder?" içerikleri izlenme ve yorum toplar.
- **Kitle geniş.** Sadece flipper'lar değil, sade yaşam akımı, taşınanlar, ek gelir arayan herkes. Para kazandırdığı için ödeme isteği yüksek.
- **Kalıcı bir ihtiyaç.** Eski eşyayı satmak trend değil.
- **Kurucunun alan bilgisi** değerlemenin doğruluğunu ve içeriğin gerçekçiliğini sağlar.
- **Agent avantajı:** Görüntü tanıma, fiyat araştırması ve ilan yazımı tek akışta. İçerik makinesi de aynı motordan beslenir.

**Kanıt sinyalleri:**
- Underpriced AI, Thrift AI ve Reliqe ABD'de ayda $5-10'a satıyor (yeni ve küçük oyuncular).
- Ludex (kart tarayıcı) $8M+ yatırım aldı, ayda $5-25 alıyor.
- Flipify B2C satıcılarla 11 ayda $18k MRR'a çıktı.
- Avrupa'da (Vinted ve Kleinanzeigen fiyatlarıyla, yerel dilde) belirgin bir rakip bulunamadı. **Doğrulanmalı.**

**Riskler:**
- **Değerleme doğruluğu:** Yanlış fiyat güveni öldürür. Her zaman aralık ve gerekçe göstermek, "tahmin" olduğunu açıkça söylemek gerekir.
- **Fiyat verisine erişim:** eBay'in satılmış ürün API'si kısıtlı, Vinted'in açık API'si yok. Aktif ilan fiyatları, eBay Browse API, kullanıcının kendi geri bildirimi ve modelin bilgisi birleştirilecek. Yüksek frekanslı scraping yapılmayacak.
- **Platformlar benzer özelliği ekleyebilir.** eBay ve Depop fotoğraftan ilan oluşturmayı ekledi. Ama platformlar arası "nerede daha pahalı satarım?" karşılaştırmasını kendileri yapmaz. Bu ayrışma noktası.
- **TikTok kuralları:** Marka hesapları şeffaf olmalı, sahte kullanıcı tanıklığı olmamalı. İçerikteki eşyalar gerçek ve değerlemeler dürüst olmalı.

**Fiyatlandırma taslağı:**
- Ücretsiz 3 tarama.
- Haftalık €3.99 / yıllık €29.99, ya da kredi paketleri.
- Faz 2: "Fırsat alarmı" (Flipify özelliği) güçlü kullanıcılar için premium katman.

**Pazar sırası:**
1. İngilizce içerik → Birleşik Krallık (Vinted ve eBay UK güçlü) + ABD (eBay).
2. Almanca ve Fransızca içerik AI ile yerelleştirilir.
3. Türkiye (Dolap, Sahibinden) sonra. TL geliri düşük.

## İlk 30 gün: önce içerikle doğrula, sonra uygulama

**1. hafta: İçerik testi (uygulama olmadan)**
- 2-3 şeffaf marka hesabı aç. Örnek: "WorthIt UK", "Was ist das wert?"
- Her gün 2-3 içerik: gerçek eşyalar, el ile (Claude vision + eBay araştırması) yapılmış dürüst değerlemeler.
- Bekleme listesi sayfası yayına al.
- **Ölç:** İzlenme, kaydetme, "benimkini de yap" yorumları, bekleme listesine kayıt.

**2-4. hafta: Asgari ürün (MVP)**
- Expo/React Native + kamera → vision LLM → fiyat araştırması → ilan metni → RevenueCat ödeme duvarı.
- Agent tabanlı içerik hattı: taramalardan otomatik carousel ve video taslağı üretimi.
- TestFlight → bekleme listesine erken erişim.

**Devam veya vazgeç ölçütleri (30. gün):**
- En az birkaç içerik 10k+ izlenme almış olmalı.
- Bekleme listesinde 300-500+ kayıt olmalı.
- Erken kullanıcılarda ödeme duvarı dönüşümü %2+ olmalı.
