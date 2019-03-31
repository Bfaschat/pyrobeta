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


class ReportPeer(Object):
    """Attributes:
        ID: ``0xae189d5f``

    Args:
        peer: Either :obj:`InputPeerEmpty <pyrogram.api.types.InputPeerEmpty>`, :obj:`InputPeerSelf <pyrogram.api.types.InputPeerSelf>`, :obj:`InputPeerChat <pyrogram.api.types.InputPeerChat>`, :obj:`InputPeerUser <pyrogram.api.types.InputPeerUser>` or :obj:`InputPeerChannel <pyrogram.api.types.InputPeerChannel>`
        reason: Either :obj:`InputReportReasonSpam <pyrogram.api.types.InputReportReasonSpam>`, :obj:`InputReportReasonViolence <pyrogram.api.types.InputReportReasonViolence>`, :obj:`InputReportReasonPornography <pyrogram.api.types.InputReportReasonPornography>`, :obj:`InputReportReasonChildAbuse <pyrogram.api.types.InputReportReasonChildAbuse>`, :obj:`InputReportReasonOther <pyrogram.api.types.InputReportReasonOther>` or :obj:`InputReportReasonCopyright <pyrogram.api.types.InputReportReasonCopyright>`

    Raises:
        :obj:`Error <pyrogram.Error>`

    Returns:
        ``bool``
    """

    ID = 0xae189d5f

    def __init__(self, peer, reason):
        self.peer = peer  # InputPeer
        self.reason = reason  # ReportReason

    @staticmethod
    def read(b: BytesIO, *args) -> "ReportPeer":
        # No flags
        
        peer = Object.read(b)
        
        reason = Object.read(b)
        
        return ReportPeer(peer, reason)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.reason.write())
        
        return b.getvalue()
