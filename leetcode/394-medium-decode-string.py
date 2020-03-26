"""

    394. Decode String

    Medium

    https://leetcode.com/problems/decode-string/

    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

    You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

    Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

    Examples:

    s = "3[a]2[bc]", return "aaabcbc".
    s = "3[a2[c]]", return "accaccacc".
    s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

"""

"""
    本题难点在于括号内嵌套括号，需要从内向外生成与拼接字符串，这与栈的先入后出特性对应。

    算法流程：

        构建辅助栈 stack， 遍历字符串 s 中每个字符 c；

        当 c 为数字时，将数字字符转化为数字 multi，用于后续倍数计算；

        当 c 为字母时，在 res 尾部添加 c；

        当 c 为 [ 时，将当前 multi 和 res 入栈，并分别置空置 00：
            记录此 [ 前的临时结果 res 至栈，用于发现对应 ] 后的拼接操作；
            记录此 [ 前的倍数 multi 至栈，用于发现对应 ] 后，获取 multi × [...] 字符串。
            进入到新 [ 后，res 和 multi 重新记录。

        当 c 为 ] 时，stack 出栈，拼接字符串 res = last_res + cur_multi * res，其中:
            last_res是上个 [ 到当前 [ 的字符串，例如 "3[a2[c]]" 中的 a；
            cur_multi是当前 [ 到 ] 内字符串的重复倍数，例如 "3[a2[c]]" 中的 2。

        返回字符串 res。

    复杂度分析：

        时间复杂度 O(N)，一次遍历 s

        空间复杂度 O(N)，辅助栈在极端情况下需要线性空间，例如 2[2[2[a]]]

"""


def decode_string(s: str):
    # 辅助栈
    stack = []
    # 用于存放临时字符串
    res = ""
    # 用于存放临时系数
    multi = 0

    for c in s:
        if c == '[':
            # 将 [ 前面的 系数、临时字符串res 入栈
            stack.append([multi, res])
            # 置空
            res, multi = "", 0
        elif c == ']':
            # 出栈
            cur_multi, last_res = stack.pop()
            # 拼接字符串
            res = last_res + cur_multi * res
        elif '0' <= c <= '9':
            # 计算系数multi, * 10 是为了计算大于10的系数
            multi = multi * 10 + int(c)
        else:
            # 将字符加到res后面
            res += c

    return res


def is_valid(s: str):
    """
        only check the following rules:
         1) the number must be followed by '['
         2) the '[' and ']' must be matched.

        Refer: https://github.com/haoel/leetcode/blob/master/algorithms/cpp/decodeString/DecodeString.cpp

    """
    stack = []
    i = 0
    while i < len(s):
        if '0' <= s[i] <= '9':
            i += 1
            while '0' <= s[i] <= '9':
                i += 1
            if s[i] != '[':
                return False
            stack.append('[')
        elif s[i] == ']':
            if stack[-1] != '[':
                return False
            stack.pop()

        i += 1

    return len(stack) == 0


if __name__ == '__main__':
    print(is_valid("3[ab2[c]2[e]]"))
    print(decode_string("3[ab2[c]2[e]]"))
