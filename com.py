while True:
  text = input()
  if 'q' == text:
    break
  total_length = 40
  text_length = len(text)
  padding = (total_length - text_length) // 2

  result = f"# {'-' * padding} {text} {'-' * (total_length - text_length - padding)}"

  print(result)