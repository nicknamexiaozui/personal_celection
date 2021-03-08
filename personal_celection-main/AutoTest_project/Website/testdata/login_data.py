#正常场景 测试数据
# success_data = {"user":"test","passwd":"123456"}
success_data = {"user":"sys_admin","passwd":"123456","yanzm":"1234"}
#异常，无输入时，登录
kong_data = {"user":"","passwd":"","yanzm":""}
#用户不存在
nouser_data = {"user":"sys_admin1","passwd":"123456","yanzm":"1234"}
#用户密码错误
errorpasswd_data = {"user":"sys_admin","passwd":"1234567","yanzm":"1234"}
#系统管理员
sysadmin_data = {"user":"sys_admin","passwd":"123456","yanzm":"1234"}
#安全管理员
secadmin_data = {"user":"sys_admin","passwd":"123456","yanzm":"1234"}
#审计管理员
audadmin_data = {"user":"sys_admin","passwd":"123456","yanzm":"1234"}
