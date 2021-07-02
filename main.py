import datetime
import aiohttp
import requests
import random
import asyncio
from threading import Thread
from discord.ext.commands import Bot
from urllib.request import urlopen
from urllib.request import Request, urlopen
from discord.voice_client import VoiceClient
from discord.ext import commands
import discord
import json
import os
import psutil
import sys
import time

infractions = {}
limit = 20

prefix = ["$"]

TOKEN = os.getenv("DISCORD_TOKEN")

start_time = datetime.datetime.utcnow()

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive=True)
bot.remove_command("help")

bot.anti = True

async def status_task():
    while True:
        activity = discord.Game(name=f" with {len(set(bot.get_all_members()))} members", type=3)
        await bot.change_presence(status=discord.Status.dnd, activity=activity)
        await asyncio.sleep(10)
        activity = discord.Game(name=f".gg/wet | $help", type=3)
        await bot.change_presence(status=discord.Status.dnd, activity=activity)
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print("Bot is ready.")
    ...
    bot.loop.create_task(status_task())


@bot.command(description="antiraid")
@commands.has_permissions(ban_members=True)
async def antiraid(ctx):
    if bot.antiraid is False:
        bot.antiraid = True
        await ctx.send("Antiraid has now been turned on")
        return
    if bot.antiraid is True:
        bot.antiraid = False
        await ctx.send("Antiraid has now been turned off")
        return

