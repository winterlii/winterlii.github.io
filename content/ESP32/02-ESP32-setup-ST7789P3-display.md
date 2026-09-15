Title: ESP32 setup ST7789P3 display
Date: 2026-09-15 19:00
Category: Embedded
Tags: ESP32,lvgl
Lang: zh-CN

[TOC]

## Hardware Prepare
- ESP32-s3 develop board 淘宝购买 [ESP32-S3 N16R8](https://detail.tmall.com/item.htm?app=weixin&bc_fl_src=share-1041512994912843-2-1&bxsign=scdG-wsy5A5JpHob5iV98c4wv5aFAnHEgMvqux6Q9LZo1G0eMXLXeoOJmjdeU_Hwtcd1CWHmCYK_XVN0UNOhPvZl0f5T5vijvXWo5RAAUmtnBTigmcF2S3b1rxqTSfaDjyB&cpp=1&h5_spm=a-tb-item.b-tb-item&id=775315741690&share_crt_v=1&shareurl=true&short_name=h.8LPcQFOSLrR3L9m&sp_tk=VlBPQ1Q2Vk5pQjA%3D&spm=a2159r.13376460.0.0&tbSocialPopKey=shareItem&tk=VPOCT6VNiB0&un=535208b4d620fcbcd707d2abce2ca380&un_site=0&ut_sk=1.Ywm80VtKljgDAO%2FJEzolAHHG_21380790_1788777356234.TaoPassword-Weixin.1&wxsign=tbwlgyOXChpNjZE3Vrs7TkbbJi3757fUfRyDEKYxhLAaohOOaBwMTUKRQRScGWCL8ReTKAIIr2xXyhk-gy7AO02OuElGuKWGJplWOQ0CMF934eCr2fTV94LfqfJBNoX4nZN&x-ssr=true)
- 转接板, 嘉立创打样
- ST7789 屏幕
- 其他硬件：排针，排母，按键

### 硬件到齐后进行组装
以下是IO接口顺序
| ESP32-S3 | ST7789 |
| --- | --- |
| GND | GND |
| V3P3 | VCC |
| GIO12 | SCL |
| GIO11 | SDA |
| GIO3  | RST |
| GIO4  | DC |
| GIO10 | CS |
| GIO9  | BL |

## 软件开发步骤
0. 我现在使用的IDF版本是6.1
1. 依照 [01-ESP32-environment-setup](01-ESP32-environment-setup.md) 搭建好环境
2. 登录ubuntu系统
3. 打开IDF插件-> Command -> Advanced -> New project 
4. 新建项目向导中选择-> ESP-IDF Example -> Pripherials -> lcd -> tjpgd
5. 打开main函数的， 路径在main\lcd_tjpgd_example_main.c
6. 修改第32 - 39 行 如下
```
#define EXAMPLE_LCD_BK_LIGHT_ON_LEVEL  1
#define EXAMPLE_LCD_BK_LIGHT_OFF_LEVEL !EXAMPLE_LCD_BK_LIGHT_ON_LEVEL
#define EXAMPLE_PIN_NUM_DATA0          11  /*!< for 1-line SPI, this also refereed as MOSI */
#define EXAMPLE_PIN_NUM_PCLK           12
#define EXAMPLE_PIN_NUM_CS             10
#define EXAMPLE_PIN_NUM_DC             4
#define EXAMPLE_PIN_NUM_RST            3
#define EXAMPLE_PIN_NUM_BK_LIGHT       9
```
7. 点击VSCODE底部工具栏的小扳手进行编译，点击闪电进行下载，至此，屏幕上应该就会显示ESP32S的图片了