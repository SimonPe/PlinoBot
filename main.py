import discord
from discord.ext import commands
import random
import youtube_dl


bot = commands.Bot(command_prefix="*", description="Bot Utiitaire !")
funFact = [
    "L'eau mouille", "Le feu brule",
    "Lorsque vous volez, vous ne touchez pas le sol", "Winter is coming",
    "Mon créateur est Furio360",
    "Il n'est pas possible d'aller dans l'espace en restant sur terre",
    "La terre est ronde", "La moitié de 2 est 1", "7 est un nombre heureux",
    "Les allemands viennent d'allemagne",
    "Le coronavirus est un virus se répandant en Europe, en avez vous entendu parler ?",
    "J'apparais 2 fois dans l'année, a la fin du matin et au début de la nuit, qui suis-je ?",
    "Le plus grand complot de l'humanité est", "Pourquoi lisez vous ca ?"
]


@bot.event
async def on_ready():
    print("Ready !")


@bot.command()
async def Help(ctx):
    embed = discord.Embed(title="Menu Help",
                          description="Voici les commandes:",
                          url="https://discord.com/",
                          color=0xfa8072)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/860894908671066113/9d25f4fc672ca54f8ea7a4311df80f42.png?siz%22"
    )
    embed.add_field(name="Help1: Commandes Admin",
                    value=ctx.author.name,
                    inline=False)
    embed.add_field(name="Help2: Commandes Utilitaires",
                    value=ctx.author.name,
                    inline=False)
    embed.add_field(name="Help3: Parler avec le bot",
                    value=ctx.author.name,
                    inline=False)
    embed.set_footer(text=random.choice(funFact))


    await ctx.send(embed=embed)
    

@bot.command()
async def ban(ctx,
              user: discord.User,
              *,
              reason="Aucune raison n'a été donné"):
    await ctx.guild.ban(user, reason=reason)
    embed = discord.Embed(title="Banissement",
                          description="Un modérateur a frappé !",
                          url="https://discord.com",
                          color=0xfa8072)
    embed.set_author(name=ctx.author.name,
                     icon_url=ctx.author.avatar_url,
                     url="https://discord.com")
    embed.set_thumbnail(
        url="https://discordemoji.com/assets/emoji/BanneHammer.png")
    embed.add_field(name="Membre banni", value=user.name, inline=True)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.add_field(name="Modérateur", value=ctx.author.name, inline=True)
    embed.set_footer(text=random.choice(funFact))

    await ctx.send(embed=embed)
  
@bot.command()
async def kick(ctx,
               user: discord.User,
               *,
               reason="Aucune raison n'a été donné"):
    await ctx.guild.kick(user, reason=reason)
    embed = discord.Embed(title="Kick",
                          description="Un modérateur a frappé !",
                          url="https://discord.com",
                          color=0xfa8072)
    embed.set_author(name=ctx.author.name,
                     icon_url=ctx.author.avatar_url,
                     url="https://discord.com")
    embed.set_thumbnail(
        url="https://discordemoji.com/assets/emoji/BanneHammer.png")
    embed.add_field(name="Membre kick", value=user.name, inline=True)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.add_field(name="Modérateur", value=ctx.author.name, inline=True)
    embed.set_footer(text=random.choice(funFact))

    await ctx.send(embed=embed)
 

@bot.command()
async def Clear(ctx, nombre: int):
    messages = await ctx.channel.history(limit=nombre + 1).flatten()
    for message in messages:
        await message.delete()

@bot.command()
async def serveurinfo(ctx):
    server = ctx.guild
    numberOfTextChannels = len(server.text_channels)
    numberOfVoiceChannels = len(server.voice_channels)
    serverDescription = server.description
    numberOfPerson = server.member_count
    serverName = server.name
    message = f"Le serveur **{serverName}** contient *{numberOfPerson}* personnes ! \nLa description du serveur est {serverDescription}. Ce serveur possède {numberOfTextChannels} salons écrit et {numberOfVoiceChannels} salon vocaux."
    await ctx.send(message)
   

@bot.command()
async def Salut(ctx):
    await ctx.send("Salut ! ça va ?")

