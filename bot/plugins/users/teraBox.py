import os

from pyrogram import Client, filters
from pyrogram.types import Message
from bot.logging import LOGGER
from bot.helpers.terabox import teraBoxFile


@Client.on_message(filters.command(["terabox", "tera", "dl"]))
async def teraBoxDl(_, message: Message):
    """
    Download file from terabox.
    """
    if len(message.command) < 2:
        return await message.reply_text("No url provided")
    url = message.text.split(None, 1)[1]
    LOGGER(__name__).info(f"Downloading file from {url}")

    try:
        file = await teraBoxFile(url)
        await message.reply_document(document=file, quote=True) and os.remove(file)
        LOGGER(__name__).info(f"Downloaded file from {url}")
    except Exception as e:
        LOGGER(__name__).error(f"Failed to download file from {url}\n{str(e)}")
        await message.reply_text(f"Failed to download file from {url}\n'Error: '{str(e)}")
