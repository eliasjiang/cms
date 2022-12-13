FROM python:3.9

ENV TZ=Asia/Shanghai

ENV LANG=zh_CN.UTF-8 \
    LC_ALL=zh_CN.UTF-8
COPY ./locale /etc/default/locale
# 方便下面使用缓存加载
COPY ./requirements.txt /requirements.txt


RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --default-timeout=1000 --no-cache-dir --upgrade -r /requirements.txt


