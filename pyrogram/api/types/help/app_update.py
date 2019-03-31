# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2019 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.api.core import *


class AppUpdate(Object):
    """Attributes:
        ID: ``0x1da7158f``

    Args:
        id: ``int`` ``32-bit``
        version: ``str``
        text: ``str``
        entities: List of either :obj:`MessageEntityUnknown <pyrogram.api.types.MessageEntityUnknown>`, :obj:`MessageEntityMention <pyrogram.api.types.MessageEntityMention>`, :obj:`MessageEntityHashtag <pyrogram.api.types.MessageEntityHashtag>`, :obj:`MessageEntityBotCommand <pyrogram.api.types.MessageEntityBotCommand>`, :obj:`MessageEntityUrl <pyrogram.api.types.MessageEntityUrl>`, :obj:`MessageEntityEmail <pyrogram.api.types.MessageEntityEmail>`, :obj:`MessageEntityBold <pyrogram.api.types.MessageEntityBold>`, :obj:`MessageEntityItalic <pyrogram.api.types.MessageEntityItalic>`, :obj:`MessageEntityCode <pyrogram.api.types.MessageEntityCode>`, :obj:`MessageEntityPre <pyrogram.api.types.MessageEntityPre>`, :obj:`MessageEntityTextUrl <pyrogram.api.types.MessageEntityTextUrl>`, :obj:`MessageEntityMentionName <pyrogram.api.types.MessageEntityMentionName>`, :obj:`InputMessageEntityMentionName <pyrogram.api.types.InputMessageEntityMentionName>`, :obj:`MessageEntityPhone <pyrogram.api.types.MessageEntityPhone>` or :obj:`MessageEntityCashtag <pyrogram.api.types.MessageEntityCashtag>`
        popup (optional): ``bool``
        document (optional): Either :obj:`DocumentEmpty <pyrogram.api.types.DocumentEmpty>` or :obj:`Document <pyrogram.api.types.Document>`
        url (optional): ``str``

    See Also:
        This object can be returned by :obj:`help.GetAppUpdate <pyrogram.api.functions.help.GetAppUpdate>`.
    """

    ID = 0x1da7158f

    def __init__(self, id: int, version: str, text: str, entities: list, popup: bool = None, document=None, url: str = None):
        self.popup = popup  # flags.0?true
        self.id = id  # int
        self.version = version  # string
        self.text = text  # string
        self.entities = entities  # Vector<MessageEntity>
        self.document = document  # flags.1?Document
        self.url = url  # flags.2?string

    @staticmethod
    def read(b: BytesIO, *args) -> "AppUpdate":
        flags = Int.read(b)
        
        popup = True if flags & (1 << 0) else False
        id = Int.read(b)
        
        version = String.read(b)
        
        text = String.read(b)
        
        entities = Object.read(b)
        
        document = Object.read(b) if flags & (1 << 1) else None
        
        url = String.read(b) if flags & (1 << 2) else None
        return AppUpdate(id, version, text, entities, popup, document, url)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.popup is not None else 0
        flags |= (1 << 1) if self.document is not None else 0
        flags |= (1 << 2) if self.url is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        b.write(String(self.version))
        
        b.write(String(self.text))
        
        b.write(Vector(self.entities))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        return b.getvalue()
