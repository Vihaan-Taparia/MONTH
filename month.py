import calendar

# Display all month names
print("Months of the Year:")
for month in calendar.month_name:
    if month:  # Skip the empty string at index 0
        print(month)