@bot.command()
async def Help1(ctx):
    embed = discord.Embed(title="Menu Help",
                          description="Voici les commandes:",
                          url="https://discord.com/",
                          color=0xfa8072)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/860894908671066113/9d25f4fc672ca54f8ea7a4311df80f42.png?siz%22"
    )
    embed.add_field(name="Ban <user> <raison>: Pour ban",
                    value=ctx.author.name,
                    inline=False)
    embed.add_field(name="Kick <user> <raison>: Pour kick",
                    value=ctx.author.name,
                    inline=False)
    embed.add_field(name="Clear <nombres>: Pour clear les messages",
                    value=ctx.author.name,
                    inline=False)
    embed.set_footer(text=random.choice(funFact))

    await ctx.send(embed=embed)

 

@bot.command()
async def Help2(ctx):
    embed = discord.Embed(title="Menu Help",
                          description="Voici les commandes:",
                          url="https://discord.com/",
                          color=0xfa8072)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/860894908671066113/9d25f4fc672ca54f8ea7a4311df80f42.png?siz%22"
    )
  
    embed.add_field(name="serverinfo: Pour avoir des info sur le serveur",
                    value=ctx.author.name,
                    inline=False)
    embed.add_field(name="Funfact: Pour avoir une Funfact",
                    value=ctx.author.name,
                    inline=False)
    embed.add_field(name="Run: Pour s'avoir si le bot est en ligne",
                    value=ctx.author.name,
                    inline=False)
    embed.add_field(name="Suggestion <On-veux-plus-de-frite-a-la-cantine> (tout sa sans espace)",
                    value=ctx.author.name,
                    inline=False)    
    embed.set_footer(text=random.choice(funFact))

    await ctx.send(embed=embed)
  
@bot.command()
async def Funfact(ctx):
    await ctx.send(random.choice(funFact))


@bot.command()
async def Help3(ctx):
    embed = discord.Embed(title="Menu Help",
                          description="Voici les commandes:",
                          url="https://discord.com/",
                          color=0xfa8072)
    embed.set_thumbnail(
        url=
        "https://cdn.discordapp.com/avatars/860894908671066113/9d25f4fc672ca54f8ea7a4311df80f42.png?siz%22"
    )
    embed.add_field(name="Salut: Pour lui dire Coucou",
                    value=ctx.author.name,
                    inline=False)
    embed.add_field(name="OuiEttoi: Pour répondre",
                    value=ctx.author.name,
                    inline=True)
    embed.add_field(name="tg: Pour faire tère le bot",
                    value=ctx.author.name,
                    inline=False)
    embed.add_field(name="jtm: Pour dire au bot que tu l'aime",
                    value=ctx.author.name,
                    inline=False)
    embed.set_footer(text=random.choice(funFact))

    await ctx.send(embed=embed)
   

@bot.command()
async def tg(ctx):
    await ctx.send("Ok je vait me tère :sob: ")
   

@bot.command()
async def Ouiettoi(ctx):
    await ctx.send(
        "Nickel ! et encore plus si vous m'invitez sur votre serveur avec le lien dans #annonce"
    )
  
@bot.command()
async def Run(ctx):
    await ctx.send("Oui je suis bien en ligne")
 
@bot.command()
async def jtm (ctx):
    await ctx.send("Moi aussi Baby ")

@bot.command()
async def Suggestion(ctx,
               reason="Aucune raison n'a été donné"):
    embed = discord.Embed(title="Menu de Suggestion",
                          url="https://discord.com",
                          color=0xfa8072)
    embed.set_author(name=ctx.author.name,
                     icon_url=ctx.author.avatar_url,
                     url="https://discord.com")
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/860894908671066113/9d25f4fc672ca54f8ea7a4311df80f42.png?siz%22")
    embed.add_field(name="Votre Suggestion:", value=reason, inline=False)
    embed.add_field(name="Merci de ne pas mettre d'espace",value=ctx.author.name, inline=False)
    print ("Suggestion ! (serveurinfo)")

    await ctx.send(embed=embed)

@bot.command()
async def TestE(ctx):
    embed = discord.Embed(title="Menu Help",
                          description="Voici les commandes:",
                          url="https://discord.com/",
                          color=0xfa8072)
              
bot.run("ODYwODk0OTA4NjcxMDY2MTEz.YOB43A.hh3eOaxvxnLQc39NS5_coYfJJuY")
