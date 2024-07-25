# Base image with a CUDNN runtime
FROM pytorch/pytorch:2.3.1-cuda12.1-cudnn8-runtime

# Set working directory
WORKDIR /app

COPY . /app

RUN chmod 777 ./environment/solver/cplex_studio2211.linux_x86_64.bin
RUN ./environment/solver/cplex_studio2211.linux_x86_64.bin < ./environment/solver/responses.txt

RUN pip install -r requirements.txt

CMD ["python", "train.py"]
