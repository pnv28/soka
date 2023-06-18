import discord
from discord.ext import commands
import requests
from discord import Option
import anime_images_api
from discord.commands import SlashCommandGroup
anime = anime_images_api.Anime_Images()

color = discord.Color.from_rgb(255, 192, 203)


class Anime(commands.Cog):
    def __inti__(self, bot):
        self.bot = bot
    
    anime = SlashCommandGroup("anime", "commands related to anime")
    images = SlashCommandGroup("images", "Slap, Kill, Pat, etc. anime images")
    # @discord.slash_command(name="anime_quote", description="Fetches a random quote")
    @anime.command(description="Gives a random anime quote")
    async def random_quote(self, ctx):
        response = requests.get("https://kyoko.rei.my.id/api/quotes.php")
        quote = response.json()["apiResult"][0]["english"]
        author = response.json()["apiResult"][0]["character"]
        animeName = response.json()["apiResult"][0]["anime"]
        quoteEmbed = discord.Embed(
            title=f"Quote from {animeName}",
            description = f"```{quote} - {author}```",
            color = color

        )
        await ctx.respond(embed = quoteEmbed)
    
    @anime.command(description="Gives Information about specified anime")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def information(self, ctx, anime: Option(str, description="Name of the anime")):
        response = requests.get(f"https://kyoko.rei.my.id/api/myanimelist.php?q={anime}")
        data = response.json()["apiResult"]
        image = data["images"]["jpg"]["image_url"]
        title = data["titles"][0]["title"]
        status = data["status"]
        airing = data["aired"]["string"]
        synopsis = data["synopsis"]
        animeType = data["demographics"][0]["name"]

        infoEmbed = discord.Embed(
            title=title,
            color=color,
            description=synopsis
        )
        infoEmbed.set_thumbnail(url = image)
        infoEmbed.set_footer(text=f"Requested by {ctx.author}")
        infoEmbed.add_field(name="Status", value=status, inline=True)
        infoEmbed.add_field(name="Date", value=airing, inline=True)
        infoEmbed.add_field(name="Demographics", value=animeType, inline=True)
        await ctx.respond(embed=infoEmbed)

    @images.command(name="kill", description="Fake Kills the specified user with Anime Gifs")
    async def kill(self, ctx, user: Option(discord.Member, description="The user to fake kill")):
        gif = anime.get_sfw('kill')
        killEmbed = discord.Embed(
            title=f"{ctx.author} killed {user}",
            color= color
        )
        killEmbed.set_image(url=gif)
        await ctx.respond(embed = killEmbed)
    
    @images.command(name="pat", description="Fake Hugs the specified user with Anime Gifs")
    async def pat(self, ctx, user: Option(discord.Member, description="To fake pat a user")):
        gif = anime.get_sfw('pat')
        title=f"{ctx.author} patted {user}"
        if (ctx.author.id == 389306174119608321) and (user.id == 696740455789887599):
            gif = "https://cdn.discordapp.com/attachments/1115645744284704798/1119516686974996520/pika_pat.gif"
        patEmbed = discord.Embed(
            title= title,
            color= color
        )
        patEmbed.set_image(url = gif)
        await ctx.respond(embed = patEmbed)

    @images.command(name="slap", description="Fake Slaps the specified users with anime slaps")
    async def slap(slef, ctx, user: Option(discord.Member, description="Person to fake slap")):
        gif = anime.get_sfw('slap')
        slapEmbed = discord.Embed(
            title=f"{ctx.author} slapped {user}",
            color=color
        )
        slapEmbed.set_image(url = gif)
        await ctx.respond(embed = slapEmbed)

    @images.command(name="cuddle", description="Fake cuddles the specified user with anime cuddles")
    async def cuddle(self, ctx, user: Option(discord.Member, description="Fake Cuddle")):
        gif = anime.get_sfw('cuddle')
        cuddleEmbed = discord.Embed(
            title=f"{ctx.author} cuddles {user}",
            color=color
        )
        cuddleEmbed.set_image(url = gif)
        await ctx.respond(embed = cuddleEmbed)
        
    
        

def setup(bot):
    bot.add_cog(Anime(bot))