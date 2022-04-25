class LongestSubstrting:

    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [0] * 128
        print(chars)
        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]
            print("r", r, ord(r))
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                print("l", l, ord(l))
                chars[ord(l)] -= 1
                left += 1

            res = max(res, right - left + 1)
            print(f"Result: {res}", right, left)

            right += 1
        return res


if __name__ == "__main__":
    obj = LongestSubstrting()
    s = "abbcabcbb"
    print(obj.lengthOfLongestSubstring(s))
