FROM oraclelinux:7-slim
WORKDIR /function
ADD . /function/
#RUN  yum -y install python3 
#RUN yum install python3-pip -y
RUN pip3 install --target /python/  --no-cache --no-cache-dir -r requirements.txt &&\
    rm -fr ~/.cache/pip /tmp* requirements.txt func.yaml Dockerfile .venv &&\
    chmod -R o+r /python
ADD terraform /function/
RUN mv /function/terraform /usr/local/bin
RUN rm -fr /function/.pip_cache
RUN terraform -version
ENTRYPOINT ["/python/bin/fdk", "/function/func.py", "handler"]