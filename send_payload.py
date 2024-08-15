import requests
import sys
import numpy as np
import re


def generate_payload(url_file, payload_file):
    open_urls = open(url_file, 'r')
    urls = np.array(open_urls.readlines())

    open_payloads = open(payload_file, 'r')
    payloads = np.array(open_payloads.readlines())

    for url in urls:
        print(url)
        for payload in payloads:
            url_payload = re.sub(r'=(.*?)(?=&|$)', f'={payload}', url)
            print(f"URL: {url_payload}")
            response = requests.get(
                url=url_payload
            )
            result = response.text
            print(result)
            with open("result_payload.txt", "a") as output:
                output.write(f"URL: {url_payload}\n{result}\n\n")


generate_payload(sys.argv[1], sys.argv[2])
