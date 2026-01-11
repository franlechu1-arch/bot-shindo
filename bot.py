import discord
from discord.ext import commands
import random

# ======================
# CONFIGURAÇÕES DO BOT
# ======================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="%", intents=intents)

# ======================
# LISTAS EDITÁVEIS
# ======================
# 👉 COLE AQUI TODAS AS GENKAIS

genkais = [
    "Odin Saberu",
    "Boil",
    "Akuma",
    "Bankai-Inferno",
    "Xeno Dokei",
    "Blood",
    "Explosion",
    "Light Jokei",
    "Saberu",
    "Arahaki-Jokei",
    "Jayramaki",
    "Tsunami",
    "Seishin",
    "Nectar",
    "Koncho",
    "Renshiki",
    "Pika Senko",
    "Vine",
    "Black Lightning    ",
    "Minakami",
    "Forged Rengoku",
    "Mecha Spirit",
    "Ryuji Kenichi",
    "Kerada",
    "Shindai Rengoku",
    "Azarashi",
    "Senko",
    "Shado",
    "Emerald",
    "Dio Senko",
    "Smoke",
    "Kenichi",
    "Ashen-Storm",
    "Ares-Koncho",
    "Narumaki",
    "Sengoku",
    "Clay",
    "Shindai Akuma",
    "Alphirama-Shizen",
    "Glacier",
    "Wanziame",
    "Typhoon",
    "Minakaze",
    "Raion Akuma",
    "Sound",
    "Menza",
    "Okami",
    "Satori Rengoku",
    "Mud",
    "Shizen",
    "Wood",
    "Storm",
    "Dust",
    "Rengoku",
    "Kokotsu",
    "Kagoku",
    "Sand",
    "Azim-Senko",
    "Eastwood Korashi",
    "Eternal",
    "Web",
    "Crystal",
    "Borumaki",
    "Frost",
    "Tengoku",
    "Kamaki",
    "Ghost Korashi",
    "Riser Akuma",
    "Scorch",
    "Shiro Glacier",
    "Inferno",
    "Sarachia Akuma",
    "Doku Tengoku",
    "Apollo-Sand",
    "Shiver Akuma",
    "Bankai-Akuma",
    "Giovanni Shizen",
    "Kaijin",
    "Ink",
    "Lava",
    "Dangan",
    "Hair",
    "Bolt",
    "Jokei",
    "Vanhelsing",
    "Bubble",
    "Aidens-Son-Mud",
    "Raion Rengoku",
    "Satori Akuma",
    "Paper",
    "Cobra",
    "Dokei",
    "Ice",
    "Gold Sand",
    "Rykan Shizen",
    "Magma",
    "Fizz",
    "Code Gaiden",
    "Kamaki Akuma",
    "Vengeance",
    "Strange",
    "Fume",
    "Sean Kerada",
    "Raion Gaiden",
    "Six Path Narumaki",
    "Borumaki Gaiden",
    "Raiden Saberu",
    "Getsuga",
    "Aizden",
    "Indra Akuma",
    "Snakeman",
    "Surge",
    "Tetsuo Kaijin",
    "Headless",
    "Kagoku",
    "Deva Rengoku",
    "Octo-Ink",
    "Ashura Shizen",
    "Jinshiki",
    "Ragnar",
    "Bruce Kenichi",
    "Powder",
    "Apol-Sand"
]

# 👉 COLE AQUI TODOS OS ELEMENTOS

elementos = [
    "Earth",
    "Fire",
    "Lightning",
    "Water",
    "Wind",
    "Shiver",
    "Combustion",
    "Gale",
    "Acid",
    "Cement",
    "Yin (Yang)",
    "Chaos",
    "Pyro"
]

# ======================
# EVENTO
# ======================

@bot.event
async def on_ready():
    print(f"✅ Bot online como {bot.user}")

# ======================
# COMANDOS
# ======================

@bot.command()
async def genkai(ctx):
    if len(genkais) < 4:
        await ctx.send("❌ Não há genkais suficientes para sortear.")
        return

    sorteadas = random.sample(genkais, 4)

    msg = "**🧬 Suas Genkais Sorteadas:**\n"
    for g in sorteadas:
        msg += f"• {g}\n"

    await ctx.send(msg)

@bot.command()
async def elemento(ctx):
    if len(elementos) < 4:
        await ctx.send("❌ Não há elementos suficientes para sortear.")
        return

    sorteados = random.sample(elementos, 4)

    msg = "**🌪️ Seus Elementos Sorteados:**\n"
    for e in sorteados:
        msg += f"• {e}\n"

    await ctx.send(msg)

# ======================
# TOKEN
# ======================

import os
bot.run(os.getenv("TOKEN"))