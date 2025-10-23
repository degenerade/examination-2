"""histogram module"""

from collections import Counter
from typing import Dict, Iterable


class Histogram:
    """
    this is a histogram of integer roll values.

        h = Histogram()
        h.add(roll)
        h.add_many([1,2,3])
        print(h.as_freq())
    """

    def __init__(self):
        self.counter = Counter()
        self.total = 0

    def add(self, value: int) -> None:
        self.counter[value] += 1
        self.total += 1

    def add_many(self, values: Iterable[int]) -> None:
        for v in values:
            self.add(v)

    def as_freq(self) -> Dict[int, float]:
        """return frequency (0..1) per face value."""
        if self.total == 0:
            return {}
        return {k: v / self.total for k, v in sorted(self.counter.items())}

    def most_common(self, n: int = 5):
        return self.counter.most_common(n)

    def reset(self) -> None:
        self.counter.clear()
        self.total = 0
