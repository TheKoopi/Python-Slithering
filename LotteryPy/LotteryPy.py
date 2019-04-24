import Lotto649 as L
import LottoExample as E
import time
from multiprocessing import Pool

if __name__ == "__main__":

    pool = Pool()
    start = (time.time()*1000)
    for _i in range(0, 30):
        result1 = pool.apply_async(L.lotto649)
        result2 = pool.apply_async(E.lottoexample)

    pool.close()
    pool.join()
    end = (time.time() * 1000)
    print(f"Total time to execute: {end - start} ms")
