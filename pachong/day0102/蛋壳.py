
from bs4 import BeautifulSoup
import requests

# html_str = """
# <!DOCTYPE html>
# <html>
# <head>
#     <meta charset="utf-8"/>
#     <title>杭州租房网_杭州市白领公寓个人房源出租_靠谱房屋价格信息平台_蛋壳公寓官网</title>
#     <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
#     <meta name='keywords' content='杭州租房网,白领公寓出租价格,杭州靠谱房屋租赁信息网,杭州出租房屋信息,蛋壳公寓靠谱,上市租房信息'>
#     <meta name="applicable-device" content="pc,mobile">
#     <meta name="MobileOptimized" content="width"/>
#     <meta name="HandheldFriendly" content="true"/>
#     <meta name="description"
#           content="杭州蛋壳公寓官网为您提供杭州市个人房源费用信息平台,专为城市白领打造轻时尚最好公寓出租,杭州租房,合租房,整租房,上市租房就找蛋壳公寓.蛋壳公寓让租房变的简单快乐."/>
#     <link rel="icon" type="image/x-icon" href="//pangu-s1.danke.com.cn/favicon.ico">
#     <!-- Set render engine for multi engine browser -->
#     <meta name="renderer" content="webkit">
#     <!-- Disable Baidu Siteapp -->
#     <meta http-equiv="Cache-Control" content="no-siteapp"/>
#     <meta http-equiv="Cache-Control" content="no-transform "/>
#     <link media="all" type="text/css" rel="stylesheet" href="//pangu-s1.danke.com.cn/build/bower/bootstrap/dist/css/bootstrap-ec3bb52a00.min.css">
#
#     <link media="all" type="text/css" rel="stylesheet" href="//pangu-s2.danke.com.cn/build/css/swiper-0b941af5db.min.css">
#
#     <link media="all" type="text/css" rel="stylesheet" href="//pangu-s1.danke.com.cn/build/css/website/common-018d1d65a5.css">
#
#
#     <script src="//pangu-s1.danke.com.cn/build/bower/jquery/dist/jquery-2f6b11a7e9.min.js"></script>
#
#     <script src="//pangu-s2.danke.com.cn/build/bower/bootstrap/dist/js/bootstrap-5869c96cc8.min.js"></script>
#
#     <script src="//pangu-s1.danke.com.cn/build/js/pc_home/swiper-3-cd2bffb7f2.3.1.min.js"></script>
#
#     <script src="//pangu-s1.danke.com.cn/build/js/md5-ea27c6f755.min.js"></script>
#
#     <script src="//pangu-s1.danke.com.cn/build/js/pc_home/city-b83380172d.js"></script>
#
#     <script src="//pangu-s3.danke.com.cn/build/js/website/public-2fcd575a2f.js"></script>
#
#     <script src="//pangu-s1.danke.com.cn/build/js/sensors-analytics/sa-8f9c5970ba.js"></script>
#
#     <script src="//pangu-s3.danke.com.cn/build/js/sensors-analytics/sa-method-b2b96e8e3e.js"></script>
#
#         <link media="all" type="text/css" rel="stylesheet" href="//pangu-s1.danke.com.cn/build/css/list_base-13b76f8ba2.css">
#
#     <script>
#         var _hmt = _hmt || [];
#         (function () {
#             var hm = document.createElement("script");
#             hm.src = "//hm.baidu.com/hm.js?814ef98ed9fc41dfe57d70d8a496561d";
#             var s = document.getElementsByTagName("script")[0];
#             s.parentNode.insertBefore(hm, s);
#         })();
#     </script>
#     <script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");
#         document.write(unescape("%3Cspan id='cnzz_stat_icon_1271579284'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s13.cnzz.com/z_stat.php%3Fid%3D1271579284%26show%3Dpic1' type='text/javascript'%3E%3C/script%3E"));</script>
#     <style>
#         [id^="cnzz_stat_icon_"] {
#             display: none;
#         }
#     </style>
#     <script> (function () {
#             var bp = document.createElement('script');
#             var curProtocol = window.location.protocol.split(':')[0];
#             if (curProtocol === 'https') {
#                 bp.src = 'https://zz.bdstatic.com/linksubmit/push.js';
#             }
#             else {
#                 bp.src = 'http://push.zhanzhang.baidu.com/push.js';
#             }
#             var s = document.getElementsByTagName("script")[0];
#             s.parentNode.insertBefore(bp, s);
#         })(); </script>
#     <script>
#         var id = '';
#         $.ajax({
#             type: 'GET',
#             url: '/web-api/user/info',
#             async: false,
#             error: function (msg) {
#                 console.log(msg)
#             },
#             success: function (data) {
#                 id = data.data.mobile || '';
#             },
#         })
#
#         sa.register({
#             'platformType': 'PC',
#             'pid': 'dankegongyu_customer',
#             'cid': 'hz',
#             'ucid': id,
#             'uuid': id,
#             'ssid': id,
#             'lmei': '',
#             'android_id': '',
#             'idfa': '',
#             'idfv': '',
#             'mac_id': '',
#         });
#         $(function () {
#             $('.nav-owner').click(function () {
#                 saMethod.ClickingHomepage('月租', $(this).attr('key') || '', '', '')
#             })
#         })
#
#         //sa.quick('autoTrack');
#
#         function GetUrlParam(paraName) {
#             var url = document.location.toString();
#             var arrObj = url.split("?");
#
#             if (arrObj.length > 1) {
#                 var arrPara = arrObj[1].split("&");
#                 var arr;
#
#                 for (var i = 0; i < arrPara.length; i++) {
#                     arr = arrPara[i].split("=");
#
#                     if (arr != null && arr[0] == paraName) {
#                         return arr[1];
#                     }
#                 }
#                 return "";
#             } else {
#                 return "";
#             }
#         }
#     </script>
#     </head>
#
#
# <!--[if lte IE 8]>
# <script src="//pangu-s2.danke.com.cn/build/js/pc_home/html5shiv-0ce8f35589.js"></script>
#
# <script src="//pangu-s2.danke.com.cn/build/js/pc_home/respond-972b9d5576.min.js"></script>
#
# <![endif]-->
#
# <!--[if lt IE 8]>
# <div class="alert-danger text-center">您正在使用<strong>过时</strong>的浏览器，本网站不能很好的支持。
#     <a href="http://browser.qq.com/" target="_blank">立即使用最新QQ浏览器</a> 获得更好的使用体验！
# </div>
# <![endif]-->
#
# <body>
# <input type="hidden" value="400-666-2738" id="zjhPhoneNumber">
# <input type="hidden" value="hz" name="website-city-code">
# <input type="hidden" value="找房" name="website-page-name">
# <input type="hidden" name="_token" value="KiXUcaP7ZnsekTKv11DFkSEe3dMiunS48lkBbC16">
# <div class="danke_header" id="topbar" data-spy="affix" data-offset-top="32">
#     <div class="wibsite-center header-center">
#
#         <div class="logo fl">
#             <a href="/"><img src="//public.danke.com.cn/public-20181123-Fv8X-dI45m6srAWMQkW3mRfqXntE" title="蛋壳公寓官网"
#                              alt="蛋壳公寓官网"></a>
#             <h2 style="display: none;">蛋壳公寓官网，租房，整租，合租</h2>
#         </div>
#         <div class="fl dkcity hd-sprite-ab">
#             <span id="dropdownMenu1" data-toggle="dropdown"><i></i>杭州</span>
#             <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
#                                     <li><a href="javascript:void(0)" rel="bj">北京市</a></li>
#                                     <li><a href="javascript:void(0)" rel="sz">深圳市</a></li>
#                                     <li><a href="javascript:void(0)" rel="sh">上海市</a></li>
#                                     <li><a href="javascript:void(0)" rel="hz">杭州市</a></li>
#                                     <li><a href="javascript:void(0)" rel="tj">天津市</a></li>
#                                     <li><a href="javascript:void(0)" rel="wh">武汉市</a></li>
#                                     <li><a href="javascript:void(0)" rel="nj">南京市</a></li>
#                                     <li><a href="javascript:void(0)" rel="gz">广州市</a></li>
#                                     <li><a href="javascript:void(0)" rel="cd">成都市</a></li>
#                                     <li><a href="javascript:void(0)" rel="gs">苏州市</a></li>
#                             </ul>
#         </div>
#         <div class="nav fl">
#             <a href="/" data-subject="首页">首页</a>
#             <a href="https://www.danke.com/room/hz" data-subject="找房">找房</a>
#             <a href="/recommend-list/hz?rent_type=joint_rent" data-subject="合租">合租</a>
#             <a href="/recommend-list/hz?rent_type=entire_rent" data-subject="整租">整租</a>
#             <a href="/rent-cycle-recommend/hz?rent_cycle=1" data-subject="月租" class="nav-owner">
#                 月租
#                 <img src="https://public.danke.com.cn/public-20181026-Fk40x9Wf9fpcZcvRlpfytkExj3k9" alt="月租图标"
#                      class="owner-gray-icon">
#             </a>
#             <a href="https://www.danke.com/about/yezhu.html"
#                data-subject="业主">业主</a>
#             <a href="https://www.danke.com/about/aboutus.html"
#                data-subject="关于">关于</a>
#             <a href="/easy-rent-recommend" data-subject="轻松整租" class="nav-owner" style="display: none!important;">
#                 轻松整租
#                 <img src="https://public.danke.com.cn/public-20181106-Fjn7IEUAr9PgMQIsxkj3Lt77w-rh" alt="轻松整租图标"
#                      class="owner-gray-icon">
#             </a>
#         </div>
#                     <a class="dklogin fr" href="/user-center/login.html">登录</a>
#                 <div class="dkphone fr">
#             <div class="serphoen fl hd-sprite-ab">
#                 <label></label>
#                 <span>服务时间：09:00 ~ 21:00</span>
#             </div>
#         </div>
#     </div>
# </div>
# <div class="right-fixed">
#     <div class="fixed-wrapper">
#         <div class="scroll-to-top">
#             <a href="javascript:void(0)" target="_parent"></a>
#         </div>
#         <div class="scroll-to-app">
#             <a href="javascript:void(0)"></a>
#             <div>
#                 <span></span>
#                 <img src="https://public.danke.com.cn/public-20180519-FnAV1svjF0c8wOsSWq7SpdfEKGzX" alt="app下载">
#                 <p>扫描下载蛋壳APP</p>
#             </div>
#         </div>
#         <div class="scroll-to-phone">
#             <a href="javascript:void(0)"></a>
#             <div>
#                 <img src="https://public.danke.com.cn/public-20180519-Fq8UiGCwbNXfmt4u4-DDZLkzBEQN" alt="客服电话图片">
#                 <span>400-666-2738</span>
#             </div>
#         </div>
#         <div class="scroll-to-xcx">
#             <a href="javascript:void(0)"></a>
#             <div>
#                 <span class="xcx-close"></span>
#                 <span></span>
#                 <img src="https://public.danke.com.cn/public-20180606-Fma_F2IgLSK0VW-TZVo5UokQpm6w"
#                      style="width:95px;height:95px" alt="app下载">
#                 <p>小程序找房更容易</p>
#             </div>
#         </div>
#
#         <div class="custom_huose" data-toggle="modal" data-target="#orderRoom" style="position:relative;top: 15px;">
#             <img src="https://public.danke.com.cn/public-20181122-FlZjLr74CPQQXfkPbMZ0l4-BLJGE" alt="房源定制">
#         </div>
#     </div>
# </div>
# <div class="website-main">
#         <input type="hidden" name="" id="windowId" value="list">
#         <div class="wrapper">
#             <div class="shade"></div>
#     <div class="header-crumbs">
#         <a target="_blank" href="/">蛋壳公寓</a>>
#         <a target="_blank" href="/room/bj">杭州租房</a>
#                                     </div>
#     <div class="search-header-wrapper">
#         <div class="search-header">
#             <div class="logo-wrapper">
#                 <a class="search-logo" href="/"><img src="//public.danke.com.cn/public-20180112-FgKd1DNNCyC_3Jq8dqbMIX7oCLCA" alt="蛋壳公寓官网"></a>
#             </div>
#             <div class="nav-help fl"></div>
#             <div class="screen-wrapper">
#                             <div class="btn-wrapper">
#                     <div class="default-btn">区域</div>
#                     <div class="screen-item">
#                         <div class="div">
#                             <div class="option_list" style="padding-bottom: 0;">
#                                 <a
#                                 class="onlist qy">区域</a>
#
#                                 <a
#                                 class=" dt">地铁</a>
#                             </div>
#                             <dl class="dl_lst list area" >
#                                 <dd>
#                                                                             <div class="option_list" style="display: block;">
#                                             <a href="https://www.danke.com/room/hz"
#                                                 class="onlist">不限</a>
#
#                                                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA.html"
#                                                         class="">
#                                                         滨江区
#                                                     </a>
#                                                     <div class="sub_option_list">
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E8%A5%BF%E5%85%B4.html"
#                                                                 class="">
#                                                                 西兴
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E9%95%BF%E6%B2%B3%E8%B7%AF.html"
#                                                                 class="">
#                                                                 长河路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E5%A5%A5%E4%BD%93%E4%B8%AD%E5%BF%83.html"
#                                                                 class="">
#                                                                 奥体中心
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E7%99%BD%E9%A9%AC%E6%B9%96.html"
#                                                                 class="">
#                                                                 白马湖
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E5%BD%A9%E8%99%B9%E5%9F%8E.html"
#                                                                 class="">
#                                                                 彩虹城
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E6%B5%A6%E6%B2%BF.html"
#                                                                 class="">
#                                                                 浦沿
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E6%BB%A8%E5%92%8C%E8%B7%AF.html"
#                                                                 class="">
#                                                                 滨和路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E6%9D%A8%E5%AE%B6%E5%A2%A9.html"
#                                                                 class="">
#                                                                 杨家墩
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E6%98%9F%E6%B0%91.html"
#                                                                 class="">
#                                                                 星民
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E6%B1%9F%E9%99%B5%E8%B7%AF.html"
#                                                                 class="">
#                                                                 江陵路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E4%B8%AD%E5%8C%BB%E8%8D%AF%E5%A4%A7%E5%AD%A6.html"
#                                                                 class="">
#                                                                 中医药大学
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E8%81%94%E5%BA%84.html"
#                                                                 class="">
#                                                                 联庄
#                                                             </a>
#                                                                                                             </div>
#                                                 </div>
#                                                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA.html"
#                                                         class="">
#                                                         西湖区
#                                                     </a>
#                                                     <div class="sub_option_list">
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B8%B0%E6%BD%AD%E8%B7%AF.html"
#                                                                 class="">
#                                                                 丰潭路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%8C%AF%E5%8D%8E%E8%B7%AF.html"
#                                                                 class="">
#                                                                 振华路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B8%89%E5%A2%A9.html"
#                                                                 class="">
#                                                                 三墩
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%96%87%E4%B8%80%E8%A5%BF%E8%B7%AF.html"
#                                                                 class="">
#                                                                 文一西路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E7%BF%A0%E8%8B%91.html"
#                                                                 class="">
#                                                                 翠苑
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%8F%A4%E8%8D%A1.html"
#                                                                 class="">
#                                                                 古荡
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E9%BB%84%E9%BE%99.html"
#                                                                 class="">
#                                                                 黄龙
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%98%89%E7%BB%BF.html"
#                                                                 class="">
#                                                                 嘉绿
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B9%9D%E8%8E%B2.html"
#                                                                 class="">
#                                                                 九莲
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E7%95%99%E4%B8%8B.html"
#                                                                 class="">
#                                                                 留下
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%B8%85%E6%B3%A2.html"
#                                                                 class="">
#                                                                 清波
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%96%87%E4%B8%89%E8%A5%BF%E8%B7%AF.html"
#                                                                 class="">
#                                                                 文三西路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E8%A5%BF%E6%BA%AA.html"
#                                                                 class="">
#                                                                 西溪
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%AD%A6%E5%86%9B.html"
#                                                                 class="">
#                                                                 学军
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B9%8B%E6%B1%9F.html"
#                                                                 class="">
#                                                                 之江
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E8%BD%AC%E5%A1%98.html"
#                                                                 class="">
#                                                                 转塘
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%B5%99%E5%A4%A7%E7%B4%AB%E9%87%91%E6%B8%AF.html"
#                                                                 class="">
#                                                                 浙大紫金港
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%AD%A6%E9%99%A2%E8%B7%AF.html"
#                                                                 class="">
#                                                                 学院路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%B1%B1%E6%B0%B4.html"
#                                                                 class="">
#                                                                 山水
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E9%87%91%E5%AE%B6%E6%B8%A1.html"
#                                                                 class="">
#                                                                 金家渡
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%B1%9F%E5%9F%8E%E8%B7%AF.html"
#                                                                 class="">
#                                                                 江城路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%8F%A4%E5%A2%A9%E8%B7%AF.html"
#                                                                 class="">
#                                                                 古墩路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E7%99%BD%E6%B4%8B.html"
#                                                                 class="">
#                                                                 白洋
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%A2%A9%E7%A5%A5%E8%A1%97.html"
#                                                                 class="">
#                                                                 墩祥街
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E8%92%8B%E6%9D%91.html"
#                                                                 class="">
#                                                                 蒋村
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B8%8B%E5%AE%81%E6%A1%A5.html"
#                                                                 class="">
#                                                                 下宁桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%96%87%E6%96%B0.html"
#                                                                 class="">
#                                                                 文新
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B8%89%E5%9D%9D.html"
#                                                                 class="">
#                                                                 三坝
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E8%99%BE%E9%BE%99%E5%9C%A9.html"
#                                                                 class="">
#                                                                 虾龙圩
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%8F%A4%E7%BF%A0%E8%B7%AF.html"
#                                                                 class="">
#                                                                 古翠路
#                                                             </a>
#                                                                                                             </div>
#                                                 </div>
#                                                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA.html"
#                                                         class="">
#                                                         拱墅区
#                                                     </a>
#                                                     <div class="sub_option_list">
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E7%94%B3%E8%8A%B1.html"
#                                                                 class="">
#                                                                 申花
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%8D%8A%E5%B1%B1.html"
#                                                                 class="">
#                                                                 半山
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%A4%A7%E5%85%B3.html"
#                                                                 class="">
#                                                                 大关
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%BE%B7%E8%83%9C.html"
#                                                                 class="">
#                                                                 德胜
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E4%B8%81%E6%A1%A5.html"
#                                                                 class="">
#                                                                 丁桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%8B%B1%E5%AE%B8%E6%A1%A5.html"
#                                                                 class="">
#                                                                 拱宸桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%8B%BE%E5%BA%84.html"
#                                                                 class="">
#                                                                 勾庄
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%92%8C%E7%9D%A6.html"
#                                                                 class="">
#                                                                 和睦
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%B9%96%E5%A2%85.html"
#                                                                 class="">
#                                                                 湖墅
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%A1%A5%E8%A5%BF.html"
#                                                                 class="">
#                                                                 桥西
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E4%B8%89%E5%A1%98.html"
#                                                                 class="">
#                                                                 三塘
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E7%9F%B3%E6%A1%A5%28%E6%9D%AD%E5%B7%9E%29.html"
#                                                                 class="">
#                                                                 石桥(杭州)
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E4%B8%87%E8%BE%BE%E5%B9%BF%E5%9C%BA.html"
#                                                                 class="">
#                                                                 万达广场
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E4%BF%A1%E4%B9%89%E5%9D%8A.html"
#                                                                 class="">
#                                                                 信义坊
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E4%B8%AD%E5%A4%A7%E9%93%B6%E6%B3%B0.html"
#                                                                 class="">
#                                                                 中大银泰
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E8%BF%90%E6%B2%B3%E5%B9%BF%E5%9C%BA.html"
#                                                                 class="">
#                                                                 运河广场
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%B2%88%E5%A1%98%E6%A1%A5.html"
#                                                                 class="">
#                                                                 沈塘桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%B1%BD%E8%BD%A6%E5%8C%97%E7%AB%99.html"
#                                                                 class="">
#                                                                 汽车北站
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%B9%96%E5%B7%9E%E8%A1%97.html"
#                                                                 class="">
#                                                                 湖州街
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%96%84%E8%B4%A4.html"
#                                                                 class="">
#                                                                 善贤
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%A4%A7%E8%BF%90%E6%B2%B3.html"
#                                                                 class="">
#                                                                 大运河
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E8%90%8D%E6%B0%B4%E8%A1%97.html"
#                                                                 class="">
#                                                                 萍水街
#                                                             </a>
#                                                                                                             </div>
#                                                 </div>
#                                                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA.html"
#                                                         class="">
#                                                         江干区
#                                                     </a>
#                                                     <div class="sub_option_list">
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%87%91%E6%B2%99%E6%B9%96.html"
#                                                                 class="">
#                                                                 金沙湖
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%BA%91%E6%B0%B4.html"
#                                                                 class="">
#                                                                 云水
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B8%8B%E6%B2%99%E6%B1%9F%E6%BB%A8.html"
#                                                                 class="">
#                                                                 下沙江滨
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E7%81%AB%E8%BD%A6%E4%B8%9C%E7%AB%99.html"
#                                                                 class="">
#                                                                 火车东站
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%87%87%E8%8D%B7.html"
#                                                                 class="">
#                                                                 采荷
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%9F%8E%E4%B8%9C%E6%96%B0%E5%9F%8E.html"
#                                                                 class="">
#                                                                 城东新城
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%A4%A7%E5%AD%A6%E5%9F%8E%E5%8C%97.html"
#                                                                 class="">
#                                                                 大学城北
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%AB%98%E6%95%99%E5%9B%AD%E5%8C%BA%E4%B8%9C.html"
#                                                                 class="">
#                                                                 高教园区东
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%AB%98%E6%95%99%E5%9B%AD%E5%8C%BA%E8%A5%BF.html"
#                                                                 class="">
#                                                                 高教园区西
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%B7%A5%E4%B8%9A%E5%9B%AD%E5%8C%97.html"
#                                                                 class="">
#                                                                 工业园北
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%8D%8E%E5%AE%B6%E6%B1%A0.html"
#                                                                 class="">
#                                                                 华家池
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%9B%9B%E5%AD%A3%E9%9D%92%28%E6%9D%AD%E5%B7%9E%29.html"
#                                                                 class="">
#                                                                 四季青(杭州)
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E7%AC%95%E6%A1%A5.html"
#                                                                 class="">
#                                                                 笕桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%99%AF%E8%8A%B3.html"
#                                                                 class="">
#                                                                 景芳
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B9%9D%E5%A0%A1.html"
#                                                                 class="">
#                                                                 九堡
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%8D%97%E8%82%96%E5%9F%A0.html"
#                                                                 class="">
#                                                                 南肖埠
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%92%B1%E6%B1%9F%E6%96%B0%E5%9F%8E.html"
#                                                                 class="">
#                                                                 钱江新城
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B8%89%E9%87%8C%E4%BA%AD.html"
#                                                                 class="">
#                                                                 三里亭
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%B2%BF%E6%B1%9F%E5%8C%97.html"
#                                                                 class="">
#                                                                 沿江北
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%B2%BF%E6%B1%9F%E5%8D%97.html"
#                                                                 class="">
#                                                                 沿江南
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%97%B8%E5%BC%84%E5%8F%A3.html"
#                                                                 class="">
#                                                                 闸弄口
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%AE%A2%E8%BF%90%E4%B8%AD%E5%BF%83.html"
#                                                                 class="">
#                                                                 客运中心
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B9%9D%E5%92%8C%E8%B7%AF.html"
#                                                                 class="">
#                                                                 九和路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%BD%AD%E5%9F%A0.html"
#                                                                 class="">
#                                                                 彭埠
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B8%83%E5%A0%A1.html"
#                                                                 class="">
#                                                                 七堡
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B8%8B%E6%B2%99%E8%A5%BF.html"
#                                                                 class="">
#                                                                 下沙西
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%92%B1%E6%B1%9F%E8%B7%AF.html"
#                                                                 class="">
#                                                                 钱江路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%BA%86%E6%98%A5%E5%B9%BF%E5%9C%BA.html"
#                                                                 class="">
#                                                                 庆春广场
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%BA%86%E8%8F%B1%E8%B7%AF.html"
#                                                                 class="">
#                                                                 庆菱路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%96%B0%E9%A3%8E.html"
#                                                                 class="">
#                                                                 新风
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%B1%9F%E9%94%A6%E8%B7%AF.html"
#                                                                 class="">
#                                                                 江锦路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%9F%8E%E6%98%9F%E8%B7%AF.html"
#                                                                 class="">
#                                                                 城星路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%96%87%E6%B5%B7%E5%8D%97%E8%B7%AF.html"
#                                                                 class="">
#                                                                 文海南路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%96%87%E6%B3%BD%E8%B7%AF.html"
#                                                                 class="">
#                                                                 文泽路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%AB%98%E6%B2%99%E8%B7%AF.html"
#                                                                 class="">
#                                                                 高沙路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B8%8B%E6%B2%99%E8%B7%AF.html"
#                                                                 class="">
#                                                                 下沙路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%96%B0%E5%A1%98.html"
#                                                                 class="">
#                                                                 新塘
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%B8%82%E6%B0%91%E4%B8%AD%E5%BF%83.html"
#                                                                 class="">
#                                                                 市民中心
#                                                             </a>
#                                                                                                             </div>
#                                                 </div>
#                                                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA.html"
#                                                         class="">
#                                                         下城区
#                                                     </a>
#                                                     <div class="sub_option_list">
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E8%A5%BF%E6%B9%96%E6%96%87%E5%8C%96%E5%B9%BF%E5%9C%BA.html"
#                                                                 class="">
#                                                                 西湖文化广场
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%BB%BA%E5%9B%BD%E5%8C%97%E8%B7%AF.html"
#                                                                 class="">
#                                                                 建国北路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%B5%81%E6%B0%B4%E8%8B%91.html"
#                                                                 class="">
#                                                                 流水苑
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%9C%9D%E6%99%96.html"
#                                                                 class="">
#                                                                 朝晖
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%BD%AE%E9%B8%A3.html"
#                                                                 class="">
#                                                                 潮鸣
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%BE%B7%E8%83%9C%E4%B8%9C.html"
#                                                                 class="">
#                                                                 德胜东
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%92%8C%E5%B9%B3.html"
#                                                                 class="">
#                                                                 和平
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E4%B8%9D%E7%BB%B8%E5%9F%8E.html"
#                                                                 class="">
#                                                                 丝绸城
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E4%BD%93%E8%82%B2%E5%9C%BA%E8%B7%AF.html"
#                                                                 class="">
#                                                                 体育场路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%A4%A9%E6%B0%B4.html"
#                                                                 class="">
#                                                                 天水
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%AD%A6%E6%9E%97.html"
#                                                                 class="">
#                                                                 武林
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E9%95%BF%E5%BA%86.html"
#                                                                 class="">
#                                                                 长庆
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E4%BC%97%E5%AE%89%E6%A1%A5.html"
#                                                                 class="">
#                                                                 众安桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%89%93%E9%93%81%E5%85%B3.html"
#                                                                 class="">
#                                                                 打铁关
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E4%B8%AD%E6%B2%B3%E5%8C%97%E8%B7%AF.html"
#                                                                 class="">
#                                                                 中河北路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%87%A4%E8%B5%B7%E8%B7%AF.html"
#                                                                 class="">
#                                                                 凤起路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%AD%A6%E6%9E%97%E9%97%A8.html"
#                                                                 class="">
#                                                                 武林门
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%AD%A6%E6%9E%97%E5%B9%BF%E5%9C%BA.html"
#                                                                 class="">
#                                                                 武林广场
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%AE%9D%E5%96%84%E6%A1%A5.html"
#                                                                 class="">
#                                                                 宝善桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%9D%AD%E6%B0%A7.html"
#                                                                 class="">
#                                                                 杭氧
#                                                             </a>
#                                                                                                             </div>
#                                                 </div>
#                                                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA.html"
#                                                         class="">
#                                                         余杭区
#                                                     </a>
#                                                     <div class="sub_option_list">
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E7%BF%A1%E7%BF%A0%E5%9F%8E.html"
#                                                                 class="">
#                                                                 翡翠城
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E4%B9%94%E5%8F%B8.html"
#                                                                 class="">
#                                                                 乔司
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E6%9C%AA%E6%9D%A5%E7%A7%91%E6%8A%80%E5%9F%8E.html"
#                                                                 class="">
#                                                                 未来科技城
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E9%97%B2%E6%9E%97.html"
#                                                                 class="">
#                                                                 闲林
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E6%98%9F%E6%A1%A5.html"
#                                                                 class="">
#                                                                 星桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E4%B9%94%E5%8F%B8%E5%8D%97.html"
#                                                                 class="">
#                                                                 乔司南
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E7%BF%81%E6%A2%85.html"
#                                                                 class="">
#                                                                 翁梅
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E5%8D%97%E8%8B%91.html"
#                                                                 class="">
#                                                                 南苑
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E6%9D%9C%E7%94%AB%E6%9D%91.html"
#                                                                 class="">
#                                                                 杜甫村
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E4%BA%94%E5%B8%B8.html"
#                                                                 class="">
#                                                                 五常
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E6%9D%AD%E5%B8%88%E5%A4%A7%E4%BB%93%E5%89%8D.html"
#                                                                 class="">
#                                                                 杭师大仓前
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E8%89%AF%E7%9D%A6%E8%B7%AF.html"
#                                                                 class="">
#                                                                 良睦路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E5%88%9B%E6%99%AF%E8%B7%AF.html"
#                                                                 class="">
#                                                                 创景路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E7%BB%BF%E6%B1%80%E8%B7%AF.html"
#                                                                 class="">
#                                                                 绿汀路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E6%B0%B8%E7%A6%8F.html"
#                                                                 class="">
#                                                                 永福
#                                                             </a>
#                                                                                                             </div>
#                                                 </div>
#                                                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA.html"
#                                                         class="">
#                                                         上城区
#                                                     </a>
#                                                     <div class="sub_option_list">
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%9F%8E%E7%AB%99.html"
#                                                                 class="">
#                                                                 城站
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%A4%8D%E5%85%B4%E8%B7%AF.html"
#                                                                 class="">
#                                                                 复兴路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E9%BC%93%E6%A5%BC%28%E6%9D%AD%E5%B7%9E%29.html"
#                                                                 class="">
#                                                                 鼓楼(杭州)
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E6%B9%96%E6%BB%A8.html"
#                                                                 class="">
#                                                                 湖滨
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E8%BF%91%E6%B1%9F.html"
#                                                                 class="">
#                                                                 近江
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%8D%97%E6%98%9F.html"
#                                                                 class="">
#                                                                 南星
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E6%B8%85%E6%B3%B0.html"
#                                                                 class="">
#                                                                 清泰
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E6%9C%9B%E6%B1%9F.html"
#                                                                 class="">
#                                                                 望江
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E9%9B%84%E9%95%87%E6%A5%BC.html"
#                                                                 class="">
#                                                                 雄镇楼
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%AE%9A%E5%AE%89%E8%B7%AF.html"
#                                                                 class="">
#                                                                 定安路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E9%BE%99%E7%BF%94%E6%A1%A5.html"
#                                                                 class="">
#                                                                 龙翔桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E6%B0%B4%E6%BE%84%E6%A1%A5.html"
#                                                                 class="">
#                                                                 水澄桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%8D%97%E6%98%9F%E6%A1%A5.html"
#                                                                 class="">
#                                                                 南星桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E7%94%AC%E6%B1%9F%E8%B7%AF.html"
#                                                                 class="">
#                                                                 甬江路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%A9%BA%E6%B1%9F%E8%B7%AF.html"
#                                                                 class="">
#                                                                 婺江路
#                                                             </a>
#                                                                                                             </div>
#                                                 </div>
#                                                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA.html"
#                                                         class="">
#                                                         萧山区
#                                                     </a>
#                                                     <div class="sub_option_list">
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E9%92%B1%E6%B1%9F%E4%B8%96%E7%BA%AA%E5%9F%8E.html"
#                                                                 class="">
#                                                                 钱江世纪城
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E9%97%BB%E5%A0%B0.html"
#                                                                 class="">
#                                                                 闻堰
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%B9%98%E6%B9%96.html"
#                                                                 class="">
#                                                                 湘湖
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E8%90%A7%E5%B1%B1%E5%BC%80%E5%8F%91%E5%8C%BA.html"
#                                                                 class="">
#                                                                 萧山开发区
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E4%B9%89%E6%A1%A5.html"
#                                                                 class="">
#                                                                 义桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E9%A3%9E%E8%99%B9%E8%B7%AF.html"
#                                                                 class="">
#                                                                 飞虹路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E5%BB%BA%E8%AE%BE%E4%B8%89%E8%B7%AF.html"
#                                                                 class="">
#                                                                 建设三路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%9B%B9%E5%AE%B6%E6%A1%A5.html"
#                                                                 class="">
#                                                                 曹家桥
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%9C%9D%E9%98%B3.html"
#                                                                 class="">
#                                                                 朝阳
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%9D%AD%E5%8F%91%E5%8E%82.html"
#                                                                 class="">
#                                                                 杭发厂
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E5%BB%BA%E8%AE%BE%E4%B8%80%E8%B7%AF.html"
#                                                                 class="">
#                                                                 建设一路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E9%87%91%E5%9F%8E%E8%B7%AF.html"
#                                                                 class="">
#                                                                 金城路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%BD%98%E6%B0%B4.html"
#                                                                 class="">
#                                                                 潘水
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E4%BA%BA%E6%B0%91%E8%B7%AF.html"
#                                                                 class="">
#                                                                 人民路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E4%BF%A1%E6%81%AF%E6%B8%AF.html"
#                                                                 class="">
#                                                                 信息港
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E7%9B%88%E4%B8%B0%E8%B7%AF.html"
#                                                                 class="">
#                                                                 盈丰路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%8C%AF%E5%AE%81%E8%B7%AF.html"
#                                                                 class="">
#                                                                 振宁路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E4%BA%BA%E6%B0%91%E5%B9%BF%E5%9C%BA.html"
#                                                                 class="">
#                                                                 人民广场
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%BB%A8%E5%BA%B7%E8%B7%AF.html"
#                                                                 class="">
#                                                                 滨康路
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E7%9B%9B%E4%B8%9C.html"
#                                                                 class="">
#                                                                 盛东
#                                                             </a>
#                                                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E4%B8%B0%E5%8C%97.html"
#                                                                 class="">
#                                                                 丰北
#                                                             </a>
#                                                                                                             </div>
#                                                 </div>
#                                                                                     </div>
#                                                                     </dd>
#                             </dl>
#                             <dl class="dl_lst list subway" style="display: none;">
#                                 <dd>
#                                                                     <div class="option_list">
#                                         <a href="https://www.danke.com/room/hz"
#                                             class="onlist">不限</a>
#
#                                                                                     <div class="area-ls-wp" style="display:inline-block;">
#                                                 <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF.html"
#                                                     class="">
#                                                     1号线
#                                                 </a>
#                                                 <div class="sub_option_list">
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%B9%98%E6%B9%96.html"
#                                                             class="">
#                                                             湘湖
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%BB%A8%E5%BA%B7%E8%B7%AF.html"
#                                                             class="">
#                                                             滨康路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E8%A5%BF%E5%85%B4.html"
#                                                             class="">
#                                                             西兴
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%BB%A8%E5%92%8C%E8%B7%AF.html"
#                                                             class="">
#                                                             滨和路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%B1%9F%E9%99%B5%E8%B7%AF.html"
#                                                             class="">
#                                                             江陵路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E8%BF%91%E6%B1%9F.html"
#                                                             class="">
#                                                             近江
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%A9%BA%E6%B1%9F%E8%B7%AF.html"
#                                                             class="">
#                                                             婺江路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%9F%8E%E7%AB%99.html"
#                                                             class="">
#                                                             城站
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%AE%9A%E5%AE%89%E8%B7%AF.html"
#                                                             class="">
#                                                             定安路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E9%BE%99%E7%BF%94%E6%A1%A5.html"
#                                                             class="">
#                                                             龙翔桥
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%87%A4%E8%B5%B7%E8%B7%AF.html"
#                                                             class="">
#                                                             凤起路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%AD%A6%E6%9E%97%E5%B9%BF%E5%9C%BA.html"
#                                                             class="">
#                                                             武林广场
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E8%A5%BF%E6%B9%96%E6%96%87%E5%8C%96%E5%B9%BF%E5%9C%BA.html"
#                                                             class="">
#                                                             西湖文化广场
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%89%93%E9%93%81%E5%85%B3.html"
#                                                             class="">
#                                                             打铁关
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E9%97%B8%E5%BC%84%E5%8F%A3.html"
#                                                             class="">
#                                                             闸弄口
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E7%81%AB%E8%BD%A6%E4%B8%9C%E7%AB%99.html"
#                                                             class="">
#                                                             火车东站
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%BD%AD%E5%9F%A0.html"
#                                                             class="">
#                                                             彭埠
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B8%83%E5%A0%A1.html"
#                                                             class="">
#                                                             七堡
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B9%9D%E5%92%8C%E8%B7%AF.html"
#                                                             class="">
#                                                             九和路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B9%9D%E5%A0%A1.html"
#                                                             class="">
#                                                             九堡
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%AE%A2%E8%BF%90%E4%B8%AD%E5%BF%83.html"
#                                                             class="">
#                                                             客运中心
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B8%8B%E6%B2%99%E8%A5%BF.html"
#                                                             class="">
#                                                             下沙西
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E9%87%91%E6%B2%99%E6%B9%96.html"
#                                                             class="">
#                                                             金沙湖
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E9%AB%98%E6%B2%99%E8%B7%AF.html"
#                                                             class="">
#                                                             高沙路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%96%87%E6%B3%BD%E8%B7%AF.html"
#                                                             class="">
#                                                             文泽路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%96%87%E6%B5%B7%E5%8D%97%E8%B7%AF.html"
#                                                             class="">
#                                                             文海南路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%BA%91%E6%B0%B4.html"
#                                                             class="">
#                                                             云水
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B8%8B%E6%B2%99%E6%B1%9F%E6%BB%A8.html"
#                                                             class="">
#                                                             下沙江滨
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B9%94%E5%8F%B8%E5%8D%97.html"
#                                                             class="">
#                                                             乔司南
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B9%94%E5%8F%B8.html"
#                                                             class="">
#                                                             乔司
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E7%BF%81%E6%A2%85.html"
#                                                             class="">
#                                                             翁梅
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%8D%97%E8%8B%91.html"
#                                                             class="">
#                                                             南苑
#                                                         </a>
#                                                                                                     </div>
#                                             </div>
#                                                                                     <div class="area-ls-wp" style="display:inline-block;">
#                                                 <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF.html"
#                                                     class="">
#                                                     5号线
#                                                 </a>
#                                                 <div class="sub_option_list">
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E6%BB%A8%E5%BA%B7%E8%B7%AF.html"
#                                                             class="">
#                                                             滨康路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%9F%8E%E7%AB%99.html"
#                                                             class="">
#                                                             城站
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E6%89%93%E9%93%81%E5%85%B3.html"
#                                                             class="">
#                                                             打铁关
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E4%BA%BA%E6%B0%91%E8%B7%AF.html"
#                                                             class="">
#                                                             人民路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%BB%BA%E5%9B%BD%E5%8C%97%E8%B7%AF.html"
#                                                             class="">
#                                                             建国北路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E4%B8%89%E5%9D%9D.html"
#                                                             class="">
#                                                             三坝
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%8D%97%E6%98%9F%E6%A1%A5.html"
#                                                             class="">
#                                                             南星桥
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%96%84%E8%B4%A4.html"
#                                                             class="">
#                                                             善贤
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%A4%A7%E8%BF%90%E6%B2%B3.html"
#                                                             class="">
#                                                             大运河
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%92%8C%E7%9D%A6.html"
#                                                             class="">
#                                                             和睦
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E8%90%8D%E6%B0%B4%E8%A1%97.html"
#                                                             class="">
#                                                             萍水街
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E6%B5%99%E5%A4%A7%E7%B4%AB%E9%87%91%E6%B8%AF.html"
#                                                             class="">
#                                                             浙大紫金港
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E8%92%8B%E6%9D%91.html"
#                                                             class="">
#                                                             蒋村
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E4%BA%94%E5%B8%B8.html"
#                                                             class="">
#                                                             五常
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E6%9D%AD%E5%B8%88%E5%A4%A7%E4%BB%93%E5%89%8D.html"
#                                                             class="">
#                                                             杭师大仓前
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E8%89%AF%E7%9D%A6%E8%B7%AF.html"
#                                                             class="">
#                                                             良睦路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E6%B0%B8%E7%A6%8F.html"
#                                                             class="">
#                                                             永福
#                                                         </a>
#                                                                                                     </div>
#                                             </div>
#                                                                                     <div class="area-ls-wp" style="display:inline-block;">
#                                                 <a href="https://www.danke.com/room/hz/l6%E5%8F%B7%E7%BA%BF.html"
#                                                     class="">
#                                                     6号线
#                                                 </a>
#                                                 <div class="sub_option_list">
#                                                                                                             <a href="https://www.danke.com/room/hz/l6%E5%8F%B7%E7%BA%BF-s%E6%B1%9F%E9%99%B5%E8%B7%AF.html"
#                                                             class="">
#                                                             江陵路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l6%E5%8F%B7%E7%BA%BF-s%E4%B8%AD%E5%8C%BB%E8%8D%AF%E5%A4%A7%E5%AD%A6.html"
#                                                             class="">
#                                                             中医药大学
#                                                         </a>
#                                                                                                     </div>
#                                             </div>
#                                                                                     <div class="area-ls-wp" style="display:inline-block;">
#                                                 <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF.html"
#                                                     class="">
#                                                     4号线
#                                                 </a>
#                                                 <div class="sub_option_list">
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E8%BF%91%E6%B1%9F.html"
#                                                             class="">
#                                                             近江
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E7%81%AB%E8%BD%A6%E4%B8%9C%E7%AB%99.html"
#                                                             class="">
#                                                             火车东站
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E5%BD%AD%E5%9F%A0.html"
#                                                             class="">
#                                                             彭埠
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E9%92%B1%E6%B1%9F%E8%B7%AF.html"
#                                                             class="">
#                                                             钱江路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%96%B0%E9%A3%8E.html"
#                                                             class="">
#                                                             新风
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%96%B0%E5%A1%98.html"
#                                                             class="">
#                                                             新塘
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%99%AF%E8%8A%B3.html"
#                                                             class="">
#                                                             景芳
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%B1%9F%E9%94%A6%E8%B7%AF.html"
#                                                             class="">
#                                                             江锦路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E5%B8%82%E6%B0%91%E4%B8%AD%E5%BF%83.html"
#                                                             class="">
#                                                             市民中心
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E5%9F%8E%E6%98%9F%E8%B7%AF.html"
#                                                             class="">
#                                                             城星路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%B5%A6%E6%B2%BF.html"
#                                                             class="">
#                                                             浦沿
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%9D%A8%E5%AE%B6%E5%A2%A9.html"
#                                                             class="">
#                                                             杨家墩
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E4%B8%AD%E5%8C%BB%E8%8D%AF%E5%A4%A7%E5%AD%A6.html"
#                                                             class="">
#                                                             中医药大学
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%B0%B4%E6%BE%84%E6%A1%A5.html"
#                                                             class="">
#                                                             水澄桥
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E5%A4%8D%E5%85%B4%E8%B7%AF.html"
#                                                             class="">
#                                                             复兴路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E5%8D%97%E6%98%9F%E6%A1%A5.html"
#                                                             class="">
#                                                             南星桥
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E7%94%AC%E6%B1%9F%E8%B7%AF.html"
#                                                             class="">
#                                                             甬江路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E8%81%94%E5%BA%84.html"
#                                                             class="">
#                                                             联庄
#                                                         </a>
#                                                                                                     </div>
#                                             </div>
#                                                                                     <div class="area-ls-wp" style="display:inline-block;">
#                                                 <a href="https://www.danke.com/room/hz/l7%E5%8F%B7%E7%BA%BF.html"
#                                                     class="">
#                                                     7号线
#                                                 </a>
#                                                 <div class="sub_option_list">
#                                                                                                             <a href="https://www.danke.com/room/hz/l7%E5%8F%B7%E7%BA%BF-s%E5%9F%8E%E7%AB%99.html"
#                                                             class="">
#                                                             城站
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l7%E5%8F%B7%E7%BA%BF-s%E5%BB%BA%E8%AE%BE%E4%B8%89%E8%B7%AF.html"
#                                                             class="">
#                                                             建设三路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l7%E5%8F%B7%E7%BA%BF-s%E5%B8%82%E6%B0%91%E4%B8%AD%E5%BF%83.html"
#                                                             class="">
#                                                             市民中心
#                                                         </a>
#                                                                                                     </div>
#                                             </div>
#                                                                                     <div class="area-ls-wp" style="display:inline-block;">
#                                                 <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF.html"
#                                                     class="">
#                                                     2号线
#                                                 </a>
#                                                 <div class="sub_option_list">
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%87%A4%E8%B5%B7%E8%B7%AF.html"
#                                                             class="">
#                                                             凤起路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%9C%9D%E9%98%B3.html"
#                                                             class="">
#                                                             朝阳
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%9B%B9%E5%AE%B6%E6%A1%A5.html"
#                                                             class="">
#                                                             曹家桥
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%BD%98%E6%B0%B4.html"
#                                                             class="">
#                                                             潘水
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%BA%BA%E6%B0%91%E8%B7%AF.html"
#                                                             class="">
#                                                             人民路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%9D%AD%E5%8F%91%E5%8E%82.html"
#                                                             class="">
#                                                             杭发厂
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%BA%BA%E6%B0%91%E5%B9%BF%E5%9C%BA.html"
#                                                             class="">
#                                                             人民广场
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%BB%BA%E8%AE%BE%E4%B8%80%E8%B7%AF.html"
#                                                             class="">
#                                                             建设一路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%BB%BA%E8%AE%BE%E4%B8%89%E8%B7%AF.html"
#                                                             class="">
#                                                             建设三路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%8C%AF%E5%AE%81%E8%B7%AF.html"
#                                                             class="">
#                                                             振宁路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E9%A3%9E%E8%99%B9%E8%B7%AF.html"
#                                                             class="">
#                                                             飞虹路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E7%9B%88%E4%B8%B0%E8%B7%AF.html"
#                                                             class="">
#                                                             盈丰路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E9%92%B1%E6%B1%9F%E4%B8%96%E7%BA%AA%E5%9F%8E.html"
#                                                             class="">
#                                                             钱江世纪城
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E9%92%B1%E6%B1%9F%E8%B7%AF.html"
#                                                             class="">
#                                                             钱江路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%BA%86%E6%98%A5%E5%B9%BF%E5%9C%BA.html"
#                                                             class="">
#                                                             庆春广场
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%BA%86%E8%8F%B1%E8%B7%AF.html"
#                                                             class="">
#                                                             庆菱路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%BB%BA%E5%9B%BD%E5%8C%97%E8%B7%AF.html"
#                                                             class="">
#                                                             建国北路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%B8%AD%E6%B2%B3%E5%8C%97%E8%B7%AF.html"
#                                                             class="">
#                                                             中河北路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%AD%A6%E6%9E%97%E9%97%A8.html"
#                                                             class="">
#                                                             武林门
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%B2%88%E5%A1%98%E6%A1%A5.html"
#                                                             class="">
#                                                             沈塘桥
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%AD%A6%E9%99%A2%E8%B7%AF.html"
#                                                             class="">
#                                                             学院路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%8F%A4%E7%BF%A0%E8%B7%AF.html"
#                                                             class="">
#                                                             古翠路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%B8%89%E5%A2%A9.html"
#                                                             class="">
#                                                             三墩
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%9D%9C%E7%94%AB%E6%9D%91.html"
#                                                             class="">
#                                                             杜甫村
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E7%99%BD%E6%B4%8B.html"
#                                                             class="">
#                                                             白洋
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E9%87%91%E5%AE%B6%E6%B8%A1.html"
#                                                             class="">
#                                                             金家渡
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%A2%A9%E7%A5%A5%E8%A1%97.html"
#                                                             class="">
#                                                             墩祥街
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E8%99%BE%E9%BE%99%E5%9C%A9.html"
#                                                             class="">
#                                                             虾龙圩
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%B8%89%E5%9D%9D.html"
#                                                             class="">
#                                                             三坝
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%96%87%E6%96%B0.html"
#                                                             class="">
#                                                             文新
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%B8%B0%E6%BD%AD%E8%B7%AF.html"
#                                                             class="">
#                                                             丰潭路
#                                                         </a>
#                                                                                                             <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%B8%8B%E5%AE%81%E6%A1%A5.html"
#                                                             class="">
#                                                             下宁桥
#                                                         </a>
#                                                                                                     </div>
#                                             </div>
#                                                                                     <div class="area-ls-wp" style="display:inline-block;">
#                                                 <a href="https://www.danke.com/room/hz/l8%E5%8F%B7%E7%BA%BF.html"
#                                                     class="">
#                                                     8号线
#                                                 </a>
#                                                 <div class="sub_option_list">
#                                                                                                             <a href="https://www.danke.com/room/hz/l8%E5%8F%B7%E7%BA%BF-s%E6%96%87%E6%B5%B7%E5%8D%97%E8%B7%AF.html"
#                                                             class="">
#                                                             文海南路
#                                                         </a>
#                                                                                                     </div>
#                                             </div>
#                                                                             </div>
#                                                                 </dd>
#                             </dl>
#                         </div>
#                     </div>
#                 </div>
#                 <div class="btn-wrapper">
#                     <div class="default-btn">价格</div>
#                     <div class="screen-item">
#                         <div class="div">
#                             <div class="option_list">
#                                 <a href="https://www.danke.com/room/hz?"
#                                 class="onlist">不限</a>
#                                                                     <a href="https://www.danke.com/room/hz/p0.html"
#                                     class="">
#                                         1500元以下
#                                     </a>
#                                                                     <a href="https://www.danke.com/room/hz/p1500.html"
#                                     class="">
#                                         1500~2000元
#                                     </a>
#                                                                     <a href="https://www.danke.com/room/hz/p2000.html"
#                                     class="">
#                                         2000~2500元
#                                     </a>
#                                                                     <a href="https://www.danke.com/room/hz/p2500.html"
#                                     class="">
#                                         2500~3000元
#                                     </a>
#                                                                     <a href="https://www.danke.com/room/hz/p3000.html"
#                                     class="">
#                                         3000元以上
#                                     </a>
#                                                             </div>
#                         </div>
#                     </div>
#                 </div>
#                 <div class="btn-wrapper">
#                     <div class="default-btn">居室</div>
#                     <div class="screen-item">
#                         <div class="div">
#                             <div class="option_list">
#                                 <a href="https://www.danke.com/room/hz?"
#                                 class="onlist">不限</a>
#
#                                                                                                                                                 <a href="https://www.danke.com/room/hz/n1.html?"
#                                         class="">一居室</a>
#                                                                                                                                                                                     <a href="https://www.danke.com/room/hz/n2.html?"
#                                         class="">两居室</a>
#                                                                                                                                                                                     <a href="https://www.danke.com/room/hz/n3.html?"
#                                         class="">三居室</a>
#                                                                                                                                                                                     <a href="https://www.danke.com/room/hz/n4.html?"
#                                         class="">四居室以上</a>
#                                                                                                 </div>
#                         </div>
#                     </div>
#                 </div>
#                 <div class="btn-wrapper">
#                     <div class="default-btn">类型</div>
#                     <div class="screen-item">
#                         <div class="div">
#                             <div class="option_list">
#                                 <a href="https://www.danke.com/room/hz?"
#                                     class="onlist">不限</a>
#
#                                 <a href="https://www.danke.com/room/hz/c%E6%95%B4%E7%A7%9F.html?"
#                                     class="">整租</a>
#
#                                 <a href="https://www.danke.com/room/hz/c%E5%90%88%E7%A7%9F.html?"
#                                     class="">合租</a>
#                             </div>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#             <form method="GET" action="https://www.danke.com/room/hz?page=1" accept-charset="UTF-8">
#             <div class="search-wrapper">
#                 <input class="search-input" type="text" name="search_text" value=""
#                         placeholder="请输入区域、地铁、小区名" autocomplete="off"/><!--
#                 --><button class="search-btn" type="submit">搜索</button><!--
#                 --><!--
#                 --><a class="map-btn" href="https://www.danke.com/map/hz?from=room" target="_blank">地图找房</a>
#             </div>
#             </form>
#         </div>
#     </div>
#
#     <div class="zf_c_box">
#         <form method="GET" action="https://www.danke.com/room/hz?page=1" accept-charset="UTF-8">
#         <div class="zf_sebox">
#             <div class="sear_menu">
#                 <!-- <img src="//public.danke.com.cn/public-20171228-FjTtnKSKO0QnS4PiivwOHIMZslgq"> -->
#                 <input type="text" class="sear_input" name="search_text" value=""
#                        placeholder="请输入区域、地铁、小区名" autocomplete="off"/><!--
#                 --><button type="submit" class="search_btn">搜索</button>
#
#                 <a class="map_btn" href="https://www.danke.com/map/hz?from=room" target="_blank">地图找房</a>
#                 <strong>&times;</strong>
#             </div>
#             <div class="sear_more">
#                 <a href="https://www.danke.com/room/hz/x%E7%8E%B0%E6%88%BF.html">现房</a>
#                 <a href="https://www.danke.com/room/hz/n1.html?from=hot_keywords">一居室</a>
#
#                                                     <a href="https://www.danke.com/room/hz?from=hot_keywords&search_text=%E5%A5%A5%E4%BD%93">奥体</a>
#                                     <a href="https://www.danke.com/room/hz?from=hot_keywords&search_text=%E4%B8%89%E5%A2%A9">三墩</a>
#                                     <a href="https://www.danke.com/room/hz?from=hot_keywords&search_text=%E4%B8%87%E8%BE%BE%E5%B9%BF%E5%9C%BA">万达广场</a>
#                                     <a href="https://www.danke.com/room/hz?from=hot_keywords&search_text=%E9%87%91%E6%B2%99%E6%B9%96">金沙湖</a>
#                                     <a href="https://www.danke.com/room/hz?from=hot_keywords&search_text=%E4%B9%9D%E5%A0%A1">九堡</a>
#                                 <a href="https://www.danke.com/room/hz">所有房源</a>
#             </div>
#         </div>
#         </form>
#         <div class="recommend-box">
#         </div>
#         <div class="filter_options">
#             <dl class="dl_lst">
#                 <dt>位置：</dt>
#                 <dd>
#                     <div class="option_list">
#                          <a id="qy"
#                             class="onlist">区域</a>
#
#                          <a id="dt"
#                             class="">地铁</a>
#                      </div>
#                  </dd>
#             </dl>
#             <dl class="dl_lst list area" >
#                 <dd>
#                                             <div class="option_list" style="display: block;">
#                             <a href="https://www.danke.com/room/hz"
#                                 class="onlist">不限</a>
#
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA.html"
#                                     class="">
#                                     滨江区
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E8%A5%BF%E5%85%B4.html"
#                                                 class="">
#                                                 西兴
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E9%95%BF%E6%B2%B3%E8%B7%AF.html"
#                                                 class="">
#                                                 长河路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E5%A5%A5%E4%BD%93%E4%B8%AD%E5%BF%83.html"
#                                                 class="">
#                                                 奥体中心
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E7%99%BD%E9%A9%AC%E6%B9%96.html"
#                                                 class="">
#                                                 白马湖
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E5%BD%A9%E8%99%B9%E5%9F%8E.html"
#                                                 class="">
#                                                 彩虹城
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E6%B5%A6%E6%B2%BF.html"
#                                                 class="">
#                                                 浦沿
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E6%BB%A8%E5%92%8C%E8%B7%AF.html"
#                                                 class="">
#                                                 滨和路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E6%9D%A8%E5%AE%B6%E5%A2%A9.html"
#                                                 class="">
#                                                 杨家墩
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E6%98%9F%E6%B0%91.html"
#                                                 class="">
#                                                 星民
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E6%B1%9F%E9%99%B5%E8%B7%AF.html"
#                                                 class="">
#                                                 江陵路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E4%B8%AD%E5%8C%BB%E8%8D%AF%E5%A4%A7%E5%AD%A6.html"
#                                                 class="">
#                                                 中医药大学
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%BB%A8%E6%B1%9F%E5%8C%BA-b%E8%81%94%E5%BA%84.html"
#                                                 class="">
#                                                 联庄
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA.html"
#                                     class="">
#                                     西湖区
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B8%B0%E6%BD%AD%E8%B7%AF.html"
#                                                 class="">
#                                                 丰潭路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%8C%AF%E5%8D%8E%E8%B7%AF.html"
#                                                 class="">
#                                                 振华路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B8%89%E5%A2%A9.html"
#                                                 class="">
#                                                 三墩
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%96%87%E4%B8%80%E8%A5%BF%E8%B7%AF.html"
#                                                 class="">
#                                                 文一西路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E7%BF%A0%E8%8B%91.html"
#                                                 class="">
#                                                 翠苑
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%8F%A4%E8%8D%A1.html"
#                                                 class="">
#                                                 古荡
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E9%BB%84%E9%BE%99.html"
#                                                 class="">
#                                                 黄龙
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%98%89%E7%BB%BF.html"
#                                                 class="">
#                                                 嘉绿
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B9%9D%E8%8E%B2.html"
#                                                 class="">
#                                                 九莲
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E7%95%99%E4%B8%8B.html"
#                                                 class="">
#                                                 留下
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%B8%85%E6%B3%A2.html"
#                                                 class="">
#                                                 清波
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%96%87%E4%B8%89%E8%A5%BF%E8%B7%AF.html"
#                                                 class="">
#                                                 文三西路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E8%A5%BF%E6%BA%AA.html"
#                                                 class="">
#                                                 西溪
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%AD%A6%E5%86%9B.html"
#                                                 class="">
#                                                 学军
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B9%8B%E6%B1%9F.html"
#                                                 class="">
#                                                 之江
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E8%BD%AC%E5%A1%98.html"
#                                                 class="">
#                                                 转塘
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%B5%99%E5%A4%A7%E7%B4%AB%E9%87%91%E6%B8%AF.html"
#                                                 class="">
#                                                 浙大紫金港
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%AD%A6%E9%99%A2%E8%B7%AF.html"
#                                                 class="">
#                                                 学院路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%B1%B1%E6%B0%B4.html"
#                                                 class="">
#                                                 山水
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E9%87%91%E5%AE%B6%E6%B8%A1.html"
#                                                 class="">
#                                                 金家渡
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%B1%9F%E5%9F%8E%E8%B7%AF.html"
#                                                 class="">
#                                                 江城路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%8F%A4%E5%A2%A9%E8%B7%AF.html"
#                                                 class="">
#                                                 古墩路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E7%99%BD%E6%B4%8B.html"
#                                                 class="">
#                                                 白洋
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%A2%A9%E7%A5%A5%E8%A1%97.html"
#                                                 class="">
#                                                 墩祥街
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E8%92%8B%E6%9D%91.html"
#                                                 class="">
#                                                 蒋村
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B8%8B%E5%AE%81%E6%A1%A5.html"
#                                                 class="">
#                                                 下宁桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E6%96%87%E6%96%B0.html"
#                                                 class="">
#                                                 文新
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E4%B8%89%E5%9D%9D.html"
#                                                 class="">
#                                                 三坝
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E8%99%BE%E9%BE%99%E5%9C%A9.html"
#                                                 class="">
#                                                 虾龙圩
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%A5%BF%E6%B9%96%E5%8C%BA-b%E5%8F%A4%E7%BF%A0%E8%B7%AF.html"
#                                                 class="">
#                                                 古翠路
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA.html"
#                                     class="">
#                                     拱墅区
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E7%94%B3%E8%8A%B1.html"
#                                                 class="">
#                                                 申花
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%8D%8A%E5%B1%B1.html"
#                                                 class="">
#                                                 半山
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%A4%A7%E5%85%B3.html"
#                                                 class="">
#                                                 大关
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%BE%B7%E8%83%9C.html"
#                                                 class="">
#                                                 德胜
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E4%B8%81%E6%A1%A5.html"
#                                                 class="">
#                                                 丁桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%8B%B1%E5%AE%B8%E6%A1%A5.html"
#                                                 class="">
#                                                 拱宸桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%8B%BE%E5%BA%84.html"
#                                                 class="">
#                                                 勾庄
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%92%8C%E7%9D%A6.html"
#                                                 class="">
#                                                 和睦
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%B9%96%E5%A2%85.html"
#                                                 class="">
#                                                 湖墅
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%A1%A5%E8%A5%BF.html"
#                                                 class="">
#                                                 桥西
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E4%B8%89%E5%A1%98.html"
#                                                 class="">
#                                                 三塘
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E7%9F%B3%E6%A1%A5%28%E6%9D%AD%E5%B7%9E%29.html"
#                                                 class="">
#                                                 石桥(杭州)
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E4%B8%87%E8%BE%BE%E5%B9%BF%E5%9C%BA.html"
#                                                 class="">
#                                                 万达广场
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E4%BF%A1%E4%B9%89%E5%9D%8A.html"
#                                                 class="">
#                                                 信义坊
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E4%B8%AD%E5%A4%A7%E9%93%B6%E6%B3%B0.html"
#                                                 class="">
#                                                 中大银泰
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E8%BF%90%E6%B2%B3%E5%B9%BF%E5%9C%BA.html"
#                                                 class="">
#                                                 运河广场
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%B2%88%E5%A1%98%E6%A1%A5.html"
#                                                 class="">
#                                                 沈塘桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%B1%BD%E8%BD%A6%E5%8C%97%E7%AB%99.html"
#                                                 class="">
#                                                 汽车北站
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E6%B9%96%E5%B7%9E%E8%A1%97.html"
#                                                 class="">
#                                                 湖州街
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%96%84%E8%B4%A4.html"
#                                                 class="">
#                                                 善贤
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E5%A4%A7%E8%BF%90%E6%B2%B3.html"
#                                                 class="">
#                                                 大运河
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%8B%B1%E5%A2%85%E5%8C%BA-b%E8%90%8D%E6%B0%B4%E8%A1%97.html"
#                                                 class="">
#                                                 萍水街
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA.html"
#                                     class="">
#                                     江干区
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%87%91%E6%B2%99%E6%B9%96.html"
#                                                 class="">
#                                                 金沙湖
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%BA%91%E6%B0%B4.html"
#                                                 class="">
#                                                 云水
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B8%8B%E6%B2%99%E6%B1%9F%E6%BB%A8.html"
#                                                 class="">
#                                                 下沙江滨
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E7%81%AB%E8%BD%A6%E4%B8%9C%E7%AB%99.html"
#                                                 class="">
#                                                 火车东站
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%87%87%E8%8D%B7.html"
#                                                 class="">
#                                                 采荷
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%9F%8E%E4%B8%9C%E6%96%B0%E5%9F%8E.html"
#                                                 class="">
#                                                 城东新城
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%A4%A7%E5%AD%A6%E5%9F%8E%E5%8C%97.html"
#                                                 class="">
#                                                 大学城北
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%AB%98%E6%95%99%E5%9B%AD%E5%8C%BA%E4%B8%9C.html"
#                                                 class="">
#                                                 高教园区东
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%AB%98%E6%95%99%E5%9B%AD%E5%8C%BA%E8%A5%BF.html"
#                                                 class="">
#                                                 高教园区西
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%B7%A5%E4%B8%9A%E5%9B%AD%E5%8C%97.html"
#                                                 class="">
#                                                 工业园北
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%8D%8E%E5%AE%B6%E6%B1%A0.html"
#                                                 class="">
#                                                 华家池
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%9B%9B%E5%AD%A3%E9%9D%92%28%E6%9D%AD%E5%B7%9E%29.html"
#                                                 class="">
#                                                 四季青(杭州)
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E7%AC%95%E6%A1%A5.html"
#                                                 class="">
#                                                 笕桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%99%AF%E8%8A%B3.html"
#                                                 class="">
#                                                 景芳
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B9%9D%E5%A0%A1.html"
#                                                 class="">
#                                                 九堡
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%8D%97%E8%82%96%E5%9F%A0.html"
#                                                 class="">
#                                                 南肖埠
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%92%B1%E6%B1%9F%E6%96%B0%E5%9F%8E.html"
#                                                 class="">
#                                                 钱江新城
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B8%89%E9%87%8C%E4%BA%AD.html"
#                                                 class="">
#                                                 三里亭
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%B2%BF%E6%B1%9F%E5%8C%97.html"
#                                                 class="">
#                                                 沿江北
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%B2%BF%E6%B1%9F%E5%8D%97.html"
#                                                 class="">
#                                                 沿江南
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%97%B8%E5%BC%84%E5%8F%A3.html"
#                                                 class="">
#                                                 闸弄口
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%AE%A2%E8%BF%90%E4%B8%AD%E5%BF%83.html"
#                                                 class="">
#                                                 客运中心
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B9%9D%E5%92%8C%E8%B7%AF.html"
#                                                 class="">
#                                                 九和路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%BD%AD%E5%9F%A0.html"
#                                                 class="">
#                                                 彭埠
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B8%83%E5%A0%A1.html"
#                                                 class="">
#                                                 七堡
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B8%8B%E6%B2%99%E8%A5%BF.html"
#                                                 class="">
#                                                 下沙西
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%92%B1%E6%B1%9F%E8%B7%AF.html"
#                                                 class="">
#                                                 钱江路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%BA%86%E6%98%A5%E5%B9%BF%E5%9C%BA.html"
#                                                 class="">
#                                                 庆春广场
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%BA%86%E8%8F%B1%E8%B7%AF.html"
#                                                 class="">
#                                                 庆菱路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%96%B0%E9%A3%8E.html"
#                                                 class="">
#                                                 新风
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%B1%9F%E9%94%A6%E8%B7%AF.html"
#                                                 class="">
#                                                 江锦路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%9F%8E%E6%98%9F%E8%B7%AF.html"
#                                                 class="">
#                                                 城星路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%96%87%E6%B5%B7%E5%8D%97%E8%B7%AF.html"
#                                                 class="">
#                                                 文海南路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%96%87%E6%B3%BD%E8%B7%AF.html"
#                                                 class="">
#                                                 文泽路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E9%AB%98%E6%B2%99%E8%B7%AF.html"
#                                                 class="">
#                                                 高沙路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E4%B8%8B%E6%B2%99%E8%B7%AF.html"
#                                                 class="">
#                                                 下沙路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E6%96%B0%E5%A1%98.html"
#                                                 class="">
#                                                 新塘
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E6%B1%9F%E5%B9%B2%E5%8C%BA-b%E5%B8%82%E6%B0%91%E4%B8%AD%E5%BF%83.html"
#                                                 class="">
#                                                 市民中心
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA.html"
#                                     class="">
#                                     下城区
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E8%A5%BF%E6%B9%96%E6%96%87%E5%8C%96%E5%B9%BF%E5%9C%BA.html"
#                                                 class="">
#                                                 西湖文化广场
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%BB%BA%E5%9B%BD%E5%8C%97%E8%B7%AF.html"
#                                                 class="">
#                                                 建国北路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%B5%81%E6%B0%B4%E8%8B%91.html"
#                                                 class="">
#                                                 流水苑
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%9C%9D%E6%99%96.html"
#                                                 class="">
#                                                 朝晖
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%BD%AE%E9%B8%A3.html"
#                                                 class="">
#                                                 潮鸣
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%BE%B7%E8%83%9C%E4%B8%9C.html"
#                                                 class="">
#                                                 德胜东
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%92%8C%E5%B9%B3.html"
#                                                 class="">
#                                                 和平
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E4%B8%9D%E7%BB%B8%E5%9F%8E.html"
#                                                 class="">
#                                                 丝绸城
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E4%BD%93%E8%82%B2%E5%9C%BA%E8%B7%AF.html"
#                                                 class="">
#                                                 体育场路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%A4%A9%E6%B0%B4.html"
#                                                 class="">
#                                                 天水
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%AD%A6%E6%9E%97.html"
#                                                 class="">
#                                                 武林
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E9%95%BF%E5%BA%86.html"
#                                                 class="">
#                                                 长庆
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E4%BC%97%E5%AE%89%E6%A1%A5.html"
#                                                 class="">
#                                                 众安桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%89%93%E9%93%81%E5%85%B3.html"
#                                                 class="">
#                                                 打铁关
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E4%B8%AD%E6%B2%B3%E5%8C%97%E8%B7%AF.html"
#                                                 class="">
#                                                 中河北路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%87%A4%E8%B5%B7%E8%B7%AF.html"
#                                                 class="">
#                                                 凤起路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%AD%A6%E6%9E%97%E9%97%A8.html"
#                                                 class="">
#                                                 武林门
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%AD%A6%E6%9E%97%E5%B9%BF%E5%9C%BA.html"
#                                                 class="">
#                                                 武林广场
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E5%AE%9D%E5%96%84%E6%A1%A5.html"
#                                                 class="">
#                                                 宝善桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8B%E5%9F%8E%E5%8C%BA-b%E6%9D%AD%E6%B0%A7.html"
#                                                 class="">
#                                                 杭氧
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA.html"
#                                     class="">
#                                     余杭区
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E7%BF%A1%E7%BF%A0%E5%9F%8E.html"
#                                                 class="">
#                                                 翡翠城
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E4%B9%94%E5%8F%B8.html"
#                                                 class="">
#                                                 乔司
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E6%9C%AA%E6%9D%A5%E7%A7%91%E6%8A%80%E5%9F%8E.html"
#                                                 class="">
#                                                 未来科技城
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E9%97%B2%E6%9E%97.html"
#                                                 class="">
#                                                 闲林
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E6%98%9F%E6%A1%A5.html"
#                                                 class="">
#                                                 星桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E4%B9%94%E5%8F%B8%E5%8D%97.html"
#                                                 class="">
#                                                 乔司南
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E7%BF%81%E6%A2%85.html"
#                                                 class="">
#                                                 翁梅
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E5%8D%97%E8%8B%91.html"
#                                                 class="">
#                                                 南苑
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E6%9D%9C%E7%94%AB%E6%9D%91.html"
#                                                 class="">
#                                                 杜甫村
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E4%BA%94%E5%B8%B8.html"
#                                                 class="">
#                                                 五常
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E6%9D%AD%E5%B8%88%E5%A4%A7%E4%BB%93%E5%89%8D.html"
#                                                 class="">
#                                                 杭师大仓前
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E8%89%AF%E7%9D%A6%E8%B7%AF.html"
#                                                 class="">
#                                                 良睦路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E5%88%9B%E6%99%AF%E8%B7%AF.html"
#                                                 class="">
#                                                 创景路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E7%BB%BF%E6%B1%80%E8%B7%AF.html"
#                                                 class="">
#                                                 绿汀路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%BD%99%E6%9D%AD%E5%8C%BA-b%E6%B0%B8%E7%A6%8F.html"
#                                                 class="">
#                                                 永福
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA.html"
#                                     class="">
#                                     上城区
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%9F%8E%E7%AB%99.html"
#                                                 class="">
#                                                 城站
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%A4%8D%E5%85%B4%E8%B7%AF.html"
#                                                 class="">
#                                                 复兴路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E9%BC%93%E6%A5%BC%28%E6%9D%AD%E5%B7%9E%29.html"
#                                                 class="">
#                                                 鼓楼(杭州)
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E6%B9%96%E6%BB%A8.html"
#                                                 class="">
#                                                 湖滨
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E8%BF%91%E6%B1%9F.html"
#                                                 class="">
#                                                 近江
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%8D%97%E6%98%9F.html"
#                                                 class="">
#                                                 南星
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E6%B8%85%E6%B3%B0.html"
#                                                 class="">
#                                                 清泰
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E6%9C%9B%E6%B1%9F.html"
#                                                 class="">
#                                                 望江
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E9%9B%84%E9%95%87%E6%A5%BC.html"
#                                                 class="">
#                                                 雄镇楼
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%AE%9A%E5%AE%89%E8%B7%AF.html"
#                                                 class="">
#                                                 定安路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E9%BE%99%E7%BF%94%E6%A1%A5.html"
#                                                 class="">
#                                                 龙翔桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E6%B0%B4%E6%BE%84%E6%A1%A5.html"
#                                                 class="">
#                                                 水澄桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%8D%97%E6%98%9F%E6%A1%A5.html"
#                                                 class="">
#                                                 南星桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E7%94%AC%E6%B1%9F%E8%B7%AF.html"
#                                                 class="">
#                                                 甬江路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E4%B8%8A%E5%9F%8E%E5%8C%BA-b%E5%A9%BA%E6%B1%9F%E8%B7%AF.html"
#                                                 class="">
#                                                 婺江路
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA.html"
#                                     class="">
#                                     萧山区
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E9%92%B1%E6%B1%9F%E4%B8%96%E7%BA%AA%E5%9F%8E.html"
#                                                 class="">
#                                                 钱江世纪城
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E9%97%BB%E5%A0%B0.html"
#                                                 class="">
#                                                 闻堰
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%B9%98%E6%B9%96.html"
#                                                 class="">
#                                                 湘湖
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E8%90%A7%E5%B1%B1%E5%BC%80%E5%8F%91%E5%8C%BA.html"
#                                                 class="">
#                                                 萧山开发区
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E4%B9%89%E6%A1%A5.html"
#                                                 class="">
#                                                 义桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E9%A3%9E%E8%99%B9%E8%B7%AF.html"
#                                                 class="">
#                                                 飞虹路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E5%BB%BA%E8%AE%BE%E4%B8%89%E8%B7%AF.html"
#                                                 class="">
#                                                 建设三路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%9B%B9%E5%AE%B6%E6%A1%A5.html"
#                                                 class="">
#                                                 曹家桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%9C%9D%E9%98%B3.html"
#                                                 class="">
#                                                 朝阳
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%9D%AD%E5%8F%91%E5%8E%82.html"
#                                                 class="">
#                                                 杭发厂
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E5%BB%BA%E8%AE%BE%E4%B8%80%E8%B7%AF.html"
#                                                 class="">
#                                                 建设一路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E9%87%91%E5%9F%8E%E8%B7%AF.html"
#                                                 class="">
#                                                 金城路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%BD%98%E6%B0%B4.html"
#                                                 class="">
#                                                 潘水
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E4%BA%BA%E6%B0%91%E8%B7%AF.html"
#                                                 class="">
#                                                 人民路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E4%BF%A1%E6%81%AF%E6%B8%AF.html"
#                                                 class="">
#                                                 信息港
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E7%9B%88%E4%B8%B0%E8%B7%AF.html"
#                                                 class="">
#                                                 盈丰路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%8C%AF%E5%AE%81%E8%B7%AF.html"
#                                                 class="">
#                                                 振宁路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E4%BA%BA%E6%B0%91%E5%B9%BF%E5%9C%BA.html"
#                                                 class="">
#                                                 人民广场
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E6%BB%A8%E5%BA%B7%E8%B7%AF.html"
#                                                 class="">
#                                                 滨康路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E7%9B%9B%E4%B8%9C.html"
#                                                 class="">
#                                                 盛东
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/d%E8%90%A7%E5%B1%B1%E5%8C%BA-b%E4%B8%B0%E5%8C%97.html"
#                                                 class="">
#                                                 丰北
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                     </div>
#                                     </dd>
#             </dl>
#             <dl class="dl_lst list subway" style="display: none;">
#                 <dd>
#                                             <div class="option_list">
#                             <a href="https://www.danke.com/room/hz"
#                                 class="onlist">不限</a>
#
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF.html"
#                                         class="">
#                                         1号线
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%B9%98%E6%B9%96.html"
#                                                 class="">
#                                                 湘湖
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%BB%A8%E5%BA%B7%E8%B7%AF.html"
#                                                 class="">
#                                                 滨康路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E8%A5%BF%E5%85%B4.html"
#                                                 class="">
#                                                 西兴
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%BB%A8%E5%92%8C%E8%B7%AF.html"
#                                                 class="">
#                                                 滨和路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%B1%9F%E9%99%B5%E8%B7%AF.html"
#                                                 class="">
#                                                 江陵路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E8%BF%91%E6%B1%9F.html"
#                                                 class="">
#                                                 近江
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%A9%BA%E6%B1%9F%E8%B7%AF.html"
#                                                 class="">
#                                                 婺江路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%9F%8E%E7%AB%99.html"
#                                                 class="">
#                                                 城站
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%AE%9A%E5%AE%89%E8%B7%AF.html"
#                                                 class="">
#                                                 定安路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E9%BE%99%E7%BF%94%E6%A1%A5.html"
#                                                 class="">
#                                                 龙翔桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%87%A4%E8%B5%B7%E8%B7%AF.html"
#                                                 class="">
#                                                 凤起路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%AD%A6%E6%9E%97%E5%B9%BF%E5%9C%BA.html"
#                                                 class="">
#                                                 武林广场
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E8%A5%BF%E6%B9%96%E6%96%87%E5%8C%96%E5%B9%BF%E5%9C%BA.html"
#                                                 class="">
#                                                 西湖文化广场
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%89%93%E9%93%81%E5%85%B3.html"
#                                                 class="">
#                                                 打铁关
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E9%97%B8%E5%BC%84%E5%8F%A3.html"
#                                                 class="">
#                                                 闸弄口
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E7%81%AB%E8%BD%A6%E4%B8%9C%E7%AB%99.html"
#                                                 class="">
#                                                 火车东站
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%BD%AD%E5%9F%A0.html"
#                                                 class="">
#                                                 彭埠
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B8%83%E5%A0%A1.html"
#                                                 class="">
#                                                 七堡
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B9%9D%E5%92%8C%E8%B7%AF.html"
#                                                 class="">
#                                                 九和路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B9%9D%E5%A0%A1.html"
#                                                 class="">
#                                                 九堡
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%AE%A2%E8%BF%90%E4%B8%AD%E5%BF%83.html"
#                                                 class="">
#                                                 客运中心
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B8%8B%E6%B2%99%E8%A5%BF.html"
#                                                 class="">
#                                                 下沙西
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E9%87%91%E6%B2%99%E6%B9%96.html"
#                                                 class="">
#                                                 金沙湖
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E9%AB%98%E6%B2%99%E8%B7%AF.html"
#                                                 class="">
#                                                 高沙路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%96%87%E6%B3%BD%E8%B7%AF.html"
#                                                 class="">
#                                                 文泽路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E6%96%87%E6%B5%B7%E5%8D%97%E8%B7%AF.html"
#                                                 class="">
#                                                 文海南路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%BA%91%E6%B0%B4.html"
#                                                 class="">
#                                                 云水
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B8%8B%E6%B2%99%E6%B1%9F%E6%BB%A8.html"
#                                                 class="">
#                                                 下沙江滨
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B9%94%E5%8F%B8%E5%8D%97.html"
#                                                 class="">
#                                                 乔司南
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E4%B9%94%E5%8F%B8.html"
#                                                 class="">
#                                                 乔司
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E7%BF%81%E6%A2%85.html"
#                                                 class="">
#                                                 翁梅
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l1%E5%8F%B7%E7%BA%BF-s%E5%8D%97%E8%8B%91.html"
#                                                 class="">
#                                                 南苑
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF.html"
#                                         class="">
#                                         5号线
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E6%BB%A8%E5%BA%B7%E8%B7%AF.html"
#                                                 class="">
#                                                 滨康路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%9F%8E%E7%AB%99.html"
#                                                 class="">
#                                                 城站
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E6%89%93%E9%93%81%E5%85%B3.html"
#                                                 class="">
#                                                 打铁关
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E4%BA%BA%E6%B0%91%E8%B7%AF.html"
#                                                 class="">
#                                                 人民路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%BB%BA%E5%9B%BD%E5%8C%97%E8%B7%AF.html"
#                                                 class="">
#                                                 建国北路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E4%B8%89%E5%9D%9D.html"
#                                                 class="">
#                                                 三坝
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%8D%97%E6%98%9F%E6%A1%A5.html"
#                                                 class="">
#                                                 南星桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%96%84%E8%B4%A4.html"
#                                                 class="">
#                                                 善贤
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%A4%A7%E8%BF%90%E6%B2%B3.html"
#                                                 class="">
#                                                 大运河
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E5%92%8C%E7%9D%A6.html"
#                                                 class="">
#                                                 和睦
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E8%90%8D%E6%B0%B4%E8%A1%97.html"
#                                                 class="">
#                                                 萍水街
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E6%B5%99%E5%A4%A7%E7%B4%AB%E9%87%91%E6%B8%AF.html"
#                                                 class="">
#                                                 浙大紫金港
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E8%92%8B%E6%9D%91.html"
#                                                 class="">
#                                                 蒋村
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E4%BA%94%E5%B8%B8.html"
#                                                 class="">
#                                                 五常
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E6%9D%AD%E5%B8%88%E5%A4%A7%E4%BB%93%E5%89%8D.html"
#                                                 class="">
#                                                 杭师大仓前
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E8%89%AF%E7%9D%A6%E8%B7%AF.html"
#                                                 class="">
#                                                 良睦路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l5%E5%8F%B7%E7%BA%BF-s%E6%B0%B8%E7%A6%8F.html"
#                                                 class="">
#                                                 永福
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/l6%E5%8F%B7%E7%BA%BF.html"
#                                         class="">
#                                         6号线
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/l6%E5%8F%B7%E7%BA%BF-s%E6%B1%9F%E9%99%B5%E8%B7%AF.html"
#                                                 class="">
#                                                 江陵路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l6%E5%8F%B7%E7%BA%BF-s%E4%B8%AD%E5%8C%BB%E8%8D%AF%E5%A4%A7%E5%AD%A6.html"
#                                                 class="">
#                                                 中医药大学
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF.html"
#                                         class="">
#                                         4号线
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E8%BF%91%E6%B1%9F.html"
#                                                 class="">
#                                                 近江
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E7%81%AB%E8%BD%A6%E4%B8%9C%E7%AB%99.html"
#                                                 class="">
#                                                 火车东站
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E5%BD%AD%E5%9F%A0.html"
#                                                 class="">
#                                                 彭埠
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E9%92%B1%E6%B1%9F%E8%B7%AF.html"
#                                                 class="">
#                                                 钱江路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%96%B0%E9%A3%8E.html"
#                                                 class="">
#                                                 新风
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%96%B0%E5%A1%98.html"
#                                                 class="">
#                                                 新塘
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%99%AF%E8%8A%B3.html"
#                                                 class="">
#                                                 景芳
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%B1%9F%E9%94%A6%E8%B7%AF.html"
#                                                 class="">
#                                                 江锦路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E5%B8%82%E6%B0%91%E4%B8%AD%E5%BF%83.html"
#                                                 class="">
#                                                 市民中心
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E5%9F%8E%E6%98%9F%E8%B7%AF.html"
#                                                 class="">
#                                                 城星路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%B5%A6%E6%B2%BF.html"
#                                                 class="">
#                                                 浦沿
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%9D%A8%E5%AE%B6%E5%A2%A9.html"
#                                                 class="">
#                                                 杨家墩
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E4%B8%AD%E5%8C%BB%E8%8D%AF%E5%A4%A7%E5%AD%A6.html"
#                                                 class="">
#                                                 中医药大学
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E6%B0%B4%E6%BE%84%E6%A1%A5.html"
#                                                 class="">
#                                                 水澄桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E5%A4%8D%E5%85%B4%E8%B7%AF.html"
#                                                 class="">
#                                                 复兴路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E5%8D%97%E6%98%9F%E6%A1%A5.html"
#                                                 class="">
#                                                 南星桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E7%94%AC%E6%B1%9F%E8%B7%AF.html"
#                                                 class="">
#                                                 甬江路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l4%E5%8F%B7%E7%BA%BF-s%E8%81%94%E5%BA%84.html"
#                                                 class="">
#                                                 联庄
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/l7%E5%8F%B7%E7%BA%BF.html"
#                                         class="">
#                                         7号线
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/l7%E5%8F%B7%E7%BA%BF-s%E5%9F%8E%E7%AB%99.html"
#                                                 class="">
#                                                 城站
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l7%E5%8F%B7%E7%BA%BF-s%E5%BB%BA%E8%AE%BE%E4%B8%89%E8%B7%AF.html"
#                                                 class="">
#                                                 建设三路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l7%E5%8F%B7%E7%BA%BF-s%E5%B8%82%E6%B0%91%E4%B8%AD%E5%BF%83.html"
#                                                 class="">
#                                                 市民中心
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF.html"
#                                         class="">
#                                         2号线
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%87%A4%E8%B5%B7%E8%B7%AF.html"
#                                                 class="">
#                                                 凤起路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%9C%9D%E9%98%B3.html"
#                                                 class="">
#                                                 朝阳
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%9B%B9%E5%AE%B6%E6%A1%A5.html"
#                                                 class="">
#                                                 曹家桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%BD%98%E6%B0%B4.html"
#                                                 class="">
#                                                 潘水
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%BA%BA%E6%B0%91%E8%B7%AF.html"
#                                                 class="">
#                                                 人民路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%9D%AD%E5%8F%91%E5%8E%82.html"
#                                                 class="">
#                                                 杭发厂
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%BA%BA%E6%B0%91%E5%B9%BF%E5%9C%BA.html"
#                                                 class="">
#                                                 人民广场
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%BB%BA%E8%AE%BE%E4%B8%80%E8%B7%AF.html"
#                                                 class="">
#                                                 建设一路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%BB%BA%E8%AE%BE%E4%B8%89%E8%B7%AF.html"
#                                                 class="">
#                                                 建设三路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%8C%AF%E5%AE%81%E8%B7%AF.html"
#                                                 class="">
#                                                 振宁路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E9%A3%9E%E8%99%B9%E8%B7%AF.html"
#                                                 class="">
#                                                 飞虹路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E7%9B%88%E4%B8%B0%E8%B7%AF.html"
#                                                 class="">
#                                                 盈丰路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E9%92%B1%E6%B1%9F%E4%B8%96%E7%BA%AA%E5%9F%8E.html"
#                                                 class="">
#                                                 钱江世纪城
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E9%92%B1%E6%B1%9F%E8%B7%AF.html"
#                                                 class="">
#                                                 钱江路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%BA%86%E6%98%A5%E5%B9%BF%E5%9C%BA.html"
#                                                 class="">
#                                                 庆春广场
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%BA%86%E8%8F%B1%E8%B7%AF.html"
#                                                 class="">
#                                                 庆菱路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%BB%BA%E5%9B%BD%E5%8C%97%E8%B7%AF.html"
#                                                 class="">
#                                                 建国北路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%B8%AD%E6%B2%B3%E5%8C%97%E8%B7%AF.html"
#                                                 class="">
#                                                 中河北路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%AD%A6%E6%9E%97%E9%97%A8.html"
#                                                 class="">
#                                                 武林门
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%B2%88%E5%A1%98%E6%A1%A5.html"
#                                                 class="">
#                                                 沈塘桥
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%AD%A6%E9%99%A2%E8%B7%AF.html"
#                                                 class="">
#                                                 学院路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%8F%A4%E7%BF%A0%E8%B7%AF.html"
#                                                 class="">
#                                                 古翠路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%B8%89%E5%A2%A9.html"
#                                                 class="">
#                                                 三墩
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%9D%9C%E7%94%AB%E6%9D%91.html"
#                                                 class="">
#                                                 杜甫村
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E7%99%BD%E6%B4%8B.html"
#                                                 class="">
#                                                 白洋
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E9%87%91%E5%AE%B6%E6%B8%A1.html"
#                                                 class="">
#                                                 金家渡
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E5%A2%A9%E7%A5%A5%E8%A1%97.html"
#                                                 class="">
#                                                 墩祥街
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E8%99%BE%E9%BE%99%E5%9C%A9.html"
#                                                 class="">
#                                                 虾龙圩
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%B8%89%E5%9D%9D.html"
#                                                 class="">
#                                                 三坝
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E6%96%87%E6%96%B0.html"
#                                                 class="">
#                                                 文新
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%B8%B0%E6%BD%AD%E8%B7%AF.html"
#                                                 class="">
#                                                 丰潭路
#                                             </a>
#                                                                                     <a href="https://www.danke.com/room/hz/l2%E5%8F%B7%E7%BA%BF-s%E4%B8%8B%E5%AE%81%E6%A1%A5.html"
#                                                 class="">
#                                                 下宁桥
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                             <div class="area-ls-wp" style="display:inline-block;">
#                                     <a href="https://www.danke.com/room/hz/l8%E5%8F%B7%E7%BA%BF.html"
#                                         class="">
#                                         8号线
#                                     </a>
#                                     <div class="sub_option_list">
#                                                                                     <a href="https://www.danke.com/room/hz/l8%E5%8F%B7%E7%BA%BF-s%E6%96%87%E6%B5%B7%E5%8D%97%E8%B7%AF.html"
#                                                 class="">
#                                                 文海南路
#                                             </a>
#                                                                             </div>
#                                 </div>
#                                                     </div>
#                                     </dd>
#             </dl>
#
#             <dl class="dl_lst" style="padding-top: 7px;">
#                 <dt>价格：</dt>
#                 <dd>
#                     <div class="option_list">
#                         <a href="https://www.danke.com/room/hz?"
#                            class="onlist">不限</a>
#                                                     <a href="https://www.danke.com/room/hz/p0.html"
#                                class="">
#                                 1500元以下
#                             </a>
#                                                     <a href="https://www.danke.com/room/hz/p1500.html"
#                                class="">
#                                 1500~2000元
#                             </a>
#                                                     <a href="https://www.danke.com/room/hz/p2000.html"
#                                class="">
#                                 2000~2500元
#                             </a>
#                                                     <a href="https://www.danke.com/room/hz/p2500.html"
#                                class="">
#                                 2500~3000元
#                             </a>
#                                                     <a href="https://www.danke.com/room/hz/p3000.html"
#                                class="">
#                                 3000元以上
#                             </a>
#                                             </div>
#                 </dd>
#             </dl>
#             <dl class="dl_lst">
#                 <dt>居室：</dt>
#                 <dd>
#                     <div class="option_list">
#                         <a href="https://www.danke.com/room/hz?"
#                            class="onlist">不限</a>
#
#                                                                                                                 <a href="https://www.danke.com/room/hz/n1.html?"
#                                    class="">一居室</a>
#                                                                                                                                             <a href="https://www.danke.com/room/hz/n2.html?"
#                                    class="">两居室</a>
#                                                                                                                                             <a href="https://www.danke.com/room/hz/n3.html?"
#                                    class="">三居室</a>
#                                                                                                                                             <a href="https://www.danke.com/room/hz/n4.html?"
#                                    class="">四居室以上</a>
#                                                                         </div>
#                 </dd>
#             </dl>
#              <dl class="dl_lst">
#                  <dt>类型：</dt>
#                  <dd>
#                      <div class="option_list">
#                          <a href="https://www.danke.com/room/hz?"
#                             class="onlist">不限</a>
#
#                          <a href="https://www.danke.com/room/hz/c%E6%95%B4%E7%A7%9F.html?"
#                             class="">整租</a>
#
#                          <a href="https://www.danke.com/room/hz/c%E5%90%88%E7%A7%9F.html?"
#                             class="">合租</a>
#                      </div>
#                  </dd>
#              </dl>
#             <dl class="dl_lst">
#                 <dt>特色：</dt>
#                 <div class="option_list">
#                     <a href="https://www.danke.com/room/hz?"
#                         class="onlist" >不限</a>
#                 </div>
#                 <!--风格style-->
#                 <div class="directionbox selectmodel">
#                     <div class="dropdown">
#                         <button class="btn btn-default dropdown-toggle w98" type="button" id="dropdownMenu2"
#                                 data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
#                             房源风格
#                             <span class="caret"></span>
#                         </button>
#                         <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
#                             <li><a href="https://www.danke.com/room/hz?">不限</a></li>
#                                                                                             <li><a href="https://www.danke.com/room/hz/zMUJI%E9%A3%8E.html?">MUJI风</a></li>
#                                                                                             <li><a href="https://www.danke.com/room/hz/z%E5%B7%A5%E4%B8%9A%E9%A3%8E.html?">工业风</a></li>
#                                                                                             <li><a href="https://www.danke.com/room/hz/z%E5%8C%97%E6%AC%A7%E5%AE%9C%E5%AE%B6.html?">北欧宜家</a></li>
#                                                                                             <li><a href="https://www.danke.com/room/hz/z%E7%8E%B0%E4%BB%A3%E7%AE%80%E7%BA%A6.html?">现代简约</a></li>
#                                                     </ul>
#                     </div>
#                 </div>
#                 <!--朝向face-->
#                 <div class="directionbox selectmodel">
#                     <div class="dropdown">
#                         <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu2"
#                                 data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
#                             朝向
#                             <span class="caret"></span>
#                         </button>
#                         <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
#                             <li><a href="https://www.danke.com/room/hz?">不限</a></li>
#                             <li><a href="https://www.danke.com/room/hz/f%E4%B8%9C.html?">东</a></li>
#                             <li><a href="https://www.danke.com/room/hz/f%E5%8D%97.html?">南</a></li>
#                             <li><a href="https://www.danke.com/room/hz/f%E8%A5%BF.html?">西</a></li>
#                             <li><a href="https://www.danke.com/room/hz/f%E5%8C%97.html?">北</a></li>
#                         </ul>
#                     </div>
#                 </div>
#                 <!--面积-->
#                 <div class="directionbox selectmodel">
#                     <div class="dropdown">
#                         <button class="btn btn-default dropdown-toggle" type="button" id="dropdownMenu2"
#                                 data-toggle="dropdown" aria-haspopup="true" aria-expanded="true">
#                             面积
#                             <span class="caret"></span>
#                         </button>
#                         <ul class="dropdown-menu mj" aria-labelledby="dropdownMenu2">
#                                                             <li><a href="https://www.danke.com/room/hz/q0_8.html?">10㎡以下</a></li>
#                                                             <li><a href="https://www.danke.com/room/hz/q8_10.html?">10-12㎡</a></li>
#                                                             <li><a href="https://www.danke.com/room/hz/q10_13.html?">12-15㎡</a></li>
#                                                             <li><a href="https://www.danke.com/room/hz/q13_18.html?">15-20㎡</a></li>
#                                                             <li><a href="https://www.danke.com/room/hz/q18_10000.html?">20㎡以上</a></li>
#                                                     </ul>
#                     </div>
#                 </div>
#                 <dd>
#                                         <div class="dlul">
#                                                     <a href="https://www.danke.com/room/hz/t%E6%9C%89.html?"
#                                class=""><i></i>独立卫生间</a>
#                                                     <a href="https://www.danke.com/room/hz/y%E6%9C%89.html?"
#                                class=""><i></i>独立阳台</a>
#                                                     <a href="https://www.danke.com/room/hz/w%E6%9C%89.html?"
#                                class=""><i></i>独立淋浴</a>
#
#                                                     <a href="https://www.danke.com/room/hz/g%E6%98%AF.html?"
#                                class=""><i></i>月租</a>
#
#                     </div>
#                 </dd>
#             </dl>
#         </div>
#     </div>
#
#
#
#
#                     <script>
#         $('.search-btn').click(function () {
#             saMethod.Clickingsearchitem('点击搜索按钮', window.location.href)
#         })
#
#         $('.sear_input').on('click', function () {
#             saMethod.Clickingsearchitem('点击搜索框', window.location.href)
#         })
#
#         $('.filter_options a').on('click', function () {
#
#             var house_positiontype = '',
#                 house_position = '',
#                 house_price = '',
#                 house_type = '',
#                 rent_type = '',
#                 house_feature = '';
#
#             if ($(this).parents('.dl_lst').find('dt').text() == '位置：') {
#                 if ($(this).text() == '区域' || $(this).text() == '地铁') {
#                     house_positiontype = $(this).text()
#                 }
#                 house_position =  $(this).text()
#             }
#             if($(this).parents('.dl_lst').find('dt').text() == '价格：'){
#                 house_price =  $(this).text()
#             }
#             if($(this).parents('.dl_lst').find('dt').text() == '居室：'){
#                 house_type =  $(this).text()
#             }
#             if($(this).parents('.dl_lst').find('dt').text() == '类型：'){
#                 rent_type =  $(this).text()
#             }
#             if($(this).parents('.dl_lst').find('dt').text() == '特色：'){
#                 house_feature =  $(this).text()
#             }
#             saMethod.ListPageScreening(rent_type, house_positiontype, house_position, house_price, house_feature, '', '', '', '', house_type)
#         })
#
#         function GetUrlParam(paraName) {
#     　　　　var url = document.location.toString();
#     　　　　var arrObj = url.split("?");
#     　　　　if (arrObj.length > 1) {
#     　　　　　　var arrPara = arrObj[1].split("&");
#     　　　　　　var arr;
#     　　　　　　for (var i = 0; i < arrPara.length; i++) {
#     　　　　　　　　arr = arrPara[i].split("=");
#
#     　　　　　　　　if (arr != null && arr[0] == paraName) {
#     　　　　　　　　　　return arr[1];
#     　　　　　　　　}
#     　　　　　　}
#     　　　　　　return "";
#     　　　　}else {
#     　　　　　　return "";
#     　　　　}
#         }
#
#         var from = GetUrlParam('from')
#         var style = GetUrlParam('style')
#         var page_type = '找房频道'
#         var source_type = '找房搜索'
#
#         if(from == 'home'){
#             page_type = '首页频道'
#             source_type = '首页搜索'
#         }
#         if(from == 'month'){
#             page_type = '月租频道'
#             source_type = '月租搜索'
#         }
#         if(from == 'month'){
#             page_type = '整租频道'
#             source_type = '精选房源模块'
#         }
#         if(from == 'with'){
#             page_type = '合租频道'
#             if(style == '%E5%B7%A5%E4%B8%9A%E9%A3%8E'){
#                 source_type = '工业风格房源模块'
#             }
#             if(style == 'MUJI%E9%A3%8E'){
#                 source_type = 'MUJI风格房源模块'
#             }
#         }
#
#         // sa.quick('autoTrack', {
#         //     'page_type': page_type,
#         //     'source_type': source_type,
#         //     'house_positiontype': '',
#         //     'house_position': '',
#         //     'house_scope': '',
#         //     'house_price': '',
#         //     'house_type': '',
#         //     'business_circle': '',
#         //     'house_rentway': '',
#         //     'house_area': '',
#         //     'house_id': '',
#         //     'housedel_id': '',
#         //     'resblock_name': '',
#         // });
#
#         $('.r_ls a').on('click', function () {
#             console.log($(this).text())
#             saMethod.ListPageScreening('', '', '', '', '', '', '', '', $(this).text(), '')
#         })
#
#         $('.btn-wrapper').hover(function () {
#             $(this).find('.default-btn').addClass('hover-btn')
#             $(this).find('.screen-item').show()
#         }, function () {
#             $(this).find('.default-btn').removeClass('hover-btn')
#             $(this).find('.screen-item').hide()
#         })
#
#         $('.screen-item .qy').click(function () {
#             $(this).addClass('onlist')
#             $('.screen-item .dt').removeClass('onlist')
#             $('.screen-item .area').show()
#             $('.screen-item .subway').hide()
#         })
#         $('.screen-item .dt').click(function () {
#             $(this).addClass('onlist')
#             $('.screen-item .qy').removeClass('onlist')
#             $('.screen-item .area').hide()
#             $('.screen-item .subway').show()
#         })
#
#         $('.area-ls-wp').hover(function () {
#             $(this).find('.sub_option_list').show();
#             if($(this).offset().top - $(this).parents('.option_list').offset().top === 0){
#                 $(this).find('.sub_option_list').css('top', '24px')
#             }else if($(this).offset().top - $(this).parents('.option_list').offset().top > 0){
#                 if($(this).offset().top - $(this).parents('.option_list').offset().top == 15){
#                     $(this).find('.sub_option_list').css({'top':'78px', 'left': '-80px'})
#                 }else if($(this).offset().top - $(this).parents('.option_list').offset().top == 53){
#                     $(this).find('.sub_option_list').css({'top':'116px', 'left': '-80px'})
#                 }else{
#                     $(this).find('.sub_option_list').css('top', '62px')
#                 }
#
#             }
#         }, function () {
#             $(this).find('.sub_option_list').hide();
#         })
#
#         if($('#qy').hasClass('onlist')){
#             $('.area.list').show()
#             $('.subway.list').hide()
#         }
#         if($('#dt').hasClass('onlist')){
#             $('.subway.list').show()
#             $('.area.list').hide()
#         }
#
#     </script>
#         <div class="clear"></div>
#
#         <!--房源列表-->
#         <div class="roomlist">
#
#                 <div class="r_ls">
#                 <a href="https://www.danke.com/room/hz?"
#             class="ck_on" style="padding-right: 0px;">默认排序</a>
#                     <a
#                 href="https://www.danke.com/room/hz/oprice-aasc.html?"
#                 class=" ck_up">
#                 价格<i></i>
#             </a>
#                     <a
#                 href="https://www.danke.com/room/hz/oroomArea-aasc.html?"
#                 class=" ck_up">
#                 面积<i></i>
#             </a>
#             </div>
#     <!-- <img class="px" src="//public.danke.com.cn/public-20180104-FqPrC5QhRc8uOdBlSfSdEWZ9qEvk"> -->
#
#
#                                 <div class="list-wrapper">
#     <div class="r_ls_box">
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='0' xiaoqu='大华海派风景'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20181215-Fnlv8mkEUv637pP3CnPUY3u6upyb?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">1</span>
#                         <a href="https://www.danke.com/room/1285958206.html" key='0' xiaoqu='大华海派风景' target="_blank" title="万达广场  大华海派风景 4室1厅">
#                             万达广场  大华海派风景 4室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约13㎡ | 7楼
#                         | 4室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#                                 <span class="ty_b">1560</span>&nbsp;元/月
#                             </div>
#                                                                 <a class="lk_more" key='0' xiaoqu='大华海派风景' href="https://www.danke.com/room/1285958206.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='1' xiaoqu='三塘南村'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20190325-Flede1tuhAmHyIN4CS8qhYalNqCk?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">2</span>
#                         <a href="https://www.danke.com/room/2049035880.html" key='1' xiaoqu='三塘南村' target="_blank" title="三塘  三塘南村 3室1厅">
#                             三塘  三塘南村 3室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距1号线,5号线打铁关站2550米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约13㎡ | 6楼
#                         | 3室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                             <div class="new-price-hot">
#                             <div class="new-price-link">
#                                 <em style="background: #ffffff;border: 1px solid #0cc6a2;color:#0cc6a2">返现</em>
#                                 满租1年,最高返现
#                                 1000元!
#                                                                     <a href="https://www.danke.com/zhuanti/template-rooms-Intelligence?subject_id=236" target="_blank">详情<img
#                                                 src="//public.danke.com.cn/public-20180105-FoPdY6GcChXaYqkekSWLAshCDt7w"></a>
#                                                             </div>
#                         </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#
#                                                 <span class="ty_b">
#                                                     1576
#                                                     </span>
#                                 <span class="ty_c">元/月</span>
#                                 <div class="room_price">
#                                     <span>月租金:</span>
#                                     <em style="font-size:12px;">¥1660／月</em>
#                                 </div>
#                             </div>
#                                                                 <a class="lk_more" key='1' xiaoqu='三塘南村' href="https://www.danke.com/room/2049035880.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='2' xiaoqu='曙光之城'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20180702-Fn5WznydYjsPZpRZ5pbWeV0LohfV?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">3</span>
#                         <a href="https://www.danke.com/room/2127311243.html" key='2' xiaoqu='曙光之城' target="_blank" title="城东新城  曙光之城 4室1厅">
#                             城东新城  曙光之城 4室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距1号线,4号线火车东站站1500米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约8㎡ | 4楼
#                         | 4室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                             <div class="new-price-hot">
#                             <div class="new-price-link">
#                                 <em style="background: #ffffff;border: 1px solid #0cc6a2;color:#0cc6a2">立减</em>
#                                 首月租金立减1000元！
#                                 额外最高返现2000元！
#                                                                     <a href="https://www.danke.com/zhuanti/template-rooms-Intelligence?subject_id=236" target="_blank">详情<img
#                                                 src="//public.danke.com.cn/public-20180105-FoPdY6GcChXaYqkekSWLAshCDt7w"></a>
#                                                             </div>
#                         </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#                                                                     <span class="ty_c first-month">首月</span>
#
#                                                 <span class="ty_b">
#                                                     730
#                                                     </span>
#                                 <span class="ty_c">元/月</span>
#                                 <div class="room_price">
#                                     <span>月租金:</span>
#                                     <em style="font-size:12px;">¥1730／月</em>
#                                 </div>
#                             </div>
#                                                                 <a class="lk_more" key='2' xiaoqu='曙光之城' href="https://www.danke.com/room/2127311243.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='3' xiaoqu='世纪坊'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20181001-FqE7x98qiVwHgduumCJtu9Zq8aQ9?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">4</span>
#                         <a href="https://www.danke.com/room/41517536.html" key='3' xiaoqu='世纪坊' target="_blank" title="近江  世纪坊 3室1厅">
#                             近江  世纪坊 3室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距1号线,4号线近江站650米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约9㎡ | 7楼
#                         | 3室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#                                 <span class="ty_b">1890</span>&nbsp;元/月
#                             </div>
#                                                                 <a class="lk_more" key='3' xiaoqu='世纪坊' href="https://www.danke.com/room/41517536.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='4' xiaoqu='丰瑞南苑'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20181123-FngyoeLxmQ5_0HNQuJQWFbNq5dDx?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">5</span>
#                         <a href="https://www.danke.com/room/1919651467.html" key='4' xiaoqu='丰瑞南苑' target="_blank" title="振宁路  丰瑞南苑 3室1厅">
#                             振宁路  丰瑞南苑 3室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距2号线振宁路站1700米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约15㎡ | 1楼
#                         | 3室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                             <div class="new-price-hot">
#                             <div class="new-price-link">
#                                 <em style="background: #ffffff;border: 1px solid #0cc6a2;color:#0cc6a2">立减</em>
#                                 首月租金立减1000元！
#                                 额外最高返现2000元！
#                                                                     <a href="https://www.danke.com/zhuanti/template-rooms-Intelligence?subject_id=236" target="_blank">详情<img
#                                                 src="//public.danke.com.cn/public-20180105-FoPdY6GcChXaYqkekSWLAshCDt7w"></a>
#                                                             </div>
#                         </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#                                                                     <span class="ty_c first-month">首月</span>
#
#                                                 <span class="ty_b">
#                                                     860
#                                                     </span>
#                                 <span class="ty_c">元/月</span>
#                                 <div class="room_price">
#                                     <span>月租金:</span>
#                                     <em style="font-size:12px;">¥1860／月</em>
#                                 </div>
#                             </div>
#                                                                 <a class="lk_more" key='4' xiaoqu='丰瑞南苑' href="https://www.danke.com/room/1919651467.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='5' xiaoqu='世纪坊'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20190406-FrHo6zCZcJfLWyZhW5Flv_clPs59?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">6</span>
#                         <a href="https://www.danke.com/room/572838434.html" key='5' xiaoqu='世纪坊' target="_blank" title="近江  世纪坊 4室1厅">
#                             近江  世纪坊 4室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距1号线,4号线近江站650米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约10㎡ | 6楼
#                         | 4室1卫                          | 朝北
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                             <div class="new-price-hot">
#                             <div class="new-price-link">
#                                 <em style="background: #ffffff;border: 1px solid #0cc6a2;color:#0cc6a2">返现</em>
#                                 满租1年,最高返现
#                                 1000元!
#                                                                     <a href="https://www.danke.com/zhuanti/template-rooms-Intelligence?subject_id=236" target="_blank">详情<img
#                                                 src="//public.danke.com.cn/public-20180105-FoPdY6GcChXaYqkekSWLAshCDt7w"></a>
#                                                             </div>
#                         </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#
#                                                 <span class="ty_b">
#                                                     1876
#                                                     </span>
#                                 <span class="ty_c">元/月</span>
#                                 <div class="room_price">
#                                     <span>月租金:</span>
#                                     <em style="font-size:12px;">¥1960／月</em>
#                                 </div>
#                             </div>
#                                                                 <a class="lk_more" key='5' xiaoqu='世纪坊' href="https://www.danke.com/room/572838434.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='6' xiaoqu='翠苑一区'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20181220-FoCA4Ohf5VTXuicEE7X8IBVgUYsu?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">7</span>
#                         <a href="https://www.danke.com/room/1182294957.html" key='6' xiaoqu='翠苑一区' target="_blank" title="翠苑  翠苑一区 2室1厅">
#                             翠苑  翠苑一区 2室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距2号线学院路站300米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约7㎡ | 2楼
#                         | 2室1卫                          | 朝北
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                             <div class="new-price-hot">
#                             <div class="new-price-link">
#                                 <em style="background: #ffffff;border: 1px solid #0cc6a2;color:#0cc6a2">返现</em>
#                                 满租1年,最高返现
#                                 1000元!
#                                                                     <a href="https://www.danke.com/zhuanti/template-rooms-Intelligence?subject_id=236" target="_blank">详情<img
#                                                 src="//public.danke.com.cn/public-20180105-FoPdY6GcChXaYqkekSWLAshCDt7w"></a>
#                                                             </div>
#                         </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#
#                                                 <span class="ty_b">
#                                                     1836
#                                                     </span>
#                                 <span class="ty_c">元/月</span>
#                                 <div class="room_price">
#                                     <span>月租金:</span>
#                                     <em style="font-size:12px;">¥1920／月</em>
#                                 </div>
#                             </div>
#                                                                 <a class="lk_more" key='6' xiaoqu='翠苑一区' href="https://www.danke.com/room/1182294957.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='7' xiaoqu='大华海派风景'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20181215-FtulBheyLN90jh8JxC9mN77fT-HP?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">8</span>
#                         <a href="https://www.danke.com/room/1143540447.html" key='7' xiaoqu='大华海派风景' target="_blank" title="万达广场  大华海派风景 4室1厅">
#                             万达广场  大华海派风景 4室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约16㎡ | 7楼
#                         | 4室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                             <span class=color-e64d3d>独立阳台</span>
#                                             </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#                                 <span class="ty_b">1630</span>&nbsp;元/月
#                             </div>
#                                                                 <a class="lk_more" key='7' xiaoqu='大华海派风景' href="https://www.danke.com/room/1143540447.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='8' xiaoqu='凯盛公寓'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20190324-FmAydVd_4Va3tRyCKkrm1s3f6XfT?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">9</span>
#                         <a href="https://www.danke.com/room/1453242110.html" key='8' xiaoqu='凯盛公寓' target="_blank" title="三墩  凯盛公寓 2室1厅">
#                             三墩  凯盛公寓 2室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距2号线白洋站650米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约11㎡ | 16楼
#                         | 2室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                             <span class=color-e64d3d>独立阳台</span>
#                                             </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#                                 <span class="ty_b">1630</span>&nbsp;元/月
#                             </div>
#                                                                 <a class="lk_more" key='8' xiaoqu='凯盛公寓' href="https://www.danke.com/room/1453242110.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='9' xiaoqu='滨江德信东方星城'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20190314-FqM8VpUccFxz-8O_zawG8CZyIEFL?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">10</span>
#                         <a href="https://www.danke.com/room/1619982171.html" key='9' xiaoqu='滨江德信东方星城' target="_blank" title="城东新城  滨江德信东方星城 5室1厅">
#                             城东新城  滨江德信东方星城 5室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距1号线,4号线火车东站站1300米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约19㎡ | 2楼
#                         | 5室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                             <span class=color-e64d3d>独立阳台</span>
#                                             </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#                                 <span class="ty_b">1930</span>&nbsp;元/月
#                             </div>
#                                                                 <a class="lk_more" key='9' xiaoqu='滨江德信东方星城' href="https://www.danke.com/room/1619982171.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='10' xiaoqu='迎春东苑'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20190215-Fgi4kJe7yC_PH3ee_mBqP9uhKYhh?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">11</span>
#                         <a href="https://www.danke.com/room/1495212401.html" key='10' xiaoqu='迎春东苑' target="_blank" title="滨和路  迎春东苑 4室1厅">
#                             滨和路  迎春东苑 4室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距1号线滨和路站350米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约11㎡ | 4楼
#                         | 4室1卫                          | 朝北
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                             <div class="new-price-hot">
#                             <div class="new-price-link">
#                                 <em style="background: #ffffff;border: 1px solid #0cc6a2;color:#0cc6a2">返现</em>
#                                 满租1年,最高返现
#                                 1000元!
#                                                                     <a href="https://www.danke.com/zhuanti/template-rooms-Intelligence?subject_id=236" target="_blank">详情<img
#                                                 src="//public.danke.com.cn/public-20180105-FoPdY6GcChXaYqkekSWLAshCDt7w"></a>
#                                                             </div>
#                         </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#
#                                                 <span class="ty_b">
#                                                     1836
#                                                     </span>
#                                 <span class="ty_c">元/月</span>
#                                 <div class="room_price">
#                                     <span>月租金:</span>
#                                     <em style="font-size:12px;">¥1920／月</em>
#                                 </div>
#                             </div>
#                                                                 <a class="lk_more" key='10' xiaoqu='迎春东苑' href="https://www.danke.com/room/1495212401.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='11' xiaoqu='昆仑红苹果'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20180727-Fr0Qb9_lkka1zXVSA-UD1e7vD6Sb?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">12</span>
#                         <a href="https://www.danke.com/room/102122384.html" key='11' xiaoqu='昆仑红苹果' target="_blank" title="客运中心  昆仑红苹果 4室1厅">
#                             客运中心  昆仑红苹果 4室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距1号线客运中心站1100米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约10㎡ | 2楼
#                         | 4室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                             <div class="new-price-hot">
#                             <div class="new-price-link">
#                                 <em style="background: #ffffff;border: 1px solid #0cc6a2;color:#0cc6a2">返现</em>
#                                 满租1年,最高返现
#                                 1000元!
#                                                                     <a href="https://www.danke.com/zhuanti/template-rooms-Intelligence?subject_id=236" target="_blank">详情<img
#                                                 src="//public.danke.com.cn/public-20180105-FoPdY6GcChXaYqkekSWLAshCDt7w"></a>
#                                                             </div>
#                         </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#
#                                                 <span class="ty_b">
#                                                     1476
#                                                     </span>
#                                 <span class="ty_c">元/月</span>
#                                 <div class="room_price">
#                                     <span>月租金:</span>
#                                     <em style="font-size:12px;">¥1560／月</em>
#                                 </div>
#                             </div>
#                                                                 <a class="lk_more" key='11' xiaoqu='昆仑红苹果' href="https://www.danke.com/room/102122384.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='12' xiaoqu='圣苑小区'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20181211-FuMXfGSzxflCQR20Ns5X3IDb1JDI?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">13</span>
#                         <a href="https://www.danke.com/room/1366462553.html" key='12' xiaoqu='圣苑小区' target="_blank" title="三坝  圣苑小区 3室1厅">
#                             三坝  圣苑小区 3室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距2号线,5号线三坝站450米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约16㎡ | 1楼
#                         | 3室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#                                 <span class="ty_b">1990</span>&nbsp;元/月
#                             </div>
#                                                                 <a class="lk_more" key='12' xiaoqu='圣苑小区' href="https://www.danke.com/room/1366462553.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='13' xiaoqu='省水利厅宿舍'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20190508-FmqofDBqjS82_Lu3RGdThhXLIIgV?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">14</span>
#                         <a href="https://www.danke.com/room/877986609.html" key='13' xiaoqu='省水利厅宿舍' target="_blank" title="南肖埠  省水利厅宿舍 3室1厅">
#                             南肖埠  省水利厅宿舍 3室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距4号线景芳站900米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约10㎡ | 3楼
#                         | 3室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#                                 <span class="ty_b">1960</span>&nbsp;元/月
#                             </div>
#                                                                 <a class="lk_more" key='13' xiaoqu='省水利厅宿舍' href="https://www.danke.com/room/877986609.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='14' xiaoqu='缤纷东苑'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20180130-FjuqesJsQgh5oVQVKQmkZKW2uS0s?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">15</span>
#                         <a href="https://www.danke.com/room/152242531.html" key='14' xiaoqu='缤纷东苑' target="_blank" title="江陵路  缤纷东苑 4室1厅">
#                             江陵路  缤纷东苑 4室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约14㎡ | 3楼
#                         | 4室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                             <div class="new-price-hot">
#                             <div class="new-price-link">
#                                 <em style="background: #ffffff;border: 1px solid #0cc6a2;color:#0cc6a2">返现</em>
#                                 满租1年,最高返现
#                                 2000元!
#                                                                     <a href="https://www.danke.com/zhuanti/template-rooms-Intelligence?subject_id=236" target="_blank">详情<img
#                                                 src="//public.danke.com.cn/public-20180105-FoPdY6GcChXaYqkekSWLAshCDt7w"></a>
#                                                             </div>
#                         </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#
#                                                 <span class="ty_b">
#                                                     1813
#                                                     </span>
#                                 <span class="ty_c">元/月</span>
#                                 <div class="room_price">
#                                     <span>月租金:</span>
#                                     <em style="font-size:12px;">¥1980／月</em>
#                                 </div>
#                             </div>
#                                                                 <a class="lk_more" key='14' xiaoqu='缤纷东苑' href="https://www.danke.com/room/152242531.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='15' xiaoqu='缤纷东苑'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20180130-Fj2rd2s13h6lunKmvR_aGWa8ZJTx?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">16</span>
#                         <a href="https://www.danke.com/room/1644598467.html" key='15' xiaoqu='缤纷东苑' target="_blank" title="江陵路  缤纷东苑 4室1厅">
#                             江陵路  缤纷东苑 4室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约13㎡ | 18楼
#                         | 4室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                             <div class="new-price-hot">
#                             <div class="new-price-link">
#                                 <em style="background: #ffffff;border: 1px solid #0cc6a2;color:#0cc6a2">返现</em>
#                                 满租1年,最高返现
#                                 2000元!
#                                                                     <a href="https://www.danke.com/zhuanti/template-rooms-Intelligence?subject_id=236" target="_blank">详情<img
#                                                 src="//public.danke.com.cn/public-20180105-FoPdY6GcChXaYqkekSWLAshCDt7w"></a>
#                                                             </div>
#                         </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#
#                                                 <span class="ty_b">
#                                                     1813
#                                                     </span>
#                                 <span class="ty_c">元/月</span>
#                                 <div class="room_price">
#                                     <span>月租金:</span>
#                                     <em style="font-size:12px;">¥1980／月</em>
#                                 </div>
#                             </div>
#                                                                 <a class="lk_more" key='15' xiaoqu='缤纷东苑' href="https://www.danke.com/room/1644598467.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='16' xiaoqu='近江苑'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20190415-Fu-Lwr44kbu_5O81w5ONINXeKxHB?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">17</span>
#                         <a href="https://www.danke.com/room/1017885577.html" key='16' xiaoqu='近江苑' target="_blank" title="婺江路  近江苑 3室1厅">
#                             婺江路  近江苑 3室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距1号线婺江路站550米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约9㎡ | 2楼
#                         | 3室1卫                          | 朝东南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                             <div class="new-price-hot">
#                             <div class="new-price-link">
#                                 <em style="background: #ffffff;border: 1px solid #0cc6a2;color:#0cc6a2">返现</em>
#                                 满租1年,最高返现
#                                 1000元!
#                                                                     <a href="https://www.danke.com/zhuanti/template-rooms-Intelligence?subject_id=236" target="_blank">详情<img
#                                                 src="//public.danke.com.cn/public-20180105-FoPdY6GcChXaYqkekSWLAshCDt7w"></a>
#                                                             </div>
#                         </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#
#                                                 <span class="ty_b">
#                                                     1836
#                                                     </span>
#                                 <span class="ty_c">元/月</span>
#                                 <div class="room_price">
#                                     <span>月租金:</span>
#                                     <em style="font-size:12px;">¥1920／月</em>
#                                 </div>
#                             </div>
#                                                                 <a class="lk_more" key='16' xiaoqu='近江苑' href="https://www.danke.com/room/1017885577.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='17' xiaoqu='金地西溪风华'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20180702-FmM3kbJ-diy4G6S-2AQQQdEF2zdk?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">18</span>
#                         <a href="https://www.danke.com/room/779367169.html" key='17' xiaoqu='金地西溪风华' target="_blank" title="未来科技城  金地西溪风华 5室1厅">
#                             未来科技城  金地西溪风华 5室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约13㎡ | 3楼
#                         | 5室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#                                 <span class="ty_b">1490</span>&nbsp;元/月
#                             </div>
#                                                                 <a class="lk_more" key='17' xiaoqu='金地西溪风华' href="https://www.danke.com/room/779367169.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='18' xiaoqu='保利霞飞郡'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20181114-Fk86urWVIt6bmo2SIA0o8JsY9y2o?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">19</span>
#                         <a href="https://www.danke.com/room/1340719049.html" key='18' xiaoqu='保利霞飞郡' target="_blank" title="信息港  保利霞飞郡 4室1厅">
#                             信息港  保利霞飞郡 4室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距2号线建设一路站1950米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约16㎡ | 26楼
#                         | 4室1卫                          | 朝南
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                             <span class=color-e64d3d>独立阳台</span>
#                                             </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#                                 <span class="ty_b">1800</span>&nbsp;元/月
#                             </div>
#                                                                 <a class="lk_more" key='18' xiaoqu='保利霞飞郡' href="https://www.danke.com/room/1340719049.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#
#             <div class="r_lbx">
#                 <a href="javascript:" class="rimg" target="_blank" key='19' xiaoqu='华苑公寓'>
#                     <span class="img-hint">
#                         <span></span>
#                         <span></span>
#                     </span>
#                     <img
#                         src="https://public.danke.com.cn/public-20181109-FtB_jlEH_neXXn7Bj1TSyhVqSI2j?imageView2/1/w/380/h/285" width="260" height="173"
#                         title=""
#                         alt="图片"/>
#
#                                     </a>
#                 <div class="r_lbx_cen">
#                     <div class="r_lbx_cena">
#                         <span class="location">20</span>
#                         <a href="https://www.danke.com/room/327990705.html" key='19' xiaoqu='华苑公寓' target="_blank" title="古墩路  华苑公寓 3室1厅">
#                             古墩路  华苑公寓 3室1厅
#                         </a>
#                                                     <div class="r_lbx_cena">
#                                 <div class="sub_img"></div>
#                                 距2号线古翠路站1900米
#                             </div>
#                                             </div>
#                     <div class="r_lbx_cenb">
#                         <div class="address_img"></div>
#                         建筑面积约7㎡ | 4楼
#                         | 3室1卫                          | 朝西
#                                                     <i>合</i>
#                                             </div>
#                     <div class="r_lbx_cenc">
#                                                                     </div>
#                                             <div class="new-price-hot">
#                             <div class="new-price-link">
#                                 <em style="background: #ffffff;border: 1px solid #0cc6a2;color:#0cc6a2">返现</em>
#                                 满租1年,最高返现
#                                 1000元!
#                                                                     <a href="https://www.danke.com/zhuanti/template-rooms-Intelligence?subject_id=236" target="_blank">详情<img
#                                                 src="//public.danke.com.cn/public-20180105-FoPdY6GcChXaYqkekSWLAshCDt7w"></a>
#                                                             </div>
#                         </div>
#                                     </div>
#                 <div class="r_lbx_money">
#                                                                         <div class="r_lbx_moneya">
#
#                                                 <span class="ty_b">
#                                                     1636
#                                                     </span>
#                                 <span class="ty_c">元/月</span>
#                                 <div class="room_price">
#                                     <span>月租金:</span>
#                                     <em style="font-size:12px;">¥1720／月</em>
#                                 </div>
#                             </div>
#                                                                 <a class="lk_more" key='19' xiaoqu='华苑公寓' href="https://www.danke.com/room/327990705.html" target="_blank">
#                         查看详情
#                     </a>
#                 </div>
#             </div>
#             </div>
#     <div class="list-map-wrapper">
#         <div id="list-map"></div>
#         <div class="pop-list"></div>
#         <div class="hot-room">
#             <div class="hot-room-title">
#                 <h2>热门房源</h2>
#                 <div>
#                     <a class="pre"><</a>
#                     <span class="one isthispage">1</span>
#                     <span>/</span>
#                     <span class="two">2</span>
#                     <a class="nex">></a>
#                 </div>
#             </div>
#             <div class="hot-room-list">
#                     <div class="hot-room-list-wp">
#                     </div>
#             </div>
#         </div>
#     </div>
# </div>
#
# <!--翻页插件-->
#
# <div class="page">
#
#
#                                                                                             <a href="https://www.danke.com/room/hz?page=1"
#                class="on">1</a>
#                                 <a href="https://www.danke.com/room/hz?page=2"
#                class="">2</a>
#                                 <a href="https://www.danke.com/room/hz?page=3"
#                class="">3</a>
#                                 <a href="https://www.danke.com/room/hz?page=4"
#                class="">4</a>
#                                 <a href="https://www.danke.com/room/hz?page=5"
#                class="">5</a>
#
#                     <a href="https://www.danke.com/room/hz?page=2"> > </a>
#         </div>
#
# <div class="shade-wrapper">
#     <div class="shade-area">
#         <a href="javascript:;" class="shade-close"></a>
#         <div class="shade-img">
#             <img class="big-img" src="" alt="">
#             <div class="small-img">
#                 <span class="small-img-pre"></span>
#                 <div class="img-list-wrapper">
#                     <div>
#
#                     </div>
#                 </div>
#                 <span class="small-img-nex"></span>
#             </div>
#         </div>
#         <div class="info-wrapper">
#             <h1 class="info-title"></h1>
#             <div class="money-look">
#
#             </div>
#             <div>
#                 <div class="info-sub"></div>
#                 <div class="info-pattern"></div>
#                 <div class="configuration">
#                 </div>
#             </div>
#             <input type="hidden" id="room_id" value="">
#             <a href="#" target="_blank" class="subscribe-btn">预约看房</a>
#             <div class="phone-subscribe">
#                 <div class="pnum">400-110-1027</div>
#                 <div class="tim">电话咨询服务时间：9:00 - 21:00（节假日照常）</div>
#             </div>
#         </div>
#     </div>
# </div>
#
# <!--翻页插件 end-->
# <script type="text/javascript" src="//api.map.baidu.com/api?v=3.0&ak=uM4lFGsjuz3NHGbgIwvqxRLca2LDBpMS&s=1"></script>
# <script>
#
#     window.onload = function () {
#         function GetUrlParam(paraName) {
#     　　　　var url = document.location.toString();
#     　　　　var arrObj = url.split("?");
#     　　　　if (arrObj.length > 1) {
#     　　　　　　var arrPara = arrObj[1].split("&");
#     　　　　　　var arr;
#     　　　　　　for (var i = 0; i < arrPara.length; i++) {
#     　　　　　　　　arr = arrPara[i].split("=");
#
#     　　　　　　　　if (arr != null && arr[0] == paraName) {
#     　　　　　　　　　　return arr[1];
#     　　　　　　　　}
#     　　　　　　}
#     　　　　　　return "";
#     　　　　}else {
#     　　　　　　return "";
#     　　　　}
#         }
#         // 神策
#         $('.r_lbx a').on('click', function(){
#             saMethod.Clickingthesearchresults(GetUrlParam('search_text'), '', '', '', $(this).attr('key'), '', '', $(this).attr('xiaoqu'), window.location.href)
#         })
#
#         var from = GetUrlParam('from')
#         var style = GetUrlParam('style')
#         var page_type = '找房频道'
#         var source_type = '房源列表'
#
#         if(from == 'home'){
#             page_type = '首页频道'
#             source_type = '房源列表'
#         }
#         if(from == 'month'){
#             page_type = '月租频道'
#             source_type = '房源列表'
#         }
#         if(from == 'all'){
#             page_type = '整租频道'
#             source_type = '精选房源模块'
#         }
#         if(from == 'with'){
#             page_type = '合租频道'
#             if(style == '%E5%B7%A5%E4%B8%9A%E9%A3%8E'){
#                 source_type = '工业风格房源模块'
#             }
#             if(style == 'MUJI%E9%A3%8E'){
#                 source_type = 'MUJI风格房源模块'
#             }
#         }
#
#         sa.quick('autoTrack', {
#             'page_type': page_type,
#             'source_type': source_type,
#             'house_positiontype': '',
#             'house_position': '',
#             'house_scope': '',
#             'house_price': '',
#             'house_type': '',
#             'business_circle': '',
#             'house_rentway': '',
#             'house_area': '',
#             'house_id': '',
#             'housedel_id': '',
#             'resblock_name': '',
#         });
#
#
#         var location = $.trim($('#location').val());
#
#         // 创建地图实例
#         var map = new BMap.Map("list-map", {maxZoom: 17, enableMapClick: false});
#         // 创建点坐标
#         var point = new BMap.Point(116.404, 39.915);
#         // 初始化地图，设置中心点坐标和地图级别
#         map.centerAndZoom(point, 12);
#         // 禁用地图事件
#         map.enableInertialDragging()
#         map.disableDoubleClickZoom()
#         // 缩放组件
#         var opts = {
#             type: BMAP_NAVIGATION_CONTROL_ZOOM,
#             anchor: BMAP_ANCHOR_BOTTOM_RIGHT
#         }
#         map.addControl(new BMap.NavigationControl(opts));
#         // 定义自定义覆盖物的构造函数
#         function SquareOverlay(index, object){
#             this._index = index;
#             this._object = object;
#         }
#         // 继承API的BMap.Overlay
#         SquareOverlay.prototype = new BMap.Overlay();
#         // 实现初始化方法
#
#         var mapx = 0;
#         var mapy = 0;
#
#         SquareOverlay.prototype.initialize = function(map){
#             // 保存map对象实例
#             this._map = map;
#             // 创建div元素，作为自定义覆盖物的容器
#             var div = document.createElement("div");
#             div.style.position = "absolute";
#             div.style.boxShadow = '0px 2px 3px #dfdedc';
#             div.setAttribute('class', 'map-icon-text');
#
#             var t = document.createElement("div");
#             t.setAttribute('class', 'map-text');
#             t.innerText = this._object.xiaoquName;
#             div.appendChild(t)
#
#             var text = document.createElement("div");
#             text.innerText = this._index;
#             text.setAttribute('class', 'map-icon');
#             div.appendChild(text)
#
#             var pop = document.createElement("div");
#             pop.setAttribute('class', 'map-icon-pop');
#             pop.setAttribute('index', this._index);
#             // div.appendChild(pop)
#
#             var pos = new BMap.Point(this._object.xiaoquLonLat.split(",")[1], this._object.xiaoquLonLat.split(",")[0])
#
#             var position = this._map.pointToOverlayPixel(pos);
#             pop.style.left = position.x - 366 - 20 + mapx + "px";
#             pop.style.top = position.y - 65 + mapy + "px";
#
#             var img = document.createElement("img");
#             img.style.float = 'left'
#             img.setAttribute('src', this._object.roomImages);
#             pop.appendChild(img)
#
#             var title = document.createElement("div");
#             title.style.float = 'left';
#             title.style.paddingTop = '10px';
#             var add = document.createElement("div");
#             add.innerText = this._object.block + this._object.xiaoquName + this._object.bedroomNum + '室' + this._object.publicSpaceNum + '厅';
#             add.style.fontSize = '14px'
#             add.style.color = '#333'
#             add.style.maxWidth = '200px'
#             add.style.overflow = 'hidden'
#             add.style.textOverflow = 'ellipsis'
#             add.style.whiteSpace = 'nowrap'
#             var sub = document.createElement("div");
#
#             var list = {"1285958206":"","2049035880":"\u8ddd1\u53f7\u7ebf,5\u53f7\u7ebf\u6253\u94c1\u5173\u7ad92550\u7c73","2127311243":"\u8ddd1\u53f7\u7ebf,4\u53f7\u7ebf\u706b\u8f66\u4e1c\u7ad9\u7ad91500\u7c73","41517536":"\u8ddd1\u53f7\u7ebf,4\u53f7\u7ebf\u8fd1\u6c5f\u7ad9650\u7c73","1919651467":"\u8ddd2\u53f7\u7ebf\u632f\u5b81\u8def\u7ad91700\u7c73","572838434":"\u8ddd1\u53f7\u7ebf,4\u53f7\u7ebf\u8fd1\u6c5f\u7ad9650\u7c73","1182294957":"\u8ddd2\u53f7\u7ebf\u5b66\u9662\u8def\u7ad9300\u7c73","1143540447":"","1453242110":"\u8ddd2\u53f7\u7ebf\u767d\u6d0b\u7ad9650\u7c73","1619982171":"\u8ddd1\u53f7\u7ebf,4\u53f7\u7ebf\u706b\u8f66\u4e1c\u7ad9\u7ad91300\u7c73","1495212401":"\u8ddd1\u53f7\u7ebf\u6ee8\u548c\u8def\u7ad9350\u7c73","102122384":"\u8ddd1\u53f7\u7ebf\u5ba2\u8fd0\u4e2d\u5fc3\u7ad91100\u7c73","1366462553":"\u8ddd2\u53f7\u7ebf,5\u53f7\u7ebf\u4e09\u575d\u7ad9450\u7c73","877986609":"\u8ddd4\u53f7\u7ebf\u666f\u82b3\u7ad9900\u7c73","152242531":"","1644598467":"","1017885577":"\u8ddd1\u53f7\u7ebf\u5a7a\u6c5f\u8def\u7ad9550\u7c73","779367169":"","1340719049":"\u8ddd2\u53f7\u7ebf\u5efa\u8bbe\u4e00\u8def\u7ad91950\u7c73","327990705":"\u8ddd2\u53f7\u7ebf\u53e4\u7fe0\u8def\u7ad91900\u7c73"};
#
#             sub.innerText = list[this._object.roomId]
#
#             sub.style.fontSize = '10px'
#             sub.style.color = '#666'
#             var unit = document.createElement("div");
#             unit.innerText = '约'+ this._object.publicArea +'㎡ |  '+ this._object.floor +'楼 | '+ this._object.bedroomNum +'室'+ this._object.toiletNum +'卫 | 朝' + this._object.face;
#             unit.style.fontSize = '10px'
#             unit.style.color = '#666'
#             title.appendChild(add)
#             title.appendChild(sub)
#             title.appendChild(unit)
#             pop.appendChild(title)
#
#             $('.pop-list').append(pop)
#
#             // 将div添加到覆盖物容器中
#             map.getPanes().markerPane.appendChild(div);
#             // 保存div实例
#             this._div = div;
#             // 需要将div元素作为方法的返回值，当调用该覆盖物的show、
#             // hide方法，或者对覆盖物进行移除时，API都将操作此元素。
#             return div;
#         }
#         // 实现绘制方法
#         SquareOverlay.prototype.draw = function(){
#         // 根据地理坐标转换为像素坐标，并设置给容器
#             var pos = new BMap.Point(this._object.xiaoquLonLat.split(",")[1], this._object.xiaoquLonLat.split(",")[0])
#             var position = this._map.pointToOverlayPixel(pos);
#             this._div.style.left = position.x + "px";
#             this._div.style.top = position.y - 28 + "px";
#         }
#
#         // 拖拽时提示信息重新定位
#         var startX = 0;
#         var startY = 0;
#
#         map.addEventListener("mousedown", function(event){
#             var e = event || window.event;
#             startX = e.screenX
#             startY = e.screenY
#         });
#
#         map.addEventListener("dragend", function(event){
#             var e = event || window.event;
#             var endX = e.screenX
#             var endY = e.screenY
#             var popArr = $('.map-icon-pop')
#             var x = endX - startX
#             var y = endY - startY
#             mapx += x;
#             mapy += y;
#
#             for(var i=0; i<popArr.length;i++){
#                 var startTop = parseInt($(popArr[i]).css('top'))
#                 var startLeft = parseInt($(popArr[i]).css('left'))
#
#                 $(popArr[i]).css('left', startLeft + x + 'px')
#                 $(popArr[i]).css('top', startTop + y + 'px')
#             }
#         });
#
#         // 缩放时提示信息重新定位
#         var sTop = []
#         var sLeft = []
#
#         map.addEventListener("zoomstart", function(){
#             // console.log($('.map-icon-text').offset().top, $('.map-icon-text').offset().left)
#             var textArr = $('.map-icon-text')
#
#             sTop = []
#             sLeft = []
#
#             for(var i=0; i<textArr.length; i++){
#                 sTop.push($(textArr[i]).offset().top)
#                 sLeft.push($(textArr[i]).offset().left)
#             }
#
#         });
#
#         map.addEventListener("zoomend", function(){
#             // console.log($('.map-icon-text').offset().top, $('.map-icon-text').offset().left)
#             var eTop = []
#             var eLeft = []
#
#             var textArr = $('.map-icon-text')
#
#             for(var i=0; i<textArr.length; i++){
#                 eTop.push($(textArr[i]).offset().top)
#                 eLeft.push($(textArr[i]).offset().left)
#             }
#
#             var popArr = $('.map-icon-pop')
#
#             for(var i=0; i<popArr.length;i++){
#                 var startTop = parseInt($(popArr[i]).css('top'))
#                 var startLeft = parseInt($(popArr[i]).css('left'))
#
#                 var x = eLeft[i] - sLeft[i]
#                 var y = eTop[i] - sTop[i]
#
#                 $(popArr[i]).css('left', startLeft + x + 'px')
#                 $(popArr[i]).css('top', startTop + y + 'px')
#             }
#         });
#
#         // 鼠标移入点亮图标
#
#         $('.r_ls_box').on('mouseover', '.r_lbx .r_lbx_cena', function (event) {
#             $(this).find('.location').css('backgroundImage', 'url(https://public.danke.com.cn/public-20180523-FnLHK8FP36IMbKInXTCffJmu_g19)')
#             // 点亮地图定位图标
#             var text = $(this).find('.location').text();
#             for(var i=0;i<$('.map-icon').length;i++){
#                 if($($('.map-icon')[i]).text() === text){
#                     $($('.map-icon')[i]).css('backgroundImage', 'url(https://public.danke.com.cn/public-20180524-FlwQZ5AWFFeeRC-BMu4THJ2L_tJ5)')
#                     $($('.map-icon')[i]).parent().css('zIndex', 999)
#                     $($('.map-icon')[i]).parent().addClass('map-anm')
#                 }
#             }
#         })
#
#         $('.r_ls_box').on('mouseout', '.r_lbx .r_lbx_cena', function () {
#             $(this).find('.location').css('backgroundImage', 'url(https://public.danke.com.cn/public-20180523-Fm5iKtPPcef3z39yBP9yhjVv7jpn)')
#             // 点亮地图定位图标
#             var text = $(this).find('.location').text();
#             for(var i=0;i<$('.map-icon').length;i++){
#                 if($($('.map-icon')[i]).text() === text){
#                     $($('.map-icon')[i]).css('backgroundImage', 'url(https://public.danke.com.cn/public-20180524-FvUdjFbF06JdgYdeyj2qZGA5mhtF')
#                     $($('.map-icon')[i]).parent().removeClass('map-anm')
#                 }
#             }
#         })
#
#         $('.list-map-wrapper').on('mouseover', '.map-icon-text', function () {
#
#             var index = $(this).find('.map-icon').text() * 1 - 1;
#             $(this).find('.map-icon').css('backgroundImage', 'url(https://public.danke.com.cn/public-20180524-FlwQZ5AWFFeeRC-BMu4THJ2L_tJ5)')
#             $(this).css('z-index', 999)
#             // $($('.map-icon-pop')[index]).show()
#             $($('.location')[index]).css('backgroundImage', 'url(https://public.danke.com.cn/public-20180523-FnLHK8FP36IMbKInXTCffJmu_g19)')
#
#             var text = $(this).find('.map-icon').text()
#             for(var i=0;i<$('.map-icon-pop').length;i++){
#                 if($($('.map-icon-pop')[i]).attr('index') === text){
#                     $($('.map-icon-pop')[i]).show()
#                 }
#             }
#         })
#         $('.list-map-wrapper').on('mouseout', '.map-icon-text', function () {
#
#             var index = $(this).find('.map-icon').text() * 1 - 1;
#             $(this).find('.map-icon').css('backgroundImage', 'url(https://public.danke.com.cn/public-20180524-FvUdjFbF06JdgYdeyj2qZGA5mhtF')
#             $(this).css('z-index', 900)
#             // $($('.map-icon-pop')[index]).hide()
#             $($('.location')[index]).css('backgroundImage', 'url(https://public.danke.com.cn/public-20180523-Fm5iKtPPcef3z39yBP9yhjVv7jpn)')
#
#             var text = $(this).find('.map-icon').text()
#             for(var i=0;i<$('.map-icon-pop').length;i++){
#                 if($($('.map-icon-pop')[i]).attr('index') === text){
#                     $($('.map-icon-pop')[i]).hide()
#                 }
#             }
#         })
#
#         // 改变屏幕宽度重置地图框定位位置
#         window.onresize = function () {
#             if($('.map-fixed')){
#                 if($(document).width() > 1190){
#                     $('.map-fixed').css('right', ($(window).width() - 1190) / 2)
#                 }else{
#                     $('.map-fixed').css('right', ($(window).width() - 1190))
#                 }
#             }
#         }
#
#         if($('.list-map-wrapper').offset().top - $(window).scrollTop() - 60 <= 0){
#             $('.list-map-wrapper').addClass('map-fixed').css('right', ($(window).width() - 1190) / 2)
#         }
#         if($('.list-wrapper').offset().top + $('.list-wrapper').height() - $(window).scrollTop() - 60 < 675){
#             $('.list-map-wrapper').removeClass('map-fixed').css({'right': 0, 'top': $('.list-wrapper').height() - 680 + 'px'})
#         }
#
#         // 滚动条滚动事件
#         var roomsObject = {"current_page":1,"data":[{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u62f1\u5885\u533a","subway":null,"block":"\u4e07\u8fbe\u5e7f\u573a","price":1560,"bedroomNum":4,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u4e3b\u5367","face":"\u5357","searchText":"61205-B,\u5927\u534e\u6d77\u6d3e\u98ce\u666f\u5c0f\u533a2\u697c2\u5355\u5143703\u5ba4,\u90ed\u6653\u5764,\u5927\u534e\u6d77\u6d3e\u98ce\u666f,,\u4e07\u8fbe\u5e7f\u573a,\u62f1\u5885\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u5408\u79df,\u590d\u5f0f,loft,Loft,LOFT,\u5355\u8eab\u516c\u5bd3,\u590d\u5f0f\u516c\u5bd3,\u9752\u5e74\u516c\u5bd3,\u5730\u94c1,\u51af\u5bb6\u6d5c,\u8c22\u5bb6\u5858,\u4ead\u5b50\u5934","subwayLines":null,"xiaoquName":"\u5927\u534e\u6d77\u6d3e\u98ce\u666f","xiaoquAlias":"","roomId":"1285958206","suiteId":61205,"roomNumber":"B","roomArea":13,"monthPrice":1860,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-07-05","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20181215-Fnlv8mkEUv637pP3CnPUY3u6upyb?imageView2\/1\/w\/380\/h\/285","floor":7,"totalFloor":11,"toiletNum":1,"suiteArea":90,"suiteImages":null,"hasLift":"\u6709","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.298293,120.127523","blockLatLon":"30.350354,120.122502","xiaoquLonLat":"30.35256804,120.1267291","subwayLonLat":null,"subwayTitle":null,"subwayDuration":null,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":380,"roomTip":"\u8ddd\u4e07\u8fbe\u5e7f\u573a475\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":1440},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190620-FgMuwk6QzDBnCRiDiJWv7aqcmPaO\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":16889,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"61205-B","id":200062,"publicArea":13,"publicSuiteArea":90,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u62f1\u5885\u533a","subway":"1\u53f7\u7ebf,5\u53f7\u7ebf","block":"\u4e09\u5858","price":1660,"bedroomNum":3,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u6b21\u5367","face":"\u5357","searchText":"116530-C,\u4e09\u5858\u5357\u6751\u5c0f\u533a12\u697c3\u5355\u5143602\u5ba4,\u7530\u542f\u660e,\u4e09\u5858\u5357\u6751,,1\u53f7\u7ebf,5\u53f7\u7ebf,\u4e09\u5858,\u62f1\u5885\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u676d\u5dde2019\u5e747\u6708\u79df\u623f\u7acb\u77011000\u5143,\u5408\u79df,\u6768\u516d\u6751,\u738b\u5b50\u5858,\u5fb7\u80dc\u91cc,\u897f\u8054\u6865,7\u6708\u676d\u5dde\u6d3b\u52a8","subwayLines":"1\u53f7\u7ebf,5\u53f7\u7ebf","xiaoquName":"\u4e09\u5858\u5357\u6751","xiaoquAlias":null,"roomId":"2049035880","suiteId":116530,"roomNumber":"C","roomArea":13,"monthPrice":1960,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-05-25","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20190325-Flede1tuhAmHyIN4CS8qhYalNqCk?imageView2\/1\/w\/380\/h\/285","floor":6,"totalFloor":7,"toiletNum":1,"suiteArea":76,"suiteImages":null,"hasLift":"\u65e0","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.298293,120.127523","blockLatLon":"30.314786,120.173845","xiaoquLonLat":"30.311648,120.171919","subwayLonLat":"30.290878,120.183435","subwayTitle":"\u6253\u94c1\u5173","subwayDuration":3143,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":375,"roomTip":"\u8ddd\u4e09\u5858395\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":10},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190528-FmpAwuq6MwefEZDoke3uvDWhQ-cr\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":14354,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"116530-C","id":331884,"publicArea":13,"publicSuiteArea":76,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u6c5f\u5e72\u533a","subway":"1\u53f7\u7ebf,4\u53f7\u7ebf","block":"\u57ce\u4e1c\u65b0\u57ce","price":1730,"bedroomNum":4,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u6b21\u5367","face":"\u5357","searchText":"30050-B,\u66d9\u5149\u4e4b\u57ce\u5c0f\u533a14\u697c2\u5355\u5143403\u5ba4,\u962e\u5bb6\u660c,\u66d9\u5149\u4e4b\u57ce,,1\u53f7\u7ebf,4\u53f7\u7ebf,\u57ce\u4e1c\u65b0\u57ce,\u6c5f\u5e72\u533a,\u676d\u5dde\u5e02,\u6708\u79df\u623f\u6e90,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u676d\u5dde2019\u5e747\u6708\u79df\u623f\u7acb\u77013000\u5143,\u5408\u79df,\u77ed\u79df,\u82b1\u56ed\u515c,\u67b8\u6854\u5f04,\u677e\u78a7\u8857,\u8349\u5e84,\u6885\u5bb6\u66f2,\u65b0\u98ce\u6751,\u7126\u5bb6\u515c,\u53cc\u51c9\u4ead,\u676d\u5dde\u8fd1\u5730\u94c1\u6d3b\u52a8","subwayLines":"1\u53f7\u7ebf,4\u53f7\u7ebf","xiaoquName":"\u66d9\u5149\u4e4b\u57ce","xiaoquAlias":null,"roomId":"2127311243","suiteId":30050,"roomNumber":"B","roomArea":8,"monthPrice":2060,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-07-07","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20180702-Fn5WznydYjsPZpRZ5pbWeV0LohfV?imageView2\/1\/w\/380\/h\/285","floor":4,"totalFloor":17,"toiletNum":1,"suiteArea":89,"suiteImages":null,"hasLift":"\u6709","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.26286,120.208389","blockLatLon":"30.301196,120.213047","xiaoquLonLat":"30.310149,120.213989","subwayLonLat":"30.297241,120.219653","subwayTitle":"\u706b\u8f66\u4e1c\u7ad9","subwayDuration":2195,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":370,"roomTip":"\u8ddd\u57ce\u4e1c\u65b0\u57ce1.0\u516c\u91cc","roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":60,"viewMin":10},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190523-FvJtdbf9AzIEi5XhMPAz7rIlZyEO\"}]","fireHouse":"\u662f","hasError":0,"housekeeperId":18974,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"30050-B","id":100265,"publicArea":8,"publicSuiteArea":89,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u4e0a\u57ce\u533a","subway":"1\u53f7\u7ebf,4\u53f7\u7ebf","block":"\u8fd1\u6c5f","price":1890,"bedroomNum":3,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u6b21\u5367","face":"\u5357","searchText":"35639-A,\u4e16\u7eaa\u574a-9-1-702,\u53f6\u8fdb\u8d24,\u4e16\u7eaa\u574a,,1\u53f7\u7ebf,4\u53f7\u7ebf,\u8fd1\u6c5f,\u4e0a\u57ce\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u5408\u79df,\u5730\u94c1,\u57ce\u661f\u8def,\u57ce\u661f\u8def\u7ad9,\u8fd1\u6c5f\u7ad9,\u89c2\u97f3\u5858","subwayLines":"1\u53f7\u7ebf,4\u53f7\u7ebf","xiaoquName":"\u4e16\u7eaa\u574a","xiaoquAlias":null,"roomId":"41517536","suiteId":35639,"roomNumber":"A","roomArea":9,"monthPrice":2230,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-06-17","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20181001-FqE7x98qiVwHgduumCJtu9Zq8aQ9?imageView2\/1\/w\/380\/h\/285","floor":7,"totalFloor":7,"toiletNum":1,"suiteArea":77,"suiteImages":null,"hasLift":"\u65e0","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.236985,120.181422","blockLatLon":"30.236672,120.204409","xiaoquLonLat":"30.236781,120.211321","subwayLonLat":"30.236847,120.204085","subwayTitle":"\u8fd1\u6c5f","subwayDuration":800,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":370,"roomTip":"\u8ddd1\u53f7\u7ebf,4\u53f7\u7ebf\u8fd1\u6c5f696\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":60},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190522-FuQoU00R_M5o4f-f0kDFfR_ov9nx\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":14339,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"35639-A","id":115172,"publicArea":9,"publicSuiteArea":77,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u8427\u5c71\u533a","subway":"2\u53f7\u7ebf","block":"\u632f\u5b81\u8def","price":1860,"bedroomNum":3,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u4e3b\u5367","face":"\u5357","searchText":"57474-B,\u4e30\u745e\u5357\u82d1\u5c0f\u533a11\u697c3\u5355\u5143102\u5ba4,\u5434\u6167\u6770,\u4e30\u745e\u5357\u82d1,,2\u53f7\u7ebf,\u632f\u5b81\u8def,\u8427\u5c71\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u676d\u5dde2019\u5e747\u6708\u79df\u623f\u7acb\u77013000\u5143,\u5408\u79df,\u5408\u4e30\u5357,\u5408\u4e30\u4e1c,\u5408\u4e30\u5317,\u676d\u5dde\u8fd1\u5730\u94c1\u6d3b\u52a8","subwayLines":"2\u53f7\u7ebf","xiaoquName":"\u4e30\u745e\u5357\u82d1","xiaoquAlias":"","roomId":"1919651467","suiteId":57474,"roomNumber":"B","roomArea":15,"monthPrice":2200,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-03-08","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20181123-FngyoeLxmQ5_0HNQuJQWFbNq5dDx?imageView2\/1\/w\/380\/h\/285","floor":1,"totalFloor":6,"toiletNum":1,"suiteArea":80,"suiteImages":null,"hasLift":"\u65e0","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u71c3\u6c14\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.217362,120.369726","blockLatLon":"30.223227,120.275784","xiaoquLonLat":"30.219829,120.258241","subwayLonLat":"30.223227,120.275784","subwayTitle":"\u632f\u5b81\u8def","subwayDuration":2199,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":360,"roomTip":null,"roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":10},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190522-FrjNBjA_Nc3zlfJlS6x9He5AqxIQ\"}]","fireHouse":"\u662f","hasError":0,"housekeeperId":23306,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"57474-B","id":186537,"publicArea":15,"publicSuiteArea":80,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u4e0a\u57ce\u533a","subway":"1\u53f7\u7ebf,4\u53f7\u7ebf","block":"\u8fd1\u6c5f","price":1960,"bedroomNum":4,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u6b21\u5367","face":"\u5317","searchText":"81075-B,\u4e16\u7eaa\u574a\u5c0f\u533a10\u697c1\u5355\u5143601\u5ba4,\u5f20\u8d21\u5b5d,\u4e16\u7eaa\u574a,,1\u53f7\u7ebf,4\u53f7\u7ebf,\u8fd1\u6c5f,\u4e0a\u57ce\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u676d\u5dde2019\u5e747\u6708\u79df\u623f\u7acb\u77011000\u5143,\u5408\u79df,\u5730\u94c1,\u57ce\u661f\u8def,\u57ce\u661f\u8def\u7ad9,\u8fd1\u6c5f\u7ad9,\u89c2\u97f3\u5858,7\u6708\u676d\u5dde\u6d3b\u52a8","subwayLines":"1\u53f7\u7ebf,4\u53f7\u7ebf","xiaoquName":"\u4e16\u7eaa\u574a","xiaoquAlias":null,"roomId":"572838434","suiteId":81075,"roomNumber":"B","roomArea":10,"monthPrice":2330,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-05-06","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20190406-FrHo6zCZcJfLWyZhW5Flv_clPs59?imageView2\/1\/w\/380\/h\/285","floor":6,"totalFloor":7,"toiletNum":1,"suiteArea":96,"suiteImages":null,"hasLift":"\u65e0","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.236985,120.181422","blockLatLon":"30.236672,120.204409","xiaoquLonLat":"30.236781,120.211321","subwayLonLat":"30.236847,120.204085","subwayTitle":"\u8fd1\u6c5f","subwayDuration":800,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":360,"roomTip":"\u8ddd1\u53f7\u7ebf,4\u53f7\u7ebf\u8fd1\u6c5f696\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":1440},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190522-Fmh8Coai02YB_Krl1BhaapLFSxNH\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":31095,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"81075-B","id":323554,"publicArea":10,"publicSuiteArea":96,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u897f\u6e56\u533a","subway":"2\u53f7\u7ebf","block":"\u7fe0\u82d1","price":1920,"bedroomNum":2,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u9694\u65ad","face":"\u5317","searchText":"62674-B,\u7fe0\u82d1\u4e00\u533a\u5c0f\u533a28\u697c2\u5355\u5143204\u5ba4,\u738b\u948a1,\u7fe0\u82d1\u4e00\u533a,,2\u53f7\u7ebf,\u7fe0\u82d1,\u897f\u6e56\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u676d\u5dde2019\u5e747\u6708\u79df\u623f\u7acb\u77011000\u5143,\u94f6\u6cf0\u57ce,\u57ce\u897f\u94f6\u6cf0,\u5408\u79df,\u5730\u94c1,\u5b66\u9662\u8def,\u5b66\u9662\u8def\u7ad9,\u5b8b\u6c5f\u6751,\u4fdd\u4ead\u5df7,7\u6708\u676d\u5dde\u6d3b\u52a8","subwayLines":"2\u53f7\u7ebf","xiaoquName":"\u7fe0\u82d1\u4e00\u533a","xiaoquAlias":"","roomId":"1182294957","suiteId":62674,"roomNumber":"B","roomArea":7,"monthPrice":2290,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-06-01","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20181220-FoCA4Ohf5VTXuicEE7X8IBVgUYsu?imageView2\/1\/w\/380\/h\/285","floor":2,"totalFloor":7,"toiletNum":1,"suiteArea":47,"suiteImages":null,"hasLift":"\u65e0","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u71c3\u6c14\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.276339,120.134422","blockLatLon":"30.29445,120.129171","xiaoquLonLat":"30.291894,120.134347","subwayLonLat":"30.28904,120.13586","subwayTitle":"\u5b66\u9662\u8def","subwayDuration":436,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":360,"roomTip":"\u8ddd2\u53f7\u7ebf\u5b66\u9662\u8def349\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":60,"viewMin":10},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190530-Fp4RWWJSThSW8yTWZMdfTM5r4DZq\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":31724,"isSeparatedRoom":"\u662f","isNewTrend":null,"roomCode":"62674-B","id":204687,"publicArea":7,"publicSuiteArea":47,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u62f1\u5885\u533a","subway":null,"block":"\u4e07\u8fbe\u5e7f\u573a","price":1630,"bedroomNum":4,"hasToilet":"\u65e0","hasBalcony":"\u6709","hasShower":"\u65e0","bedroomType":"\u9694\u65ad","face":"\u5357","searchText":"61205-A,\u5927\u534e\u6d77\u6d3e\u98ce\u666f\u5c0f\u533a2\u697c2\u5355\u5143703\u5ba4,\u90ed\u6653\u5764,\u5927\u534e\u6d77\u6d3e\u98ce\u666f,,\u4e07\u8fbe\u5e7f\u573a,\u62f1\u5885\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u5408\u79df,\u590d\u5f0f,loft,Loft,LOFT,\u5355\u8eab\u516c\u5bd3,\u590d\u5f0f\u516c\u5bd3,\u9752\u5e74\u516c\u5bd3,\u5730\u94c1,\u51af\u5bb6\u6d5c,\u8c22\u5bb6\u5858,\u4ead\u5b50\u5934","subwayLines":null,"xiaoquName":"\u5927\u534e\u6d77\u6d3e\u98ce\u666f","xiaoquAlias":"","roomId":"1143540447","suiteId":61205,"roomNumber":"A","roomArea":16,"monthPrice":1930,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-06-17","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20181215-FtulBheyLN90jh8JxC9mN77fT-HP?imageView2\/1\/w\/380\/h\/285","floor":7,"totalFloor":11,"toiletNum":1,"suiteArea":90,"suiteImages":null,"hasLift":"\u6709","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.298293,120.127523","blockLatLon":"30.350354,120.122502","xiaoquLonLat":"30.35256804,120.1267291","subwayLonLat":null,"subwayTitle":null,"subwayDuration":null,"publicSpaceNum":1,"style":"\u5de5\u4e1a\u98ce","houseRank":360,"roomTip":"\u8ddd\u4e07\u8fbe\u5e7f\u573a475\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":60,"subScribeMin":1440,"viewMin":1440},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190620-FgMuwk6QzDBnCRiDiJWv7aqcmPaO\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":16889,"isSeparatedRoom":"\u662f","isNewTrend":null,"roomCode":"61205-A","id":200061,"publicArea":16,"publicSuiteArea":90,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u897f\u6e56\u533a","subway":"2\u53f7\u7ebf","block":"\u4e09\u58a9","price":1630,"bedroomNum":2,"hasToilet":"\u65e0","hasBalcony":"\u6709","hasShower":"\u65e0","bedroomType":"\u4e3b\u5367","face":"\u5357","searchText":"114967-B,\u51ef\u76db\u516c\u5bd3\u5c0f\u533a4\u697c2\u5355\u51431602\u5ba4,\u738b\u4fca\u6021,\u51ef\u76db\u516c\u5bd3,,2\u53f7\u7ebf,\u4e09\u58a9,\u897f\u6e56\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u5408\u79df,\u5730\u94c1,\u767d\u6d0b,\u767d\u6d0b\u7ad9,\u674e\u5bb6\u89d2,\u6234\u5bb6\u5858,\u7532\u6765\u57ce,\u738b\u5bb6\u6597","subwayLines":"2\u53f7\u7ebf","xiaoquName":"\u51ef\u76db\u516c\u5bd3","xiaoquAlias":null,"roomId":"1453242110","suiteId":114967,"roomNumber":"B","roomArea":11,"monthPrice":1930,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-07-04","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20190324-FmAydVd_4Va3tRyCKkrm1s3f6XfT?imageView2\/1\/w\/380\/h\/285","floor":16,"totalFloor":25,"toiletNum":1,"suiteArea":55,"suiteImages":null,"hasLift":"\u6709","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.276339,120.134422","blockLatLon":"30.329505,120.08576","xiaoquLonLat":"30.351083,120.081501","subwayLonLat":"30.356972,120.079569","subwayTitle":"\u767d\u6d0b","subwayDuration":300,"publicSpaceNum":1,"style":"\u5de5\u4e1a\u98ce","houseRank":360,"roomTip":"\u8ddd2\u53f7\u7ebf\u767d\u6d0b681\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":1440},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190706-Fr3hKlf1pv7vprGxD8oBKGMPzmEI\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":24268,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"114967-B","id":330046,"publicArea":11,"publicSuiteArea":55,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u6c5f\u5e72\u533a","subway":"1\u53f7\u7ebf,4\u53f7\u7ebf","block":"\u57ce\u4e1c\u65b0\u57ce","price":1930,"bedroomNum":5,"hasToilet":"\u65e0","hasBalcony":"\u6709","hasShower":"\u65e0","bedroomType":"\u9694\u65ad","face":"\u5357","searchText":"114933-D,\u6ee8\u6c5f\u5fb7\u4fe1\u4e1c\u65b9\u661f\u57ce\u5c0f\u533a13\u697c2\u5355\u5143201\u5ba4,\u5b8b\u5bb6\u73b2,\u6ee8\u6c5f\u5fb7\u4fe1\u4e1c\u65b9\u661f\u57ce,,1\u53f7\u7ebf,4\u53f7\u7ebf,\u57ce\u4e1c\u65b0\u57ce,\u6c5f\u5e72\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u5408\u79df,\u706b\u8f66\u4e1c\u7ad9,\u706b\u8f66\u4e1c\u7ad9\u7ad9,\u7126\u5bb6\u515c,\u89c2\u4e91\u5df7,\u6797\u5bb6\u6f3e,\u8349\u5e84,\u53cc\u51c9\u4ead,\u7b15\u4e1c\u6865,\u677e\u78a7\u8857,\u82b1\u56ed\u515c,\u962e\u5bb6\u6751,\u9ece\u660e\u6751,\u8fce\u5bbe\u6865","subwayLines":"1\u53f7\u7ebf,4\u53f7\u7ebf","xiaoquName":"\u6ee8\u6c5f\u5fb7\u4fe1\u4e1c\u65b9\u661f\u57ce","xiaoquAlias":null,"roomId":"1619982171","suiteId":114933,"roomNumber":"D","roomArea":19,"monthPrice":2290,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-07-13","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20190314-FqM8VpUccFxz-8O_zawG8CZyIEFL?imageView2\/1\/w\/380\/h\/285","floor":2,"totalFloor":17,"toiletNum":1,"suiteArea":127,"suiteImages":null,"hasLift":"\u6709","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u71c3\u6c14\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.26286,120.208389","blockLatLon":"30.301196,120.213047","xiaoquLonLat":"30.308885,120.222097","subwayLonLat":"30.297241,120.219653","subwayTitle":"\u706b\u8f66\u4e1c\u7ad9","subwayDuration":1669,"publicSpaceNum":1,"style":"\u5de5\u4e1a\u98ce","houseRank":360,"roomTip":null,"roomUrgency":{"hotBlock":null,"daikanMin":null,"subScribeMin":1440,"viewMin":1440},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":15175,"isSeparatedRoom":"\u662f","isNewTrend":null,"roomCode":"114933-D","id":324729,"publicArea":19,"publicSuiteArea":127,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u6ee8\u6c5f\u533a","subway":"1\u53f7\u7ebf","block":"\u6ee8\u548c\u8def","price":1920,"bedroomNum":4,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u9694\u65ad","face":"\u5317","searchText":"69617-B,\u8fce\u6625\u4e1c\u82d1\u5c0f\u533a16\u697c2\u5355\u5143401\u5ba4,\u4e8e\u5c0f\u5149,\u8fce\u6625\u4e1c\u82d1,,1\u53f7\u7ebf,\u6ee8\u548c\u8def,\u6ee8\u6c5f\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u676d\u5dde2019\u5e747\u6708\u79df\u623f\u7acb\u77011000\u5143,\u5408\u79df,\u5730\u94c1,\u6ee8\u548c\u8def\u7ad9,\u897f\u5174,\u897f\u5174\u7ad9,\u6c5f\u9675\u8def,\u6c5f\u9675\u8def\u7ad9,7\u6708\u676d\u5dde\u6d3b\u52a8","subwayLines":"1\u53f7\u7ebf","xiaoquName":"\u8fce\u6625\u4e1c\u82d1","xiaoquAlias":"","roomId":"1495212401","suiteId":69617,"roomNumber":"B","roomArea":11,"monthPrice":2290,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-05-09","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20190215-Fgi4kJe7yC_PH3ee_mBqP9uhKYhh?imageView2\/1\/w\/380\/h\/285","floor":4,"totalFloor":6,"toiletNum":1,"suiteArea":102,"suiteImages":null,"hasLift":"\u65e0","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.209447,120.209161","blockLatLon":"30.205784,120.224058","xiaoquLonLat":"30.204407,120.227674","subwayLonLat":"30.205784,120.224058","subwayTitle":"\u6ee8\u548c\u8def","subwayDuration":535,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":350,"roomTip":"\u8ddd1\u53f7\u7ebf\u6ee8\u548c\u8def380\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":10},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190520-Fg0DWa9XjY0LrckgQwhn2x2HBYhg\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":3923,"isSeparatedRoom":"\u662f","isNewTrend":null,"roomCode":"69617-B","id":223443,"publicArea":11,"publicSuiteArea":102,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u6c5f\u5e72\u533a","subway":"1\u53f7\u7ebf","block":"\u5ba2\u8fd0\u4e2d\u5fc3","price":1560,"bedroomNum":4,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u6b21\u5367","face":"\u5357","searchText":"32125-A,\u6606\u4ed1\u7ea2\u82f9\u679c\u5c0f\u533a8\u697c2\u5355\u5143202\u5ba4,\u9ad8\u4f73\u6770,\u6606\u4ed1\u7ea2\u82f9\u679c,,1\u53f7\u7ebf,\u5ba2\u8fd0\u4e2d\u5fc3,\u6c5f\u5e72\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u676d\u5dde2019\u5e747\u6708\u79df\u623f\u7acb\u77011000\u5143,\u5408\u79df,\u5730\u94c1,\u5ba2\u8fd0\u4e2d\u5fc3\u7ad9,\u6768\u516c\u6751,7\u6708\u676d\u5dde\u6d3b\u52a8","subwayLines":"1\u53f7\u7ebf","xiaoquName":"\u6606\u4ed1\u7ea2\u82f9\u679c","xiaoquAlias":"","roomId":"102122384","suiteId":32125,"roomNumber":"A","roomArea":10,"monthPrice":1860,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-05-12","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20180727-Fr0Qb9_lkka1zXVSA-UD1e7vD6Sb?imageView2\/1\/w\/380\/h\/285","floor":2,"totalFloor":16,"toiletNum":1,"suiteArea":112,"suiteImages":null,"hasLift":"\u6709","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.26286,120.208389","blockLatLon":"30.316902,120.285122","xiaoquLonLat":"30.308696,120.291794","subwayLonLat":"30.316913,120.285099","subwayTitle":"\u5ba2\u8fd0\u4e2d\u5fc3","subwayDuration":1492,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":350,"roomTip":null,"roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":1440},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190519-FjKQxdl7ii0jSmWMSEllNE8-mfsz\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":24382,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"32125-A","id":105876,"publicArea":10,"publicSuiteArea":112,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u897f\u6e56\u533a","subway":"2\u53f7\u7ebf,5\u53f7\u7ebf","block":"\u4e09\u575d","price":1990,"bedroomNum":3,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u4e3b\u5367","face":"\u5357","searchText":"60752-A,\u5723\u82d1\u5c0f\u533a\u5c0f\u533a10\u697c2\u5355\u5143103\u5ba4,\u90ed\u6653\u5764,\u5723\u82d1\u5c0f\u533a,,2\u53f7\u7ebf,5\u53f7\u7ebf,\u4e09\u575d,\u897f\u6e56\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u94f6\u6cf0\u57ce,\u57ce\u897f\u94f6\u6cf0,\u5408\u79df,\u4e09\u575d\u7ad9,\u867e\u9f99\u5729,\u867e\u9f99\u5729\u7ad9,\u6d66\u5bb6\u6865,\u7ae0\u6865\u5934","subwayLines":"2\u53f7\u7ebf,5\u53f7\u7ebf","xiaoquName":"\u5723\u82d1\u5c0f\u533a","xiaoquAlias":"","roomId":"1366462553","suiteId":60752,"roomNumber":"A","roomArea":16,"monthPrice":2360,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-06-09","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20181211-FuMXfGSzxflCQR20Ns5X3IDb1JDI?imageView2\/1\/w\/380\/h\/285","floor":1,"totalFloor":25,"toiletNum":1,"suiteArea":92,"suiteImages":null,"hasLift":"\u6709","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u71c3\u6c14\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.276339,120.134422","blockLatLon":"30.305556,120.104686","xiaoquLonLat":"30.309176,120.101633","subwayLonLat":"30.305556,120.104686","subwayTitle":"\u4e09\u575d","subwayDuration":4152,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":350,"roomTip":"\u8ddd2\u53f7\u7ebf,5\u53f7\u7ebf\u4e09\u575d498\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":60},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190619-Fm89mfyLVEsPqRsnsqsT89-fqVQk\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":16889,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"60752-A","id":196795,"publicArea":16,"publicSuiteArea":92,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u6c5f\u5e72\u533a","subway":"4\u53f7\u7ebf","block":"\u5357\u8096\u57e0","price":1960,"bedroomNum":3,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u6b21\u5367","face":"\u5357","searchText":"121937-A,\u7701\u6c34\u5229\u5385\u5bbf\u820d\u5c0f\u533a1\u697c3\u5355\u5143302\u5ba4,\u5415\u6770\u633a_D_20190702,\u7701\u6c34\u5229\u5385\u5bbf\u820d,,4\u53f7\u7ebf,\u5357\u8096\u57e0,\u6c5f\u5e72\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u5408\u79df,\u5730\u94c1,\u5e86\u83f1\u8def,\u5e86\u83f1\u8def\u7ad9,\u5e86\u6625\u5e7f\u573a,\u5e86\u6625\u5e7f\u573a\u7ad9,\u666f\u82b3\u4ead,\u4e25\u5bb6\u5f04,\u91d1\u5170\u6c60","subwayLines":"4\u53f7\u7ebf","xiaoquName":"\u7701\u6c34\u5229\u5385\u5bbf\u820d","xiaoquAlias":"","roomId":"877986609","suiteId":121937,"roomNumber":"A","roomArea":10,"monthPrice":2330,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-06-17","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20190508-FmqofDBqjS82_Lu3RGdThhXLIIgV?imageView2\/1\/w\/380\/h\/285","floor":3,"totalFloor":6,"toiletNum":1,"suiteArea":56,"suiteImages":null,"hasLift":"\u65e0","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.26286,120.208389","blockLatLon":"30.267435,120.203657","xiaoquLonLat":"30.27194533,120.2047318","subwayLonLat":"30.27199,120.214247","subwayTitle":"\u666f\u82b3","subwayDuration":1218,"publicSpaceNum":1,"style":"\u6b46\u52a8LIFE","houseRank":350,"roomTip":"\u8ddd\u534e\u5bb6\u6c60454\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":null,"subScribeMin":1440,"viewMin":1440},"kujialeImage":"{\"4\":{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"\"}}","fireHouse":"\u5426","hasError":0,"housekeeperId":15020,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"121937-A","id":351891,"publicArea":10,"publicSuiteArea":56,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u6ee8\u6c5f\u533a","subway":null,"block":"\u6c5f\u9675\u8def","price":1980,"bedroomNum":4,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u9694\u65ad","face":"\u5357","searchText":"16429-B,\u7f24\u7eb7\u4e1c\u82d1\u5c0f\u533a10\u697c1\u5355\u5143304\u5ba4,\u4e8e\u5c0f\u5149,\u7f24\u7eb7\u4e1c\u82d1,,\u6c5f\u9675\u8def,\u6ee8\u6c5f\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u676d\u5dde2019\u5e747\u6708\u79df\u623f\u7acb\u77012000\u5143,\u5408\u79df,\u5730\u94c1,\u676d\u5dde\u8fd1\u5730\u94c1\u6d3b\u52a8","subwayLines":null,"xiaoquName":"\u7f24\u7eb7\u4e1c\u82d1","xiaoquAlias":"","roomId":"152242531","suiteId":16429,"roomNumber":"B","roomArea":14,"monthPrice":2360,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-05-12","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20180130-FjuqesJsQgh5oVQVKQmkZKW2uS0s?imageView2\/1\/w\/380\/h\/285","floor":3,"totalFloor":27,"toiletNum":1,"suiteArea":108,"suiteImages":null,"hasLift":"\u6709","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.209447,120.209161","blockLatLon":"30.215452,120.223004","xiaoquLonLat":"30.22253,120.230929","subwayLonLat":null,"subwayTitle":null,"subwayDuration":null,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":340,"roomTip":null,"roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":60},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190519-Flf38W-GS6pXO7qfPxOZMbW4j3He\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":3923,"isSeparatedRoom":"\u662f","isNewTrend":null,"roomCode":"16429-B","id":53121,"publicArea":14,"publicSuiteArea":108,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u6ee8\u6c5f\u533a","subway":null,"block":"\u6c5f\u9675\u8def","price":1980,"bedroomNum":4,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u9694\u65ad","face":"\u5357","searchText":"16328-B,\u7f24\u7eb7\u4e1c\u82d1\u5c0f\u533a5\u697c1\u5355\u51431804\u5ba4,\u865e\u94a6\u950b1,\u7f24\u7eb7\u4e1c\u82d1,,\u6c5f\u9675\u8def,\u6ee8\u6c5f\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u676d\u5dde2019\u5e747\u6708\u79df\u623f\u7acb\u77012000\u5143,\u5408\u79df,\u5730\u94c1,\u676d\u5dde\u8fd1\u5730\u94c1\u6d3b\u52a8","subwayLines":null,"xiaoquName":"\u7f24\u7eb7\u4e1c\u82d1","xiaoquAlias":"","roomId":"1644598467","suiteId":16328,"roomNumber":"B","roomArea":13,"monthPrice":2360,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-06-01","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20180130-Fj2rd2s13h6lunKmvR_aGWa8ZJTx?imageView2\/1\/w\/380\/h\/285","floor":18,"totalFloor":25,"toiletNum":1,"suiteArea":110,"suiteImages":null,"hasLift":"\u6709","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.209447,120.209161","blockLatLon":"30.215452,120.223004","xiaoquLonLat":"30.22253,120.230929","subwayLonLat":null,"subwayTitle":null,"subwayDuration":null,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":340,"roomTip":null,"roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":1440},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190605-Fm4uHy1IM3ieolvb5u0gk1-YYJYc\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":26754,"isSeparatedRoom":"\u662f","isNewTrend":null,"roomCode":"16328-B","id":52705,"publicArea":13,"publicSuiteArea":110,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u4e0a\u57ce\u533a","subway":"1\u53f7\u7ebf","block":"\u5a7a\u6c5f\u8def","price":1920,"bedroomNum":3,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u6b21\u5367","face":"\u4e1c\u5357","searchText":"120999-A,\u8fd1\u6c5f\u82d1\u5c0f\u533a8\u697c3\u5355\u5143202\u5ba4,\u5510\u52e41_D_20190702,\u8fd1\u6c5f\u82d1,,1\u53f7\u7ebf,\u5a7a\u6c5f\u8def,\u4e0a\u57ce\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u676d\u5dde2019\u5e747\u6708\u79df\u623f\u7acb\u77011000\u5143,\u5408\u79df,\u5730\u94c1,\u8fd1\u6c5f,\u8fd1\u6c5f\u7ad9,\u5a7a\u6c5f\u8def\u7ad9,\u89c2\u97f3\u5858,\u8fd1\u6c5f\u6751,\u603b\u7ba1\u5858,7\u6708\u676d\u5dde\u6d3b\u52a8","subwayLines":"1\u53f7\u7ebf","xiaoquName":"\u8fd1\u6c5f\u82d1","xiaoquAlias":null,"roomId":"1017885577","suiteId":120999,"roomNumber":"A","roomArea":9,"monthPrice":2290,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-07-09","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20190415-Fu-Lwr44kbu_5O81w5ONINXeKxHB?imageView2\/1\/w\/380\/h\/285","floor":2,"totalFloor":7,"toiletNum":1,"suiteArea":63,"suiteImages":null,"hasLift":"\u65e0","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.236985,120.181422","blockLatLon":"30.242674,120.197411","xiaoquLonLat":"30.243323,120.203553","subwayLonLat":"30.242686,120.197416","subwayTitle":"\u5a7a\u6c5f\u8def","subwayDuration":500,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":340,"roomTip":"\u8ddd1\u53f7\u7ebf\u5a7a\u6c5f\u8def594\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":1440},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190520-FgIXAdu0bEyyxpzjEywsnXY79Ucj\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":10648,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"120999-A","id":347371,"publicArea":9,"publicSuiteArea":63,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u4f59\u676d\u533a","subway":null,"block":"\u672a\u6765\u79d1\u6280\u57ce","price":1490,"bedroomNum":5,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u6b21\u5367","face":"\u5357","searchText":"30486-E,\u91d1\u5730\u897f\u6eaa\u98ce\u534e\u5c0f\u533a19\u697c3\u5355\u5143301\u5ba4,\u9648\u51ef\u8fea,\u91d1\u5730\u897f\u6eaa\u98ce\u534e,,\u672a\u6765\u79d1\u6280\u57ce,\u4f59\u676d\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u5408\u79df,\u5730\u94c1,\u6c38\u798f\u6751,\u4f55\u6bcd\u6865,\u6a2a\u5bb6\u6865","subwayLines":null,"xiaoquName":"\u91d1\u5730\u897f\u6eaa\u98ce\u534e","xiaoquAlias":null,"roomId":"779367169","suiteId":30486,"roomNumber":"E","roomArea":13,"monthPrice":1790,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-06-23","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20180702-FmM3kbJ-diy4G6S-2AQQQdEF2zdk?imageView2\/1\/w\/380\/h\/285","floor":3,"totalFloor":6,"toiletNum":1,"suiteArea":136,"suiteImages":null,"hasLift":"\u6709","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.425214,120.309313","blockLatLon":"30.284844,120.033075","xiaoquLonLat":"30.28019,120.037545","subwayLonLat":null,"subwayTitle":null,"subwayDuration":null,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":340,"roomTip":"\u8ddd\u672a\u6765\u79d1\u6280\u57ce673\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":null,"subScribeMin":1440,"viewMin":10},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190630-FkR9U8nDBUzWuh7UhdKtyriIZtcX\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":23934,"isSeparatedRoom":"\u5426","isNewTrend":null,"roomCode":"30486-E","id":98403,"publicArea":13,"publicSuiteArea":136,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u8427\u5c71\u533a","subway":"2\u53f7\u7ebf","block":"\u4fe1\u606f\u6e2f","price":1800,"bedroomNum":4,"hasToilet":"\u65e0","hasBalcony":"\u6709","hasShower":"\u65e0","bedroomType":"\u9694\u65ad","face":"\u5357","searchText":"55099-D,\u4fdd\u5229\u971e\u98de\u90e1\u5c0f\u533a25\u697c1\u5355\u51432603\u5ba4,\u6c5f\u4e07\u6797,\u4fdd\u5229\u971e\u98de\u90e1,,2\u53f7\u7ebf,\u4fe1\u606f\u6e2f,\u8427\u5c71\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u5408\u79df,\u5174\u8bae\u6751,\u5408\u4e30\u5317,\u5408\u4e30\u5357","subwayLines":"2\u53f7\u7ebf","xiaoquName":"\u4fdd\u5229\u971e\u98de\u90e1","xiaoquAlias":"","roomId":"1340719049","suiteId":55099,"roomNumber":"D","roomArea":16,"monthPrice":2130,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-06-28","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20181114-Fk86urWVIt6bmo2SIA0o8JsY9y2o?imageView2\/1\/w\/380\/h\/285","floor":26,"totalFloor":27,"toiletNum":1,"suiteArea":89,"suiteImages":null,"hasLift":"\u6709","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.217362,120.369726","blockLatLon":"30.209957,120.254082","xiaoquLonLat":"30.207458,120.254074","subwayLonLat":"30.200097,120.273004","subwayTitle":"\u5efa\u8bbe\u4e00\u8def","subwayDuration":2611,"publicSpaceNum":1,"style":"\u5de5\u4e1a\u98ce","houseRank":335,"roomTip":"\u8ddd\u4fe1\u606f\u6e2f278\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":null,"subScribeMin":1440,"viewMin":60},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190520-FuW6m_z4IL5wKJm2477oYYfqMxO_\"}]","fireHouse":"\u662f","hasError":0,"housekeeperId":16664,"isSeparatedRoom":"\u662f","isNewTrend":null,"roomCode":"55099-D","id":178475,"publicArea":16,"publicSuiteArea":89,"isActiveRoom":true},{"brand":"\u86cb\u58f3\u516c\u5bd3","rentType":"\u5408\u79df","city":"\u676d\u5dde\u5e02","district":"\u897f\u6e56\u533a","subway":"2\u53f7\u7ebf","block":"\u53e4\u58a9\u8def","price":1720,"bedroomNum":3,"hasToilet":"\u65e0","hasBalcony":"\u65e0","hasShower":"\u65e0","bedroomType":"\u9694\u65ad","face":"\u897f","searchText":"52997-B,\u534e\u82d1\u516c\u5bd3\u5c0f\u533a1\u697c1\u5355\u5143402\u5ba4,\u4f55\u4fca\u6d9b,\u534e\u82d1\u516c\u5bd3,,2\u53f7\u7ebf,\u53e4\u58a9\u8def,\u897f\u6e56\u533a,\u676d\u5dde\u5e02,\u670d\u52a1\u8d39\u6253\u516b\u6298,\u676d\u5dde2019\u5e747\u6708\u79df\u623f\u7acb\u77011000\u5143,\u94f6\u6cf0\u57ce,\u57ce\u897f\u94f6\u6cf0,\u5408\u79df,\u6587\u65b0,\u6587\u65b0\u7ad9,\u9a86\u5bb6\u5e84,\u6842\u82b1\u57ce,\u7d2b\u540d\u5df7,\u96c5\u4ed5\u82d1,7\u6708\u676d\u5dde\u6d3b\u52a8","subwayLines":"2\u53f7\u7ebf","xiaoquName":"\u534e\u82d1\u516c\u5bd3","xiaoquAlias":"","roomId":"327990705","suiteId":52997,"roomNumber":"B","roomArea":7,"monthPrice":2030,"roomStatus":"\u53ef\u51fa\u79df","availableDate":"2019-05-20","hasImage":"\u6709","hasVideo":"\u65e0","roomImages":"https:\/\/public.danke.com.cn\/public-20181109-FtB_jlEH_neXXn7Bj1TSyhVqSI2j?imageView2\/1\/w\/380\/h\/285","floor":4,"totalFloor":7,"toiletNum":1,"suiteArea":67,"suiteImages":null,"hasLift":"\u65e0","heating":"\u65e0\u6696\u6c14","hotWaterType":"\u7535\u70ed\u6c34\u5668","subwayNearby":null,"isMonth":"\u5426","panorama":null,"isNearSubway":null,"subwayDistance":null,"suiteStatus":"\u73b0\u623f","districtLatLon":"30.276339,120.134422","blockLatLon":"30.285438,120.106607","xiaoquLonLat":"30.293455,120.104439","subwayLonLat":"30.288553,120.123766","subwayTitle":"\u53e4\u7fe0\u8def","subwayDuration":2397,"publicSpaceNum":1,"style":"MUJI\u98ce","houseRank":330,"roomTip":"\u8ddd2\u53f7\u7ebf\u6587\u65b0241\u7c73","roomUrgency":{"hotBlock":null,"daikanMin":1440,"subScribeMin":1440,"viewMin":60},"kujialeImage":"[{\"roomName\":\"\\u6237\\u578b\\u56fe\",\"picId\":\"\\u6237\\u578b\\u56fe\",\"created\":\"\",\"img\":\"public-20190522-Fl61IWRfZa2gv_5Xfd_6qnci7a5I\"}]","fireHouse":"\u5426","hasError":0,"housekeeperId":8353,"isSeparatedRoom":"\u662f","isNewTrend":null,"roomCode":"52997-B","id":173075,"publicArea":7,"publicSuiteArea":67,"isActiveRoom":true}],"from":1,"last_page":250,"next_page_url":"\/?page=2","path":"\/","per_page":20,"prev_page_url":null,"to":20,"total":4985}
#         var newArr = []
#         var rlbxArr = $('.r_lbx')
#         var mapArr = roomsObject.data
#
#         addOrRemoveArr(rlbxArr, newArr)
#         resetMap(newArr)
#         addRoomLocation(newArr)
#
#         window.onscroll = function () {
#             if($('.zf_sebox').offset().top - $(window).scrollTop() + 20 <= 0){
#                 $('.search-header-wrapper').fadeIn(500)
#                 $('.danke_header').fadeOut(500)
#
#             }else{
#                 $('.search-header-wrapper').fadeOut(500)
#                 $('.danke_header').fadeIn(500)
#             }
#
#             if($('.list-wrapper').offset().top + $('.list-wrapper').height() - $(window).scrollTop() - 60 > 675){
#                 $('.list-map-wrapper').addClass('map-fixed').css({'right': ($(window).width() - 1190) / 2, 'top': '60px'})
#             }
#
#             if($('.list-map-wrapper').offset().top - $(window).scrollTop() - 60 <= 0){
#                 $('.list-map-wrapper').addClass('map-fixed').css('right', ($(window).width() - 1190) / 2)
#             }
#             if($('.list-wrapper').offset().top - $(window).scrollTop() - 60 > 0){
#                 $('.list-map-wrapper').removeClass('map-fixed').css({'right': 0, 'top': 0})
#             }
#
#             // console.log($('.list-wrapper').offset().top + $('.list-wrapper').height() - $(window).scrollTop() - 60)
#             if($('.list-wrapper').offset().top + $('.list-wrapper').height() - $(window).scrollTop() - 60 < 675){
#                 $('.list-map-wrapper').removeClass('map-fixed').css({'right': 0, 'top': $('.list-wrapper').height() - 680 + 'px'})
#             }
#
#             addOrRemoveArr(rlbxArr, newArr)
#             resetMap(newArr)
#             addRoomLocation(newArr)
#         }
#
#         function addOrRemoveArr(rlbxArr, newArr) {
#             for(var i=0; i<rlbxArr.length; i++){
#                 if($(rlbxArr[i]).offset().top - $(window).scrollTop() < $(window).height() && $(rlbxArr[i]).offset().top - $(window).scrollTop() > -234 && newArr.indexOf($(rlbxArr[i]).find('.location').text()) === -1){
#                     newArr.push($(rlbxArr[i]).find('.location').text())
#                 }
#                 else if($(rlbxArr[i]).offset().top - $(window).scrollTop() > $(window).height() && newArr.indexOf($(rlbxArr[i]).find('.location').text()) !== -1){
#                     var index = newArr.indexOf($(rlbxArr[i]).find('.location').text())
#                     newArr.splice(index, 1)
#                 }
#                 else if($(rlbxArr[i]).offset().top - $(window).scrollTop() + 234 < 0 && newArr.indexOf($(rlbxArr[i]).find('.location').text()) !== -1){
#                     var index = newArr.indexOf($(rlbxArr[i]).find('.location').text())
#                     newArr.splice(index, 1)
#                 }
#             }
#         }
#
#         function addRoomLocation(newArr) {
#             map.clearOverlays()
#             $('.pop-list').empty()
#             for(var i=0; i<newArr.length; i++){
#                 var room = mapArr[newArr[i] * 1 - 1]
#                 if(room){
#                     var a = new SquareOverlay(newArr[i], room);
#                     map.addOverlay(a);
#                 }
#             }
#         }
#
#         function resetMap(newArr) {
#             var viewpoints = [];
#             for(var i=0; i<newArr.length; i++){
#                 var room = mapArr[newArr[i] * 1 - 1]
#                 if(room){
#                     var pos = new BMap.Point(room.xiaoquLonLat.split(",")[1], room.xiaoquLonLat.split(",")[0])
#                     viewpoints.push(pos)
#                 }
#             }
#             // map.setViewport(viewpoints);
#             var a = map.getViewport(viewpoints);
#             map.centerAndZoom(a.center, a.zoom);
#         }
#
#         // 查看大图
#         var rimgArr = $('.rimg'),
#             sourceType = 'room';
#
#         rimgArr.each(function (i, n) {
#             $(n).on('click', function () {
#                 $('.shade-wrapper').show()
#                 $($('.img-list-wrapper div img')[0]).css('border', '1px solid red')
#                 $('.big-img').attr('src', $($('.img-list-wrapper div img')[0]).attr('src'))
#                 $('.img-list-wrapper div').empty()
#                 $('.configuration').empty()
#                 if($(this).siblings('.r_lbx_cen').find('.r_lbx_cena').find('a').attr('href').split('duanzu').length>1){
#                     sourceType='duanzu';
#                 }
#                 $.ajax({
#                     type: 'GET',
#                     url: '/room/info/' + mapArr[i].roomId + '?source=' + sourceType,
#                     async: false,
#                     error: function(msg) {
#                     },
#                     success: function(data) {
#                         if(data.success){
#                             console.log(data)
#                             $('.big-img').attr('src', data.data.images[0])
#                             $(data.data.images).each(function (index, value) {
#                                 var img = document.createElement("img");
#                                 $(img).attr('src', value)
#                                 $(img).attr('alt', data.data.title)
#                                 $('.img-list-wrapper div').append(img)
#                             })
#                             $('.info-title').text(data.data.title)
#
#                             if(data.data.is_activity){
#                                 $('.money-look').html(
#                                     '<div>' +
#                                         '<div>' +
#                                             '<span class="money-unit">月租金 &nbsp;&nbsp;</span>' +
#                                             '<s>'+ data.data.price +' 元/月</s>' +
#                                         '</div>' +
#                                         '<div>' +
#                                            ' <span>' +
#                                                 '<span class="money-unit">首月租金 &nbsp;&nbsp;</span>' +
#                                                 '<span class="money-num">'+ data.data.activity.yearReduceMoney +'</span>' +
#                                                 '<span class="money-unit">元/月</span>' +
#                                             '</span>' +
#                                             '<a class="look-btn" target="_blank" href="'+ data.data.room_link +'" style="margin-left:60px;">查看房间详情</a>' +
#                                         '</div>' +
#                                         '<div style="margin-top:10px;">' +
#                                             '<span class="money-unit">活动说明 &nbsp;&nbsp;</span>' +
#                                             '<span>'+ data.data.activity.activityTitle +'</span>' +
#                                         '</div>' +
#                                     '</div>'
#                                 )
#                             }else(
#                                 $('.money-look').html(
#                                     '<div>' +
#                                         '<span>' +
#                                             '<span class="money-num">'+ data.data.price +'</span>' +
#                                             '<span class="money-unit">元/月</span>' +
#                                         '</span>' +
#                                         '<a class="look-btn" target="_blank" href="'+ data.data.room_link +'">查看房间详情</a>' +
#                                     '</div>'
#                                 )
#                             )
#
#                             // $('.look-btn').attr('href', data.data.room_link)
#                             $('.info-sub').html('<span></span>' + data.data.nearby_subway)
#                             $('.info-pattern').html('<span></span>约'+ data.data.area +'㎡ |  '+ data.data.floor +'楼 | '+ data.data.bedroom_num +' | 朝' + data.data.face)
#                             $('.subscribe-btn').attr('href', data.data.room_link + '?clickbtn=true')
#
#                             var colorClass = {
#                                 '独立卫生间': 'red-color',
#                                 '独立淋浴': 'red-color',
#                                 '独立阳台': 'red-color',
#                                 '集中供暖': 'yellow-color',
#                                 '自采暖': 'yellow-color',
#                                 '装配中可预约': 'green-color',
#                                 '可立即入住': 'green-color',
#                             };
#
#                             $(data.data.labels).each(function (index, val) {
#                                 var span = document.createElement("span");
#                                 $(span).addClass(colorClass[val] || '')
#                                 $(span).text(val)
#                                 $('.configuration').append(span)
#                             })
#                             lookBigImg()
#                         }
#                     },
#                 })
#             })
#         })
#
#         $('.shade-close').on('click', function () {
#             $('.shade-wrapper').hide()
#         })
#
#         lookBigImg()
#
#         function lookBigImg() {
#             $($('.img-list-wrapper div img')[0]).css('border', '1px solid red')
#             $('.img-list-wrapper div img').on('mouseover', function () {
#                 var url = $(this).attr('src')
#                 $('.big-img').attr('src', url)
#                 $(this).css('border', '1px solid red')
#                 $(this).siblings().css('border', 'none')
#             })
#
#             if($('.img-list-wrapper div img').length > 5){
#                 $('.small-img-nex').addClass('nex-can-click')
#                 $('.nex-can-click').on('click', function () {
#                     $('.small-img-pre').addClass('pre-can-click')
#                     $('.small-img-nex').removeClass('nex-can-click')
#
#                     $('.img-list-wrapper div').stop().animate({left:'-624px'});
#
#                     $('.pre-can-click').on('click', function () {
#                         $('.small-img-pre').removeClass('pre-can-click')
#                         $('.small-img-nex').addClass('nex-can-click')
#                         $('.img-list-wrapper div').stop().animate({left:'8.5px'});
#                     })
#                 })
#             }else{
#                 $('.small-img-pre').removeClass('pre-can-click')
#                 $('.small-img-nex').removeClass('nex-can-click')
#             }
#         }
#
#         // 获取热门房源
#         $.ajax({
#             type: 'GET',
#             url: '/room/hotroom/' + 'bj',
#             async: false,
#             error: function(msg) {
#             },
#             success: function(data) {
#                 if(data.success){
#                     var a = ''
#
#                     $(data.data).each(function (i, val) {
#
#                         a += '<div class="hot-room-item">' +
#                                 '<a href="'+ val.room_link +'" target="_blank">'+
#                                     '<img src="'+ val.pic +'" alt="">' +
#                                     ' <div class="hot-room-content">' +
#                                             '<div>' +
#                                                 '<span class="hot-room-money">￥'+ val.price +'</span>' +
#                                                 '<span class="hot-room-unit">元/月</span>' +
#                                             '</div>' +
#                                             ' <div>'+ val.name +'</div>' +
#                                             '<div>地铁'+ val.subway +'</div>' +
#                                     '</div>' +
#                                 '</a>'+
#                             '</div>'
#                     })
#
#                     $('.hot-room-list div').html(a)
#                 }
#             },
#         })
#
#         // 热门房源分
#         var tim = null
#
#         hotRoomCarousel()
#         function hotRoomCarousel() {
#             tim = setInterval(function () {
#                 if($('.one').hasClass('isthispage')){
#                     $('.two').addClass('isthispage')
#                     $('.one').removeClass('isthispage')
#                     $('.hot-room-list-wp').stop().animate({'left': '-381px'}, 'slow')
#                 } else {
#                     $('.one').addClass('isthispage')
#                     $('.two').removeClass('isthispage')
#                     $('.hot-room-list-wp').stop().animate({'left': 0}, 'slow')
#                 }
#             }, 5000)
#         }
#
#         $('.pre').on('click', function () {
#             clearInterval(tim)
#             $('.one').addClass('isthispage')
#             $('.two').removeClass('isthispage')
#             $('.hot-room-list-wp').stop().animate({'left': 0}, 'slow')
#             hotRoomCarousel()
#         })
#         $('.nex').on('click', function () {
#             clearInterval(tim)
#             $('.two').addClass('isthispage')
#             $('.one').removeClass('isthispage')
#             $('.hot-room-list-wp').stop().animate({'left': '-381px'}, 'slow')
#             hotRoomCarousel()
#         })
#
#         $('.rimg').hover(function () {
#             $(this).css('box-shadow', '0px 5px 5px 0px #d1d1d1')
#         }, function () {
#             $(this).css('box-shadow', 'none')
#         })
#     }
#
# </script>
#
#
#                     </div>
#
#         <!--房源列表 end-->
#
#     <!--附近推荐-->
#             <!--附近推荐-->
#
#     <!--猜你喜欢-->
#         <div class="y_like_box" id="y-guest-like">
#             <div class="lk_titl">
#                 好房推荐
#             </div>
#             <div class="lk_room_box" id="guest-like"></div>
#             <script>
#                 saMethod.RecoModuleEXP('找房频道', '房源列表', window.location.href, '', '', '', '', '', '猜你喜欢', '')
#             </script>
#         </div>
#         <!--猜你喜欢 end-->
#     </div>
#
#     <script>
#         $('.lk_room_box').click(function () {
#             saMethod.RecoClick('找房频道', '房源列表', window.location.href, '', '', '', '', '', '', '', $(this).siblings('.lk_titl').text(), '')
#         })
#     </script>
#
# </div>
# <div class="footer">
#     <div class="website-help">
#         <div class="wibsite-center">
#             <div class="website-f-list">
#                 <span>用户帮助</span>
#                 <p><a href="/about/notice.html" target="_blank">入住指南</a></p>
#                 <p><a href="/zhuanti/20180111lifeHacks" target="_blank">生活常识</a></p>
#                 <p><a href="/about/problem.html" target="_blank">租房问题</a></p>
#             </div>
#             <div class="website-f-list">
#                 <span>商务合作</span>
#                 <p><a href="/zhuanti/20171219Styleforum" target="_blank">商务合作</a></p>
#             </div>
#             <div class="website-f-list">
#                 <span>公司信息</span>
#                 <p><a href="https://www.danke.com/about/aboutus.html"
#                       target="_blank">关于蛋壳</a></p>
#                 <p><a href="https://www.danke.com/about/contact.html"
#                       target="_blank">联系蛋壳</a></p>
#                 <p><a href="https://www.danke.com/about/join.html" target="_blank">加入蛋壳</a>
#                 </p>
#             </div>
#             <div class="website-f-list">
#                 <span>客服热线</span>
#                 <p>4001-551-551</p>
#                 <p class="time">服务时间 09:00-21:00</p>
#             </div>
#             <div class="website-f-right">
#                 <div class="website-f-pic index-qyx">
#                     <b><img src="//public.danke.com.cn/public-20190220-Fk9q0ko59hYEY9cPOzSca0TaC6_A" title="企优享"
#                             alt="企优享"></b>
#                     <p>企优享</p>
#                 </div>
#                 <div class="website-f-pic index-zfb">
#                     <b><img src="//public.danke.com.cn/public-20190116-FkDQ7BtPiOtdR1VnMaqzsodSAhPJ" title="支付宝小程序"
#                             alt="支付宝小程序"></b>
#                     <p>支付宝小程序</p>
#                 </div>
#                 <div class="website-f-pic index-xcx">
#                     <b><img src="//public.danke.com.cn/public-20180702-FlfqqYRpjYyFKdRUiJMD8b6RO02m" title="下载蛋壳公寓APP"
#                             alt="下载蛋壳公寓APP"></b>
#                     <p>小程序找房</p>
#                 </div>
#                 <div class="website-f-pic index-app">
#                     <b><img src="https://public.danke.com.cn/public-20180724-FvFKon429iKW8-oJFhggv0NQk_cH"
#                             style="padding:0;" title="下载蛋壳公寓APP" alt="下载蛋壳公寓APP"></b>
#                     <p>蛋壳公寓APP</p>
#                 </div>
#                 <div class="website-f-pic index-wechat">
#                     <b><img src="//public.danke.com.cn/public-20180104-FuHnSFKo71wRSuJSK4Z0pt6l76zh" title="关注蛋壳公寓官方微信"
#                             alt="关注蛋壳公寓官方微信"></b>
#                     <p>关注微信公众号</p>
#                 </div>
#             </div>
#             <div style="clear:both;padding-top: 20px;display:none">
#                 <p style="color:#fff;font-size: 16px">专属管家、极速WIFI、双周保洁、环保装修、高档家居</p>
#             </div>
#         </div>
#     </div>
#     <div class="crumbs">
#         <div class="crumbs-classify">
#             <a class="crumbs-sel" code="city" href="javascript:;">城市租房</a>
#             <a href="javascript:;" code="dirc">城区租房</a>
#             <a href="javascript:;" code="block">商圈租房</a>
#             <a href="javascript:;" code="plot">小区租房</a>
#         </div>
#         <div>
#             <div class="crumbs-list city">
#
#             </div>
#             <div class="crumbs-list dirc" style="display:none">
#
#             </div>
#             <div class="crumbs-list block" style="display:none">
#
#             </div>
#             <div class="crumbs-list plot" style="display:none">
#
#             </div>
#         </div>
#     </div>
#     <div class="copy-right">
#         <div class="wibsite-center">
#             <div class="footer-logo">
#                 <a href="/">
#                     <img src="https://public.danke.com.cn/public-20180702-FkLmdf41L0FSNAktybhKBxCs7ztn" alt="蛋壳公寓">
#                 </a>
#             </div>
#             <div class="copy-right-text">
#                 <div><a href="http://www.beian.miit.gov.cn" target="_blank" style="color: #fff">© 2019 蛋壳公寓 沪ICP备18043153号-1</a></div>
#                 <div>
#                     <img src="https://public.danke.com.cn/public-20190628-FinEALw7ifYIV2baxOAzDe1ctz1S" style="display: inline-block;width: 10px">
#                     <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102003786" target="_blank" style="color: #fff">京公网安备 11010102003786号</a>
#                 </div>
#             </div>
#         </div>
#     </div>
#
#     <div class="custom-house">
#         <div class="custom-center">
#             <div class="custom-house-title">输入您的找房需求，我们会尽快安排销售，用心带您找到心仪的房源</div>
#             <div class="custom-house-address">
#                 <div class="intention-position">意向位置：</div>
#                 <div class="list_part">
#                     <div class="city_xs">
#                         <div class="city_list_title"></div>
#                         <div class="city_list_tab">
#                             <ul class="city_ul">
#                             </ul>
#                         </div>
#                     </div>
#
#                     <div class="district_xs">
#                         <div class="district_list_title">不限</div>
#                         <div class="district_list_tab">
#                             <ul class="district_ul">
#                             </ul>
#                         </div>
#                     </div>
#
#                     <div class="block_xs">
#                         <div class="block_list_title">不限</div>
#                         <div class="block_list_tab">
#                             <ul class="block_ul">
#                             </ul>
#                         </div>
#                     </div>
#                 </div>
#             </div>
#             <div class="import-address">
#                 <input type="text" placeholder="可手动输入多个地址，以，隔开" class="address_inp" maxlength="50">
#             </div>
#             <div class="price-budget">
#                 <div class="budget-title">租房预算：</div>
#                 <div class="budget_list_title">不限</div>
#                 <div class="budget_list_tab">
#                     <ul class="budget_ul">
#                         <li class="on">不限</li>
#                         <li>1500以下</li>
#                         <li>1500-2000元</li>
#                         <li>2000-2500元</li>
#                         <li>2500-3000元</li>
#                         <li>3000元</li>
#                     </ul>
#                 </div>
#             </div>
#             <div class="custom-phoneNum">
#                 <div class="phoneNum-part">
#                     <div class="phoneNum-title"><span class="sign">*</span>联系方式：</div>
#                 </div>
#                 <input type="tel" placeholder="请输入正确电话，以便我们联系到您" class="phone_num_inp" maxlength="11">
#             </div>
#             <div class="submit_btn" data-toggle="modal" data-target="#myroom">提交</div>
#             <div class="close_img"></div>
#         </div>
#     </div>
#
#     <div class="order_room">
#         <div class="succesbox_detail" style="display: block">
#             <div class="success_close">×</div>
#             <div class="wt_detail">
#                 <div class="wt_explain">
#                     <div class="wt_img"></div>
#                     <h2 class="wt_title">意向提交成功！</h2>
#                     <h3 class="wt_sub_title">客服会在24小时内联系您，请不要拒接座机，
#                         保持电话畅通噢！</h3>
#                 </div>
#                 <div class="wt_dec_title">让租房变得简单和快乐
#                     <div class="wt_line"></div>
#                 </div>
#                 <div class="wt_icons">
#                     <div class="detail_img_logo"></div>
#                 </div>
#             </div>
#             <div class="wt_ewm">
#                 <div class="wt_ewm_image"></div>
#                 <div class="wt_sm">扫一扫</div>
#                 <div class="wt_sm">下载<span>蛋壳公寓</span></div>
#             </div>
#         </div>
#     </div>
#
#
# </div>
# <script type="text/javascript">
#     /*退出登录*/
#
#     $(".dklogout").on("click", function () {
#         $.ajaxSetup({
#     headers: {
#         'X-CSRF-TOKEN': 'KiXUcaP7ZnsekTKv11DFkSEe3dMiunS48lkBbC16'
#     },
#     cache: false,
#     async: false,
# });;
#         $.ajax({
#             url: '/web-api/user/logout',
#             type: "POST",
#             success: function (data) {
#                 location.reload()
#             },
#             error: function (err) {
#                 console.log(err);
#             }
#         })
#     })
#
#     $('.dklogined-wrapper').hover(function () {
#         $('.dklogined-center').show()
#         $('.dklogined').css('background', 'url(https://public.danke.com.cn/public-20180519-FqitD4IbypL6rbHSVa_yq4iSsaQE)')
#     }, function () {
#         $('.dklogined-center').hide()
#         $('.dklogined').css('background', 'url(https://public.danke.com.cn/public-20180519-FtfmOHVmUq7-6Tzol_cyQBE9yt3y)')
#     })
#
#     $('.scroll-to-phone').hover(function () {
#         $('.scroll-to-phone div').show()
#         $('.scroll-to-xcx div').hide()
#         $('.xcx-close').hide()
#     }, function () {
#         $('.scroll-to-phone div').hide()
#     })
#
#     $('.scroll-to-app').hover(function () {
#         $('.scroll-to-app div').show()
#         $('.scroll-to-xcx div').hide()
#         $('.scroll-to-app a').css('background-color', '#3dbcc6')
#         $('.xcx-close').hide()
#     }, function () {
#         $('.scroll-to-app div').hide()
#         $('.scroll-to-app a').css('background-color', '#333333')
#     })
#
#     $('.scroll-to-xcx').hover(function () {
#         $('.scroll-to-xcx div').show()
#         $('.scroll-to-xcx a').css('background-color', '#3dbcc6')
#     }, function () {
#         $('.scroll-to-xcx div').hide()
#         $('.scroll-to-xcx a').css('background-color', '#333333')
#         $('.xcx-close').hide()
#     })
#
#     $('.xcx-close').on('click', function () {
#         $('.scroll-to-xcx div').hide()
#         $('.xcx-close').hide()
#     })
#
#     $('.crumbs-classify a').on('click', function () {
#         $(this).addClass('crumbs-sel')
#         $(this).siblings().removeClass('crumbs-sel')
#
#         var code = '.crumbs-list.' + $(this).attr('code')
#         $(code).show()
#         $(code).siblings().hide()
#     });
#
#
#     $('.custom_huose').on('click', function () {
#         $('body').css('overflow-y', 'hidden');
#         $('.custom-house').show();
#         saMethod.orderRoomPCClick('PC入口点击');
#     });
#
#     $('.close_img').on('click', function () {
#         $('body').css('overflow-y', 'auto');
#         $('.custom-house').hide();
#     });
#
#     $('.success_close').on('click', function () {
#         $('.order_room').hide();
#     });
#
#     var city_id_list = [],
#             city_name_list = [],
#             district_id_list = [],
#             district_name_list = [],
#             block_id_list = [],
#             block_name_list = [],
#             myBudget = '不限',
#             currentCityId,
#             currentCityName,
#             currentDistrictId = 0,
#             currentDistrictName,
#             currentBlockId = 0,
#             currentBlockName,
#             submit = true,
#             token = $("input[name='_token']").val();
#
#     //城市id
#     var city_id = true;
#     $('.city_list_title').on('click', function () {
#         if (city_id) {
#             $('.city_list_tab').show();
#             $('.district_list_tab').hide();
#             $('.block_list_tab').hide();
#             city_id = false;
#             district_id = true;
#             block_id = true;
#         } else {
#             $('.city_list_tab').hide();
#             city_id = true;
#         }
#     });
#
#     //district id
#     var district_id = true;
#     $('.district_list_title').on('click', function () {
#         if (district_id) {
#             $('.district_list_tab').show();
#             $('.city_list_tab').hide();
#             $('.block_list_tab').hide();
#             city_id = true;
#             district_id = false;
#             block_id = true;
#         } else {
#             $('.district_list_tab').hide();
#             district_id = true;
#         }
#     });
#
#     //block id
#     var block_id = true;
#     $('.block_list_title').on('click', function () {
#         if (block_id) {
#             $('.block_list_tab').show();
#             $('.city_list_tab').hide();
#             $('.district_list_tab').hide();
#             city_id = true;
#             district_id = true;
#             block_id = false;
#         } else {
#             $('.block_list_tab').hide();
#             block_id = true;
#         }
#     });
#
#
#     var price_select = true;
#     $(".budget_list_title").on('click', function () {
#         if (price_select) {
#             $('.budget_list_tab').show();
#             price_select = false;
#         } else {
#             $('.budget_list_tab').hide();
#             price_select = true;
#         }
#     });
#
#     $('.budget_ul li').on('click', function () {
#         $('.budget_ul li').removeClass('on');
#         $(this).addClass('on');
#         $('.budget_list_tab').hide();
#         $('.budget_list_title').text($(this).text());
#         price_select = true;
#         myBudget = $(this).text();
#     });
#
#     $(".phone_num_inp").bind("input propertychange", function (event) {
#         if ($(".phone_num_inp").val().length == 11) {
#             $('.submit_btn').css('background', '#3DBCC6');
#             submit = true;
#         } else {
#             $('.submit_btn').css('background', '#E4E4E4');
#             submit = false;
#         }
#     });
#
#     function district(currentCityId) {
#         $.ajax({
#             url: '/pangu-activity/marketing/custom-house-resource/district/' + currentCityId,
#             type: 'get',
#             success: function (res) {
#                 if (res.success) {
#                     district_id_list = [];
#                     district_name_list = [];
#                     $('.district_ul').empty();
#                     $('.district_ul').append('<li class="district_bx">不限</li>');
#                     $('.district_list_tab').animate({scrollTop: 0}, 100);
#                     currentDistrictId = '0';
#                     $.each(res.data, function (idx, item) {
#                         district_name_list.push(res.data[idx]);
#                         district_id_list.push(idx);
#                         $('.district_ul').append('<li>' + res.data[idx] + '</li>');
#                     });
#
#                     currentDistrictId = district_id_list[district_name_list.indexOf($('.district_ul li').eq(1).text())];
#                     $('.district_list_title').text($('.district_ul li').eq(1).text());
#                     $('.district_ul li').eq(1).addClass('on');
#                     blockPart(currentDistrictId);
#
#                     $('.district_ul li').on('click', function () {
#                         $('.district_ul li').removeClass('on');
#                         $(this).addClass('on');
#                         currentDistrictId = district_id_list[district_name_list.indexOf($(this).text())];
#                         currentDistrictName = $(this).text();
#                         $('.district_list_tab').hide();
#                         district_id = true;
#                         $('.district_list_title').text(currentDistrictName);
#                         blockPart(currentDistrictId);
#                     });
#                     $('.district_bx').click(function () {
#                         $('.city_block_list').hide();
#                         currentDistrictId = '0';
#                         blockPart(currentDistrictId);
#                     })
#                 } else {
#                     alert(res.msg);
#                 }
#             },
#             error: function () {
#                 //alert('请重新刷新此页面');
#             }
#         })
#     }
#
#     function blockPart(currentDistrictId) {
#         $.ajax({
#             url: '/pangu-activity/marketing/custom-house-resource/block/' + currentDistrictId,
#             type: 'get',
#             success: function (res) {
#                 if (res.success) {
#                     block_id_list = [];
#                     block_name_list = [];
#                     $('.block_ul').empty();
#                     $('.block_ul').append('<li class="district_bx">不限</li>');
#                     $('.block_list_title').text('不限');
#                     $('.block_list_tab').animate({scrollTop: 0}, 100);
#                     currentBlockId = '0';
#                     $.each(res.data, function (idx, item) {
#                         block_name_list.push(res.data[idx]);
#                         block_id_list.push(idx);
#                         $('.block_ul').append('<li>' + res.data[idx] + '</li>');
#                     });
#
#                     currentBlockId = block_id_list[block_name_list.indexOf($('.block_ul li').eq(1).text())];
#                     $('.block_list_title').text($('.block_ul li').eq(1).text());
#                     $('.block_ul li').eq(1).addClass('on');
#
#                     $('.block_ul li').on('click', function () {
#                         $('.block_ul li').removeClass('on');
#                         $(this).addClass('on');
#                         currentBlockId = block_id_list[block_name_list.indexOf($(this).text())];
#                         currentBlockName = $(this).text();
#                         $('.block_list_tab').hide();
#                         block_id = true;
#                         $('.block_list_title').text(currentBlockName);
#                     });
#                     $('.district_bx').click(function () {
#                         currentBlockId = '0';
#                     })
#                 } else {
#                     //alert(res.msg);
#                 }
#             },
#             error: function () {
#                 //alert('请重新刷新此页面');
#             }
#         })
#     }
#
#     $.ajax({
#         url: '/pangu-activity/marketing/custom-house-resource/city-list',
#         type: 'get',
#         success: function (res) {
#             if (res.success) {
#                 $.each(res.data, function (idx, item) {
#                     city_name_list.push(res.data[idx]);
#                     city_id_list.push(idx);
#                     $('.city_ul').append('<li>' + res.data[idx] + '</li>');
#                 });
#
#                 currentCityId = city_id_list[city_name_list.indexOf('杭州市')];
#                 $('.city_ul').children().eq(city_id_list.indexOf(currentCityId)).addClass('on');
#                 $('.city_list_title').text(res.data[currentCityId]);
#                 currentCityName = res.data[currentCityId];
#                 district(currentCityId);
#                 //点击更换城市
#                 $('.city_ul li').on('click', function () {
#                     $('.city_ul li').removeClass('on');
#                     $(this).addClass('on');
#                     currentCityId = city_id_list[city_name_list.indexOf($(this).text())];
#                     currentCityName = $(this).text();
#                     district(currentCityId);
#                     $('.city_list_tab').hide();
#                     city_id = true;
#                     $('.city_list_title').text(currentCityName)
#                 })
#             } else {
#                 alert(res.msg);
#             }
#         },
#         error: function () {
#             //alert('请重新刷新此页面');
#         }
#     });
#
#     $('.submit_btn').click(function (platform) {
#         var mobilePhone = $('.phone_num_inp').val();
#         var address_inp = $('.address_inp').val();
#         var edg = /^1[3456789][0-9]{9}$/;
#
#         if (!mobilePhone) {
#             alert('请输入手机号');
#             return;
#         }
#         if (!edg.test(mobilePhone)) {
#             alert('请输入正确的手机号');
#             return;
#         }
#
#         if (submit) {
#             submit = false;
#             $.ajax({
#                 url: '/pangu-activity/marketing/custom-house-resource/custom-info',
#                 type: 'post',
#                 data: {
#                     'mobile': mobilePhone,
#                     'city_id': currentCityId,
#                     'district_id': currentDistrictId,
#                     'block_id': currentBlockId,
#                     'address': address_inp,
#                     'budget': myBudget,
#                     '_token': token,
#                 },
#                 success: function (res) {
#                     if (res.success) {
#                         $('body').css('overflow-y', 'auto');
#                         $('.custom-house').hide();
#                         $('.modal-backdrop').show();
#                         $('.order_room').show();
#                     } else {
#                         alert(res.msg);
#                     }
#                     saMethod.orderRoomCommitBtn(mobilePhone, currentCityName, currentDistrictName, currentBlockName, address_inp, myBudget);
#                     submit = true;
#                 },
#                 error: function () {
#                     //alert('请重新刷新此页面');
#                 }
#             })
#         } else {
#             //alert('请重新刷新此页面');
#         }
#     });
#
#
#
#     getCityList('杭州', 'hz');
#     getDircList('杭州', 'hz', '')
#     getBlockList('杭州', 'hz', '')
#     getPlotList('杭州', 'hz', '')
#
# </script>
# <!--APP推广层 end-->
#     <!-- 有新房源通知我 -->
#     <div class="modal fade" id="myroom" tabindex="-1" role="dialog" aria-labelledby="myWeixinLabel" aria-hidden="true">
#         <div class="modal-dialog modal-sm onlineroom">
#             <div class="modal-content">
#                 <div class="modal-header">
#                     <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
#                     <h4 class="modal-title" id="myModalLabel">
#                         有新房源通知我
#                     </h4>
#                 </div>
#                 <div class="modal-body">
#     <form method="POST" class="form-horizontal">
#         <input type="hidden" name="_token" value="KiXUcaP7ZnsekTKv11DFkSEe3dMiunS48lkBbC16">
#         <input type="hidden" name="type" id="type" value="list">
#         <input type="hidden" name="citycode" id="citycode" value="hz">
#         <div class="state_tmobilex_box">
#                             <div class="sta_tx_b clearfix">
#                     <div class="sta_tx_b1">
#                         <span>*</span>您的需求：
#                     </div>
#                     <div class="sta_tx_b2">
#                         <textarea id="note" name="note" cols="" rows="" class="input_txt"
#                                   placeholder="我在国贸工作，我想找10号线附近的有独立卫生间，价格在2300左右的房子。" maxlength="80"></textarea>
#                     </div>
#                 </div>
#                         <input type="hidden" name="room_id" id="room_id" value="">
#                             <div class="sta_tx_b clearfix">
#                     <div class="sta_tx_b1">
#                         <span>*</span>您的姓名：
#                     </div>
#                     <div class="sta_tx_b2">
#                         <input type="text" class="text350" maxlength="20" name="name" autocomplete="off" id="name"
#                                placeholder="请输入您的姓名"/>
#                     </div>
#                 </div>
#                         <div class="sta_tx_b clearfix">
#                 <div class="sta_tx_b1">
#                     <span>*</span>联系电话：
#                 </div>
#                 <div class="sta_tx_b2">
#                     <input type="text" class="text350" name="mobile" id="mobile" autocomplete="off" maxlength="11"
#                            placeholder="请输入您的手机号"/>
#                 </div>
#             </div>
#             <div class="sta_tx_b clearfix">
#                 <div class="sta_tx_b1">
#                     <span>*</span>图片验证码：
#                 </div>
#                 <div class="sta_tx_b2">
#                     <input type="text" class="text220" name="piccode" id="piccode" placeholder="请输入图片验证码" maxlength="6">
#                     <img src="https://www.danke.com/collect/captcha"/>
#                     <a href="javascript:void(0)">换一张</a>
#                 </div>
#             </div>
#             <div class="sta_tx_b clearfix">
#                 <div class="sta_tx_b1">
#                     <span>*</span>验证码：
#                 </div>
#                 <div class="sta_tx_b2">
#                     <input type="text" class="text220" name="code" id="messgecode" autocomplete="off"
#                            placeholder="请输入短信验证码" maxlength="6">
#                     <b>获取验证码</b>
#                     <strong>60s重新获取</strong>
#                 </div>
#             </div>
#
#
#             <div class="pclogintip"></div>
#             <div class="sub_tab">
#                 <div class="pcloginbtnbox">
#                     <a href="javascript:void(0)" class="huise">立即预约</a>
#                     <a href="javascript:void(0)" class="chengse" id="click_submit_order">立即预约</a>
#                 </div>
#
#             </div>
#         </div>
#     </form>
#     <div class="modal-body text-center gui9 telred">
#         收不到短信？
#         拨打
#         <a href="tel:400-666-2738">400-666-2738</a> 联系客服MM电话预约
#     </div>
#
#     <div class="succesbox_yezhu" style="display: none">
#         <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
#         <div class="wt_detail">
#             <div class="wt_explain">
#                 <div class="wt_img"></div>
#                 <h2 class="wt_title">提交委托成功！</h2>
#                 <h3 class="wt_sub_title">客服会在24小时内联系您，请不要拒接座机，
#                     保持电话畅通噢！</h3>
#             </div>
#             <div class="wt_dec_title">做省心房东，只需四步
#                 <div class="wt_line"></div>
#             </div>
#             <div class="wt_icons">
#                 <div class="wt_yxgt"></div>
#                 <div class="wt_arrow"></div>
#                 <div class="wt_skcl"></div>
#                 <div class="wt_arrow"></div>
#                 <div class="wt_hzqy"></div>
#                 <div class="wt_arrow"></div>
#                 <div class="wt_zxsy"></div>
#             </div>
#         </div>
#         <div class="wt_ewm">
#             <div class="wt_ewm_image"></div>
#             <div class="wt_sm">扫一扫</div>
#             <div class="wt_sm">下载<span>蛋壳公寓</span></div>
#         </div>
#     </div>
#
#
#     <div class="succesbox_detail" style="display: none">
#         <button type="button" class="close"
#                 data-dismiss="modal" aria-hidden="true">
#             &times;
#         </button>
#         <div class="wt_detail">
#             <div class="wt_explain">
#                 <div class="wt_img"></div>
#                 <h2 class="wt_title">  意向提交成功！</h2>
#                 <h3 class="wt_sub_title">客服会在24小时内联系您，请不要拒接座机，
#                     保持电话畅通噢！</h3>
#             </div>
#             <div class="wt_dec_title">让租房变得简单和快乐
#                 <div class="wt_line"></div>
#             </div>
#             <div class="wt_icons">
#                 <div class="detail_img_logo"></div>
#             </div>
#         </div>
#         <div class="wt_ewm">
#             <div class="wt_ewm_image"></div>
#             <div class="wt_sm">扫一扫</div>
#             <div class="wt_sm"><span>查看房源</span></div>
#         </div>
#     </div>
# </div>
#     <script src="//pangu-s1.danke.com.cn/build/bower/jquery/dist/jquery-2f6b11a7e9.min.js"></script>
#
# <style type="text/css">
#     .close {
#         position: relative;
#         z-index: 10;
#     }
#
#     .succesbox_yezhu {
#         width: 705px;
#         height: 340px;
#         margin-top: -20px;
#         margin-left: -15px;
#     }
#
#     .succesbox_detail {
#         width: 705px;
#         height: 340px;
#     }
#
#     .wt_img {
#         width: 98px;
#         height: 75px;
#         display: inline-block;
#         float: left;
#         background: url("//public.danke.com.cn/public-20180411-Fswx3jxRozhi72aI37XjAG10LdU5") no-repeat;
#     }
#
#     .wt_detail {
#         padding-top: 50px;
#         float: left;
#         padding-left: 50px;
#         width: 515px;
#         text-align: left;
#     }
#
#     .wt_title {
#         color: #3dbcc6;
#         font-size: 30px;
#         margin-left: 23px;
#         display: inline;
#     }
#
#     .wt_sub_title {
#         font-size: 14px;
#         color: #999999;
#         display: inline-block;
#         width: 300px;
#         margin-left: 23px;
#         font-weight: bold;
#         margin-top: 5px;
#         line-height: 20px;
#     }
#
#     .wt_dec_title {
#         margin-top: 50px;
#         color: #333333;
#         font-size: 14px;
#         font-weight: bold;
#     }
#
#     .wt_line {
#         width: 260px;
#         height: 2px;
#         display: inline-block;
#         background: #dbdbdb;
#         position: relative;
#         top: -5px;
#         margin-left: 15px;
#     }
#
#     .wt_icons {
#         margin-top: 35px;
#     }
#
#     .wt_icons div {
#         display: inline-block;
#         margin-right: 30px;
#     }
#
#     .wt_icons .wt_arrow {
#         margin-bottom: 20px;
#     }
#
#     .wt_yxgt {
#         width: 48px;
#         height: 55px;
#         background: url("//public.danke.com.cn/public-20180411-FoHSvtZR3Dge1l_n3UsyfCc4nGqD") no-repeat;
#     }
#
#     .wt_skcl {
#         width: 48px;
#         height: 55px;
#         background: url("//public.danke.com.cn/public-20180411-Fme6-JrLoEvpg9bActhx9A4hwf8T") no-repeat;
#     }
#
#     .wt_hzqy {
#         margin-bottom: 3px;
#         width: 48px;
#         height: 55px;
#         background: url("//public.danke.com.cn/public-20180411-FqfpklDBN2ipzm3D-nXeYmajtSig") no-repeat;
#     }
#
#     .wt_zxsy {
#         width: 48px;
#         height: 55px;
#         background: url("//public.danke.com.cn/public-20180411-FvOEKxzD2kj1nS8iyHooljd106qX") no-repeat;
#     }
#
#     .wt_arrow {
#         width: 9px;
#         height: 15px;
#         background: url("//public.danke.com.cn/public-20180411-FqYCHQht6hVEGMIZEkfKutxxsh-I") no-repeat;
#     }
#
#     .wt_ewm {
#         width: 190px;
#         height: 100%;
#         float: right;
#         text-align: center;
#         background: #f5f5f5;
#     }
#
#     .wt_ewm_image {
#         margin: 0 auto;
#         width: 126px;
#         height: 148px;
#         margin-top: 100px;
#         margin-bottom: 10px;
#         background: url("//public.danke.com.cn/public-20181113-Fh4RlH9xUt3rqvuHT2tXsOOZ1Q9I") no-repeat;
#         background-size: 100%;
#     }
#
#     .wt_sm {
#         font-size: 16px;
#         margin-top: 5px;
#         color: #999999;
#     }
#
#     .wt_sm span {
#         color: #3dbcc6;
#     }
#
#     .succesbox_detail .wt_ewm {
#         margin-top: -21px;
#         position: relative;
#         left: 5px;
#         border-radius: 0 5px 5px 0;
#     }
#
#     .detail_img_logo {
#         margin-left: 100px;
#         width: 227px;
#         height: 77px;
#         background: url("//public.danke.com.cn/public-20181126-FjoNUiiaAoiaJRj-pbSuy893SI9O") no-repeat center top;
#     }
#
#     input::-webkit-contacts-auto-fill-button {
#         visibility: hidden;
#         display: none !important;
#         pointer-events: none;
#         position: absolute;
#         right: 0;
#     }
#
#     /*有新房源通知我*/
#     .onlineroom {
#         width: 600px;
#     }
#
#     .modal-header {
#         padding: 15px;
#         border-bottom: 1px solid #e5e5e5;
#     }
#
#     .modal-header .close {
#         margin-top: -2px;
#     }
#
#     button.close {
#         -webkit-appearance: none;
#         padding: 0;
#         cursor: pointer;
#         background: 0 0;
#         border: 0;
#     }
#
#     .close {
#         float: right;
#         font-size: 21px;
#         font-weight: 700;
#         line-height: 1;
#         color: #000;
#         text-shadow: 0 1px 0 #fff;
#         filter: alpha(opacity=20);
#         opacity: .2;
#     }
#
#     .onlineroom .modal-body, .modal-body {
#         padding-top: 20px;
#         text-align: center;
#         font-size: 14px;
#     }
#
#     .sta_tx_b {
#         padding: 10px 0;
#         overflow: hidden;
#     }
#
#     .sta_tx_b1 {
#         float: left;
#         width: 150px;
#         height: 50px;
#         color: #666666;
#         text-align: right;
#         /* font-weight: bold; */
#         font-size: 16px;
#         line-height: 50px;
#     }
#
#     .sta_tx_b1 span {
#         padding-right: 4px;
#         color: #ff643a;
#     }
#
#     .text350 {
#         float: left;
#         width: 348px;
#         height: 50px;
#         line-height: 50px;
#         border: 1px solid #c4c4c4;
#         border-radius: 3px;
#         color: #333;
#         text-indent: 10px;
#         font-size: 16px;
#     }
#
#     .text220 {
#         float: left;
#         width: 178px;
#         height: 48px;
#         border: 1px solid #c4c4c4;
#         border-radius: 2px;
#         color: #333;
#         text-indent: 10px;
#         font-size: 14px;
#         line-height: 48px;
#     }
#
#     .sta_tx_b2 {
#         float: left;
#         width: 350px;
#     }
#
#     .sta_tx_b2 img {
#         float: left;
#         width: 102px;
#         height: 48px;
#         cursor: pointer;
#     }
#
#     .sta_tx_b2 a {
#         line-height: 48px;
#         float: left;
#         margin-left: 5px;
#         color: #337ab7;
#         width: 58px;
#         text-align: center;
#     }
#
#     .sta_tx_b2 b, .sta_tx_b2 strong {
#         float: right;
#         width: 165px;
#         height: 48px;
#
#         color: #fff;
#         text-align: center;
#         font-size: 16px;
#         line-height: 53px;
#         cursor: pointer;
#     }
#
#     .sta_tx_b2 textarea {
#         width: 348px;
#         border: 1px solid #e6e6e6;
#         border-radius: 2px;
#         resize: none;
#         height: 100px;
#         font-size: 16px;
#         padding: 10px;
#         margin-top: 10px;
#     }
#
#     .sta_tx_b2 b {
#         display: block;
#         background: #4BB4BB;
#     }
#
#     .sta_tx_b2 strong {
#         display: none;
#         background: #dddddd;
#     }
#
#     .pclogintip {
#         display: block;
#         height: 35px;
#         color: #f00;
#         text-align: center;
#         font-size: 14px;
#         line-height: 25px;
#     }
#
#     .sub_tab {
#         overflow: hidden;
#         width: 100%;
#     }
#
#     .pcloginbtnbox {
#         display: block;
#         overflow: hidden;
#         width: 348px;
#         margin: 0 auto;
#     }
#
#     .pcloginbtnbox a {
#         height: 45px;
#         -webkit-border-radius: 6px;
#         -moz-border-radius: 6px;
#         border-radius: 6px;
#         color: #fff;
#         text-align: center;
#         font-size: 18px;
#         line-height: 45px;
#     }
#
#     .huise {
#         display: block;
#         background: #ddd;
#     }
#
#     .chengse {
#         display: none;
#         background: #4BB4BB;
#     }
#
#     .telred a {
#         color: #FF3300;
#         font-weight: bold;
#     }
#
#     /*有新房源通知我 end*/
#     /*预约优化*/
#     </style>
# <script>
#     $(function () {
#                 //手机号
#                 var newMobile = /^1[3-9]\d{9}$/;
#                 var roomType = $('#type').val();
#                 var cityCode = $('#citycode').val();
#                 var data = {};
#                 var tipText = $('.pclogintip');
#
#                 var flag = 0; // 获取验证码次数标识
#                 var errorFlag = 0 //获取失败标识
#                 var mobilFlag = false // 获取频繁标记
#                 var preMobile = ''; // 上一次手机号
#
#                 //详情页预约
#                                 // 初始化图形验证码（隐藏）
#                                     $('.sta_tx_b:nth-child(5)').hide();
#                                 $.ajaxSetup({
#     headers: {
#         'X-CSRF-TOKEN': 'KiXUcaP7ZnsekTKv11DFkSEe3dMiunS48lkBbC16'
#     },
#     cache: false,
#     async: false,
# });                // 登录回显手机号
#                 $.ajax({
#                     type: 'GET',
#                     url: '/web-api/user/info',
#                     async: false,
#                     error: function (msg) {
#                         console.log(msg)
#                     },
#                     success: function (data) {
#                         $('#mobile').val(data.data.mobile)
#                     }
#                 });
#
#                 //手机号是否发生改变
#                 $('#mobile').keyup(function () {
#                     if (preMobile && preMobile == $(this).val() && errorFlag != 1) {
#                         flag = 2
#                                                     $('.sta_tx_b:nth-child(5)').hide();
#                                             } else if (preMobile && preMobile != $(this).val() && errorFlag != 1) {
#                         flag = 0
#                                                     $('.sta_tx_b:nth-child(5)').hide();
#                                             }
#                 })
#
#                 if (roomType == 'index') {
#                     $('.telred').html('收不到短信？ 拨打 <a href="tel:400-062-8688">400-062-8688</a> 联系客服MM电话委托');
#                     $('.pcloginbtnbox a').text('立即委托')
#                 }
#                 //提交委托
#                 $('.pcloginbtnbox a.huise').click(function () {
#                     tipText.text('请完善您的资料!');
#                 });
#                 $('.sta_tx_b input').keyup(function () {
#                     tipText.text('');
#                     var name = $('#name').val();
#                     var mobile = $('#mobile').val();
#                     var messgeCode = $('#messgecode').val();
#                     var picCode = $('#piccode').val();
#                     if (flag >= 2) {
#                         if (name !== '' && mobile !== '' && messgeCode !== '' && picCode !== '') {
#                             switch (roomType) {
#                                 case "index" :
#                                     var city = $('#city').val();
#                                     var areaName = $('#areaname').val();
#                                     if (city != '' && areaName != '') {
#                                         btnShow();
#                                     } else {
#                                         btnHide();
#                                     }
#                                     break;
#                                 case "detail":
#                                     var note = $('#note').val();
#                                     if (note != '') {
#                                         btnShow();
#                                     } else {
#                                         btnHide();
#                                     }
#                                     break;
#                                 case "list":
#                                     btnShow();
#                                     break;
#                             }
#                         } else {
#                             btnHide();
#                         }
#                     } else {
#                         if (name !== '' && mobile !== '' && messgeCode !== '') {
#                             switch (roomType) {
#                                 case "index" :
#                                     var city = $('#city').val();
#                                     var areaName = $('#areaname').val();
#                                     if (city != '' && areaName != '') {
#                                         btnShow();
#                                     } else {
#                                         btnHide();
#                                     }
#                                     break;
#                                 case "detail":
#                                     var note = $('#note').val();
#                                     if (note != '') {
#                                         btnShow();
#                                     } else {
#                                         btnHide();
#                                     }
#                                     break;
#                                 case "list":
#                                     btnShow();
#                                     break;
#                             }
#                         } else {
#                             btnHide();
#                         }
#                     }
#
#                 });
#                 //获取验证码
#                 $('.sta_tx_b2 b').click(function () {
#                     var codeFlag = false
#                     var timer = 60;
#                     var mobile = $('#mobile').val();
#                     preMobile = mobile;
#                     var piccode = $('#piccode').val();
#                     if (!newMobile.test(mobile)) {
#                         tipText.text('请输入正确的手机号码！');
#                         return false;
#                     } else {
#                         flag++
#                     }
#                     if (flag >= 2) {
#                                                     $('.sta_tx_b:nth-child(5)').show();
#                                                 if (flag == 2 && !mobilFlag) $('.sta_tx_b2 a').click();
#                         if (piccode == '') {
#                             tipText.text('请输入图片验证码！');
#                             return false;
#                         } else {
#                             $.ajax({
#                                 type: 'POST',
#                                 url: "https://www.danke.com/collect/img-code",
#                                 data: {'mobile': mobile, 'verify_code': piccode},
#                                 async: false,
#                                 error: function (msg) {
#                                     alert("提交失败，请退出重试。");
#                                     if (roomType == 'index') {
#                                         saMethod.GetVerifyingCode('立即委托', '立即委托', false)
#                                     } else if (roomType == 'detail') {
#                                         saMethod.GetVerifyingCode('预约看房', '预约看房', false)
#                                     }
#                                     return
#                                 },
#                                 success: function (data) {
#                                     if (data.msg == '验证码不正确') {
#                                         $('.sta_tx_b2 a').click();
#                                         $('#piccode').val('')
#                                         codeFlag = true
#                                         tipText.text('图片验证码不正确!');
#                                     }
#                                     if (roomType == 'index') {
#                                         saMethod.GetVerifyingCode('立即委托', '立即委托', true)
#                                     } else if (roomType == 'detail') {
#                                         saMethod.GetVerifyingCode('预约看房', '预约看房', true)
#                                     }
#                                 }
#                             });
#                         }
#                     }
#                     //widget include
#
#                     if (codeFlag) return
#
#                     $.ajax({
#                         type: 'POST',
#                         url: "https://www.danke.com/collect/send-text-verify-code",
#                         data: {'mobile': mobile},
#                         async: false,
#                         error: function (msg) {
#                             flag--;
#                             errorFlag = 1;
#                             console.log(msg)
#                             if (roomType == 'index') {
#                                 saMethod.GetVerifyingCode('委托页', '立即委托', false)
#                             } else if (roomType == 'detail') {
#                                 saMethod.GetVerifyingCode('预约看房页', '预约看房', false)
#                             }
#                         },
#                         success: function (data) {
#                             if (data.msg == '验证码发送频繁') {
#                                                                     $('.sta_tx_b:nth-child(5)').show();
#                                                                         $('.sta_tx_b2 a').click();
#                                 mobilFlag = true;
#                                 tipText.text('请输入图片验证码!');
#                                 return
#                             }
#                             if (!data['success']) {
#                                 $('.sta_tx_b2 a').click();
#                                 return
#                             }
#
#                             if (roomType == 'index') {
#                                 saMethod.GetVerifyingCode('立即委托页', '立即委托', true)
#                             } else if (roomType == 'detail') {
#                                 saMethod.GetVerifyingCode('预约看房页', '预约看房', true)
#                             }
#
#                             $('.sta_tx_b2 b').hide();
#                             $('.sta_tx_b2 strong').css('display', 'block').text(timer + 's重新获取');
#                             //获取接口
#                             var tim = setInterval(function () {
#                                 timer--;
#                                 $('.sta_tx_b2 strong').text(timer + 's重新获取');
#                                 if (timer == 0) {
#                                     clearInterval(tim);
#                                     $('.sta_tx_b2 strong').hide();
#                                     $('.sta_tx_b2 b').css('display', 'block').text('重新获取');
#                                 }
#                             }, 1000)
#                         },
#                     });
#
#                 });
#
#                 //提交
#                 $('.pcloginbtnbox a.chengse').click(function () {
#                     var name = $('#name').val();
#                     var mobile = $('#mobile').val();
#                     var smsCode = $('#messgecode').val();
#                     if (!newMobile.test(mobile)) {
#                         tipText.text('请输入正确的手机号码！');
#                         return false;
#                     }
#                     tipText.text('');
#                     switch (roomType) {
#                         case "index" :
#                             var areaName = $('#areaname').val();
#                             data = {name: name, mobile: mobile, sms_code: smsCode, type: 'index', areaname: areaName};
#                             break;
#                         case "detail":
#                             var roomId = $('#room_id').val();
#                             data = {mobile: mobile, sms_code: smsCode, type: 'detail', room_id: roomId};
#                             break;
#                         case "list":
#                             var note = $('#note').val();
#                             var source = '官网';
#                             data = {
#                                 name: name,
#                                 mobile: mobile,
#                                 sms_code: smsCode,
#                                 type: 'detail',
#                                 note: note,
#                                 source: source
#                             };
#                             break;
#                     }
#                     $.ajax({
#                         type: "POST",
#                         url: "https://www.danke.com/collect/ajax-info/hz",
#                         data: data,
#                         async: false,
#                         error: function (msg) {
#                             alert("输入错误，请重新输入");
#                             if (roomType == 'index') {
#                                 saMethod.EntrustRoomButton($('#name').val(), $('#mobile').val(), $('#areaname').val(), false)
#                             } else if (roomType == 'detail') {
#                                 saMethod.RoomreservationButton('找房频道', '房源详情页', '', '', $('#room_id').val(), '', $('#name').val(), $('#mobile').val(), false)
#                             }
#                         },
#                         success: function (data) {
#                             // 判断是否提交成功
#                             if (!data.success) {
#                                 $('.sta_tx_b2 a').click();
#                                 $('#piccode').val('');
#                                 $('.pclogintip').text(data['msg']);
#                                 return false;
#                             } else {
#
#                                 if (document.URL.indexOf('yezhu') !== -1) {
#                                     // 委托框隐藏
#                                     $("#myroom").fadeOut(200);
#
#                                     // 成功提示框显示
#                                     $(".success-layer-wrap").show();
#                                     setTimeout(function () {
#                                         $(".success-inner").css({
#                                             transform: "translate(0,0)"
#                                         });
#                                         setTimeout(function () {
#                                             $(".success-inner")[0].style.opacity = 1;
#                                         }, 300);
#                                     }, 50)
#
#                                     // 神策
#                                     saMethod.EntrustRoomButton($('#name').val(), $('#mobile').val(), $('#areaname').val(), true)
#                                 } else {
#                                     $('#myroom .onlineroom').css({'width': '705px'});
#                                     $('.modal-body').css({'width': '705px', 'height': '340px'});
#                                     $('.form-horizontal,.gui9.telred').hide();
#                                     $('.succesbox_detail').show();
#                                     $('.modal-header').hide();
#
#                                     // 神策
#                                     saMethod.RoomreservationButton('找房频道', '房源详情页', '', '', $('#room_id').val(), '', $('#name').val(), $('#mobile').val(), true)
#                                 }
#
#                             }
#                         }
#                     });
#                 });
#
#                 //换验证图片
#                 $('.sta_tx_b2 a,.sta_tx_b2 img').click(function () {
#                     var timestamp = new Date().getTime();
#                     $('.sta_tx_b2 img').attr('src', '/get-img-code/90/30' + "?mobile=" + $('#mobile').val() + "&time=" + new Date().getTime());
#                 });
#                 $('.text350').click(function () {
#                     if (roomType === 'index') {
#                         saMethod.ClickPhoneInput('立即委托')
#                     } else if (roomType === 'detail') {
#                         saMethod.ClickPhoneInput('立即预约')
#                     }
#
#                 })
#
#             }
#     );
#     function btnShow() {
#         $('.pcloginbtnbox a.huise').hide();
#         $('.pcloginbtnbox a.chengse').css('display', 'block');
#     }
#     function btnHide() {
#         $('.pcloginbtnbox a.chengse').hide();
#         $('.pcloginbtnbox a.huise').css('display', 'block');
#     }
# </script>
#             </div><!-- /.modal-content -->
#         </div><!-- /.modal -->
#     </div>
#     <script src="//pangu-s2.danke.com.cn/build/js/pc_home/jquery-9642b4bbfe.bootstrap-dropdown-hover.min.js"></script>
#
#     <script src="//pangu-s1.danke.com.cn/build/js/pc_home/list-ce43389f38.js"></script>
#
# <div class="layout-collection-website">
#     <a href="javascript:void(0)" class="layout-collection-website-close"></a>
#     <div class="layout-collection-show">
#         <span>友情提示</span>
#         <p>亲爱的蛋宝宝们，由于我们修改了网站域名（新域名：www.danke.com）<br/>为了您更快速的访问，请收藏此网站～</p>
#         <div class="layout-collection-website-btn">
#             <label class="layout-collection-not">暂不收藏</label>
#             <label class="layout-collection-yes">一键收藏</label>
#         </div>
#     </div>
#     <div class="layout-collection-hide">
#         <span>收藏成功</span>
#     </div>
# </div>
# </body>
# </html>
#
# """

