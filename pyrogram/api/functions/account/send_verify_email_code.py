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


class SendVerifyEmailCode(Object):
    """Attributes:
        ID: ``0x7011509f``

    Args:
        email: ``str``

    Raises:
        :obj:`Error <pyrogram.Error>`

    Returns:
        :obj:`account.SentEmailCode <pyrogram.api.types.account.SentEmailCode>`
    """

    ID = 0x7011509f

    def __init__(self, email: str):
        self.email = email  # string

    @staticmethod
    def read(b: BytesIO, *args) -> "SendVerifyEmailCode":
        # No flags
        
        email = String.read(b)
        
        return SendVerifyEmailCode(email)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.email))
        
        return b.getvalue()
