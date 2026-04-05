def calculate_salary(base , months):
    total  = base * months
    daily = base/30
    return total, daily
total, daily = calculate_salary(12000, 6)
print(f"Total salary for 6 months: ${total}")
print(f"daily salary is: {daily:.2f}")