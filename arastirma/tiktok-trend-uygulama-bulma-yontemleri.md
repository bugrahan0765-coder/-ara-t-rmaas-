# TikTok'ta organik olarak trend olmuş uygulamaları bulma yöntemleri (12 Eki 2026)

Soru: "Ürün fikrini ve stratejiyi TikTok trendlerine göre kuralım. Organik içerikle trend olmuş uygulamaları nasıl buluruz? Opus anahtarı gerekir mi?"

## 1. Fikir hakkında görüş

**Mantıklı, ama bir şartla.** TikTok trendi bize **dağıtım uyumunu** gösterir: bu tür içerik bu kanalda yayılıyor mu? **Kalıcı talebi ve ödeme isteğini göstermez.** Trend olup para kazanmayan çok uygulama var. Bu yüzden trend bir **filtre** olarak kullanılmalı, tek başına karar sebebi olmamalı:

1. **Trend filtresi:** Kategoride genç bir uygulama organik TikTok ile yükseliyor mu? (yeni radar)
2. **Gelir filtresi:** Para kazanıyor mu? (TrustMRR doğrulanmış veya Screensdesign tahmini, ayrıca top grossing)
3. **Talep filtresi:** Kalıcı arama talebi var mı? (otomatik tamamlama)
4. **Boşluk filtresi:** Coğrafya veya dilde açık var mı?

Kısıtımız organik, yüzsüz ve creator'sız. Bu yüzden 1. filtre bizim için diğer kurucu tiplerine göre **daha önemli.** Reklamla büyüyen bir rakibin kanalını kopyalayamayız. Organik büyüyeninkini kopyalayabiliriz.

## 2. Yöntemleri test ettim

