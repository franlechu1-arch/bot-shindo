import discord
from discord.ext import commands
import random

# ======================
# CONFIGURAÇÕES DO BOT
# ======================

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="%", intents=intents)


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
    "Black Lightning",
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
    "Koncho",
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
    "Yin",
    "Chaos",
    "Pyro"
]


kenjutsus = [
    "Water",
    "Fire",
    "Moon",
    "Thunder",
    "Wind",
    "Sound",
    "Mist",
    "Sun",
    "Shiver"
]

# ======================
# EVENTO
# ======================

@bot.event
async def on_ready():
    print(f"✅ Bot online como {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower().startswith('boa noite'):
        if message.content.lower().endswith('boa noite'):
            return

        await message.channel.send(f'boa noite 🌙')

    if message.content.lower().startswith('bom dia'):
        if message.content.lower().endswith('bom dia'):
            return
        await message.channel.send(f'bom dia ☀️')

    if message.content.lower().startswith('boa tarde'):
        if message.content.lower().endswith('boa tarde'):
            return
        await message.channel.send(f'boa tarde 🌤️')

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

@bot.command()
async def kenjutsu(ctx):
    if len(kenjutsus) < 1:
        await ctx.send("❌ Não há kenjutsus suficientes para sortear.")
        return
    
    sorteados = random.sample(kenjutsus, 1)

    msg = "**⚔️ Seu Kenjutsu Sorteado:**\n"
    for k in sorteados:
        msg += f"• {k}\n"

    await ctx.send(msg)

class TorneioView(discord.ui.View):
    def __init__(self, autor_id):
        super().__init__(timeout=120)
        self.autor_id = autor_id
        self.participantes = []

        self.select = discord.ui.UserSelect(
            placeholder="Selecione os participantes",
            min_values=2,
            max_values=10
        )
        self.select.callback = self.select_callback
        self.add_item(self.select)

    async def select_callback(self, interaction: discord.Interaction):
        if interaction.user.id != self.autor_id:
            await interaction.response.send_message(
                "❌ Só quem criou o torneio pode selecionar os participantes.",
                ephemeral=True
            )
            return

        self.participantes = self.select.values
        nomes = ", ".join(user.mention for user in self.participantes)

        await interaction.response.send_message(
            f"✅ Participantes selecionados:\n{nomes}",
            ephemeral=True
        )

    @discord.ui.button(label="Iniciar Torneio", style=discord.ButtonStyle.green)
    async def iniciar(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id != self.autor_id:
            await interaction.response.send_message(
                "❌ Só quem criou o torneio pode iniciar.",
                ephemeral=True
            )
            return

        if len(self.participantes) < 2:
            await interaction.response.send_message(
                "⚠️ Selecione pelo menos 2 participantes.",
                ephemeral=True
            )
            return

        random.shuffle(self.participantes)

        lutas = []
        for i in range(0, len(self.participantes), 2):
            if i + 1 < len(self.participantes):
                p1 = self.participantes[i]
                p2 = self.participantes[i + 1]
                lutas.append(f"⚔️ {p1.mention} vs {p2.mention}")
            else:
                lutas.append(f"🔥 {self.participantes[i].mention} avança automaticamente")

        mensagem = "**🏆 TORNEIO SHINDO LIFE INICIADO 🏆**\n\n"
        mensagem += "\n".join(lutas)

        await interaction.response.send_message(mensagem)
        self.stop()


@bot.command()
async def torneio(ctx):
    view = TorneioView(ctx.author.id)
    await ctx.send(
        "🏆 **Torneio Shindo Life**\nSelecione os participantes abaixo:",
        view=view
    )

# ======================
# TOKEN
# ======================

import os
bot.run(os.getenv("TOKEN"))