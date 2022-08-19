import disnake
import os
import json
from disnake.ext import commands,tasks

client = commands.Bot(command_prefix='!', intents=disnake.Intents.all(),help_command=None)

class levelControl(commands.Cog):
	def __init__(self,client):
		self.client = client
		self.levelcontrol.start()

	@tasks.loop(seconds=10)
	async def levelcontrol(self):
		for member in self.client.get_all_members():
			with open(f"guilds/{member.guild.id}/options/{member.guild.id}") as file:
				data = json.load(file)
				language = data['language']
			textchannel = self.client.get_channel(data['defaultChannel'])
			file_there = os.path.isfile(f"guilds/{member.guild.id}/levels/{member.id}")
			if file_there:
				if not member.bot:
						with open(f"guilds/{member.guild.id}/levels/{member.id}") as file:
							data = json.load(file)

						level = data['level']
						maximumXP = data['maximumXP']
						XP = data['XP']
						XPmax = data['XPmax']
						XPmin = data['XPmin']
						XPdiv = data['XPdiv']

						if XP > maximumXP:
							if level == 0:
								data['level'] = 1
								data['maximumXP'] = 1500
								data['XPmax'] = 500
								data['XPmin'] = 1000
								data['XPdiv'] = 15
								with open(f"guilds/{member.guild.id}/levels/{member.id}","w") as file:
									json.dump(data,file,indent=4)
							
							else:
								level += 1
								maximumXP += (maximumXP * 0.5)
								XPmax += (XPmax * 0.5)
								XPmin += (XPmin * 0.5)
								XPdiv += (XPdiv * 0.5)
								
								data['level'] = level
								data['maximumXP'] = maximumXP
								data['XPmax'] = XPmax
								data['XPmin'] = XPmin
								data['XPdiv'] = XPdiv
								
								with open(f"guilds/{member.guild.id}/levels/{member.id}","w") as file:
									json.dump(data,file,indent=4)

								with open(f"guilds/localization/{language}.json") as file:
									localization = json.load(file)

								await textchannel.send(f"{localization['LEVEL_UP_MESSAGE'].format(member=member.mention,level = level)}")

							
								
			if not file_there:
				with open(f"guilds/{member.guild.id}/levels/{member.id}","w") as file:
					data = {
						"XP" : 1,
						"maximumXP" : 1000,
						"level" : 0,
						"XPmax" : 1000,
						"XPmin" : 0,
						"XPdiv" : 10
					}
					json.dump(data,file,indent=4)

			
	@levelcontrol.before_loop
	async def beforeLevelControl(self):
		await self.client.wait_until_ready()
		print("Seviye sistemi döngüsü hazır!")

	

def setup(client):
	client.add_cog(levelControl(client))
