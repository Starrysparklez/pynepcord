# -*- coding: utf-8 -*-

# MIT License
#
# Copyright (c) 2020 NellyD3v
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import aiohttp
from random import choice
from asyncio.events import AbstractEventLoop

from pynepcord import CATEGORIES
from pynepcord import IMAGES_API
from pynepcord.models import ImageResponse
from pynepcord.errors import InvalidCategory
from pynepcord.errors import Unauthorized


class ImageSession:
  """Create a new async NeppedCord Image session.
  
  Uses `aiohttp` library (async).

  Methods
  -------
  :coroutine: get_image(category: str)
      Fetch image (gif-animation) from NeppedAPI Images by category.
  """
  def __init__(self, api_key, asyncio_loop: AbstractEventLoop=None):
    """Init a new image session for NeppedCord API.

    Parameters
    ----------
    api_key : str
        NeppedAPI key to access their service.
    asyncio_loop : Optional[asyncio.events.AbstractEventLoop]
        Asyncio event loop.
    """
    self.api_key = api_key
    self.session = aiohttp.ClientSession(loop=asyncio_loop)


  def __check_category(self, category: str) -> bool:
    """Check if given category is available.

    Parameters
    ----------
    category : str
        Image category that you need.

    Returns
    -------
    True
        If given category is available.
    False
        If not.
    """
    if category in CATEGORIES:
      return True
    return False


  async def get_image(self, category: str) -> ImageResponse:
    """Get image from the NeppedCord Images API. Using requests.

    :coroutine:

    Available image categories:
      baka, cry, cuddle, happy, hug, kiss, sad, wag

    Parameters
    ----------
    category : str
        Image category that you need.

    Returns
    -------
    pynepcord.models.ImageResponse
        Response with image data from the NeppedAPI.

    Raises
    ------
    pynepcord.errors.InvalidCategory
        If given category is invalid or unavailable.
    pynepcord.errors.Unauthorized
        Raises when API key is incorrect.
    """
    if category == 'random':
      category = choice(CATEGORIES)

    if not self.__check_category(category):
      raise InvalidCategory(f"Category '{category}' does not exists or unavailable.")

    async with self.session.get(IMAGES_API + category, headers={
      "Authorization": self.api_key,
      "User-Agent": "pynepcord/1.0.0"
    }) as response:
      resp_json = await response.json()

    if resp_json.get('error') and response.status == 401:
      raise Unauthorized("Your API key is incorrect. Get one at https://neppedcord.top/panel")

    resp_url = resp_json['url']
    filename = resp_url.split('/')[-1]

    return ImageResponse(url=resp_url,
                         code=response.status,
                         filename=filename,
                         category=category)
