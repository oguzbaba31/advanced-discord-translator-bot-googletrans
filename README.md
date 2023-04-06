# discord-tr-translator-bot-googletrans
cw's discord translator bot with googletrans free api

This code provides a translation function for text or attached files to a target language using a predefined command in Discord servers. Users can use the command in the format !translate [target_language] [text]. When typing the text that needs to be translated into the target language, if they are using multiple words, they should leave spaces between them. This command is written using the discord.py library and performs the following functions:<br><br>

When attaching a file, it changes the image by adding the translation text for images and sends them to the Discord server.<br>
Translates text-based files such as PDF, doc, docx, and txt files.<br>
Translates the translation of the sent text into the target language.<br>
Stores and saves the translations for later use.<br>
Uses the get_long_text_translation function for very long texts.<br><br>

This code also uses some external dependencies, namely: os: Interacts with the operating system.<br>
re: Used for text processing with regular expressions.<br>
asyncio: Used for asynchronous operations.<br>
discord: Used for Discord APIs.<br>
aiohttp: Used for making HTTP requests.<br>
pytesseract: Used for OCR functionality.<br>
googletrans: Used for Google Translate APIs.<br>
difflib: Used to find string similarities.<br>
dotenv: Used to load authentication information from environment variables.<br>
io: Used for input/output operations.<br>
PIL: Python image library with functionality for image files.<br>

<br><br><br>

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
