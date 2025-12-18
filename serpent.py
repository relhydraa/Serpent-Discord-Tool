import requests
import os 
import json


os.system("title Main Loader")
logo = """
\033[38;2;0;0;230m  █████████                                                    █████   
\033[38;2;0;0;255m ███░░░░░███                                                  ░░███    
\033[38;2;26;26;255m░███    ░░░   ██████  ████████  ████████   ██████  ████████   ███████  
\033[38;2;51;51;255m░░█████████  ███░░███░░███░░███░░███░░███ ███░░███░░███░░███ ░░░███░  
\033[38;2;77;77;255m ░░░░░░░░███░███████  ░███ ░░░  ░███ ░███░███████  ░███ ░███   ░███   
\033[38;2;102;102;255m ███    ░███░███░░░   ░███      ░███ ░███░███░░░   ░███ ░███   ░███ ███
\033[38;2;128;128;255m░░█████████ ░░██████  █████     ░███████ ░░██████  ████ █████  ░░█████ 
\033[38;2;153;153;255m ░░░░░░░░░   ░░░░░░  ░░░░░      ░███░░░   ░░░░░░  ░░░░ ░░░░░    ░░░░░  
\033[38;2;179;179;255m                                ░███                                   
                                █████                                  
                               ░░░░░                                  \033[38;2;255;255;255m                                      
"""

while True:
    os.system("title Serpent Discord Tool / Version: Alpha")
    os.system("cls")
    print(logo)
    print("Made by: RelHydraa")
    print("")
    print("--> [1] Webhook Manager")  # Manages multiple webhooks URLs
    print("--> [2] Webhook Info")  # Displays info about a selected webhook
    print("--> [3] Webhook Deleter")  # Deletes a selected webhook
    print("--> [4] Webhook Message Sender")  # Sends a message to a selected webhook
    print("--> [5] Webhook Spammer")  # Spams a selected webhook
    print("--> [6] Exit")
    print("")
    x = input("Option: ")

    # Load webhooks from file
    webhooks_file = "webhooks.json"
    webhooks = {}
    
    if os.path.exists(webhooks_file):
        with open(webhooks_file, 'r') as f:
            webhooks = json.load(f)
    
    if x == '1':
        os.system("cls")
        print("Webhook Manager")
        action = input("Choose an action: [1] Add Webhook [2] View Webhooks [3] Remove Webhook: ")
        
        if action == '1':
            os.system("cls")
            name = input("Enter a name for the webhook: ")
            webhook_url = input("Enter the webhook URL to add: ")
            webhooks[name] = webhook_url
            with open(webhooks_file, 'w') as f:
                json.dump(webhooks, f)
            print(f"Webhook '{name}' added successfully.")
        
        elif action == '2':
            os.system("cls")
            if webhooks:
                print("Your webhooks:")
                for i, name in enumerate(webhooks.keys(), 1):
                    print(f"{i}. {name}")
            else:
                print("No webhooks saved.")
        
        elif action == '3':
            os.system("cls")
            if webhooks:
                for i, name in enumerate(webhooks.keys(), 1):
                    print(f"{i}. {name}")
                choice = input("Enter the number of the webhook to remove: ")
                name = list(webhooks.keys())[int(choice)-1]
                del webhooks[name]
                with open(webhooks_file, 'w') as f:
                    json.dump(webhooks, f)
                print(f"Webhook '{name}' removed.")
            else:
                os.system("cls")
                print("No webhooks to remove.")
        else:
            os.system("cls")
            print("Invalid action.")

    elif x in ['2', '3', '4', '5']:
        os.system("cls")
        if not webhooks:
            os.system("cls")
            print("No webhooks saved. Please add one in Webhook Manager.")
        else:
            os.system("cls")
            print("Select a webhook:")
            for i, name in enumerate(webhooks.keys(), 1):
                print(f"{i}. {name}")
            choice = input("Enter the number: ")
            webhook_url = list(webhooks.values())[int(choice)-1]
            
            if x == '2':
                try:
                    os.system("cls")
                    response = requests.get(webhook_url)
                    if response.status_code == 200:
                        webhook_info = response.json()
                        print("Webhook Info:")
                        print(f"Name: {webhook_info.get('name', 'N/A')}")
                        print(f"ID: {webhook_info.get('id', 'N/A')}")
                        print(f"Channel ID: {webhook_info.get('channel_id', 'N/A')}")
                        print(f"Guild ID: {webhook_info.get('guild_id', 'N/A')}")
                except Exception as e:
                    os.system("cls")
                    print(f"An error occurred: {e}")
                    
            elif x == '3':
                try:
                    os.system("cls")
                    response = requests.delete(webhook_url)
                    if response.status_code == 204:
                        print("Webhook deleted successfully.")
                except Exception as e:
                    os.system("cls")
                    print(f"An error occurred: {e}")

            elif x == '4':
                os.system("cls")
                while True:
                    message = input("Enter the message to send (or press '2' to exit): ")
                    if message == '2':
                        break
                    try:
                        os.system("cls")
                        response = requests.post(webhook_url, json={"content": message})
                        if response.status_code == 204:
                            print("Message sent successfully.")
                        else:
                            print(f"Failed to send message. Status code: {response.status_code}")
                    except Exception as e:
                        os.system("cls")
                        print(f"An error occurred: {e}")

            elif x == '5':
                os.system("cls")
                message = input("Enter the message to spam: ")
                count = int(input("How many times to spam: "))
                try:
                    os.system("cls")
                    for i in range(count):
                        response = requests.post(webhook_url, json={"content": message})
                        if response.status_code != 204:
                            print(f"Failed at message {i+1}")
                            break
                    print(f"Spam completed: {count} messages sent.")
                except Exception as e:
                    os.system("cls")
                    print(f"An error occurred: {e}")

    elif x == '6':
        os.system("cls")
        break
    else:
        print("Invalid option, please try again.")
        os.system("cls")
    
    input("Press Enter to continue...")