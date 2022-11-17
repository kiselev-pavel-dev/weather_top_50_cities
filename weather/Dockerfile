FROM python:3.8
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
RUN python -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir
ADD . /app/
CMD ["gunicorn", "weather.wsgi:application", "--bind", "0:8000" ]
