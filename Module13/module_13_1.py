import asyncio
import time


async def start_strongman(name, power):
    balls = 5
    n = name
    if power > 6:
        p = 6
    elif power < 1:
        p = 1
    else:
        p = power
    print(f'Силач {n} начал соревнования.')
    while balls > 0:
        await asyncio.sleep(7 - p)
        print(f'Силач {n} поднял {6-balls} шар')
        balls -= 1
    print(f'Силач {n} закончил соревнования.')

async def main():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

start = time.time()
asyncio.run(main())
finish = time.time()

print (f'Working time = {round(finish-start, 2)} seconds')