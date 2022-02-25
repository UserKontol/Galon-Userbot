from userbot.utils import kyy_cmd
from userbot import CMD_HELP, CMD_HANDLER as cmd


@kyy_cmd(pattern="(?:dm)\\s?(.*)?")
async def remoteaccess(event):

    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:
        chat_id = int(chat_id)
    except BaseException:

        pass

    msg = ""
    mssg = await event.get_reply_message()
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("`Success Mengirim Pesan Anda.`")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("`Success Mengirim Pesan Anda.`")
    except BaseException:
        await event.edit("**Terjadi Error. Gagal Mengirim Pesan.**")

CMD_HELP.update(
    {
        "message": f"`{cmd}dm`\
    \nMengirim Pesan Dengan Jarak Jauh Dengan .dm <username> <pesan>."
    })