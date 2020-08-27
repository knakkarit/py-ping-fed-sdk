import os
import requests
from time import sleep
from requests.auth import HTTPBasicAuth


def safe_name(unsafe_string, unsafe_char="/", sub_char="_"):
    safe_string_list = [
        x if x not in unsafe_char else sub_char for x in unsafe_string
    ]
    safe_string_list = [
        x if x not in "{}-" else "" for x in safe_string_list
    ]

    return "".join(safe_string_list)


def safe_variable(unsafe_variable):
    """
    Some APIs define variables that are unsafe to Python code
    e.g. id and type are both reserved words in Python.
    This helper adds 'var_' to the beginning to avoid shadowing
    these builtins.
    """
    if unsafe_variable == "id":
        return "var_id"
    elif unsafe_variable == "type":
        return "var_type"
    return unsafe_variable


def ref_type_convert(ref_obj):
    if ref_obj["$ref"].startswith("Map"):
        return "dict"
    if ref_obj["$ref"].startswith("Set"):
        return "set"
    return ref_obj["$ref"]


def json_type_convert(json_type):
    if json_type in ("enum", "string", "File"):
        return "str"
    elif json_type == "boolean":
        return "bool"
    elif json_type == "array":
        return "list"
    elif json_type == "integer":
        return "int"
    elif json_type == "void":
        return "None"
    return ""


def get_auth_session():
    ping_user = os.environ.get(
        "PING_IDENTITY_DEVOPS_ADMINISTRATOR", "administrator"
    )
    ping_pass = os.environ.get(
        "PING_IDENTITY_DEVOPS_PASSWORD", "2FederateM0re"
    )

    session = requests.Session()
    session.auth = HTTPBasicAuth(ping_user, ping_pass)
    session.headers = {
        "Accept": "application/json",
        "X-Xsrf-Header": "PingFederate"
    }

    return session


def retry_with_backoff(func, retries=5, backoff=5):
    total_retries = retries
    while retries:
        try:
            func()
        except Exception as ex:
            print(
                f'{ex}, attempting retry'
                f'{total_retries - (retries + 1)}/{total_retries},'
                f'wait {backoff} seconds...'
            )
            retries -= 1
            sleep(backoff)
            backoff += backoff
            continue
        return True
    if not retries:
        return False


def get_exception_by_code(http_response_code):
    if http_response_code == 204:
        return "ObjectDeleted"
    elif http_response_code == 400:
        return "BadRequest"
    elif http_response_code == 403:
        return "NotImplementedError"
    elif http_response_code == 404:
        return "NotFound"
    elif http_response_code == 422:
        return "ValidationError"


def get_request_path(raw_path):
    return raw_path.replace("{id}", "{var_id}").replace("{type}", "{var_type}")


def has_substitution(check_string):
    """
    Return True if the string needs to be converted to an f-string
    because it has {} for substitution
    """
    l_paren = check_string.find("{") + 1
    r_paren = check_string.find("}") + 1
    return l_paren and r_paren and l_paren < r_paren


def write_template(content, file_name="PINGVERSION", folder=".."):
    """
    Given a version of Ping will write it out into a PINGVERSION file.
    """
    filedirectory = os.path.dirname(os.path.realpath(__file__))
    targetdirectory = os.path.join(
        filedirectory,
        folder
    )

    if not os.path.exists(targetdirectory):
        os.makedirs(targetdirectory)

    path = f"{targetdirectory}/{file_name}"
    with open(os.path.join(filedirectory, path), "w") as fh:
        fh.write(content)