#! /usr/bin/python3

from time import sleep

class PrimeFinder:
    def __init__(self, limit):
        self.limit = limit
        self.primes = []
        self.index = 0
        # not very elegant, but fills self.primes
        self.get_primes()

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.primes):
            raise StopIteration()
        sleep(0.5)
        self.index += 1
        return self.primes[self.index-1]

    def search_primes(self, test_num):
        for prime in self.primes:
            if test_num % prime == 0:
                return 0
        return test_num

    def get_primes(self, start=2):
        # iterate through numbers 
        # iterate through primes for each number
        if self.primes == []:
            self.primes.append(start)

        for i in range(start+1, self.limit+1):
            check = self.search_primes(i)
            if check:
                self.primes.append(i)

    def change_limit(self, new_limit):
        old_limit = self.limit
        self.limit = new_limit
        if new_limit > old_limit:
            self.get_primes(start=old_limit)
        elif old_limit > new_limit:
            while self.primes[-1] > new_limit:
                self.primes.pop()
                print(self.primes[-1])
        else:
            pass
