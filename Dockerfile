FROM python:3.9-alpine

RUN set -ex; \
  # fftcgtool prerequisites
  apk add --no-cache \
    git \
    # fftcgtool deps
    g++ \
    jpeg-dev \
    zlib-dev \
  ;

# env setup
ENV \
  TTSBOT_TOKEN="MISSING"

# install bot
COPY . /usr/src/ttsimport_bot
RUN set -ex; \
  pip3 --no-cache-dir install /usr/src/ttsimport_bot;

CMD ["ttsimport-bot"]
