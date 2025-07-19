import asyncio
from pyrogram import Client
from pyrogram.raw.functions.messages import RequestAppWebView
from pyrogram.raw.types import InputBotAppShortName, InputUser
from urllib.parse import unquote
from curl_cffi import AsyncSession
from .classes.Exceptions import authDataError

async def update_auth(
    api_id: int | str = None,
    api_hash: str = None,
    session_string: str = "",
    session_name: str = "session",
    bot_username: str = "mrkt",
    bot_short_name: str = "app",
    platform: str = "android"
) -> str:
    
    if not session_string and (not api_id or not api_hash):
        raise authDataError("MRKT API: update_auth(): You must provide either api_id and api_hash or a session_string.")

    if session_string:
        client = Client(session_name, session_string=session_string)
    else:
        client = Client(session_name, api_id=api_id, api_hash=api_hash)

    async with client:
        bot_entity = await client.get_users(bot_username)
        peer = await client.resolve_peer(bot_username)
        bot = InputUser(user_id=bot_entity.id, access_hash=bot_entity.raw.access_hash)
        bot_app = InputBotAppShortName(bot_id=bot, short_name=bot_short_name)
        web_view = await client.invoke(
            RequestAppWebView(
                peer=peer,
                app=bot_app,
                platform=platform,
            )
        )
        init_data = unquote(web_view.url.split('tgWebAppData=', 1)[1].split('&tgWebAppVersion', 1)[0])
        auth_data = {"data": init_data}

        async with AsyncSession() as s:
            r = await s.post(url="https://api.tgmrkt.io/api/v1/auth", json=auth_data)
            rj = r.json()
            token = rj.get('token') if rj else None

    return token
