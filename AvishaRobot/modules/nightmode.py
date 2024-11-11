from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telethon import functions, types
from telethon.tl.types import ChatBannedRights
from telethon import TelegramClient, events, Button
from AvishaRobot import (
    BOT_NAME,
    BOT_USERNAME)
from AvishaRobot import telethn as tbot
from AvishaRobot.events import register
from AvishaRobot.modules.sql.night_mode_sql import (
    add_nightmode,
    get_all_chat_id,
    is_nightmode_indb,
    rmnightmode,
)


async def is_register_admin(chat, user):
    if isinstance(chat, (types.InputPeerChannel, types.InputChannel)):

        return isinstance(
            (
                await tbot(functions.channels.GetParticipantRequest(chat, user))
            ).participant,
            (types.ChannelParticipantAdmin, types.ChannelParticipantCreator),
        )
    elif isinstance(chat, types.InputPeerChat):

        ui = await tbot.get_peer_id(user)
        ps = (
            await tbot(functions.messages.GetFullChatRequest(chat.chat_id))
        ).full_chat.participants.participants
        return isinstance(
            next((p for p in ps if p.user_id == ui), None),
            (types.ChatParticipantAdmin, types.ChatParticipantCreator),
        )
    else:
        return None


hehes = ChatBannedRights(
    until_date=None,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    send_polls=True,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)
openhehe = ChatBannedRights(
    until_date=None,
    send_messages=False,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    send_polls=False,
    invite_users=False,
    pin_messages=False,
    change_info=False,
)
button_row = [
        [Button.url('ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ', f'https://t.me/{BOT_USERNAME}?startgroup=new')]
    ]
@register(pattern="^/nightmode")
async def close_ws(event):
    if event.is_group:
        if not (await is_register_admin(event.input_chat, event.message.sender_id)):
            await event.reply("𖣐 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ꜱᴏ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ...")
            return

    if not event.is_group:
        await event.reply("𖣐 ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴇɴᴀʙʟᴇ ɴɪɢʜᴛ ᴍᴏᴅᴇ ɪɴ ɢʀᴏᴜᴘꜱ.")
        return
    if is_nightmode_indb(str(event.chat_id)):
        await event.reply("𖣐 ᴛʜɪꜱ ᴄʜᴀᴛ ɪꜱ ʜᴀꜱ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ɴɪɢʜᴛ ᴍᴏᴅᴇ")
        return
    add_nightmode(str(event.chat_id))
    await event.reply(
        f"𖣐 ɴɪɢʜᴛ ᴍᴏᴅᴇ ᴇɴᴀʙʟᴇᴅ ɪɴ ᴛʜɪs ᴄʜᴀᴛ.\n\n● ᴀᴅᴅᴇᴅ ᴄʜᴀᴛ ➥ `{event.chat.title}`\n● ɢʀᴏᴜᴘ ɪᴅ ➥ `{event.chat_id}`\n\n❖ ᴛʜɪꜱ ɢʀᴏᴜᴘ ᴡɪʟʟ ʙᴇ ᴄʟᴏꜱᴇᴅ ᴏɴ 12 ᴀᴍ(ɪꜱᴛ) ᴀɴᴅ ᴡɪʟʟ ᴏᴘᴇɴᴇᴅ ᴏɴ 06 ᴀᴍ(ɪꜱᴛ)",
       buttons=button_row )


@register(pattern="^/rmnight")
async def disable_ws(event):
    if event.is_group:
        if not (await is_register_admin(event.input_chat, event.message.sender_id)):
            await event.reply("𖣐 ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ ꜱᴏ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ..")
            return

    if not event.is_group:
        await event.reply("𖣐 ʏᴏᴜ ᴄᴀɴ ᴏɴʟʏ ᴅɪꜱᴀʙʟᴇ ɴɪɢʜᴛ ᴍᴏᴅᴇ ɪɴ ɢʀᴏᴜᴘꜱ.")
        return
    if not is_nightmode_indb(str(event.chat_id)):
        await event.reply("𖣐 ᴛʜɪꜱ ᴄʜᴀᴛ ɪꜱ ɴᴏᴛ ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ ɴɪɢʜᴛ ᴍᴏᴅᴇ")
        return
    rmnightmode(str(event.chat_id))
    await event.reply(
        f"𖣐 ɴɪɢʜᴛ ᴍᴏᴅᴇ ᴏғғ ᴀᴛ ᴛʜɪs ɢʀᴏᴜᴘ\n\n● ʀᴇᴍᴏᴠᴇᴅ ᴄʜᴀᴛ ➥ `{event.chat.title}` \n● ɢʀᴏᴜᴘ ɪᴅ ➥  `{event.chat_id}` \n\n𖣐 ᴘᴏᴡᴇʀᴅ ʙʏ ➥ [˹Ҩ፝֟፝ͷ ꫝɴᴊᴀʟɪ˼ [🇮🇳]](https://t.me/AnjaliOwnerBot)", buttons=button_row
    )