@bot.event
async def on_message(message: discord.Message):
    channel = bot.get_channel(829103469435682836)
    if message.guild is None and not message.author.bot:
        if "/" in message.content:
            return
        if "http" in message.content:
            return
        if ".gg" in message.content:
            return
        embed = discord.Embed(title=f"{message.content}", description=f"Sent by {message.author} or {message.author.id}", color=0x2f3136)
        await channel.send(embed=embed)
    await bot.process_commands(message)
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(description="The help command.")
async def help(ctx, c: str=None):
    if not c:
        await ctx.message.delete()
        embed = discord.Embed(title='**Help**', description=f'welcome to th♡ts bot', color=0x2f3136)
        embed.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/811467176690974721/845409919691391006/original_19.jpg")
        embed.add_field(name='**Fun Commands**', value=f'$help fun', inline=False)
        embed.add_field(name='**Mod commands**', value=f'$help mod', inline=False)
        embed.add_field(name='**Utility Commands**', value=f'$help util', inline=False)
        embed.set_footer(text=f"Command prefix is \"$ \" | discord.gg/wet")
        await ctx.send(embed=embed)
    elif c.lower() == 'fun':
        await ctx.message.delete()
        embed1 = discord.Embed(title='**Fun Commands**', color=0x2f3136)
        embed1.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/811467176690974721/845409919691391006/original_19.jpg")
        embed1.add_field(name="**kiss**", value="Kisses mentioned user.", inline=False)
        embed1.add_field(name="**spank**", value="Spanks mentioned user.", inline=False)
        embed1.add_field(name="**hug**", value="Hugs mentioned user.", inline=False)
        embed1.add_field(name="**lick**", value="Licks mentioned user.", inline=False)
        embed1.add_field(name="**cuddle**", value="Cuddles mentioned user.", inline=False)
        embed1.add_field(name="**cat**", value="Cute kitten pics.", inline=False)
        embed1.add_field(name="**tickle**", value="Tickles the mentioned user.", inline=False)
        embed1.add_field(name="**slap**", value="Slaps mentioned user.", inline=False)
        embed1.add_field(name="**nsfw**", value="Shows a picture from r/nsfw.", inline=False)
        embed1.add_field(name="**pussy**", value="Pussy pics hehe.", inline=False)
        embed1.add_field(name="**boobs**", value="BOOBIES!.", inline=False)
        embed1.add_field(name="**fuck**", value="Fucks mentioned user.", inline=False)
        embed1.add_field(name="**dick**", value="Dick size.", inline=False)
        embed1.add_field(name="**tweet**", value="Generated a tweet.", inline=False)
        embed1.add_field(name="**ph**", value="PH [name] [text] will generate a pornhub comment.", inline=False)
        embed1.set_footer(text=f"Command prefix is \"$ \" | discord.gg/wet")
        await ctx.send(embed=embed1)
    elif c.lower() == 'util':
        await ctx.message.delete()
        embed4 = discord.Embed(title='**Utility Commands**', color=0x2f3136)
        embed4.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/811467176690974721/845409919691391006/original_19.jpg")
        embed4.add_field(name="**ping**", value="[ip/host] pings a ip or host.", inline=False)
        embed4.add_field(name="**btc**", value="Shows current btc price.", inline=False)
        embed4.add_field(name='**whois**', value='Gets invo on the mentioned user.', inline=False)
        embed4.add_field(name='**geoip**', value='Looks up the given ip address.', inline=False)
        embed4.add_field(name="**av**", value="Gets the pfp of the mentioned user.", inline=False)
        embed4.add_field(name="**poll**", value="Generates a poll for users to do.", inline=False)
        embed4.add_field(name="**guildinfo**", value="Information about the guild", inline=False)
        embed4.add_field(name="**roblox**", value="[roblox-name] shows the persons roblox character.", inline=False)
        embed4.add_field(name="**snipe**", value="Snipes the previous deleted message.", inline=False)
        embed4.add_field(name="**help**", value="Shows all commands.", inline=False)
        embed4.set_footer(text=f"Command prefix is \"$ \" | discord.gg/wet")
        await ctx.send(embed=embed4)
    elif c.lower() == 'mod':
        await ctx.message.delete()
        embed5 = discord.Embed(title='**Utility Commands**', color=0x2f3136)
        embed5.set_thumbnail(
            url="https://cdn.discordapp.com/attachments/811467176690974721/845409919691391006/original_19.jpg")
        embed5.add_field(name="**ban**", value="Bans mentioned user.", inline=False)
        embed5.add_field(name="**unban**", value="Unbans mentioned user.", inline=False)
        embed5.add_field(name="**unbanall**", value="Mass unbans all users.", inline=False)
        embed5.add_field(name="**kick**", value="Kicks mentioned user.", inline=False)
        embed5.add_field(name="**mute**", value="Mutes mentioned user.", inline=False)
        embed5.add_field(name="**unmute**", value="Unmutes mentioned user.", inline=False)
        embed5.add_field(name="**lock**", value="Locks the channel.", inline=False)
        embed5.add_field(name="**antiraid**", value="Stops new members from verifing.", inline=False)
        embed5.add_field(name="**unlock**", value="Unlocks the channel.", inline=False)
        embed5.add_field(name="**purge**", value="Purges amount of messages.", inline=False)
        embed5.add_field(name="**slow**", value="adds slow mode to the channel.", inline=False)
        embed5.add_field(name="**role**", value="roles a user.", inline=False)
        embed5.add_field(name="**roleall**", value="gives a role to all members.", inline=False)
        embed5.set_footer(text=f"Command prefix is \"$ \" | discord.gg/wet")
        await ctx.send(embed=embed5)
    else:
        pass


snipe_message_author = {}
snipe_message_content = {}


@bot.event
async def on_message_delete(message):
    snipe_message_author[message.channel.id] = message.author
    snipe_message_content[message.channel.id] = message.content


@bot.command(name='snipe')
async def snipe(ctx):
    channel = ctx.channel
    try:  # This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name=f"Last deleted message in #{channel.name}",
                           description=snipe_message_content[channel.id], color=0x2f3136)
        em.set_footer(text=f"This message was sent by {snipe_message_author[channel.id]}")
        await ctx.send(embed=em)
    except:  # This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send(f"There are no recently deleted messages in #{channel.name}")


