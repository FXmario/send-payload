import requests
import sys
import numpy as np


def generate_payload(url, file):
    open_payloads = open(file, 'r')
    payloads = np.array(open_payloads.readlines())

    for payload in payloads:
        url_payload = f"{url}{payload}"
        print(f"URL: {url_payload}")
        response = requests.get(
            url=url_payload
        )
        print(response.text)


generate_payload(sys.argv[1], sys.argv[2])
