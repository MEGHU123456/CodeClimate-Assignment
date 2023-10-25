def calculate_area(length, width):
    return length * width

def calculate_perimeter(length, width):
    return 2 * (length + width)

def calculate_volume(length, width, height):
    return length * width * height

def calculate_surface_area(length, width, height):
    return 2 * (calculate_area(length, width) + calculate_area(length, height) + calculate_area(width, height))

# Reusable function for area and perimeter calculations
def calculate_area_and_perimeter(length, width):
    area = calculate_area(length, width)
    perimeter = calculate_perimeter(length, width)
    return area, perimeter
