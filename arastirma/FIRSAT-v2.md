# FIRSAT v2: Birleşik hat ile bulunan fırsat (12 Eki 2026)

> Yöntemler: [yontem-sentezi-v2.md](yontem-sentezi-v2.md). Ham veri: `araclar/v2/`.

## 1. Hat ve evren
1. **Evren:** 12 ülke (US, GB, DE, FR, ES, IT, NL, BR, MX, CA, AU, TR) × 22 kategori × (top grossing + top free, 200'er) = 528 RSS → **17.000+ uygulama.**
2. **Genç kazananlar:** 2025+ çıkışlı ve en az bir ülkede kazanç listesinde ilk 100'de olan **2.685 uygulama.**
3. **Organik TikTok filtresi:** Bunlardan seçilenler (3+ ülke veya ilk 25) + genç ABD kazanç uygulamaları ≈ **1.000 uygulama** TikTok embed ile tarandı (hesap, takipçi, son 12 video izlenmesi, slayt gösterisi oranı).
4. **Yerelleştirme boşluğu:** Sadece İngilizce olup İngilizce konuşulmayan ülkelerde çok değerlendirme alan uygulamalar.
5. **Dönüşüm:** Kazanç sırası ve çok ülkede kazanç listesinde olma. **Kalibrasyon:** TrustMRR'da doğrulanmış uygulamalarla (bkz. 3).
6. **Talep:** Çok dilli otomatik tamamlama. **Rakip:** yerel dilde App Store araması.
7. **Şeytanın avukatı:** Bağımsız alt agent ile çürütme denemesi.

## 2. Bulunan aday aileleri (organik TikTok ve dönüşüm birlikte)
| Aile | Örnekler (kazanç sırası / TikTok) | Bizim kısıtımıza uyum | Not |
|---|---|---|---|
| **Bebek ek gıda / BLW** | Solid Starts (EN; US Ed #32, GB #12, NL #15, DE #67; TikTok 360k). BabyPlate (EN, PL şirketi; ES Food #38; **yüzsüz slayt gösterileri 184k ve 123k**). Cuisinez pour bébé (FR Food #7; TikTok 202k; 700k indirme, kendi beyanı). BLW Ideas (ES Food **#2**). Svezzy (IT Food #10). Beikost App (DE Food #25, sadece 118 değerlendirme) | ✅ Yüzsüz slayt kanıtı var (BabyPlate). Yerel dilde kazanan var, Almanya'da güçlü bir uygulama yok | Ana aday, bkz. 4 |
| Sosyal medyadan kaydetme (tarif, seyahat) | Avocadish (DE Food #2, en yüksek video 3,5M). GoomY (FR Food #6, 972k). CookNest (ES #8). Herbi (GB #3). mio travel, itinio (ES Travel #20, 690k) | ✅ İçerik TikTok'un kendisinden geliyor | Her ülkede yerel oyuncu zaten var |
| AI yüz/vücut analizi (depuff, renk analizi) | Depuff AI (TrustMRR **$59k MRR**, sadece EN, DE/FR/ES/MX'te çok değerlendirme) | ✅ Görsel "sonuç ortaya çıkma" anı | Trend riski, beden imajı, iddia riski |
| AI arkadaş / "book boyfriend" | Heyyyy (US Ent #43; video başına ortanca **1M** izlenme, slayt + POV) | ✅ Yüzsüz | Reşit olmayan kullanıcı ve AI arkadaş regülasyonu riski çok yüksek |
| Yerel AI öğrenme (KI-Lernapp) | Retain Cards, Studyflash, Astra AI (DE) | Kısmen | Doymaya yakın |
| Yüzsüz veri slaytları | Sanity (NYC sağlık denetimi, 10/10 slayt), Wolf of Washington, ServicePerks | ✅ Tamamen ajanla otomatik | Gelir kanıtı zayıf |

## 3. Gelir kalibrasyonu (yeni bulgu)
| Uygulama | TrustMRR (doğrulanmış) son 30 gün | 12 ülkede kazanç listesi (ilk 100) |
|---|---|---|
| Nutria/Calyra (kalori) | $85.683 | Sadece TR Health #22 |
| Depuff AI (yüz ödemi) | MRR $59.194 | Hiçbirinde yok (sadece MX free #72) |
| AbMaxx | $48.068 | Sadece MX Health #93 |
| Boothie | $43.453 | Sadece TR Photo #31 |
| GoTall | $31.422 | Sadece TR Health #99 |
| Imposter AI | $18.904 | Hiçbirinde yok |

**Sonuç:** Ayda $30-85k kazanan uygulamalar bile ABD Health ve Photo ilk 100'üne giremiyor. Yani ABD veya GB'de Health, Education ya da Medical ilk 100'ünde olmak **çok büyük gelir** demek. Food ve Lifestyle gibi kategorilerde eşik daha düşük. **Önceki "MenuFit ABD Health #47" yorumu da bu yüzden büyük gelire işaret ediyor.**
