from celery import Celery

app = Celery(
        'tpcelery',
        broker='amqp://guest:guest@127.0.0.1/',
        backend='rpc://'
)

@app.task
def addition(x, y):
    print(f'1. {x} + {y} = {x+y}')
    print(f'2. {x} + {y} = {x+y}')
    print(f'3. {x} + {y} = {x+y}')
    print(f'4. {x} + {y} = {x+y}')

    return x + y 