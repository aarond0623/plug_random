import asyncio
from kasa import SmartPlug
from random import randint

# Initial delay in seconds.
DELAY = 10 * 60
# Run time min and max in seconds.
RUN_MIN = 3
RUN_MAX = 30
# Wait time min and max in seconds.
WAIT_MIN = 30
WAIT_MAX = 5 * 60

async def toggle(plug):
    if plug.is_on:
        await plug.turn_off()
    else:
        await plug.turn_on()

if __name__ == '__main__':
    plug_ip = input("Enter plug IP address: ")
    plug = SmartPlug(plug_ip)
    try:
        asyncio.run(plug.update())
    except SmartDeviceError:
        print ("Cannot communicate with plug.")
        exit()

    await plug.turn_off()
    await asyncio.sleep(DELAY)
    while True:
        run_time = randint(RUN_MIN, RUN_MAX)
        wait_time = randint(WAIT_MIN, WAIT_MAX)
        toggle(plug)
        await asyncio.sleep(run_time)
        toggle(plug)
        await asyncio.sleep(wait_time)
