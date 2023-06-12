import socket
import random
import time


def send_sale_broadcast(product_no):
    # Opret en UDP-socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    # Broadcast-adresse og portnummer
    serverName = '255.255.255.255'
    port = 14014

    try:
        # Send beskeden hvert 1-3 sekunder
        while True:
            amount_sold = random.randint(1, 10)  # Generate a new random value for each broadcast
            # Lav besked i ønsket format
            message = {'productNo': product_no, 'sold': amount_sold}

            # Konverter beskeden til bytes
            data = str(message).encode('utf-8')

            # Send beskeden som broadcast
            sock.sendto(data, (serverName, port))
            print(f"Broadcasted sale: {message}")

            # Vent i 1-3 sekunder før næste salg
            time.sleep(random.randint(1, 3))
    finally:
        sock.close()

# Test eksempel
product_no = 8013
send_sale_broadcast(product_no)
