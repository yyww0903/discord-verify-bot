
# 필수설치 모듈
#pip install discord.py
#pip install captcha

import discord
from captcha.image import ImageCaptcha
import random
import time

client = discord.Client()

@client.event
async def on_ready():
    print("인증 봇이 정상적으로 실행되었습니다.")
    game = discord.Game('조선을 위해 산다~')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("/인증"): #명령어 /인증
        a = ""
        Captcha_img = ImageCaptcha()
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        Captcha_img.write(a, name)

        await message.channel.send(f"""{message.author.mention} 아래 숫자를 10초 내에 입력해주세요. """)
        await message.channel.send(file=discord.File(name))

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check) # 제한시간 10초
        except:
            await message.channel.purge(limit=3)
            chrhkEmbed = discord.Embed(title='❌ 인증실패', color=0xFF0000)
            chrhkEmbed.add_field(name='닉네임', value=message.author, inline=False)
            chrhkEmbed.add_field(name='이유', value='시간초과', inline=False)
            await message.channel.send(embed=chrhkEmbed)
            print(f'{message.author} 님이 시간초과로 인해 인증을 실패함.')
            return

        if msg.content == a:
            role = discord.utils.get(message.guild.roles, name="💮〘  백 성  〙💮")
            await message.channel.purge(limit=4)
            tjdrhdEmbed = discord.Embed(title='인증성공', color=0x04FF00)
            tjdrhdEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tjdrhdEmbed.add_field(name='5초후 인증역할이 부여됩니다.', value='** **', inline=False)
            tjdrhdEmbed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=tjdrhdEmbed)
            time.sleep(5)
            await message.author.add_roles(role)
        else:
            await message.channel.purge(limit=4)
            tlfvoEmbed = discord.Embed(title='❌ 인증실패', color=0xFF0000)
            tlfvoEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tlfvoEmbed.add_field(name='이유', value='잘못된 숫자', inline=False)
            await message.channel.send(embed=tlfvoEmbed)
            print(f'{message.author} 님이 잘못된 숫자로 인해 인증을 실패함.')

client.run('NzY3MTE2ODk3ODgzNjUyMDk2.X4tPSA.Q5kdtZpE45yME8J_g3wk7pFHnXQ')


