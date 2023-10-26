
import datetime
import logging


if __name__ == '__main__':
    time = datetime.datetime.now()
    logging.warning(f'This log is from dockerized dummy thingsboard app, ran on {time}')
