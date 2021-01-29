# PyNepCord - NeppedAPI Python Library
PyNepCord is easy-to-use library that uses [NeppedAPI](https://api-docs.neppedcord.top). 
 
Check the `Docs` directory for getting started guide, usage examples and API reference.

# Basic usage
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from pynepcord.base import ImageSession


if __name__ == '__main__':
    key = 'your-api-token'
    session = ImageSession(key) # Create a session to get images
    image = session.get_image('happy') # get the image by the 'happy' category
    print(image.url) # display the URL of the picture in the terminal
```

# async/await
```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
from pynepcord.aio import ImageSession
# pynepcord.base - the non-async version that uses `requests`.
# pynepcord.aio - same, but uses `aiohttp` and async/await syntax.


async def main():
    key = 'your-api-token'
    session = ImageSession(key)
    image = await session.get_image('happy')
    print(image.url)

if __name__ == '__main__':
    asyncio.run(main())
```

# License

```
MIT License

Copyright (c) 2020 NellyD3v

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
