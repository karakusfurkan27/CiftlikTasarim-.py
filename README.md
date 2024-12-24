# Sürdürülebilir Çiftlik Tasarım Yazılımı

Bu yazılım, tarımda sürdürülebilir uygulamaları desteklemek için geliştirilmiş bir araçtır. Kullanıcılar, arazi optimizasyonu, su tüketimi yönetimi, enerji optimizasyonu ve gübre kullanımı gibi çeşitli hesaplamalar yapabilir. Bu sayede tarım alanlarında verimliliği artırırken, çevresel etkilerin de minimize edilmesine yardımcı olur.

## Özellikler

1. **Arazi Optimizasyonu**:
   - Kullanıcılar, toprak tipini (kumlu, killi, tınlı) ve ürünlerini belirleyerek, hangi ürünlerin topraklarına daha uygun olduğunu öğrenebilirler.
   - Ürünlerin ekonomik getirileri hesaplanarak en karlı seçenekler sıralanır.

2. **Su Tüketimi Hesaplama**:
   - Belirtilen bitki türü, alan ve su ihtiyacı bilgileriyle toplam su tüketimi hesaplanır.
   - Tarım alanlarında su verimliliğini artırmak için gerekli bilgiler sağlanır.

3. **Enerji Optimizasyonu**:
   - Günlük enerji tüketimi ile kullanılan yenilenebilir enerji kaynakları (güneş, rüzgar) arasında denge sağlanır.
   - Yenilenebilir enerji kaynaklarının sağladığı tasarruf ve karbon ayak izi hesaplanır.

4. **Gübre Kullanımı Hesaplama**:
   - Seçilen bitki türü ve alan büyüklüğüne göre gerekli gübre miktarı hesaplanır.
   - Organik veya kimyasal gübre tercihi yapılabilir.

## Kullanım

1. **Arazi Yönetimi**:
   - *Toprak Tipi* ve *Ürünler* giriş alanlarını kullanarak, araziye en uygun ürünlerin ve bunların ekonomik getirisinin hesaplanmasını sağlayın.

2. **Su Tüketimi Hesaplama**:
   - *Bitki Tipi*, *Alan* ve *Su İhtiyacı (m² başına)* verilerini girerek, toplam su tüketimini öğrenebilirsiniz.

3. **Enerji Yönetimi**:
   - *Günlük Enerji Tüketimi (kWh)* ve *Enerji Kaynakları* (güneş, rüzgar) bilgilerini girerek, yenilenebilir enerji kaynaklarıyla tasarrufu ve karbon ayak izini hesaplayabilirsiniz.

4. **Gübre Hesaplama**:
   - *Bitki Tipi* ve *Alan* verilerini girerek, kullanılacak gübre miktarını hesaplayın. Ayrıca organik veya kimyasal gübre seçenekleri de mevcuttur.

## Gereksinimler

- Python 3.x
- Tkinter kütüphanesi (GUI için)
- NumPy kütüphanesi (matematiksel hesaplamalar için)

## Kurulum

1. Python ve gerekli kütüphaneleri sisteminize kurun. (Eğer Tkinter ve NumPy kurulu değilse, şu komutlarla yükleyebilirsiniz):
   ```bash
   pip install tkinter numpy
   ```

2. Yazılımı çalıştırmak için Python dosyasını (`surdurulebilir_ciftlik_tasarimi.py`) çalıştırın:
   ```bash
   python surdurulebilir_ciftlik_tasarimi.py
   ```

## Ekran Görüntüsü

Yazılımın arayüzü kullanıcı dostudur ve her bölümü net bir şekilde ayrılmıştır. Her hesaplama işlemi için ayrı butonlar ve giriş alanları bulunmaktadır.

## Katkı

Bu yazılım açık kaynaklıdır ve katkılarınız her zaman memnuniyetle karşılanır. Lütfen önerilerinizi ve hata raporlarınızı GitHub üzerinden iletiniz.
