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
from io import BytesIO
from datetime import datetime

from pynepcord import SHARP_API
from pynepcord.models import SharpEntry
from pynepcord.errors import UserNotFound
from pynepcord.errors import Unauthorized


class SharpSession:
    """Create a new NeppedCord Sharp session.

    Is in development!!!

    Parameters
    ----------
    api_key : str
        NeppedAPI key to access their service.

    Methods
    -------
    check(user_id: int)
        Check if given user is in Sharp Database.
    """
    def __init__(self, api_key):
        """Init a new sharp session for NeppedCord API.

        Parameters
        ----------
        api_key : str
            API key for NeppedCord API.
        """
        self.api_key = api_key


    def check(self, user_id: int) -> SharpEntry:
        """Check if given user is in Sharp Database.

        Is in development!!!

        Parameters
        ----------
        user_id : int
            Target discord user id.

        Returns
        -------
        pynepcord.models.SharpEntry
            Object that contains data about given user from Sharp.

        Raises
        ------
        pynepcord.errors.UserNotFound
            Raises when given user wasn't found in Sharp Database.
        pynepcord.errors.Unauthorized
            Raises when API key is incorrect.
        """
        raise NotImplementedError("Sharp API isn't completed.")


    def ban(self, user_id: int, reason: str=None, image: str=None) -> bool:
        """Add user to the Sharp Database.

        Parameters
        ----------
        user_id : int
            Target discord user id.
        reason : str
            Ban reason.
        image : str
            URL or Base64-encoded image data.

        Returns
        -------
        True
            If user added to Sharp successfully.
        False
            If everything is OK, but service respond with False.

        Raises
        ------
        pynepcord.errors.Unauthorized
            Raises when API key is incorrect.
        pynepcord.errors.Forbidden
            Raises when you have no permissions to add users.
        pynepcord.errors.Unprocessable
            Raises when current user already exist in Sharp.
        """
        raise NotImplementedError("Sharp API isn't completed.")


    def unban(self, user_id: int) -> bool:
        """Add user to the Sharp Database.

        Parameters
        ----------
        user_id : int
            Target discord user id.

        Returns
        -------
        True
            If user added to Sharp successfully.
        False
            If everything is OK, but service respond with False.

        Raises
        ------
        pynepcord.errors.Unauthorized
            Raises when API key is incorrect.
        pynepcord.errors.Forbidden
            Raises when you have no permissions to add users.
        """
        raise NotImplementedError("Sharp API isn't completed.")
