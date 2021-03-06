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


class JsonObject(Object):
    """Attributes:
        ID: ``0x99c1d49d``

    Args:
        value: List of :obj:`JsonObjectValue <pyrogram.api.types.JsonObjectValue>`

    See Also:
        This object can be returned by :obj:`help.GetAppConfig <pyrogram.api.functions.help.GetAppConfig>`.
    """

    ID = 0x99c1d49d

    def __init__(self, value: list):
        self.value = value  # Vector<JSONObjectValue>

    @staticmethod
    def read(b: BytesIO, *args) -> "JsonObject":
        # No flags
        
        value = Object.read(b)
        
        return JsonObject(value)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.value))
        
        return b.getvalue()
