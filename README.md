# 天翼飞Young校园网认证器（Python）
基于Selenium的飞young校园网登录器

人在广州工商学院，大概适用于下图登录界面。README过段时间完善程序了再来补上。现在先提供个能用的程序

![image](https://user-images.githubusercontent.com/60568280/138116103-2bdfcc72-b6e6-4206-8a1d-7e83e1689bd4.png)

## 更新日志
### 2021.10.20
初版，能跑就行
### 2021.10.26
1. 增加了网络连通性判断
2. 增加了运行失败后自动重试的功能
3. 模块化了代码
## 使用教程
程序基于python3.8编写，以chrome浏览器为依赖运行，请先安装好python和chrome

1. Star本项目（划掉
2. clone下这个仓库到本地<br>
```git clone https://github.com/smile31768/young-authenticator.git ```
3. 安装依赖模块<br>
```pip install -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt```
4. 配置好chromedriver[参考教程]<https://www.jianshu.com/p/ffcb62574050>
4. 使用notepad打开run.py按照提示修改认证信息
5. 双击run.py
6. 你或许可以把这玩意加入定时任务，每五分钟运行一次，杜绝断网<br>
```具体定时任务设定方法不同系统不一样，请自行参照百度```
