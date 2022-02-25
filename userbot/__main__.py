# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot start point """

import sys
from importlib import import_module

import requests
from telethon.tl.functions.channels import InviteToChannelRequest as Addbot

from userbot import BOTLOG_CHATID, BOT_USERNAME, BOT_TOKEN, BOT_VER, LOGS, ALIVE_NAME, ALIVE_LOGO, galonbl, bot
from userbot.modules import ALL_MODULES
from userbot.utils import autobot

try:
    bot.start()
    user = bot.get_me()
    galonbl = requests.get(
        "https://gist.githubusercontent.com/galihpujiirianto/256ac0a53805f984b67d7715cd67438b/raw/782be745471d8147c4cf94433a6f94a3ab178f51/galonbl.json"
    ).json()
    if user.id in galonbl:
        LOGS.warning(
            "YAHHAHAHA BADUT BADUT, MAKANYA JADI ORANG JANGAN TOLOL, KU MATIIN AH BOTNYA, NAJIS KALO DIPAKE SAMA LU!"
        )
        sys.exit(1)
except Exception as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)

LOGS.info(
    f"Yep! Botnya berhasil dijalankan. Kalau ada masalah bisa langsung tanya di https://t.me/GalonSupport ya!")
LOGS.info(
    f"✨Galon-Userbot✨ ⚙️ V{BOT_VER} [TELAH DIAKTIFKAN!]")


async def check_alive():
    try:
        if BOTLOG_CHATID != 0:
            await bot.send_file(BOTLOG_CHATID, ALIVE_LOGO, caption=f"✨ **Galon-Userbot Has Been Actived**!!\n━━━━━━━━━━━━━━━\n➠ **Userbot Version** - {BOT_VER}@Galon-Userbot\n━━━━━━━━━━━━━━━\n➠ **Powered By @GalonUpdates.** ")
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(Addbot(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass

bot.loop.run_until_complete(check_alive())
if not BOT_TOKEN:
    LOGS.info(
        "BOT_TOKEN Vars tidak terisi, Memulai Membuat BOT Otomatis di @Botfather..."
    )
    bot.loop.run_until_complete(autobot())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
