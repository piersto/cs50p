import re


def remove_url_anchor(url):
    url = re.sub(r"#.+", "", url)
    return url
