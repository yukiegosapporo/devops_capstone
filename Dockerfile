# FROM python:3.6.8
# ENV LC_ALL C.UTF-8
# ENV LANG C.UTF-8
# ENV PIPENV_TIMEOUT 100000

# RUN apt-get -y update && \
#     apt-get -y upgrade && \
#     apt-get install -y libsasl2-dev && \
#     apt-get install -y python-dev && \
#     apt-get install -y libldap2-dev && \
#     apt-get install -y libssl-dev && \
#     apt-get install -y libsnmp-dev && \
#     apt-get install -y libopenmpi-dev && \
#     apt-get install -y cmake && \
#     apt-get install -y python3-dev && \
#     apt-get install -y zlib1g-dev && \
#     apt-get install -y git && \
#     pip install --upgrade pip


# COPY app /app
# COPY requirements.txt /app/requirements.txt
# WORKDIR /app

# # EXPOSE 80

# RUN pip install -r requirements.txt

# CMD python app.py


FROM python:3.6.8-stretch

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY app /app
COPY requirements.txt /app/requirements.txt

## Step 3:
# Install packages from requirements.txt
# hadolint ignore=DL3013
RUN pip install --upgrade pip &&\
    pip install --trusted-host pypi.python.org -r requirements.txt

## Step 4:
# Expose port 80
EXPOSE 80

## Step 5:
# Run app.py at container launch
ENTRYPOINT [ "python" ]

CMD [ "app.py" ]