@bot.command()
async def status(ctx, *, value):
    if ctx.message.author.id == 343700313942786048:
        activity = discord.Game(name=f"{value}", type=3)
        await bot.change_presence(status=discord.Status.dnd, activity=activity)
        embed = discord.Embed(title=f"Bots status has been changed to {value}", description=f"", color=0xff3487)
        await ctx.send(embed=embed)
        await bot.process_commands(message)
    else:
        await ctx.send(f"ha lol kys nice try")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"This command is on cooldown you can use it in {round(error.retry_after, 2)} seconds")


@bot.command()
@commands.has_permissions(manage_channels=True)
async def close(ctx: commands.Context):
    await ctx.channel.delete()

@bot.command()
async def supportdm(ctx, *, value):
    channel = bot.get_channel(343700313942786048)
    await ctx.message.delete()
    embed = discord.Embed(title=f"{value}", description=f"Support request sent by {ctx.author.display_name} or  or {ctx.message.author.id}", color=0x2f3136)
    await channel.send(embed=embed)
    await bot.process_commands(message)

@bot.command()
@commands.has_permissions(ban_members=True)
async def tickets(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='**Support**', description=f'here is where you can open tickets', color=0x2f3136)
    embed.set_thumbnail(
        url="https://cdn.discordapp.com/avatars/804803763218284544/06432766189c9e4e556b0242a5827afd.png?size=2048")
    embed.add_field(name='**Support server**', value=f'discord.gg/th♡ts', inline=False)
    embed.add_field(name='**Open a ticket**', value=f'$ticket', inline=False)
    embed.set_footer(text=f"Command prefix is \"$\" | discord.gg/th♡ts")
    await ctx.send(embed=embed)


# MODERARTION BAN/KICK/MUTE

@bot.command()
@commands.has_permissions(manage_channels=True)
async def slow(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Slowmode in this channel has been set to {seconds} seconds!")


@bot.command(name="toggle", description="Enable or disable a command!")
async def toggle(ctx, *, command):
    command = bot.get_command(command)
    if ctx.message.author.id == 343700313942786048:

        if command is None:
            await ctx.send("theres no commands called that")

        elif ctx.command == command:
            await ctx.send("You cannot disable this command.")

        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            await ctx.send(f"Command {command.qualified_name} has been {ternary}")


@bot.command(aliases=["quit"])
async def shutdown(ctx):
    if ctx.message.author.id == 343700313942786048:
        await ctx.send("Shutting down.")
        await bot.close()

@bot.command()
@commands.has_permissions(ban_members=True)
async def unbanall(ctx): # b'\xfc'
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    await ctx.send(f"Unbanned all users.")
    for users in banlist:
        try:
            await asyncio.sleep(1)
            await ctx.guild.unban(user=users.user)
        except:
            pass


@bot.command()
async def dm(ctx, user: discord.User, *, value):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{value}", description=f"Sent by {ctx.author.display_name}", color=0xff3487)
    await user.send(embed=embed)
    await ctx.send(f"DM has been sent", delete_after=3)
    

@bot.command()
async def anondm(ctx, user: discord.User, *, value):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{value}", description=f"discord.gg/wet", color=0xff3487)
    await user.send(embed=embed)
    await ctx.send(f"DM has been sent", delete_after=3)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx):
    embed = discord.Embed(
        title=f"**The channel has been nuked.**", color=0xfffafa,
    )
    embed.set_image(url='https://gifimage.net/wp-content/uploads/2017/10/nuclear-explosion-animated-gif-1.gif')
    embed.set_footer(text=f"Nuked by: {ctx.author.name}#{ctx.author.discriminator}")
    pos = ctx.channel.position
    await ctx.channel.delete()
    channel = await ctx.channel.clone()
    await channel.edit(position=pos)
    await channel.send(embed=embed)


@bot.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False, view_channel=False)
    await ctx.send(ctx.channel.mention + " is now in lockdown.")


@bot.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True, view_channel=False)
    await ctx.send(ctx.channel.mention + " has been unlocked.")


