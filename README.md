![md5_decrypt](https://github.com/user-attachments/assets/830c3448-18b2-4034-a31d-468748daf691)
### MD5 Decrypt Script
This script is designed to crack MD5 hashes using a wordlist of potential passwords. It sends notifications about the completion of the password cracking process via WhatsApp. The script includes logging functionality to record the status and results of the operations. It accomplishes this by:

1. Loading `environment variables` for `API credentials`.
2. Configuring a `logger` to capture and store `logs` of events.
3. Reading `hashes` and `passwords` from specified files.
4. Attempting to `match` each hash with the hashed versions of passwords from the `wordlist`.
5. Reporting `found passwords` and writing the `results` to an output file.
5. Sending a `completion message` via WhatsApp once the process is finished.

**Cracking Function**
* The script takes the paths to the `hashes file`, `wordlist file`, and `output file`.
* Opens and reads the `hashes` and `wordlist`, storing them in lists.
* For each hash, it checks `every password` in the wordlist by hashing it and comparing it to the given hash. If a match is found, it records this password.
* After `attempting to crack` the hashes, it writes the `results` to the specified output file and logs a `completion message`.
* Once cracking is completed, it sends a `summary message` detailing how many passwords were cracked.

![CrackMD5Hash1-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/5d06dcdd-413c-499d-b49a-443d48df306e)

### Installing `python3` and its required packages `requests` and `dotenv`

`sudo apt update`

`sudo apt install python3`

`sudo apt install python3-pip`

`pip3 install requests python-dotenv`  

