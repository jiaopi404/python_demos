## 常用 linux命令

小技巧
- `ctrl + shift + =` 放大终端字体
- `ctrl + -` 缩小

命令:

command | desc | usuage
-|-|-
ls | list | list the content of the directory
pwd | print work directory | the directory you are in
cd [dir] | change directory | --
touch [file name] | if the file is not existed, then create it
mkdir | make dir | --
rm [file name] | remove | remove the file
clear | clear | clear the screen

查阅命令: 

- command --help
- man command

## 文件和目录常用命令

- 查看目录内容
    + ls
- 切换目录
    + cd
- 创建和删除操作
    + touch
    + rm
    + mkdir
- 拷贝和移动文件
    + cp
    + mv
- 查看文件内容
    + cat
    + more
    + grep
- 其他
    + echo
    + 重定向 > 和 >>
    + 管道 |

### ls 命令说明

linux 下文件和目录的特点

- linux 文件或者目录名称最长可以到 256 字符
- 以 `.` 开头的文件为隐藏文件 ,需要用 -a 参数才能显示
- `.` 代表当前目录
- `..`代表上一级目录

#### ls 常用选项

- `-a` 所有子目录与文件, 包括隐藏
- `-l` 以列表方式显示文件的详细信息
- `-h` 配合 `-l` 以人性化的方式显示文件大小

可以连用, 比如 `ls -lah` 三个一起用, 或者 `ls -lh` 不看隐藏文件

#### ls 通配符的使用(类似正则)

通配符 | 含义
-|-|-
* | 任意个字符
? | 代表任意一个字符, 至少一个
[] | 表示可以匹配字符组中的任意一个

如, `ls 1*` 可以列出 1.txt, 123.txt

### 切换目录

#### cd

cd stands for change directory

==linux 所有的 目录 和 文件名 都是大小写敏感的==

command | desc
-|-|-
cd | 切换到当前用户的主目录(/home/用户目录)
cd ~ | 同上
cd . | 保持当前目录不变
cd .. | 上一级
cd - | 可以在最近两次工作目录之间来回切换

#### 绝对路径 / 相对路径

## 文件相关目录

### 创建和删除操作

1. touch
    + 若不存在: 创建
    + 存在: 修改最后修改时间

2. mkdir
    + 参数 `-p` 可以递归创建目录
    + 如创建: `/a/b/c/d`, `mkdir -p a/b/c/d`
    + 不允许重名

3. rm
    + 可以删除文件 或 目录
    + rm 删除后不可恢复
    + `rm -f`: 强制删除, 忽略不存在的文件, 无需提示
    + `rm -r`: 递归删除目录下内容, 删除文件夹时 必须添加此参数
    + 可以使用通配符, 清空文件夹 `rm -r *`

### 移动和拷贝文件

command | word | desc
-|-|-
tree [dir] | tree | 以树状图列出文件目录结构
cp 源文件 目标文件 | copy | 复制文件或者 dir
mv origin_file target_file | move | remove file or dir / file or dir rename

1. tree
    + `tree -d` 只显示目录

2. cp
    + `cp -i` 覆盖前提示
    + `cp -r` 若给出的源文件是目录文件, 则 cp 会递归复制该目录下的所有子目录和文件, 目标文件必须为一个目录名

3. mv
    + 可以移动文件 或 目录, 也可以重命名
    + `mv -i` 覆盖前提醒

### 查看文件内容

command | word | desc
-|-|-
cat file_name | concatenate | 查看文件内容, 创建文件, 文件合并, 追加文件内容等功能
more file_name | more | 分屏显示文件内容
grep 搜索文本 文件名 | grep | 搜索文本文件内容

1. cat
    + 会一次显示所有内容, 适合查看内容较少的文本文件
    + -b 对非空输出行编号
    + -n 对输出的所有行编号
    + 另外, linux 中还有一个 nl 命令与 cat -b 效果等价

2. more
    + 分屏显示, 每次显示一页
    + 查看内容较多的文件

operation_key | desc
-|-
space | next screen
enter | 一次滚动手册页的一行
b | back a screen
f | forward a screen
q | quit
/word | 搜索 word 字符串

3. grep
    + grep 是一种强大的文本搜索工具
    + grep 允许对文本文件进行模式查找, 所谓模式查找, 即为正则表达式

