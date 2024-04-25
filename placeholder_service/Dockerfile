ARG BUILD_FROM=ghcr.io/hassio-addons/base:15.0.8
FROM $BUILD_FROM


# Python 3 HTTP Server serves the current working dir
# So let's set it to our add-on persistent app directory.
WORKDIR /app

# Copy data for add-on
COPY requirements.txt .
COPY placeholder_service.py .
COPY run.sh /
RUN chmod a+x /run.sh

# Install requirements for add-on
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN apk add --no-cache --virtual build-deps gcc python3-dev musl-dev
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg
RUN pip install Pillow
RUN apk del build-deps


CMD [ "/run.sh" ]
