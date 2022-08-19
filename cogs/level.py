import disnake
import os
from disnake.ext import commands
from main import client
import json
import urllib.request
from PIL import Image, ImageDraw,ImageOps,ImageFont,ImageColor

class LevelPNG(commands.Cog):
    def __init__(self,userID,guildID):
        self.guild = client.get_guild(guildID)
        self.userID = userID
        self.getIcon()
        
    def getIcon(self):
        user = self.guild.get_member(self.userID)
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        # filename = f"Levels/{user.id}.png"
        filename = f"guilds/{self.guildID}/files/images/{self.userID}.png"
        url = user.display_avatar.url
        urllib.request.urlretrieve(str(url),filename)
        self.__makeRound()

    def makeImage(self):
        with open(f"guilds/{self.guildID}/levels/{self.userID}.json") as file:
            data = json.load(file)
        user = self.guild.get_member(self.userID)
        color = user.top_role.color
        color = ImageColor.getcolor(str(color),"RGB")
        XP_ = data['XP']
        level_ = data['level']
        # maximumXP = data['maximumXP']
        XPdiv = data['XPdiv']
        XPmin = data['XPmin']
        # XPmax = data['XPmax']
        XPBar = ((XP_-XPmin)/XPdiv)*5.9
        rank_ = self.getRank()
        image = Image.new("RGB",(934,282),color=(28,28,28))
        image.paste(self.output,(20,11),mask=self.mask)
        text = ImageDraw.Draw(image)
        
        nickname = user.name
        size = 75
        discriminatorSize = 45
        
        nick = ImageFont.truetype("files/-fonts/PrimaSansBT-Roman.otf", size=size)
        nickWidth = nick.getsize(nickname)
        nicknameLength= len(nickname)
        
        discriminator = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=discriminatorSize)
        discriminatorY = 46
        
        if nicknameLength > 7:
            
            if nicknameLength > 12:
                nickname = nickname[0:12] + "..."
                nick = ImageFont.truetype("files/fonts/PrimaSansBT-Roman.otf", size=55)
                nickWidth = nick.getsize(nickname)
                
                discriminator = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=33)
                
                text.text((305,15),text=nickname,font=nick,fill=(255,255,255))
                text.text((nickWidth[0]+310,42),text=f"#{user.discriminator}",font=discriminator,fill=(70,70,70))
           
            else:
                while nicknameLength > 7 and nicknameLength <= 12:
                    size -= 5
                    discriminatorSize -= 3
                    discriminatorY -= 2.4
                    nicknameLength -= 1
                nick = ImageFont.truetype("files/fonts/PrimaSansBT-Roman.otf", size=size)
                nickWidth = nick.getsize(nickname)
                discriminator = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=discriminatorSize)
                text.text((305,7),text=nickname,font=nick,fill=(255,255,255))
           
        else:
            nick = ImageFont.truetype("files/fonts/PrimaSansBT-Roman.otf", size=size)
            discriminator = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=discriminatorSize)
            text.text((305,7),text=nickname,font=nick,fill=(255,255,255))
            text.text((nickWidth[0]+310,discriminatorY),text=f"#{user.discriminator}",font=discriminator,fill=(70,70,70))

        text.rounded_rectangle([(300,220),(905,250)],radius=20,fill=(105,105,105))
        text.rounded_rectangle([(300,220),(315+XPBar,250)],radius=20,fill=color)

        XP = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=30)
        xpNumber = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=55)
        level = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=30)
        number = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=70)
        rank = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=30)
        if rank_ >= 10 and rank_ < 100:
            rankNumber = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=50)
        elif rank_ > 99:
            rankNumber = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=33)
        else:
            rankNumber = ImageFont.truetype("files/fonts/HarmoniaSansProCyr-Regular.ttf",size=70)
            
        nickWidth = nick.getsize(f"{user.name}")
        if rank_ > 99:
            text.text((875,28),text="99+",font=rankNumber,fill=color)
        else:
            text.text((875,15),text=f"{rank_}",font=rankNumber,fill=color)
        text.text((780,31),text=f"RANK :",font=rank,fill=(255,255,255))
        text.text((315,180),text=f"LEVEL",font=level,fill=(255,255,255))
        text.text((397,152),text=f"{level_}",font=number,fill=color)
        text.text((670,180),text=f"XP",font=XP,fill=(255,255,255))
        text.text((715,164),text=f"{XP_}",font=xpNumber,fill=color)

        image.save(f"guilds/{self.guildID}/files/images/{self.userID}.png",quality=100)
        border = Image.new("RGB",(1000,346),color=(37,37,37))
        rectangle = ImageDraw.Draw(border)
        border.paste(image,(34,34))
        border.save(f"guilds/{self.guildID}/files/images/{self.userID}.png")
        self.__finalize()



    def getRank(self):
        di = {}
        user = self.guild.get_member(self.userID)
        for member in client.get_all_members():
            if member.id == 1009068314158432288:
                pass
            else:
                with open(f"guilds/{self.guildID}/levels/{member.id}.json") as file:
                    data = json.load(file)
                XP = data['XP']
                di[member.name] = int(XP)
        sözlük = dict(sorted(di.items(),key=lambda item:item[1],reverse=True))
        number = ((list(sözlük.keys()).index(user.name)) + 1)
        return number
	
	
    def __makeRound(self):
        size = (256, 256)
        self.mask = Image.new('L', size, 0)
        draw = ImageDraw.Draw(self.mask) 
        draw.ellipse((0, 0) + size, fill=255)
        
        image = Image.open(f"guilds/{self.guildID}/files/images/{self.userID}.png")
        self.output = ImageOps.fit(image, self.mask.size, centering=(0.5, 0.5))
        self.output.putalpha(self.mask)
        os.remove(f"guilds/{self.guildID}/files/images/{self.userID}.png")
        self.output.save(f"guilds/{self.guildID}/files/images/{self.userID}.png")
        self.makeImage()
        
        


    def __finalize(self):
        image = Image.open(f"guilds/{self.guildID}/files/images/{self.userID}.png")
        rad = 20
        circle = Image.new('L', (rad * 2, rad * 2), 0)
        draw = ImageDraw.Draw(circle)
        draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
        alpha = Image.new('L', image.size, 255)
        w, h = image.size
        alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
        alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
        alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
        alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
        image.putalpha(alpha)
        
        self.im = Image.open(f"guilds/{self.guildID}/files/images/{self.userID}.png")
        self.im.save(f"guilds/{self.guildID}/files/images/{self.userID}.png")





class Level(commands.Cog):
    def __init__(self,client):
        self.client = client
        
    @commands.slash_command(name = "level", description= "Bir kullanıcının seviyesini görüntülemek için kullan.")
    async def level(self,inter, kullanıcı : disnake.Member = None):
        
        with open(f"guilds/{inter.guild.id}/options/{inter.guild.id}") as file:
            data = json.load(file)
            embedColor = data['embedColor']
            language = data['language']        


        with open(f"localization/{language}.json") as file:
            localization = json.load(file)

        if kullanıcı == None:
            user = inter.author
        else:
            user = kullanıcı

        file_there = os.path.isfile(f"guilds/{inter.guild.id}/levels/{user.id}.json")
        if file_there:
            LevelPNG(user.id,inter.guild.id)
            file = disnake.File(f"guilds/{self.guildID}/files/images/{self.userID}.png",filename= "image.png")
            await inter.response.send_message(file=file)

        else:
            embed = disnake.Embed(
                title = localization['LEVEL_ERROR_EMBED_TITLE'],
                description = localization['LEVEL_ERROR_EMBED_DESCRIPTION'],
                color = embedColor
            )
            await inter.response.send_message(embed=embed,ephemeral=True)
        

def setup(client):
    client.add_cog(Level(client))