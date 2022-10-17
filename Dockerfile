FROM fnproject/python:3.9-dev as build-stage
WORKDIR /function
ADD requirements.txt /function/
RUN pip3 install --target /python/  --no-cache --no-cache-dir -r requirements.txt &&\
    rm -fr ~/.cache/pip /tmp* requirements.txt func.yaml Dockerfile .venv &&\
    chmod -R o+r /python
ADD . /function/
RUN rm -fr /function/.pip_cache
FROM fnproject/python:3.9
WORKDIR /function
COPY --from=build-stage /python /python
COPY --from=build-stage /function /function
RUN chmod -R o+r /function
ENV PYTHONPATH=/function:/python
# RUN pip3 install terraform-install 
RUN cd /tmp
RUN wget https://releases.hashicorp.com/terraform/1.3.2/terraform_1.3.2_linux_amd64.zip
RUN unzip terraform_1.3.2_linux_amd64.zip -d ./terraform 
RUN rm -rf /tmp/*.zip
RUN chmod +x terraform
RUN ls -l /tmp/terraform
RUN terraform -version
#RUN which terraform

RUN chmod +x /usr/local/bin/terraform
RUN ls -l /usr/local/bin/terraform
ENTRYPOINT ["/python/bin/fdk", "/function/func.py", "handler"]