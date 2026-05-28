import math

def circle_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius ** 2

try:
    radius = float(input("Enter the radius: "))
    area = circle_area(radius)
    print(f"The area of the circle with radius {radius} is: {area:.4f}")
except ValueError as e:
    print(f"Invalid input: {e}")
