def display_list_options():
    print("AVAILABLE DEVICE LIST OPTIONS: ")
    print("These are standard devices that can be attached to the smart plug: ")
    device_list = ["Lamp", "TV", "Computer", "Phone Recharger", "Heater"]
    for i, device in enumerate(device_list):
        device_id = i + 1
        print(device_id, "- " + device)
