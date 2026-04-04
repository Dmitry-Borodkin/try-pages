import re

my_dict = {"voidc_repo_url": "https://gitlab.com/voidc-lab/voidc/-/blob/master"}


def do_replace(match):

    return my_dict.get(match.group(1), "???")


pattern = re.compile(r"\{\{(\w+)\}\}")

def do_line(line):

    return pattern.sub(do_replace, line)


def patch(lines):

    return map(do_line, lines)

