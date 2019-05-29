order = 'water water water'
def item_order(order):
    salad = 0
    water = 0
    hamburger = 0
    i = 0
    for j in order:
        if order[i:i+5] == 'salad':
            salad = salad + 1
            i = i + 5
        elif order[i:i+5] == 'water':
              water = water + 1
              i = i + 5
        elif order[i:i+9] == 'hamburger':
              hamburger = hamburger + 1
              i = i + 9
        
        else:
            i = i + 1
        
        
    return "salad:%i hamburger:%i water:%i" %(salad, hamburger, water)
print item_order(order)