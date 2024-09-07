import hashlib
import os
import logging
import requests
from dotenv import load_dotenv # Import the load_dotenv function from the dotenv module

# Function to print the logo
def print_logo():
    print(r"""
 _____            _       _   _          _______        _
|  __ \          | |     | | (_)        |__   __|      | |
| |  | |___  ___ | |_   _| |_ _  ___  _ __ | | ___  ___| |__
| |  | / __|/ _ \| | | | | __| |/ _ \| '_ \| |/ _ \/ __| '_ '\
| |__| \__ \ (_) | | |_| | |_| | (_) | | | | |  __/ (__| | | |
|_____/|___/\___/|_|\__,_|\__|_|\___/|_| |_|_|\___|\___|_| |_|
                    +-+-+-+-+-+-+-+-+-+-+-+
                    |M|D|5|_|D|e|c|r|y|p|t|
                    +-+-+-+-+-+-+-+-+-+-+-+
""")

print_logo()

# Load environment variables
load_dotenv()

# Configure logging to write logs
log_file = "md5_cracker.log"  # Name of the log file
LOGGING_FORMAT = '%(asctime)s - %(message)s' # Format of the log messages
logging.basicConfig(filename=log_file, level=logging.INFO, format=LOGGING_FORMAT) # Configure the logging module
logger = logging.getLogger(__name__) # Get the logger object

# Get the WhatsApp API token, chat ID, and instance ID from the environment variables
WHATSAPP_API_TOKEN = os.environ.get('WHATSAPP_API_TOKEN') # Get the WhatsApp API token
WHATSAPP_CHAT_ID = os.environ.get('WHATSAPP_CHAT_ID') # Get the WhatsApp chat ID
WHATSAPP_INSTANCE_ID = os.environ.get('WHATSAPP_INSTANCE_ID') # Get the WhatsApp instance ID
WHATSAPP_URL = f'https://7103.api.greenapi.com/waInstance{WHATSAPP_INSTANCE_ID}/sendMessage/{WHATSAPP_API_TOKEN}' # Set the WhatsApp API URL
headers = {'Content-Type': 'application/json'} # Set the headers for the WhatsApp API

# Function to send a message to WhatsApp using the WhatsApp API
def send_message(message):
    data = {"chatId": WHATSAPP_CHAT_ID, "message": message} # Set the chat ID and message data
    try: # Try to send the message
        response = requests.post(WHATSAPP_URL, headers=headers, json=data) # Send a POST request to the WhatsApp API
        if response.status_code == 200: # Check if the message was sent successfully
            logger.info(f'Message sent to {WHATSAPP_CHAT_ID}') # Log the message sent
        else: # Handle errors that occur during message sending
            logger.error(f'Failed to send message to {WHATSAPP_CHAT_ID}') # Log the error
            logger.error(response.text) # Log the response text
    except Exception as e: # Handle any exceptions that occur during message sending
        logger.error(f'Error sending message: {str(e)}') # Log the error

# Function to crack MD5 hashes
def md5_cracker(hashes_file, wordlist_file, output_file):
    # Read the hashes from the hashes file
    with open(hashes_file, 'r', encoding='utf-8') as file: # Open the hashes file
        hashes = [line.strip() for line in file] # Read the hashes from the file

    # Read the passwords from the wordlist file
    with open(wordlist_file, 'r', encoding='utf-8') as file: # Open the wordlist file
        wordlist = [line.strip() for line in file] # Read the passwords from the file

    # Prepare a results list
    results = [] # List to store the results
    cracked_count = 0  # Counter for successfully cracked passwords

    # Iterate over each hash to crack
    for hash_to_crack in hashes: # Iterate over each hash in the list
        found_password = None  # Initialize the found password to None
        for password in wordlist: # Iterate over each password in the wordlist
            # Calculate the MD5 hash of the current password
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            
            # Check if the generated hash matches the target hash
            if hashed_password == hash_to_crack:
                print(f"Password found for hash {hash_to_crack} : {password}") # Print the found password
                found_password = password  # Store the found password
                cracked_count += 1  # Increment cracked count
                break  # Move to the next hash

        # Append the result to the results list
        if found_password:
            results.append(f"{hash_to_crack} : {found_password}")  # Found a password
        else: 
            results.append(f"{hash_to_crack} : ")  # No password found

    # Write results to the output file
    with open(output_file, 'w', encoding='utf-8') as file: 
        for result in results: # Iterate over the results
            file.write(result + '\n') # Write the result to the file
            
    logger.info(f"Cracked passwords written to {output_file}.") # Log the completion message
    print(f"Cracked passwords written to {output_file}.") # Print the completion message
    
    # Send a WhatsApp message upon completion
    send_message(f"MD5 cracking completed. {cracked_count} passwords have been cracked!")

if __name__ == "__main__":
    # Paths to your files
    hashes_path = "md5_hashes.txt"  # Change to the path of your hashes file
    wordlist_path = "w0rdl1$t_4728.txt"     # Change to the path of your wordlist file
    output_path = "results.txt"      # This will be the output file for results

    # Call the md5_cracker function
    md5_cracker(hashes_path, wordlist_path, output_path)
