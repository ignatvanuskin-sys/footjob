"""Premium custom-emoji identifiers used across the Telegram user interface.

Telegram renders the literal emoji as a fallback and swaps in the premium
`<tg-emoji emoji-id="...">` asset when the client supports it. These IDs are
stable premium emoji provided by Telegram.

Usage in message bodies (HTML):

    f"{msg(EMOJI.SETTINGS, 'Настройки')}"

Usage on buttons -- pass the numeric emoji id string as ``icon`` to
``Button.inline(...)`` / ``Button.text(...)``; the rendered glyph is read from
``EMOJI.GLYPH`` matching the id.
"""

from __future__ import annotations

from html import escape


class EMOJI:
    """Stable premium emoji identifiers."""

    SETTINGS = "5870982283724328568"
    PROFILE = "5870994129244131212"
    PEOPLE = "5870772616305839506"
    PERSON_CHECK = "5891207662678317861"
    PERSON_CROSS = "5893192487324880883"
    FILE = "5870528606328852614"
    SMILE = "5870764288364252592"
    CHART_UP = "5870930636742595124"
    STATS = "5870921681735781843"
    HOUSE = "5873147866364514353"
    LOCK = "6037249452824072506"
    UNLOCK = "6037496202990194718"
    MEGAPHONE = "6039422865189638057"
    CHECK = "5870633910337015697"
    CROSS = "5870657884844462243"
    PENCIL = "5870676941614354370"
    TRASH = "5870875489362513438"
    POINT_DOWN = "5893057118545646106"
    SEARCH = "5893057118545646106"
    PAPERCLIP = "6039451237743595514"
    LINK = "5769289093221454192"
    INFO = "6028435952299413210"
    BOT = "6030400221232501136"
    EYE = "6037397706505195857"
    EYE_OFF = "6037243349675544634"
    SEND = "5963103826075456248"
    DOWNLOAD = "6039802767931871481"
    BELL = "6039486778597970865"
    GIFT = "6032644646587338669"
    CLOCK = "5983150113483134607"
    CONFETTI = "6041731551845159060"
    TEXT = "5870801517140775623"
    EDIT = "5870753782874246579"
    MEDIA = "6035128606563241721"
    LOCATION = "6042011682497106307"
    WALLET = "5769126056262898415"
    BOX = "5884479287171485878"
    CRYPTO = "5260752406890711732"
    CALENDAR = "5890937706803894250"
    TAG = "5886285355279193209"
    TIME_PAST = "5775896410780079073"
    APPS = "5778672437122045013"
    BRUSH = "6050679691004612757"
    ADD_TEXT = "5771851822897566479"
    RESIZE = "5778479949572738874"
    MONEY = "5904462880941545555"
    MONEY_SEND = "5890848474563352982"
    MONEY_RECEIVE = "5879814368572478751"
    CODE = "5940433880585605708"
    LOADING = "5345906554510012647"


class GLYPH:
    """Fallback rendered glyph for each premium emoji id."""

    SETTINGS = "⚙️"
    PROFILE = "👤"
    PEOPLE = "👥"
    PERSON_CHECK = "👤"
    PERSON_CROSS = "👤"
    FILE = "📁"
    SMILE = "🙂"
    CHART_UP = "📊"
    STATS = "📊"
    HOUSE = "🏘"
    LOCK = "🔒"
    UNLOCK = "🔓"
    MEGAPHONE = "📣"
    CHECK = "✅"
    CROSS = "❌"
    PENCIL = "🖋"
    TRASH = "🗑"
    POINT_DOWN = "📰"
    SEARCH = "📰"
    PAPERCLIP = "📎"
    LINK = "🔗"
    INFO = "ℹ️"
    BOT = "🤖"
    EYE = "👁"
    EYE_OFF = "👁"
    SEND = "⬆️"
    DOWNLOAD = "⬇️"
    BELL = "🔔"
    GIFT = "🎁"
    CLOCK = "⏰"
    CONFETTI = "🎉"
    TEXT = "🔗"
    EDIT = "✍️"
    MEDIA = "🖼"
    LOCATION = "📍"
    WALLET = "👛"
    BOX = "📦"
    CRYPTO = "👾"
    CALENDAR = "📅"
    TAG = "🏷"
    TIME_PAST = "🕓"
    APPS = "📦"
    BRUSH = "🖌"
    ADD_TEXT = "🔡"
    RESIZE = "↔️"
    MONEY = "🪙"
    MONEY_SEND = "🪙"
    MONEY_RECEIVE = "🪙"
    CODE = "🔨"
    LOADING = "🔄"


def msg(emoji_id: int | str, text: str) -> str:
    """Render ``text`` with a leading premium emoji in HTML message markup."""
    value = _str_id(emoji_id)
    if len(value) != 19 or not value.isdigit():
        raise ValueError("invalid premium emoji id")
    return (
        f'<tg-emoji emoji-id="{value}">{_glyph_for(value)}</tg-emoji> '
        f"<b>{escape(text)}</b>"
    )


def plain(emoji_id: int | str, text: str) -> str:
    """Render ``text`` with a leading plain (fallback) emoji; no markup."""
    return f"{_glyph_for(emoji_id)} {text}"


def glyph(emoji_id: int | str) -> str:
    return _glyph_for(emoji_id)


def icon_id(emoji_id: str) -> int | None:
    """Return the integer emoji id for use as a Telethon button icon."""
    if emoji_id is None:
        return None
    return int(emoji_id)


def _glyph_for(emoji_id: int | str) -> str:
    target = _normalize(emoji_id)
    for name, value in vars(EMOJI).items():
        if _normalize(value) == target:
            return getattr(GLYPH, name)
    raise ValueError("unknown premium emoji id")


def _str_id(emoji_id: int | str) -> str:
    if isinstance(emoji_id, int):
        return str(emoji_id)
    return emoji_id


def _normalize(emoji_id: int | str) -> str:
    return _str_id(emoji_id).strip()