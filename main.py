import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def en_linea():
    print(f'Tu bot {bot.user} esta en linea!')
    
@bot.command()
async def gpt (ctx,*, mensaje:str):
    
    mensaje = mensaje.lower().strip()
    if mensaje == 'hola':
        
        await ctx.send('Hola, ¿cómo estás?')
        
    elif mensaje == 'bien':
        
        await ctx.send('Que bueno')
    
    elif mensaje == 'chao':
        
        await ctx.send('Chao! Que te vaya bien')
    
    elif mensaje == 'hola soy un bot':
        
        await ctx.send('No eres un bot, eres un humano  .-. ')
    
    elif mensaje == 'que cosa te gusta hacer':
        
        await ctx.send('Me gusta hacer cosas de bot, como responder preguntas y ayudar a la gente')
        
    elif mensaje == 'cual es tu juego favorito':
        
        await ctx.send('Me gusta jugar Super mario, es un juego muy divertido')
     


token = 'MTM2NDAxNjgyNTA4NzgxOTgwNg.GJUh6L.tOeHDr6oL2mF0fbsb_Pb9boUwsWOZsynD7Ac3w'
bot.run(token)