import concurrent.futures
import math
from concurrent.futures import ProcessPoolExecutor
from logging import StreamHandler, Formatter, INFO, getLogger


PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419,
]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def init_logger():
    handler = StreamHandler()
    handler.setLevel(INFO)
    handler.setFormatter(Formatter("[%(asctime)s] [%(threadName)s] %(message)s"))
    logger = getLogger()
    logger.addHandler(handler)
    logger.setLevel(INFO)


def main():
    init_logger()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for prime in executor.map(is_prime, PRIMES):
            # for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print("is prime: %s" % (prime))
            getLogger().info("")


if __name__ == "__main__":
    main()
