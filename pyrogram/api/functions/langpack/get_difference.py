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


class GetDifference(Object):
    """Attributes:
        ID: ``0x9d51e814``

    Args:
        lang_code: ``str``
        from_version: ``int`` ``32-bit``

    Raises:
        :obj:`Error <pyrogram.Error>`

    Returns:
        :obj:`LangPackDifference <pyrogram.api.types.LangPackDifference>`
    """

    ID = 0x9d51e814

    def __init__(self, lang_code: str, from_version: int):
        self.lang_code = lang_code  # string
        self.from_version = from_version  # int

    @staticmethod
    def read(b: BytesIO, *args) -> "GetDifference":
        # No flags
        
        lang_code = String.read(b)
        
        from_version = Int.read(b)
        
        return GetDifference(lang_code, from_version)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.lang_code))
        
        b.write(Int(self.from_version))
        
        return b.getvalue()
