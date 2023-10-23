import time

def fizzBuzz(size):
    results = []

    for num in range(1, size+1):
        if (num % 3 == 0) and (num % 5 == 0) : results.append("FizzBuzz")
        else:
            if num % 3 == 0 :
                results.append("Fizz")
            elif num % 5 == 0 :
                results.append("Buzz")
            else :
                results.append(str(num))
    
    return results


def fizzBuzz2(size):
    results = []

    for num in range(1, size+1):
        if (num % 3 == 0) and (num % 5 == 0) : results.append("FizzBuzz")
        else:
            results.append('Fizz' if num % 3 == 0 else 'Buzz' if(num % 3 == 0 or num % 5 == 0) else str(num))

    return results

def fizzBuzz3(size):
    results = []

    for num in range(1, size+1):
        if num % 3 == 0 and num % 5 != 0:
            results.append("Fizz")
        elif num % 5 == 0 and num % 3 != 0:
            results.append("Buzz")
        elif num % 3 != 0 and num % 5 != 0:
            results.append(str(num))
        else :
            results.append("FizzBuzz")

    return results

def fizzBuzz4(size):
    results = []

    for num in range(1, size+1):
        if num % 3 != 0 and num % 5 != 0:
            results.append(str(num))
        elif num % 3 == 0 and num % 5 != 0:
            results.append("Fizz")
        elif num % 5 == 0 and num % 3 != 0:
            results.append("Buzz")
        else :
            results.append("FizzBuzz")

    return results

def fizzBuzz5(size):
    results = []

    for num in range(1, size+1):
        if num % 3 != 0 and num % 5 != 0:
            if num % 5 != 0 : results.append(str(num))
            elif num % 5 == 0 : results.append("Buzz")
        elif num % 3 == 0 and num % 5 != 0:
            results.append("Fizz")
        else :
            results.append("FizzBuzz")

    return results


times = []
for _ in [ fizzBuzz, fizzBuzz2, fizzBuzz3, fizzBuzz4, fizzBuzz5 ] :
    avg = 0
    itr = 10000
    for a in range(itr):
        start = time.perf_counter()
        _(150)
        end = time.perf_counter()
        avg += end-start

    times.append[( avg )]
    print(str(_.__name__) + ": " + str(avg/itr))

times.sort()
print(str(_.__name__) + ": " + str(avg/itr))