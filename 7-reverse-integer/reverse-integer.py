class Solution:
    int_size = 2**31

    def reverse(self, x: int) -> int:
        l = [*f"{ x }"]
        l = l[1:] if x < 0 else l
        l.reverse()
        s = "".join(l)
        s = int(s) if x > 0 else -int(s)
        s = s if s < self.int_size and s > -self.int_size else 0
        return s
