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


import requests
from random import choice

from pynepcord import CATEGORIES
from pynepcord import IMAGES_API
from pynepcord.models import ImageResponse
from pynepcord.errors import InvalidCategory
from pynepcord.errors import Unauthorized


class ImageSession:
  """Create a new NeppedCord Image session.
  
  Uses `requests` library (non-async).

  Methods
  -------
  get_image(category: str)
      Fetch image (gif-animation) from NeppedAPI Images by category.
  """
  def __init__(self, api_key):
    """Init a new Image session for NeppedCord API

    Parameters
    ----------
    api_key : str
        NeppedAPI key to access their service.
    """
    self.api_key = api_key


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


  def get_image(self, category: str) -> ImageResponse:
    """Get image from the NeppedCord Images API. Using requests.

    Available image categories:
      baka, cry, cuddle, happy, hug, kiss, sad, wag

    Parameters
    ----------
    category : str
        Image category that you need.

    Raises
    ------
    pynepcord.errors.InvalidCategory
        If given category is invalid or unavailable.
    pynepcord.errors.Unauthorized
        Raises when API key is incorrect.

    Returns
    -------
    pynepcord.models.ImageResponse
        Response with image data from the NeppedAPI.
    """
    if category == 'random':
      category = choice(CATEGORIES)

    if not self.__check_category(category):
      raise InvalidCategory(f"Category '{category}' does not exists or unavailable.")

    response = requests.get(IMAGES_API + category, headers={
      "Authorization": self.api_key,
      "User-Agent": "pynepcord/1.0.0"
    })
    resp_json = response.json()

    if resp_json.get('error') and response.status_code == 401:
      raise Unauthorized("Your API key is incorrect. Get one at https://neppedcord.top/panel")

    resp_url = resp_json['url']
    filename = resp_url.split('/')[-1]

    return ImageResponse(url=resp_url,
                         code=response.status_code,
                         filename=filename,
                         category=category)
