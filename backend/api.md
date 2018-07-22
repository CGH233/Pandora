#1 用户注册

|URL|Header|Method|
|:--|:--|:--|
|/api/signup/|无|POST|

**POST data**
```
{
	"username":string,
	"password":string	
}
```
**Return data**
```
{
	"message":1  //注册成功
	"message":0  //已被注测
}
```
**Status Code**
```
200  OK
400  用户已存在/输入信息有错误
```

#2 用户登录

|URL|Header|Method|
|:--|:--|:--|
|/api/signin/|无|POST|

**POST data(json)**
```
{
	"username" : string,
	"password":string
}
```
**Return data(json)**
```
{
	"uid":int,
	"token":string   //成功
	"uid":-1,
	"token":-1    //失败
}
```
**Status Code**
```
200  OK
401  输入信息有错误
```


#3 问卷

|URL|Header|Method|
|:--|:--|:--|
|/api/questionnaire/application/`<int:uid>`/|登录Header|POST|

Header格式: token:xxxxx
 
**POST data**
```
{
	"number": int //数量
	"sgoal":[{
			"name": string,
			"hour": int,
			"ddl": string,
			"importance": int	
	},{
	...
	}]	
}
``` 
**Return data**
```
无
```
**Status Code**
```  
200  OK
502  服务器端错误
``` 

#4 个人数据

##1 状态展示

|URL|Header|Method|
|:--|:--|:--|
|/api/user/`<int:uid>`/detal/|登录Header|GET|

Header格式: `token`:`xxxxx`

**POST data**
```
无
```
**Return data**
```
{
	"username": string,
	"score": int, //金钱
	"sstaus": int,  //固定目标进度
	"pstatus": int, //个人目标进度
	"time": string,
	"goal":[{
		"importance": int, //优先级
		"name": string,
		"hour": int, //每日所需时间
		"ddl": string,
		"result": int, //完成:1 未完成:0
		"gid": int //任务id
	},
	{
	...
	}] //多个任务
}
```
**Status Code**
```
200  OK
502  服务器端错误
``` 

##2 完成任务/取消

|URL|Header|Method|
|:--|:--|:--|
|/api/user/`<int:uid>`/`<int:gid>`/result/|登录Header|POST|

Header格式: `token`:`xxxxx`

**POST data**
```
{
	"result": int
}
```
**Return data**
```
无
```
**Status Code**
```
200  OK
502  服务器端错误
``` 

##3 添加任务

|URL|Header|Method|
|:--|:--|:--|
|/api/user/`<int:uid>`/addition/|登录Header|POST|

Header格式: `token`:`xxxxx`

**POST data**
```
{
	"importance": int,
	"name": string,
	"hour": int,
	"ddl": string
}
```
**Return data**
```
{
	"gid":gid 
}
```
**Status Code**
```
200  OK
502  服务器端错误
```

##4 修改任务

|URL|Header|Method|
|:--|:--|:--|
|/api/user/`<int:uid>`/`<int:gid>`/exchange/|登录Header|POST|

Header格式: `token`:`xxxxx`

**POST data**
```
{
	"importance": int,
	"name": string,
	"hour": int,
	"ddl": string,
	"cost": int
}
```
**Return data**
```
无
```
**Status Code**
```
200  OK
502  服务器端错误
```
