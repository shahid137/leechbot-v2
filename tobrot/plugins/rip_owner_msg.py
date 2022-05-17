import asyncio 

async def rip_owner_msg(message):
  if "@The_Fourth_Minato" is in message.text:
    await message.reply_text("the owner of this bot is ded")