@bot.command(description="Bans a member")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    embed = discord.Embed(title=f'**{member} was banned from wet**', color=0xff3487)
    embed.add_field(name='**Moderator**', value=f'{ctx.author.name}#{ctx.author.discriminator}', inline=False)
    embed.add_field(name='**Reason**', value=f'{reason}', inline=False)
    embed.set_image(url='https://cdn.discordapp.com/attachments/843728699165114388/843855420148809759/ilovekylie.gif')
    await member.ban(reason=f"{reason} by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.send(embed=embed)


@bot.command(description="Kicks a member")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    embed = discord.Embed(title=f'**{member} was kicked from wet**', color=0xfffafa)
    embed.add_field(name='**Moderator**', value=f'{ctx.author.name}#{ctx.author.discriminator}', inline=False)
    embed.add_field(name='**Reason**', value=f'{reason}', inline=False)
    embed.set_image(url='https://c.tenor.com/2e8AooY21ZIAAAAM/sao-liz.gif')
    await member.kick(reason=f"{reason} by {ctx.author.name}#{ctx.author.discriminator}")
    await ctx.send(embed=embed)


@bot.command(description="Unbans a member")
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    bannedUsers = await ctx.guild.bans()
    name, discriminator = member.split("#")

    for ban in bannedUsers:
        user = ban.user

        if (user.name, user.discriminator) == (name, discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} was unbanned.")
            return


@bot.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True,
                                          read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"you got muted {member.mention} {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")


@bot.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")


@bot.command(pass_context=True)
@commands.has_permissions(manage_channels=True)
async def purge(ctx, limit: int):
    await ctx.channel.purge(limit=limit)
    await ctx.send('Purged by {}'.format(ctx.author.mention))
    await ctx.message.delete()

@bot.command(description="gives a member a role")
@commands.has_permissions(administrator=True)
async def role(ctx, member: discord.Member, role: discord.Role):
    await member.add_roles(role)
    await ctx.send(f"The role ''**{role}**'' has been given to {member.mention}")

@bot.command(description="ddd")
@commands.has_permissions(administrator=True)
async def roleall(ctx, role: discord.Role):
    await ctx.send(f"Giving ''**{role}**'' to all members")
    for user in ctx.guild.members:
        if role not in user.roles:
            try:
                await user.add_roles(role)
            except:
                pass
    

@bot.command(description="dmall")
async def dmall(ctx, *, message):
    if ctx.message.author.id == 343700313942786048:
        await ctx.send(f"dming all members ")
        for user in ctx.guild.members:
            try:
                print("dm sent")
                await user.send(f"{message}")
            except:
                pass


# COMMANDS


@bot.command(aliases=['dong', 'penis'])
async def dick(ctx, *, user: discord.Member = None): # b'\xfc'
    await ctx.message.delete()
    if user is None:
        user = ctx.author
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong = "="
    em = discord.Embed(title=f"{user}'s Dick size", description=f"8{dong}D", colour=0x2f3136)
    await ctx.send(embed=em)


@bot.command(aliases=['bit'])
async def btc(ctx):
    await ctx.message.delete()
    r = requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP')
    r = r.json()
    usd = r['USD']
    eur = r['EUR']
    gbp = r['GBP']
    embed = discord.Embed(title='**BTC**', color=0xFFFAFA)
    embed.add_field(name="**USD**", value=usd)
    embed.add_field(name="**EUR**", value=eur)
    embed.add_field(name="**GBP**", value=gbp)
    await ctx.send(embed=embed)


