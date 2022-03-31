from random import randint
from functools import partial

D100 = partial(randint, 0, 99)
D20 = partial(randint, 1, 20)
D12 = partial(randint, 1, 12)
D10 = partial(randint, 1, 10)
D8 = partial(randint, 1, 8)
D6 = partial(randint, 1, 6)
D4 = partial(randint, 1, 4)

__all__ = ["D100", "D20", "D12", "D10", "D8", "D6", "D4"]


