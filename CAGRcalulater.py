def calculate_cagr(beginning_value, ending_value, years):
    if beginning_value <= 0 or years <= 0:
        raise ValueError("Beginning value and years must be greater than 0.")
    
    cagr = (ending_value / beginning_value) ** (1 / years) - 1
    return cagr * 100  # Return as percentage

# Take user input
try:
    start_value = float(input("Enter the beginning value: "))
    end_value = float(input("Enter the ending value: "))
    time_period = float(input("Enter the number of years: "))

    cagr_result = calculate_cagr(start_value, end_value, time_period)
    print(f"CAGR: {cagr_result:.2f}%")

except ValueError as e:
    print(f"Error: {e}")
