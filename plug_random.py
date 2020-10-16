import asyncio
from kasa import SmartPlug
from random import randint
from time import sleep

# Initial delay in seconds.
DELAY = 5 * 60
# Run time min and max in seconds.
RUN_MIN = 3
RUN_MAX = 30
# Wait time min and max in seconds.
WAIT_MIN = 30
WAIT_MAX = 3 * 60

def countdown(t):
    mins = t // 60
    secs = t - (mins * 60)
    for m in range(mins, -1, -1):
        for s in range(secs, -1, -1):
            print("  {:02d}:{:02d}".format(m, s), end="\r")
            sleep(1)
        secs = 59


async def main():
    plug_ip = input("Enter plug IP address: ")
    plug = SmartPlug(plug_ip)
    try:
        await plug.update()
    except:
        print ("Cannot communicate with plug.")
        exit()
    
    await plug.turn_off()
    print("Beginning countdown.")
    countdown(DELAY)
    while True:
        run_time = randint(RUN_MIN, RUN_MAX)
        wait_time = randint(WAIT_MIN, WAIT_MAX)
        await plug.turn_on()
        sleep(run_time)
        await plug.turn_off()
        sleep(wait_time)

if __name__ == '__main__':
    asyncio.run(main())
