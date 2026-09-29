def reverse_string(text: str) -> str:
    """Возвращает перевернутую строку."""
    return text[::-1]

def get_squares_dict(n: int) -> dict:
    """Возвращает словарь, где ключи - числа от 1 до n, а значения - их квадраты."""
    return {i: i ** 2 for i in range(1, n + 1)}

def get_gcd(a: int, b: int) -> int:
    """Находит наибольший общий делитель (НОД) двух чисел."""
    while b != 0:
        a, b = b, a % b
    return a

def binary_search(arr: list, target: int) -> int:
    """Выполняет бинарный поиск в отсортированном списке. Возвращает индекс или -1."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return -1