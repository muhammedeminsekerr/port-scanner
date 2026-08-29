# Port Scanner

Bir hedef üzerindeki açık portları tespit eden çok iş parçacıklı (multi-threaded) tarayıcı.

## Ne İşe Yarar?

Bir sunucuda hangi portların açık olduğunu ve üzerlerinde hangi servislerin çalıştığını tespit eder. Açık portlar bir sistemin dış dünyaya açılan kapılarıdır; güvenlik değerlendirmesinin ilk adımı bunları haritalamaktır.

## Özellikler

- Yaygın portların ve servislerinin taranması
- Çok iş parçacıklı tarama (hızlı)
- Açık port ve servis raporu

## Kullanım

    python port_scanner.py

## Nasıl Çalışır?

Her port için bir bağlantı denemesi yapar. Bağlantı başarılıysa port açıktır. Her portu ayrı bir thread'de tarayarak tümünü aynı anda dener, bu da taramayı tek tek beklemeye göre çok hızlandırır.

## Yasal Uyarı

Yalnızca kendi sistemlerinizde veya izniniz olan hedeflerde kullanın. İzinsiz port taraması birçok ülkede yasa dışıdır.

## Yazar

Muhammed Emin Şeker — Bilgisayar Mühendisliği Öğrencisi
GitHub: https://github.com/muhammedeminsekerr
