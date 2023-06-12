import socket
import requests
import json

def create_shopping_item(product_no, quantity):
    # Define API endpoint
    url = "https://shoppingapiapi20230612134120.azurewebsites.net/api/ShoppingItems/"

    # Create a new ShoppingItem
    payload = {
        'productNo': product_no,
        'quantity': quantity,
        'price': 20,  # Set the price as needed
        'name': 'Hello',  # Set the name as needed
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.status_code == 201:
        created_item = response.json()
        print("ShoppingItem created successfully")
        print("ShoppingItem created successfully:")
        print("ID:", created_item['id'])
        print("Name:", created_item['name'])
        print("Quantity:", created_item['quantity'])
        print("Price:", created_item['price'])
    else:
        print(f"Failed to create ShoppingItem. Status code: {response.status_code}")


def udp_server():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the server's IP address and port number
    server_address = ('0.0.0.0', 14014)
    sock.bind(server_address)

    while True:
        print('\nWaiting to receive message')
        data, address = sock.recvfrom(4096)

        print(f"Received {len(data)} bytes from {address}")

        if data:
            message = data.decode('utf-8')
            message = message.replace("'", '"')  # Replace single quotes with double quotes for JSON
            message = json.loads(message)  # Load the JSON string into a Python dictionary
            product_no = message['productNo']
            quantity = message['sold']
            create_shopping_item(product_no, quantity)


# Run the server
udp_server()
