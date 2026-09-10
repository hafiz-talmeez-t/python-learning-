products = {
    "milk": {"quantity": 20, "price": 120, "minimum_stock": 10},
    "bread": {"quantity": 15, "price": 80, "minimum_stock": 8},
    "eggs": {"quantity": 8, "price": 300, "minimum_stock": 12},
    "rice": {"quantity": 5, "price": 250, "minimum_stock": 10}
}
sales = {
    "milk": 7,
    "bread": 4,
    "eggs": 3,
    "rice": 8
}
reorder=set()
no_product=[]
total_revenue=0
for product,quantity in sales.items():
    if product in products:
        if quantity<=products[product]["quantity"]:
            total_revenue+=quantity*products[product]["price"]
            products[product]["quantity"]=products[product]["quantity"]-quantity
        else:
            print(f"product name: {product}\n required quantity: {quantity}\navailable quantity : {products[product]['quantity']}")
            reorder.add(product)
    else:
        no_product.append(product)
            
print("Successful-sales revenue: ",total_revenue)
remaining_value=0
for product2,info in products.items():
    remaining_value+=info["price"]*info['quantity']
    if info['quantity']<info['minimum_stock']:
        reorder.add(product2)
    
print("Remaining inventory value",remaining_value)
print("Products needing reorder: ",reorder)
print("Product dosn't exist: ",no_product)
print("Final stock : ",products)