option | desc
-|-
-n | 显示匹配行及行号
-v | 显示不包含匹配行的所有行
-i | 忽略大小写

常用两种模式查找

param | desc
-|-
^a | 行首, 搜索以a 开头
ke$ | 搜索以 ke 结尾

### 其他命令

1. echo
    + 在终端中显示参数指定的文字, 通常会和重定向联合使用

2. 重定向 > and >>
    + linux允许将命令执行结果重定向到一个文件
    + 将本应该显示在终端上的内容 输出 / 追加 到指定文件中
    + `>` 表示输出, 会覆盖文件原有内容
    + `>>` 表示追加, 将内容追加到已有文件末尾

3. 管道 |
    + linux 允许将 一个命令的输出 通过管道 作为 另一个命令的输入
    + 左端写入, 又端取出
    + 常用的管道命令有: more, grep


## 远程管理常用命令

- shutdown

### 1. 关机 / 重启

- shutdown option time
- -r 重新启动
- 如 `shutdown -r now`
- 不指定选项和参数, 默认 1 分钟后关闭电脑
- 远程维护服务器时, 最好不要关闭系统, 应重启系统
- `shutdown -c` 取消
- `shutwdown now` 立即关机
- `shutdown 20:25`
- `shutdown +10` 再过十分钟后关机

### 2.1 网卡 和 ip 地址

网卡:
- 专门负责网络通讯的 硬件设备
- ip 地址是设置在网卡上的地址信息(SIM 卡 与 电话号)

ip 地址
- 每台电脑都有ip, 保证电脑之间正常通讯
- ip不能相同, 否则地址冲突

### 2.2 ifconfig

- `ifconfig | grep inet` 查看 / 配置 计算机当前的网卡配置信息
- 一台计算机中可能会有一个物理网卡 和 多个虚拟网卡, 在 linux 中, 物理网卡的名字通常以`ensXX`
- `127.0.0.1` 本地回环 / 换回 地址, 一般测试本机网卡是否正常

### 2.3 ping

- `ping ip_address` 检测目标主机是否连接正常
    + 有连接, 会接到包, 时间越长, 速度越慢
    + 没有连接, `unreachable`
- `ping 127.0.0.7` 检测本地网卡是否正常
- 原理类似潜水艇

### 3. 远程登陆和复制文件

command | e_word | desc
-|-|-
ssh username@ip | secure shell | shutdown / reboot
`scp username@ip:[filename or path] username@ip:[filename or path]` | secure copy | 远程复制文件

#### 3.1 ssh (important)

在 linux 中 ssh 是非常常用的工具, 通过 ssh 客户端, 我们可以连接到运行了 ssh 服务器的远程机器上

`ssh client <= 加密, 压缩 =>ssh server`

- ssh client 是使用 `Secure Shell (SSH)` 协议连接到远程计算机的软件程序
- ssh 是目前比较可靠, 专为远程登陆绘画和其他网络服务 提供安全性的协议
    + 有效防止远程管理中的 信息泄露
    + 对数据加密, 防止 DNS 欺骗 和 ip 欺骗
- 压缩, 加快速度

域名: ip 别名
款口号:

serve | port
-|-
SSH server | 22
Web server | 80
HTTPS | 443
FTP server | 21

==SSH client==

`ssh [-p port] user@remote`
- user: username
- remote: ip / domain_name
- port: ssh server 监听的端口, 不指定即为22


- exit 推出当前用户登陆
- ssh 终端命令只能在 linux or unix 系统使用
- windows: 安装 PuTTY or XShell 客户端软件


- `sudo ...` 超级用户


==windows 下 SSH 客户端的安装==

- Putty
- XShell


#### 3.2 scp (important)

scp is secure copy: 远程拷贝文件

他的地址可是与 ssh 基本相同, 但是 ==指定端口时使用的时大写的 `-P`==

==`-r` 复制文件夹==

```ssh
// local -> remote /home/Desktop/01.py
// 相对路径, 以用户 home 作为参照路径
scp -P port 01.py user@remote:Desktop/01.py

// remote /home/Desktop/01.py -> local
scp -P port user@remote:Desktop/01.py 01.py

```

param | desc
-|-
`-r` | 必须为目录名, 递归复制该文件夹下所有内容
`-P` | 若端口不是 22, 指定端口