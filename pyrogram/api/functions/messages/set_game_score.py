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


class SetGameScore(Object):
    """Attributes:
        ID: ``0x8ef8ecc0``

    Args:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>` or :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`
        id: ``int`` ``32-bit``
        user_id: Either :obj:`InputUserEmpty <pyrogram.api.types.InputUserEmpty>`, :obj:`InputUserSelf <pyrogram.api.types.InputUserSelf>` or :obj:`InputUser <pyrogram.api.types.InputUser>`
        score: ``int`` ``32-bit``
        edit_message (optional): ``bool``
        force (optional): ``bool``

    Raises:
        :obj:`Error <pyrogram.Error>`

    Returns:
        Either :obj:`UpdatesTooLong <pyrogram.api.types.UpdatesTooLong>`, :obj:`UpdateShortMessage <pyrogram.api.types.UpdateShortMessage>`, :obj:`UpdateShortChatMessage <pyrogram.api.types.UpdateShortChatMessage>`, :obj:`UpdateShort <pyrogram.api.types.UpdateShort>`, :obj:`UpdatesCombined <pyrogram.api.types.UpdatesCombined>`, :obj:`Update <pyrogram.api.types.Update>` or :obj:`UpdateShortSentMessage <pyrogram.api.types.UpdateShortSentMessage>`
    """

    ID = 0x8ef8ecc0

    def __init__(self, peer, id: int, user_id, score: int, edit_message: bool = None, force: bool = None):
        self.edit_message = edit_message  # flags.0?true
        self.force = force  # flags.1?true
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.user_id = user_id  # InputUser
        self.score = score  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "SetGameScore":
        flags = Int.read(b)
        
        edit_message = True if flags & (1 << 0) else False
        force = True if flags & (1 << 1) else False
        peer = Object.read(b)
        
        id = Int.read(b)
        
        user_id = Object.read(b)
        
        score = Int.read(b)
        
        return SetGameScore(peer, id, user_id, score, edit_message, force)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.edit_message is not None else 0
        flags |= (1 << 1) if self.force is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        b.write(self.user_id.write())
        
        b.write(Int(self.score))
        
        return b.getvalue()
