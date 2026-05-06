# Storing Location in Different tuples

panipat = ('29.3909', '76.9635')
delhi = ('28.7041', '77.1025')
chandigarh = ('30.7333', '76.7794')

# Combining Tuples

locations = (('29.3909', '76.9635'), ('28.7041', '77.1025'), ('30.7333', '76.7794'))


# Print Latitute and Longitudes

print('Panipat Latitude:', panipat[0])
print('Panipat Longitude:', panipat[1])
print('Delhi Latitude:', delhi[0])
print('Delhi Longitude:', delhi[1])
print('Chandigarh Latitude:', chandigarh[0])
print('Chandigarh Longitude:', chandigarh[1])


# Print Combined Tuples

print("\nCombined Tuple Printing\n")

print(locations)
print("First nested tuple:", locations[0])
print("First nested latitude:", locations[0][0])
print("First nested longitude:", locations[0][1])