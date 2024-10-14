employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")]
print(employee_list[0])

def get_employee(id):
    for employee in employee_list:
        if employee[0] == id:
            return {"id": employee[0], "name": employee[1], "department": employee[2]}

print(get_employee(12458))


'''
In this code, employee_list is a list of tuples. The code runs well and will return the user Paul, as its ID, 12458, is matched. The challenge comes when the list gets bigger. 

Instead of two employees, you may have 2000 or even 20,000. The code will have to iterate over the list sequentially until the number is matched. 

You could optimize the code to split the search, but even with this, it still lacks in performance in comparison to other data structures, such as the dictionary.

'''



employee_dict = {
    12345: {
        "id": "12345",
        "name": "John", 
        "department": "Kitchen"    
    },
    12458: {
        "id": "12458",
        "name": "Paul", 
        "department": "House Floor"    
    }
}

def get_employee_from_dict(id):
    return employee_dict[id]


print(get_employee_from_dict(12458))


