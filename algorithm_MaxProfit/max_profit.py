price = {5: ("T", 1500), 4: ("P", 1000), 10: ("C", 2000)}

def maximum_profit(time_units):
    profits = []
    results = []

    max_counts = {bt: time_units // bt for bt in price}

    for t_count in range(max_counts[5] + 1):
        for p_count in range(max_counts[4] + 1):
            for c_count in range(max_counts[10] + 1):
                if t_count == p_count == c_count == 0:
                    continue
                build_list = [5] * t_count + [4] * p_count + [10] * c_count  
    
                if sum(build_list) > time_units:
                    continue
                total_profit = 0
                time_used = 0
                valid = True
                for bt in build_list:
                    time_used += bt
                    remaining = time_units - time_used
                    if remaining <= 0:
                        valid = False  # Last building earns nothing — skip
                        break
                    total_profit += price[bt][1] * remaining
                if not valid:
                    continue
                profits.append(total_profit)
                results.append({"T": t_count, "P": p_count, "C": c_count})

    return profits, results


test_case_inputs = [7, 8, 13]
for t in test_case_inputs:
    print(f"\n===== Time Unit: {t} =====")
    profits, solutions = maximum_profit(t)
    best = max(profits)
    print(f"Earnings: ${best:,}")
    print("Solutions:")
    idx = 1
    seen = []
    for p, sol in zip(profits, solutions):
        if p == best and sol not in seen:
            print(f"  {idx}. T:{sol['T']} P:{sol['P']} C:{sol['C']}")
            seen.append(sol)
            idx += 1

