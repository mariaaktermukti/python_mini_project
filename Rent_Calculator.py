# Input we need from user are :
#     1. total rent
#     2. total food order
#     3. Electricity units spend
#     4. Charge per Unit 
#     5. Person living in flat or hostel


# Output show you: total payment you have to pay


rent= int(input("Enter the total amount of your flat/ hostel rent = "))
food= int(input("Enter the amount of food you ordered = "))
electricity_spend= int(input("Enter the total of electricity spend = "))
charge_per_unit=int(input("Enter the charge of electricity of per unit = "))
persons=int(input("Enter the total number of person in a flat or hostel = "))


total_electricity_bill= electricity_spend * charge_per_unit

output= ( rent + food + total_electricity_bill) // persons
print("Each person will pay = ",output)