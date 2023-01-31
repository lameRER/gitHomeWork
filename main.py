import asyncio

from time import sleep
from tqdm import tqdm


async def main():
    for i in tqdm(range(10), desc='STEP 1'):
        await asyncio.sleep(.01)
        for j in tqdm(range(100), desc='STEP 2', leave=False):
            await asyncio.sleep(.01)


if __name__ == '__main__':
    asyncio.run(main())
