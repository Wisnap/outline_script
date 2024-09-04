import base64
import json
import argparse
import time
from urllib.parse import urlparse, unquote

def create_outline(key):
    parsed_url = urlparse(unquote(key))
    method_password = base64.b64decode(parsed_url.username).decode()
    method, password = method_password.split(':')
    host = parsed_url.hostname
    port = parsed_url.port

    template_vars = {
        "server": host,
        "server_port": port,
        "local_port": 1080,  # can be modified as needed
        "password": password,
        "method": method,
        "remarks": "Outline Server"
    }


    with open(f'outputs/outline{int(time.time())}.json', 'w') as f:
        f.write(json.dumps(template_vars, indent=4))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Обработка ключа Outline сервера.')
    parser.add_argument('key', type=str, help='Ключ Outline сервера')

    args = parser.parse_args()
    create_outline(args.key)