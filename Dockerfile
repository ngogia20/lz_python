FROM fnproject/python:3.9-dev as build-stage
WORKDIR /function
ADD requirements.txt /function/
RUN pip3 install --target /python/  --no-cache --no-cache-dir -r requirements.txt &&\
    rm -fr ~/.cache/pip /tmp* requirements.txt func.yaml Dockerfile .venv &&\
    chmod -R o+r /python
ADD . /function/
ADD terraform /function/
RUN chmod +x terraform
RUN wget https://github.com/ngogia20/oci_lz/archive/refs/heads/master.zip
RUN UNZIP oci_lz-master.zip
RUN /function/terraform -version
#RUN mv /function/terraform /usr/local/bin
RUN rm -fr /function/.pip_cache
FROM fnproject/python:3.9
WORKDIR /function
COPY --from=build-stage /python /python
COPY --from=build-stage /function /function
RUN chmod -R o+r /function
ENV PYTHONPATH=/function:/python
# RUN pip3 install terraform-install 
RUN mv /function/terraform /usr/local/bin
RUN terraform -version
RUN cd /function/oci_lz-master
RUN terraform init
RUN terraform apply
ENTRYPOINT ["/python/bin/fdk", "/function/func.py", "handler"]