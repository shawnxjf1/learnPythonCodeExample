## 安装
pip install crypto ## 注意crypto c不是大写
pip install rsa

## 2019年3月14日 windows上安装
C:\Users\58pc>pip install crpto
Collecting crpto
  Could not find a version that satisfies the requirement crpto (from versions: )
No matching distribution found for crpto

解决办法：
C:\Users\58pc>pip install crypto  -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
Looking in indexes: http://pypi.douban.com/simple/
