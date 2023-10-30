import datetime
import logging
import time as t

logger = logging.getLogger(__name__)

def printer() -> str:
    current_time = datetime.datetime.now()
    something = (f"This string is returned from dockerized dummy things board app, "
                 f"indicating that it returned something, ran on {current_time}")
    logger.error(f"This string is the log from dockerized dummy things board app "
                 f"indicating that it returned something, ran on {current_time}")
    print(f"This is the print statement from dockerized dummy things board app "
                 f"indicating that it returned something, ran on {current_time}")
    return something


st = printer()
count = 0
while count < 10:
    logging.warning(st)
    t.sleep(2)
    count += 1
