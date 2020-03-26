"""
    https://leetcode.com/problems/valid-parentheses/
	
	20. Valid Parentheses
	
	Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

	An input string is valid if:

	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
	Note that an empty string is also considered valid.

	Example 1:

	Input: "()"
	Output: true
	Example 2:

	Input: "()[]{}"
	Output: true
	Example 3:

	Input: "(]"
	Output: false
	Example 4:

	Input: "([)]"
	Output: false
	Example 5:

	Input: "{[]}"
	Output: true
"""

def is_valid_inplace(s):
    while '{}' in s or '[]' in s or '()' in s:
        s = s.replace('{}', '')
        s = s.replace('[]', '')
        s = s.replace('()', '')
    
    return len(s) == 0


def is_valid_use_stack(s):
    st = []
    for char in s:
        if char == '{' or char == '[' or char == '(':
            st.append(char)
        elif char == '}' or char == ']' or char == ')':
            if len(st) == 0:
                return False
            top_char = st[-1]
            if (top_char == '{' and char == '}') or (top_char == '[' and char == ']') or \
                    (top_char == '(' and char == ')'):
                st.pop()
            else:
                return False
        else:
            return False

    return len(st) == 0


if __name__ == '__main__':
    s = '{{}{[]()}}'
    print(is_valid_inplace(s))
    print(is_valid_use_stack(s))