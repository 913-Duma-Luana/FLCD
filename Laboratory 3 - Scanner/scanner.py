import re

from specification import *


def is_part_of_operator(char):
    for op in operators:
        if char in op:
            return True
    return False


def is_escaped_quote(line, index):
    return False if index == 0 else line[index - 1] == '\\'


def get_string_token(line, index):
    token = ''
    quotes = 0

    while index < len(line) and quotes < 2:
        if line[index] == '"' and not is_escaped_quote(line, index):
            quotes += 1
        token += line[index]
        index += 1

    return token, index


def get_token_for_operator(line, index):
    token = ''

    while index < len(line) and is_part_of_operator(line[index]):
        token += line[index]
        index += 1

    return token, index


def separate_into_tokens(line, separators):
    token = ''
    index = 0

    while index < len(line):
        if line[index] == '"':
            if token:
                yield token
            token, index = get_string_token(line, index)
            yield token
            token = ''

        elif is_part_of_operator(line[index]):
            if token:
                yield token
            token, index = get_token_for_operator(line, index)
            yield token
            token = ''

        elif line[index] in separators:
            if token:
                yield token
            token, index = line[index], index + 1
            yield token
            token = ''

        else:
            token += line[index]
            index += 1
    if token:
        yield token


def is_identifier(token):
    match = re.match(r'^[a-zA-Z]([a-zA-Z]|[0-9]|_){,64}$', token) is not None
    return match


def is_constant(token):
    strToken = str(token)
    if strToken[0] == '"' and strToken[-1] == '"':
        return True
    if strToken[0] == '”' and strToken[-1] == '”':
        return True
    if strToken[0] == "'" and strToken[-1] == "'":
        return True
    varianta1 = re.match('^(0|[\+\-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$', token)
    varianta2 = re.match('"\w*"', token)
    return (varianta1 is not None) or (varianta2 is not None)
