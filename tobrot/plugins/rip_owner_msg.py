import asyncio 

async def rip_owner_msg(message):
  if message in not None:
    if message.text.lower().startswith("@The_Fourth_Minato"):
      await message.reply_text("the owner of this bot @The_Fourth_Minato is ded 🥲")
      return 
 

