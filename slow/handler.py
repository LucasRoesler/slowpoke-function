import os
import time

delay = os.environ.get("delay", "10")

time.sleep(int(delay))

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    return f"slept for {delay} and then {req}"
