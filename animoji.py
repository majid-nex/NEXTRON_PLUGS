import asyncio
from collections import deque

from ULTRA.utils import admin_cmd, edit_or_reply, sudo_cmd
from ULTRA import CMD_HELP


@bot.on(admin_cmd(pattern="think$", outgoing=True))
@bot.on(sudo_cmd(pattern="think$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "think")
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"lmao$"))
@bot.on(sudo_cmd(pattern="lmao$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "lmao")
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"nothappy$"))
@bot.on(sudo_cmd(pattern="nothappy$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "nathappy")
    deq = deque(list("😁☹️😁☹️😁☹️😁"))
    for _ in range(48):
        await asyncio.sleep(0.4)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(outgoing=True, pattern="clock$"))
@bot.on(sudo_cmd(pattern="clock$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "clock")
    deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=r"muah$"))
@bot.on(sudo_cmd(pattern="muah$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "muah")
    deq = deque(list("😗😙😚😚😘"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="heart$"))
@bot.on(sudo_cmd(pattern="heart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "heart")
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern="gym$", outgoing=True))
@bot.on(sudo_cmd(pattern="gym$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "gym")
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"earth$", outgoing=True))
@bot.on(sudo_cmd(pattern="earth$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "earth")
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(outgoing=True, pattern="moon$"))
@bot.on(sudo_cmd(pattern="moon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "moon")
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@bot.on(admin_cmd(pattern=f"smoon$", outgoing=True))
@bot.on(sudo_cmd(pattern="smoon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "smoon")
    animation_interval = 0.1
    animation_ttl = range(101)
    await event.edit("smoon..")
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 8])


@bot.on(admin_cmd(pattern=f"tmoon$", outgoing=True))
@bot.on(sudo_cmd(pattern="tmoon$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "tmoon")
    animation_interval = 0.1
    animation_ttl = range(117)
    await event.edit("tmoon")
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 32])

@bot.on(admin_cmd(pattern=f"hart$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"hart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.5
    animation_ttl = range(20)
    event = await edit_or_reply(event, "❤️")
    animation_chars = ["🖤", "❤️", "🖤", "❤️", "‎"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 4])


@bot.on(admin_cmd(pattern=f"anim$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"anim$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(20)
    event = await edit_or_reply(event, "😢")
    animation_chars = [
        "😁",
        "😧",
        "😡",
        "😢",
        "😁",
        "😧",
        "😡",
        "😢",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 10])


@bot.on(admin_cmd(pattern=f"fnl$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"fnl$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(6)
    event = await edit_or_reply(event, "Hey There....")
    animation_chars = ["😁🏿", "😁🏾", "😁🏽", "😁🏼", "‎😁"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])


@bot.on(admin_cmd(pattern=f"monkey$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"monkey$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(12)
    event = await edit_or_reply(event, "Hey There....")
    animation_chars = ["🐵", "🙉", "🙈", "🙊", "🖕‎🐵🖕"]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 6])

@bot.on(admin_cmd(pattern=f"hand$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"hand$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(13)
    event = await edit_or_reply(event, "🖐️")
    animation_chars = [
        "👈",
        "👉",
        "☝️",
        "👆",
        "🖕",
        "👇",
        "✌️",
        "🤞",
        "🖖",
        "🤘",
        "🤙",
        "🖐️",
        "👌",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 13])


@bot.on(admin_cmd(pattern=f"gsg$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"gsg$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(12)
    event = await edit_or_reply(event, "ContDown....")
    animation_chars = [
        "🔟",
        "9️⃣",
        "8️⃣",
        "7️⃣",
        "6️⃣",
        "5️⃣",
        "4️⃣",
        "3️⃣",
        "2️⃣",
        "1️⃣",
        "0️⃣",
        "🆘",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@bot.on(admin_cmd(pattern=r"theart$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"theart$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(54)
    event = await edit_or_reply(event, "🖤")
    animation_chars = [
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
        "❤️",
        "🧡",
        "💛",
        "💚",
        "💙",
        "💜",
        "🖤",
        "💘",
        "💝",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])



CMD_HELP.update(
    {
        "animoji": """**Plugin : **`animoji`
        
**Commands in animoji are **
  •  `.think`
  •  `.lmao`
  •  `.nothappy`
  •  `.clock`
  •  `.muah`
  •  `.heart`
  •  `.gym`
  •  `.earth`
  •  `.moon`
  •  `.smoon`
  •  `.tmoon`
  •  `.hart`
  •  `.anim`
  •  `.fnl`
  •  `.monkey`
  •  `.hand`
  •  `.gsg`
  •  `.theart`
  
**Function : **__Different kinds of emoji animation commands check yourself for their animation .__"""
    }
)
