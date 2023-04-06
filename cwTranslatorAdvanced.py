import os
import re
import asyncio
import discord
import aiohttp
import pytesseract
from googletrans import Translator
from difflib import SequenceMatcher
from googletrans import LANGUAGES
from discord.ext import commands
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

load_dotenv()
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
translator = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])

ceviriler = {}

async def translate_attachments(message, dest_lang):
    attachments = message.attachments
    if len(attachments) > 0:
        for attachment in attachments:
            try:
                content_type = attachment.filename.split('.')[-1]
                file_path = f"{attachment.id}.{content_type}"
                await attachment.save(file_path)
                ceviri = await translate_file(file_path, dest_lang)
                if content_type == 'jpg' or content_type == 'jpeg' or content_type == 'png' or content_type == 'bmp':
                    image = Image.open(file_path)
                    img_with_text = add_text_to_image(image, ceviri)
                    bytesIO = BytesIO()
                    img_with_text.save(bytesIO, format='PNG')
                    bytes = bytesIO.getvalue()
                    await message.channel.send(file=discord.File(fp=BytesIO(bytes), filename=f'{attachment.filename} çeviri.png'))
                else:
                    await message.channel.send(f"{attachment.filename} çevirisi:\n{ceviri}")
            except Exception as e:
                await message.channel.send(f"Hata oluştu: {e}")
            finally:
                os.remove(file_path)

async def translate_image(image, dest_lang):
    try:
        content = pytesseract.image_to_string(image)
        ceviri = await translator.translate(content, dest_lang)
        return ceviri.text
    except Exception as e:
        return f"Hata oluştu: {e}"

async def translate_file(file_path, dest_lang):
    try:
        content_type = file_path.split('.')[-1]
        if content_type == 'txt' or content_type == 'doc' or content_type == 'docx' or content_type == 'pdf':
            with open(file_path, 'rb') as file:
                content = file.read().decode('utf-8')
            if len(content) > 2000:
                ceviri = await get_long_text_translation(content, dest_lang)
            else:
                ceviri = await get_translation(content, dest_lang)

        elif content_type == 'jpg' or content_type == 'jpeg' or content_type == 'png' or content_type == 'bmp':
            with open(file_path, 'rb') as file:
                image = Image.open(BytesIO(file.read()))
            ceviri = await translate_image(image, dest_lang)

        return ceviri
    except Exception as e:
        return f"Hata oluştu:{e}"

async def get_long_text_translation(text, dest_lang):

    text_parts = [text[i:i+1999] for i in range(0, len(text), 1999)]
    translations = []
    for part in text_parts:
        translation = await get_translation(part, dest_lang)
        translations.append(translation)
    return "\n".join(translations)

async def get_translation(text, dest_lang):
    try:
        translation = await translator.translate(text, dest_lang)
        return translation.text
    except Exception as e:
        return f"Hata oluştu: {e}"

def add_text_to_image(image, text):
    width, height = image.size
    draw = ImageDraw.Draw(image)
    font_size = 1
    while True:
        font = ImageFont.truetype("arial.ttf", font_size)
        text_width, text_height = draw.textsize(text, font)
        if text_width < width and text_height < height:
            break
        font_size += 1
    text_color = (255, 255, 255)
    x = (width - text_width) / 2
    y = (height - text_height) / 2
    draw.text((x, y), text, fill=text_color, font=font)
    return image

@bot.event
async def on_ready():
    print(f'{bot.user.name} is ready.')

@bot.command(name='translate', help='Verilen metni hedef dile çevirir. Örnek kullanım: !translate [hedef_dil] [metin]')
async def translate(ctx, dest_lang, *args):
    text = ' '.join(args)
    if (text, dest_lang) in ceviriler:
        await ctx.send(ceviriler[(text, dest_lang)])
        return
    await translate_attachments(ctx.message, dest_lang)
    ceviri = await get_translation(text, dest_lang)
    await ctx.send(ceviri)
    ceviriler[(text, dest_lang)] = ceviri

    if len(ceviri) > 2000:
        ceviri = await get_long_text_translation(text, dest_lang)
        await ctx.send(ceviri)
        ceviriler[(text, dest_lang)] = ceviri

    else:
        ceviri = await get_translation(text, dest_lang)
        await ctx.send(ceviri)
        ceviriler[(text, dest_lang)] = ceviri

bot.run('BOT_TOKEN')
