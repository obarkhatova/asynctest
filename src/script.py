import asyncio
import hashlib
import sys

COUNT_MAX = 50
DELAY_MAX = 10


def check_params(**kwargs):
    for k in ('name', 'vacancy', 'salary', 'delay', 'count'):
        if kwargs.get(k) is None:
            raise ValueError(f'{k} is missing')
    if kwargs['count'] > COUNT_MAX:
        raise ValueError(f'Count greater than {COUNT_MAX}')
    if kwargs['delay'] > DELAY_MAX:
        raise ValueError(f'Delay greater than {DELAY_MAX}')


async def prt_info(name, vacancy, salary, **kwargs):
    print(f'{name} applies for "{vacancy}" position with expected salary {salary}')


async def delayed_task(task, delay, *args, **kwargs):
    await asyncio.sleep(delay)
    asyncio.gather(task(*args, **kwargs))


async def launch_tasks(count, delay, info):
    for i in range(count):
        await asyncio.gather(delayed_task(prt_info, delay*i, **info))


def str_to_sha256(s):
    return hashlib.sha256(s.encode()).hexdigest()


def run(**kwargs):
    check_params(**kwargs)
    info = {
        'name': kwargs['name'],
        'vacancy': kwargs['vacancy'],
        'salary': kwargs['salary'],
    }
    asyncio.run(launch_tasks(kwargs['count'], kwargs['delay'], info))
    sys.stdout.write('\nPlease type smth to finish  ')
    sys.stdout.flush()

    data = sys.stdin.readline().strip()
    data = str_to_sha256(data)
    sys.stdout.write(data)

