import asyncio
from kasa import SmartPlug
from random import randint
import time

# Initial delay in seconds.
DELAY = 10 * 60
# Run time min and max in seconds.
RUN_MIN = 3
RUN_MAX = 30
# Wait time min and max in seconds.
WAIT_MIN = 30
WAIT_MAX = 5 * 60

async def main():
    plug_ip = input("Enter plug IP address: ")
    plug = SmartPlug(plug_ip)
    try:
        await plug.update()
    except:
        print ("Cannot communicate with plug.")
        exit()
    
    await plug.turn_off()
    time.sleep(DELAY)
    while True:
        run_time = randint(RUN_MIN, RUN_MAX)
        wait_time = randint(WAIT_MIN, WAIT_MAX)
        await plug.turn_on()
        time.sleep(run_time)
        await plug.turn_off()
        time.sleep(wait_time)

if __name__ == '__main__':
    asyncio.run(main())
