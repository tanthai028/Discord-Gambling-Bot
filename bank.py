
@client.command()
async def withdraw(ctx):
    walletAmt = users[str(user.id)]["wallet"]
    bankAmt = users[str(user.id)]["bank"]
    users[str(user.id)]["wallet"] += bankAmt
    users[str(user.id)]["bank"] -= bankAmt
    

@client.command()
async def deposit(ctx):
    walletAmt = users[str(user.id)]["wallet"]
    bankAmt = users[str(user.id)]["bank"]
    users[str(user.id)]["bank"] += walletAmt
    users[str(user.id)]["wallet"] -= walletAmt



@client.command()
async def angy(ctx):
    x = emojize(":angry:")
    await ctx.send(f"Ready {x}")
    


@client.command()
async def shop(ctx):
    emoji = discord.utils.get(client.emojis, name='chaosorb')
    
    await ctx.send(f'''
Buy an item with the buy-item [quantity] <name> command.
For more information on an item use the item-info <name> command.

{emoji}1 - Rain of Chaos
''')
