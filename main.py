from telethon.sync import TelegramClient, events,types

from telethon import TelegramClient, events, sync,Button,functions

from time import gmtime, strftime

import asyncio


from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins
from telethon.errors import ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError
from telethon.utils import get_input_location
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio, datetime
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights, User
from telethon.sync import TelegramClient, events


api_id="10953300"

api_hash="9c24426e5d6fa1d441913e3906627f87"

token="6296935998:AAFwCdwG_A1ZROBTzJI2sz8Bl_XoouIqgLY"

bot=TelegramClient('programerhashbot', api_id, api_hash).start(bot_token=token)





# pass in the filter function as an argument to the `func` parameter
@bot.on(events.NewMessage(pattern="(?i)nme"))
async def _(event):
        await event.reply("Shunchaki")

@bot.on(events.NewMessage(pattern="(?i)hoz"))
async def _(event):
        await event.reply("ok man kutaman")

@bot.on(events.NewMessage(pattern="(?i)nmag"))
async def _(event):
        await event.reply("Shunchaki")

@bot.on(events.NewMessage( pattern="(?i)(?i)(?i)salo.+"))
async def _(event):
	print("salom")
	await event.reply("Assalomu alaykum")
@bot.on(events.NewMessage(pattern="(?i)qal.+"))
async def _(event):
	print("(?!)qale")
	await event.reply("Yaxshi , rahmat")

@bot.on(events.NewMessage(pattern="(?i)lc"))
async def _(event):
	await event.reply("YOQ!!!!")


@bot.on(events.NewMessage(pattern="(?i)lic"))
async def _(event):
        await event.reply("YOQ!!!!")


@bot.on(events.NewMessage( pattern="(?i)ssalo.+"))
async def _(event):
        print("Assalom")
@bot.on(events.NewMessage(pattern="(?i)otin"))
async def _(event):
        await event.reply("ótmiman.!!!.")

@bot.on(events.NewMessage(pattern="/start"))
async def any_message_arrived_handler(event):
    await event.reply('Hi')
@bot.on(events.NewMessage(pattern="(?i)nma"))
async def handler(event):
	await event.reply("Hechnima")

@bot.on(events.NewMessage(pattern="(?i)nima"))
async def handler(event):
        await event.reply("Hechnima")

@bot.on(events.NewMessage(pattern="options"))
async def handler(event):

	keyboard = [
        [  
            Button.inline("First option", b"1"), 
            Button.inline("Second option", b"2")
        ],
        [
            Button.inline("Third option", b"3"), 
            Button.inline("Fourth option", b"4")
        ],
        [
            Button.inline("Fifth option", b"5")
        ]
    ]

	await bot.send_message(event.chat_id,"OPTIONS \n\n\n\n\n:",buttons=keyboard)

bot.start()
print("started")
bot.run_until_disconnected()

