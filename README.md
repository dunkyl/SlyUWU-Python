# ![sly logo](https://raw.githubusercontent.com/dunkyl/SlyMeta/main/sly%20logo.svg) Sly UWU Random (aaS) for Python

> 🚧 **This library is an early work in progress! Breaking changes may be frequent.**

> 🐍 For Python 3.10+

## No-boilerplate, *async* and *typed* uwurandom-as-a-service access. 😸

```shell
pip install slyuwu
```

---

Example usage:

```python
import asyncio
from SlyUWU import *

async def main():

    uwurand = await UWURandom()

    random = await uwurand.of_length(20)

    print(random) # :3 AAAAAAAAAAA gajhu
    assert len(random) == 20
    
asyncio.run(main())
```
