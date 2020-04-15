# Kolayca film/dizi indirme scripti.

Bu kod ile puhu.tv üzerinden kolaylıkla film/dizi indirebilirsiniz. Dizi için özellikle bir script yazmadım ancak `puhu.py` modülünü kullanarak dizinin bölümlerini teker teker indirmekte kullanabilirsiniz. Mekanizma aynı işler.

**Örnek Çıktı:**

```bash
duoqu@DESKTOP-MB5HK7H MINGW64 ~/Projects/puhu
$ python interface.py
.
.
.
[77] Dedektif Galban
[78] Benimle Git
[79] Basınç
[80] Kırılma
[81] Skyark İçin Savaş
[82] Bitmeyen Kavga
[83] Geçmişin Gölgesinde
[84] Yarış
[85] Jack Strong
[86] Son Savaş: Aşk
[87] Kaçış Planı
[88] Sihirbazlar Çetesi
[89] Manhattan Gecesi
[90] Yolcular
[91] Koruyucu
[92] Sevimli Kahraman
[93] The Outsider
[94] Kolay Para 3
[95] Tetikçi
[96] Kurtarıcı
[97] Bilgisayar Korsanı
Film id'sini seçiniz: 97
Film: [Bilgisayar Korsanı]
Kalite '240', [bilgisayar-korsani-izle-240.m3u8] adı ile dosyaya kaydedildi.
FFMPEG Komutu:
ffmpeg -protocol_whitelist file,https,tls,tcp -i bilgisayar-korsani-izle-240.m3u8 bilgisayar-korsani-izle-240.mkv
--------------------------------------
Film: [Bilgisayar Korsanı]
Kalite '360', [bilgisayar-korsani-izle-360.m3u8] adı ile dosyaya kaydedildi.
FFMPEG Komutu:
ffmpeg -protocol_whitelist file,https,tls,tcp -i bilgisayar-korsani-izle-360.m3u8 bilgisayar-korsani-izle-360.mkv
--------------------------------------
Film: [Bilgisayar Korsanı]
Kalite '480', [bilgisayar-korsani-izle-480.m3u8] adı ile dosyaya kaydedildi.
FFMPEG Komutu:
ffmpeg -protocol_whitelist file,https,tls,tcp -i bilgisayar-korsani-izle-480.m3u8 bilgisayar-korsani-izle-480.mkv
--------------------------------------
Film: [Bilgisayar Korsanı]
Kalite '720', [bilgisayar-korsani-izle-720.m3u8] adı ile dosyaya kaydedildi.
FFMPEG Komutu:
ffmpeg -protocol_whitelist file,https,tls,tcp -i bilgisayar-korsani-izle-720.m3u8 bilgisayar-korsani-izle-720.mkv
--------------------------------------
Film: [Bilgisayar Korsanı]
Kalite '1080', [bilgisayar-korsani-izle-1080.m3u8] adı ile dosyaya kaydedildi.
FFMPEG Komutu:
ffmpeg -protocol_whitelist file,https,tls,tcp -i bilgisayar-korsani-izle-1080.m3u8 bilgisayar-korsani-izle-1080.mkv
--------------------------------------
```

## `interface.py` kullanımı:

```bash
duoqu@DESKTOP-MB5HK7H MINGW64 ~/Projects/puhu
$ python interface.py
```

## `puhu.py` kullanımı:

```python
# Yazdığınız scriptin `puhu.py` ile aynı klasörde bulunması gerekmektedir.
from puhu import getPlist


# İçerisinde {`kalite`: `m3u8 data`} formatında veri vardır, kalite `144, 240, 360, 480, 720, 1080` değerleridir.
# m3u8 data ise direk m3u8 formatında veridir. Dosyaya kaydetmekte kullanabilirsiniz.
m3u8 = getPlist("/ejderha-gozler-izle")
