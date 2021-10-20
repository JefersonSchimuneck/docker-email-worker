import redis
import json
import os
from time import sleep
from random import randint

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    r = redis.Redis(host=redis_host, port=6379, db=0)
    print('Waiting for messages...')
    while True:
        mensagem = json.loads(r.blpop('sender')[1])
        print('Sendind message:', mensagem['assunto'])
        sleep(randint(15, 45))
        print('Message', mensagem['assunto'], 'sent')