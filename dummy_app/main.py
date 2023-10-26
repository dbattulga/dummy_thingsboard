import datetime
import logging


def printer() -> str:
    current_time = datetime.datetime.now()
    something = (f"This string is returned from dockerized dummy things board app, "
                 f"indicating that it returned something, ran on {current_time}")
    return something


st = printer()
logging.warning(st)
