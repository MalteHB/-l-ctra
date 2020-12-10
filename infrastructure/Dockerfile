# RUN FROM /bachelor_project/infrastructure
# docker build --tag electra_google:1.0 .
# docker run --gpus device=0 -v ~/bachelor_project:/bachelor_project --name gpu_0_electra -it electra_google:1.0
# docker run --gpus device=1 -v ~/bachelor_project:/bachelor_project --name gpu_1_electra -it electra_google:1.0

FROM  tensorflow/tensorflow:1.15.4-gpu-py3

RUN python3 -m pip install --upgrade pip

RUN apt-get update
RUN apt-get install git -y

COPY requirements.txt ./
RUN pip install -r "requirements.txt"
