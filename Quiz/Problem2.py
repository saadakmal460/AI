inventory = {
    'item1':10,
    'item2':20,
}

operations = [
    ("add" , "item1" , 5),
    ("remove" , "item2" , 10),
    ("check" , "item1"),
    ("remove" , "item3" , 5)
]

def manage_inventory(inventory , operations):
    
    for i in operations:
        
        action  = i[0]
        
        if action == 'add':
            prev_cost = inventory[i[1]]
            inventory[i[1]] = prev_cost + i[2]
        if action == 'remove':
            if i[1] not in inventory:
                print(f'The operation {action} can not be performed on {i[1]}')
            else:
                prev_cost = inventory[i[1]]
                if prev_cost - i[2] >= 0:
                    inventory[i[1]] = prev_cost - i[2]
                
        if action == 'check':
            print(f'Quantity is : {inventory[i[1]]}')
            
    return inventory
                

        
finally_inventory = manage_inventory(inventory , operations)        
print(finally_inventory)