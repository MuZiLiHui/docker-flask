# Dockerfile

# 使用 Python 运行时作为基础镜像
FROM daocloud.io/library/python

# 设置 /app 为工作路径
WORKDIR /app

# 将当前目录所有内容复制到容器的 /app 目录下
ADD . /app

# 安装 requirements.txt 中指定的包
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

# 对容器外开放5000端口
EXPOSE 5000

# 定义环境变量
ENV NAME World

# 当容器启动时运行 app.py 
CMD ["python", "app.py"]