import re
import math


class StringToInt:
    def my_a_to_i(self, s: str) -> int:
        # Remove leading white spaces
        # Remove leading white spaces
        s = s.strip()
        if len(s) == 0:
            return 0
        mul = 1
        if s[0] == "-":
            mul = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]
        if len(s) > 0:
            if s[0].isdigit():
                # print(re.findall(r'\d+', s)[0])
                s = re.findall(r'\d+', s)[0]
                s = mul * int(s)
                if s > (math.pow(2, 31) - 1):
                    return mul * int(math.pow(2, 31) - 1)
                elif s < -math.pow(2, 31):
                    return mul * int(math.pow(2, 31))
                return s
        return 0


if __name__ == "__main__":
    obj = StringToInt()
    inp = "-9999999999999"
    out = obj.my_a_to_i(inp)
    print(out)
