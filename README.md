# 小石课表回顾总结

- ***动机***

  1. 先前所用的“超级课程表”使用体验过差（启动慢，广告多，UI丑，体积大，功能杂）
  2. 兴趣驱动，联想我掌握的知识能否自己做一个课程表app来用？

- ***怎么做一个app？***

  1. **原生开发**

     - 安卓原生

       页面语言（XML），逻辑语言（java，但现在更多转kotlin），开发环境（要对安卓系统和生态有一定了解）以及开发工具（Android Studio和SDK）

     - ios原生

       Objective - C或Swift结合Xcode，ios开发在国内比较冷门，我不是很了解

     - 鸿蒙原生

       ArkTs为主的一系列华为提供的开发方案，目前也比较冷门，但在国内来说应该比ios好一点，未来发展也应该不错

  2. **H5封装**

     完全基于web前端技术，上手最快，但性能最差（i川农就是一个很典型的例子），因为其本质一般都是网页套壳一个webview（具体还要看框架是怎么实现的）

  3. **混合开发**

     基本基于web前端技术，主要有React Native,Ionic,Flutter等等，性能和开发难度介于前两者之间

- ***小石课技术栈***

  架构：前后端分离

  后端：Flask(python的一个轻量级web框架)+requests(python的网络请求库)+re(python内置正则表达式库)

  前端：vue3+uniapp(dcloud公司旗下的前端框架)

  服务器及环境：阿里云学生活动白嫖的十个月云服务器+Linux发行版（Ubuntu22)+宝塔面板（封装了linux上的文件操作且使文件系统可视化，适合非专业运维人员）+uwsgi+nginx+python3.10

- ***问题及反馈***

    优化建议：

  1. 目前app裸体积57MB左右，仍可通过精简页面和功能压缩10MB以上，小石课持续追求“小而美”
  2. 优化本地存储的结构，进一步减小用户数据占用的存储

    推广建议：

      1. 解决用户信任问题（担心教务网密码被开发者后台看到），解决方法（改变导课模式，架构改为纯前端，即在app端跳转教务网后获取课程原始html后将现有的基于python的清洗代码转义为js）（app备案）
      1. 多平台推广（目前只有安卓端，ios端尚未打包，鸿蒙端赛道太小暂不考虑）
      1. 邀请感兴趣的小伙伴一起完善优化小石课
