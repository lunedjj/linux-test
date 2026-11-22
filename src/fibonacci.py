def generate_fibonacci(n):
    if n < 0:
        raise ValueError("项数不能为负数")
    if n == 0:
        return []
    
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

if __name__ == "__main__":
    res = generate_fibonacci(10)
    print("斐波那契数列前 10 项:", res)
