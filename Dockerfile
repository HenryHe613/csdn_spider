FROM python:3.12.7-slim-bookworm
ARG author="nanyancc"

COPY requirements.txt /tmp/requirements.txt

RUN apt update && apt install -y --no-install-recommends wget unzip libnss3-tools && \
    wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt install -y ./google-chrome-stable_current_amd64.deb && \
    rm -f ./google-chrome-stable_current_amd64.deb && \
    wget -q https://storage.googleapis.com/chrome-for-testing-public/$(google-chrome --version | sed 's/^Google Chrome //' | sed 's/ //')/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/local/share/chromedriver && \
    rm -rf chromedriver-linux64.zip chromedriver-linux64 && \
    apt clean && rm -rf /var/lib/apt/lists/*  && \
    pip install --no-cache-dir -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt

ENTRYPOINT ["python"]