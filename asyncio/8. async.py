# import requests
# from time import time
#
#
# def get_file(url):
#
#     r = requests.get(url)
#     return r
#
#
# def write_file(response):
#     filename = response.url.split('/')[-1]
#     with open(filename, 'wb') as file:
#         file.write(response.content)
#
#
# def main():
#
#     t0 = time()
#     url = 'http://loremflickr.com/320/240'
#
#     for i in range(10):
#         write_file(get_file(url))
#
#     print(time() - t0)
#
#
# if __name__ == '__main__':
#     main()
#

##########

import asyncio
from time import time

import aiohttp


def write_image(data):

    filename = 'file-{}.jpg'.format(int(time() * 1000))
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch_content(url, session):

    async with session.get(url) as response:
        data = await response.read()
        write_image(data)


async def main():

    url = 'http://loremflickr.com/320/240'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(10):
            tasks.append(asyncio.create_task(fetch_content(url, session)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':

    t0 = time()
    asyncio.run(main())
    print('time have passed', time() - t0)
