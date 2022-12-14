-- MySQL dump 10.13  Distrib 5.7.36, for osx10.13 (x86_64)
--
-- Host: localhost    Database: cms
-- ------------------------------------------------------
-- Server version	5.7.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

create database if not exists `cms` default character set UTF8mb4 collate utf8mb4_unicode_ci;
USE database `cms`;

--
-- Table structure for table `action`
--

DROP TABLE IF EXISTS `action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `action` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '权限ID',
  `level1_name` varchar(20) NOT NULL DEFAULT '' COMMENT '一级菜单名称',
  `level2_name` varchar(20) NOT NULL DEFAULT '' COMMENT '二级菜单名称',
  `name` varchar(20) NOT NULL DEFAULT '' COMMENT '权限名',
  `url` varchar(255) NOT NULL DEFAULT '' COMMENT '允许访问的链接,用特殊字符分割',
  `level1_weight` tinyint(4) NOT NULL DEFAULT '0' COMMENT '一级菜单权重',
  `level2_weight` tinyint(4) NOT NULL DEFAULT '0' COMMENT '二级菜单权重',
  `weight` tinyint(4) NOT NULL DEFAULT '0' COMMENT '权重 越大排名越前面',
  `is_important` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否是重要权限',
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1 有效 0无效',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COMMENT='权限表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `action`
--

LOCK TABLES `action` WRITE;
/*!40000 ALTER TABLE `action` DISABLE KEYS */;
INSERT INTO `action` VALUES (1,'系统日志','访问日志','访问日志','/home/log/access',1,60,1,0,1,'2022-12-03 19:31:31','2022-12-03 00:58:46'),(3,'系统日志','错误日志','错误日志','/home/log/error',1,50,1,0,1,'2022-12-03 17:52:04','2022-12-03 01:04:24'),(6,'仪表盘','首页','首页','/home/',60,1,1,0,1,'2022-12-03 18:13:22','2022-12-03 17:51:45'),(7,'网址之家','网址管理','网址管理','/home/link/index',55,60,1,0,1,'2022-12-03 18:05:39','2022-12-03 17:54:40'),(8,'员工管理','员工列表','员工管理','/home/rbac/staff/index',50,60,1,0,1,'2022-12-03 17:55:24','2022-12-03 17:55:24'),(9,'员工管理','部门列表','部门管理','/home/rbac/dept/index',50,55,1,0,1,'2022-12-03 17:56:32','2022-12-03 17:56:32'),(10,'员工管理','权限分配','权限分配','/home/rbac/grant/assign',50,50,1,1,1,'2022-12-03 19:31:25','2022-12-03 17:57:01'),(11,'员工管理','权限管理','权限管理','/home/rbac/grant/index',50,45,1,0,1,'2022-12-03 17:57:39','2022-12-03 17:57:39'),(12,'网址之家','网址管理','编辑/添加','/home/link/set',55,50,1,0,1,'2022-12-03 18:05:25','2022-12-03 18:05:17'),(13,'网址之家','网址管理','删除/恢复','/home/link/ops',55,45,1,0,1,'2022-12-03 18:09:50','2022-12-03 18:09:50'),(14,'员工管理','部门列表','添加/编辑','/home/rbac/dept/set',50,55,1,0,1,'2022-12-03 18:10:34','2022-12-03 18:10:34'),(15,'员工管理','部门列表','删除/恢复','/home/rbac/dept/ops',50,55,1,0,1,'2022-12-03 18:10:50','2022-12-03 18:10:50'),(16,'员工管理','员工列表','添加/编辑','/home/rbac/staff/set',50,60,1,0,1,'2022-12-03 18:11:19','2022-12-03 18:11:19'),(17,'员工管理','员工列表','删除/恢复','/home/rbac/staff/ops',50,60,1,0,1,'2022-12-03 18:11:38','2022-12-03 18:11:38'),(18,'员工管理','权限管理','添加/编辑/复制','/home/rbac/grant/set',50,45,1,0,1,'2022-12-03 18:12:33','2022-12-03 18:12:05'),(19,'员工管理','权限管理','删除/恢复','/home/rbac/grant/ops',50,45,1,0,1,'2022-12-03 18:12:27','2022-12-03 18:12:27');
/*!40000 ALTER TABLE `action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_access_log`
--

DROP TABLE IF EXISTS `app_access_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_access_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL DEFAULT '0' COMMENT '用户表id',
  `uname` varchar(20) NOT NULL DEFAULT '' COMMENT '用户表姓名',
  `referer_url` varchar(1000) NOT NULL DEFAULT '' COMMENT '当前访问的refer',
  `target_url` varchar(1000) NOT NULL DEFAULT '' COMMENT '访问的url',
  `query_params` varchar(1000) NOT NULL DEFAULT '' COMMENT 'get和post参数',
  `ua` varchar(1000) NOT NULL DEFAULT '' COMMENT '访问ua',
  `ip` varchar(32) NOT NULL DEFAULT '' COMMENT '访问ip',
  `note` varchar(1000) NOT NULL DEFAULT '' COMMENT 'json格式备注字段',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入日期',
  PRIMARY KEY (`id`),
  KEY `idx_created_time` (`created_time`),
  KEY `idx_uid` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8mb4 COMMENT='用户访问日志记录表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_access_log`
