# PyNepCord Images Examples

### Random image by category
Available categories:
`baka`, `cry`, `cuddle`, `dance`, `happy`, `hug`, `kiss`, `pat`, `poke`, `sad`, `smug`, `wag`
 
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

### Random image by ... random category?

```python
#!/usr/bin/python
# -*- coding: utf-8 -*-

from pynepcord.base import ImageSession


if __name__ == '__main__':
    key = 'your-api-token'
    session = ImageSession(key)
    image = session.get_image('random') # if you specify a 'random' category, it will be selected at random
    print(image.url) # display the URL of the picture in the terminal
    print(image.category) # display the category name
```

### async/await variant
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

# PyNepCord Sharp Examples
Nope! :klass:
The Sharp API is not yet ready, so any of the SharpSession methods will throw a `NotImplementedError` exception.
