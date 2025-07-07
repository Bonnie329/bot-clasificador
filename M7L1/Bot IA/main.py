import discord
from discord.ext import commands
import os, random
import requests

from modelo import *
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ia(ctx):
    if ctx.message.attachments:
        for archivo in ctx.message.attachments:
            nombre_archivo = archivo.filename
            url_archivo = archivo.url
            await archivo.save(f"./img/{nombre_archivo}")
            await ctx.send(f"su imagen se guardo en: ./img/{nombre_archivo}")
            class_name, confidence_score = get_class(f"./img/{nombre_archivo}")
            respuesta = f"**prediccion:** {class_name}\n**confianza**{confidence_score: 2f}"
            await ctx.send(respuesta)
    else:
        await ctx.send("no ingreso ninguna imagen")

# Intents necesarios para que funcione correctamente
intents = discord.Intents.default()
intents.message_content = True

# Lista de recomendaciones alimenticias
recomendaciones = [
    "🍎 Come al menos 5 porciones de frutas y verduras al día.",
    "💧 Bebe suficiente agua, mínimo 8 vasos diarios.",
    "🍚 Elige cereales integrales en lugar de refinados.",
    "🍗 Incluye proteínas magras como pollo, pescado o legumbres.",
    "🚫 Evita el exceso de azúcares y alimentos ultraprocesados.",
    "🥛 Consume productos lácteos bajos en grasa o sus alternativas.",
    "🥗 No te saltes el desayuno: debe ser equilibrado.",
    "🧂 Reduce el consumo de sal para cuidar tu presión arterial.",
    "🕒 Come a horarios regulares y no te saltes comidas.",
    "🏃‍♂️ Combina una buena alimentación con ejercicio diario."
]

# Comando para pedir una recomendación
@bot.command(name='recomienda')
async def recomienda(ctx):
    recomendacion = random.choice(recomendaciones)
    await ctx.send(f"🥗 Recomendación saludable:\n{recomendacion}")

bot.run("")