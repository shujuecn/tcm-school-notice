# tcm-school-notice

这是一个爬虫项目，默认用于查询发布于**2023**年的，与**复试**相关的中医学类**硕士**研究生招生通知。该项目允许用户自定义查询字段，以便更精准地获取所需信息。具体而言，该爬虫会在指定的院校官网上搜索符合条件的通知，并将搜索结果呈现在终端。

## 使用

1. 克隆项目，安装依赖

   ```
   git clone https://github.com/shujuecn/tcm-school-notice.git
   cd tcm-school-notice
   pip3 install -r requirements.txt
   ```

2. 修改字段，启动爬虫

   ```python
   # setting.py

   NoticeType = "调剂"			# 修改需要查询的字段
   SchoolInfo = {
     "湖南中医药大学": [...],
     "湖北民族大学": [...]
   }											  # 修改需要查询的院校
   ```

3. 启动爬虫

   ```
   python3 spider.py
   ```



## 效果

* macOS Terminal
	* ![image-20230311103126169](https://p.ipic.vip/6ybl39.png)


## 已支持院校

### 27所中医药类院校

* [ ] [中国中医科学院](http://www.yjstcm.ac.cn/index.php?id=123)
* [x] [北京中医药大学](http://yanjiusheng.bucm.edu.cn/index.htm)
* [x] [河北中医学院](http://yjsxy.hebcm.edu.cn/)
* [x] [上海中医药大学](https://yjsy.shutcm.edu.cn/1125/list.htm)
* [x] [广州中医药大学](https://yjsy.gzucm.edu.cn/)
* [x] [安徽中医药大学](http://yjsb.ahtcm.edu.cn/zsjy/zsdt.htm)
* [x] [成都中医药大学](https://yjs.cdutcm.edu.cn/)
* [x] [浙江中医药大学](http://yjsgl.zcmu.edu.cn/list/19)
* [x] [天津中医药大学](http://yjsy.tjutcm.edu.cn/index.htm)
* [x] [长春中医药大学](https://y.ccucm.edu.cn/info/1087/16160.htm)
* [x] [黑龙江中医药大学](http://yjsy.hljucm.net/index.htm)
* [x] [南京中医药大学](https://gra.njucm.edu.cn/2898/list.htm)
* [x] [福建中医药大学](https://yjsy.fjtcm.edu.cn/yjsb/1390339007786/)
* [x] [广西中医药大学](http://yjsy.gxtcmu.edu.cn/Default.aspx)
* [x] [湖南中医药大学](https://yjsy.hnucm.edu.cn/zsxx/tzgg.htm)
* [x] [江西中医药大学](https://yjsy.jxutcm.edu.cn/index.htm)
* [x] [山东中医药大学](https://yjs.sdutcm.edu.cn/zsgz1.htm)
* [x] [河南中医药大学](https://yjs.hactcm.edu.cn/list-5.html)
* [x] [湖北中医药大学](https://yjs.hbtcm.edu.cn/zsgz.htm)
* [x] [云南中医药大学](http://www.yjsc.ynutcm.edu.cn/index.shtml)
* [x] [陕西中医药大学](http://yzb.sntcm.edu.cn/info/iList.jsp?cat_id=1608)
* [x] [甘肃中医药大学](http://yjsc.gszy.edu.cn/)
* [x] [山西中医药大学](https://yjsb.sxtcm.edu.cn/)
* [x] [贵州中医药大学](http://yjs.gzy.edu.cn/)
* [ ] [辽宁中医药大学](http://yjs.lnutcm.edu.cn/home)
* [ ] [山西省中医药研究院](https://www.sxzyy.com/html/web/yanjiushengjiaoyu/index.html)
* [ ] [黑龙江省中医药科学院](http://web.hljstcm.org.cn/)

### 38所其他院校

* [x] [湖北民族大学](https://www.hbmzu.edu.cn/yjsc/zsxx.htm)
* [ ] [新疆医科大学](http://yjsxy.xjmu.edu.cn/index.htm)
* [ ] [广州医科大学](https://yjs.gzhmu.edu.cn/)
* [ ] [安徽医科大学](http://yjsxy.ahmu.edu.cn/1850/list.htm)
* [ ] [西南医科大学](http://yjs.swmu.edu.cn/index.htm)
* [ ] [重庆医科大学](https://yjszs.cqmu.edu.cn/)
* [ ] [天津医科大学](http://gs.tmu.edu.cn/)
* [ ] [大连医科大学](https://yjs.dmu.edu.cn/zsgz/tzgg.htm)
* [ ] [广西医科大学](https://yjs.gxmu.edu.cn/)
* [ ] [河北医科大学](http://gschool.hebmu.edu.cn/index.aspx)
* [ ] [兰州大学](http://yz.lzu.edu.cn/zhaoshengdongtai/index.html)
* [ ] [青岛大学](https://grad.qdu.edu.cn/index.do)
* [ ] [南方医科大学](http://portal.smu.edu.cn/yzw/)
* [ ] [宁夏医科大学](http://www.nxmu.edu.cn/yjsy/)
* [ ] [锦州医科大学](http://yjsc.jzmu.edu.cn/)
* [ ] [暨南大学](https://gs.jnu.edu.cn/tzgg/list.htm)
* [ ] [广东药科大学](https://yjsxy.gdpu.edu.cn/ )
* [ ] [厦门大学](https://zs.xmu.edu.cn/sss/zsjz.htm)
* [ ] [复旦大学](http://www.gs.fudan.edu.cn/)
* [ ] [北京大学医学部](http://yjsy.bjmu.edu.cn/)
* [ ] [北京协和医学院](http://graduate.pumc.edu.cn/zsw/)
* [ ] [内蒙古医科大学](https://yjsxy.immu.edu.cn/)
* [ ] [扬州大学](http://yjsc.yzu.edu.cn/)
* [ ] [华北理工大学](http://yjsxy.ncst.edu.cn/col/1413000421816/index.html)
* [ ] [华中科技大学](http://gszs.hust.edu.cn/)
* [ ] [成都体育学院](http://yjs.cdsu.edu.cn/Web1.aspx?id=58)
* [ ] [承德医学院](http://yjs.cdmc.edu.cn/col/col145/index.html?uid=755&pageNum=1)
* [ ] [川北医学院](https://www.nsmc.edu.cn/gs/1119/1)
* [ ] [青海大学](https://yjs.qhu.edu.cn/zsgz/xlsszs/index.htm)
* [ ] [潍坊医学院](https://yjshb.wfmc.edu.cn/681/list.htm)
* [ ] [滨州医学院](https://yjszs.bzmc.edu.cn/2056/list.htm)
* [ ] [海南医学院](https://www.hainmc.edu.cn/zsw/yjszs1.htm)
* [ ] [三峡大学](https://sxdxyjsy.ctgu.edu.cn/zsgl/tzgg.htm)
* [ ] [温州医科大学](http://yjsy.wmu.edu.cn/list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1010)
* [ ] [延边大学](https://grad.ybu.edu.cn/tzgg/zs.htm)
* [ ] [中国医科大学](https://www.cmu.edu.cn/cmuyjs/zsxx/tkss.htm)
* [ ] [河北大学](http://yjsy.hbu.edu.cn/)
* [ ] [首都医科大学](https://yjsh.ccmu.edu.cn/yytz_2977/zs_3101/2b64ad2b90d649439787f3479d18cc25.htm)

## 致谢

* 所用的院校列表来源于[【青竹医考】23考研招生简章更新汇总](https://doc.weixin.qq.com/sheet/e3_ATUALgaLAH4d9vFodn1S1SWCQSoBd?scode=APQAjQf6AAY7QZQJ87ATUALgaLAH4&force_open_in_wx=1&tab=BB08J2)，感谢青竹的分享！
* 感谢ChatGPT、New Bing与Github Copilot的耐心指导！
* 感谢使用本程序的中医同仁，如果对该项目有任何疑问、建议或发现了错误，欢迎通过提issue的方式提交。
