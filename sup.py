import sys
import requests
import threading
from termcolor import colored

def check_url_status(url, output_file=None):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if 'sitemap' in response.url:
                status_message = colored(f"200 OK -->> {response.url}", "green")
                if output_file:
                    output_file.write(f"{url}\n")
            else:
                status_message = colored(f"200 OK but no sitemap {response.url}. Confirm manually!", "yellow")
        else:
            status_message = colored(f"{response.status_code} {response.reason}", "red")
        print(f"{url} - {status_message}")
    except requests.exceptions.RequestException as e:
        error_message = colored(str(e), "red")
        print(f"{url} - {error_message}")

def process_urls(urls, output_file=None):
    threads = []
    for url in urls:
        url = url.strip()
        thread = threading.Thread(target=check_url_status, args=(url, output_file))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Get the file name and output option from command-line arguments
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    output_option = sys.argv[2] if len(sys.argv) > 2 else None
    output_file_path = sys.argv[3] if len(sys.argv) > 2 else None
else:
    print("Please provide the file name as a command-line argument.")
    sys.exit(1)

with open(file_path, "r") as file:
    urls = file.readlines()

output_file = None
if output_option == "-o":
    output_file = open(output_file_path, "w+")

process_urls(urls, output_file)

if output_file:
    output_file.close()
    print(f"\n[+] URLs with 200 status code have been saved to {output_file_path}")


print(colored("[+] Some results are not always 100% accurate.", "yellow"))
