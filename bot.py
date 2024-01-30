#!/usr/bin/env python
# -*- coding: utf-8 -*- 
#
# ┌──────────────────────────────────────┐
# │                                      │
# │    > installing guide :              │
# │       pip install pyrogram==2.0.106  │
# │       pip install replicate          │
# │       pip install asyncio            │
# │       pip install requests           │
# │                                      │
# │                                      │
# │    > Developer :                     │
# │         @LampStack                   │
# └──────────────────────────────────────┘


import os, replicate, requests
from pyrogram import Client, filters, errors


#           ---         ---         ---         #
api_id = 00000000 # main api id from my.telegram.org/apps
api_hash = 'xxxxxxxxxxxxxxxx' # main api hash from my.telegram.org/apps
bot_token = '000000000:xxxxxxxxxxxxxxxxxxxxxxxx' # main bot token from @botFather
os.environ["REPLICATE_API_TOKEN"] = "xxxxxxxxxxxxxxxxx"  # get it from https://replicate.com
#           ---         ---         ---         #


async def create_AI_Art(prompt:str="Astronaut in a jungle, cold color palette, muted colors, detailed, 8k") -> str:
    output = replicate.run(
    "playgroundai/playground-v2-1024px-aesthetic:42fe626e41cc811eaf02c94b892774839268ce1994ea778eba97103fe1ef51b8",
    input={
        "width": 1024,
        "height": 1024,
        "prompt": prompt,
        "scheduler": "K_EULER_ANCESTRAL",
        "guidance_scale": 3,
        "apply_watermark": False,
        "negative_prompt": "",
        "num_inference_steps": 50
    }
    )
    return output[0]


async def high_resolution(url:str="https://replicate.delivery/pbxt/IngEkQmZiZ3whtbkNAiOIdCsYAWVMkmoIBJnw7t2TPgvJn5S/photo.jpg") -> str:
    output = replicate.run(
    "sczhou/codeformer:7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56",
    input={
        "image": url,
        "upscale": 1,
        "face_upsample": True,
        "background_enhance": True,
        "codeformer_fidelity": 0.7
    }
    )
    return output


async def image_colorize(url:str="https://replicate.delivery/pbxt/I9uDZgopnhz6X956zgaBoorFWbUmu5HHDyjkd3BY3ZnxVAdu/1.jpg") -> str:
    output = replicate.run(
    "arielreplicate/deoldify_image:0da600fab0c45a66211339f1c16b71345d22f26ef5fea3dca1bb90bb5711e950",
    input={
        "model_name": "Artistic",
        "input_image": url,
        "render_factor": 35
    }
    )
    return output


async def remove_background(url:str="https://replicate.delivery/pbxt/HoW8AeYS7KdWdDyasWuk2DNyXlstzrQKqaBkShVvF54n38lM/Screenshot%202022-11-18%20at%2001.10.34.png") -> str:
    output = replicate.run(
    "pollinations/modnet:da7d45f3b836795f945f221fc0b01a6d3ab7f5e163f13208948ad436001e2255",
    input={
        "image": url
    }
    )
    return output


async def photo_desribe_AI(url:str="https://replicate.delivery/pbxt/JfvBi04QfleIeJ3ASiBEMbJvhTQKWKLjKaajEbuhO1Y0wPHd/view.jpg") -> str:
    output = replicate.run(
    "yorickvp/llava-13b:e272157381e2a3bf12df3a8edd1f38d1dbd736bbb7437277c8b34175f8fce358",
    input={
        "image": url,
        "top_p": 1,
        "prompt": "describe it",
        "max_tokens": 1024,
        "temperature": 0.2
    }
    )
    return ''.join([char for char in output])


pid = os.getpid()
os.system("clear")
bot = Client(
    "bot",
    bot_token = bot_token,
    api_id = api_id,
    api_hash = api_hash
)
print(f"Bot Started At {pid}")


