city_map = {
    'Warehouse' :{'A':5 , 'B':10},
    'A' : {'Warehouse':5 , 'C':15},
    'B' : {'Warehouse':10 , 'C':20},
    'C' : {'A':15 , 'B':20}
}

delivery_points = ['A' , 'B']

# a = delivery_points.pop(0)
# b = city_map.get(a,[])
# for i in b:
#     print(i)

def delivery_route(city_map , delivery_points):
    path = []
    wareHouse = 'Warehouse'
    path.append('Warehouse')
    while delivery_points:
        print(wareHouse)
        neighbors = city_map.get(wareHouse,[])
        cost =  0
        for i  in neighbors:
            if neighbors[i] < cost:
                path.append(i)
                cost = cost + neighbors[i]
                a = delivery_points.pop(0)
                wareHouse = a
                break                
                
            
    return path,cost
        
        
         
    
p = delivery_route(city_map , delivery_points)       
print(p)    
           