import asyncio
import datetime

async def display_date(loop):
  end_date = loop.time() + 5
  while True:
    print(datetime.datetime.now())
    if loop.time() + 1 >= end_date:
      break
    await asyncio.sleep(3)


loop = asyncio.get_event_loop()
loop.run_until_complete(display_date(loop))
loop.close()
