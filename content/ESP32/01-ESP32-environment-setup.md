Title: ESP32 Environment Setup
Date: 2026-09-14 10:20
Category: Embedded
Tags: esp32,ubuntu,vscode
Lang: zh-CN

[TOC]

## 产品来源
淘宝购买 [ESP32-S3 N16R8](https://detail.tmall.com/item.htm?app=weixin&bc_fl_src=share-1041512994912843-2-1&bxsign=scdG-wsy5A5JpHob5iV98c4wv5aFAnHEgMvqux6Q9LZo1G0eMXLXeoOJmjdeU_Hwtcd1CWHmCYK_XVN0UNOhPvZl0f5T5vijvXWo5RAAUmtnBTigmcF2S3b1rxqTSfaDjyB&cpp=1&h5_spm=a-tb-item.b-tb-item&id=775315741690&share_crt_v=1&shareurl=true&short_name=h.8LPcQFOSLrR3L9m&sp_tk=VlBPQ1Q2Vk5pQjA%3D&spm=a2159r.13376460.0.0&tbSocialPopKey=shareItem&tk=VPOCT6VNiB0&un=535208b4d620fcbcd707d2abce2ca380&un_site=0&ut_sk=1.Ywm80VtKljgDAO%2FJEzolAHHG_21380790_1788777356234.TaoPassword-Weixin.1&wxsign=tbwlgyOXChpNjZE3Vrs7TkbbJi3757fUfRyDEKYxhLAaohOOaBwMTUKRQRScGWCL8ReTKAIIr2xXyhk-gy7AO02OuElGuKWGJplWOQ0CMF934eCr2fTV94LfqfJBNoX4nZN&x-ssr=true)

## 环境搭建
由于ESP32 windows下编译效率比较低，所以我选择的ubuntu主机和windows remote方式来实现的编译调试。
以下分为ubuntu安装步骤和windows 的ssh步骤分别介绍
### ubuntu 系统安装要求及步骤
- 使用的ubuntu系统: Ubuntu 24.04.4 LTS
- 安装eim

```
# step 1 添加乐鑫软件镜像源到ubuntu apt list
echo "deb [trusted=yes] https://dl.espressif.com/dl/eim/apt/ stable main" | sudo tee /etc/apt/sources.list.d/espressif.list
sudo apt update 

# step 2 安装eim
sudo apt install eim

# setp 3 启动eim
eim
```
- 启动eim后，点击新安装，再选择简易安装即可，静待安装完成
- 由于usb系统需要添加allow list 所以需要将如下list添加入ubuntu的路径/etc/udev/rules.d/60-openocd.rules 路径[官方参考文件路径](https://github.com/openocd-org/openocd/blob/master/contrib/60-openocd.rules)[^ai-node]
- 添加完成后执行以下命令[^ai-node]
```
sudo udevadm control --reload-rules
sudo udevadm trigger
sudo udevadm trigger
```
[^ai-node]: 此处仅需在ubuntu系统无法识别到usb设备时执行

### windows 系统安装要求
- 安装vscode
- 在vscode 安装remote ssh
- 通过remote ssh 连接ubuntu主机.
- 连接成功后，在vscode 连接成功界面添加插件ESP-IDF 插件
- 插件安装完成，点击侧边栏，选择Advanced折叠标签，选择新项目向导
![alt text](..\images\image-2.png)
- 新建hello world 工程
![alt text](..\images\image-3.png)
- 进入工程后，在Vscode下方工具条，分别点选红框选项
    - 1. USB-JTAG
    - 2. USB 选择带Espressif的tty，如果没有参照ai-node进行配置安装
    - 3. device选择esp32s3
![alt text](..\images\image-4.png)
- windows 按F1，创建ESP-IDF VSCODE configure文件
![alt text](..\images\image-5.png)
- 打开OpenOCD，这里我有踩到一个坑，如果openocd打开失败，可以在ubuntu系统执行指令 lsusb, 如果显示的303a:4001则说明芯片现在boot的模式由固件接管，那么openocd无法执行调试，此问题解决方式也简单，按照如下步骤
    - 1. 拔下usb
    - 2. 按住板子上的boot按键，插上usb，此时boot按键不要松开
    - 3. 按以下rst按键，此时boot键也不要松开
    - 4. 松开boot按键
    - 5. 再在ubuntu系统执行lsusb，就可以看到设备标识编程303a:1001了，这个状态下再去startopenocd，就可以实现调试了。

## 以上步骤都执行完，就可以实现观察代码的编译和调试了
- 点击VSCODE下方的编译按钮编译新建的工程
- 点击调试按钮即可看到debug界面了，不过这里的debug是无法实现vscode和debug断点的连接的，等我下一篇文章介绍。
![alt text](..\images\image-6.png)