async def job_close():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await tbot.send_message(
                int(warner.chat_id),
                f"𖣐 ɢʀᴏᴜᴘ ɪꜱ ᴄʟᴏꜱɪɴɢ, ɢᴏᴏᴅ ɴɪɢʜᴛ ᴇᴠᴇʀʏᴏɴᴇ !\n\n● ᴍᴀʏ ᴛʜᴇ ᴀɴɢᴇʟs ғʀᴏᴍ ʜᴇᴀᴠᴇɴ ʙʀɪɴɢ ᴛʜᴇ sᴡᴇᴇᴛᴇsᴛ ᴏғ ᴀʟʟ ᴅʀᴇᴀᴍs ғᴏʀ ʏᴏᴜ. ᴍᴀʏ ʏᴏᴜ ʜᴀᴠᴇ ʟᴏɴɢ ᴀɴᴅ ʙʟɪssғᴜʟ sʟᴇᴇᴘ ғᴜʟʟ ᴏғ ʜᴀᴘᴘʏ ᴅʀᴇᴀᴍs.\n\n𖣐 ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ [˹Ҩ፝֟፝ͷ ꫝɴᴊᴀʟɪ˼ [🇮🇳]](https://t.me/AnjaliOwnerBot)",buttons=button_row)
            await tbot(
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=int(warner.chat_id), banned_rights=hehes
                )
            )
        except Exception as e:
            logger.info(f"⬤ ᴜɴᴀʙʟᴇ ᴛᴏ ᴄʟᴏꜱᴇ ɢʀᴏᴜᴘ {warner} ➥ {e}")


# Run everyday at 12am
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_close, trigger="cron", hour=23, minute=59)
scheduler.start()


async def job_open():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await tbot.send_message(
                int(warner.chat_id),
                f"𖣐 ɢʀᴏᴜᴘ ɪꜱ ᴏᴘᴇɴɪɴɢ, ɢᴏᴏᴅ ᴍᴏʀɴɪɴɢ ᴇᴠᴇʀʏᴏɴᴇ !\n\n● ᴍᴀʏ ᴛʜɪs ᴅᴀʏ ᴄᴏᴍᴇ ᴡɪᴛʜ ᴀʟʟ ᴛʜᴇ ʟᴏᴠᴇ ʏᴏᴜʀ ʜᴇᴀʀᴛ ᴄᴀɴ ʜᴏʟᴅ ᴀɴᴅ ʙʀɪɴɢ ʏᴏᴜ ᴇᴠᴇʀʏ sᴜᴄᴄᴇss ʏᴏᴜ ᴅᴇsɪʀᴇ. ᴍᴀʏ ᴇᴀᴄʜ ᴏғ ʏᴏᴜʀ ғᴏᴏᴛsᴛᴇᴘs ʙʀɪɴɢ ᴊᴏʏ ᴛᴏ ᴛʜᴇ ᴇᴀʀᴛʜ ᴀɴᴅ ʏᴏᴜʀsᴇʟғ. ɪ ᴡɪsʜ ʏᴏᴜ ᴀ ᴍᴀɢɪᴄᴀʟ ᴅᴀʏ ᴀɴᴅ ᴀ ᴡᴏɴᴅᴇʀғᴜʟ ʟɪғᴇ ᴀʜᴇᴀᴅ.\n\n𖣐 ᴘᴏᴡᴇʀᴇᴅ ʙʏ ➥ [˹Ҩ፝֟፝ͷ ꫝɴᴊᴀʟɪ˼ [🇮🇳]](https://t.me/AnjaliOwnerBot)",buttons=button_row)
            await tbot(
                functions.messages.EditChatDefaultBannedRightsRequest(
                    peer=int(warner.chat_id), banned_rights=openhehe
                )
            )
        except Exception as e:
            logger.info(f"⬤ ᴜɴᴀʙʟᴇ ᴛᴏ ᴏᴘᴇɴ ɢʀᴏᴜᴘ {warner.chat_id} ➥ {e}")


# Run everyday at 06
scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_open, trigger="cron", hour=6, minute=1)
scheduler.start()

__help__ = """

 ⬤ /nightmode *➥* ᴀᴅᴅs ɢʀᴏᴜᴘ ᴛᴏ ɴɪɢʜᴛᴍᴏᴅᴇ ᴄʜᴀᴛs.
 ⬤ /rmnight *➥* ʀᴇᴍᴏᴠᴇs ɢʀᴏᴜᴘ ғʀᴏᴍ ɴɪɢʜᴛᴍᴏᴅᴇ ᴄʜᴀᴛs.
"""
__mod_name__ = "ɴ-ᴍᴏᴅᴇ"

