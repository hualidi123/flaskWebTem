# flaskWebTem
flask web开发模板框架
用flask开发web需要自己去构建MTV的全部东西，太繁琐。这套模板可以极大简化创建app的过程，更多的去关注view的实现即可。

# 表结构
```sql
CREATE TABLE `alarm_rank` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '自增主键',
  `app` varchar(255) NOT NULL,
  `project` varchar(255) DEFAULT NULL,
  `appManager` varchar(255) DEFAULT NULL,
  `projectManager` varchar(50) DEFAULT NULL,
  `country` varchar(5) DEFAULT NULL,
  `currenttime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=83 DEFAULT CHARSET=utf8mb4
```
