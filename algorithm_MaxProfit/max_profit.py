price = {5: ("T", 1500), 4: ("P", 1000), 10: ("C", 2000)}

def maximum_profit(time_units):
    profits = []
    results = []

    for build_time, (building, earning) in price.items():
        remaining = time_units
        total_profit = 0
        count = 0

        while remaining >= build_time:
            remaining -= build_time
            total_profit += remaining * earning
            count += 1

        result = {"T": 0, "P": 0, "C": 0}
        
        if remaining == 4:
            result["P"] += 1
            total_profit += 0 * 1000  
            
        result[building] = count

        profits.append(total_profit)
        results.append(result)

    return profits, results


test_case_inputs = [7, 8, 13]
for t in test_case_inputs:
    print(f"\n===== Time Unit: {t} =====")

    profits, solutions = maximum_profit(t)
    best = max(profits)

    print("Earnings: $", best)
    print("Solution:")

    idx = 1
    for p, sol in zip(profits, solutions):
        if p == best:
            print(f"{idx}. T:{sol['T']} P:{sol['P']} C:{sol['C']}")
            idx += 1
