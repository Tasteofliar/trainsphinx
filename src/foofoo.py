import math

def numberChance(num):
    '''
    number chance function, a new way to calculate how many random number chance.

    :param int num: input your number.

    :returns: chance count.
    :rtype: int

    code example

    .. code-block:: python

        myChance = numberChance(10)
        print(myChance)

    Output

    .. code-block:: python

        13168189440000
        
    '''
    chance = math.factorial(num)*math.factorial(num)
    return chance

