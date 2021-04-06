# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV GOOGLE_APPLICATION_CREDENTIALS="/app/[credential 파일 이름]"

# Run app.py when the container launches
CMD ["python", "twitter2.py"]
