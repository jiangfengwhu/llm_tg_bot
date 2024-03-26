import requests


def upload_image(name, blob):
    data = {"subfolder": "", "overwrite": "true"}
    files = {
        "image": (name, blob),
        "overwrite": "true",
    }
    resp = requests.post(
        "http://123.123.110.133:8099/upload/image", files=files, data=data
    )
    print(resp.content)


def queue_prompt(input_name):
    data = {
        "template_id": "幽光精灵",
        "images": {"13": input_name},
        "type": "t2i",
    }
    resp = requests.post("http://123.123.110.133:8099/gapi/queue_prompt", json=data)
    print(resp.json())
    return resp.json()
