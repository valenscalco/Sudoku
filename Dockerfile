FROM python:3

RUN git clone https://github.com/valenscalco/Sudoku.git
WORKDIR /Sudoku


RUN pip3 install -r requirements.txt
RUN pip install parameterized

CMD [ "python3", "test_sudoku.py"]