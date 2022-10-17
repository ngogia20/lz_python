FROM fnproject/python:3.9-dev as build-stage
WORKDIR /function
ADD requirements.txt /function/
RUN pip3 install --target /python/  --no-cache --no-cache-dir -r requirements.txt &&\
    rm -fr ~/.cache/pip /tmp* requirements.txt func.yaml Dockerfile .venv &&\
    chmod -R o+r /python
ADD . /function/
ADD terraform /function/
RUN chmod +x terraform
RUN rm -fr /function/.pip_cache
FROM fnproject/python:3.9
WORKDIR /function
COPY --from=build-stage /python /python
COPY --from=build-stage /function /function
RUN chmod -R o+r /function
ENV PYTHONPATH=/function:/python
RUN mv /function/terraform /usr/local/bin
RUN terraform -version
RUN cd /function/oci_lz-master
RUN cd oci_lz-master
RUN ls -l
RUN terraform init /function/oci_lz-master/
RUN terraform plan
ENTRYPOINT ["/python/bin/fdk", "/function/func.py", "handler"]