html_str = """
    <body>
        <div class="asd">
            <li id="bn"><div>gdfgd</div></li>
            <li class="a"> <a href="javascript:history.back(-1);"><span>回到上一页</span></a></li>
            <li class="b"><div id="kk">asd</div></li>
            <li class="c"><a href="https://blog.csdn.net/kylinxjd/article/details/95978485">爬取百度贴吧</a></li>
            <li class="d"><div>fgh</div></li>
        </div>
    </body>
"""

url = 'https://www.danke.com/room/hz?page=1'

head = {
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

# html = requests.get(url=url, headers=head).text

soup = BeautifulSoup(html_str, 'html.parser')
# print(soup.prettify())
# obj = soup.select('.r_lbx')
# obj = soup.select('div #zjhPhoneNumber')
# obj = soup.select('div[id=topbar] a')
# for item in obj:
#     print(item.attrs['href'])
#     print(item.get_text())
# print("kkkkkkkkkkkkkkkkkk")
# print(type(obj))
# print(len(obj))

obj1 = soup.select('.a')
obj2 = soup.select('#bn')
obj3 = soup.select('.asd a')
obj4 = soup.select('a')
print(obj1)
print(obj2)
print(obj3)
print(obj4)
for i in obj4:
    print(i.attrs['href'])
    print(i.get_text())
