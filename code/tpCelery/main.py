from tpcelery.celery import addition
import time
import random

if __name__ == '__main__':

    while(True):
        nombre1 = random.randint(1,100)
        nombre2 = random.randint(1,100)
        time.sleep(0.1)
        addition.delay(nombre1, nombre2)

    # while(True):
    #     time.sleep(0.4)
    #     if task.ready():
    #         print(task.result)
    #     else:
    #         print('Resultat pas pret')


    


