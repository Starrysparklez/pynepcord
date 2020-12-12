# Table of Contents

* [pynepcord](#pynepcord)
* [pynepcord.errors](#pynepcord.errors)
  * [NepuError](#pynepcord.errors.NepuError)
  * [InvalidCategory](#pynepcord.errors.InvalidCategory)
  * [UserNotFound](#pynepcord.errors.UserNotFound)
  * [Unauthorized](#pynepcord.errors.Unauthorized)
* [pynepcord.models](#pynepcord.models)
  * [ImageResponse](#pynepcord.models.ImageResponse)
    * [\_\_init\_\_](#pynepcord.models.ImageResponse.__init__)
  * [SharpEntry](#pynepcord.models.SharpEntry)
    * [\_\_init\_\_](#pynepcord.models.SharpEntry.__init__)
* [pynepcord.\_\_main\_\_](#pynepcord.__main__)
* [pynepcord.base](#pynepcord.base)
* [pynepcord.base.images](#pynepcord.base.images)
  * [ImageSession](#pynepcord.base.images.ImageSession)
    * [\_\_init\_\_](#pynepcord.base.images.ImageSession.__init__)
    * [get\_image](#pynepcord.base.images.ImageSession.get_image)
* [pynepcord.base.sharp](#pynepcord.base.sharp)
  * [SharpSession](#pynepcord.base.sharp.SharpSession)
    * [\_\_init\_\_](#pynepcord.base.sharp.SharpSession.__init__)
    * [check](#pynepcord.base.sharp.SharpSession.check)
    * [ban](#pynepcord.base.sharp.SharpSession.ban)
    * [unban](#pynepcord.base.sharp.SharpSession.unban)
* [pynepcord.aio](#pynepcord.aio)
* [pynepcord.aio.images](#pynepcord.aio.images)
  * [ImageSession](#pynepcord.aio.images.ImageSession)
    * [\_\_init\_\_](#pynepcord.aio.images.ImageSession.__init__)
    * [get\_image](#pynepcord.aio.images.ImageSession.get_image)
* [pynepcord.aio.sharp](#pynepcord.aio.sharp)
  * [SharpSession](#pynepcord.aio.sharp.SharpSession)
    * [\_\_init\_\_](#pynepcord.aio.sharp.SharpSession.__init__)
    * [check](#pynepcord.aio.sharp.SharpSession.check)
    * [ban](#pynepcord.aio.sharp.SharpSession.ban)
    * [unban](#pynepcord.aio.sharp.SharpSession.unban)

<a name="pynepcord"></a>
# pynepcord

<a name="pynepcord.errors"></a>
# pynepcord.errors

<a name="pynepcord.errors.NepuError"></a>
## NepuError Objects

```python
class NepuError(BaseException)
```

Base exception class that represents pynepcord errors.

<a name="pynepcord.errors.InvalidCategory"></a>
## InvalidCategory Objects

```python
class InvalidCategory(NepuError)
```

Exception that raises when given invalid image category.

<a name="pynepcord.errors.UserNotFound"></a>
## UserNotFound Objects

```python
class UserNotFound(NepuError)
```

Exception that raises when given user wasn't found.

<a name="pynepcord.errors.Unauthorized"></a>
## Unauthorized Objects

```python
class Unauthorized(NepuError)
```

Exception that raises when given API key is incorrect.

<a name="pynepcord.models"></a>
# pynepcord.models

<a name="pynepcord.models.ImageResponse"></a>
## ImageResponse Objects

```python
class ImageResponse()
```

Images API response.

<a name="pynepcord.models.ImageResponse.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(*args, **kwargs)
```

Init a new ImageResponse.

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

<a name="pynepcord.models.SharpEntry"></a>
## SharpEntry Objects

```python
class SharpEntry()
```

Sharp API response.

<a name="pynepcord.models.SharpEntry.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(*args, **kwargs)
```

Init a new ImageResponse.

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

<a name="pynepcord.__main__"></a>
# pynepcord.\_\_main\_\_

<a name="pynepcord.base"></a>
# pynepcord.base

<a name="pynepcord.base.images"></a>
# pynepcord.base.images

<a name="pynepcord.base.images.ImageSession"></a>
## ImageSession Objects

```python
class ImageSession()
```

Create a new NeppedCord Image session.

Uses `requests` library (non-async).

Methods
-------
get_image(category: str)
    Fetch image (gif-animation) from NeppedAPI Images by category.

<a name="pynepcord.base.images.ImageSession.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(api_key)
```

Init a new Image session for NeppedCord API

Parameters
----------
api_key : str
    NeppedAPI key to access their service.

<a name="pynepcord.base.images.ImageSession.get_image"></a>
#### get\_image

```python
 | get_image(category: str) -> ImageResponse
```

Get image from the NeppedCord Images API. Using requests.

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

<a name="pynepcord.base.sharp"></a>
# pynepcord.base.sharp

<a name="pynepcord.base.sharp.SharpSession"></a>
## SharpSession Objects

```python
class SharpSession()
```

Create a new NeppedCord Sharp session.

Is in development!!!

Parameters
----------
api_key : str
    NeppedAPI key to access their service.

Methods
-------
check(user_id: int)
    Check if given user is in Sharp Database.

<a name="pynepcord.base.sharp.SharpSession.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(api_key)
```

Init a new sharp session for NeppedCord API.

Parameters
----------
api_key : str
    API key for NeppedCord API.

<a name="pynepcord.base.sharp.SharpSession.check"></a>
#### check

```python
 | check(user_id: int) -> SharpEntry
```

Check if given user is in Sharp Database.

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

<a name="pynepcord.base.sharp.SharpSession.ban"></a>
#### ban

```python
 | ban(user_id: int, reason: str = None, image: str = None) -> bool
```

Add user to the Sharp Database.

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

<a name="pynepcord.base.sharp.SharpSession.unban"></a>
#### unban

```python
 | unban(user_id: int) -> bool
```

Add user to the Sharp Database.

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

<a name="pynepcord.aio"></a>
# pynepcord.aio

<a name="pynepcord.aio.images"></a>
# pynepcord.aio.images

<a name="pynepcord.aio.images.ImageSession"></a>
## ImageSession Objects

```python
class ImageSession()
```

Create a new async NeppedCord Image session.

Uses `aiohttp` library (async).

Methods
-------
:coroutine: get_image(category: str)
    Fetch image (gif-animation) from NeppedAPI Images by category.

<a name="pynepcord.aio.images.ImageSession.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(api_key, asyncio_loop: AbstractEventLoop = None)
```

Init a new image session for NeppedCord API.

Parameters
----------
api_key : str
    NeppedAPI key to access their service.
asyncio_loop : Optional[asyncio.events.AbstractEventLoop]
    Asyncio event loop.

<a name="pynepcord.aio.images.ImageSession.get_image"></a>
#### get\_image

```python
 | async get_image(category: str) -> ImageResponse
```

Get image from the NeppedCord Images API. Using requests.

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

<a name="pynepcord.aio.sharp"></a>
# pynepcord.aio.sharp

<a name="pynepcord.aio.sharp.SharpSession"></a>
## SharpSession Objects

```python
class SharpSession()
```

Create a new async NeppedCord Sharp session.

Is in development!!!

Methods
-------
:coroutine: check(user_id: int)
    Check if given user is in Sharp Database.

<a name="pynepcord.aio.sharp.SharpSession.__init__"></a>
#### \_\_init\_\_

```python
 | __init__(api_key, asyncio_loop: AbstractEventLoop = None)
```

Init a new sharp session for NeppedCord API.

Is in development!!!

Parameters
----------
api_key : str
    NeppedAPI key to access their service.
asyncio_loop : Optional[asyncio.events.AbstractEventLoop]
    Asyncio event loop.

<a name="pynepcord.aio.sharp.SharpSession.check"></a>
#### check

```python
 | async check(user_id: int) -> SharpEntry
```

Check if given user is in Sharp Database.

Is in development!!!
:coroutine:

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

<a name="pynepcord.aio.sharp.SharpSession.ban"></a>
#### ban

```python
 | ban(user_id: int, reason: str = None, image: str = None) -> bool
```

Add user to the Sharp Database.

:coroutine:

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

<a name="pynepcord.aio.sharp.SharpSession.unban"></a>
#### unban

```python
 | unban(user_id: int) -> bool
```

Add user to the Sharp Database.

:coroutine:

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

