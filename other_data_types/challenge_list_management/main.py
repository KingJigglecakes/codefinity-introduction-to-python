"""
Initialize Lists:
    Create a list meat with the values: "Ham", 3.99, 50, "Sliced";
    Create a list cheese with the values: "Cheddar", 5.49, 100, "Sharp";
    Create a list condiment with the values: "Mustard", 1.99, 75, "Spicy".
"""

meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
condiment = ["Mustard", 1.99, 75, "Spicy"]

"""
Create Main List:
    Combine meat, cheese, and condiment lists into a single list called deli_dept.
Restock Item:
    If "Ham" is in the meat list and its quantity is less than 100, update its quantity to 100.
    Print the initial state of deli_dept with the message: "Initial Deli List: <$deli_dept>".
"""
if "Ham" in meat and meat[2] < 100:
    meat[2] = 100
deli_dept = [meat, cheese, condiment]
print("Initial Deli list: ", deli_dept)

"""
Add Seasonal Meat:
    Create a list seasonal_meat with the values: "Turkey", 4.50, 100, "Sliced";
    Append seasonal_meat to deli_dept.
"""

seasonal_meat = ["Turkey", 4.50, 100, "Sliced"]
deli_dept.append(seasonal_meat)

"""
Remove Condiment:
    Remove the condiment list from deli_dept.
"""

deli_dept.remove(condiment)

"""
Sort List:
    Sort deli_dept alphabetically based on the first element of each sublist using the sort() method.
"""

deli_dept.sort()

"""
After all operations, print the updated state of deli_dept with the message: "Updated Deli List: <$deli_dept>".
"""

print("Updated Deli list: ", deli_dept)