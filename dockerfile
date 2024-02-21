# Select an os
FROM python:3.12.1

# Generate python output
ENV PYTHONUNBUFFERED 1

# Create the root directory
RUN mkdir /app-root

# Set the working directory
WORKDIR /app-root

# Copy and link with my docker file
ADD . /app-root

#
RUN pip install -r requirements.txt
