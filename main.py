#Initialize Input variable
menuSelect = 0  
newVehicle = None
AllowedVehiclesList = None
removeVehicle = None
confirmRemove = None
#Create Functions
#Function for printing authorized vehicles
def printVehicles():
    AllowedVehiclesList = open("AllowedVehiclesList.txt","r")
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: \n")
    for vehicle in AllowedVehiclesList:
        print(vehicle)
    AllowedVehiclesList.close

#Function for searching authorized vehicles
def searchVehicles():
    AllowedVehiclesList = open("AllowedVehiclesList.txt","r")
    vehicleSearch = input("Please Enter the full Vehicle name: \n")    
    if vehicleSearch in AllowedVehiclesList:
        print(vehicleSearch + " is an authorized vehicle")
    else:
        print(vehicleSearch + " is not an authorized vehicle, if you received this in error please check the spelling and try again")
    AllowedVehiclesList.close            
#Function for adding authorized vehicles
def addVehicles():
    AllowedVehiclesList = open("AllowedVehiclesList.txt","a")
    newVehicle = input("Enter the full Vehicle name you would like to add: \n")
    AllowedVehiclesList.write("\n" + newVehicle)   
    print("You have added " + newVehicle + " as an authorized vehicle")
    AllowedVehiclesList.close
#Function for deleting authorized vehicles
def deleteVehicles():
    AllowedVehiclesList = open("AllowedVehiclesList.txt","r")
    removeVehicle = input("Enter the full Vehicle name you would like to remove: \n")
    lines = AllowedVehiclesList.readlines()
    confirmRemove = input("Are you sure you want to remove " + removeVehicle + " from the Authorized Vehicle List?\n")
    if confirmRemove == "yes":
        AllowedVehiclesList = open("AllowedVehiclesList.txt","w")
        for line in lines:
            if line != removeVehicle:
                AllowedVehiclesList.write(line)
    else:
        return
    print("You have REMOVED " + removeVehicle + " as an authorized vehicle")


while int(menuSelect) != 5:
    #Present Menu
    print("********************************\n"
    "AutoCountry Vehicle Finder v0.4\n"
    "********************************\n"
    "Please Enter the following number below from the following menu:\n\n"
    "1. PRINT all Authorized Vehicles\n"
    "2. SEARCH for Authorized Vehicle\n"
    "3. ADD Authorized Vehicle\n"
    "4. DELETE Authorized Vehicle\n"
    "5. Exit\n"
    "********************************\n")
    #Get User Input
    menuSelect = input()
    #Convert input to integer and evaluate
    if int(menuSelect) == 1:
        printVehicles()
    elif int(menuSelect) == 2:
        searchVehicles()
    elif int(menuSelect) == 3:
        addVehicles()
    elif int(menuSelect) == 4:
        deleteVehicles()
print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
exit