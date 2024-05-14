import discord
from discord.ext import commands

# Créer une instance du bot
bot = commands.Bot(command_prefix='!')

# Événement de démarrage du bot
@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

# Commande simple pour tester le bot
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')



# Créer un dictionnaire pour stocker l'inventaire de chaque utilisateur
inventories = {}

# Commande pour ajouter un objet à l'inventaire
@bot.command()
async def add(ctx, item):
    user_id = ctx.author.id
    if user_id not in inventories:
        inventories[user_id] = []
    inventories[user_id].append(item)
    await ctx.send(f"{item} ajouté à ton inventaire !")

# Commande pour afficher l'inventaire
@bot.command()
async def inventory(ctx):
    user_id = ctx.author.id
    if user_id not in inventories:
        await ctx.send("Ton inventaire est vide !")
    else:
        inventory_list = "\n".join(inventories[user_id])
        await ctx.send(f"Ton inventaire :\n{inventory_list}")

# Commande pour supprimer un objet de l'inventaire
@bot.command()
async def remove(ctx, item):
    user_id = ctx.author.id
    if user_id not in inventories or item not in inventories[user_id]:
        await ctx.send("Cet objet n'est pas dans ton inventaire !")
    else:
        inventories[user_id].remove(item)
        await ctx.send(f"{item} retiré de ton inventaire !")
        



# démarrage bot
bot.run('MTI0MDAwNzkxNjE3ODc3MjAxOQ.Gy3h7U.hiUiduG-HU2-9qF0jSIfcp0kKAOaSN62wt-KKk')

