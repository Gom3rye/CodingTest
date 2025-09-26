def count_bugs_dp(N):
    # Initialize bugs born in odd years: age 0,1,2
    odd = [1, 0, 0]  # Initially, one bug born in year 1 (odd)
    even = [0, 0, 0, 0]  # No even-year bugs yet

    for year in range(2, N + 1):
        # Step 1: Count all currently alive bugs to reproduce
        total = sum(odd) + sum(even)

        # Step 2: New bugs born
        if year % 2 == 1:  # Odd year
            new_odd0 = total
            new_even0 = 0
        else:  # Even year
            new_odd0 = 0
            new_even0 = total

        # Step 3: Age the bugs
        new_odd = [new_odd0, odd[0], odd[1]]  # age 0 -> 1, 1 -> 2, 2 -> gone
        new_even = [new_even0, even[0], even[1], even[2]]  # 0->1, 1->2, 2->3, 3->gone

        # Update states
        odd = new_odd
        even = new_even

    return sum(odd) + sum(even)

# Input & Output
N = int(input())
print(count_bugs_dp(N))