| # | Yöntem | Sonuç | Not |
|---|---|---|---|
| 1 | **Kategori top free listeleri (ABD ve GB) → genç uygulamalar (2025-06 sonrası) → site veya handle tahmini ile TikTok hesabı → kalp/video oranı** | ✅ **ÇALIŞIYOR** (ana yöntem) | 8 kategori × 2 ülkede 89 genç uygulama bulundu. 10'unun sitesinde TikTok linki var. ~45'i handle tahminiyle bulundu. Script: `araclar/` |
| 2 | **Kalp/video oranı = organik viralite göstergesi** | ✅ Ayırt edici | WayShot 90.640, NeatEat 82.420, Herbi 8.040. Karşılaştırma: DealSeek 216 (ABD Shopping #6, büyük ihtimalle ücretli edinim) |
| 3 | **"Listede üst sırada ama TikTok hesabı boş"** = ücretli veya ASO ile büyüme | ✅ Eleme için faydalı | Scrambly (ABD Health #5, 98k değerlendirme, 0 video), Shots (Photo #6, 0 video), Rips (Shopping #10, 0 video) |
| 4 | App Store yorumlarında "TikTok" geçme oranı | ❌ İşe yaramıyor | Cal AI (TikTok ile büyüdüğü biliniyor) en faydalı 50 yorumda 0 kez geçiyor. Yorum RSS'i de kararsız: aynı istek bazen 0 kayıt dönüyor |
| 5 | Otomatik tamamlama: "{kategori} app from tiktok" | ⚠️ Zayıf, sadece kategori düzeyinde | Çıkanlar: recipe app from tiktok, recipe saving app, tea app, dating app, ai app, language learning app, habit tracker app tiktok, workout/study/budget app tiktok. Uygulama adı vermiyor |
| 6 | TikTok discover ve hashtag sayfaları | ❌ Kapalı | HTML'de video verisi yok (bot koruması, sadece JS ile yükleniyor) |
| 7 | TikTok Creative Center (trend hashtag, ses, Top Ads) | ⚠️ Sadece tarayıcıdan, elle | API `40101 no permission` dönüyor. Tarayıcıda ücretsiz: trend hashtag ve sesler. Top Ads için TikTok Ads hesabıyla giriş gerekir |
| 8 | TikTok Ad Library (library.tiktok.com) | ⚠️ Elle | Sayfa JS ile yükleniyor. Programatik erişim TikTok **Commercial Content API** ile (developers.tiktok.com, başvuru gerekir). Sadece AB/EEA reklamlarını gösterir (DSA). Kullanımı: rakip reklam veriyor mu → organik mi? |
| 9 | Meta Ad Library | ⚠️ Elle | curl ile 403. Tarayıcıda çalışır |
| 10 | Genel (kategorisiz) top free listesi | ❌ Gürültülü | Büyük markalar (Meta, X, Primark) ve ücretli edinimli kısa dizi uygulamaları (PineDrama, VibeShort, BlinkDrama) dolduruyor |
| 11 | Sıralama hızı (günlük anlık görüntü, sıra sıçraması) | ⏳ Zamanlama gerekir | Tek anlık görüntü hızı göstermez. Günlük çalışan bir görev gerekir (bkz. bölüm 4) |
| 12 | TrustMRR channel=TikTok ve SGE vaka indeksi | ✅ Daha önce kullanıldı | Doğrulanmış gelir ve kanal beyanı. Az sayıda ama en güvenilir |

Ücretli üçüncü parti araçlar: Kalodata ve FastMoss TikTok Shop'taki fiziksel ürünleri izler, uygulamaları değil. TikTok Research API sadece akademisyenlere açık. Scraping hizmetleri TikTok kullanım şartlarına göre gri alanda. **Önerim: bunlara para verme.**

## 3. Radar v0'ın ilk bulguları (12 Eki 2026)

Kaynak: Apple kategori top free RSS (ABD ve GB), iTunes Lookup, TikTok profil HTML'i (`followerCount`, `heartCount`, `videoCount`). Gelir değerleri **Screensdesign tahmini** (doğrulanmış değil).

| Uygulama | Çıkış | Liste | TikTok | Kalp/video | Gelir | Doğrulama |
|---|---|---|---|---|---|---|
| **Herbi: Meal Planner + Recipes** | 2026-06-16 | **GB Food #13** | @herbi.app, 41,3k takipçi, 120 video | 8.040 | **~$15k/ay (Screensdesign tahmini)** | Bio linki herbiapp.com ✅ |
| **NeatEat - Meal Planner** | 2026-07-17 | **ABD Food #9** | @neateat.app, 24,9k takipçi, 5 görünür video | 82.420 | Screensdesign'da yok | Bio linki App Store id6783742855 ✅ |
| **WayShot: Aesthetic Photo Editor** | 2025-08-10 | ABD Photo #17, GB Photo #41 | @wayshot_app, 32,9k takipçi, 203 video | 90.640 | Screensdesign'da yok | Bio: "The #1 viral digicam app on TikTok" ✅ |
| Sporecast (mantar tanıma) | 2025-07-02 | GB Education #45 | @sporecast.app, 16,5k takipçi, 9 video | 5.311 | yok | Bio sporecast.com ✅ |
| MenuFit (referans) | 2025-08-06 | ABD Health #20 | @menufit.app, 23,6k takipçi, 225 video | 630 | ~$850k/ay (tahmin, önceki tur) | Büyümesi creator kodlarıyla, kendi hesabıyla değil |
| DealSeek (karşı örnek) | 2025-06-19 | ABD Shopping #6 | @dealseekapp, 47k takipçi, 744 video | 216 | yok | Çok video, az etkileşim. Büyüme başka kanaldan |

**Ne anlama geliyor:**
- **Yemek planlama ve tarif, şu an TikTok'ta organik olarak çalışan bir kategori.** 2026 yazında çıkan iki uygulama (Herbi GB'de, NeatEat ABD'de) birkaç ay içinde Food listesinde ilk 15'e girdi ve TikTok hesapları viral. Otomatik tamamlamada da "recipe app from tiktok" ilk sırada. Bu, yemek nişinin (MenuFit yönü) kendi organik içeriğimizle büyüyebileceğine dair **yeni ve olumlu bir kanıt.**
- **Düzeltme ve uyarı:** Daha önce "Almanya meal planner boşluğu" varsayımının yanlış olduğunu bulmuştuk. Burada da meal planner kategorisinin kalabalık olduğu görülüyor (Herbi, NeatEat, mise, TapCook). Herbi'nin GB'de yaptığı, MenuFit'in "restoranda ne sipariş edilir" açısından farklı. Yine de **aynı kitle ve aynı içerik dili.**
- **MenuFit'in kalp/video oranı düşük (630).** Bu, önceki bulguyu doğruluyor: MenuFit kendi hesabıyla değil, creator'larla büyüdü. Bizim modelimiz (kendi hesabı) için **Herbi ve NeatEat daha iyi referans.** İçerik analizinde onları incelemek gerekiyor.
- Fotoğraf tarafında WayShot ("digicam" estetiği), Boothie tipi fikrin kanalının çalıştığını bir kez daha gösteriyor.

## 4. Opus anahtarı (Anthropic API key) gerekir mi?

**Bu araştırma için hayır.** Yukarıdaki her şey bu Claude Code oturumunda çalıştı. Ayrı bir anahtar gerekmedi.

Anahtar sadece **otomatik ve düzenli çalışan bir radar** istersen gündeme gelir. Orada da üç seçenek var:

| Seçenek | Anahtar gerekir mi? | Maliyet | Ne zaman |
|---|---|---|---|
| A. **Claude Code rutini** (bu ortamda zamanlanmış görev, örn. haftada bir radar çalıştırıp `arastirma/`'ya rapor yazar) | Hayır, aboneliğinle çalışır | Ek API ücreti yok | **Önerilen.** En az kurulum |
| B. **Kendi sunucunda cron + Python** (sadece veri toplama) | Hayır. Toplama işi LLM gerektirmez | Sunucu ücreti | Sadece ham tablo yeterliyse |
| C. **Kendi sunucunda cron + Claude API** (uygulamayı sınıflandırma, içerik analizi, özet) | **Evet:** `ANTHROPIC_API_KEY` ortam değişkeni (veya `ant auth login`) | Claude Opus 5.5 (`claude-opus-5-5`): $4/$20 (girdi/çıktı, milyon token başına). Günde ~100 uygulama × ~2k token ≈ 200k girdi ≈ **~$1/gün.** Daha ucuz modeller de var: Sonnet 5.5 $2/$10, Haiku 5.5 $0,10/$0,50 (basit sınıflandırma için yeterli olabilir) | Kendi ürününe gömülü bir radar veya bir SaaS kurmak istersen |

Not: Uygulamanın kendisi (ör. menü fotoğrafından kcal okuma) yapıldığında, ürün içinde de bir API anahtarı gerekecek. Bu ayrı bir konu ve test aşamasında gerekmiyor.

## 5. Önerilen kullanım ve sonraki adımlar

1. **Radarı haftada bir çalıştır** (seçenek A). Çıktı: genç uygulama, liste sırası, TikTok hesabı, kalp/video oranı. Kalp/video > 5.000 ve son 3 ayda çıkmış olanlar "organik trend adayı" olur. Sonra onları gelir, talep ve boşluk filtrelerinden geçir.
2. **Herbi ve NeatEat'in TikTok içeriklerini analiz et:** format (slayt gösterisi mi, video mu), hook'lar, CTA, gönderi sıklığı. 14 günlük test paketindeki A hesabı hook'larını buna göre güncelle.
3. Radar kapsamını genişlet: DE, FR ve diğer kategoriler (Lifestyle, Finance, Health alt nişleri).
4. Sıralama hızı için günlük anlık görüntü (aynı rutin, ek bir dosyaya).

Scriptler: [`../araclar/tiktok-radar-1-grafik.py`](../araclar/tiktok-radar-1-grafik.py), [`../araclar/tiktok-radar-2-handle-tahmin.py`](../araclar/tiktok-radar-2-handle-tahmin.py). Ham çıktı: [`../araclar/radar-cikti-2026-10-12.jsonl`](../araclar/radar-cikti-2026-10-12.jsonl).

Sınırlar:
- Handle tahmini yanlış hesaba denk gelebilir. Tabloda bio linki doğrulanmış olanlar ✅ ile işaretli.
- Kalp sayısı hesabın tüm zamanlardaki toplamı. Silinmiş videolar oranı şişirebilir (NeatEat: 5 görünür video).
- Liste sırası tek bir günün anlık görüntüsü.
