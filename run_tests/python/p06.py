def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

test_values = [0, 100, -40, 37]
for c in test_values:
    f = celsius_to_fahrenheit(c)
    print(f"{c}°C = {f:.2f}°F")
