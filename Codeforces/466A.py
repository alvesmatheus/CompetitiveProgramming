# @author Matheus Alves dos Santos

rides, pack_size, single_price, pack_price = list(map(int, input().split()))
useful_pack = (pack_price <= (pack_size * single_price))

if (useful_pack):
    hibrid_cost = (rides // pack_size) * pack_price
    hibrid_cost += (rides % pack_size) * single_price

    pack_cost = (rides // pack_size) * pack_price
    if ((rides % pack_size) != 0):
        pack_cost += pack_price        
    
    cost = min(hibrid_cost, pack_cost)
else:
    cost = single_price * rides

print(cost)