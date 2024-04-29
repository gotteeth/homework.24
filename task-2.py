

def clean_up_ids(customer_ids):
    unique_ids = set(customer_ids)
    for id in unique_ids:
        print(id)
    return unique_ids


customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique_customer_ids = clean_up_ids(customer_ids)
print("unique customer IDs:", unique_customer_ids)
