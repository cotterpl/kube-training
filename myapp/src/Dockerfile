FROM python:3.9-slim as compile-image

# Create virtualenv and start using it
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN pip install --upgrade pip pip-tools wheel

WORKDIR /build

# Install dependencies
COPY requirements.txt ./
RUN pip-sync requirements.txt


FROM python:3.9-slim AS build-image

# Copy virtualenv from compile image
COPY --from=compile-image /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy the application
WORKDIR /app
COPY setup.py README.md VERSION.txt requirements.in requirements.txt ./
COPY myapp ./myapp
RUN pip install --no-deps .

EXPOSE 80

CMD python -m uvicorn myapp.main:app --host 0.0.0.0 --port 80