@bot.command()
async def hug(ctx, member : discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/hug")
    embed = discord.Embed(description=f"hugs {member.mention}", color=0xFFFAFA)
    embed.set_image(url=r.json()['url'])
    await ctx.send(embed=embed)


@bot.command()
async def boobs(ctx, member : discord.Member=None):
    if ctx.channel.is_nsfw():
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/boobs")
        embed = discord.Embed(color=0xFFFAFA)
        embed.set_image(url=r.json()['url'])
        await ctx.send(embed=embed)
    if not ctx.channel.is_nsfw():
        await ctx.send("This is not a NSFW channel.")


@bot.command()
async def spank(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/spank').json()
    embed = discord.Embed(description=f"spanks {member.mention}", color=0xFFFAFA)
    embed.set_image(url=r['url'])
    await ctx.send(embed=embed)


@bot.command()
async def fuck(ctx, member: discord.Member=None):
    if ctx.channel.is_nsfw():
        await ctx.message.delete()
        r = requests.get('https://api.neko-chxn.xyz/v1/fuck/img').json()
        embed = discord.Embed(description=f'fucks {member.mention}', color=0xFFFAFA)
        embed.set_image(url=r["url"])
        await ctx.send(embed=embed)
    if not ctx.channel.is_nsfw():
        await ctx.send("This is not a NSFW channel.")

@bot.command()
async def antinuke(ctx):
    if ctx.message.author.id == 746876511805505637:
        if bot.anti is False:
            bot.anti = True
            await ctx.send("antinuke is now on")
            return
        if bot.anti is True:
            bot.anti = False
            await ctx.send("antinuke is now off")
            return

@bot.event
async def on_member_remove(member):
    if bot.anti is False:
        return
    try:
        guild = member.guild
        async for i in guild.audit_logs(limit = 1, action = discord.AuditLogAction.kick, after = datetime.datetime.utcnow() - datetime.timedelta(seconds = 10), oldest_first = False): # 10 to prevent join-kick-join-leave false-positives
            if i.created_at < datetime.datetime.utcnow() - datetime.timedelta(seconds = 10):
                print("kicked whithin 10s")
                continue
            id = i.user.id
            infractions[id] = infractions.get(id, 0) + 1
            print("warned")
            if infractions[id] >= limit:
                print("banned - " + i.user.name)
                await guild.ban(i.user, reason="User kicked - Anti-Nuke")
    except Exception as e:
        print(e)
        

@bot.event
async def on_member_ban(guild: discord.Guild, user: discord.user):
    if bot.anti is False:
        return
    try:
        async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
            id = i.user.id
            infractions[id] = infractions.get(id, 0) + 1
            if infractions[id] >= limit:
                print("banned - " + i.user.name)
                await guild.ban(i.user, reason="User banned - Anti-Nuke")
    except Exception as e:
        print(e)

@bot.event
async def on_member_join(member):
    if bot.anti is True and member.bot:
        try:
            guild = member.guild
            async for i in guild.audit_logs(limit=1, action=discord.AuditLogAction.bot_add):
                await guild.ban(member, reason="Bot added - Anti-Nuke")
        except Exception as e:
            print(e)

@bot.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *, message):
    if ctx.message.author.id == 547188560407691266:
            for i in range(amount):
                await ctx.send(message)

@bot.command()
async def tweet(ctx, username, *, message):
    await ctx.message.delete()
    r = requests.get(f'https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}').json()
    embed = discord.Embed(color=0xFFFAFA)
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed)


