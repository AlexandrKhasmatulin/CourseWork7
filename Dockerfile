FROM python:3.10-slim
WORKDIR /CourseWork7
COPY ./requirements.txt /CourseWork7/
RUN pip install -r requirements.txt
COPY . .