--

LOCK TABLES `app_access_log` WRITE;
/*!40000 ALTER TABLE `app_access_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_access_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_err_log`
--

DROP TABLE IF EXISTS `app_err_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app_err_log` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `request_uri` varchar(255) NOT NULL DEFAULT '' COMMENT '请求uri',
  `referer` varchar(500) NOT NULL DEFAULT '' COMMENT '来源url',
  `content` varchar(3000) NOT NULL DEFAULT '' COMMENT '日志内容',
  `ip` varchar(100) NOT NULL DEFAULT '' COMMENT 'ip',
  `ua` varchar(1000) NOT NULL DEFAULT '' COMMENT 'ua信息',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  KEY `idx_created_time` (`created_time`)
) ENGINE=InnoDB AUTO_INCREMENT=314 DEFAULT CHARSET=utf8mb4 COMMENT='app错误日表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_err_log`
--

LOCK TABLES `app_err_log` WRITE;
/*!40000 ALTER TABLE `app_err_log` DISABLE KEYS */;

/*!40000 ALTER TABLE `app_err_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `name` varchar(180) NOT NULL DEFAULT '' COMMENT '课程名称',
  `cover` varchar(250) NOT NULL DEFAULT '' COMMENT '封面',
  `video` varchar(250) NOT NULL DEFAULT '' COMMENT '视频',
  `description` text COMMENT '描述',
  `part` varchar(60) NOT NULL DEFAULT '' COMMENT '部位',
  `difficult` varchar(60) NOT NULL DEFAULT '' COMMENT '难度',
  `tags` varchar(250) NOT NULL DEFAULT '' COMMENT '标签',
  `status` smallint(3) NOT NULL DEFAULT '0' COMMENT '状态',
  `created_at` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `upated_at` int(11) NOT NULL DEFAULT '0' COMMENT '更改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='课程表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '用户ID',
  `email` varchar(120) NOT NULL DEFAULT '' COMMENT '用户邮箱(账号)',
  `username` varchar(60) NOT NULL DEFAULT '' COMMENT '用户名',
  `password_hash` varchar(250) NOT NULL DEFAULT '' COMMENT '用户密码(加密字符串)',
  `name` varchar(60) NOT NULL DEFAULT '' COMMENT '客户姓名',
  `address` varchar(250) NOT NULL DEFAULT '' COMMENT '用户地址',
  `city` varchar(60) NOT NULL DEFAULT '' COMMENT '城市或县',
  `province` varchar(60) NOT NULL DEFAULT '' COMMENT '省',
  `mobile` varchar(30) NOT NULL DEFAULT '' COMMENT '手机号码',
  `balance` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '账户余额',
  `credit_level` smallint(3) NOT NULL DEFAULT '0' COMMENT '信用等级 一级为10%的折扣，不能透支；二级为15%的折扣，不能透支；三级为15%的折扣，透支有额度限制；四级为20%的折扣，透支有额度限制；五级为25%的折扣',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 COMMENT='客户表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;

INSERT INTO `customer` (`id`, `email`, `username`, `password_hash`, `name`, `address`, `city`, `province`, `mobile`, `balance`, `credit_level`) VALUES
(1, 'admin@domain.com', 'admin', 'pbkdf2:sha256:260000$edaPrhmkFTg63c9J$aa74a2ef9d1f5bb3877f01043fc224bf8e83941dbddcc60c07766e91640cc2e6', 'Test', 'Room 8903, LongShan', 'Chongqing', 'Chongqing', '13224040934', '0.00', 0);

/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food`
--

DROP TABLE IF EXISTS `food`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `name` varchar(180) NOT NULL DEFAULT '' COMMENT '食物名称',
  `cover` varchar(250) NOT NULL DEFAULT '' COMMENT '封面',
  `video` varchar(250) NOT NULL DEFAULT '' COMMENT '视频',
  `description` text COMMENT '描述',
  `tags` varchar(250) NOT NULL DEFAULT '' COMMENT '标签',
  `created_at` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `upated_at` int(11) NOT NULL DEFAULT '0' COMMENT '更改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='课程表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food`
--

LOCK TABLES `food` WRITE;
/*!40000 ALTER TABLE `food` DISABLE KEYS */;
/*!40000 ALTER TABLE `food` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `food_category`
--

DROP TABLE IF EXISTS `food_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `food_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '目录ID',
  `parent_id` int(11) NOT NULL DEFAULT '0' COMMENT '上级目录ID',
  `name` varchar(120) NOT NULL DEFAULT '' COMMENT '目录名',
  `description` varchar(250) NOT NULL DEFAULT '' COMMENT '目录描述',
  `sort_num` smallint(3) NOT NULL DEFAULT '0' COMMENT '目录排序号',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='书目录';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `food_category`
--

LOCK TABLES `food_category` WRITE;
/*!40000 ALTER TABLE `food_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `food_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gym_action`
--

DROP TABLE IF EXISTS `gym_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gym_action` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `name` varchar(180) NOT NULL DEFAULT '' COMMENT '动作名称',
  `cover` varchar(250) NOT NULL DEFAULT '' COMMENT '封面',
  `video` varchar(250) NOT NULL DEFAULT '' COMMENT '视频',
  `description` text COMMENT '描述',
  `category_id` int(11) NOT NULL DEFAULT '0' COMMENT '动作分类',
  `tags` varchar(250) NOT NULL DEFAULT '' COMMENT '标签',
  `created_at` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `upated_at` int(11) NOT NULL DEFAULT '0' COMMENT '更改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='课程表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_action`
--

LOCK TABLES `gym_action` WRITE;
/*!40000 ALTER TABLE `gym_action` DISABLE KEYS */;
/*!40000 ALTER TABLE `gym_action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gym_action_category`
--

DROP TABLE IF EXISTS `gym_action_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gym_action_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '目录ID',
  `parent_id` int(11) NOT NULL DEFAULT '0' COMMENT '上级目录ID',
  `name` varchar(120) NOT NULL DEFAULT '' COMMENT '目录名',
  `description` varchar(250) NOT NULL DEFAULT '' COMMENT '目录描述',
  `sort_num` smallint(3) NOT NULL DEFAULT '0' COMMENT '目录排序号',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='书目录';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gym_action_category`
--

LOCK TABLES `gym_action_category` WRITE;
/*!40000 ALTER TABLE `gym_action_category` DISABLE KEYS */;
/*!40000 ALTER TABLE `gym_action_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `link`
--

DROP TABLE IF EXISTS `link`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `link` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `type` tinyint(4) NOT NULL DEFAULT '0' COMMENT '类型',
  `title` varchar(100) NOT NULL DEFAULT '' COMMENT '标题',
  `url` varchar(300) NOT NULL DEFAULT '' COMMENT '网址',
  `weight` int(11) NOT NULL DEFAULT '1' COMMENT '权重 越大越排前',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态： 1：有效  0：无效',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COMMENT='网址管理';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `link`
--

LOCK TABLES `link` WRITE;
/*!40000 ALTER TABLE `link` DISABLE KEYS */;
INSERT INTO `link` VALUES (1,5,'西大健身官网','http://www.jixuejima.cn/',1,1,'2022-12-03 20:05:00','2022-12-03 14:31:23'),(2,5,'西大健身博文','http://www.jixuejima.cn/article/index',1,1,'2022-12-03 20:04:56','2022-12-03 14:31:43'),(3,5,'西大健身文档中心','http://dcenter.jixuejima.cn/#/',1,1,'2022-12-03 14:32:14','2022-12-03 14:32:14'),(4,5,'CTBox：网址收藏夹','http://dcenter.jixuejima.cn/#/ctbox/readme',1,1,'2022-12-03 20:04:27','2022-12-03 14:32:32'),(5,5,'编程浪子','http://www.54php.cn/',1,1,'2022-12-03 20:05:24','2022-12-03 14:32:51'),(6,3,'Jobs（乔布斯）管理调度平台','http://dcenter.jixuejima.cn/#/flask/jobs/readme',1,1,'2022-12-03 20:05:58','2022-12-03 14:33:18');
/*!40000 ALTER TABLE `link` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plan`
--

DROP TABLE IF EXISTS `plan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plan` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `name` varchar(250) NOT NULL DEFAULT '' COMMENT '训练计划名称',
  `description` text COMMENT '详情',
  `course_id` int(11) NOT NULL DEFAULT '0' COMMENT '课程ID',
  `charge` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '收取费用',
  `status` smallint(3) NOT NULL DEFAULT '0' COMMENT '状态',
  `start_date` int(11) NOT NULL DEFAULT '0' COMMENT '开始时间',
  `end_date` int(11) NOT NULL DEFAULT '0' COMMENT '结束时间',
  `created_at` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `updated_at` int(11) NOT NULL DEFAULT '0' COMMENT '更改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订阅表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plan`
--

LOCK TABLES `plan` WRITE;
/*!40000 ALTER TABLE `plan` DISABLE KEYS */;
/*!40000 ALTER TABLE `plan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '角色ID',
  `name` varchar(255) NOT NULL DEFAULT '' COMMENT '角色名',
  `pid` int(11) NOT NULL DEFAULT '0' COMMENT '父级id',
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1有效 0无效',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COMMENT='角色部门表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (1,'总裁办',0,1,'2022-12-03 01:26:04','2022-12-03 01:16:15'),(2,'人事部门',1,1,'2022-12-03 20:21:05','2022-12-03 01:23:19'),(3,'研发部门',1,1,'2022-12-03 01:34:08','2022-12-03 01:33:55'),(4,'设计部门',1,1,'2022-12-03 01:37:14','2022-12-03 01:37:14');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_action`
--

DROP TABLE IF EXISTS `role_action`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_action` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '角色权限ID',
  `role_id` int(11) NOT NULL DEFAULT '0' COMMENT '角色ID',
  `action_id` int(11) NOT NULL DEFAULT '0' COMMENT '权限ID',
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '1有效 0无效',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_role_action_id` (`role_id`,`action_id`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='角色权限表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_action`
--

LOCK TABLES `role_action` WRITE;
/*!40000 ALTER TABLE `role_action` DISABLE KEYS */;
/*!40000 ALTER TABLE `role_action` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscription`
--

DROP TABLE IF EXISTS `subscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscription` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `customer_id` int(11) NOT NULL DEFAULT '0' COMMENT '客户ID',
  `plan_id` int(11) NOT NULL DEFAULT '0' COMMENT '计划ID',
  `charge` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '收取费用',
  `status` smallint(3) NOT NULL DEFAULT '0' COMMENT '状态',
  `is_renewed` tinyint(3) NOT NULL DEFAULT '0' COMMENT '是否续订',
  `start_date` int(11) NOT NULL DEFAULT '0' COMMENT '开始时间',
  `end_date` int(11) NOT NULL DEFAULT '0' COMMENT '结束时间',
  `created_at` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  `updated_at` int(11) NOT NULL DEFAULT '0' COMMENT '更改时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='订阅表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscription`
--

LOCK TABLES `subscription` WRITE;
/*!40000 ALTER TABLE `subscription` DISABLE KEYS */;
/*!40000 ALTER TABLE `subscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL DEFAULT '' COMMENT '用户名',
  `email` varchar(50) NOT NULL DEFAULT '' COMMENT '邮箱地址也是登录用户名',
  `role_id` int(11) NOT NULL DEFAULT '0' COMMENT '人员所属部门',
  `salt` varchar(64) NOT NULL DEFAULT '' COMMENT '随机码',
  `is_root` tinyint(1) NOT NULL DEFAULT '0' COMMENT '是否是管理员 1：是 0：不是',
  `status` tinyint(1) NOT NULL DEFAULT '1' COMMENT '状态 1：有效 0：无效',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后一次更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `uk_email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'西大健身工作室','ericjiang8@163.com',0,'HRD60OnSkN4dpCDH',1,1,'2022-12-03 14:41:11','2022-12-03 23:50:43');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_news`
--

DROP TABLE IF EXISTS `user_news`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_news` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '消息id',
  `uid` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '用户id',
  `title` varchar(255) NOT NULL DEFAULT '' COMMENT '标题',
  `content` varchar(1500) NOT NULL DEFAULT '' COMMENT '内容',
  `status` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '状态 0：未读 1：已读',
  `updated_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '更新时间',
  `created_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC COMMENT='用户站内消息表';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_news`
--

LOCK TABLES `user_news` WRITE;
/*!40000 ALTER TABLE `user_news` DISABLE KEYS */;
INSERT INTO `user_news` VALUES (1,1,'欢迎使用西大健身','教程',0,'2022-12-03 21:52:33','2022-12-03 21:52:33');
/*!40000 ALTER TABLE `user_news` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_oauth_bind`
--

DROP TABLE IF EXISTS `user_oauth_bind`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_oauth_bind` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL DEFAULT '0' COMMENT '用户id',
  `openid` varchar(80) NOT NULL DEFAULT '' COMMENT '第三方id',
  `unionid` varchar(100) NOT NULL DEFAULT '' COMMENT '第三方用户统一标识id',
  `type` tinyint(3) unsigned NOT NULL DEFAULT '1' COMMENT '绑定类型 1：邮箱登录  2：微信开放平台 ',
  `status` tinyint(4) NOT NULL DEFAULT '1' COMMENT '状态 1：有效 0：无效',
  `updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '最后更新时间',
  `created_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '插入时间',
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `uk_user_id_openid` (`user_id`,`openid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户第三方登录绑定关系';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_oauth_bind`
--

LOCK TABLES `user_oauth_bind` WRITE;
/*!40000 ALTER TABLE `user_oauth_bind` DISABLE KEYS */;
/*!40000 ALTER TABLE `user_oauth_bind` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-13 22:44:36
