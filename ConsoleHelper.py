def display_list_options(device_list):
    print("AVAILABLE DEVICE LIST OPTIONS: ")
    print("These are standard devices that can be attached to the smart plug: ")
    for i, device in enumerate(device_list):
        print(i + 1, "- " + device)
