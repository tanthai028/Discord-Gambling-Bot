import discord
from discord.ext import commands
import json
import os
import random
import emoji
from emoji import emojize

os.chdir("C:\\Users\\tanth\\OneDrive\\Desktop\\Discord Bot")

client = commands.Bot(command_prefix = '!')

@client.command()
async def bal(ctx):
    await openAccount(ctx.author)
    users = await getBankData()
    user = ctx.author

    walletAmt = users[str(user.id)]["wallet"]
    bankAmt = users[str(user.id)]["bank"]
    networthAmt = users[str(user.id)]["networth"]
    
    em = discord.Embed(title = f"{ctx.author.name}'s balance", color = discord.Color.blue())
    em.add_field(name = "Cash:", value = walletAmt)
    em.add_field(name = "Bank:", value = bankAmt)
    em.add_field(name = "Networth:", value = networthAmt)
    await ctx.send(embed = em)
        
@client.command()
async def work(ctx):
    await openAccount(ctx.author)

    users = await getBankData()

    user = ctx.author

    earnings = random.randrange(101)

    await ctx.send(f"You were given {earnings} dollars!")

    users[str(user.id)]["wallet"] += earnings

    walletAmt = users[str(user.id)]["wallet"]
    bankAmt = users[str(user.id)]["bank"]
    users[str(user.id)]["networth"] = walletAmt + bankAmt

    with open("mainbank.json", "w") as f:
        json.dump(users,f)

async def openAccount(user):
    users = await getBankData()

    # check if account exists
    if str(user.id) in users:
            return False
    # open account
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
        users[str(user.id)]["networth"] = 0

    with open("mainbank.json", "w") as f:
        json.dump(users, f)

    return True

async def getBankData():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

    return users

# ----------------------------------------------

@client.event
async def on_ready():
    print("Ready")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
async def emoji(ctx):
    emoji = 
    await ctx.send()

client.run("NzUyNjQ0NDYwODgxMzc5NDQ4.X1aoxg.043MLqbF-cRmBqg4SaqLGep2hmw")
