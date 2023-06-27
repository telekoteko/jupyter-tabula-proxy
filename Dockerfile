FROM jupyter/minimal-notebook:latest

USER root
RUN apt-get update \
 && apt-get install -y \
    curl \
    unzip \
    wget

# install tabula
ENV TABULA_VERSION=1.2.1
RUN apt install default-jre \
 && wget -q "https://github.com/tabulapdf/tabula/releases/download/v${TABULA_VERSION}/tabula-jar-${TABULA_VERSION}.zip -O tabula-jar.zip" \
 && unzip tabula-jar.zip -d /tmp \
 && mv /tmp/tabula/tabula.jar /usr/bin/tabula.jar

# setup package, enable classic extension, build lab extension
USER "${NB_USER}"
WORKDIR "${HOME}"
RUN python3 -m pip install --no-cache-dir https://github.com/telekoteko/jupyter-tabula-proxy/releases/download/1.0.0/jupyter-tabula-proxy-1.0.0.tar.gz
RUN jupyter serverextension enable --sys-prefix jupyter_server_proxy

# copy configs, update permissions as root
USER root
RUN cp /etc/jupyter/jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config_base.py
COPY jupyter_notebook_config.py /etc/jupyter/jupyter_notebook_config.py
RUN fix-permissions /etc/jupyter

USER "${NB_USER}"
