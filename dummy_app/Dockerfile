FROM python:3.8-alpine


# WORKDIR /testapp
#COPY . /testapp

COPY . .
RUN pip3 install -r requirements.txt
RUN apk update
RUN apk add git

# Disable gitpython check for the git executable, cachito-api doesn't use git
# ENV GIT_PYTHON_REFRESH=quiet
# ENV PATH=$PATH:/usr/bin/git
# ENV GIT_PYTHON_GIT_EXECUTABLE=/usr/bin/git

ENTRYPOINT ["python"]
CMD ["main.py"]
