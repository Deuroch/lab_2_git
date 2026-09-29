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

def bubble_sort(arr: list) -> list:
    """Сортирует список методом пузырька."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

if __name__ == "__main__":
    # Блок для проверки работы функций
    print("Переворот строки:", reverse_string("Привет, Git!"))
    print("Словарь квадратов (до 5):", get_squares_dict(5))
    print("НОД 48 и 18:", get_gcd(48, 18))
    
    test_list = [64, 34, 25, 12, 22, 11, 90]
    sorted_list = bubble_sort(test_list.copy())
    print("Сортировка пузырьком:", sorted_list)
    print("Бинарный поиск числа 25:", binary_search(sorted_list, 25))