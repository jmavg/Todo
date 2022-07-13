FROM python:3.10.4-alpine3.16

RUN apk update
RUN mkdir /opt/TODO && apk add git

WORKDIR /opt/TODO/

RUN git clone https://github.com/jmavg/Todo.git
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["./todo_app/todo.py"]

