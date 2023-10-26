import os
import time as T
import logging

from git import Repo, GitCommandError


def pull_from_git():
    cwd = os.path.dirname(os.getcwd())
    repodir = os.path.join(os.path.abspath(cwd), 'repodir/dummy_thingsboard')
    repolink = "https://github.com/dbattulga/dummy_thingsboard.git"
    print(f"repodir path: {repodir}")
    print(f"CWD is: {cwd}")
    try:
        Repo.clone_from(repolink, repodir)
        print('Cloning successful!')
    except GitCommandError as e:
        print('Cloning failed:', str(e))
    # TODO handle it with exception
    print("This log is from within dag pull function")


def continuous_job():
    while True:
        print("cont")
        logging.error("cont")
        T.sleep(2)
