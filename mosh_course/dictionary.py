customer = {
    "name": "Bob Jones",
    "age": 45,
    "is_verified": True   
}

print(customer)

print(customer["age"])
print(customer.get("Phone"))

print(customer.get("birthdate", 75))