@bot.command()
async def cuddle(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://api.neko-chxn.xyz/v1/cuddle/img').json()
    embed = discord.Embed(description=f'cuddles {member.mention}', color=0xFFFAFA)
    embed.set_image(url=r["url"])
    await ctx.send(embed=embed)


@bot.command()
async def lick(ctx, member: discord.Member=None):
    await ctx.message.delete()
    r = requests.get('https://api.neko-chxn.xyz/v1/lick/img').json()
    embed = discord.Embed(description=f'licks {member.mention}', color=0xFFFAFA)
    embed.set_image(url=r["url"])
    await ctx.send(embed=embed)


@bot.command()
async def kiss(ctx, member: discord.Member = None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/kiss")
    embed = discord.Embed(description=f"kisses <@{member.id}>", color=0x2f3136)
    embed.set_image(url=r.json()['url'])
    await ctx.send(embed=embed)


@bot.command()
async def tickle(ctx, member: discord.Member = None):
    await ctx.message.delete()
    r = requests.get('https://nekos.life/api/v2/img/tickle').json()
    embed = discord.Embed(description=f"tickles {member.mention}", color=0x2f3136)
    embed.set_image(url=r['url'])
    await ctx.send(embed=embed)


@bot.command()
async def ph(ctx, user, *, message):
    await ctx.message.delete()
    r = requests.get(
        f'https://nekobot.xyz/api/imagegen?type=phcomment&text={message}&username={user}&image=https://i.imgur.com/raRKTgZ.jpg').json()
    embed = discord.Embed(color=0x2f3136)
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed)


@bot.command()
async def roblox(ctx, user):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{user}'s roblox avatar", color=0x2f3136)
    embed.set_image(url=f"http://www.roblox.com/Thumbs/Avatar.ashx?x=250&y=250&Format=Png&username={user}")
    await ctx.send(embed=embed)


@bot.command(aliases=['avatar'])
async def av(ctx, *, member: discord.Member = None):
    await ctx.message.delete()
    embed = discord.Embed(title=f"{member}'s avatar", color=0x2f3136)
    avatarurl = member.avatar_url
    embed.set_image(url=avatarurl)
    await ctx.send(embed=embed)


@bot.command(description="Gets the bot's latency.")
async def ping(ctx):
    latency = round(bot.latency * 1000, 1)
    await ctx.send(f"Pong! {latency}ms")


@purge.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("nigga you have no perms")


@bot.command()
async def nsfw(ctx):
    if ctx.channel.is_nsfw():
        embed = discord.Embed(title="Porn", description="your a horny cunt", color=0x2f3136)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/nsfw/new.json?sort=top') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
    if not ctx.channel.is_nsfw():
        await ctx.send("This is not a NSFW channel.")


@bot.command()
async def gay(ctx):
    if ctx.channel.is_nsfw():
        embed = discord.Embed(title="Gay", description="uwu xx", color=0x2f3136)
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/gayporn/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'][random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)
    if not ctx.channel.is_nsfw():
        await ctx.send("This is not a NSFW channel.")


@bot.command()
async def cat(ctx, member : discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/meow")
    embed = discord.Embed(color=0x2f3136)
    embed.set_image(url=r.json()['url'])
    await ctx.send(embed=embed)


@bot.command()
async def slap(ctx, user: discord.Member=None):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/slap")
    res = r.json()
    embed = discord.Embed(description=f"{bot.user.mention} slaps {user.mention}", color=0x2f3136)
    embed.set_image(url=res['url'])
    await ctx.send(embed=embed)


@bot.command(aliases=['porn'])
async def pussy(ctx):
    if ctx.channel.is_nsfw():
        await ctx.message.delete()
        r = requests.get("https://nekobot.xyz/api/image?type=pussy").json()
        embed = discord.Embed(color=0x2f3136)
        embed.set_image(url=str(r["message"]))
        await ctx.send(embed=embed)
    if not ctx.channel.is_nsfw():
        await ctx.send(f"This is not a NSFW channel.")


@bot.command()
async def poll(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(title="**Poll**", color=0x2f3136)
    embed.add_field(name=f"{message}", value="✅ ❌", inline=False)
    message = await ctx.send(embed=embed)
    await message.add_reaction("✅")
    await message.add_reaction("❌")


@bot.command(aliases=["whois"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=0x2f3136, timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.send(embed=embed)


@bot.command(aliases=['serverinfo'])
async def guildinfo(ctx):
    await ctx.message.delete()
    embed = discord.Embed(title='**Guild Info**', color=0xFFFAFA)
    guild = ctx.message.guild
    roles = [role.mention for role in reversed(guild.roles)]
    embed.add_field(name='**Owner**', value=f'<@{ctx.message.guild.owner_id}>', inline=False)
    embed.add_field(name='**Created At**', value=guild.created_at, inline=False)
    embed.add_field(name='**Amount of Roles**', value=len(guild.roles), inline=False)
    embed.add_field(name='**Amount of Members**', value=len(guild.members), inline=False)
    embed.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

bot.run("ODYwNjY1NTk2NzE4NDgxNDM4.YN-jTA.NBcmI6exuHZ4SggjIe_P8bwaK_Y")