#           StartCommand            #
@bot.on_message(filters.command(['start']))
async def StartCommand(client, message):
    await message.reply(f"""👋🏻 Hi, welcome to AI tools.

● <b>Create AI Art (Text To Image)</b>
</code>/art</code> <u>[prompt]</u>

● <b>Robust face restoration algorithm for old photos :</b>
</code>/resolution</code> <u>(Please reply on a photo)</u>

● <b>Add colours to old images</b>
</code>/colorize</code> <u>(Please reply on a photo)</u>

● <b>Remove photos background</b>
</code>/removebg</code> <u>(Please reply on a photo)</u>

● <b>Visual instruction tuning towards large language and vision models with GPT-4 level capabilities</b>
</code>/describe</code> <u>(Please reply on a photo)</u>
""", quote=True)


#           Create AI Art            #
@bot.on_message(filters.regex('[!/.][aA][rR][tT] (.*)'))
async def CreateAIArt(client, message):
    prompt = message.text.replace(message.text.split()[0], '')
    msg = await message.reply(f'<b>Analizing ...</b>', quote=True)
    output = await create_AI_Art(prompt)
    await msg.delete()
    await bot.send_photo(message.chat.id, photo=output, caption=f"<b>Complete !</b>", reply_to_message_id=message.id)


#           Create Hight Resolution            #
@bot.on_message(filters.regex('[!/.][rR][eE][sS][oO][lL][uU][tT][iI][oO][nN]') & filters.reply)
async def HightResolution(client, message):
    if message.reply_to_message.photo:
        msg = await message.reply(f'<b>Analizing ...</b>', quote=True)
        file_path = requests.get(f'https://api.telegram.org/bot{bot_token}/getFile?file_id={message.reply_to_message.photo.file_id}').json()
        file_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path['result']['file_path']}"
        output = await high_resolution(file_url)
        await msg.delete()
        await bot.send_photo(message.chat.id, photo=output, caption=f"<b>Complete !</b>", reply_to_message_id=message.id)


#           Create Colorize Photo            #
@bot.on_message(filters.regex('[!/.][cC][oO][lL][oO][rR][iI][zZ][eE]') & filters.reply)
async def ColorizePhoto(client, message):
    if message.reply_to_message.photo:
        msg = await message.reply(f'<b>Analizing ...</b>', quote=True)
        file_path = requests.get(f'https://api.telegram.org/bot{bot_token}/getFile?file_id={message.reply_to_message.photo.file_id}').json()
        file_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path['result']['file_path']}"
        output = await image_colorize(file_url)
        await msg.delete()
        await bot.send_photo(message.chat.id, photo=output, caption=f"<b>Complete !</b>", reply_to_message_id=message.id)


#           Remove Background Photo            #
@bot.on_message(filters.regex('[!/.][rR][eE][mM][oO][vV][eE][bB][gG]') & filters.reply)
async def ColorizePhoto(client, message):
    if message.reply_to_message.photo:
        msg = await message.reply(f'<b>Analizing ...</b>', quote=True)
        file_path = requests.get(f'https://api.telegram.org/bot{bot_token}/getFile?file_id={message.reply_to_message.photo.file_id}').json()
        file_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path['result']['file_path']}"
        output = await remove_background(file_url)
        await msg.delete()
        await bot.send_photo(message.chat.id, photo=output, caption=f"<b>Complete !</b>", reply_to_message_id=message.id)


#           Describe Photo            #
@bot.on_message(filters.regex('[!/.][dD][eE][sS][cC][rR][iI][bB][eE]') & filters.reply)
async def DescribePhoto(client, message):
    if message.reply_to_message.photo:
        msg = await message.reply(f'<b>Analizing ...</b>', quote=True)
        file_path = requests.get(f'https://api.telegram.org/bot{bot_token}/getFile?file_id={message.reply_to_message.photo.file_id}').json()
        file_url = f"https://api.telegram.org/file/bot{bot_token}/{file_path['result']['file_path']}"
        output = await photo_desribe_AI(file_url)
        await msg.edit(f"<b>{output}</b>")



bot.run()
