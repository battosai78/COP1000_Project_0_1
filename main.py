#Initialize Array
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
#Initialize Input variable
menuSelect = None

#Present Menu
print("********************************\n"
"AutoCountry Vehicle Finder v0.1\n"
"********************************\n"
"Please Enter the following number below from the following menu:\n\n"
"1. PRINT all Authorized Vehicles\n"
"2. Exit")

menuSelect = input()

if int(menuSelect) == 1:
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
elif int(menuSelect) == 2:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")