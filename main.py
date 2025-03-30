#Initialize Array
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
#Initialize Input variable
menuSelect = None

#Present Menu
print("********************************\n"
"AutoCountry Vehicle Finder v0.2\n"
"********************************\n"
"Please Enter the following number below from the following menu:\n\n"
"1. PRINT all Authorized Vehicles\n"
"2. SEARCH for Authorized Vehicle\n"
"3. Exit")

#Get User Input
menuSelect = input()

#Convert input to integer and evaluate
if int(menuSelect) == 1:
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
elif int(menuSelect) == 2:
    print("Please Enter the full Vehicle name: ")
    vehicleSearch = input()
    if vehicleSearch in AllowedVehiclesList:
        print(vehicleSearch + " is an authorized vehicle")
    else:
        print(vehicleSearch + " is not an authorized vehicle, if you received this in error please check the spelling and try again")
elif int(menuSelect) == 3:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")