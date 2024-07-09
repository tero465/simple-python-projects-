import time
import pywhatkit
# List of phone numbers with country code (e.g., +1234567890)
phone_numbers = [
    "+9779841204899",
    "9779820008352",
    # Add more phone numbers here
]

# Message to be sent
message = "Hello, this is a test message sent using Python and pywhatkit!"

# Function to send messages to each phone number in the list
def send_messages():
    for number in phone_numbers:
        try:
            pywhatkit.sendwhatmsg(number, message, time.localtime().tm_hour, time.localtime().tm_min + 2)
            print(f"Message sent to {number}")
            time.sleep(10)  # Add a delay between messages to avoid rate limiting
        except Exception as e:
            print(f"Error sending message to {number}: {str(e)}")

if __name__ == "__main__":
    send_messages()