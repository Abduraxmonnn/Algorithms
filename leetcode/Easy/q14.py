from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]):
        strs_size = len(strs)

        if strs_size == 0:
            return ""

        prefix = strs[-1]
        if prefix == "":
            return ""
        for word in strs:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution().longestCommonPrefix(strs))

# Description od this question:
# Цикл, проверка, начинается ли текущий элемент с (prefix)
# если нет, удалите с конца prefix,
# до тех пор, пока .startswith (prefix) не будет равно True

# в ( prefix = strs[-1] ) мы начинаем проверять элементы с конца

# В контексте f.readline()[:-1]это означает: «Я почти уверен, что строка заканчивается новой строкой,
# и я хочу ее удалить».

# Когда объект является строкой, len()функция возвращает количество символов в строке.

# https://leetcode.com/problems/longest-common-prefix/
