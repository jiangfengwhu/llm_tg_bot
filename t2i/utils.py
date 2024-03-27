from urllib.parse import urljoin

import requests

from config.t2i import baseUrl, update_tpl


def upload_image(name, blob):
    data = {"subfolder": "", "overwrite": "true"}
    files = {
        "image": (name, blob),
        "overwrite": "true",
    }
    resp = requests.post(urljoin(baseUrl, "/upload/image"), files=files, data=data)
    print(resp.content)


def queue_prompt(input_name, tpl):
    data = {
        "template_id": tpl,
        "images": {"13": input_name},
        "type": "t2i",
    }
    resp = requests.post(urljoin(baseUrl, "/gapi/queue_prompt"), json=data)
    print(resp.json())
    return resp.json()


def query_tpl():
    resp = requests.get(urljoin(baseUrl, "/gapi/home"))
    update_tpl(resp.json().get("data", []))
