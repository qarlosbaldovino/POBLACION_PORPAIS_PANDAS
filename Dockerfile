FROM python:3.8

WORKDIR /13.Pandas
COPY requeriments.txt requeriments.txt

RUN pip install --no-cache-dir --upgrade -r /13.Pandas/requeriments.txt

COPY . 13.PANDAS/

CMD bash -c "while true; do sleep 1; done"