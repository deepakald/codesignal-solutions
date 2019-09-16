def mathPractice(numbers):
    return functools.reduce(lambda x,y:x*numbers[y] if y%2==0 else x+numbers[y],range(len(numbers)),1)