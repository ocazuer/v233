# v233

模仿 [v2ex](v2ex.com) 的论坛项目

## 依赖

```
pip3 install flask flask-sqlalchemy flask-migrate flask-script flask-markdown gunicorn
```

## 初始化

```
sh init.sh
```

## 运行

```
nohup gunicorn -b '0.0.0.0:80' wsgi:app &
```