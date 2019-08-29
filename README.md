# Continuous-Integration

持续集成

来源:[自动化测试开发框架My-Test-Automation-Frameworks](https://github.com/Gavinwhy/My-Test-Automation-Frameworks)

# 持续集成的实施过程

## 输入

从代码库下载源代码

调用构建工具构建新版本

将版本保存在某个特定位置

## 安装部署

定时检测新版本

保存测试版本信息

读取配置信息

自动安装部署到相应平台

备份新版本并开始运行

## 执行测试

自动启动测试脚本

运行所有测试脚本

产生测试结果日志

测试另外的平台

产生测试结果日志

生成最终的测试报告

发送邮件并归档结果

# 对持续集成的思考

## 工作流程

构建: 管理版本

SVN GIT TFS VSS \ Ant Maven Grandle

部署: 

安装 启动 文件传输 Samba FTP SSH SCP命令 容器化部署Docker

测试: 

调用测试脚本 UI 接口 性能 报告 发送报告

发布: 

根据测试情况进行评估,确定是否发布

运维: 

安装操作系统 配置服务器环境 配置网络 备份数据库 部署新版本 监控服务器运行状态 开发自动化运维脚本
