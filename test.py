from playerio import *
import discord
import asyncio
import datetime
import requests
import random
from discord.ext import commands
from keep_alive import keep_alive

bot = commands.Bot(command_prefix=['h', 'H'], description="Some Text")

def is_owner():
    def predicate(ctx):
        return ctx.message.author.id == 473693528262705173, 585606270061641728
    return commands.check(predicate)

@bot.event
async def on_ready():
  print(f"I'm online \nLogged in as {bot.user.name} \nID {bot.user.id}")
  import sqlite3 as db
  conn = db.connect('main.db')
  cursor = conn.cursor()
  while True:
    await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Activity(name="Helmet Heroes", type=3))
    await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Activity(name="MadNasty", type=2))
    await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Activity(name="Katie", type=2))
    await asyncio.sleep(5)
    await bot.change_presence(activity=discord.Activity(name="Kami", type=3))

import sqlite3 as db
conn = db.connect('main.db')
cursor = conn.cursor()

@bot.event
async def on_message(message):
  if 'hmisc CuzinX' in message.content:
    return
  elif 'hmisc Jarsu' in message.content:
    return
  elif 'hmisc MadNasty' in message.content:
    return
  await bot.process_commands(message)

@bot.command()
async def servers(ctx):
  try:
    embed = discord.Embed(title="Severs List")
    a = requests.get('http://www.helmet-heroes.com/includes/getTotal.php?898920.3714678395')
    await ctx.send(f"```{a.text}```")
  except Exception as err:
    b = str(err)
    await ctx.send(f"```{b}```")

@bot.command(name='online', help='Get the current number of player online.')
async def online(ctx):
  client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
  players_online = 0

  for room in client.list_rooms('MyCode'):
    players_online += room.players_online

  players = f'{players_online}\n'

  embed = discord.Embed(title = "Players Online", description = players, color=0xFF0000)
  await ctx.send(embed = embed)

@bot.command(name='skills', help='Get the skills of the given player.')
async def online(ctx, player: str):  
  client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
  skills = client.bigdb_load('skillsData', player)
  await ctx.send(f"```{skills}```")

@bot.command(name='pro', help='Get the proficency of the given player.')
async def pro(ctx, player: str):
  client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
  pro = client.bigdb_load('proficiencyTable', player)
  await ctx.send(f"```{pro}```")

@bot.command(name='lwinners', help='Get the winners of the lottery.')
async def lwinners(ctx):
  client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
  winners = client.bigdb_load('miscTable', 'lotteryWinners')
  await ctx.send(f"```{winners}```")

@bot.command(name='linfo', help='Get lottery info.')
async def linfo(ctx):
  client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
  info = client.bigdb_load('miscTable', 'lotteryInfo')
  await ctx.send(f"```{info}```")

#@bot.command(name='misc', hidden=True)
#@is_owner()
#async def misc(ctx, player: str):
  #client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
  #info = client.bigdb_load('pMiscTable', player)
  #await ctx.send(f"```{info}```")

#@misc.error
#async def misc_error(ctx, error):
  #if isinstance(error, commands.errors.CheckFailure):
    #await ctx.send("You can't execute this command")

@bot.command(name='payvault')
async def payvault(ctx, *, name:str):
  client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
  info = client.bigdb_load('payVaultItems', name)
  await ctx.send(f"```{info}```")

@bot.command(name='guild', help='')
async def guild(ctx, guild: str):
  client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
  info = client.bigdb_load('guildsData', guild)
  await ctx.send(f"```{info}```")

@bot.command(name='pet', help='')
async def pet(ctx, player: str):
  client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
  info = client.bigdb_load('petData', player)
  await ctx.send(f"```{info}```")


#cursor.execute('''CREATE TABLE MAIN
         #(ID INT PRIMARY KEY     NOT NULL,
         #NAME           TEXT    NOT NULL,
         #NUMBER         TEXT    NOT NULL,
         #RANK           TEXT    NOT NULL,
         #DIE            TEXT    NOT NULL,
         #AGE          INT);''')

@bot.command()
async def info(ctx, *, msg:str):
  try:
    client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
    lol = client.create_join_room('test', 'MyCode', True)
    a = (client.bigdb_load('PlayerObjects',"simple" + msg))
    embed = discord.Embed(title=f"{msg} Account's Info", color=0x7DFF33)
    embed.add_field(name='\u200b', value=f"``{a}``", inline=False)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f"Requested by {ctx.author.name}")
    #await ctx.send(embed=embed)
    await ctx.send(f"```{a}```")
    #await ctx.send(f"```{a}```")
  except Exception as err:
    b = str(err)
    await ctx.send(f"```{b}```")

@info.error
async def info_error(ctx, error):
  if isinstance(error, commands.MissingRequiredArgument):
    client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
    lol = client.create_join_room('test', 'MyCode', True)
    cursor.execute(f"SELECT NAME from MAIN where ID = {ctx.author.id}")
    data = cursor.fetchall()
    for row in data:
      name = row[0]
      a = (client.bigdb_load('PlayerObjects',"simple" + name))
      await ctx.send(f"``{a}``")

@bot.command(name='bank', help='')
async def binfo(ctx, player: str):
  client = Client('hello-world-f8wdei2ucusdudkhbayw9g', 'BeholdABot', 'test')
  info = client.bigdb_load('bankData', player)
  await ctx.send(f"```{info}```")

@bot.command()
async def name(ctx, *, msg:str):
  try:
      cursor.execute(f"INSERT INTO main (ID,NAME,NUMBER,RANK,DIE,AGE) \
      VALUES ('{ctx.author.id}', '{msg}', 'LOL', 'LOL', 'LOL', '17')");
      conn.commit()
      await ctx.send(f"You registered you acc in database as ``{msg}``, now if you will do ``hinfo`` without a name will display you acc's info")
  except Exception as err:
    a = str(err)
    await ctx.send(a)

@bot.command(name="s", hidden=True)
async def s(ctx, *, msg:str):
  channel = bot.get_channel(691301275085701183)
  await channel.send(msg)

@bot.command()
@is_owner()
async def ip(ctx, *, msg:str):
  a = ['142.158.54.51', '28.31.168.225','117.161.147.6','35.12.17.158','38.197.32.179','197.230.247.19','227.161.125.231','15.2.67.110','124.77.15.187','125.102.96.104']
  await ctx.send(random.choice(a))

@bot.event
async def on_disconnect():
  print('offline...')

keep_alive()
bot.run('NjcyNzgzMDgyODUxNTMyODUx.Xm-VlA._nRsiA1lOC47QVLiCsIAPzA1W-8')

#run = "pip3 install \"protobuf>=3.4.0,<3.7\" && pip3 install discord && pip3 install flask && pip3 install asyncio && pip3 install requests && pip3 install datetime && python3 test.py"