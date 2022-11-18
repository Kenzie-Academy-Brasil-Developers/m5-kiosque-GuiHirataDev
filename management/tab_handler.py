from menu import products

def calculate_tab(dict_list):
    product = []
    for item in products:
        for item_dict in dict_list:
            if item["_id"] == item_dict["_id"]:
                product.append(item)
    product_value = []
    for prod_value in product:
        product_value.append(prod_value["price"])
    result = []
    amount = []
    for amount_dict in dict_list:
        amount.append(amount_dict["amount"])
    amount_values = len(product_value)
    for i in range(amount_values):
        result.append(product_value[i] * amount[i])
    subtotal = 0
    for count in result:
        subtotal += count
    return {"subtotal": round(subtotal, 2)} 