from email.mime import message
from re import M
from types import new_class
import discord
from discord.ext import commands
from bot_mantik import *
from Bot_A_settings import *
import os
from food_sorter import get_class
import random

# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# client (istemci) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi {bot.user}! I am a chatbot!')

@bot.command()
async def emoji(ctx):
    await ctx.send(emoji_olusturucu())

@bot.command()
async def _help(ctx):
    await ctx.send("Try these commands:$hello, $emoji, $password, $bye, $coolbot, $choose, $coin, $add, $roll, $repeat, $joined, $cool, $duck, $dog, $fox, $code_meme, $animal_meme, $image_sorter. Just a few commands really! Oh and also go to this link for a full instruction manual: xxx.xxxxxxxxxx.xxx")

@bot.command()
async def password(ctx, passs: int):
    await ctx.send(gen_pass(passs))

@bot.command()
async def bye(ctx):
    await ctx.send(":slight_smile:")

@bot.command()
async def coolbot(ctx):
    await ctx.send('Yes, the bot is cool.')

@bot.command()
async def choose(ctx, *choices: str):
    await ctx.send(random.choice(choices))

@bot.command()
async def coin(ctx):
    await ctx.send(yazi_tura())

@bot.command()
async def add(ctx, left: int, right: int):
    await ctx.send(left + right)

@bot.command()
async def roll(ctx, dice: str):
    try:
        rolls, limit = map(int, dice.split('+'))
    except Exception:
        await ctx.send('Format has to be in yournumber+yourothernumber!')
        return

    result = ', '.join(str(random.randint(1, limit)) for q in range(rolls))
    await ctx.send(result)

@bot.command()
async def repeat(ctx, times: int, content: str):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def joined(ctx, member: discord.Member):
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}') # type: ignore

@bot.group()
async def cool(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')

@bot.command()
async def duck(ctx):
    image_url1 = get_duck_image_url()
    await ctx.send(image_url1)

@bot.command()
async def dog(ctx):
    image_url2 = get_dog_image_url()
    await ctx.send(image_url2)

@bot.command()
async def fox(ctx):
    image_url3 = get_fox_image_url()
    await ctx.send(image_url3)

@bot.command()
async def code_meme(ctx):
    c=random.choice(os.listdir("images"))
    with open(f'images/{c}', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

@bot.command()
async def animal_meme(ctx):
    a=random.choice(os.listdir("imagesa"))
    with open(f'imagesa/{a}', 'rb') as s:
        picture2 = discord.File(s)
        await ctx.send(file=picture2)

@bot.command()
async def image_sorter(ctx):
    model_path="keras_model.h5"
    labels_path="labels.txt"
    file_path="download.jpg"
    await ctx.send("İmage detection has begun.")
    if ctx.message.attachments:
        await ctx.send("An image has been found.")
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f"images/{file_name}"
            await attachment.save(file_path)
            await ctx.send("The image is saved.")
            class_name, score = get_class(model_path, labels_path, file_path)
            await ctx.send(f"I am pretty sure that this is a {class_name}" )
            await ctx.send(f"I am also {int(score*100)}% sure of that.")
    else:
        await ctx.send("Please upload a picture with the command.")

@bot.command()
async def nature(ctx):
    await ctx.send("To save nature we must stop global warming.")
    await ctx.send("For that we must:")
    with open("nature bot/recycle1.jpg", "rb") as a:
        r1=discord.File(a)
    with open("nature bot/recycle1.jpg", "rb") as b:
        r2=discord.File(b)

@bot.command()
async def game(ctx, guess_number):
    try:
        await ctx.send("Guess the number between 1 and 10.")
        number = random.randint(1, 10)
        if guess_number == number:
            await ctx.send("You guessed right! The number was", number,"!")
        else:
            await ctx.send("Sorry. The number was", number,". You'll guess next time.")
    except:
        await ctx.send("It has to be like this: $game yournumber")

bot.run(TOKEN)