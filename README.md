# discord-tr-translator-bot-googletrans
cw's discord tr translator bot with googletrans free api

Bu kod, Discord sunucularında, önceden belirlenmiş bir komut kullanarak, hedef dile metin veya ek dosyalar çevirme işlevi sağlar. Kullanıcılar komutu !translate [hedef_dil] [metin] şeklinde kullanabilirler. Hedef dile çevrilmesi gereken metni yazarken, birden fazla kelime kullanıyorsa, aralarına boşluk bırakmalıdırlar. Bu komut, discord.py kütüphanesi kullanarak yazılmıştır ve aşağıdaki işlevleri yerine getirir:

Ek dosya eklerken, resimler için çeviri metni ekleyerek görüntüyü değiştirir ve resimleri Discord sunucusuna gönderir.
PDF, doc, docx ve txt dosyaları gibi metin tabanlı dosyaları çevirir.
Gönderilen metnin çevirisini hedef dile tercüme eder.
Çevirileri hafızaya alır ve tekrar kullanılanları saklar.
Çok uzun metinler için get_long_text_translation fonksiyonu kullanır.
Bu kod, aynı zamanda bazı dışa bağımlılıkları kullanır, bunlar:

os: İşletim sistemi ile etkileşim sağlar.
re: Düzenli ifadelerle metin işleme için kullanılır.
asyncio: Asenkron işlemler için kullanılır.
discord: Discord API'leri için kullanılır.
aiohttp: HTTP istekleri yapmak için kullanılır.
pytesseract: OCR işlevselliği için kullanılır.
googletrans: Google Translate API'leri için kullanılır.
difflib: Dize benzerliği bulmak için kullanılır.
dotenv: Kimlik doğrulama bilgilerini çevre değişkenlerinden yüklemek için kullanılır.
io: Giriş/Çıkış işlemleri için kullanılır.
PIL: Resim dosyaları için işlevselliğe sahip olan Python resim kütüphanesi.
