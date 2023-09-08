def check_cost(cost: int):
    discount = 0
    if cost > 1000:
        discount = 0.1 * cost
    elif cost > 500:
        discount = 0.05 * cost
    elif cost > 100:
        discount = 0.03 * cost
    
    return cost-discount

def check_len(vari: str):
    return None if len(vari) == 0 else vari

print(check_cost(2000))
print(check_len('String'))
