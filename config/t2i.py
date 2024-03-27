baseUrl = "http://123.123.110.133:8099/"

templates = []


def update_tpl(data):
    global templates
    templates = list(map(lambda x: x.get("id"), data))


def get_templates():
    global templates
    return templates
