total_seconds = int(input("Enter a number of seconds: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{total_seconds} seconds is equal to {hours} hours, {minutes} minutes, and {seconds} seconds")
