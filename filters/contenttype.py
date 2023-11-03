from aiogram import types
from aiogram.filters import BaseFilter


class ContentTypeFilter(BaseFilter):
    key = 'custom_content_type'

    def __init__(self, custom_content_type):
        self.custom_content_type = custom_content_type

    async def check(self, message: types.Message):
        # Check if the message has the specified custom content type
        return message.content_type == self.custom_content_type
