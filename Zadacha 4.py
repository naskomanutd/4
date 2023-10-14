def sort_numbers(numbers):
  """
  Сортира списък от числа по възходящ ред.

  Args:
    numbers: Списъкът с числа, който да се сортира.

  Returns:
    Сортираният списък с числа.
  """

  for i in range(len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
      if numbers[i] > numbers[j]:
        numbers[i], numbers[j] = numbers[j], numbers[i]
  return numbers


def main():
  """
  Точка на влизане в програмата.
  """

  numbers = [5, 2, 3, 1, 4]
  sorted_numbers = sort_numbers(numbers)
  print(f"Сортираният списък с числа е {sorted_numbers}")


if __name__ == "__main__":
  main()