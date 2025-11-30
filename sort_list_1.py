#Definierar listan cars och experimenterar med sortering
cars = ['bmw', 'audi', 'volvo', 'toyota', 'volkswagen', 'ford']
print("Here is the original list:")
print(cars)

print("\nAnd here is a temporarily sorted list:")
print(sorted(cars))

print("\nAnd here is the original list again:")
print(cars)

print("\nAnd here is the original list reversed:")
cars.reverse()

print("\nAnd here is the original list reversed again, so its back to normal:")
cars.reverse()
print(cars)

print(f"\nThe list contains {len(cars)} items")