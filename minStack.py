"""
问题：实现一个minStack,以及push(), pop(), top(), 和getMin()
思路：用两个stacks 一个regular，一个min,也就是python中的list啦
1. push（）的时候先把number直接加上regular，只有在min是空的时候或者新数字比min top小的时候加入min stacks
2. pop()，先把regular stack的pop出来，如果regular和min的top值相等，就把min也pop了
3. top（）就是看regular的最上一位
4. getMin()就是看min的最上一位
"""
