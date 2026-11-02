
number_of_shows = int(input("Enter number of shows: "))

booked_seats_total = 0
available_seats_total = 0
high_demand_count = 0
highest_occupancy = -1
highest_show = ""

for i in range(number_of_shows):

    show_name = input("Enter the Show Name: ")
    total_seats = int(input("Total Seats: "))
    booked_seats = int(input("Booked Seats: "))

    available_seats = total_seats - booked_seats
    occupancy_percentage = (booked_seats / total_seats) * 100

    if occupancy_percentage >= 80:
        category = "House Full"
    elif occupancy_percentage >= 60:
        category = "High Demand"
    elif occupancy_percentage >= 40:
        category = "Moderate"
    else:
        category = "Low Demand"

    print(f"{show_name} - Available: {available_seats} - Occupancy: {occupancy_percentage:.2f} % - {category}")

    booked_seats_total = booked_seats_total + booked_seats
    available_seats_total = available_seats_total + available_seats

    if category == "High Demand" or category == "House Full":
        high_demand_count = high_demand_count + 1

    if occupancy_percentage > highest_occupancy:
        highest_occupancy = occupancy_percentage
        highest_show = show_name

print()
print(f"Highest Occupancy: {highest_show}")
print(f"Total Booked Seats: {booked_seats_total}")
print(f"Total Available Seats: {available_seats_total}")
print(f"High Demand/House Full Shows: {high_demand_count}")
