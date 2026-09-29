def reverse_string(text: str) -> str:
    """Возвращает перевернутую строку."""
    return text[::-1]
    
def get_squares_dict(n: int) -> dict:
    """Возвращает словарь, где ключи - числа от 1 до n, а значения - их квадраты."""
    return {i: i ** 2 for i in range(1, n + 1)}