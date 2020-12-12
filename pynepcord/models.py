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


class ImageResponse:
  """Images API response."""
  def __init__(self, *args, **kwargs):
    """Init a new ImageResponse.

    Parameters
    ----------
    url: str
      Image url.
    code: int
      Status code for current API response.
    filename: str
      Given file name.
    category: str
      Requested images category.
    """
    self.url = kwargs.pop('url')
    self.code = kwargs.pop('code')
    self.filename = kwargs.pop('filename')
    self.category = kwargs.pop('category')


  def __repr__(self):
    return f"<ImageResponse[{self.code}] {self.category}/{self.filename}>"


  def __str__(self):
    return self.url


class SharpEntry:
  """Sharp API response."""
  def __init__(self, *args, **kwargs):
    """Init a new ImageResponse.

    Parameters
    ----------
    user_id: int
      Discord target user ID.
    moderator_id: int
      ID of user that added current user to the database.
    reason: str
      Ban reason.
    image: str
      Image preview.
    code: int
      Status code for current API response.
    time: datetime.datetime
      Ban date and time.
    """
    self.moderator_id = kwargs.pop('moderator_id')
    self.user_id = kwargs.pop('user_id')
    self.reason = kwargs.pop('reason')
    self.image = kwargs.pop('image')
    self.code = kwargs.pop('code')
    self.time = kwargs.pop('time')


  def __repr__(self):
    return f"<SharpEntry '{self.moderator_id}' banned '{self.user_id}' at '{self.time}'>"
