# Use an official Python image as a parent image
FROM python:3.9

# Set environment variables (optional)
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE project.settings

# Create and set the working directory
RUN mkdir /app
WORKDIR /app

# Copy the project files into the container
COPY . /app/

# Install project dependencies
RUN pip install -r requirements.txt

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port your Django app will run on (usually 8000)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

