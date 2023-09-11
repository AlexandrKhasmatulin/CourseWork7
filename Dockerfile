FROM python:3
WORKDIR /CourseWork7
COPY ./requirements.txt /CourseWork7/
RUN pip install -r requirements.txt
COPY . .
