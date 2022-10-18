FROM oraclelinux:7-slim

RUN  yum -y install oracle-release-el7 oracle-nodejs-release-el7 && \
     yum-config-manager --disable ol7_developer_EPEL && \
     yum -y install oracle-instantclient19.3-basiclite nodejs && \
     dnf install python3 &&\
     rm -rf /var/cache/yum

WORKDIR /function
RUN python3 -V
ADD . /function/
ADD terraform /function/
RUN chmod +x terraform
RUN rm -fr /function/.pip_cache
#RUN cp oci_api_key.pem /function/oci_lz
