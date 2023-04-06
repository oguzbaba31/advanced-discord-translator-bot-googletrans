# discord-tr-translator-bot-googletrans
cw's discord tr translator bot with googletrans free api

Bu kod, Discord sunucularında, önceden belirlenmiş bir komut kullanarak, hedef dile metin veya ek dosyalar çevirme işlevi sağlar. Kullanıcılar komutu !translate [hedef_dil] [metin] şeklinde kullanabilirler. Hedef dile çevrilmesi gereken metni yazarken, birden fazla kelime kullanıyorsa, aralarına boşluk bırakmalıdırlar. Bu komut, discord.py kütüphanesi kullanarak yazılmıştır ve aşağıdaki işlevleri yerine getirir:<br><br>

Ek dosya eklerken, resimler için çeviri metni ekleyerek görüntüyü değiştirir ve resimleri Discord sunucusuna gönderir.<br>
PDF, doc, docx ve txt dosyaları gibi metin tabanlı dosyaları çevirir.<br>
Gönderilen metnin çevirisini hedef dile tercüme eder.<br>
Çevirileri hafızaya alır ve tekrar kullanılanları saklar.<br>
Çok uzun metinler için get_long_text_translation fonksiyonu kullanır.<br><br>

Bu kod, aynı zamanda bazı dışa bağımlılıkları kullanır, bunlar:
os: İşletim sistemi ile etkileşim sağlar.<br>
re: Düzenli ifadelerle metin işleme için kullanılır.<br>
asyncio: Asenkron işlemler için kullanılır.<br>
discord: Discord API'leri için kullanılır.<br>
aiohttp: HTTP istekleri yapmak için kullanılır.<br>
pytesseract: OCR işlevselliği için kullanılır.<br>
googletrans: Google Translate API'leri için kullanılır.<br>
difflib: Dize benzerliği bulmak için kullanılır.<br>
dotenv: Kimlik doğrulama bilgilerini çevre değişkenlerinden yüklemek için kullanılır.<br>
io: Giriş/Çıkış işlemleri için kullanılır.<br>
PIL: Resim dosyaları için işlevselliğe sahip olan Python resim kütüphanesi.
