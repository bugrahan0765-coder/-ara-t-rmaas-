# Yöntem Sentezi v2: Tüm araştırma yöntemleri tek hatta (12 Eki 2026)

Bu belge, bu sohbet boyunca öğrenilen tüm yöntemleri, bu turda bulunan **yeni** yöntemleri ve hepsinin birleştiği **v2 doğrulama hattını** özetler.

## A. Önceden kullanılan yöntemler (çalışanlar)
| # | Yöntem | Ne kanıtlar | Güvenilirlik |
|---|---|---|---|
| 1 | TrustMRR (`/channels/*`, `/category/*`, `/startup/{slug}.md`) | Doğrulanmış gelir ve kanal beyanı | ⭐⭐⭐ (gelir doğrulanmış, kanal beyanı kurucuya ait) |
| 2 | App Store top grossing RSS (çok ülke × kategori) | Gelir sırası | ⭐⭐⭐ (Apple verisi, sadece sıra) |
| 3 | iTunes Lookup/Search (çoklu ID ve ülke) | Çıkış tarihi, ülke bazında değerlendirme, dil, satıcı, site | ⭐⭐⭐ |
| 4 | Screensdesign gelir tahmini | Gelir tahmini | ⭐ (**bu turda 10 kat hatalı çıktı**, bkz. C) |
| 5 | Coğrafi arbitraj (ülke listeleri) | Pazar boşluğu | ⭐⭐ |
| 6 | Google otomatik tamamlama (çok dilli) | Arama talebi | ⭐⭐ |
| 7 | TikTok profil HTML'i | Takipçi, kalp, video sayısı | ⭐⭐ |
| 8 | Organik radar (genç uygulama → TikTok → kalp/video) | Organik dağıtım | ⭐⭐ |
| 9 | Dönüşüm filtresi (grossing ile free sırasını karşılaştırma) | İzlenme → para | ⭐⭐ |

## B. Bu turda bulunan yeni yöntemler
| # | Yöntem | Nasıl | Sonuç |
|---|---|---|---|
| N1 | **TikTok creator embed** (`tiktok.com/embed/@hesap`) | HTML içindeki `__FRONTITY_CONNECT_STATE__` JSON'u. Son ~12 video: izlenme, açıklama, kapak URL'si (`photomode` = slayt gösterisi). Video ID'si >> 32 = yayın zamanı | ✅ **Apify'sız video düzeyinde veri.** Format (slayt mı video mu), hook metni, yayın sıklığı, son gönderi tarihi |
| N2 | **Yerelleştirme boşluğu tarayıcısı** | Genç ABD kazanç uygulamaları için tek seferde 100 ID'lik `lookup?country=XX` ile 12 ülkede değerlendirme sayısı ve `languageCodesISO2A` | ✅ Sadece İngilizce olup DE, FR, ES ve MX'te binlerce değerlendirme alan uygulamalar = yerel dilde karşılanmamış talep |
| N3 | **TrustMRR çapraz kontrolü (gizli listeler)** | Stealth profillerinin slug'ı ürünü ele veriyor (örn. `depuff-ai`). Kuruluş tarihi, RevenueCat ve App Store çıkış tarihiyle eşleştirildi | ✅ Doğrulanmış gelire sahip gizli uygulamalar bulundu |
| N4 | **Yerel dilde rakip araması** | iTunes Search, yerel anahtar kelimeyle (örn. "gesicht abschwellen") | ✅ ASO boşluğunu ölçer |
| N5 | Pazar yeri listeleri (Flippa "organic TikTok") | Satıştaki uygulamaların doğrulanmış (vetted) P&L verisi | ⭐⭐ Sınırlı ama doğrulanmış |
| N6 | Vaka blogları (Shortimize, IH) | Çok hesaplı yüzsüz TikTok oyun kitapları | ⭐ (doğrulanmamış, sadece desen kanıtı) |
| ✗ | Reddit arama JSON'u | `403` | Kapalı |

## C. Önemli düzeltmeler
- **Screensdesign güvenilmez:** Depuff AI için Screensdesign tahmini **$6k/ay**. TrustMRR'da doğrulanmış (RevenueCat) MRR'ı **$59.194**. Yaklaşık 10 kat düşük tahmin. Bundan sonra Screensdesign sadece "taban" olarak kullanılacak, karar verirken asla tek başına kullanılmayacak.

(Hattın tamamı ve sonuçlar: [FIRSAT-v2.md](FIRSAT-v2.md))
