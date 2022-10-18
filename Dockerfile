FROM oraclelinux:7-slim

RUN  yum install python3 
    
WORKDIR /function
RUN python -V
ADD . /function/
ADD terraform /function/
RUN chmod +x terraform
RUN rm -fr /function/.pip_cache
#RUN cp oci_api_key.pem /function/oci_lz
