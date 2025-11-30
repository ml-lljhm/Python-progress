#Experimenterar med sortering av listor
places = ['Japan', 'Iceland', 'Norway', 'Italy', 'Hawai', 'Finland']

print(places)

print("\nHere is the list in alphabetic order")
print(sorted(places))

print("\nHere is the original list again")
print(places)

print("\nHere is the list temporarily reversed alphabetically:")
print(sorted(places, reverse=True))

print("\nAnd here it is once again in its original form:")
print(places)

print("\nHere is the list again, chronologically reversed:")
places.reverse()
print(places)

print("\n...And of course here it is in original order again:")
places.reverse()
print(places)

print("\nNow lets try to store it permanently in alphabetical order:")
places.sort()
print(places)

print("\nAnd now we permanently reverse it from alphabetical order:")
places.sort(reverse=True)
print(places)

print(f"\nMy list of countries I'd like to visit contains {len(places)} destinations!")


