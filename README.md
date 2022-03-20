# CampusNetwork-AutoLogin
用于广西农业职业技术大学校园网登录

大一的时候发现校园网每天都要重新登录一次，烦得要死 所以当时弄了个脚本

通过树莓派/openwrt等设置定时任务运行即可实现每天自动登录

# 运行环境
- Python3.x
- Linux
- Windows

# 配置方法
- StudentID #学号
- Password  #密码
- Operator  #联通unicom 电信telecom 运营商选择
- Retry     #True开启 False关闭 用于登录失败后是否重试（无限重试，直到登录成功才结束进程）
