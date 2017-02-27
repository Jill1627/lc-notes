private static boolean isValidParen(String input) {
  if (input == null || input.length() == 0) {
    return false;
  }
  Stack<Character> stack = new Stack<>();
  for (char c : input.toCharArray()) {
    if (c == ')' && !stack.isEmpty()) {
      stack.pop();
    } else {
      stack.push(c);
    }
  }
  return stack.isEmpty();
}

private static int countValidParen(String input) {
  if (input == null || input.length() == 0) {
    return 0;
  }
  int stack = 0;
  int count = 0;
  for (char c : input.toCharArray()) {
    if (c == '(') {
      stack += 1;
    } else if (c == ')' && stack > 0) {
      stack -= 1;
      count += 1;
    }
  }
  return count;
}
