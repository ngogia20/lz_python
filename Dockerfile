FROM fnproject/python:3.9-dev as build-stage
WORKDIR /function
ADD requirements.txt /function/
RUN pip3 install --target /python/  --no-cache --no-cache-dir -r requirements.txt &&\
    rm -fr ~/.cache/pip /tmp* requirements.txt func.yaml Dockerfile .venv &&\
    chmod -R o+r /python
ADD . /function/
ADD terraform /tmp
RUN rm -fr /function/.pip_cache
FROM fnproject/python:3.9
WORKDIR /function
COPY --from=build-stage /python /python
COPY --from=build-stage /function /function
RUN chmod -R o+r /function
ENV PYTHONPATH=/function:/python
# RUN pip3 install terraform-install 
RUN cd /tmp
RUN chmod +x terraform
RUN terraform version
RUN mv terraform /usr/bin
RUN terraform -version
ENTRYPOINT ["/python/bin/fdk", "/function/func.py", "handler"]