from functools import reduce
products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":240,"stock":10},
    {"item_name":"bournvita","mrp":320,"stock":20},
    {"item_name":"horlicks","mrp":280,"stock":13},
    {"item_name":"nutricharge","mrp":275,"stock":0},
]

#to print all the product names

product=list(map(lambda product:product["item_name"],products))
print(product)

#ptint the out of stock product details

out_of_stock=list(filter(lambda product:product["stock"]==0,products))
print(out_of_stock)

#print all product details available below <250

pr=list(filter(lambda product:product["mrp"]<250,products))
print(pr)

#highest cost
prices=list(map(lambda p1:p1["mrp"],products))
#prices=max(list(map(lambda p1:p1["mrp"],products)))
print(prices)

high=reduce(lambda p1,p2:p1 if p1>p2 else p2,prices)
print(high)