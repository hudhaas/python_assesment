
vehicle_type = input("[car/Bike/suv] : ")
hours = float(input("Duration : "))

vehicles = ["car", "bike", "suv"]

if vehicle_type.lower() not in vehicles:
    print("Invalid Vehicle Type")

elif hours < 0:
    print("Invalid parking duration")

else:
    if vehicle_type.lower() == "car":
        first_rate = 50
        extra_rate = 20

    elif vehicle_type.lower() == "bike":
        first_rate = 30
        extra_rate = 10

    else:
        first_rate = 70
        extra_rate = 30

    if hours < 1:
        hours = 1

    if hours <= 2:
        parking_fee = first_rate

    else:
        extra_hours = hours - 2
        parking_fee = first_rate + (extra_hours * extra_rate)

    print("=" * 30)
    print("Vehicle :", vehicle_type)
    print("Hours :", hours)
    print(f"Parking Fee : {int(parking_fee)}/-")
