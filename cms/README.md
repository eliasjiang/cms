## 西大健身Flask CMS


### dockerc-compose 部署

假定您已经搭建好docker环境和docker-compose环境, 以下为搭建docker环境的文档



#### 打开终端，cd到你的项目目录cms

```shell
sudo chmod +x run.sh
./run.sh start
```

#### 初次启动项目之后，需要手动执行以下命令导入数据库文件

```shell
docker cp docker/init/db.sql docker-db-1:/
docker exec -it docker-db-1  bash
mysql -uroot -p
```

输入密码 root

然后进入mysql的客户端

```shell

use cms;
source db.sql;
exit;
```
退出mysql, 继续执行退出容器

```shell
exit
```


#### 在浏览器中打开 http://127.0.0.1:8889/ 访问网站。