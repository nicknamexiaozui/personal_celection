#新增域时输入正常的数据,每次测试时需修改yuname和yusuperaccount对应的值（系统具有唯一信）
normal_data = {"sysadminpasswd":"123456","yuname":"wugui8.com","maxusers":"120","yusuperaccount":"superwugui8",
               "yusuperofname":"ceshi","yusystempasswd":"123456","confirmpasswd":"123456"}
#空数据
kong_data = {"sysadminpasswd":"","yuname":"","maxusers":"","yusuperaccount":"",
               "yusuperofname":"","yusystempasswd":"","confirmpasswd":""}
#系统管理员密码错误
systempasswdwrong_data = {"sysadminpasswd":"12345","yuname":"wuguii4.com","maxusers":"120","yusuperaccount":"superwuguii4",
               "yusuperofname":"ceshi","yusystempasswd":"123456","confirmpasswd":"123456"}
#域超级管理员账号已经注册
nameused_data = {"sysadminpasswd":"12345","yuname":"wugui4.com","maxusers":"120","yusuperaccount":"superwugui4",
               "yusuperofname":"ceshi","yusystempasswd":"123456","confirmpasswd":"123456"}
#域名称已被注册
yunameused_data = {"sysadminpasswd":"123456","yuname":"wugui4.com","maxusers":"120","yusuperaccount":"superwugui4",
               "yusuperofname":"ceshi","yusystempasswd":"123456","confirmpasswd":"123456"}
