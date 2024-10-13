def main():
    earnings = []
    months = int(input("Enter the number of months: "))

    for month in range(1, months + 1):
        monthly_income = float(input(f"Input income for month {month}: "))
        earnings.append(monthly_income)

    display_report(earnings)


def display_report(earnings):
    print("\nIncome Summary\n--------------")
    cumulative = 0
    for month, earning in enumerate(earnings, 1):
        cumulative += earning
        print(f"Month {month:2} - Earnings: ${earning:10.2f} Cumulative Total: ${cumulative:10.2f}")


main()
