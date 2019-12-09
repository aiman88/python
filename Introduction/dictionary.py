customer = {
 "name": "John Smith",
 "age": 30,
 "is_verified": True
}

print(customer["name"])

print(customer.get("birthday","Jan 1 1980"))

customer["name"] = "Jack Smith"

print(customer)