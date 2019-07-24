# -*- coding:utf-8 -*-
import re

import requests

# res = requests.get('https://movie.douban.com/top250?start=0')
#
# print(res.text)
from lxml import etree

html = """
<script type="text/javascript">
if (typeof param != 'undefined'){
param.currentPage = "0";
param.pageNumbers = "19";
param.numFound = "2165";
param.preciseFound="2165";
if("{pageType}"=="{pageType}"){
snSearch.productUtil.makeProductName($("#product-list,#bottom_pager"));
}
param.mutil = true;
param.isSort = true;
param.preciseKG=true;
param.showAdProduct="0";
}
</script>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-10985347748    mobileProduct   " id="0070094634-10985347748" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||10985347748||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="31">
<a target="_blank" title="麒麟710，6.21英寸珍珠屏，2400万广角三摄大存储大电池" href="//product.suning.com/0070094634/10985347748.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10985347748','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic31-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic31-1_0_0_10985347748_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_31:0070094634_10985347748">
<img alt="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待" src="//imgservice2.suning.cn/uimg1/b2c/atmosphere/JkoiMX87alhsokZc4hgMIA.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10985347748subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985347748" name="10985347748" version="?ver=2013" color="" isDynamic="true" vendorId= "0070094634"   colorValue="幻夜黑"  alt="幻夜黑" title="幻夜黑" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/xB89vZYMlMVYaBKcQ-C2eA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985347748" name="10985347786" version="?ver=2011" color="" isDynamic="true" vendorId= "0070094634"   colorValue="极光蓝"  alt="极光蓝" title="极光蓝" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/s-1900ucit7rFQOpDkHUWQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985347748" name="10985624242" version="?ver=2010" color="" isDynamic="true" vendorId= "0070094634"   colorValue="珊瑚红"  alt="珊瑚红" title="珊瑚红" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/DnVtp8smsayoWnH0vKX0aA.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10985347748|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10985347748','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic31-1_jz','cateid':'20006'}" name="{pageType}_pro_name31-1_0_0_10985347748_0070094634" title="麒麟710，6.21英寸珍珠屏，2400万广角三摄大存储大电池"target="_blank" href="//product.suning.com/0070094634/10985347748.html">华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待
<em  style="display:none" >麒麟710，6.21英寸珍珠屏，2400万广角三摄大存储大电池</em>
</a>
</div>
<div class="info-config" title=" 128GB |4GB |6.21英寸">
<em> 128GB <i>|</i>4GB <i>|</i>6.21英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10985347748','shopid':'0070094634','searchvalue':'ssdln_pic31-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen31-1_0_0_10985347748_0070094634" href="//product.suning.com/0070094634/10985347748.html#pro_detail_tab"><i>200+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=10985347748'   sa-data="{'eletp':'shop','prdid':'10985347748','shopid':'70094634','searchvalue':'ssdln_pic31-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10985347748','shopid':'0070094634','searchvalue':'ssdln_pic31-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-10985347748" name="{pageType}_pro_compare31-1_0_0_10985347748_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10985347748','shopid':'0070094634','searchvalue':'ssdln_pic31-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-10985347748','000000010985347748',this);" name="{pageType}_pro_collect31-1_0_0_10985347748_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010985347748',10985347748,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'10985347748','shopid':'0070094634','searchvalue':'ssdln_pic31-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy31-1_0_0_10985347748_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-10989586988    mobileProduct   " id="0070094634-10989586988" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||10989586988||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="32">
<a target="_blank" title="麒麟980智慧芯片，6.1英寸OLED全面屏，超感光徕卡三摄，30倍数字变焦。" href="//product.suning.com/0070094634/10989586988.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10989586988','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic32-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic32-1_0_0_10989586988_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_32:0070094634_10989586988">
<img alt="华为(HUAWEI) 华为P30 麒麟980 超感光徕卡三摄 全网通版 8GB+128GB 天空之境 移动联通电信4G手机 双卡双待" src="//imgservice3.suning.cn/uimg1/b2c/atmosphere/8JnHsMBdiN6UpwLq8UN-ZQ.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10989586988subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10989586988" name="10989586988" version="?ver=2009" color="" isDynamic="true" vendorId= "0070094634"   colorValue="天空之境"  alt="天空之境" title="天空之境" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/f_fHvgISMLmmtA-SqBQHuA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10989586988" name="10989570890" version="?ver=2007" color="" isDynamic="true" vendorId= "0070094634"   colorValue="亮黑色"  alt="亮黑色" title="亮黑色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/h8fqJV63ntM4pvAvBYEW-Q.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10989586988" name="10989586992" version="?ver=2002" color="" isDynamic="true" vendorId= "0070094634"   colorValue="极光色"  alt="极光色" title="极光色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/skEMj85yADQTiyRCv7fFNw.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10989586988" name="10989587000" version="?ver=2001" color="" isDynamic="true" vendorId= "0070094634"   colorValue="赤茶橘"  alt="赤茶橘" title="赤茶橘" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/5PiUR25NnhtexYB-1MoTfg.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10989586988" name="10989586998" version="?ver=2001" color="" isDynamic="true" vendorId= "0070094634"   colorValue="珠光贝母"  alt="珠光贝母" title="珠光贝母" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/ATmEcXP3ogoBkvn701-zbQ.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10989586988|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10989586988','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic32-1_jz','cateid':'20006'}" name="{pageType}_pro_name32-1_0_0_10989586988_0070094634" title="麒麟980智慧芯片，6.1英寸OLED全面屏，超感光徕卡三摄，30倍数字变焦。"target="_blank" href="//product.suning.com/0070094634/10989586988.html">华为(HUAWEI) 华为P30 麒麟980 超感光徕卡三摄 全网通版 8GB+128GB 天空之境 移动联通电信4G手机 双卡双待
<em  style="display:none" >麒麟980智慧芯片，6.1英寸OLED全面屏，超感光徕卡三摄，30倍数字变焦。</em>
</a>
</div>
<div class="info-config" title=" 128GB |8GB |6.1英寸">
<em> 128GB <i>|</i>8GB <i>|</i>6.1英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10989586988','shopid':'0070094634','searchvalue':'ssdln_pic32-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen32-1_0_0_10989586988_0070094634" href="//product.suning.com/0070094634/10989586988.html#pro_detail_tab"><i>70+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=10989586988'   sa-data="{'eletp':'shop','prdid':'10989586988','shopid':'70094634','searchvalue':'ssdln_pic32-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10989586988','shopid':'0070094634','searchvalue':'ssdln_pic32-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-10989586988" name="{pageType}_pro_compare32-1_0_0_10989586988_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10989586988','shopid':'0070094634','searchvalue':'ssdln_pic32-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-10989586988','000000010989586988',this);" name="{pageType}_pro_collect32-1_0_0_10989586988_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010989586988',10989586988,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'10989586988','shopid':'0070094634','searchvalue':'ssdln_pic32-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy32-1_0_0_10989586988_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-10985358058    mobileProduct   " id="0070094634-10985358058" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||10985358058||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="33">
<a target="_blank" title="高清珍珠屏，大存储大音量，出彩夜拍。" href="//product.suning.com/0070094634/10985358058.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10985358058','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic33-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic33-1_0_0_10985358058_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_33:0070094634_10985358058">
<img alt="华为(HUAWEI)华为畅享9e 全网通版 3GB+64GB 幻夜黑 移动联通电信4G手机 双卡双待" src="//imgservice2.suning.cn/uimg1/b2c/atmosphere/ysq5P-erK9yRfp3Qp_COKA.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10985358058subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985358058" name="10985358058" version="?ver=2009" color="" isDynamic="true" vendorId= "0070094634"   colorValue="幻夜黑"  alt="幻夜黑" title="幻夜黑" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/Hc6pczfBJlvHRh7huKQ60g.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985358058" name="10985358036" version="?ver=2008" color="" isDynamic="true" vendorId= "0070094634"   colorValue="宝石蓝"  alt="宝石蓝" title="宝石蓝" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/2suatvfeTyR-2Uq4P46yNA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985358058" name="10985347510" version="?ver=2008" color="" isDynamic="true" vendorId= "0070094634"   colorValue="琥珀棕"  alt="琥珀棕" title="琥珀棕" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/yOUidp68Nj9JnwQlUhzAmA.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10985358058|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10985358058','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic33-1_jz','cateid':'20006'}" name="{pageType}_pro_name33-1_0_0_10985358058_0070094634" title="高清珍珠屏，大存储大音量，出彩夜拍。"target="_blank" href="//product.suning.com/0070094634/10985358058.html">华为(HUAWEI)华为畅享9e 全网通版 3GB+64GB 幻夜黑 移动联通电信4G手机 双卡双待
<em  style="display:none" >高清珍珠屏，大存储大音量，出彩夜拍。</em>
</a>
</div>
<div class="info-config" title=" 64GB |3GB |6.088英寸">
<em> 64GB <i>|</i>3GB <i>|</i>6.088英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10985358058','shopid':'0070094634','searchvalue':'ssdln_pic33-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen33-1_0_0_10985358058_0070094634" href="//product.suning.com/0070094634/10985358058.html#pro_detail_tab"><i>100+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=10985358058'   sa-data="{'eletp':'shop','prdid':'10985358058','shopid':'70094634','searchvalue':'ssdln_pic33-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10985358058','shopid':'0070094634','searchvalue':'ssdln_pic33-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-10985358058" name="{pageType}_pro_compare33-1_0_0_10985358058_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10985358058','shopid':'0070094634','searchvalue':'ssdln_pic33-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-10985358058','000000010985358058',this);" name="{pageType}_pro_collect33-1_0_0_10985358058_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010985358058',10985358058,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'10985358058','shopid':'0070094634','searchvalue':'ssdln_pic33-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy33-1_0_0_10985358058_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-10657749544    mobileProduct   " id="0070094634-10657749544" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||10657749544||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="34">
<a target="_blank" title="麒麟980智能芯片，大广角徕卡三摄，高屏占比，长续航" href="//product.suning.com/0070094634/10657749544.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10657749544','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic34-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic34-1_0_0_10657749544_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_34:0070094634_10657749544">
<img alt="华为(HUAWEI) 华为mate20 全网通版 6GB+64GB 亮黑色 移动联通电信4G手机 麒麟980 全面屏 徕卡三摄 华为手机 Mate20" src="//imgservice3.suning.cn/uimg1/b2c/atmosphere/_XGjsxUU6sO7JGLvL7miSw.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10657749544subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10657749544" name="10657749544" version="?ver=2054" color="" isDynamic="true" vendorId= "0070094634"   colorValue="亮黑色"  alt="亮黑色" title="亮黑色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/pUT6YDN393Zx7c7p77BL4g.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10657749544" name="10657661006" version="?ver=2014" color="" isDynamic="true" vendorId= "0070094634"   colorValue="宝石蓝"  alt="宝石蓝" title="宝石蓝" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/1kqhdNm20SPq_DCuU5uyTA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10657749544" name="10657749609" version="?ver=2012" color="" isDynamic="true" vendorId= "0070094634"   colorValue="极光色"  alt="极光色" title="极光色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/Fi1sNb3IqcUYJvfUgTPLgQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10657749544" name="10657738132" version="?ver=2012" color="" isDynamic="true" vendorId= "0070094634"   colorValue="翡冷翠"  alt="翡冷翠" title="翡冷翠" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/zl1ImU-4RyhopqIVxTak1g.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10657749544|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10657749544','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic34-1_jz','cateid':'20006'}" name="{pageType}_pro_name34-1_0_0_10657749544_0070094634" title="麒麟980智能芯片，大广角徕卡三摄，高屏占比，长续航"target="_blank" href="//product.suning.com/0070094634/10657749544.html">华为(HUAWEI) 华为mate20 全网通版 6GB+64GB 亮黑色 移动联通电信4G手机 麒麟980 全面屏 徕卡三摄 华为手机 Mate20
<em  style="display:none" >麒麟980智能芯片，大广角徕卡三摄，高屏占比，长续航</em>
</a>
</div>
<div class="info-config" title=" 64GB |6GB |6.53英寸">
<em> 64GB <i>|</i>6GB <i>|</i>6.53英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10657749544','shopid':'0070094634','searchvalue':'ssdln_pic34-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen34-1_0_0_10657749544_0070094634" href="//product.suning.com/0070094634/10657749544.html#pro_detail_tab"><i>300+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=10657749544'   sa-data="{'eletp':'shop','prdid':'10657749544','shopid':'70094634','searchvalue':'ssdln_pic34-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10657749544','shopid':'0070094634','searchvalue':'ssdln_pic34-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-10657749544" name="{pageType}_pro_compare34-1_0_0_10657749544_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10657749544','shopid':'0070094634','searchvalue':'ssdln_pic34-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-10657749544','000000010657749544',this);" name="{pageType}_pro_collect34-1_0_0_10657749544_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010657749544',10657749544,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'10657749544','shopid':'0070094634','searchvalue':'ssdln_pic34-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy34-1_0_0_10657749544_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-10617829377    mobileProduct   " id="0070094634-10617829377" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||10617829377||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="35">
<a target="_blank" title="AI智慧美颜，麒麟710芯片，游戏更酣畅，AI前后双摄 让美更精细。" href="//product.suning.com/0070094634/10617829377.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10617829377','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic35-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic35-1_0_0_10617829377_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_35:0070094634_10617829377">
<img alt="华为(HUAWEI)华为nova3i 全面屏AI智慧四摄游戏手机 全网通 6GB+128GB 亮黑色 移动联通电信4G手机 双卡双待 华为nova 3i" src="//imgservice3.suning.cn/uimg1/b2c/atmosphere/230eTWI5ggAuWvfrCdHwcw.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10617829377subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10617829377" name="10617829377" version="?ver=2043" color="" isDynamic="true" vendorId= "0070094634"   colorValue="亮黑色"  alt="亮黑色" title="亮黑色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/-ZKxRXcY2his6I2lLzqw9w.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10617829377" name="10617829375" version="?ver=2004" color="" isDynamic="true" vendorId= "0070094634"   colorValue="蓝楹紫"  alt="蓝楹紫" title="蓝楹紫" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/G0tRrIhIxpVNimuRT8sjXg.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10617829377|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10617829377','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic35-1_jz','cateid':'20006'}" name="{pageType}_pro_name35-1_0_0_10617829377_0070094634" title="AI智慧美颜，麒麟710芯片，游戏更酣畅，AI前后双摄 让美更精细。"target="_blank" href="//product.suning.com/0070094634/10617829377.html">华为(HUAWEI)华为nova3i 全面屏AI智慧四摄游戏手机 全网通 6GB+128GB 亮黑色 移动联通电信4G手机 双卡双待 华为nova 3i
<em  style="display:none" >AI智慧美颜，麒麟710芯片，游戏更酣畅，AI前后双摄 让美更精细。</em>
</a>
</div>
<div class="info-config" title=" 128GB |6GB |6.3英寸">
<em> 128GB <i>|</i>6GB <i>|</i>6.3英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10617829377','shopid':'0070094634','searchvalue':'ssdln_pic35-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen35-1_0_0_10617829377_0070094634" href="//product.suning.com/0070094634/10617829377.html#pro_detail_tab"><i>500+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=10617829377'   sa-data="{'eletp':'shop','prdid':'10617829377','shopid':'70094634','searchvalue':'ssdln_pic35-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10617829377','shopid':'0070094634','searchvalue':'ssdln_pic35-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-10617829377" name="{pageType}_pro_compare35-1_0_0_10617829377_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10617829377','shopid':'0070094634','searchvalue':'ssdln_pic35-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-10617829377','000000010617829377',this);" name="{pageType}_pro_collect35-1_0_0_10617829377_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010617829377',10617829377,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'10617829377','shopid':'0070094634','searchvalue':'ssdln_pic35-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy35-1_0_0_10617829377_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-10519063911    mobileProduct   " id="0070094634-10519063911" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||10519063911||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="36">
<a target="_blank" title="麒麟970智慧芯片，安全快充，AI摄影，4D预测追焦，新一代莱卡双镜头" href="//product.suning.com/0070094634/10519063911.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10519063911','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic36-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic36-1_0_0_10519063911_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_36:0070094634_10519063911">
<img alt="华为(HUAWEI) 华为P20 AI智慧全面屏 全网通版 6GB+64GB 极光色 移动联通电信4G手机 双卡双待" src="//imgservice3.suning.cn/uimg1/b2c/atmosphere/3Q2wZsvG2jT25xDzo5b_xw.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10519063911subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10519063911" name="10519063911" version="?ver=2032" color="" isDynamic="true" vendorId= "0070094634"   colorValue="极光色"  alt="极光色" title="极光色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/Lz5rK5g2pDwbmKmMq_-8iQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10519063911" name="10457794097" version="?ver=2008" color="" isDynamic="true" vendorId= "0070094634"   colorValue="亮黑色"  alt="亮黑色" title="亮黑色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/8YyM5k__S5NH4Ha_9onTXw.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10519063911|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10519063911','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic36-1_jz','cateid':'20006'}" name="{pageType}_pro_name36-1_0_0_10519063911_0070094634" title="麒麟970智慧芯片，安全快充，AI摄影，4D预测追焦，新一代莱卡双镜头"target="_blank" href="//product.suning.com/0070094634/10519063911.html">华为(HUAWEI) 华为P20 AI智慧全面屏 全网通版 6GB+64GB 极光色 移动联通电信4G手机 双卡双待
<em  style="display:none" >麒麟970智慧芯片，安全快充，AI摄影，4D预测追焦，新一代莱卡双镜头</em>
</a>
</div>
<div class="info-config" title=" 64GB |6GB |5.8英寸">
<em> 64GB <i>|</i>6GB <i>|</i>5.8英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10519063911','shopid':'0070094634','searchvalue':'ssdln_pic36-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen36-1_0_0_10519063911_0070094634" href="//product.suning.com/0070094634/10519063911.html#pro_detail_tab"><i>100+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=10519063911'   sa-data="{'eletp':'shop','prdid':'10519063911','shopid':'70094634','searchvalue':'ssdln_pic36-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10519063911','shopid':'0070094634','searchvalue':'ssdln_pic36-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-10519063911" name="{pageType}_pro_compare36-1_0_0_10519063911_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10519063911','shopid':'0070094634','searchvalue':'ssdln_pic36-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-10519063911','000000010519063911',this);" name="{pageType}_pro_collect36-1_0_0_10519063911_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010519063911',10519063911,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'10519063911','shopid':'0070094634','searchvalue':'ssdln_pic36-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy36-1_0_0_10519063911_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0000000000-10949059015    mobileProduct   " id="0000000000-10949059015" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="0" goodsType="Z001"  vendor="0000000000" searchType="14"   class="hidenInfo" dataPro="||10949059015||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="37">
<a target="_blank" title="6.21英寸珍珠屏！超广角AI三摄！拍照如此简单！" href="//product.suning.com/0000000000/10949059015.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10949059015','shopid':'0000000000','salestatus':'1','searchvalue':'ssdln_pic37-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic37-1_0_0_10949059015_0000000000"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_37:0000000000_10949059015">
<img alt="华为/HUAWEI 畅享9S 超广角AI三摄 4GB+64GB 幻夜黑移动联通电信4G全面屏全网通手机" src="//imgservice5.suning.cn/uimg1/b2c/image/feWw-GppfFl03xcgaYXQwA.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10949059015subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10949059015" name="10949059015" version="?ver=2011" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/feWw-GppfFl03xcgaYXQwA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10949059015" name="10949058804" version="?ver=2011" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/FQCrmkEoXu5YIvZ1Ew6HyQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10949059015" name="10949058715" version="?ver=2011" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/7yfPC2OPOmvTbtrsUOENlw.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10949059015|||||0000000000" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10949059015','shopid':'0000000000','salestatus':'{invStatus}','searchvalue':'ssdln_pic37-1_jz','cateid':'20006'}" name="{pageType}_pro_name37-1_0_0_10949059015_0000000000" title="6.21英寸珍珠屏！超广角AI三摄！拍照如此简单！"target="_blank" href="//product.suning.com/0000000000/10949059015.html">华为/HUAWEI 畅享9S 超广角AI三摄 4GB+64GB 幻夜黑移动联通电信4G全面屏全网通手机
<em  style="display:none" >6.21英寸珍珠屏！超广角AI三摄！拍照如此简单！</em>
</a>
</div>
<div class="info-config" title=" 64GB |4GB |6.21英寸">
<em> 64GB <i>|</i>4GB <i>|</i>6.21英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10949059015','shopid':'0000000000','searchvalue':'ssdln_pic37-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen37-1_0_0_10949059015_0000000000" href="//product.suning.com/0000000000/10949059015.html#pro_detail_tab"><i>900+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a href="javascript:void(0);" class="store-class zy">苏宁自营</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10949059015','shopid':'0000000000','searchvalue':'ssdln_pic37-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0000000000-10949059015" name="{pageType}_pro_compare37-1_0_0_10949059015_0000000000" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10949059015','shopid':'0000000000','searchvalue':'ssdln_pic37-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0000000000-10949059015','000000010949059015',this);" name="{pageType}_pro_collect37-1_0_0_10949059015_0000000000"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010949059015',10949059015,'0000000000');"  sa-data="{'eletp':'addtocart','prdid':'10949059015','shopid':'0000000000','searchvalue':'ssdln_pic37-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy37-1_0_0_10949059015_0000000000"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0000000000-10971025590    basic   " id="0000000000-10971025590" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="0" goodsType="Z001"  vendor="0000000000" searchType="0"   class="hidenInfo" dataPro="||10971025590||0"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="38">
<a target="_blank" title="千元珍珠屏！实力大音量！" href="//product.suning.com/0000000000/10971025590.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10971025590','shopid':'0000000000','salestatus':'1','searchvalue':'ssdln_pic38-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic38-1_0_0_10971025590_0000000000"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_38:0000000000_10971025590">
<img alt="华为/HUAWEI 畅享9e 千元珍珠屏 3GB+32GB 幻夜黑移动联通电信4G全面屏全网通手机" src="//imgservice3.suning.cn/uimg1/b2c/atmosphere/8QDk0z-c1wZRxLMqlbvfZg.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10971025590subCode">
<dd>
<a href="javascript:void(0)" isOwner="true">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/atmosphere/8QDk0z-c1wZRxLMqlbvfZg.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10971025590|||||0000000000" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10971025590','shopid':'0000000000','salestatus':'{invStatus}','searchvalue':'ssdln_pic38-1_jz','cateid':'20006'}" name="{pageType}_pro_name38-1_0_0_10971025590_0000000000" title="千元珍珠屏！实力大音量！"target="_blank" href="//product.suning.com/0000000000/10971025590.html">华为/HUAWEI 畅享9e 千元珍珠屏 3GB+32GB 幻夜黑移动联通电信4G全面屏全网通手机
<em  style="display:none" >千元珍珠屏！实力大音量！</em>
</a>
</div>
<div class="info-config" title=" 32GB |3GB |6.08英寸">
<em> 32GB <i>|</i>3GB <i>|</i>6.08英寸</em>
</div>
<div class="ad-label">
<i class="new">新品</i>
</div>
<div class="store-stock">
<a href="javascript:void(0);" class="store-class zy">苏宁自营</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10971025590','shopid':'0000000000','searchvalue':'ssdln_pic38-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0000000000-10971025590" name="{pageType}_pro_compare38-1_0_0_10971025590_0000000000" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10971025590','shopid':'0000000000','searchvalue':'ssdln_pic38-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0000000000-10971025590','000000010971025590',this);" name="{pageType}_pro_collect38-1_0_0_10971025590_0000000000"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010971025590',10971025590,'0000000000');"  sa-data="{'eletp':'addtocart','prdid':'10971025590','shopid':'0000000000','searchvalue':'ssdln_pic38-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy38-1_0_0_10971025590_0000000000"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0000000000-10719972854    mobileProduct   " id="0000000000-10719972854" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="0" goodsType="Z001"  vendor="0000000000" searchType="14"   class="hidenInfo" dataPro="||10719972854||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="39">
<a target="_blank" title="6.26英寸全面屏，AI智慧双摄，4000mAh大电池，强劲续航！" href="//product.suning.com/0000000000/10719972854.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10719972854','shopid':'0000000000','salestatus':'1','searchvalue':'ssdln_pic39-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic39-1_0_0_10719972854_0000000000"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_39:0000000000_10719972854">
<img alt="华为/HUAWEI 畅享9  3GB+32GB 极光蓝 高清珍珠屏 AI长续航 移动联通电信4G全网通手机" src="//imgservice3.suning.cn/uimg1/b2c/atmosphere/qnp9szmyF5b3F7gLSOtNyQ.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10719972854subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10719972854" name="10719972854" version="?ver=2037" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/iUnhGGkZaiWxPoytNJ-log.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10719972854" name="10719972845" version="?ver=2035" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/9bKh_rkf5xeVBFxA14PaXQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10719972854" name="10719972850" version="?ver=2032" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/QSl6DdvB2btE7QMKd4Pcwg.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10719972854" name="10719972863" version="?ver=2020" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/ojI3PABvKq3lJDJAMnu-cw.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10719972854|||||0000000000" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10719972854','shopid':'0000000000','salestatus':'{invStatus}','searchvalue':'ssdln_pic39-1_jz','cateid':'20006'}" name="{pageType}_pro_name39-1_0_0_10719972854_0000000000" title="6.26英寸全面屏，AI智慧双摄，4000mAh大电池，强劲续航！"target="_blank" href="//product.suning.com/0000000000/10719972854.html">华为/HUAWEI 畅享9  3GB+32GB 极光蓝 高清珍珠屏 AI长续航 移动联通电信4G全网通手机
<em  style="display:none" >6.26英寸全面屏，AI智慧双摄，4000mAh大电池，强劲续航！</em>
</a>
</div>
<div class="info-config" title=" 32GB |3GB |6.26英寸">
<em> 32GB <i>|</i>3GB <i>|</i>6.26英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10719972854','shopid':'0000000000','searchvalue':'ssdln_pic39-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen39-1_0_0_10719972854_0000000000" href="//product.suning.com/0000000000/10719972854.html#pro_detail_tab"><i>4900+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a href="javascript:void(0);" class="store-class zy">苏宁自营</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10719972854','shopid':'0000000000','searchvalue':'ssdln_pic39-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0000000000-10719972854" name="{pageType}_pro_compare39-1_0_0_10719972854_0000000000" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10719972854','shopid':'0000000000','searchvalue':'ssdln_pic39-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0000000000-10719972854','000000010719972854',this);" name="{pageType}_pro_collect39-1_0_0_10719972854_0000000000"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010719972854',10719972854,'0000000000');"  sa-data="{'eletp':'addtocart','prdid':'10719972854','shopid':'0000000000','searchvalue':'ssdln_pic39-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy39-1_0_0_10719972854_0000000000"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0000000000-10719972883    mobileProduct   " id="0000000000-10719972883" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="0" goodsType="Z001"  vendor="0000000000" searchType="14"   class="hidenInfo" dataPro="||10719972883||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="40">
<a target="_blank" title="6.26英寸全面屏，AI智慧双摄，4000mAh大电池，强劲续航！" href="//product.suning.com/0000000000/10719972883.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10719972883','shopid':'0000000000','salestatus':'1','searchvalue':'ssdln_pic40-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic40-1_0_0_10719972883_0000000000"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_40:0000000000_10719972883">
<img alt="华为/HUAWEI 畅享9  4GB+64GB 极光紫 高清珍珠屏 AI长续航 移动联通电信4G全网通手机" src="//imgservice3.suning.cn/uimg1/b2c/image/ptYSTOuFEd69U2D4iX-qLQ.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10719972883subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10719972883" name="10719972883" version="?ver=2014" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/ptYSTOuFEd69U2D4iX-qLQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10719972883" name="10719972879" version="?ver=2018" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/SJMg6IgUJyAuyK66Zsv5Pg.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10719972883" name="10719972895" version="?ver=2020" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/qSNrK9tDm0mPRI_IaorYxg.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10719972883" name="10719972909" version="?ver=2021" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/XTWqtykQmlFYC2KTbydQDQ.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10719972883|||||0000000000" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10719972883','shopid':'0000000000','salestatus':'{invStatus}','searchvalue':'ssdln_pic40-1_jz','cateid':'20006'}" name="{pageType}_pro_name40-1_0_0_10719972883_0000000000" title="6.26英寸全面屏，AI智慧双摄，4000mAh大电池，强劲续航！"target="_blank" href="//product.suning.com/0000000000/10719972883.html">华为/HUAWEI 畅享9  4GB+64GB 极光紫 高清珍珠屏 AI长续航 移动联通电信4G全网通手机
<em  style="display:none" >6.26英寸全面屏，AI智慧双摄，4000mAh大电池，强劲续航！</em>
</a>
</div>
<div class="info-config" title=" 64GB |4GB |6.26英寸">
<em> 64GB <i>|</i>4GB <i>|</i>6.26英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10719972883','shopid':'0000000000','searchvalue':'ssdln_pic40-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen40-1_0_0_10719972883_0000000000" href="//product.suning.com/0000000000/10719972883.html#pro_detail_tab"><i>8000+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a href="javascript:void(0);" class="store-class zy">苏宁自营</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10719972883','shopid':'0000000000','searchvalue':'ssdln_pic40-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0000000000-10719972883" name="{pageType}_pro_compare40-1_0_0_10719972883_0000000000" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10719972883','shopid':'0000000000','searchvalue':'ssdln_pic40-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0000000000-10719972883','000000010719972883',this);" name="{pageType}_pro_collect40-1_0_0_10719972883_0000000000"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010719972883',10719972883,'0000000000');"  sa-data="{'eletp':'addtocart','prdid':'10719972883','shopid':'0000000000','searchvalue':'ssdln_pic40-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy40-1_0_0_10719972883_0000000000"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0000000000-10971025713    mobileProduct   " id="0000000000-10971025713" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="0" goodsType="Z001"  vendor="0000000000" searchType="14"   class="hidenInfo" dataPro="||10971025713||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="41">
<a target="_blank" title="千元珍珠屏！实力大音量！" href="//product.suning.com/0000000000/10971025713.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10971025713','shopid':'0000000000','salestatus':'1','searchvalue':'ssdln_pic41-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic41-1_0_0_10971025713_0000000000"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_41:0000000000_10971025713">
<img alt="华为/HUAWEI 畅享9e 千元珍珠屏 3GB+64GB 幻夜黑移动联通电信4G全面屏全网通手机" src="//imgservice1.suning.cn/uimg1/b2c/atmosphere/o0a9XHdv8lRAatEPRyQN1Q.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10971025713subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10971025713" name="10971025713" version="?ver=2011" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/reyKQzGwVLBeXy7rJmJGGA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10971025713" name="10971001446" version="?ver=2011" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/DUpDyNROrf7aMxBiuHaorw.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10971025713" name="10971025747" version="?ver=2011" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/DF4KBsLtlGOaIgk3fmFrvQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10971025713" name="10971025727" version="?ver=2004" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/MtURPEwnqGtcZDlcb0BRFA.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10971025713|||||0000000000" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10971025713','shopid':'0000000000','salestatus':'{invStatus}','searchvalue':'ssdln_pic41-1_jz','cateid':'20006'}" name="{pageType}_pro_name41-1_0_0_10971025713_0000000000" title="千元珍珠屏！实力大音量！"target="_blank" href="//product.suning.com/0000000000/10971025713.html">华为/HUAWEI 畅享9e 千元珍珠屏 3GB+64GB 幻夜黑移动联通电信4G全面屏全网通手机
<em  style="display:none" >千元珍珠屏！实力大音量！</em>
</a>
</div>
<div class="info-config" title=" 64GB |3GB |6.08英寸">
<em> 64GB <i>|</i>3GB <i>|</i>6.08英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10971025713','shopid':'0000000000','searchvalue':'ssdln_pic41-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen41-1_0_0_10971025713_0000000000" href="//product.suning.com/0000000000/10971025713.html#pro_detail_tab"><i>2900+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a href="javascript:void(0);" class="store-class zy">苏宁自营</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10971025713','shopid':'0000000000','searchvalue':'ssdln_pic41-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0000000000-10971025713" name="{pageType}_pro_compare41-1_0_0_10971025713_0000000000" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10971025713','shopid':'0000000000','searchvalue':'ssdln_pic41-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0000000000-10971025713','000000010971025713',this);" name="{pageType}_pro_collect41-1_0_0_10971025713_0000000000"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010971025713',10971025713,'0000000000');"  sa-data="{'eletp':'addtocart','prdid':'10971025713','shopid':'0000000000','searchvalue':'ssdln_pic41-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy41-1_0_0_10971025713_0000000000"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0000000000-10949091351    mobileProduct   " id="0000000000-10949091351" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="0" goodsType="Z001"  vendor="0000000000" searchType="14"   class="hidenInfo" dataPro="||10949091351||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="42">
<a target="_blank" title="6.21英寸珍珠屏！超广角AI三摄！拍照如此简单！" href="//product.suning.com/0000000000/10949091351.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10949091351','shopid':'0000000000','salestatus':'1','searchvalue':'ssdln_pic42-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic42-1_0_0_10949091351_0000000000"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_42:0000000000_10949091351">
<img alt="华为/HUAWEI 畅享9S 超广角AI三摄 4GB+128GB 极光蓝移动联通电信4G全面屏全网通手机" src="//imgservice4.suning.cn/uimg1/b2c/image/G0icw45cNN3mjOUYeT4FsA.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10949091351subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10949091351" name="10949091351" version="?ver=2008" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/G0icw45cNN3mjOUYeT4FsA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10949091351" name="10949057915" version="?ver=2008" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/in_8Yx2capGBB93yxNp5Gw.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10949091351" name="10949057935" version="?ver=2008" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/G5ZZMgeTybZldbC62nQPvw.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10949091351|||||0000000000" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10949091351','shopid':'0000000000','salestatus':'{invStatus}','searchvalue':'ssdln_pic42-1_jz','cateid':'20006'}" name="{pageType}_pro_name42-1_0_0_10949091351_0000000000" title="6.21英寸珍珠屏！超广角AI三摄！拍照如此简单！"target="_blank" href="//product.suning.com/0000000000/10949091351.html">华为/HUAWEI 畅享9S 超广角AI三摄 4GB+128GB 极光蓝移动联通电信4G全面屏全网通手机
<em  style="display:none" >6.21英寸珍珠屏！超广角AI三摄！拍照如此简单！</em>
</a>
</div>
<div class="info-config" title=" 128GB |4GB |6.21英寸">
<em> 128GB <i>|</i>4GB <i>|</i>6.21英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10949091351','shopid':'0000000000','searchvalue':'ssdln_pic42-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen42-1_0_0_10949091351_0000000000" href="//product.suning.com/0000000000/10949091351.html#pro_detail_tab"><i>6500+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a href="javascript:void(0);" class="store-class zy">苏宁自营</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10949091351','shopid':'0000000000','searchvalue':'ssdln_pic42-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0000000000-10949091351" name="{pageType}_pro_compare42-1_0_0_10949091351_0000000000" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10949091351','shopid':'0000000000','searchvalue':'ssdln_pic42-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0000000000-10949091351','000000010949091351',this);" name="{pageType}_pro_collect42-1_0_0_10949091351_0000000000"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010949091351',10949091351,'0000000000');"  sa-data="{'eletp':'addtocart','prdid':'10949091351','shopid':'0000000000','searchvalue':'ssdln_pic42-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy42-1_0_0_10949091351_0000000000"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070517287-11197971651    mobileProduct   " id="0070517287-11197971651" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070517287" searchType="14"   class="hidenInfo" dataPro="||11197971651||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="43">
<a target="_blank" title="后置四摄、前置2400万像素、双卡双待" href="//product.suning.com/0070517287/11197971651.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'11197971651','shopid':'0070517287','salestatus':'1','searchvalue':'ssdln_pic43-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic43-1_0_0_11197971651_0070517287"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_43:0070517287_11197971651">
<img alt="华为(HUAWEI)nova5i 全网通 8GB+128GB 幻夜黑 后置四摄 前置2400万像素 双卡双待 移动联通电信4G手机" src="//imgservice4.suning.cn/uimg1/b2c/atmosphere/yYBxlhndYAHgSLtRjBWl_A.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="11197971651subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197971651" name="11197971651" version="" color="" isDynamic="true" vendorId= "0070517287"   colorValue="幻夜黑"  alt="幻夜黑" title="幻夜黑" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/kfoQpUbcknlGBngV6Syl7Q.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197971651" name="11197971759" version="" color="" isDynamic="true" vendorId= "0070517287"   colorValue="蜜语红"  alt="蜜语红" title="蜜语红" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/km0R4wE2ZKZ27GYoBfumug.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197971651" name="11197971701" version="" color="" isDynamic="true" vendorId= "0070517287"   colorValue="苏音蓝"  alt="苏音蓝" title="苏音蓝" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/RWhQx3_PkxfPRfBuUDXCxQ.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="11197971651|||||0070517287" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'11197971651','shopid':'0070517287','salestatus':'{invStatus}','searchvalue':'ssdln_pic43-1_jz','cateid':'20006'}" name="{pageType}_pro_name43-1_0_0_11197971651_0070517287" title="后置四摄、前置2400万像素、双卡双待"target="_blank" href="//product.suning.com/0070517287/11197971651.html">华为(HUAWEI)nova5i 全网通 8GB+128GB 幻夜黑 后置四摄 前置2400万像素 双卡双待 移动联通电信4G手机
<em  style="display:none" >后置四摄、前置2400万像素、双卡双待</em>
</a>
</div>
<div class="info-config" title=" 128GB |8GB |6.4英寸">
<em> 128GB <i>|</i>8GB <i>|</i>6.4英寸</em>
</div>
<div class="ad-label">
<i class="new">新品</i>
</div>
<div class="store-stock">
<a class='store-name' href='//litai.suning.com?pcode=11197971651'   sa-data="{'eletp':'shop','prdid':'11197971651','shopid':'70517287','searchvalue':'ssdln_pic43-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70517287_0'>质点旗舰店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'11197971651','shopid':'0070517287','searchvalue':'ssdln_pic43-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070517287-11197971651" name="{pageType}_pro_compare43-1_0_0_11197971651_0070517287" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'11197971651','shopid':'0070517287','searchvalue':'ssdln_pic43-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070517287-11197971651','000000011197971651',this);" name="{pageType}_pro_collect43-1_0_0_11197971651_0070517287"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000011197971651',11197971651,'0070517287');"  sa-data="{'eletp':'addtocart','prdid':'11197971651','shopid':'0070517287','searchvalue':'ssdln_pic43-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy43-1_0_0_11197971651_0070517287"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-10776826286    mobileProduct   " id="0070094634-10776826286" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||10776826286||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="44">
<a target="_blank" title="6.4英寸极点全面屏,2500万海报级自拍,8+128大存储组合,流光幻影机身。" href="//product.suning.com/0070094634/10776826286.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10776826286','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic44-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic44-1_0_0_10776826286_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_44:0070094634_10776826286">
<img alt="华为(HUAWEI) 华为nova4 4800万超广角三摄 高配 全网通版 8GB+128GB 苏音蓝 移动联通电信4G智能手机" src="//imgservice4.suning.cn/uimg1/b2c/atmosphere/rZZx5m-iFnOMy1SZ03MboA.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10776826286subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10776826286" name="10776826286" version="?ver=2021" color="" isDynamic="true" vendorId= "0070094634"   colorValue="苏音蓝"  alt="苏音蓝" title="苏音蓝" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/2D1FjTMf4EQqgTQQJx_oIw.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10776826286" name="10776826280" version="?ver=2011" color="" isDynamic="true" vendorId= "0070094634"   colorValue="亮黑色"  alt="亮黑色" title="亮黑色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/nfQnAaTSgjsEZMshaDFi8A.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10776826286" name="10776833090" version="?ver=2007" color="" isDynamic="true" vendorId= "0070094634"   colorValue="蜜语红"  alt="蜜语红" title="蜜语红" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/zHS5tXycPp2oU5JaabFtmw.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10776826286" name="10776833178" version="?ver=2001" color="" isDynamic="true" vendorId= "0070094634"   colorValue="贝母白"  alt="贝母白" title="贝母白" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/yVteawSAR-ZSIU3wOkpavA.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10776826286|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10776826286','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic44-1_jz','cateid':'20006'}" name="{pageType}_pro_name44-1_0_0_10776826286_0070094634" title="6.4英寸极点全面屏,2500万海报级自拍,8+128大存储组合,流光幻影机身。"target="_blank" href="//product.suning.com/0070094634/10776826286.html">华为(HUAWEI) 华为nova4 4800万超广角三摄 高配 全网通版 8GB+128GB 苏音蓝 移动联通电信4G智能手机
<em  style="display:none" >6.4英寸极点全面屏,2500万海报级自拍,8+128大存储组合,流光幻影机身。</em>
</a>
</div>
<div class="info-config" title=" 128GB |8GB |6.4英寸">
<em> 128GB <i>|</i>8GB <i>|</i>6.4英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10776826286','shopid':'0070094634','searchvalue':'ssdln_pic44-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen44-1_0_0_10776826286_0070094634" href="//product.suning.com/0070094634/10776826286.html#pro_detail_tab"><i>100+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=10776826286'   sa-data="{'eletp':'shop','prdid':'10776826286','shopid':'70094634','searchvalue':'ssdln_pic44-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10776826286','shopid':'0070094634','searchvalue':'ssdln_pic44-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-10776826286" name="{pageType}_pro_compare44-1_0_0_10776826286_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10776826286','shopid':'0070094634','searchvalue':'ssdln_pic44-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-10776826286','000000010776826286',this);" name="{pageType}_pro_collect44-1_0_0_10776826286_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010776826286',10776826286,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'10776826286','shopid':'0070094634','searchvalue':'ssdln_pic44-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy44-1_0_0_10776826286_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0000000000-10819539641    mobileProduct   " id="0000000000-10819539641" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="0" goodsType="Z001"  vendor="0000000000" searchType="14"   class="hidenInfo" dataPro="||10819539641||14"   bigPartys="14832870#0000000000" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="45">
<a target="_blank" title="麒麟980芯片 超广角三摄 超微距摄影 8曲面3D玻璃机身 40W超级快充!" href="//product.suning.com/0000000000/10819539641.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10819539641','shopid':'0000000000','salestatus':'1','searchvalue':'ssdln_pic45-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic45-1_0_0_10819539641_0000000000"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_45:0000000000_10819539641">
<img alt="华为/HUAWEI Mate 20 Pro 馥蕾红（UD） 8GB+128GB 屏下指纹版麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机" src="//imgservice1.suning.cn/uimg1/b2c/image/BVI7uX35CyZU_J_6zuU9NA.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10819539641subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10819539641" name="10819539641" version="?ver=2020" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/BVI7uX35CyZU_J_6zuU9NA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10819539641" name="10819539642" version="?ver=2020" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/HOrbCNCdTrH2CITXL5Jldw.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10819539641|||||0000000000" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10819539641','shopid':'0000000000','salestatus':'{invStatus}','searchvalue':'ssdln_pic45-1_jz','cateid':'20006'}" name="{pageType}_pro_name45-1_0_0_10819539641_0000000000" title="麒麟980芯片 超广角三摄 超微距摄影 8曲面3D玻璃机身 40W超级快充!"target="_blank" href="//product.suning.com/0000000000/10819539641.html">华为/HUAWEI Mate 20 Pro 馥蕾红（UD） 8GB+128GB 屏下指纹版麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机
<em  style="display:none" >麒麟980芯片 超广角三摄 超微距摄影 8曲面3D玻璃机身 40W超级快充!</em>
</a>
</div>
<div class="info-config" title=" 128GB |8GB |6.39英寸">
<em> 128GB <i>|</i>8GB <i>|</i>6.39英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10819539641','shopid':'0000000000','searchvalue':'ssdln_pic45-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen45-1_0_0_10819539641_0000000000" href="//product.suning.com/0000000000/10819539641.html#pro_detail_tab"><i>1500+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a href="javascript:void(0);" class="store-class zy">苏宁自营</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10819539641','shopid':'0000000000','searchvalue':'ssdln_pic45-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0000000000-10819539641" name="{pageType}_pro_compare45-1_0_0_10819539641_0000000000" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10819539641','shopid':'0000000000','searchvalue':'ssdln_pic45-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0000000000-10819539641','000000010819539641',this);" name="{pageType}_pro_collect45-1_0_0_10819539641_0000000000"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010819539641',10819539641,'0000000000');"  sa-data="{'eletp':'addtocart','prdid':'10819539641','shopid':'0000000000','searchvalue':'ssdln_pic45-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy45-1_0_0_10819539641_0000000000"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070517287-10804782166    mobileProduct   " id="0070517287-10804782166" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070517287" searchType="14"   class="hidenInfo" dataPro="||10804782166||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="46">
<a target="_blank" title="6.5英寸全面屏，1600万高清拍摄，4000mAh长续航。" href="//product.suning.com/0070517287/10804782166.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10804782166','shopid':'0070517287','salestatus':'1','searchvalue':'ssdln_pic46-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic46-1_0_0_10804782166_0070517287"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_46:0070517287_10804782166">
<img alt="华为(HUAWEI)畅享9 Plus 全网通版 6GB+128GB 幻夜黑色 四摄 全面屏 移动联通电信4G手机 双卡双待 华为畅享9plus" src="//imgservice2.suning.cn/uimg1/b2c/atmosphere/Y1hMc9FbMxvKpiyuHh8vlA.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10804782166subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10804782166" name="10804782166" version="?ver=2019" color="" isDynamic="true" vendorId= "0070517287"   colorValue="幻夜黑"  alt="幻夜黑" title="幻夜黑" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/6fSF2gqmYNR3AdR9tzDXCg.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10804782166" name="10805023761" version="?ver=2001" color="" isDynamic="true" vendorId= "0070517287"   colorValue="宝石蓝"  alt="宝石蓝" title="宝石蓝" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/2O3pNGTd3iNZkAwyPg_IKQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10804782166" name="10805023773" version="?ver=2001" color="" isDynamic="true" vendorId= "0070517287"   colorValue="极光紫"  alt="极光紫" title="极光紫" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/R5p-UdPNXtJnPdQYkVTKUw.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10804782166" name="10805023778" version="" color="" isDynamic="true" vendorId= "0070517287"   colorValue="樱语粉"  alt="樱语粉" title="樱语粉" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/IKDTaTYnkxtDSk5NDk0wiQ.png_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10804782166|||||0070517287" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10804782166','shopid':'0070517287','salestatus':'{invStatus}','searchvalue':'ssdln_pic46-1_jz','cateid':'20006'}" name="{pageType}_pro_name46-1_0_0_10804782166_0070517287" title="6.5英寸全面屏，1600万高清拍摄，4000mAh长续航。"target="_blank" href="//product.suning.com/0070517287/10804782166.html">华为(HUAWEI)畅享9 Plus 全网通版 6GB+128GB 幻夜黑色 四摄 全面屏 移动联通电信4G手机 双卡双待 华为畅享9plus
<em  style="display:none" >6.5英寸全面屏，1600万高清拍摄，4000mAh长续航。</em>
</a>
</div>
<div class="info-config" title=" 128GB |6GB |6.5英寸">
<em> 128GB <i>|</i>6GB <i>|</i>6.5英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10804782166','shopid':'0070517287','searchvalue':'ssdln_pic46-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen46-1_0_0_10804782166_0070517287" href="//product.suning.com/0070517287/10804782166.html#pro_detail_tab"><i>200+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//litai.suning.com?pcode=10804782166'   sa-data="{'eletp':'shop','prdid':'10804782166','shopid':'70517287','searchvalue':'ssdln_pic46-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70517287_0'>质点旗舰店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10804782166','shopid':'0070517287','searchvalue':'ssdln_pic46-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070517287-10804782166" name="{pageType}_pro_compare46-1_0_0_10804782166_0070517287" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10804782166','shopid':'0070517287','searchvalue':'ssdln_pic46-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070517287-10804782166','000000010804782166',this);" name="{pageType}_pro_collect46-1_0_0_10804782166_0070517287"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010804782166',10804782166,'0070517287');"  sa-data="{'eletp':'addtocart','prdid':'10804782166','shopid':'0070517287','searchvalue':'ssdln_pic46-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy46-1_0_0_10804782166_0070517287"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-10471273896    mobileProduct   " id="0070094634-10471273896" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||10471273896||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="47">
<a target="_blank" title="麒麟970智慧芯片，6.1英寸全面屏，夜神之眼，安全快充，AI摄影。" href="//product.suning.com/0070094634/10471273896.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10471273896','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic47-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic47-1_0_0_10471273896_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_47:0070094634_10471273896">
<img alt="华为(HUAWEI) 华为P20 Pro 全面屏 全网通版 6GB+128GB 极光色 移动联通电信4G手机 双卡双待" src="//imgservice2.suning.cn/uimg1/b2c/atmosphere/hPQOaz3QiEWCJSVA95XWNQ.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10471273896subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10471273896" name="10471273896" version="?ver=2039" color="" isDynamic="true" vendorId= "0070094634"   colorValue="极光色"  alt="极光色" title="极光色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/A4GYGr3msLLN_CH66Ot5XQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10471273896" name="10471274229" version="?ver=2007" color="" isDynamic="true" vendorId= "0070094634"   colorValue="亮黑色"  alt="亮黑色" title="亮黑色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/IuL4iabCRDsycY2yMTNHzA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10471273896" name="10600524325" version="?ver=2006" color="" isDynamic="true" vendorId= "0070094634"   colorValue="极光闪蝶"  alt="极光闪蝶" title="极光闪蝶" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/vk6sLR-5QfwJf0dfj7XsRg.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10471273896|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10471273896','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic47-1_jz','cateid':'20006'}" name="{pageType}_pro_name47-1_0_0_10471273896_0070094634" title="麒麟970智慧芯片，6.1英寸全面屏，夜神之眼，安全快充，AI摄影。"target="_blank" href="//product.suning.com/0070094634/10471273896.html">华为(HUAWEI) 华为P20 Pro 全面屏 全网通版 6GB+128GB 极光色 移动联通电信4G手机 双卡双待
<em  style="display:none" >麒麟970智慧芯片，6.1英寸全面屏，夜神之眼，安全快充，AI摄影。</em>
</a>
</div>
<div class="info-config" title=" 128GB |6GB |6.1英寸">
<em> 128GB <i>|</i>6GB <i>|</i>6.1英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10471273896','shopid':'0070094634','searchvalue':'ssdln_pic47-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen47-1_0_0_10471273896_0070094634" href="//product.suning.com/0070094634/10471273896.html#pro_detail_tab"><i>200+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=10471273896'   sa-data="{'eletp':'shop','prdid':'10471273896','shopid':'70094634','searchvalue':'ssdln_pic47-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10471273896','shopid':'0070094634','searchvalue':'ssdln_pic47-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-10471273896" name="{pageType}_pro_compare47-1_0_0_10471273896_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10471273896','shopid':'0070094634','searchvalue':'ssdln_pic47-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-10471273896','000000010471273896',this);" name="{pageType}_pro_collect47-1_0_0_10471273896_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010471273896',10471273896,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'10471273896','shopid':'0070094634','searchvalue':'ssdln_pic47-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy47-1_0_0_10471273896_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0000000000-10973073885    mobileProduct   " id="0000000000-10973073885" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="0" goodsType="Z001"  vendor="0000000000" searchType="14"   class="hidenInfo" dataPro="||10973073885||14"   bigPartys="14832840#0000000000" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="48">
<a target="_blank" title="麒麟980智慧芯片/超感光徕卡四摄/50倍数字变焦" href="//product.suning.com/0000000000/10973073885.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10973073885','shopid':'0000000000','salestatus':'1','searchvalue':'ssdln_pic48-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic48-1_0_0_10973073885_0000000000"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_48:0000000000_10973073885">
<img alt="华为/HUAWEI P30 Pro 极光色 8GB+512GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机" src="//imgservice5.suning.cn/uimg1/b2c/atmosphere/uIyfuUDetbMRvkJ-gud1Bw.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10973073885subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10973073885" name="10973073885" version="?ver=2022" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/VzZewsb-Y6dt6XWlMVD4Rw.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10973073885" name="10973073855" version="?ver=2020" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/zMJdCUxEn4Db4LcxJzwsUA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10973073885" name="10973073906" version="?ver=2022" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/ffg5NPLVthj5uFcKyH5zYw.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10973073885" name="10973073914" version="?ver=2022" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/8EWy7iPVSMk73i7xE3XTZQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10973073885" name="10973073923" version="?ver=2021" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/FhrQnVSy0SWZos-o9ujotw.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10973073885|||||0000000000" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10973073885','shopid':'0000000000','salestatus':'{invStatus}','searchvalue':'ssdln_pic48-1_jz','cateid':'20006'}" name="{pageType}_pro_name48-1_0_0_10973073885_0000000000" title="麒麟980智慧芯片/超感光徕卡四摄/50倍数字变焦"target="_blank" href="//product.suning.com/0000000000/10973073885.html">华为/HUAWEI P30 Pro 极光色 8GB+512GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机
<em  style="display:none" >麒麟980智慧芯片/超感光徕卡四摄/50倍数字变焦</em>
</a>
</div>
<div class="info-config" title=" 512GB |8GB |6.47英寸">
<em> 512GB <i>|</i>8GB <i>|</i>6.47英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10973073885','shopid':'0000000000','searchvalue':'ssdln_pic48-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen48-1_0_0_10973073885_0000000000" href="//product.suning.com/0000000000/10973073885.html#pro_detail_tab"><i>400+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a href="javascript:void(0);" class="store-class zy">苏宁自营</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10973073885','shopid':'0000000000','searchvalue':'ssdln_pic48-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0000000000-10973073885" name="{pageType}_pro_compare48-1_0_0_10973073885_0000000000" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10973073885','shopid':'0000000000','searchvalue':'ssdln_pic48-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0000000000-10973073885','000000010973073885',this);" name="{pageType}_pro_collect48-1_0_0_10973073885_0000000000"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010973073885',10973073885,'0000000000');"  sa-data="{'eletp':'addtocart','prdid':'10973073885','shopid':'0000000000','searchvalue':'ssdln_pic48-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy48-1_0_0_10973073885_0000000000"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-11197493276    mobileProduct   " id="0070094634-11197493276" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||11197493276||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="49">
<a target="_blank" title="麒麟980芯片，前置3200万像素，后置4800万AI四摄，双卡双待。" href="//product.suning.com/0070094634/11197493276.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'11197493276','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic49-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic49-1_0_0_11197493276_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_49:0070094634_11197493276">
<img alt="华为(HUAWEI) nova5 Pro 8GB+256GB 绮境森林 全网通 麒麟980 4800万AI四摄 移动联通电信4G拍照手机 华为nova5pro" src="//imgservice3.suning.cn/uimg1/b2c/atmosphere/Njrw78IkE6rZo5IAAKDkjA.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="11197493276subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197493276" name="11197493276" version="?ver=2002" color="" isDynamic="true" vendorId= "0070094634"   colorValue="绮境森林"  alt="绮境森林" title="绮境森林" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/nzxSP5g9AZk_0eov3YkmZQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197493276" name="11197493209" version="?ver=2002" color="" isDynamic="true" vendorId= "0070094634"   colorValue="仲夏紫"  alt="仲夏紫" title="仲夏紫" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/nAa46bV3ei4NHbZ2Zy5VVA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197493276" name="11197493175" version="?ver=2002" color="" isDynamic="true" vendorId= "0070094634"   colorValue="亮黑色"  alt="亮黑色" title="亮黑色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/YW7sQepuw3dJauezCDOmYg.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197493276" name="11197493247" version="?ver=2002" color="" isDynamic="true" vendorId= "0070094634"   colorValue="珊瑚橙"  alt="珊瑚橙" title="珊瑚橙" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/_yyz6BQNPwnFi9hc250nyQ.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="11197493276|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'11197493276','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic49-1_jz','cateid':'20006'}" name="{pageType}_pro_name49-1_0_0_11197493276_0070094634" title="麒麟980芯片，前置3200万像素，后置4800万AI四摄，双卡双待。"target="_blank" href="//product.suning.com/0070094634/11197493276.html">华为(HUAWEI) nova5 Pro 8GB+256GB 绮境森林 全网通 麒麟980 4800万AI四摄 移动联通电信4G拍照手机 华为nova5pro
<em  style="display:none" >麒麟980芯片，前置3200万像素，后置4800万AI四摄，双卡双待。</em>
</a>
</div>
<div class="info-config" title=" 256GB |8GB |6.39英寸">
<em> 256GB <i>|</i>8GB <i>|</i>6.39英寸</em>
</div>
<div class="ad-label">
<i class="new">新品</i>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=11197493276'   sa-data="{'eletp':'shop','prdid':'11197493276','shopid':'70094634','searchvalue':'ssdln_pic49-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'11197493276','shopid':'0070094634','searchvalue':'ssdln_pic49-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-11197493276" name="{pageType}_pro_compare49-1_0_0_11197493276_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'11197493276','shopid':'0070094634','searchvalue':'ssdln_pic49-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-11197493276','000000011197493276',this);" name="{pageType}_pro_collect49-1_0_0_11197493276_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000011197493276',11197493276,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'11197493276','shopid':'0070094634','searchvalue':'ssdln_pic49-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy49-1_0_0_11197493276_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070517287-10985358566    mobileProduct   " id="0070517287-10985358566" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070517287" searchType="14"   class="hidenInfo" dataPro="||10985358566||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="50">
<a target="_blank" title="麒麟710，6.21英寸珍珠屏，2400万广角三摄大存储大电池" href="//product.suning.com/0070517287/10985358566.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10985358566','shopid':'0070517287','salestatus':'1','searchvalue':'ssdln_pic50-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic50-1_0_0_10985358566_0070517287"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_50:0070517287_10985358566">
<img alt="华为(HUAWEI)畅享9s 全网通版 4GB+128GB 幻夜黑 2400万超广角三摄珍珠屏大存储 移动联通电信4G手机 双卡双待" src="//imgservice2.suning.cn/uimg1/b2c/atmosphere/eM0OAmhX4fLqGITAZaCoDQ.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10985358566subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985358566" name="10985358566" version="?ver=2005" color="" isDynamic="true" vendorId= "0070517287"   colorValue="幻夜黑"  alt="幻夜黑" title="幻夜黑" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/vawblf0v1Ms0kd3cBrlq1g.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985358566" name="10985338509" version="?ver=2005" color="" isDynamic="true" vendorId= "0070517287"   colorValue="极光蓝"  alt="极光蓝" title="极光蓝" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/f4HuOBFVzFCCeziOBKpjDg.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985358566" name="10985607121" version="?ver=2005" color="" isDynamic="true" vendorId= "0070517287"   colorValue="珊瑚红"  alt="珊瑚红" title="珊瑚红" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/fJmrHggSeavfeJ6XYcaWZw.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10985358566|||||0070517287" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10985358566','shopid':'0070517287','salestatus':'{invStatus}','searchvalue':'ssdln_pic50-1_jz','cateid':'20006'}" name="{pageType}_pro_name50-1_0_0_10985358566_0070517287" title="麒麟710，6.21英寸珍珠屏，2400万广角三摄大存储大电池"target="_blank" href="//product.suning.com/0070517287/10985358566.html">华为(HUAWEI)畅享9s 全网通版 4GB+128GB 幻夜黑 2400万超广角三摄珍珠屏大存储 移动联通电信4G手机 双卡双待
<em  style="display:none" >麒麟710，6.21英寸珍珠屏，2400万广角三摄大存储大电池</em>
</a>
</div>
<div class="info-config" title=" 128GB |4GB |6.21英寸">
<em> 128GB <i>|</i>4GB <i>|</i>6.21英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10985358566','shopid':'0070517287','searchvalue':'ssdln_pic50-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen50-1_0_0_10985358566_0070517287" href="//product.suning.com/0070517287/10985358566.html#pro_detail_tab"><i>200+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//litai.suning.com?pcode=10985358566'   sa-data="{'eletp':'shop','prdid':'10985358566','shopid':'70517287','searchvalue':'ssdln_pic50-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70517287_0'>质点旗舰店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10985358566','shopid':'0070517287','searchvalue':'ssdln_pic50-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070517287-10985358566" name="{pageType}_pro_compare50-1_0_0_10985358566_0070517287" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10985358566','shopid':'0070517287','searchvalue':'ssdln_pic50-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070517287-10985358566','000000010985358566',this);" name="{pageType}_pro_collect50-1_0_0_10985358566_0070517287"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010985358566',10985358566,'0070517287');"  sa-data="{'eletp':'addtocart','prdid':'10985358566','shopid':'0070517287','searchvalue':'ssdln_pic50-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy50-1_0_0_10985358566_0070517287"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-11197493140    mobileProduct   " id="0070094634-11197493140" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||11197493140||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="51">
<a target="_blank" title="麒麟980芯片，前置3200万像素，后置4800万AI四摄，双卡双待。" href="//product.suning.com/0070094634/11197493140.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'11197493140','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic51-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic51-1_0_0_11197493140_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_51:0070094634_11197493140">
<img alt="华为(HUAWEI) nova5 Pro 8GB+128GB 绮境森林 全网通 麒麟980 4800万AI四摄 移动联通电信4G拍照手机 华为nova5pro" src="//imgservice5.suning.cn/uimg1/b2c/atmosphere/oQ9BzVIpsBC_XNBZT_TB8A.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="11197493140subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197493140" name="11197493140" version="?ver=2002" color="" isDynamic="true" vendorId= "0070094634"   colorValue="绮境森林"  alt="绮境森林" title="绮境森林" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/YlPKodMfzgH4QFfa0L1BpA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197493140" name="11197493095" version="?ver=2002" color="" isDynamic="true" vendorId= "0070094634"   colorValue="仲夏紫"  alt="仲夏紫" title="仲夏紫" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/bWiYgCWDDWsf6bbwiJ4Owg.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197493140" name="11197493132" version="?ver=2002" color="" isDynamic="true" vendorId= "0070094634"   colorValue="珊瑚橙"  alt="珊瑚橙" title="珊瑚橙" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/DKeUGxVyqNim3xIpmmSc0g.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197493140" name="11197493079" version="?ver=2002" color="" isDynamic="true" vendorId= "0070094634"   colorValue="亮黑色"  alt="亮黑色" title="亮黑色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice5.suning.cn/uimg1/b2c/image/UqKl8uAeaU3VDSTI4lA2-w.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="11197493140|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'11197493140','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic51-1_jz','cateid':'20006'}" name="{pageType}_pro_name51-1_0_0_11197493140_0070094634" title="麒麟980芯片，前置3200万像素，后置4800万AI四摄，双卡双待。"target="_blank" href="//product.suning.com/0070094634/11197493140.html">华为(HUAWEI) nova5 Pro 8GB+128GB 绮境森林 全网通 麒麟980 4800万AI四摄 移动联通电信4G拍照手机 华为nova5pro
<em  style="display:none" >麒麟980芯片，前置3200万像素，后置4800万AI四摄，双卡双待。</em>
</a>
</div>
<div class="info-config" title=" 128GB |8GB |6.39英寸">
<em> 128GB <i>|</i>8GB <i>|</i>6.39英寸</em>
</div>
<div class="ad-label">
<i class="new">新品</i>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=11197493140'   sa-data="{'eletp':'shop','prdid':'11197493140','shopid':'70094634','searchvalue':'ssdln_pic51-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'11197493140','shopid':'0070094634','searchvalue':'ssdln_pic51-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-11197493140" name="{pageType}_pro_compare51-1_0_0_11197493140_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'11197493140','shopid':'0070094634','searchvalue':'ssdln_pic51-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-11197493140','000000011197493140',this);" name="{pageType}_pro_collect51-1_0_0_11197493140_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000011197493140',11197493140,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'11197493140','shopid':'0070094634','searchvalue':'ssdln_pic51-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy51-1_0_0_11197493140_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-11197591712    mobileProduct   " id="0070094634-11197591712" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||11197591712||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="52">
<a target="_blank" title="后置AI四摄，极点全面屏，前置2400万高清摄像头，双卡双待。" href="//product.suning.com/0070094634/11197591712.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'11197591712','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic52-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic52-1_0_0_11197591712_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_52:0070094634_11197591712">
<img alt="华为(HUAWEI) nova5i 6GB+128GB 苏音蓝 全网通 后置四摄 前置2400万像素 移动联通电信4G手机 双卡双待" src="//imgservice3.suning.cn/uimg1/b2c/atmosphere/VJajvtSqw4HFIphoRiR-rA.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="11197591712subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197591712" name="11197591712" version="?ver=2001" color="" isDynamic="true" vendorId= "0070094634"   colorValue="苏音蓝"  alt="苏音蓝" title="苏音蓝" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/2hQruGmeAzeKqKscyQaUww.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197591712" name="11197591691" version="?ver=2001" color="" isDynamic="true" vendorId= "0070094634"   colorValue="幻夜黑"  alt="幻夜黑" title="幻夜黑" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/6ylSfZCOJZ6RbCeDDR9prQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="11197591712" name="11197605488" version="?ver=2001" color="" isDynamic="true" vendorId= "0070094634"   colorValue="蜜语红"  alt="蜜语红" title="蜜语红" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/NCPGdAr-vbB0vpqmFe5UQQ.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="11197591712|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'11197591712','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic52-1_jz','cateid':'20006'}" name="{pageType}_pro_name52-1_0_0_11197591712_0070094634" title="后置AI四摄，极点全面屏，前置2400万高清摄像头，双卡双待。"target="_blank" href="//product.suning.com/0070094634/11197591712.html">华为(HUAWEI) nova5i 6GB+128GB 苏音蓝 全网通 后置四摄 前置2400万像素 移动联通电信4G手机 双卡双待
<em  style="display:none" >后置AI四摄，极点全面屏，前置2400万高清摄像头，双卡双待。</em>
</a>
</div>
<div class="info-config" title=" 128GB |6GB |6.4英寸">
<em> 128GB <i>|</i>6GB <i>|</i>6.4英寸</em>
</div>
<div class="ad-label">
<i class="new">新品</i>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=11197591712'   sa-data="{'eletp':'shop','prdid':'11197591712','shopid':'70094634','searchvalue':'ssdln_pic52-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'11197591712','shopid':'0070094634','searchvalue':'ssdln_pic52-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-11197591712" name="{pageType}_pro_compare52-1_0_0_11197591712_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'11197591712','shopid':'0070094634','searchvalue':'ssdln_pic52-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-11197591712','000000011197591712',this);" name="{pageType}_pro_collect52-1_0_0_11197591712_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000011197591712',11197591712,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'11197591712','shopid':'0070094634','searchvalue':'ssdln_pic52-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy52-1_0_0_11197591712_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070182176-10968727227    mobileProduct   " id="0070182176-10968727227" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070182176" searchType="14"   class="hidenInfo" dataPro="||10968727227||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="53">
<a target="_blank" title="【关注店铺领优惠券，送全屏钢化膜等】麒麟980处理器，4000mAh大容量电池" href="//product.suning.com/0070182176/10968727227.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10968727227','shopid':'0070182176','salestatus':'1','searchvalue':'ssdln_pic53-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic53-1_0_0_10968727227_0070182176"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_53:0070182176_10968727227">
<img alt="华为/荣耀(honor) 荣耀V20 魅眼全视屏 全网通高配版 8GB+128GB 幻夜黑 移动联通电信4G手机" src="//imgservice3.suning.cn/uimg1/b2c/image/PxromF01dUkU4wT6fm1hGA.png_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10968727227subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10968727227" name="10968727227" version="?ver=2001" color="" isDynamic="true" vendorId= "0070182176"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/PxromF01dUkU4wT6fm1hGA.png_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10968727227" name="10968727265" version="" color="" isDynamic="true" vendorId= "0070182176"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/KobMENf69VxHqQBDRHCtLg.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10968727227|||||0070182176" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10968727227','shopid':'0070182176','salestatus':'{invStatus}','searchvalue':'ssdln_pic53-1_jz','cateid':'20006'}" name="{pageType}_pro_name53-1_0_0_10968727227_0070182176" title="【关注店铺领优惠券，送全屏钢化膜等】麒麟980处理器，4000mAh大容量电池"target="_blank" href="//product.suning.com/0070182176/10968727227.html">华为/荣耀(honor) 荣耀V20 魅眼全视屏 全网通高配版 8GB+128GB 幻夜黑 移动联通电信4G手机
<em  style="display:none" >【关注店铺领优惠券，送全屏钢化膜等】麒麟980处理器，4000mAh大容量电池</em>
</a>
</div>
<div class="info-config" title=" 128GB |8GB |6.4英寸">
<em> 128GB <i>|</i>8GB <i>|</i>6.4英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10968727227','shopid':'0070182176','searchvalue':'ssdln_pic53-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen53-1_0_0_10968727227_0070182176" href="//product.suning.com/0070182176/10968727227.html#pro_detail_tab"><i>10+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//jiayeshoujishuma.suning.com?pcode=10968727227'   sa-data="{'eletp':'shop','prdid':'10968727227','shopid':'70182176','searchvalue':'ssdln_pic53-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70182176_0'>嘉业手机数码专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10968727227','shopid':'0070182176','searchvalue':'ssdln_pic53-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070182176-10968727227" name="{pageType}_pro_compare53-1_0_0_10968727227_0070182176" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10968727227','shopid':'0070182176','searchvalue':'ssdln_pic53-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070182176-10968727227','000000010968727227',this);" name="{pageType}_pro_collect53-1_0_0_10968727227_0070182176"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010968727227',10968727227,'0070182176');"  sa-data="{'eletp':'addtocart','prdid':'10968727227','shopid':'0070182176','searchvalue':'ssdln_pic53-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy53-1_0_0_10968727227_0070182176"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070517287-10756034330    mobileProduct   " id="0070517287-10756034330" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070517287" searchType="14"   class="hidenInfo" dataPro="||10756034330||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="54">
<a target="_blank" title="6.26英寸全面屏，AI智慧双摄，4000mAh大电池，强劲续航！" href="//product.suning.com/0070517287/10756034330.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10756034330','shopid':'0070517287','salestatus':'1','searchvalue':'ssdln_pic54-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic54-1_0_0_10756034330_0070517287"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_54:0070517287_10756034330">
<img alt="华为(HUAWEI) 畅享9 高配版 4GB+64GB 幻夜黑 全网通 移动联通电信4G手机 人脸解锁" src="//imgservice1.suning.cn/uimg1/b2c/atmosphere/_UYhfHm60UVw61YULc8UuQ.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10756034330subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10756034330" name="10756034330" version="?ver=2005" color="" isDynamic="true" vendorId= "0070517287"   colorValue="幻夜黑"  alt="幻夜黑" title="幻夜黑" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/jJPzIjZn30nkIwZMEbf9aQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10756034330" name="10756034472" version="?ver=2002" color="" isDynamic="true" vendorId= "0070517287"   colorValue="极光蓝"  alt="极光蓝" title="极光蓝" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/AHezGqPKjyt3er1Kag3uHw.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10756034330" name="10756034426" version="?ver=2001" color="" isDynamic="true" vendorId= "0070517287"   colorValue="极光紫"  alt="极光紫" title="极光紫" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/xUHP-HlWx6f9OGpJJDWf6w.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10756034330|||||0070517287" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10756034330','shopid':'0070517287','salestatus':'{invStatus}','searchvalue':'ssdln_pic54-1_jz','cateid':'20006'}" name="{pageType}_pro_name54-1_0_0_10756034330_0070517287" title="6.26英寸全面屏，AI智慧双摄，4000mAh大电池，强劲续航！"target="_blank" href="//product.suning.com/0070517287/10756034330.html">华为(HUAWEI) 畅享9 高配版 4GB+64GB 幻夜黑 全网通 移动联通电信4G手机 人脸解锁
<em  style="display:none" >6.26英寸全面屏，AI智慧双摄，4000mAh大电池，强劲续航！</em>
</a>
</div>
<div class="info-config" title=" 64GB |4GB |6.26英寸">
<em> 64GB <i>|</i>4GB <i>|</i>6.26英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10756034330','shopid':'0070517287','searchvalue':'ssdln_pic54-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen54-1_0_0_10756034330_0070517287" href="//product.suning.com/0070517287/10756034330.html#pro_detail_tab"><i>200+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//litai.suning.com?pcode=10756034330'   sa-data="{'eletp':'shop','prdid':'10756034330','shopid':'70517287','searchvalue':'ssdln_pic54-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70517287_0'>质点旗舰店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10756034330','shopid':'0070517287','searchvalue':'ssdln_pic54-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070517287-10756034330" name="{pageType}_pro_compare54-1_0_0_10756034330_0070517287" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10756034330','shopid':'0070517287','searchvalue':'ssdln_pic54-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070517287-10756034330','000000010756034330',this);" name="{pageType}_pro_collect54-1_0_0_10756034330_0070517287"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010756034330',10756034330,'0070517287');"  sa-data="{'eletp':'addtocart','prdid':'10756034330','shopid':'0070517287','searchvalue':'ssdln_pic54-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy54-1_0_0_10756034330_0070517287"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070142956-10985936863    mobileProduct   " id="0070142956-10985936863" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070142956" searchType="14"   class="hidenInfo" dataPro="||10985936863||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="55">
<a target="_blank" title="6.09英寸珍珠屏，64GB大内存，后置1300万像素，12nm八核处理器" href="//product.suning.com/0070142956/10985936863.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10985936863','shopid':'0070142956','salestatus':'1','searchvalue':'ssdln_pic55-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic55-1_0_0_10985936863_0070142956"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_55:0070142956_10985936863">
<img alt="华为(HUAWEI)华为畅享9e 3GB+64GB 全网通高配版（幻夜黑）移动联通电信4G手机 华为畅享 9e手机" src="//imgservice3.suning.cn/uimg1/b2c/image/1SOGA4Efxvl0mIBCuf1zUA.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10985936863subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985936863" name="10985936863" version="?ver=2001" color="" isDynamic="true" vendorId= "0070142956"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/1SOGA4Efxvl0mIBCuf1zUA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985936863" name="10985936785" version="?ver=2007" color="" isDynamic="true" vendorId= "0070142956"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/_B77U7bW1fJSNCXaQmY4Dw.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10985936863" name="10985936946" version="?ver=2001" color="" isDynamic="true" vendorId= "0070142956"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/Waq2jmGvXchkgrGlM26QYg.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10985936863|||||0070142956" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10985936863','shopid':'0070142956','salestatus':'{invStatus}','searchvalue':'ssdln_pic55-1_jz','cateid':'20006'}" name="{pageType}_pro_name55-1_0_0_10985936863_0070142956" title="6.09英寸珍珠屏，64GB大内存，后置1300万像素，12nm八核处理器"target="_blank" href="//product.suning.com/0070142956/10985936863.html">华为(HUAWEI)华为畅享9e 3GB+64GB 全网通高配版（幻夜黑）移动联通电信4G手机 华为畅享 9e手机
<em  style="display:none" >6.09英寸珍珠屏，64GB大内存，后置1300万像素，12nm八核处理器</em>
</a>
</div>
<div class="info-config" title=" 64GB |3GB |6.088英寸">
<em> 64GB <i>|</i>3GB <i>|</i>6.088英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10985936863','shopid':'0070142956','searchvalue':'ssdln_pic55-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen55-1_0_0_10985936863_0070142956" href="//product.suning.com/0070142956/10985936863.html#pro_detail_tab"><i>60+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//tianhuansm.suning.com?pcode=10985936863'   sa-data="{'eletp':'shop','prdid':'10985936863','shopid':'70142956','searchvalue':'ssdln_pic55-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70142956_0'>天环云手机数码官方旗舰店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10985936863','shopid':'0070142956','searchvalue':'ssdln_pic55-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070142956-10985936863" name="{pageType}_pro_compare55-1_0_0_10985936863_0070142956" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10985936863','shopid':'0070142956','searchvalue':'ssdln_pic55-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070142956-10985936863','000000010985936863',this);" name="{pageType}_pro_collect55-1_0_0_10985936863_0070142956"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010985936863',10985936863,'0070142956');"  sa-data="{'eletp':'addtocart','prdid':'10985936863','shopid':'0070142956','searchvalue':'ssdln_pic55-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy55-1_0_0_10985936863_0070142956"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0000000000-10398811280    mobileProduct   " id="0000000000-10398811280" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="0" goodsType="Z001"  vendor="0000000000" searchType="14"   class="hidenInfo" dataPro="||10398811280||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="56">
<a target="_blank" title="新一代徕卡双镜头 麒麟970智慧芯片！" href="//product.suning.com/0000000000/10398811280.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10398811280','shopid':'0000000000','salestatus':'1','searchvalue':'ssdln_pic56-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic56-1_0_0_10398811280_0000000000"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_56:0000000000_10398811280">
<img alt="华为/HUAWEI P20 6GB+128GB亮黑色移动联通电信4G全面屏全网通手机" src="//imgservice1.suning.cn/uimg1/b2c/image/kjeo1-Y_-QdIbvcZdXv_4Q.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10398811280subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10398811280" name="10398811280" version="?ver=2113" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/kjeo1-Y_-QdIbvcZdXv_4Q.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10398811280" name="10398811567" version="?ver=2113" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/0J2xXVcLo4RZL6x92J8NOA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10398811280" name="10591388398" version="?ver=2073" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/taiJ1iH1LFm3xFgvq79u2A.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10398811280|||||0000000000" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10398811280','shopid':'0000000000','salestatus':'{invStatus}','searchvalue':'ssdln_pic56-1_jz','cateid':'20006'}" name="{pageType}_pro_name56-1_0_0_10398811280_0000000000" title="新一代徕卡双镜头 麒麟970智慧芯片！"target="_blank" href="//product.suning.com/0000000000/10398811280.html">华为/HUAWEI P20 6GB+128GB亮黑色移动联通电信4G全面屏全网通手机
<em  style="display:none" >新一代徕卡双镜头 麒麟970智慧芯片！</em>
</a>
</div>
<div class="info-config" title=" 128GB |6GB |5.8英寸">
<em> 128GB <i>|</i>6GB <i>|</i>5.8英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10398811280','shopid':'0000000000','searchvalue':'ssdln_pic56-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen56-1_0_0_10398811280_0000000000" href="//product.suning.com/0000000000/10398811280.html#pro_detail_tab"><i>7000+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a href="javascript:void(0);" class="store-class zy">苏宁自营</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10398811280','shopid':'0000000000','searchvalue':'ssdln_pic56-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0000000000-10398811280" name="{pageType}_pro_compare56-1_0_0_10398811280_0000000000" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10398811280','shopid':'0000000000','searchvalue':'ssdln_pic56-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0000000000-10398811280','000000010398811280',this);" name="{pageType}_pro_collect56-1_0_0_10398811280_0000000000"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010398811280',10398811280,'0000000000');"  sa-data="{'eletp':'addtocart','prdid':'10398811280','shopid':'0000000000','searchvalue':'ssdln_pic56-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy56-1_0_0_10398811280_0000000000"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070142956-10553621290    mobileProduct   " id="0070142956-10553621290" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070142956" searchType="14"   class="hidenInfo" dataPro="||10553621290||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="57">
<a target="_blank" title="18:9高清全面屏，32GB大内存三卡槽，智能柔光自拍，听筒大音量" href="//product.suning.com/0070142956/10553621290.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10553621290','shopid':'0070142956','salestatus':'1','searchvalue':'ssdln_pic57-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic57-1_0_0_10553621290_0070142956"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_57:0070142956_10553621290">
<img alt="华为(HUAWEI) 畅享8e青春 2GB+32GB全面屏 （金色）全网通版 移动联通电信4G手机 双卡双待" src="//imgservice2.suning.cn/uimg1/b2c/image/JCtwEPL44Kpg52jMitWF3Q.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10553621290subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10553621290" name="10553621290" version="?ver=2018" color="" isDynamic="true" vendorId= "0070142956"   colorValue="金色"  alt="金色" title="金色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/JCtwEPL44Kpg52jMitWF3Q.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10553621290" name="10553621309" version="?ver=2001" color="" isDynamic="true" vendorId= "0070142956"   colorValue="黑色"  alt="黑色" title="黑色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/7DahWGL6IqbwEWbpUQx4sQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10553621290" name="10553621289" version="" color="" isDynamic="true" vendorId= "0070142956"   colorValue="蓝色"  alt="蓝色" title="蓝色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice2.suning.cn/uimg1/b2c/image/jZjcrRF1gbb-FlvmwMsc8A.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10553621290|||||0070142956" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10553621290','shopid':'0070142956','salestatus':'{invStatus}','searchvalue':'ssdln_pic57-1_jz','cateid':'20006'}" name="{pageType}_pro_name57-1_0_0_10553621290_0070142956" title="18:9高清全面屏，32GB大内存三卡槽，智能柔光自拍，听筒大音量"target="_blank" href="//product.suning.com/0070142956/10553621290.html">华为(HUAWEI) 畅享8e青春 2GB+32GB全面屏 （金色）全网通版 移动联通电信4G手机 双卡双待
<em  style="display:none" >18:9高清全面屏，32GB大内存三卡槽，智能柔光自拍，听筒大音量</em>
</a>
</div>
<div class="info-config" title=" 32GB |2GB |5.45英寸">
<em> 32GB <i>|</i>2GB <i>|</i>5.45英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10553621290','shopid':'0070142956','searchvalue':'ssdln_pic57-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen57-1_0_0_10553621290_0070142956" href="//product.suning.com/0070142956/10553621290.html#pro_detail_tab"><i>600+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//tianhuansm.suning.com?pcode=10553621290'   sa-data="{'eletp':'shop','prdid':'10553621290','shopid':'70142956','searchvalue':'ssdln_pic57-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70142956_0'>天环云手机数码官方旗舰店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10553621290','shopid':'0070142956','searchvalue':'ssdln_pic57-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070142956-10553621290" name="{pageType}_pro_compare57-1_0_0_10553621290_0070142956" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10553621290','shopid':'0070142956','searchvalue':'ssdln_pic57-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070142956-10553621290','000000010553621290',this);" name="{pageType}_pro_collect57-1_0_0_10553621290_0070142956"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010553621290',10553621290,'0070142956');"  sa-data="{'eletp':'addtocart','prdid':'10553621290','shopid':'0070142956','searchvalue':'ssdln_pic57-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy57-1_0_0_10553621290_0070142956"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070094634-10989627017    mobileProduct   " id="0070094634-10989627017" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070094634" searchType="14"   class="hidenInfo" dataPro="||10989627017||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="58">
<a target="_blank" title="麒麟980智慧芯片，支持无线充电，超感光徕卡四摄，50倍数字变焦。" href="//product.suning.com/0070094634/10989627017.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10989627017','shopid':'0070094634','salestatus':'1','searchvalue':'ssdln_pic58-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic58-1_0_0_10989627017_0070094634"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_58:0070094634_10989627017">
<img alt="华为(HUAWEI) 华为P30 Pro 麒麟980 超感光徕卡四摄 全网通版 8GB+128GB 天空之境 移动联通电信4G手机 华为p30pro" src="//imgservice1.suning.cn/uimg1/b2c/atmosphere/7i2vuk2c6fToR2jhUSAiqg.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10989627017subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10989627017" name="10989627017" version="?ver=2012" color="" isDynamic="true" vendorId= "0070094634"   colorValue="天空之境"  alt="天空之境" title="天空之境" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/iatcgLWB3Aaq_VgUF0IF7w.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10989627017" name="10989605659" version="?ver=2005" color="" isDynamic="true" vendorId= "0070094634"   colorValue="亮黑色"  alt="亮黑色" title="亮黑色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/aRzbc5HVwIkkKqrF9UBCzQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10989627017" name="10989627020" version="?ver=2003" color="" isDynamic="true" vendorId= "0070094634"   colorValue="极光色"  alt="极光色" title="极光色" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/ipMck1B7H8zFspKgNJp7ww.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10989627017" name="10989700927" version="?ver=2002" color="" isDynamic="true" vendorId= "0070094634"   colorValue="赤茶橘"  alt="赤茶橘" title="赤茶橘" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/Az7xnleUdt6YfHte9EmjhA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10989627017" name="10989700918" version="?ver=2004" color="" isDynamic="true" vendorId= "0070094634"   colorValue="珠光贝母"  alt="珠光贝母" title="珠光贝母" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice1.suning.cn/uimg1/b2c/image/vFto6bw4v010lB67nbFCow.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10989627017|||||0070094634" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10989627017','shopid':'0070094634','salestatus':'{invStatus}','searchvalue':'ssdln_pic58-1_jz','cateid':'20006'}" name="{pageType}_pro_name58-1_0_0_10989627017_0070094634" title="麒麟980智慧芯片，支持无线充电，超感光徕卡四摄，50倍数字变焦。"target="_blank" href="//product.suning.com/0070094634/10989627017.html">华为(HUAWEI) 华为P30 Pro 麒麟980 超感光徕卡四摄 全网通版 8GB+128GB 天空之境 移动联通电信4G手机 华为p30pro
<em  style="display:none" >麒麟980智慧芯片，支持无线充电，超感光徕卡四摄，50倍数字变焦。</em>
</a>
</div>
<div class="info-config" title=" 128GB |8GB |6.47英寸">
<em> 128GB <i>|</i>8GB <i>|</i>6.47英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10989627017','shopid':'0070094634','searchvalue':'ssdln_pic58-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen58-1_0_0_10989627017_0070094634" href="//product.suning.com/0070094634/10989627017.html#pro_detail_tab"><i>100+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//shop.suning.com/70094634/index.html?pcode=10989627017'   sa-data="{'eletp':'shop','prdid':'10989627017','shopid':'70094634','searchvalue':'ssdln_pic58-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70094634_0'>华科手机专营店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10989627017','shopid':'0070094634','searchvalue':'ssdln_pic58-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070094634-10989627017" name="{pageType}_pro_compare58-1_0_0_10989627017_0070094634" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10989627017','shopid':'0070094634','searchvalue':'ssdln_pic58-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070094634-10989627017','000000010989627017',this);" name="{pageType}_pro_collect58-1_0_0_10989627017_0070094634"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010989627017',10989627017,'0070094634');"  sa-data="{'eletp':'addtocart','prdid':'10989627017','shopid':'0070094634','searchvalue':'ssdln_pic58-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy58-1_0_0_10989627017_0070094634"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0000000000-10638755882    mobileProduct   " id="0000000000-10638755882" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="0" goodsType="Z001"  vendor="0000000000" searchType="14"   class="hidenInfo" dataPro="||10638755882||14"   bigPartys="14832867#0000000000" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="59">
<a target="_blank" title="麒麟980芯片 超广角三摄 超微距摄影 8曲面3D玻璃机身 40W超级快充!" href="//product.suning.com/0000000000/10638755882.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10638755882','shopid':'0000000000','salestatus':'1','searchvalue':'ssdln_pic59-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic59-1_0_0_10638755882_0000000000"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_59:0000000000_10638755882">
<img alt="华为/HUAWEI Mate 20 Pro 翡冷翠（UD） 8GB+256GB 屏下指纹版麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机" src="//imgservice4.suning.cn/uimg1/b2c/atmosphere/tEc_KvBWFia0MD1BcJZ3xQ.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10638755882subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10638755882" name="10638755882" version="?ver=2049" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/kvoU9a7p7-YxQQM6wuL65A.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10638755882" name="10638755881" version="?ver=2053" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/TlQ8-Npi6fqS6LEkgViI_Q.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10638755882" name="10638755879" version="?ver=2034" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/p2fHJquWnwDfzoELYpBRBQ.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10638755882" name="10638755878" version="?ver=2054" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/RdQ0it89QL8HZpWvwZ9MrA.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10638755882" name="10638755880" version="?ver=2020" color="" isDynamic="true" vendorId= "0000000000"   alt="" title="" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice4.suning.cn/uimg1/b2c/image/-zkbIqObwIxJQHB6cMWIWw.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10638755882|||||0000000000" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10638755882','shopid':'0000000000','salestatus':'{invStatus}','searchvalue':'ssdln_pic59-1_jz','cateid':'20006'}" name="{pageType}_pro_name59-1_0_0_10638755882_0000000000" title="麒麟980芯片 超广角三摄 超微距摄影 8曲面3D玻璃机身 40W超级快充!"target="_blank" href="//product.suning.com/0000000000/10638755882.html">华为/HUAWEI Mate 20 Pro 翡冷翠（UD） 8GB+256GB 屏下指纹版麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机
<em  style="display:none" >麒麟980芯片 超广角三摄 超微距摄影 8曲面3D玻璃机身 40W超级快充!</em>
</a>
</div>
<div class="info-config" title=" 256GB |8GB |6.39英寸">
<em> 256GB <i>|</i>8GB <i>|</i>6.39英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10638755882','shopid':'0000000000','searchvalue':'ssdln_pic59-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen59-1_0_0_10638755882_0000000000" href="//product.suning.com/0000000000/10638755882.html#pro_detail_tab"><i>1400+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a href="javascript:void(0);" class="store-class zy">苏宁自营</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10638755882','shopid':'0000000000','searchvalue':'ssdln_pic59-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0000000000-10638755882" name="{pageType}_pro_compare59-1_0_0_10638755882_0000000000" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10638755882','shopid':'0000000000','searchvalue':'ssdln_pic59-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0000000000-10638755882','000000010638755882',this);" name="{pageType}_pro_collect59-1_0_0_10638755882_0000000000"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010638755882',10638755882,'0000000000');"  sa-data="{'eletp':'addtocart','prdid':'10638755882','shopid':'0000000000','searchvalue':'ssdln_pic59-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy59-1_0_0_10638755882_0000000000"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>
<li docType="1" specFlag = "" isHwg="" class="item-wrap  0070517287-10686769004    mobileProduct   " id="0070517287-10686769004" name=""  lazy="true" hasPrice="false">
<div class="item-bg">
<div class="product-box ">
<input type="hidden" vendorType="1" goodsType="Z001"  vendor="0070517287" searchType="14"   class="hidenInfo" dataPro="||10686769004||14"   bigPartys="" order="" contract="" onloadFn="proOnloadEvent"  tryInStore="" />
<div class="res-img">
<div class="img-block" tempIndex="60">
<a target="_blank" title="7nm麒麟980智能芯片，大广角徕卡三摄，高屏占比，长续航。" href="//product.suning.com/0070517287/10686769004.html"class="sellPoint"
sa-data="{'eletp':'prd','prdid':'10686769004','shopid':'0070517287','salestatus':'1','searchvalue':'ssdln_pic60-1_jz','cateid':'20006'}"
name="{pageType}_pro_pic60-1_0_0_10686769004_0070517287"
id="{pageType}_pro_baoguang{invStatus}-0-1_1_60:0070517287_10686769004">
<img alt="华为(HUAWEI) 华为Mate20X 全网通版 6GB+128GB 宝石蓝色 移动联通电信4G手机 麒麟980 全面屏 徕卡三摄 华为mate20x" src="//imgservice3.suning.cn/uimg1/b2c/atmosphere/OOhLdD-7-yX9Mcvk84OwvQ.jpg_400w_400h_4e">
</a>
</div>
<div class="focus-box">
<a href="javascript:void(0);" class="btn-l disabled"><b></b></a> <a
href="javascript:void(0);" class="btn-r"><b></b></a>
<div class="focus-img">
<dl style="width: 360px" class="10686769004subCode">
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10686769004" name="10686769004" version="?ver=2015" color="" isDynamic="true" vendorId= "0070517287"   colorValue="宝石蓝"  alt="宝石蓝" title="宝石蓝" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/-h34OaB5V4SjjYR6e6R-Lw.jpg_400w_400h_4e">
</a>
</dd>
<dd>
<a href="javascript:void(0)" verticalUrl="" parnumber="10686769004" name="10686769007" version="?ver=2010" color="" isDynamic="true" vendorId= "0070517287"   colorValue="幻影银"  alt="幻影银" title="幻影银" isMutil="false" isSpeSubFlag="false">
<img width="32" height="32" src="//imgservice3.suning.cn/uimg1/b2c/image/CnEmOXnl9yJUOL1sxuZZLg.jpg_400w_400h_4e">
</a>
</dd>
</dl>
</div>
</div>
</div>
<div class="res-info">
<div class="price-box">
<span class="def-price" datasku="10686769004|||||0070517287" brand_id="000060864" threeGroup_id="R1901001">
</span>
</div>
<div class="title-selling-point">
<a

sa-data="{'eletp':'prd','prdid':'10686769004','shopid':'0070517287','salestatus':'{invStatus}','searchvalue':'ssdln_pic60-1_jz','cateid':'20006'}" name="{pageType}_pro_name60-1_0_0_10686769004_0070517287" title="7nm麒麟980智能芯片，大广角徕卡三摄，高屏占比，长续航。"target="_blank" href="//product.suning.com/0070517287/10686769004.html">华为(HUAWEI) 华为Mate20X 全网通版 6GB+128GB 宝石蓝色 移动联通电信4G手机 麒麟980 全面屏 徕卡三摄 华为mate20x
<em  style="display:none" >7nm麒麟980智能芯片，大广角徕卡三摄，高屏占比，长续航。</em>
</a>
</div>
<div class="info-config" title=" 128GB |6GB |7.2英寸">
<em> 128GB <i>|</i>6GB <i>|</i>7.2英寸</em>
</div>
<div class="evaluate-old clearfix">
<div class="info-evaluate">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10686769004','shopid':'0070517287','searchvalue':'ssdln_pic60-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  target="_blank" name="{pageType}_pro_commen60-1_0_0_10686769004_0070517287" href="//product.suning.com/0070517287/10686769004.html#pro_detail_tab"><i>200+</i>评价</a>
</div>
</div>
<div class="store-stock">
<a class='store-name' href='//litai.suning.com?pcode=10686769004'   sa-data="{'eletp':'shop','prdid':'10686769004','shopid':'70517287','searchvalue':'ssdln_pic60-1_jz','salestatus':'{invStatus}','cateid':'20006'}" target='_blank' name='{pageType}_pro_dp0-_0_0_70517287_0'>质点旗舰店</a>
</div>
<div class="sales-label"  isHotBrief="false"></div>
</div>
<div class="res-opt one-third">
<a  rel="nofollow"  sa-data="{'eletp':'prd','prdid':'10686769004','shopid':'0070517287','searchvalue':'ssdln_pic60-1_jz','salestatus':'{invStatus}','cateid':'20006'}" href="javascript:void(0);" id="0070517287-10686769004" name="{pageType}_pro_compare60-1_0_0_10686769004_0070517287" class="btn-db"><i></i><em>取消</em>对比</a>
<a rel="nofollow"   sa-data="{'eletp':'collect','prdid':'10686769004','shopid':'0070517287','searchvalue':'ssdln_pic60-1_jz','salestatus':'{invStatus}','cateid':'20006'}"  href="javascript:void(0);" onclick="javascript:snSearch.productButton.addToInterests('0070517287-10686769004','000000010686769004',this);" name="{pageType}_pro_collect60-1_0_0_10686769004_0070517287"  class="btn-sc"><i></i><em>已</em>关注</a>
<input type="hidden" value="1" class="cart-ipt">
<input type="hidden" value="1" class="ajaxSuccess">
<a rel="nofollow"  href="javascript:snSearch.carShopProduct.addMiniShoppingCart('000000010686769004',10686769004,'0070517287');"  sa-data="{'eletp':'addtocart','prdid':'10686769004','shopid':'0070517287','searchvalue':'ssdln_pic60-1_jz','salestatus':'{invStatus}','cateid':'20006'}" class="btn-gwc" name="{pageType}_pro_buy60-1_0_0_10686769004_0070517287"><i></i>加入购物车</a>
</div>
</div>
</div>
</li>



"""

html_doc = etree.HTML(html)

detail_url_list = html_doc.xpath('//li/div/div/div[2]/div[2]/a/@href')
url = detail_url_list[0]
print(url)

# tex = requests.get(url="https:"+url).text
kkk = """
<!DOCTYPE html>
<head>
	<meta charset="UTF-8" />
    <title>华为(HUAWEI)手机畅享9S 华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待【价格 图片 品牌 报价】-苏宁易购华科手机专营店</title>
    <meta name="keywords" content="华为(HUAWEI)手机，华为(HUAWEI)，华为(HUAWEI)手机畅享9S报价，华为(HUAWEI)畅享9S价格"/>
    <meta name="description" content="华为(HUAWEI)手机畅享9S，苏宁易购提供华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待，麒麟710，6.21英寸珍珠屏，2400万广角三摄大存储大电池，买华为(HUAWEI)手机，就来华科手机专营店！"/>
    <meta name="mobile-agent" content="format=html5;url=//m.suning.com/product/0070094634/10985347748.html">
    <meta http-equiv="Cache-Control" content="no-siteapp"/>
    <meta http-equiv="Cache-Control" content="no-transform"/>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge,chrome=1"/>
    <meta name="applicable-device" content="pc"/>
    <meta name="MobileOptimized" content="width"/>
    <meta name="HandheldFriendly" content="true"/>
    <meta content="true" name="autoclick">
    <meta content="d488778a" name="siteid"/>
    <meta content="10004" name="pageid">
    <meta content="500" name="sadelay"/>

    <meta property="og:type" content="product"/>
    <meta property="og:image" content="//imgservice.suning.cn/uimg1/b2c/image/783X00lIk6NabyNuOdOUbw.jpg_800w_800h_4e"/>
    <meta property="og:title" content="华为(HUAWEI)手机畅享9S 华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待【价格 图片 品牌 报价】-苏宁易购华科手机专营店"/>
    <meta property="og:description" content="华为(HUAWEI)手机畅享9S，苏宁易购提供华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待，麒麟710，6.21英寸珍珠屏，2400万广角三摄大存储大电池，买华为(HUAWEI)手机，就来华科手机专营店！"/>

    <link rel="alternate" media="only screen and(max-width:640px)" href="//m.suning.com/product/0070094634/10985347748.html">
    <link rel="canonical" href="//product.suning.com/0070094634/10985347748.html">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
<script type="text/javascript"> /*定义当前页面在我的易购下的类别标识*/ var mySuningSideBarSign = "dac_myego_sidebar03"; var sn = sn || {"listHost":"//list.suning.com/","conline":"conline.suning.com","ninePartNumber":"10985347748","serviceCentre":"","zoneDomain":"//zone.suning.com","prdType":"g","prdTypeVal":"textContent","virtualPartNumber":"000000000945055174","cartPath":"cart.suning.com/emall","cartHost":"cart.suning.com","now":"2019-07-22 15:44:47","onlineDomain":"online.suning.com","vcsDomain":"//vcs.suning.com","subcodeflag":"1","sizeAttr":"2","productId":"","itemId":"","yushouDomain":"//yushou.suning.com","brandFlag":"","imageDomianDir":"//image4.suning.cn","qiangDomain":"qiang.suning.com", "spikeHost":"promotion.suning.com","itemDomain":"//item.suning.com","shopMainPh":".suning.com","shopPath":"//shop","tuijianDomain":"//tuijian.suning.com","scriptDomain":"//script.suning.cn","elecProductDomain":"//product.suning.com","itemDisplayName":"华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待", "categoryName3":"手机","brandDomain":"//brand.suning.com","domain":"www.suning.com","shopType":"1","vendorCode":"0070094634","catenIds":"R1901001","catalogId":"10051", "commonResourceURL":"//image.suning.cn","category1":"20089","categoryName1":"手机/数码/配件","category2":"20002","categoryName2":"手机通讯","categoryId":"20006", "published":"1","simBuyType":"","partNumber":"000000010985347748","context":"/emall","uuid":"9301112b-da40-47bd-82b7-3652cc47923e","brandCode":"0864","brandId":"000060864", "clusterMap":[{"color": "10001","itemCuPartNumber":[{"versionId":"20003","partNumber":"000000010985358059","itemType":""},{"versionId":"20002","partNumber":"000000011082969306","itemType":""},{"versionId":"20005","partNumber":"000000000945055174","itemType":""},{"versionId":"20004","partNumber":"000000010991918870","itemType":""},{"versionId":"20001","partNumber":"000000010985347748","itemType":""},{"versionId":"20007","partNumber":"000000000945055169","itemType":""},{"versionId":"20006","partNumber":"000000000945058886","itemType":""},{"versionId":"20008","partNumber":"000000000945058793","itemType":""}]},{"color": "10002","itemCuPartNumber":[{"versionId":"20003","partNumber":"000000010985347822","itemType":""},{"versionId":"20002","partNumber":"000000011082969315","itemType":""},{"versionId":"20005","partNumber":"000000000945055175","itemType":""},{"versionId":"20004","partNumber":"000000010992045431","itemType":""},{"versionId":"20001","partNumber":"000000010985347786","itemType":""},{"versionId":"20007","partNumber":"000000000945055172","itemType":""},{"versionId":"20006","partNumber":"000000000945058887","itemType":""},{"versionId":"20008","partNumber":"000000000945058794","itemType":""}]},{"color": "10003","itemCuPartNumber":[{"versionId":"20003","partNumber":"000000010985624285","itemType":""},{"versionId":"20002","partNumber":"000000011082969382","itemType":""},{"versionId":"20005","partNumber":"000000000945055176","itemType":""},{"versionId":"20004","partNumber":"000000011036776950","itemType":""},{"versionId":"20001","partNumber":"000000010985624242","itemType":""},{"versionId":"20007","partNumber":"000000000945055173","itemType":""},{"versionId":"20006","partNumber":"000000000945058888","itemType":""},{"versionId":"20008","partNumber":"000000000945058795","itemType":""}]}], "colorList":[{"colorid":"10001","partNumber":"000000011082969306","itemType":""},{"colorid":"10002","partNumber":"000000010992045431","itemType":""},{"colorid":"10003","partNumber":"000000000945055176","itemType":""},], "pic":"//image4.suning.cn/uimg/b2c/newcatentries/0070094634-000000010985347748_1_400x400.jpg", "itemDomain":"//"+document.location.hostname, "resRoot":"//script.suning.cn/project/pdsWeb", "shopCount":1, "sellerDomain":"//www.suning.com/sellers/", "controller":[{"FOUR_ACCESSORY_INFO":"120","FOUR_PSS_ACTIVITY":"120","FOURDESC":"120","FOURTIMEPAGE":"300","PRICE_FLAG":"0","FOURBIGPOLY":"120"}], "imageCount":5, "context": "/emall", "storeId": "10052", "online": "online.suning.com", "apsDomain":"//apscore.suning.com/", "newImageDomianDir":"//image3.suning.cn", "apsId":"", "reviewNew":"//review.suning.com/", "pcShopListChange":0, "memberDomain": "member.suning.com", "renxfSwitch":"1", "cookieDomain": ".suning.com", "searchDomain": "//search.suning.com/emall/", "businessType":"", "pdsRelationURl":"/project/pdsWeb/", "qrCodeDomain":"//ma.suning.com", "qrCodeDomainNew":"//code.suning.cn", "qrCodeLongUrl":"//res.m.suning.com", "vipDomain":"//vip.suning.com", "imgHost": "//image?.suning.cn", "shopName":"华科手机专营店", "yxImRoot":"//istore.suning.com/im-web/", "treatCode":"", "buyCode":"", "jypwCatenIds":"R9004701", "ipServiceHost":"//ipservice.suning.com", "storeServiceRoot":"//store.suning.com/", "tmImageDomianDir":"//image3.suning.cn", "imgHostTag": "?", "saleVolume":0, "imgHostNumber": "5", "imgUrlStarNum": "1", "legouVendor":"0070076553", "vbuyDomain":"//vbuy.suning.com", "pgFlag":"10051_4", "passPartNumber":"000000010985347748", "flagshipid":"0070094634", "flagshipName":"华科手机专营店", "tuijianCatenIds":["R1901001","R1202001","R1207002","R1207001","R1204001","R1304001","R1502001","R1502002","R9000844","R1704002","R1501001","R9003540","R1501005","R9000843","R0128002","R0128001","R1701002","R0191001","R1301001","R1301002","R0151001","R0151004","R1302005","R1702003","R1702004","R0104001","R0104002","R0105001","R0105002","R0503002","R0504001","R2601001","R2601005","R2402001"], "comPartNumbers":[], "moisDomain":"//mois.suning.com", "curShopName":"<a target='_blank' name='item_10985347748_shop_dianpu02' href='//shop.suning.com/70094634/index.html'>华科手机专营店</a>", "swlShopFlag":false, "hwgShopFlag":false, "csSwlShopFlag":false, "tmShopFlag":false, "phoneFlag":"Y", "donateID":"R9004987", "pageType":"1", "brandName":"华为(HUAWEI)", "newResServer":"//res.suning.cn", "aqPhone":"https://aq.suning.com/asc/mobile/check.do", "paySuning":"https://passport.suning.com/ids/trustLogin?sysCode=epp&targetUrl=https://pay.suning.com/epp-epw/quickPay/quick-pay-contract!showBankList.action", "selectedDistrictName":"", "broadBandId":"", "rxfCompetency":"//sncfc.suning.com/sncfc-tps/creditpay/acctauth.do", "shopStatus":"0", "amDetailLink":"//hc.suning.com/help/channel-153317729649767636.htm", "amDetail":"退货细则及服务", "amPdsRelation":"//res.suning.cn/project/pdsWeb/", "amAbroadDetailLink":"//help.suning.com/page/channel-258.htm", "amAbroadDetail":"退货细则及服务", "amAbroadName":"_10985347748_shbz_tuihuo", "notSaleProductGroup":"", "solpUrl":"//solp.suning.com", "nowDate":"20190722", "cuxiaoType":"", "silenceType":"", "silenceTip":"", "cuxiaoSoldOut":"", "notSaleFlag":false, "newItemDesSwith":"0", "qkkUrl":"//hyj.suning.com", "icpsDomain":"//icps.suning.com", "reserveSwitch":"0", "govPriceSwitch":"", "cuxiaoSwitch":"0", "returnGoodsSwitch":"1", "icpsPriceStreetId":"01", "shoplistcacheSwitch":"1", "oldForNewBrandIds":"00006,00005,00001,00002,00003,00004,00013", "ecsDomain": "//hx.suning.com", "bookActionAddcartFlag":"1", "deliveryFlag":"1", "cDeliveryFlag":"1", "fimsFreightSwith":"0", "fimsDomain":"//fims.suning.com", "cmmdtyType":"Z001", "modelName":"畅享9S", "qualityUrl":"//qc.suning.com", "cmsBannerUrl":"//lib.suning.com", "qualitySwitch":"", "footTickCatenIds":"R9007701", "cloudAddcartFlag":"1", "liquanCount":"11", "assssDomain":"//assss.suning.com", "pcssDomain":"//pcsslabel.suning.cn", "quanUrl":"//quan.suning.com", "attachList":"000000000945055174", "reviewTotal":"0", "luaUrl":"//pas.suning.com", "hasSidebar":true, /*默认关闭，true为打开*/ "hasBottomFixed":false, /*默认关闭，true为打开*/ "hasTopFixed":false, /*默认关闭，true为打开*/ "qualificationList":"0", "itemViewFlag":false, "intelligent":"//dt.suning.com", "version":"?v=2019071306", "mjSwitch":"0", "pageNO":"02", "smartFlag":false, "itemSource":"", "pavilion":"", "bigpolylogin":"0", "juDomain":"//ju.suning.com", "recDomain":"//rec.suning.com", "pcImportantClause":"本站苏宁自营商品的商品详情信息及包装参数信息均由供应商自行设计、制作并通过苏宁向其开放的数据端口自行发布，其真实性、准确性和合法性由供应商负责。本站保证苏宁自营商品均为正品，但因生产厂家可能会在没有任何提前通知的情况下更改产品包装、产地或者一些附件，本站不能确保用户收到的货物与本站展示的图片、产地、附件说明完全一致。", "isCShop":true, "jsdUrl":"//ssds.suning.com/ssds-web", "seoBreadCrumbName":"华为(HUAWEI)畅享9S手机", "faqDomain":"//faq.suning.com", "codUrl":"//smvas.suning.com", "feastActive":"0", "pgUrl":"//pin.m.suning.com/pgs/product", "pgDomain":"//pin.m.suning.com", "compareCatalog":"0", "luaPcSosFreight":"0", "specialSaleFlag":"0", "jubaoUrl":"//jubao.suning.com/sams/accuseIndex.action", "showJubao":"0", "jubaoID":"R0191004,R0501001,R0502001,R0503002,R0504001,R0506002,R0506003,R0508001,R0701002,R0702001,R0801001,R0801003,R0801004,R0801005,R0802002,R0901003,R0901004,R0902002,R1501001,R1501002,R1501005,R1502001,R1502003,R1505003,R1506001,R1506002,R1506003,R1506004,R1506006,R1506007,R1506009,R1506010,R1704002,R1901001,R4402005,R9000548,R9000549,R9000550,R9000551,R9000843,R9000845,R9000846,R9000847,R9000848,R9000849,R9000850,R9000851,R9000852,R9000853,R9000854,R9000855,R9000856,R9000857,R9000858,R9000859,R9000860,R9000861,R9000862,R9000863,R9000864,R9000865,R9000866,R9001146,R9001147,R9001148,R9001149,R9001150,R9001151,R9001152,R9001153,R9001154,R9001155,R9001156,R9001157,R9001158,R9001219,R9001220,R9001221,R9001222,R9001223,R9001224,R9001225,R9001226,R9001227,R9001228,R9001229,R9002112,R9002113,R9002114,R9002115,R9002116,R9002117,R9002118,R9002119,R9002120,R9002121,R9002122,R9002123,R9002124,R9002125,R9002126,R9002127,R9002128,R9002129,R9002130,R9002131,R9002132,R9002133,R9002134,R9002135,R9002136,R9002137,R9002138,R9002139,R9002140,R9002141,R9002142,R9002143,R9002144,R9002145,R9002146,R9002147,R9002148,R9002149,R9002150,R9002151,R9002152,R9002153,R9002154,R9002155,R9002156,R9002157,R9002158,R9002159,R9002160,R9002161,R9002162,R9002163,R9002164,R9002165,R9003434,R9003540,R9003559,R9004516,R9004517,R9004518,R9004519,R9004520,R9004521,R9004522,R9004523,R9004524,R9004525,R9004526,R9004527,R9006049,R9006050,R9006051,R9006052,R9006053,R9006054,R9006055,R9006056,R9006057,R9006058,R9008389,R9008390,R9008391,R9008392", "showZeroBuy":"0", "ccfsUrl":"//ccfs.suning.com", "gotoXiaoYi":"false", "autoUrl":"//auto.suning.com", "ppyunDomain":"player.pptvyun.com", "zyHwgFlag":"", "mountType":"", "vendor":"", "twoFlag":true, "tmOnlineId":"14266", "hwgOnlineId":"554312", "jiwuChatId":"", "phoneCategoryId":"20006", "cuxiaoSeq":{voucherTitle:1,lhvoucherTitle:2,isXYuanNItemTitle:3,taogouyhTitle:4,giftTitle:5,limitGifts:6,ordersGifts:7,jrPromTitle:8,purchaseTitle:9,couponTitle:10,newcouponTitle:11,yfbTitle:12,rxfTitle:13,scodeTitle:14,pointTitle:15,freightfreeTitle:16,govTitle:17,jnbtTitle:18}, "blackCategoryCode":"R9010501", "weight":"1.0", "isFresh":false, "scrapeCouponUrl":"//yzdh.suning.com", "scrapeCoupon":"0", "isSevenDayOkForTm":"true", "videoUrl":"http://m4.pptvyun.com/pvod/e11a0/DbCyWb50h1oSMYz1oT9DRKD1Pmk/eyJkbCI6MTU2MDY2NjAzNywiZXMiOjYwNDgwMCwiaWQiOiIwYTJkbjZ5ZHFhbWtuSzJMNEsyZG9hZmhvYU9lbjZtYnBxQSIsInYiOiIxLjAifQ/0a2dn6ydqamknK2L4K2doafhoaOen6mbpqA.mp4", "czyHwgFlag":"", "rxfDomain":"//rxf.suning.com", "sncfcDomain":"https://sncfc.suning.com", "overseasFAQ01":"", "yzCoupon":"1", "yunfeixianPC":"0", "pchdfk":"0", "supervipDomain":"//supervip.suning.com", "memberRemain":"0", "passportDomain":"https://loginst.suning.com", "newServiceLabel":"1", "tssUrl":"//tss.suning.com", "cpmAdDomain":"//th.suning.com", "suningJiWuFlag":false, "overseasFAQSwitch":"0", "cpmAdRequestCode":"pid=100003869&pid=100003866", "orderDomain":"//order.suning.com", "clothesFlag":"0", "zyxjLink":"//sbos.suning.com/inquiryIndex.do", "showMUrl":"//show.m.suning.com", "breadcrumbsShopSwitch":"1", "fristPic":"//imgservice.suning.cn/uimg1/b2c/image/783X00lIk6NabyNuOdOUbw.jpg", "gyFlag":false, "c2mFlag":false, "mainPicDynamicUrlSwitch":"1", "virtualFlag":false, "solsUrl":"//sols.suning.com", "realNameUrl":"//c.m.suning.com/smpc.htm?source=20&terminal=31", "businessFlag":"", "businessField":"", "snassUrl":"//snasss.suning.com", "plmsUrl":"//plmslabel.suning.cn", "spesUrl":"//spes.suning.com", "envName":"PROD", "goodShopLabelCode":"C00000023", "jumUrl":"//ju.suning.com", "supermarketCheck":"", "sntkUrl":"//sntk.suning.com", "sucLabel":"0", "classifyLabel":"1", "usedCarFlag":"", "usedCarPrice":"", "usedCarOriginalPrice":"", "czHwgFlag":"", /*0422号卡用券开关*/ "haokaYongQuanSwitch":"1", "payapiDomain":"//payapi.suning.com", "ftpgsDomain":"", "rentType":"", "dsmsUrl":"//dsms.suning.com", "entryPermissionCode":"015738", "subPrdType":"", "cpmDatasGroupCode":"pid=100004623" }; /*窄屏不展示右侧工具条*/ if (window.screen.width <= 1200) { sn.hasSidebar=false; } if(sn.catenIds == sn.donateID){ sn.donateFlag = true; }else{ sn.donateFlag = false; } if(sn.catenIds == sn.blackCategoryCode){ sn.blackVirFlag = true; }else{ sn.blackVirFlag = false; } sn.isPreBuy = "0"; var snga=snga||{}; var _wmmq =_wmmq||[]; var scmInfo = scmInfo||{ "superPointText":"SUPER会员享2%云钻返", "superPointLink":"//supervip.suning.com/snprime-web/toIndex.do", "luaShbzSyb":"00001,00002,00003,00013", "pcLoginFlag":"0", "pcGuideShop":"1", "solpprescriptionflag":"1", "qrCode":"扫一扫购买", "hanBackLink":"//help.suning.com/page/id-205.htm", "broadBandId":"R0111007", "yanbaoLink":"//issp.suning.com/extendIns/index.htm", "jnbtDetail":"北京用户购买同类首件商品，节能补贴最高800元（限电脑端、手机APP及手机网页版可享受）", "jnbtUrl":"//help.suning.com/page/id-648.htm", "searchurl":"//list.suning.com", "szytTooltip":"为您提供配送到家及预约上门安装的一体化服务", "szytUrl":"//help.suning.com/page/id-463.htm", "yzDuoBei":"ACT105000030", "yzManFan":"ACT105000040", "newfreenessPay":"1", "luaHdfkDesc":"支持送货后再付款，支持刷卡、现金等支付方式", "pcJsdTitle":"下单成功后，2小时内为您急速送达", "fixParamAwardText":"请输入，采纳有机会获得10元或20元无敌券", "ffMemberSwitch":"0", "ffMemberMsgSwitch":"0", "pcAfterSalesServiceUrl":"//sale.suning.com/shfw/fuwuliucheng/index.html", "pcAfterSalesServiceText":"根据实际服务场景的不同，服务过程中可能会用到材料，服务人员会提前告知材料收费标准，经同意后使用，所用材料需收取相应费用。", "pcbigPolyInfo":"1", "pcAfterSalesServiceFlag":"1", "noProductPackage":"0", "minStartSaleNumSwitch":"1", "afterSalePicSwitch":"1", "pcAbleCouponsFlag":"1", "pcJrPromotionSwitch":"0", "cpmAdShowSwitch":"1", "sendUrlToDsa":"0", "pcYunZuanSwitch":"1", "mainPicDynamicUrlSwitch":"1", "alwaysBuyFlag":"1", "bestQuanUseFlag":"1", "pcNoGoodsPopBox":"00001,00002,00013,00007,00003,00004,00006,00005,00015,00016,00020,00025,00027,00029,00031,00019", "recommendPic":"1", "pcCityFlag":"1", "downgrade":"1", "superYunZuan":"加入会员返云钻，下单立返约yuan元", "cShopYanBaoSwitch":"1", "motherBabyCode": "00019", "motherBobyChannelId": "554312", "onlineCustomerSwitch":"1", "installFeesSwitch": "1", "preBuyLinkWindowSwitch": "1", "superVipYunZuan": "您可享2%返利，预计返价值yuan元云钻", "commSuperVipDisplay": "现在开通SUPER VIP立享会员价", "rxfDiscountSwitch": "1", "cardCitySwitch": "1", "salesRemindSwitch": "1", "hideSuperYzItem": "000010691|0010127993", "shopAllowanceSwitch": "1", "shopAllowanceRedPacket": "购物补贴", "icpsQueryGiftSwitch": "1", "autoPlaySwitch": "1", "pcAnswerSwitch": "1", "getGuideDoctSwitch":"1", "cShopBaoxianSwitch":"1", "pcTmActivitySwitch":"1", "QRcodeSwitch":"1", "qrBizCode":"i9seHn", "qrBookBizCode":"", "shopAllowanceRuleLinkText":"", "shopAllowanceRedPacketLinkSwitch":"1", "finalPriceSwitch":"1", "simSuningChannelId":"13952", "solp10302Switch":"1", "limitBuycountSwitch":"1", "recommendSwitch":"", "finalPriceBookSwitch":"1", "bigPolyMoreUrl":"//qiang.suning.com", "installServiceDisplaySwitch":"1", "installServiceTVCatenIds":"R0503002", "installServiceKTCatenIds":"R0105002|R0104002|R0105001|R0104001|R3501001|R3501002|R3501005|R3502001|R3502002|R3502006|R3502003", "installServiceTVParamVal":"008040", "installServiceKTParamVal":"010877", "luaWxslCategoryCode":"R9015846", "snqgSaleNum":"300", "snqgPriceSwitch":"1", "cpmDatasGroupSwitch":"1", "greatPriceRefreshSwitch":"0", "c2mSwitch":"1", "preBuyAddCartSwitch":"1", "recommendADSwitch":"1", "newRxfSwitch":"1", "cShopBookServiceShow":"0", "zyBookServiceShow":"1", "limitBuyTextSwitch":"1", "shopScoreInfoSwitch":"1", "carLoanSwitch":"0", "carInsureSwitch":"1", "itemYesSwitch":"", "suningCardCustPriceSwitch":"1" }; var funcDesc = { "weightHiddenBizIds":"00002,00003,00013", "weightDisplayText":"此重量为商品毛重：指商品本身的重量（净含量）加上包装容器或包装物的重量之和。仅用于计算运费", "pcYanbaoTip":"在苏宁购买商品可享受的增值售后服务，包含厂家质保期内意外保障服务、厂家质保期结束后的延长保修服务以及商品换新服务等全程保障服务业务。", "SGMWCatenIds":"R9013945" }; /*五菱汽车标识*/ sn.isSGMW = false; ; sn.review = { "vendorCode":"0070094634", "clusterId":"30357178" }; /*右侧工具条样式重置*/ var SnSidebar_config={ feedbackHref:"//ued.suning.com/survey/view/xinbansijiye" }; if(sn.prdType == "S"){ /*商品通子码关系*/ var passFlag = '0'; var gProduct = gProduct ||{ "gors":"",/*0 通 1子*/ "gType":"0", "gInfo":"", "itemSubCount":"" }; sn.pageFlag=1; gProduct.gors = parseInt(passFlag)-1; sn.passPartNumber = '000000010985347748'; if(gProduct.gors ==1){ sn.tempPartNumber = sn.partNumber; }else{ sn.tempPartNumber = ''; } gProduct.reviewPartNum = sn.partNumber; if(gProduct.gors=='1'){/*子码*/ gProduct.reviewPartNum = sn.partNumber; }else if(gProduct.itemSubCount!=undefined){ gProduct.reviewPartNum = gProduct.itemSubCount.partNumber; } } var snqa = snqa ||{ "category3":"" }; sn.o2oFlag = false; function errorMainPicture(obj,flag){ $(obj).attr('src',sn.amPdsRelation+'images/blank_pic_60.png'); if(!flag){ $(obj).attr('src-medium',sn.amPdsRelation+'images/blank_pic_800.jpg'); } $(obj).attr('src-large',sn.amPdsRelation+'images/blank_pic_800.jpg'); } </script><link rel="shortcut icon" href="//www.suning.com/favicon.ico" type="image/x-icon"/>
<link rel="stylesheet" href="//res.suning.cn/public/v3/css/??v3common.min.css,search.min.css,sn-sidebar.min.css?v=2019071101"/>
<script type="text/javascript" src="//res.suning.cn??/public/v3/js/jquery.js,/public/v3/js/sn_lazyload.js,/public/v3/js/lazyelem.min.js,/public/v3/js/SFE.base.min.js,/public/v3/js/search.min.js,/public/sidebar/build/js/sn-sidebar.min.js,/project/yunxin/js/chatCompat_mini.js?v=2019071101"></script>
<meta content="true" name="autoclick">
<meta content="d488778a" name="siteid">
<!--[if IE 6]>
<script type="text/javascript" src="//res.suning.cn/public/js/DD_belatedPNG.js"></script>
<![endif]-->
<!-- [[SHTS资源2015年4月9日21:56:29 -->
<!--<link rel="stylesheet" type="text/css" href="//resource.sop.suning.cn/shts/resource/sn_widget/css/common.widget.css?v=20190717150028">-->
<!-- ]]SHTS资源2015年4月9日21:56:29 -->
<link rel="stylesheet" type="text/css" href="//resource.sop.suning.cn/shts/resource/SN_T_1001/default/assets/css/snt1001.min.css?v=20190717150028">
<link rel="stylesheet" href="//resource.sop.suning.cn/resource/sfs/project/shopv2/c/common/css/sf.shop.min.css?v=20190717150028" type="text/css"/>
<link rel="stylesheet" href="//resource.sop.suning.cn/resource/sfs/project/shopv2/common/css/shop-modules.css?v=20190717150028" type="text/css"/>
<script>
//sn上下文
var sn = $.extend(
sn || {},
{
config : {
picDomian : '//image.suning.cn/uimg/cshop/logo/',//图片空间域名
pimgDomain : 'image.suning.cn,image1.suning.cn,image2.suning.cn,image3.suning.cn,image4.suning.cn,image5.suning.cn',//商品图片地址域名
priceDomain : 'price1.suning.cn;price2.suning.cn',//价格图片地址域名
detailDomain : '//product.suning.com/',//商品四级页地址域名
searchDomain : "//csearch.suning.com/emall/cshop/",//搜索域名
header_search : "//search.suning.com/",//头部搜索地址
cart : "//shopping.suning.com/cart.do",//购物车地址
icpsDomain : '//icps.suning.com/',//价格中心地址
sfs_ds_domain : '//ds.suning.cn/',//主站搜索ds系统域名
sfs_spes_domain : '//spes.suning.com/',//促销标签spes系统域名
pimgRule:'//resource.sop.suning.cn/resource/webstatic/common/images/goods.png?spcode={spcode}&pcode={pcode}&pscode={pscode}&pictype=0&location=1&picsize={picSize}x{picSize}&v={versionNum}'//商品动图拼接规则
},
env : 'prod',//环境名称
ds_resource_context : '//resource.sop.suning.cn/resource/sfs',//设计师静态资源上下文
rversion : '?v=20190717150028',
shop : {
item_place_holder : '//resource.sop.suning.cn/resource/sfs/project/shopv2/common/images/item_place_holder.png?v=20190717150028',//商品占位图片
search : "search",//搜索
context : '//shop.suning.com/',//展示上下文
spcode : "70094634",
shopId : "70094634",
domain : "//shop.suning.com/70094634/index.html",
shopDomain : "//shop.suning.com/",//店铺域名 http://domain.suning.com
shopContext : "//shop.suning.com/70094634/",//http://shop.suning.com/1234578/
shopType : "0"
},
qr_service_config:{
"biz.waphk.item" : "i9kfG0",
"service_url" : "//code.suning.cn/pc/build.do?longUrl=%s&bizCode=%s",
"biz.waphk.shop" : "i9kfFo",
"biz.wap.shop" : "i9kfFe",
"biz.wap.mqs" : "i9kfFx",
"biz.wap.item" : "i9kfFP",
"biz.pc.qs" : "i9kfFD"
}
}
);
</script><script>
var sn = sn || {};
//页面属性
sn.page = {
pageType : 'header'
};
</script>
<div id="_TOP_BANNER_" class="ng-top-banner"></div>
<div class="ng-toolbar">
<div class="ng-toolbar-con wrapper">
<div class="ng-toolbar-left">
<a href="//www.suning.com" class="ng-bar-node ng-bar-node-backhome" id="ng-bar-node-backhome" name="public0_none_gongju_fanhui" sap-modid="pyiw5">
<i class="ng-iconfont ng-backhome">&#xe640;</i><span>返回首页</span>
</a>
<script type="text/javascript">
if (!sn.isHome){document.getElementById('ng-bar-node-backhome').style.display = "block";};
</script>
<div class="ng-bar-node-box ng-site-nav-box lazy-bar-box" sap-modid="sTMJP">
<a href="javascript:void(0);" class="ng-bar-node ng-bar-node-site" name="public0_none_daohang_wzdh">
<span>网站导航</span><em class="ng-iconfont down">&#xe62e;</em>
</a>
<div class="ng-sn-site-nav ng-d-box site-nav-child" style="display:none;">
<!--网站导航列表-->
<div class="head-loading"></div>
<a href="javascript:void(0);" class="ng-close" name="public0_none_daohang_close"><em class="ng-iconfont">&#xe627;</em></a>
</div>
</div>
<div class="ng-bar-node-box shop-handle lazy-bar-box" sap-modid="yj2Q">
<a href="https://sop.suning.com" class="ng-bar-node ng-bar-node-pr5 ng-bar-node-shop touch-href" name="public0_none_shangjia_ruzhu" target="_blank"><span>商家入驻</span><em class="ng-iconfont down">&#xe62e;</em></a>
<div class="ng-down-box ng-d-box shop-center-child ng-ser-list" style="display:none;">
<!--商家入驻列表-->
<div class="head-loading"></div>
</div>
</div>
<!--服务中心 [[-->
<div class="ng-bar-node-box service-handle lazy-bar-box" sap-modid="Fgfr4">
<a href="javascript:void(0);" class="ng-bar-node ng-bar-node-service ng-bar-node-fix touch-href ng-bar-node-pr5" rel="nofollow" name="public0_none_kehu_fuwu"><span>客户服务</span><em class="ng-iconfont down">&#xe62e;</em>
</a>
<div class="ng-down-box ng-d-box service-center-child ng-ser-list" style="display:none;">
<!--服务中心列表-->
<div class="head-loading"></div>
<a href="javascript:navIndex();" rel="nofollow" name="public0_none_kehu_zixun" style="display:none;"><span>在线咨询</span><em class="ng-iconfont">&#xe631;</em></a>
</div>
</div>
<!--服务中心 ]]-->
<!--网站导航 ]]-->
<!-- 消息 [[ -->
<!-- <div class="ng-bar-node-box ng-msg-box">
<a href="//msg.suning.com/" class="ng-bar-node ng-bar-node-msg" name="public0_none_dbgjt_wdxx01" target="_blank">
<span>消息<i class="ng-iconfont dot"></i></span><em class="ng-iconfont down">&#xe62e;</em>
</a>
<div class="ng-d-box ng-msg-child" style="display:none;">
<div class="ng-msg-list">
<div class="ng-msg-item ng-msg-item-no">
<i></i><span>嗷~ 没有新消息...</span>
</div>
</div>
<div class="ng-msg-bottom"><a href="//msg.suning.com/" name="public0_none_dbgjt_wdxx01" target="_blank">查看更多</a></div>
</div>
</div> -->
<!-- 消息 ]] -->
</div>
<div class="ng-toolbar-right">
<!-- 登录注册 -->
<a href="javascript:void(0)" class="ng-bar-node username-bar-node username-bar-node-showside" id="username-node" rel="nofollow" style="display:none;">
<span id="usernameHtml01"></span>
<em class="hasmsg ng-iconfont">&#xe637;</em>
</a>
<div class="ng-bar-node-box username-handle" id="username-node-slide" style="display:none;" sap-modid="AVsm">
<a href="//my.suning.com" rel="nofollow" class="ng-bar-node username-bar-node username-bar-node-noside">
<span id="usernameHtml02"></span>
<em class="hasmsg ng-iconfont">&#xe637;</em>
<em class="ng-iconfont down">&#xe62e;</em>
</a>
<div class="ng-d-box ng-down-box ng-username-slide" style="display:none;">
<a href="//my.suning.com/person.do" class="ng-vip-union" target="_blank" name="public0_none_denglu_zhanghao" rel="nofollow">账号管理</a>
<a href="javascript:SFE.base.logoff();" rel="nofollow" name="public0_none_denglu_tuichu">退出登录</a>
</div>
</div>
<div class="ng-bar-node reg-bar-node" id="reg-bar-node" sap-modid="dYp4">
<a href="javascript:SFE.base.logonurl();" name="public0_none_denglu_denglu" rel="nofollow" class="login">请登录</a>
<a href="https://reg.suning.com/person.do" target="_blank" class="login reg-bbb" rel="nofollow" name="public0_none_denglu_zhuce">注册有礼</a>
</div>
<script type="text/javascript">
var stripscript = function(s){
var pattern = new RegExp("[<>]")
var rs = "";
for (var i = 0; i < s.length; i++) {
rs = rs+s.substr(i, 1).replace(pattern, '');
}
return rs;
}
function d(b) {
var a;
return (a = document.cookie.match(RegExp("(^| )" + b + "=([^;]*)(;|$)"))) ?stripscript(decodeURIComponent(a[2].replace(/\+/g, "%20"))) : null
};
var uernameA = d("logonStatus");
var usernameNode = document.getElementById('username-node');
var usernameNodeSlide = document.getElementById('username-node-slide');
var usernameHtml01 = document.getElementById('usernameHtml01') , usernameHtml02 = document.getElementById('usernameHtml02');
var regBarNode = document.getElementById('reg-bar-node');
if (uernameA != null && uernameA != "") {
var uernameC = d("nick");
// if( ((window.sidebar_config && sidebar_config.enable)||sn.hasSidebar) && !sn.hasNewSidebar ){
// usernameNode.style.display = "block";
// }else{
usernameNodeSlide.style.display = "block";
//}
usernameHtml01.innerHTML = uernameC;
usernameHtml02.innerHTML = uernameC;
regBarNode.style.display = "none";
}else{
usernameNode.style.display = "none";
usernameNodeSlide.style.display = "none";
usernameHtml01.innerHTML = " ";
usernameHtml02.innerHTML = " ";
regBarNode.style.display = "block";
}
</script>
<!--我的订单 [[-->
<div class="ng-bar-node-box myorder-handle" sap-modid="Ygnh">
<a href="//order.suning.com/order/orderList.do" rel="nofollow" name="public0_none_wode_dingdan" class="ng-bar-node ng-bar-node-fix touch-href ng-bar-node-pr5"><span>我的订单</span><em class="ng-iconfont down">&#xe62e;</em></a>
<div class="ng-down-box ng-d-box myorder-child" style="display:none;">
<a href="//order.suning.com/order/orderList.do?transStatus=waitPay" rel="nofollow" name="public0_none_wode_zhufu">待支付<em id="waitPayCounts"></em></a>
<a href="//order.suning.com/order/orderList.do?transStatus=waitReceive" rel="nofollow" name="public0_none_wode_shouhuo">待收货<em id="waitDeliveryCounts"></em></a>
<a href="//review.suning.com/my_cmmdty_review.do" rel="nofollow" name="public0_none_wode_pingjia">待评价<em id="waitEvaluation"></em></a>
<a href="//snasss.suning.com/snass-web/pc/modify/toModifyOrderList.do" rel="nofollow" name="public0_none_wode_xiugai">修改订单</a>
</div>
</div>
<!--我的订单 ]]-->
<!--我的易购 [[-->
<div class="ng-bar-node-box mysuning-handle" sap-modid="P5ptt">
<a href="//my.suning.com" rel="nofollow" name="public0_none_wode_yigou" class="ng-bar-node ng-bar-node-fix touch-href ng-bar-node-pr5"><span>我的易购</span><em class="ng-iconfont down">&#xe62e;</em></a>
<div class="ng-down-box ng-d-box mysuning-child" style="display:none;">
<div class="mysuning-infor clearfix">
<a name="public0_none_wode_touxiang" target="_blank" href="//my.suning.com/person.do?targetTab=head" class="headimg"><img src3="//image.suning.cn/uimg/cmf/cust_headpic/0000000000_01_60x60.jpg" alt="" id="userHead" /></a>
<div class="mysuning-detail">
<a name="public0_none_denglu_denglu" href="javascript:SFE.base.logonurl();" class="login" >请登录</a>
<a name="public0_none_wode_name" href="//my.suning.com" rel="nofollow" class="username" id="userNickname"></a>
</div>
</div>
<a href="//2.suning.com/myOrder/queryMyOrders.do" name="public0_none_wode_ershou" rel="nofollow" target="_blank">我的二手</a>
<a href="//favorite.suning.com/myFavoriteImg.do" rel="nofollow" name="public0_none_wode_shoucang" target="_blank">我的关注</a>
<a href="https://passport.suning.com/ids/trustLogin?sysCode=epp&targetUrl=http://my.jr.suning.com/sfp/accountAssets/index.htm" rel="nofollow" name="public0_none_wode_jinrong" target="_blank">我的金融</a>
<a href="//vip.suning.com" class="ng-vip-union" target="_blank" rel="nofollow" name="public0_none_wode_huiyuan">苏宁会员<em class="ng-iconfont">&#xe6ac;</em></a>
<a href="https://rxf.suning.com/epps-cpf/accountMgt/assetOverview.do" rel="nofollow" name="public0_none_wode_renxingfu">我的任性付</a>
<a href="//quan.suning.com/yhq.do" rel="nofollow" name="public0_none_wode_quan">我的优惠券</a>
</div>
</div>
<!--我的易购 ]]-->
<a href="//vip.suning.com/" name="public0_none_sn_huiyuan" rel="nofollow" class="ng-bar-node ng-bar-node-pr5" target="_blank" sap-modid="lAi5"><span>苏宁会员</span></a>
<!--[[ 购物车 2017-06-08 添加购物车商品 -->
<div class="ng-bar-node-box cart-handle" sap-modid="lQl9p">
<a class="ng-bar-node ng-bar-node-mini-cart " name="public0_none_gouwuche_gwc" rel="nofollow" href="//shopping.suning.com/cart.do">
<em class="ng-iconfont cart">&#xe623;</em><span>购物车</span>
<span class="total-num-box" id="J_total_num_box">
<b class="total-num J_cart_total_num" id="showTotalQty">0</b>
<span class="total-num-bg-box">
<em></em>
<i></i>
</span>
</span>
<em class="ng-iconfont down">&#xe62e;</em>
</a>
<div class="ng-down-box ng-d-box cart-child" style="display:none;"><!-- -->
<div class="cart-box">
</div>
<div class="cart-loading"><p class="loading-content">加载中...</p></div>
</div>
<script type="text/javascript">
var ngCartNum = d("totalProdQty");
ngCartNum = ( ngCartNum ==0 || ngCartNum == null )?0:ngCartNum;
ngCartNum = parseInt(ngCartNum);
ngCartNum = ngCartNum>99?'99+':ngCartNum;
document.getElementById('showTotalQty').innerHTML = ngCartNum;
</script>
</div>
<!-- 购物车 ]] -->
<a href="https://passport.suning.com/ids/trustLogin?sysCode=epp&agentType=pc&targetUrl=https://pay.suning.com/epp-epw/login/login.action" name="public0_none_yifubao_yfb" class="ng-bar-node ng-bar-node-pr5" target="_blank" sap-modid="KdRR"><span>易付宝</span></a>
<a href="//b.suning.com/" class="ng-bar-node ng-bar-node-pr5" name="public0_none_qiye_caigou" target="_blank" sap-modid="TJwSg"><span>企业采购</span></a>
<!--手机苏宁 [[-->
<div class="ng-bar-node-box app-down-box" sap-modid="3D1su">
<a href="//cuxiao.suning.com/newUser.html" target="_blank" name="public0_none_shouji_sn" rel="nofollow" class="ng-bar-node mb-suning touch-href"><span>手机苏宁</span><em class="ng-iconfont down">&#xe62e;</em></a>
<div class="ng-mb-box ng-d-box mb-down-child" style="display:none;">
<ul class="ng-app-code">
<li>
<img class="top-code" src3="//res.suning.cn/public/v3/images/sntk-top-code.png?var=01" alt="苏宁易购APP"/>
<p>关注苏宁推客公众号</p>
<p>自购省钱·分享赚钱</p>
</li>
<li>
<img class="top-code" src3="//res.suning.cn/public/v3/images/yfb-top-code.png?var=01" alt="易付宝APP"/>
<p>扫一扫</p>
<p>下载苏宁金融APP</p>
</li>
<li>
<img class="top-code" src3="//res.suning.cn/public/v3/images/app-code.jpg?var=01" alt="易购服务号"/>
<p>扫一扫</p>
<p>关注苏宁易购服务号</p>
</li>
</ul>
<div class="line"></div>
<div class="line lineTwo"></div>
</div>
</div>
<!--手机苏宁 ]]-->
</div>
<div id="ng-minicart-slide-box"></div>
</div>
</div>
<div class="g-header-wrapper">
<div class="g-header ">
<div class="wrapper">
<div class="g-search" style="z-index: 3;">
<form method="get">
<div class="search-inner clearfix">
<span class="left-sidebar"></span>
<input tabindex="0" id="searchKeywords" type="text" class="search-keyword search-keyword-yg" value="" autocomplete="off">
<input sa-uv="head_searcha" id="searchEbuySubmit" type="button" class="search-btn" value="搜易购" style="padding:0px;letter-spacing: 0px;">
<input sa-uv="head_searchs" id="searchShopSubmit" type="button" class="search-btn searchstore-btn" value="搜本店" style="padding:0px;letter-spacing: 0px;">
<span class="right-sidebar"></span>
</div>
<div class="g-search-hotwords">
</div>
<div id="snKeywordNew" style="display:none">
</div>
</form>
<div id="ac_results" class="g-ac-results hide"></div>
</div>
<div class="g-logo" id="G_SUNING_LOGO">
<!-- LOGO -->
<a href="http://www.suning.com" class="ng-logo">
<img src="//res.suning.cn/public/v3/images/logo/snlogo.png?v=2015042703" height="100" width="190" alt="苏宁易购"/>
</a>
</div>
<div class="storname">
<div class="JS_storename changeh3 shop-icon" style="overflow:inherit">
<i><a id="chead_indexUrl" href="//shop.suning.com/70094634/index.html" title="华科手机专营店"><strong>华科手机专营店</strong></a></i>
<!--<a href="javascript:void(0);" class="icon_exp" title="支持门店试穿服务" style="display:none;" id="guideShopLogo">体验店</a>-->
<!--<a href="javascript:void(0);" class="icon_exp" title="广东馆" style="display:none;" id="gdShopMark">体验店</a> -->
<span class="icon_ic" id="gdShopSpan"><i title="" id="gdShopMark"></i></span>
</div>
<div class="bd clearfix">
<div class="JS_store_grade store-grade">
<h4 id="chead_road" class="bg-none shop-star-h4">
<span>服务体验</span>
<em class="shop-star-em">
<div class="shop-start-box">
</div>
<img id="chead_roadPic" src="//resource.sop.suning.cn/resource/sfs/project/shopv2/common/css/images/juhua.gif" />
</em>
</h4>
<div class="sg-details">
<div class="clearfix">
<div class="com-grade">
<div class="hd clearfix"><span class="l">店铺评分</span><span class="r">与同行业相比</span></div>
<p><span id="chead_qualityStar">用户评价：--</span><span class="shop-star-percent" id="chead_qualityPercent"><em class="percent-orange">--</em></span></p>
<p><span id="chead_attitudeStar">物流时效：--</span><span class="shop-star-percent" id="chead_attitudePercent"><em class="percent-orange">--</em></span></p>
<p><span id="chead_deliverySpeedStar">售后服务：--</span><span class="shop-star-percent" id="chead_deliverySpeedPercent"><em class="percent-orange">--</em></span></p>
</div>
<div class="store-logo" id="chead_logoUrl"><img src="//resource.sop.suning.cn/resource/sfs/project/shopv2/common/css/images/img_shop.png" /></div>
</div>
<ul class="store_contact">
<li style="display:none;" id="id_qual_li">
<span class="dt">行业资质：</span>
<span class="dd JS_txtCtrl">
<a id="chead_qualification" href="javascript:void(0)" class="chead_qualification" target="_blank"></a>
</span>
</li>
<li>
<span class="dt">服务承诺：</span>
<span class="dd">
<i class="zp">正品保障</i>
</span>
</li>
<li><span class="dt">公司名称：</span><span class="dd JS_txtCtrl"><i id="chead_companyName"></i><a id="chead_licence" href="javascript:void(0)" class="com_licence" target="_blank"></a></span></li>
<li><span class="dt">所 在 地：</span><span class="dd JS_txtCtrl"><i id="chead_companyAddress"></i></span></li>
<li><span class="dt">客服电话：</span><span class="dd" id="chead_telPhone"></span></li>
</ul>
<div class="h-exp clearfix" style="display:none;" id = "guidShopLogoPlay"><a href="javascript:void(0);" class="btn-exp JS-nearby-store" title="身边门店" style="display:none;" id="guideShopLogo">体验店</a></div>
<!--<a href="javascript:void(0);" class="icon_exp" title="广东馆" style="display:none;" id="gdShopMark">体验店</a> -->
<!--<span class="icon_ic" id="gdShopSpan"><i title="南京青奥馆" id="gdShopMark">南京青奥馆</i></span>-->
<div class="ft clearfix">
<a id="chead_shopIndexUrl" sa-uv="head_in" href="//shop.suning.com/70094634/index.html" class="btn btn_home">进入店铺</a>
<a href="javascript:void(0)" sa-uv="head_col" class="btn btn_collect" id="storeShop3" name="SHOP_70094634_XXTT_SCAN">关注店铺</a>
<a href="//shop.suning.com/70094634/all.html" sa-uv="head_map" class="btn btn_good">商品地图</a>
</div>
</div>
</div>
<a class="online-sale" href="javascript:void(0)" id="onlineService1" sa-uv="header_online" ignore-page="true">
</a>
<a href="javascript:void(0);" class="JS-nearby-store nearby_store" style="display:none;" id="guideShopAround">身边门店</a>
</div>
</div>
<div class="JS-sf-trytoShop" style="display: none;">
<div class="sf-trytoShop">
<dl class="sf-area clearfix">
<dt>区域：</dt>
<dd class="districtContainer">
<a href="#" pguide-area="null">全部</a>
</dd>
</dl>
<div class="sf-shopadd">
<table class="sf-table">
<tbody class="storeListContainer">
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<script type="text/javascript">
$(function () {
$("[sf-evacuation-logo]").hover(function () {
$("[sf-evacuation-content]").show();
}, function () {
$("[sf-evacuation-content]").hide();
});
});
</script><div class="sf-sortbox sf-noDrag sf-autoWidth suning-show-mode">
<!-- all rights shop resolve -->
<link rel="stylesheet" type="text/css" href="//resource.sop.suning.cn/shts/resource/sn_widget/css/common.widget.css"/> <link rel="stylesheet" type="text/css" href="//resource.sop.suning.cn/shts/tpl/ds/9550323ac8184837aed21d057a0c8513/cf49c95976d743a99abce3b91a5db09d/assets/css/common.css"/> <link rel="stylesheet" type="text/css" href="//resource.sop.suning.cn/shts/tpl/ds/9550323ac8184837aed21d057a0c8513/cf49c95976d743a99abce3b91a5db09d/assets/css/common1.css"/> <link rel="stylesheet" type="text/css" href="//resource.sop.suning.cn/shts/tpl/ds/9550323ac8184837aed21d057a0c8513/cf49c95976d743a99abce3b91a5db09d/assets/css/skin/skin01.css"/>
<!-- [[head-->
<div class="sf-layoutList JS-head " layoutId="11970747"> <div class="sf-module990 " pointX="F" moduleStyle="990">
<!-- [[LAYOUT-F-->
<!-- [module][14812633][f8459d687084497587ac2a4f5eddba04]-->
<div class="sf-moduleList sf-noPadding" moduleId="14812633" moduleType=""> <style> .ng-footer{margin-top:0;} .qr-code{display:block;} </style> <style> .ds-navbar{background:#090547;} .ds-navbar .sf-navlist li a:hover{background:#f00202;} .ds-navbar .sf-allcate{background:#ee0505; } .ds-navbar .sf-allcate dd ul a{background:#000000} .ds-navbar .sf-allcate dd ul li{border-color:#ffffff;} .ds-navbar .sf-allcate dd ul a:hover, .ds-navbar .sf-allcate dd ul a.sf-sel, .ds-navbar .sf-allcate li.sf-moreList, .ds-navbar .sf-allcate li.sf-moreList a{background:#f9f9f9;} .ds-navbar .sf-allcate li.sf-moreList, .ds-navbar .sf-allcate li.sf-moreList a{border-color:#000000;} .ds-navbar .sf-allcate li.sf-moreList a:hover{background: #f00404;} .ds-navbar .ds-search{display:none;} .sf-allcate dt,.sf-navlist li a,.ds-navbar .sf-allcate dd ul a{color:#ffffff;} </style> <div class="ds-dianzhao ds-bg" style=" "> <div style="height:648px;" class="jg_tools_code">
<div class="sn-simple-logo jgabs" style="position:absolute;width:100%;height:648px;border:none;padding:0;top:auto;left:auto;">
<div class="sn-simple-logo jgabs" style="position:absolute;width:1883px;height:648px;top:auto;border:none;padding:0;">
<div class="jg_one sn-simple-logo jgabs" style="position:absolute;height:auto;width:auto;line-height:auto;margin:0;height:648px;width:1883px;top:auto;left:0px;padding:0px;">
<div style="background-color:transparent;background-repeat:no-repeat;background-attachment:scroll;background-position:center center;height:648px;width:1883px;position: relative;">
<div class="sn-simple-logo jgabs" style="position:absolute;height:auto;width:auto;line-height:auto;margin:0;left:1476px;top:1px;width:246px;height:120px;z-index:7;">
<a href="https://product.suning.com/0070094634/11221635695.html?safp=d488778a.10190700.0.62056f752e&safc=prd.0.0" target="_blank" style="display: block;font-size: 0;">
<img src="//resource.sop.suning.cn/shts/ds/editor/3372624df78a454d8f50502e78255ec5/images/2db4c330b0c646c6a607ab4e049234f3.gif" alt="" width="0" height="120" />
</a>
</div><div class="sn-simple-logo jgabs" style="position:absolute;height:auto;width:auto;line-height:auto;margin:0;left:1204px;top:-3px;width:273px;height:121px;z-index:7;">
<a href="https://product.suning.com/0070094634/11197493276.html?safp=d488778a.10190700.0.62056f752e&safc=prd.0.0" target="_blank" style="display: block;font-size: 0;">
<img src="//resource.sop.suning.cn/shts/ds/editor/3372624df78a454d8f50502e78255ec5/images/2db4c330b0c646c6a607ab4e049234f3.gif" alt="" width="0" height="121" />
</a>
</div><div class="sn-simple-logo jgabs" style="position:absolute;height:auto;width:auto;line-height:auto;margin:0;left:942px;top:0px;width:258px;height:119px;z-index:7;">
<a href="https://product.suning.com/0070094634/11142333796.html?safp=d488778a.10190700.0.62056f752e&safc=prd.0.0" target="_blank" style="display: block;font-size: 0;">
<img src="//resource.sop.suning.cn/shts/ds/editor/3372624df78a454d8f50502e78255ec5/images/2db4c330b0c646c6a607ab4e049234f3.gif" alt="" width="0" height="119" />
</a>
</div><div class="sn-simple-logo jgabs" style="position:absolute;height:auto;width:auto;line-height:auto;margin:0;left:675px;top:2px;width:264px;height:120px;z-index:7;">
<a href="https://product.suning.com/0070094634/10989627017.html?safp=d488778a.10190700.0.62056f752e&safc=prd.0.0" target="_blank" style="display: block;font-size: 0;">
<img src="//resource.sop.suning.cn/shts/ds/editor/3372624df78a454d8f50502e78255ec5/images/2db4
c330b0c646c6a607ab4e049234f3.gif" alt="" width="0" height="120" />
</a>
</div><div class="sn-simple-logo jgabs" style="position:absolute;height:auto;width:auto;line-height:auto;margin:0;left:410px;top:2px;width:262px;height:119px;z-index:7;">
<a href="https://product.suning.com/0070094634/10620428144.html?safp=d488778a.10190700.0.62056f752e&safc=prd.0.0" target="_blank" style="display: block;font-size: 0;">
<img src="//resource.sop.suning.cn/shts/ds/editor/3372624df78a454d8f50502e78255ec5/images/2db4c330b0c646c6a607ab4e049234f3.gif" alt="" width="0" height="119" />
</a>
</div><div class="sn-simple-logo jgabs" style="position:absolute;height:auto;width:auto;line-height:auto;margin:0;left:197px;top:-1px;width:197px;height:120px;z-index:7;">
<a href="https://shds.suning.com/shds-web/positiveNew/page/deco/previewIndex.action?pageId=10190699#" target="_blank" style="display: block;font-size: 0;">
<img src="//resource.sop.suning.cn/shts/ds/editor/3372624df78a454d8f50502e78255ec5/images/2db4c330b0c646c6a607ab4e049234f3.gif" alt="" width="0" height="120" />
</a>
</div><div class="img_0_55127000_1563518706 sn-simple-logo jgabs" style="position:absolute;height:auto;width:auto;line-height:auto;margin:0;overflow:hidden;display:block;background:url(https://uimgproxy.suning.cn/uimg1/sop/commodity/1orRzH-U_1JnOpE0xDFKQQ.jpg) no-repeat;left:0px;top:0px;width:1920px;height:120px;z-index:3;">
<img src="//resource.sop.suning.cn/shts/ds/editor/3372624df78a454d8f50502e78255ec5/images/2db4c330b0c646c6a607ab4e049234f3.gif"
style="width:0;height:120px;">
</div>
</div>
</div>
</div>
</div>
</div> </div> </div>
<!-- [module][14812634][d4f1259eb2b54be7848a1e3fa9bda316]-->
<div class="sf-moduleList sf-noPadding" moduleId="14812634" moduleType="" style="margin-bottom:0;"> <div class="sf-navbar ds-navbar clearfix"> <div class="ds-body"> <dl class="sf-allcate"> <dt><span>本店所有商品</span></dt> <dd> <ul class="sf-subnav" sf-category="{ctype:'1'}"> <li class="sf-it"> <a href="javascript:void(0);" sf-category-all sa-uv="nav_all" class="sf-more" moreData="[{txt:'按销量','sf-sort':'totalCount-desc','sa-uv':'nav_sales'},{txt: '按新品','sf-sort':'createTime-desc','sa-uv':'nav_new'},{txt: '按价格', 'sf-sort':'price-asc','sa-uv':'nav_price'}]">所有商品</a> </li> <li class="sf-it"><a href="javascript:void(0);" class="sf-more" sf-category-item="210465552" moreData="[]" >苹果(Apple)</a></li> <li class="sf-it"><a href="javascript:void(0);" class="sf-more" sf-category-item="200137170" moreData="[]" >华为（HUAWEI）</a></li> <li class="sf-it"><a href="javascript:void(0);" class="sf-more" sf-category-item="210175477" moreData="[]" >荣耀(honor)</a></li> <li class="sf-it"><a href="javascript:void(0);" class="sf-more" sf-category-item="200142000" moreData="[]" >小米(mi)</a></li> <li class="sf-it"><a href="javascript:void(0);" class="sf-more" sf-category-item="200212346" moreData="[]" >魅族(MEIZU)</a></li> <li class="sf-it"><a href="javascript:void(0);" class="sf-more" sf-category-item="210471236" moreData="[]" >诺基亚(NOKIA)</a></li> <li class="sf-it"><a href="javascript:void(0);" class="sf-more" sf-category-item="210602609" moreData="[]" >一加</a></li> <li class="sf-it"><a href="javascript:void(0);" class="sf-more" sf-category-item="200146857" moreData="[]" >努比亚（nubia）</a></li> <li class="sf-it"><a href="javascript:void(0);" class="sf-more" sf-category-item="210471237" moreData="[]" >美图手机</a></li> <li class="sf-moreList"></li> </ul> </dd> </dl> <ul class="sf-navlist clearfix"> <li><a href="//shop.suning.com/70094634/index.html" sf-index>首页</a></li> <li><a href="https://shop.suning.com/70094634/search/%E8%8B%B9%E6%9E%9C%E6%89%8B%E6%9C%BA.html">苹果手机</a> </li> <li><a href="https://shop.suning.com/70094634/search/%E5%8D%8E%E4%B8%BA.html">华为手机</a> </li> <li><a href="https://shop.suning.com/70094634/search/%E8%8D%A3%E8%80%80.html">荣耀手机</a> </li> <li><a href="https://shop.suning.com/70094634/search/%E5%B0%8F%E7%B1%B3.html">小米手机</a> </li> <li><a href="https://shop.suning.com/70094634/search/%E9%AD%85%E6%97%8F.html">魅族手机</a> </li> <li><a href="https://shop.suning.com/70094634/search/%E5%8A%AA%E6%AF%94%E4%BA%9A.html">努比亚手机</a> </li> <li><a href="//shop.suning.com/70094634/list_210471240_1.html">原装配件</a> </li> </ul> <div class="ds-search" sf-search> <input type="text" name="keyword" placeholder="请输入关键词" /> <a href="javascript:void(0);" title="搜索" sf-search-ok></a> </div> </div> </div> </div>
<!-- ]]LAYOUT-F-->
</div></div>
<!-- ]]head-->
<script type="text/javascript" src="//resource.sop.suning.cn/shts/resource/sn_widget/js/module.js"></script> <script type="text/javascript" src="//resource.sop.suning.cn/shts/resource/sn_widget/js/op_widget.js"></script> <script> $(function(){ var head=$(".JS-head"); var styleHead="background-repeat:repeat;background-position:left 0px;background-color:#090547;background-attachment:scroll;"; if('0'=='1'){ styleHead=styleHead+"margin-bottom:10px;"; } head.attr("style",styleHead); }); </script>
</div>
<!--[if IE 6]>
<script type="text/javascript" src="//resource.sop.suning.cn/shts/resource/sn_widget/js/DD_belatedPNG.min.js"></script>
<script type="text/javascript">
DD_belatedPNG.fix('.ds_ie6png');
</script>
<![endif]--><!-- [[SHTS资源2015年4月9日21:56:29 -->
<script type="text/javascript" src="//resource.sop.suning.cn/shts/resource/SN_T_1001/default/assets/js/snt1001.min.js?v=20190717150028"></script>
<!-- ]]SHTS资源2015年4月9日21:56:29 -->
<script type="text/javascript" src="//resource.sop.suning.cn/resource/sfs/project/shopv2/c/common/js/sf.header.shop.min.js?v=20190717150028"></script>
<link rel="stylesheet" type="text/css" href="//res.suning.cn/project/pdsWeb/csspc2017/fourth-min.css?v=2019071306"/>	<!--[if IE 6]>
    <style type="text/css">
        .icon-plusone { background:none; filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='//css.suning.cn/project/pdsWeb/css/images/icon-plusone.png');}
    </style>
    <script type="text/javascript">
        // IE6下处理PNG24图片
        DD_belatedPNG.fix(".g-sticker-80 b, .imgzoom-video-play, .proinfo-focus .proinfo-star .stars, .proinfo-focus .proinfo-star .stars em, .imgzoom .pptv-logo, .imgzoom .oversea-logo");
    </script>
    <![endif]-->

    <script type="application/ld+json">
	{
		"@context": "https://ziyuan.baidu.com/contexts/cambrian.jsonld",
		"@id": "https://product.suning.com/0070094634/10985347748.html",
		"appid": "1547978792198080",
		"title": "华为(HUAWEI)手机畅享9S 华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待【价格 图片 品牌 报价】-苏宁易购华科手机专营店",
		"images": [
					"https://imgservice.suning.cn/uimg1/b2c/image/783X00lIk6NabyNuOdOUbw.jpg_800w_800h_4e",
					"https://imgservice.suning.cn/uimg1/b2c/image/xB89vZYMlMVYaBKcQ-C2eA.jpg_800w_800h_4e",
					"https://imgservice.suning.cn/uimg1/b2c/image/ddzdq5kS5SRwp5Ks1cT1LA.jpg_800w_800h_4e"			],
		"description": "华为(HUAWEI)手机畅享9S，苏宁易购提供华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待，麒麟710，6.21英寸珍珠屏，2400万广角三摄大存储大电池，买华为(HUAWEI)手机，就来华科手机专营店！",
		"pubDate": "2018-07-17T01:00:01",
		"upDate": "2018-07-17T08:02:03",
		"lrDate": "2018-07-17T09:10:11"
	}
	</script>

</head>
<body style="min-width: initial;"  >
<input type="hidden" id="fitImage" value="//image3.suning.cn/uimg/b2c/newcatentries/0070094634-000000010985347748_1_160x160.jpg"/> <input type="hidden" id="feedback_image" value="//image4.suning.cn/uimg/b2c/newcatentries/0070094634-000000010985347748_1_60x60.jpg"/> <input type="hidden" id="catEntryId_2" value=""/> <input type="hidden" id="catEntryId_3" value=""/> <input type="hidden" id="curPartNumber" value="000000010985347748"/> <input type="hidden" value="华科手机专营店" id="shop_name"/> <input type="hidden" value="0070094634" id="shop_code"/> <input type="hidden" value="" id="shop_status"/> <input type="hidden" value="" id="brand_dacu_url"/> <input type="hidden" value="" id="ga_mainTopCategorytBean_description_name"/> <input type="hidden" value="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待" id="ga_itemDataBean_description_name"/> <input type="hidden" value="" id="ga_itemDataBean_category_parentCategory_description_name"/> <input type="hidden" value="" id="ga_itemDataBean_category_description_name"/> <input type="hidden" value="" id="ga_mainTopCategorytBean_categoryId"/> <input type="hidden" value="10985347748" id="ga_itemDataBean_itemID"/> <input type="hidden" value="0070094634" id="supplierID"/> <input type="hidden" value="" id="fourpage"/> <input type="hidden" id="resourceType" value="web"/> <input type="hidden" value="-1" id="manageInvFlag"/> <input type="hidden" value="-1" id="mdmProvinceId"/> <input type="hidden" value="-1" id="mdmCityId"/> <input type="hidden" value="-1" id="mdmDistrictId"/> <input type="hidden" value="-1" id="productStatus"/> <input type="hidden" value="-1" id="productStatusDesc"/> <input type="hidden" value="-1" id="shipOffset"/> <input type="hidden" value="1" id="vendorType"/> <input type="hidden" value="" id="ssa-stcode"/> <input type="hidden" value="1" id="operatetype"/> <input type="hidden" value="3" id="deliverytype"/> <input type="hidden" value="" id="suppliernewID"/> <input type="hidden" id="pagename" value="pgcate=10008;prdtp=00006;pgtitle=普通四级页;prdid=10985347748;shopid=0070094634;supid=;actype=;tag="> <input type="hidden" id="delivery" value=""> <!--[if lte IE 7]> <div class="pop-onsale" id="ie7_onsale" > 此款有货 <i class="d-arr"></i> </div> <![endif]--> <div class="wrapper-allwidth"> <div class="wrapper head-shop-wrapper"> <div class="breadcrumb"> <a gid="20089" class="ft" name="item_10985347748_guide_mulu01" id="category1" href="//list.suning.com/0-20089-0.html" >手机/数码/配件</a> <span class="sep">></span> <div class="dropdown"><span gid="20002" class="dropdown-text"><a class="ft" name="item_10985347748_guide_mulu02" href="//list.suning.com/0-20002-0.html">手机通讯</a></span><p></p> <i></i> </div> <span class="sep">></span> <div class="dropdown"><span gid="20006" class="dropdown-text"><a class="ft" name="item_10985347748_guide_mulu03" href="//list.suning.com/0-20006-0.html">手机</a></span><p></p> <ul class="dropdown-option" id="breadGroup"> <li><a name="item_10985347748_mulu03_fenlei01" href="https://list.suning.com/0-20006-0-0-0-0-0-0-0-0-4245046.html" title="iPhone">iPhone</a></li> <li><a name="item_10985347748_mulu03_fenlei02" href="//list.suning.com/0-20006-0-1-0-0-0-0-0-0-10011.html" title="三星">三星</a></li> <li><a name="item_10985347748_mulu03_fenlei03" href="//list.suning.com/0-20006-0-1-0-0-0-0-0-0-10167.html" title="诺基亚">诺基亚</a></li> <li><a name="item_10985347748_mulu03_fenlei04" href="//list.suning.com/0-20006-0-1-0-0-0-0-0-0-10032.html" title="HTC">HTC</a></li> <li><a name="item_10985347748_mulu03_fenlei05" href="//list.suning.com/0-20006-0-1-0-0-0-0-0-0-10028.html" title="索尼">索尼</a></li> <li><a name="item_10985347748_mulu03_fenlei06" href="//list.suning.com/0-20006-0-1-0-0-0-0-0-0-12121.html" title="小米">小米</a></li> <li><a name="item_10985347748_mulu03_fenlei07" href="//list.suning.com/0-20006-0-1-0-0-0-0-0-0-11635.html" title="华为">华为</a></li> <li><a name="item_10985347748_mulu03_fenlei08" href="//list.suning.com/0-20006-0-1-0-0-0-0-0-0-10099.html" title="联想">联想</a></li> <li><a name="item_10985347748_mulu03_fenlei09" href="//list.suning.com/0-20006-0-1-0-0-0-0-0-0-22270.html" title="Android">Android</a></li> <li><a name="item_10985347748_mulu03_fenlei10" href="//list.suning.com/0-20006-0-1-0-0-0-0-0-0-30394.html" title="WP8">WP8</a></li> <li><a name="item_10985347748_mulu03_fenlei11" href="//shouji.suning.com/" title="手机频道">手机频道</a></li> </ul> <i></i> </div> <span class="sep">></span> <div class="dropdown"><span class="dropdown-text"><a href="//www.suning.com/pinpai/0864-20006-0.html">华为(HUAWEI)<span style="display: none">手机</span></a></span><p></p> <ul class="dropdown-option" id="breadBrand"> <li><a href="//www.suning.com/pinpai/0021-20006-0.html" brandId="0021" title="Apple">Apple<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/0021-20006-0.html" brandId="0021" title="Apple">Apple<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/0864-20006-0.html" brandId="0864" title="华为HUAWEI">华为HUAWEI<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/0864-20006-0.html" brandId="0864" title="华为HUAWEI">华为HUAWEI<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/0DER-20006-0.html" brandId="0DER" title="小米mi">小米mi<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/6138-20006-0.html" brandId="6138" title="荣耀honor">荣耀honor<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/6138-20006-0.html" brandId="6138" title="荣耀honor">荣耀honor<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/0DER-20006-0.html" brandId="0DER" title="小米mi">小米mi<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/0115-20006-0.html" brandId="0115" title="OPPO">OPPO<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/J675-20006-0.html" brandId="J675" title="vivo">vivo<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/J675-20006-0.html" brandId="J675" title="vivo">vivo<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/0115-20006-0.html" brandId="0115" title="OPPO">OPPO<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/1659-20006-0.html" brandId="1659" title="三星SAMSUNG">三星SAMSUNG<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/1659-20006-0.html" brandId="1659" title="三星SAMSUNG">三星SAMSUNG<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/0OVA-20006-0.html" brandId="0OVA" title="realme">realme<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/1389-20006-0.html" brandId="1389" title="魅族MEIZU">魅族MEIZU<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/1389-20006-0.html" brandId="1389" title="魅族MEIZU">魅族MEIZU<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/0OVA-20006-0.html" brandId="0OVA" title="realme">realme<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/1459-20006-0.html" brandId="1459" title="诺基亚NOKIA">诺基亚NOKIA<span style="display: none">手机</span></a></li> <li><a href="//www.suning.com/pinpai/1459-20006-0.html" brandId="1459" title="诺基亚NOKIA">诺基亚NOKIA<span style="display: none">手机</span></a></li> </ul> <i></i> </div> <span class="sep">></span> <span class="breadcrumb-title" title="华为(HUAWEI)畅享9S手机" id="productName"><a href="//product.suning.com/0070094634/10985347748.html">华为(HUAWEI)畅享9S手机</a></span> </div> </div> </div> <div class="wrapper proinfo" sap-modid="theTop"> <div class="proinfo-container clearfix"> <div class="proinfo-left" sap-modid="02"> <div id="imgZoom" class="imgzoom"> <div class="imgzoom-main"> <div class="playmark-box" style="display: none;"> </div> <a id="bigImg" class="view-img" name="item_10985347748_sppic_bigpic01" href="javascript:void(0);"> <img onerror="this.src='//res.suning.cn/project/pdsWeb/images/blank_pic_800.jpg'" alt="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待" src="//imgservice.suning.cn/uimg1/b2c/image/783X00lIk6NabyNuOdOUbw.jpg_800w_800h_4e"> </a> <div class="imgzoom-shot"></div> <i id="labelPicture" class="g-sticker-80" style="display:none;"><b class=""></b></i> <i class="oversea-logo hide"></i> </div> <div class="imgzoom-video"><a href="javascript:void(0);" class="close"></a> <div id="imgzoom_video_con" data-playcode="" style="height: 100%;" data-playUrl=""></div> <script type="text/javascript"> var mainVedioUrl = "http://m4.pptvyun.com/pvod/e11a0/DbCyWb50h1oSMYz1oT9DRKD1Pmk/eyJkbCI6MTU2MDY2NjAzNywiZXMiOjYwNDgwMCwiaWQiOiIwYTJkbjZ5ZHFhbWtuSzJMNEsyZG9hZmhvYU9lbjZtYnBxQSIsInYiOiIxLjAifQ/0a2dn6ydqamknK2L4K2doafhoaOen6mbpqA.mp4"; if (mainVedioUrl != "" && mainVedioUrl.indexOf(".mp4") > 0) { $("#imgzoom_video_con").attr("data-playUrl", mainVedioUrl); } else if (mainVedioUrl != "" && mainVedioUrl.indexOf(".swf") > 0) { mainVedioUrl = mainVedioUrl.substring(0, mainVedioUrl.indexOf(".swf")); mainVedioUrl = mainVedioUrl.substring(mainVedioUrl.lastIndexOf("/") + 1); $("#imgzoom_video_con").attr("data-playcode", mainVedioUrl); } </script> </div> <a name="item_10985347748_vedio_vediopic-click" href="javascript:void(0);" class="imgzoom-video-play"></a> <div class="imgzoom-thumb"> <a name="item_10985347748_sppic_picup01" class="prev prev-disable" href="javascript:void(0);"></a> <div class="imgzoom-thumb-main"> <ul> <li class="current" id="fenwei"> <a name="item_10985347748_sppic_xiaop01" href="javascript:void(0);"><img onerror="javascript:errorMainPicture(this);" alt="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待" src-large="//imgservice.suning.cn/uimg1/b2c/atmosphere/JkoiMX87alhsokZc4hgMIA.jpg_800w_800h_4e" src-medium="//imgservice.suning.cn/uimg1/b2c/atmosphere/JkoiMX87alhsokZc4hgMIA.jpg_800w_800h_4e" src="//imgservice.suning.cn/uimg1/b2c/atmosphere/JkoiMX87alhsokZc4hgMIA.jpg_60w_60h_4e"></a> </li> <li > <a name="item_10985347748_sppic_xiaop01" href="javascript:void(0);"><img onerror="" alt="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待" src-large="//imgservice.suning.cn/uimg1/b2c/image/783X00lIk6NabyNuOdOUbw.jpg_800w_800h_4e" src-medium="//imgservice.suning.cn/uimg1/b2c/image/783X00lIk6NabyNuOdOUbw.jpg_800w_800h_4e" src="//imgservice.suning.cn/uimg1/b2c/image/783X00lIk6NabyNuOdOUbw.jpg_60w_60h_4e"></a> </li> <li class="" data-index="2"> <a name="item_10985347748_sppic_xiaop02" href="javascript:void(0);"><img onerror="javascript:$('.imgzoom-thumb-main li[data-index=2]').remove();" alt="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待" src-large="//imgservice.suning.cn/uimg1/b2c/image/xB89vZYMlMVYaBKcQ-C2eA.jpg_800w_800h_4e" src-medium="//imgservice.suning.cn/uimg1/b2c/image/xB89vZYMlMVYaBKcQ-C2eA.jpg_800w_800h_4e" src="//imgservice.suning.cn/uimg1/b2c/image/xB89vZYMlMVYaBKcQ-C2eA.jpg_60w_60h_4e"></a> </li> <li class="" data-index="3"> <a name="item_10985347748_sppic_xiaop03" href="javascript:void(0);"><img onerror="javascript:$('.imgzoom-thumb-main li[data-index=3]').remove();" alt="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待" src-large="//imgservice.suning.cn/uimg1/b2c/image/ddzdq5kS5SRwp5Ks1cT1LA.jpg_800w_800h_4e" src-medium="//imgservice.suning.cn/uimg1/b2c/image/ddzdq5kS5SRwp5Ks1cT1LA.jpg_800w_800h_4e" src="//imgservice.suning.cn/uimg1/b2c/image/ddzdq5kS5SRwp5Ks1cT1LA.jpg_60w_60h_4e"></a> </li> <li class="" data-index="4"> <a name="item_10985347748_sppic_xiaop04" href="javascript:void(0);"><img onerror="javascript:$('.imgzoom-thumb-main li[data-index=4]').remove();" alt="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待" src-large="//imgservice.suning.cn/uimg1/b2c/image/zNHgh6oIrHum6xRv-QpiKg.jpg_800w_800h_4e" src-medium="//imgservice.suning.cn/uimg1/b2c/image/zNHgh6oIrHum6xRv-QpiKg.jpg_800w_800h_4e" src="//imgservice.suning.cn/uimg1/b2c/image/zNHgh6oIrHum6xRv-QpiKg.jpg_60w_60h_4e"></a> </li> <li class="" data-index="5"> <a name="item_10985347748_sppic_xiaop05" href="javascript:void(0);"><img onerror="javascript:$('.imgzoom-thumb-main li[data-index=5]').remove();" alt="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待" src-large="//imgservice.suning.cn/uimg1/b2c/image/aVo9V1fSQ7o7tEYbB9yeLw.jpg_800w_800h_4e" src-medium="//imgservice.suning.cn/uimg1/b2c/image/aVo9V1fSQ7o7tEYbB9yeLw.jpg_800w_800h_4e" src="//imgservice.suning.cn/uimg1/b2c/image/aVo9V1fSQ7o7tEYbB9yeLw.jpg_60w_60h_4e"></a> </li> </ul> </div> <a name="item_10985347748_sppic_picdown01" class="next" href="javascript:void(0);"></a> </div> <div class="imgzoom-pop"><img onerror="this.src='//res.suning.cn/project/pdsWeb/images/blank_pic_800.jpg'"/> </div> </div> <div class="imgzoom-memo"> <div class="z-item compare"> <a id="compare" href="javascript:;" style="display:none;" name="item_db_01_pro"><i></i>对比</a> </div> <div class="share"> <span class="label" name="item_10985347748_basic_share"><i class="sh-i"></i>分享</span> <div class="share-list" style="display: none;"> <a rel="nofollow" target="_blank" name="item_10985347748_basic_share-weibo" title="新浪微博" class="sina" href="#"></a> <a rel="nofollow" target="_blank" name="item_10985347748_basic_share-douban" title="豆瓣" class="douban" href="#"></a> <a rel="nofollow" target="_blank" name="item_10985347748_basic_share-kaixin" title="开心" class="kaixin" href="#"></a> </div> </div> <div class="z-item favorite"> <a name="item_10985347748_basic_favorite" href="javascript:FourPage.addProductFavorite();" id="inerestBox" sa-data="{'eletp':'collect','prdid':'10985347748','shopid':'0070094634','salestatus':'1'}"><i></i>关注</a> </div> <div class="z-item research" id="research"> <a href="//ued.suning.com/survey/view/prod1"> <i></i>有奖调查</a> </div> <div class="report"> <a id="reportbtn" name="item_10985347748_jubao_rukou" href="javascript:FourPage.reportJubao();" style="display:none"><i></i>举报</a> <form id="reportForm" method='post' action="//jubao.suning.com/sams/accuseIndex.action" target='_blank' style="display:none"> <input type='hidden' name="supplierID" value="0070094634"> <input type='hidden' name="curShopName" value="华科手机专营店"> <input type='hidden' name="shopUrl" value="//shop.suning.com/70094634/index.html"> <input type='hidden' name="itemID" value="000000010985347748"> <input type='hidden' name="itemName" value="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待"> <input type='hidden' name="itemUrl" value="//product.suning.com/0070094634/10985347748.html"> <input type='hidden' name="imgUrl" value="//image4.suning.cn/uimg/b2c/newcatentries/0070094634-000000010985347748_1_120x120.jpg"> <input type='hidden' name="probrandName" value="华为(HUAWEI)"> <input type='hidden' name="procateCode" value="R1901001"> </form> </div> </div> <div class="shopping-guide-l lazy-ajax" id="shoppingGuide" data-type="function" style="display:none;"></div> <script id="shopingGuidelScriptContent" type="text/html"> <div class="sg-summary"> {{if searchStore == 1}} <strong>门店现货</strong><span>家门口的真机体验</span> {{/if}} {{if searchStore == 0}} <strong>专业导购</strong><span>身边的家电专家</span> {{/if}} </div> {{if searchStore == 1}} <div class="store "> <div class="i-loc"></div> <div class="s-info"> <p class="st-name" title="{{vstore2ndInfos[0].storeName}}"> <strong>{{vstore2ndInfos[0].storeName}}</strong> <a rel="nofollow" target="_blank" name="{{wuhuoMore}}" href="{{moreStoreUrl}}" class="more">更多门店 ></a> </p> <p class="st-address"> <strong>{{vstore2ndInfos[0].storeAddress}}</strong></p> <a target="_blank" name="{{wuhuo}}" href="{{vbuyDomain}}/vbuyshop.html?shopCode={{vstore2ndInfos[0].storeCode}}&guideId={{vstore2ndInfos[0].guideId}}&channel=10" class="btn-go l">去门店体验</a> </div> </div> {{/if}} {{if searchStore == 0}} <div class="sg-girl "> <div class="g-portrait"> <img lazy-src="{{vstore2ndInfos[0].guidePhoto}}" alt="" /> </div> <div class="girl-r"> <p> <span class="name"><strong>{{vstore2ndInfos[0].guideName}}</strong></span> <span class=" star-bg"> <i class="star-val" style="overflow: hidden; width: {{vstore2ndInfos[0].starLevel*20}}%;"></i> </span> <span class="wk-txt">已接<i class="order-num">{{vstore2ndInfos[0].orderNum}}</i>单</span> </p> <p class="store-address "><strong>{{vstore2ndInfos[0].storeName}}</strong></p> <p><a rel="nofollow" target="_blank" name="{{wuhuoMore}}" href="{{moreStoreUrl}}" class="more">更多门店 ></a></p> <a target="_blank" name="{{wuhuo}}" href="{{vbuyDomain}}/vbuyshop.html?shopCode={{vstore2ndInfos[0].storeCode}}&guideId={{vstore2ndInfos[0].guideId}}&channel=10" class="btn-go ">去门店找TA</a> </div> </div> {{/if}} </script> <script id="newShopingGuidelScriptContent" type="text/html"> <div class="sg-summary"> <strong>{{tipTitle}}</strong><span>{{tipContent}}</span> </div> <div class="sg-girl "> <div class="g-portrait"> <img lazy-src="{{guidePhoto}}" alt="" /> </div> <div class="girl-r"> <p> <span class="name"><strong>{{guideName}}</strong></span> <span class=" star-bg"> <i class="star-val" style="overflow: hidden; width: {{starLevel*20}}%;"></i> </span> <span class="wk-txt">已接<i class="order-num">{{orderNum}}</i>单</span> </p> <p class="store-address "><strong>{{storeName}}</strong></p> {{if isRouteToSntk == 0}} <p><a rel="nofollow" target="_blank" name="{{wuhuoMore}}" href="{{moreStoreUrl}}" class="more">更多门店 ></a></p> {{/if}} <a target="_blank" name="{{wuhuo}}" href="{{vbuyDomain}}/vbuyshop.html?shopCode={{storeCode}}&guideId={{guideId}}&channel=10" class="btn-go ">去门店找TA</a> </div> </div> </script></div> <div class="proinfo-main" id="proinfoMain" sap-modid="01"> <div id="borderline" class="p-r-border"></div> <div class="proinfo-short-tip" id="proinfoShortTip" style="display:none;"></div> <!--海外购国旗--> <div class="national-flag clearfix" id="NationalFlag" style="display:none;"> <i class=""></i> <div class="info" id="overSeaPlace"> </div> </div> <div class="proinfo-title"> <h1 id="itemDisplayName"> 华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待</h1> <h2 id="promotionDesc">麒麟710，6.21英寸珍珠屏，2400万广角三摄大存储大电池<a href="https://talk8.suning.com/index.htm?catalogId=10051&storeId=10052&sc=0070094634&url=https%3A%2F%2Fshop.suning.com%2F70094634%2Findex.html">【点击咨询在线客服免费领取120元电话卡】>></a></h2> </div> <div class="dajuhui-panel dajuhui-panel2" style="display:none;" id="timePanel2"> <span class="djh-logo"></span> <span class="super-quan hide"></span> <span class="djh-cd"> <i class="djh-icon"></i> <span class="active-label">此商品</span> <span class="proinfo-cd"> <span id="bigPolyTime"></span> </span> <span class="active-label">参加活动</span> <span class="proinfo-cd"><span id="snqgPrice" style="display:none"></span></span> </span> <span class="sell-tell"> <a class="qgtell-text" name="item_10985347748_kstx_click" href="javascript:reyuSnqgRemind();">开售提醒</a> </span> <div class="djh-qg" id="bigPolyMore"> </div> </div> <div class="dajuhui-panel" style="display:none;" id="timePanel"> <span class="djh-logo"></span> <span class="djh-cd"> <i class="djh-icon"></i> <span class="active-label" id="beginOrEnd">距离活动开始</span> <span class="proinfo-cd"> <em class="d">02</em> <span>天</span> <em class="h">07</em> <span>时</span> <em class="m">04</em> <span>分</span> <em class="s">39</em> <span>秒</span> <input type="hidden" id="durationTime" value="200000"> </span> </span> <span class="snqg-num" style="display: none"></span> <span class="qgcontain hide"> <span class="qgprcent"></span><i class="qg-i"></i> </span> <div class="djh-qg" id="djhBuyNum" style="display:none;"> <span class="yq">已抢</span> <span class="num"></span> </div> <div class="djh-qg" id="bigPolyMore2" style="display: none;"> </div> <div id="yushouCount" class="total presell-rule rule-fr" style="display:none;"></div> <span class="super-new-icon" id="superNewIcon" style="display: none;"></span> </div> <div id="priceDom" class="proinfo-focus clearfix"> <div class="txt-under-shelf" style="display:none;" id="xjdiv">此商品已下架</div> <div style="position: relative;" class="price-container clearfix" id="mainPrice"> </div> <dl class="price-chd" id="promotionForPds" style="display:none;"> </dl> <dl class="receive-quan proinfo-promo hide" id="discountPrice"> <dt><span class="w2" id="getCoupon">优惠</span></dt> <dd> <div id="discountPriceValue" class="receive-yxhd hide"></div> <div id="receiveLimit" class="hide"></div> <div id="shoppingAllowance"> <script id="shoppingAllowancePortal" type="text/html"> <div class="oto-panel sn-oto-cjhb" id="allowancePortal"> <span class="oto-logo"><img src="//image2.suning.cn/uimg/cms/img/154510129292334762.png"></span> <span class="oto-quan">{{bountyRulDescribe}}</span> <div class="oto-go"> <a name="item_10985347748_gwjtrk_click" href="javascript:shopAllowance.portalClick();" class="more">立即兑换 &gt;</a> </div> </div> </script> </div> </dd> <dd id="freeCouponTitle"> <div class="more-juan" id="freeCouponBox"></div> <div class="gua-juan" onclick="scrapeCouponLoginSataus()"> <a href="javascript:;" class="a1" onclick="return false;"></a> <span>100%刮中券，最高50元无敌券</span> <a href="javascript:;" class="a2" onclick="return false;">立即去刮奖&gt;</a> </div> </dd> <dd id="allcuxiao" style="display:none;"> <div class="ph-price-qrcode" id="mobileTitle" style="display:none;"> <label></label><i class="i-triangle"></i><div class="prom-info" id="mobileBox"></div> </div> <ul class="promo-list"> <li id="voucherTitle" style="display:none;"><label>满 减</label><i class="i-triangle"></i><p class="promotion-content" id="voucherBox"></p></li> <li id="lhvoucherTitle" style="display:none;"><label>联合满减</label><i class="i-triangle"></i><p class="promotion-content" id="lhvoucherBox"></p></li> <li id="isXYuanNItemTitle" style="display:none;"><label>套 装 价</label><i class="i-triangle"></i><p class="promotion-content" id="isXYuanNItemBox"></p></li> <li id="taogouyhTitle" style="display:none;"><label>套购优惠</label><i class="i-triangle"></i><p class="promotion-content" id="taogouyhBox"></p></li> <li id="giftTitle" class="promo-gift" style="display:none;"><label class="lable-zp">赠 品</label><i class="i-triangle i-tri-zp"></i><div class="zengpin clearfix" id="giftBox"></div></li> <li id="limitGifts" class="manzen-handle-li" style="display:none;"><script id="limitGiftsTmpl" type="text/html"> {{ if isStudentGift == '1' }} <label class = "xy-label">校园专享限量赠</label> {{ else }} <label>限量赠</label> {{/if}} <i class="i-triangle"></i> <p class="promotion-content"> {{ if superText4LoginOut != ""}} {{superText4LoginOut}} {{ else if stuGiftsText4LoginOut != "" }} {{stuGiftsText4LoginOut}} {{ else }} <div class="manzen-handle manzen-handle-show" id="jtzpHandle"> <span class="manzen-hendle-text"> {{ if superGift == '1' }} <i class="jtzp-super"></i> {{/if}} {{bonusLabel}} </span> {{ if firstLeveldisplayStatus == '1'}} <span class="manzen-hendle-text-pop">{{firstBonusLabel}}</span> {{ else }} <span class="manzen-hendle-text-pop manzen-pop-none">{{firstBonusLabel}}</span> {{/if}} <i class="ng-iconfont down">&#xe62e;</i> <i class="ng-iconfont up">&#xe63a;</i> <div class="manzen-pop"> {{each stepsGiftList as stepGift i}} {{ if i != 0}} {{ if stepGift.displayStatus == '1'}} <div class="manzen-pop-title">{{stepGift.bonusLabel}}</div> {{ else }} <div class="manzen-pop-title manzen-pop-none">{{stepGift.bonusLabel}}</div> {{/if}} {{/if}} <div class="manzen-pop-list"> {{each stepGift.subStepsGifts as subStepGift j}} <a target="_blank" class="manzen-pop-img-container" href="{{subStepGift.href}}" > <img class="manzen-pop-img" data-src="{{subStepGift.imgUrl}}"> {{ if subStepGift.giftFinished == '1' }} <div class="manzem-pop-img-label">已赠完</div> {{/if}} </a> <div class="manzen-pop-number">*{{subStepGift.onceQty}}</div> {{/each}} </div> {{/each}} </div> </div> {{/if}} </p> </script></li> <li id="ordersGifts" class="manzen-handle-li" style="display:none;"><script id="orderGiftsTmpl" type="text/html"> {{if isStudentGift == '1'}} <label class = "xy-label">校园专享满赠</label> {{else}} <label>满 赠</label> {{/if}} <i class="i-triangle"></i> <p class="promotion-content"> {{ if stuGiftsText4LoginOut != "" }} {{stuGiftsText4LoginOut}} {{ else }} <div class="manzen-handle manzen-handle-show" id="manzenHandle"> <span class="manzen-hendle-text">{{manzenTitle}}</span> {{ if firstLeveldisplayStatus == '1'}} <span class="manzen-hendle-text-pop">{{manzenPop}}</span> {{ else }} <span class="manzen-hendle-text-pop manzen-pop-none">{{manzenPop}}</span> {{/if}} <i class="ng-iconfont down">&#xe62e;</i> <i class="ng-iconfont up">&#xe63a;</i> <div class="manzen-pop"> {{each ordersGiftList as giftGift i}} {{ if i != 0}} {{ if giftGift.displayStatus == '1'}} <div class="manzen-pop-title">{{giftGift.manzenPop}}</div> {{ else }} <div class="manzen-pop-title manzen-pop-none">{{giftGift.manzenPop}}</div> {{/if}} {{/if}} <div class="manzen-pop-list"> {{each giftGift.subOrdergifts as subOrdergifts j}} <a target="_blank" class="manzen-pop-img-container" href="{{subOrdergifts.href}}" name="item_{{subOrdergifts.giftCode}}_ZPTZ_show"> <img class="manzen-pop-img" data-src="{{subOrdergifts.imgUrl}}"> {{ if subOrdergifts.giftFinished == '1' }} <div class="manzem-pop-img-label">已赠完</div> {{/if}} </a> <div class="manzen-pop-number">*{{subOrdergifts.onceQty}}</div> {{/each}} </div> {{/each}} </div> </div> {{if activityLink != ""}} <a href="{{activityLink}}" target="_blank" class="a-detail ml10" name="item_{{partNumber}}_CKHD_show">查看活动</a> {{/if}} {{/if}} </p> </script> </li> <li id="jrPromTitle" style="display:none;"><label>支付满减</label><i class="i-triangle"></i><p class="promotion-content" id="jrPromBox"></p></li> <li id="purchaseTitle" style="display:none;"><label>优惠换购</label><i class="i-triangle"></i><p class="promotion-content" id="purchaseBox"></p></li> <li id="couponTitle" style="display:none;"><label>返 券</label><i class="i-triangle"></i><p class="promotion-content" id="couponBox"></p></li> <li id="newcouponTitle" style="display:none;"><label>返 券</label><i class="i-triangle"></i><p class="promotion-content" id="newcouponBox"></p></li> <li id="yfbTitle" style="display:none;"><label>实名有礼</label><i class="i-triangle"></i><p class="prom-info prom-yun" id="yfbBox"><span class="desc">实名认证领苏宁支付券</span><a href="//c.m.suning.com/smpc.htm?source=20&terminal=31" target="_blank" class="a-detail ml10">立即领取 &gt;</a></p></li> <li id="rxfTitle" style="display:none;"><label>任性付</label><i class="i-triangle"></i><p class="promotion-content" id="rxfBox"></p></li> <li id="scodeTitle" style="display:none;"><label>S 码</label><i class="i-triangle"></i><p class="promotion-content" id="scodeBox"></p></li> <li id="pointTitle"class="prom-list-box" style="display:none;"><label>云 钻</label><i class="i-triangle"></i><p class="promotion-content" id="pointBox"></p><p class="promotion-content" id="yunzuan"></p></li> <li id="freightfreeTitle" style="display:none;"><label>免运费</label><i class="i-triangle"></i><p class="promotion-content" id="freightfreeBox"></p></li> <li id="govTitle" style="display:none;"></li> <li id="jnbtTitle" style="display:none;"><label>节能补贴</label><i class="i-triangle"></i><p class="promotion-content" id="jnbtBox"></p></li> </ul> <a class="zp-b-img"> <i ></i><img src="" alt=""/> <div class="zp-title"> <h4 class="txt"></h4> <p class="price">&yen</p> </div> </a> <span class="tool-tip zindex22"><i class="a-up-arrow tip-yun"></i></span> <div class="promo-closeup"> <span >更多促销<i class="ng-iconfont">&#xe62e;</i></span> </div> <div class="promo-show"> <span >收起<i class="ng-iconfont">&#xe63a;</i></span> </div> </dd> </dl> </div> <!-- 乐拼购 --> <dl class="happy-go" id="happyGo" style="display:none;"> </dl> <dl class="support-panel" style="display:none;"> <dt><span class="w2">支持</span></dt> <dd class=""> <a href="javascript:void(0);" id="4Gpackage" style="display:none;" name="item_10985347748_ysc_gm0101"> </a> <a id="yjhx" style="display:none;" href="" rel="nofollow" target="_blank" name="item_10985347748_basic_oldfornew"> </a> </dd> <span class="tool-tip"> <i class="a-up-arrow"></i> </span> </dl> <div class="proinfo-deliver"> <dl><dt><span class="w2">送至</span></dt> <dd class="clearfix"> <div id="sncity" class="l"></div> <div class="proinfo-deliver-tip"> <strong id="haveProduct" class="goods-haveNo" style="display:none;"></strong> <span id="c_kucun"></span> <strong id="nowProduct" class="yunfei-fare"></strong> <span id="zyService" class="sent-support" style="display:none;"> <em>支持</em> <ul></ul> <span class="tool-tip"> <i class="a-up-arrow"></i> </span> </span> </div> <span id="yunfei_tooltip" class="s-tooltip" style="display: none;"> V3会员自营订单满76元（含）免运费订单满76元（含）免运费订单满76元（含）免运费 <span class="tri-pointer-up"> <i class="inner-tri"></i> </span> </span> </dd> <dd class="supplier-row" id="shopNameBox" > <span id="prescription" class="arriv-infos"></span> <span id="shopName">由""直接销售和发货，并提供售后服务</span> <a id="callme" rel="nofollow" name="item_10985347748_basic_agent" href="#" class="contact-me contact-me-shop"></a> <span class="tool-tip"><i class="a-up-arrow"></i></span> </dd> <dd class="arriv-warning" id="arrivWarning" style="display:none"></dd> </dl> </div> <div class="proinfo-weight hide" id="weightid"> <dl> <dt><span class="w2">重量</span></dt> <dd id="weightcvalue"></dd> </dl> </div> <dl class="proinfo-o2o" style="display:none"> <dt>门店服务</dt> <dd> <ul> <li class="item2" style="display:none"> <a href="javascript:void(0);" class="icon" name="item_10985347748_mdfw_mdxh"></a> <a href="javascript:void(0);" name="item_10985347748_mdfw_mdxh">门店现货</a> <span>· 选择有现货的门店下单，可立即提货</span> </li> <li class="item6" style="display:none"> <a href="javascript:void(0);" class="icon"></a> <a href="javascript:void(0);" name="item_10985347748_mdfw_ddsc">到店试</a> <span>· 可支持到店试穿服务</span> </li> </ul> </dd> </dl> <div class="divide-line"></div> <div class="tzm" id="J-TZM"> <div class="pop-onsale"> 此款有货 <i class="d-arr"></i> </div> <dl id="colorItemList" class="proinfo-color-ex proattr-radio cluster-radio" > <dt> <span class="w2"> 颜色 </span> </dt> <dd> <ul class="tip-infor"> <li colorid="10001" sku="000000011082969306" itemType="" data-id="1" title="幻夜黑" class="clr-item"> <a name="item_10985347748_ysys_size01" onclick="FourPage.changeVersion('000000010985347748','000000011082969306','10001',this);return false;" sa-data="{'eletp':'prd','prdid':'082969306','shopid':'0070094634','salestatus':'1'}" href="//product.suning.com/0070094634/11082969306.html"> <img src="//image3.suning.cn/uimg/b2c/newcatentries/0070094634-000000011082969306_1_60x60.jpg" alt=""><i></i><span>幻夜黑</span> </a> </li> <li colorid="10002" sku="000000010992045431" itemType="" data-id="2" title="极光蓝" class="clr-item"> <a name="item_10985347748_ysys_size02" onclick="FourPage.changeVersion('000000010985347748','000000010992045431','10002',this);return false;" sa-data="{'eletp':'prd','prdid':'992045431','shopid':'0070094634','salestatus':'1'}" href="//product.suning.com/0070094634/10992045431.html"> <img src="//image1.suning.cn/uimg/b2c/newcatentries/0070094634-000000010992045431_1_60x60.jpg" alt=""><i></i><span>极光蓝</span> </a> </li> <li colorid="10003" sku="000000000945055176" itemType="" data-id="3" title="珊瑚红" class="clr-item"> <a name="item_10985347748_ysys_size03" onclick="FourPage.changeVersion('000000010985347748','000000000945055176','10003',this);return false;" sa-data="{'eletp':'prd','prdid':'945055176','shopid':'0070094634','salestatus':'1'}" href="//product.suning.com/0070094634/945055176.html"> <img src="//image4.suning.cn/uimg/b2c/newcatentries/0070094634-000000000945055176_1_60x60.jpg" alt=""><i></i><span>珊瑚红</span> </a> </li> </ul> <input type="hidden" /> </dd> </dl> <dl id="versionItemList" class="proinfo-buytype proattr-radio cluster-radio" > <dt> <span class="w2"> 版本 </span> </dt> <dd> <ul> <li class="disabled" versionid="20001" sku="000000010985624242" data-id="1" itemType="" title="全网通（4GB+128GB）" > <a name="item_10985347748_ysc_size01" onclick="FourPage.changeVersion('000000010985347748','000000010985624242','20001',this);return false;" sa-data="{'eletp':'prd','prdid':'985624242','shopid':'0070094634','salestatus':'1'}" href="//product.suning.com/0070094634/10985624242.html">全网通（4GB+128GB）<i></i> </a> </li> <li class="disabled" versionid="20002" sku="000000011082969382" data-id="2" itemType="" title="全网通（6GB+64GB）" > <a name="item_10985347748_ysc_size02" onclick="FourPage.changeVersion('000000010985347748','000000011082969382','20002',this);return false;" sa-data="{'eletp':'prd','prdid':'082969382','shopid':'0070094634','salestatus':'1'}" href="//product.suning.com/0070094634/11082969382.html">全网通（6GB+64GB）<i></i> </a> </li> <li class="disabled" versionid="20003" sku="000000010985358059" data-id="3" itemType="" title="全网通（4GB+64GB）" > <a name="item_10985347748_ysc_size03" onclick="FourPage.changeVersion('000000010985347748','000000010985358059','20003',this);return false;" sa-data="{'eletp':'prd','prdid':'985358059','shopid':'0070094634','salestatus':'1'}" href="//product.suning.com/0070094634/10985358059.html">全网通（4GB+64GB）<i></i> </a> </li> <li class="disabled" versionid="20004" sku="000000011036776950" data-id="4" itemType="" title="移动版（4GB+128GB）" > <a name="item_10985347748_ysc_size04" onclick="FourPage.changeVersion('000000010985347748','000000011036776950','20004',this);return false;" sa-data="{'eletp':'prd','prdid':'036776950','shopid':'0070094634','salestatus':'1'}" href="//product.suning.com/0070094634/11036776950.html">移动版（4GB+128GB）<i></i> </a> </li> <li class="disabled" versionid="20005" sku="000000000945055176" data-id="5" itemType="" title="全网通（4GB+128GB）+ 1年碎屏险套餐" > <a name="item_10985347748_ysc_size05" onclick="FourPage.changeVersion('000000010985347748','000000000945055176','20005',this);return false;" sa-data="{'eletp':'prd','prdid':'945055176','shopid':'0070094634','salestatus':'1'}" href="//product.suning.com/0070094634/945055176.html">全网通（4GB+128GB）+ 1年碎屏险套餐<i></i> </a> </li> <li class="disabled" versionid="20006" sku="000000000945058888" data-id="6" itemType="" title="全网通（6GB+64GB）+ 1年碎屏险套餐" > <a name="item_10985347748_ysc_size06" onclick="FourPage.changeVersion('000000010985347748','000000000945058888','20006',this);return false;" sa-data="{'eletp':'prd','prdid':'945058888','shopid':'0070094634','salestatus':'1'}" href="//product.suning.com/0070094634/945058888.html">全网通（6GB+64GB）+ 1年碎屏险套餐<i></i> </a> </li> <li class="disabled" versionid="20007" sku="000000000945055173" data-id="7" itemType="" title="全网通（4GB+64GB）+1年碎屏险套餐" > <a name="item_10985347748_ysc_size07" onclick="FourPage.changeVersion('000000010985347748','000000000945055173','20007',this);return false;" sa-data="{'eletp':'prd','prdid':'945055173','shopid':'0070094634','salestatus':'1'}" href="//product.suning.com/0070094634/945055173.html">全网通（4GB+64GB）+1年碎屏险套餐<i></i> </a> </li> <li class="disabled" versionid="20008" sku="000000000945058795" data-id="8" itemType="" title="移动版（4GB+128GB）+1年碎屏险套餐" > <a name="item_10985347748_ysc_size08" onclick="FourPage.changeVersion('000000010985347748','000000000945058795','20008',this);return false;" sa-data="{'eletp':'prd','prdid':'945058795','shopid':'0070094634','salestatus':'1'}" href="//product.suning.com/0070094634/945058795.html">移动版（4GB+128GB）+1年碎屏险套餐<i></i> </a> </li> </ul> <input type="hidden" /> </dd> </dl> <dl id="phonedl" class="proinfo-buytype proattr-radio proinfo-hyj" style="display:none;"> <dt>购买方式</dt> <dd> <ul class="clearfix"> </ul> <input type="hidden" /> </dd> </dl> <dl id="phoned2" class="proinfo-buytype proattr-radio proinfo-hyj-rel" style="display:none;"> <dt>合约类型</dt> <dd> </dd> </dl> <div class="tzm-border"> <div class="tip" id="nochooseInfo"><span>请选择您要的商品信息</span> </div> <a href="javascript:void(0);" class="close ng-iconfont">&#xe627;</a> </div> <dl id="nocodePackage" class="ncp proinfo-yanbao proattr-check" style="display:none;"> </dl> <div id="shouhou" class="sh-box sh-box" style="display: none"> <dl class="sh"> <dt>售后服务</dt> <dd> <ul id="afterSalesService" class="sh-list clearfix"> </ul> <div id="pcAfterSalesServiceText" class="sh-info"></div> <div class="follow-box" style="left: 154px; right: auto;"> <a href="javascript:;" class="ng-iconfont fold-icon" style="display: none;"></a> <a href="javascript:;" class="ng-iconfont extend-icon" style="display: none;"></a> </div> </dd> </dl> </div> <div class="renxf-box hide" id="freenessPay"> <dl class="renxf"> <dt>任&ensp;性&ensp;付</dt> <dd> <div class="rx-charge" id="rx_charge_box"> <span class="tri-pointer"> <i class="inner-tri"></i> </span> </div> <ul class="renxf-list clearfix hide" id="freenessInfo"> </ul> <div class="follow-box"> <span class="rxf-hui" id="freehui" style="display:none;"> </span> <a href="javascript:;" class="ng-iconfont fold-icon" name="item_10985347748_basic_renxingfu-unfold">&#xe63a;</a> <a href="javascript:;" class="ng-iconfont extend-icon" title="更多分期方案" name="item_10985347748_basic_renxingfu-unfold">&#xe62e;</a> <a href="//rxf.suning.com/" target="_blank" id="rxf-help-id" class="rxf-help" name="item_10985347748_gmq_rxfjs"> <span class="tool-tip" > <i class="a-up-arrow"></i> 任性付是苏宁推出的“先消费，后付款”的低息分期产品。支持闪电付款，最高20万，为消费者提供无抵押、免担保、0首付低利息、现金取现等服务 </span> </a> <span style="display:none" id="rxfmd" name="item_10985347748_gmq_rxfjs-hover"></span> </div> </dd> </dl> </div> <script type="text/javascript"> $("#rxf-help-id").hover(function(){ $("#rxfmd").click(); },function(){}); </script> <div class="sh-box o2o-box" style="display: none;" id="carPartO2O"></div> <dl id="yanbao" class="proinfo-yb proinfo-yanbao proattr-check" style="display:none;"> </dl> <dl id="insureCmmdty" class="proinfo-bx proinfo-yanbao proattr-check" style="display:none;"> </dl> <dl style="display:none;"> <script id="insureImpl" type="text/html"> <dt> <span class="w1">保险服务</span> </dt> <dd> <ul class="clearfix"> {{each insureList as insure i}} <li class='' data-id={{i}}> <a title='{{insure.productDesc}}' data-id='{{insure.commodityCode}}' data-vendor='{{insure.supplierCode}}' data-littlecateCode="{{insure.littleCateCode}}" name='{{insure.clickName}}' href='javascript:void(0);' class=''> <img class='icon_img' src='{{insure.logo}}'/> <span>{{insure.insureCmmdtyName}}&nbsp&nbsp&yen{{insure.basePrice}}</span> <i class='flag'></i> </a> </li> {{/each}} </ul> <input type='hidden'> <div class='follow-box'> <i class='ng-iconfont fold-icon' name=''>&#xe63a;</i> <i class='ng-iconfont extend-icon' title='更多保险' name=''>&#xe62e;</i> </div> </dd> </script> </dl> <dl class="proinfo-rentnum" id="leasePlatform" style="display:none;"> <dt><span class="w2">租期</span></dt> <dd> <a href="javascript:void(0);" class="minus func minus-disable"></a> <input type="text" id="leasePlatformText" value="1" min="1" max="30"> <a href="javascript:void(0);" class="plus func"></a> <span class="tip">天</span> <span class="tip" id="leasePlatformTip"><em></em></span> </dd> </dl> <dl id="buycount" class="proinfo-num" style="display:none;"> <dt><span class="w2">数量</span></dt> <dd><a href="javascript:void(0);" class="func minus" name="item_10985347748_gmq_fuhao-"></a><input id="buyNum" type="text" value="1" max="99" /><a href="javascript:void(0);" class="func plus" name="item_10985347748_gmq_fuhaojia"></a> <span id="productLimit" class="tip" style="display:none;">每人限购20件</span> <span id="kcjz" class="tip" style="display:none;font-weight: 600;"></span> <a id="sfrz" style="display:none;" href="//my.suning.com/getEnterpriseMemberIdentity.do" class="b jump" target="_blank">身份认证，享受大单采购</a> </dd> </dl> </div> <dl id="bigPolyVerify" class="hide"></dl> <div class="mainbtns clearfix"> <a id="buyNowAddCart" name="item_10985347748_gmq_ljgm-1shouji" class="btn-dark-buy" href="javascript:Cart.buyNowTime();" style="display:none;" sa-data="{'eletp':'buynow','prdid':'10985347748','shopid':'0070094634','salestatus':'1'}"><span>立即购买</span></a> <a id="saleRemind" name="item_10985347748_gmq_buy01-1shouji" class="btn-orange-buy btn-disabled" href="javascript:void();" style="display:none;"><i></i>开售提醒</a> <a id="addCart" name="item_10985347748_gmq_buy01-1shouji" class="btn-orange-buy btn-disabled" href="javascript:void();" sa-data="{'eletp':'addtocart','prdid':'10985347748','shopid':'0070094634','salestatus':'1'}"><i></i>加入购物车</a> <a id="superBuy" name="item_10985347748_supertqq_click" class="btn-dark-buy-super" href="javascript:void();" style="display:none;" sa-data="{'eletp':'buynow','prdid':'10985347748','shopid':'0070094634','salestatus':'1'}"><p>提前抢</p><p>SUPER会员专享</p></a> <a id="tellMe" name="item_10985347748_gmq_daohuotz01" class="btn-inform" href="javascript:FourPage.subscribeArrivalNotice();" style="display:none;"><span>到货通知</span></a> <div href="javascript:;" class="qrcode-panel" id="qrCode" style="display: none;" name="item_10985347748_basic_QR-hover"> <div class="qrc-wrapper" style="height: 0px;"> <img onerror="javascript:$('#qrCode').hide();" class="b-img"> </div> <div class="q-bottom"> <span class="s-img"></span> <div class="q-text"> <div class="cli-buy txt">客户端购买</div> <div class="q-cut txt">立减5元</div> </div> <i class="ng-iconfont">&#xe62e;</i> </div> </div> <span class="memo" id="yushouTimeWarn" style="display:none;">请在下单后15分钟之内完成支付</span> <a class="btn-ziti link hide" id="btn_mdjt" href="javascript:void(0);">查看现货门店 ></a> <span class="memo" style="display:none;" id="jhsm">注：预约享受优先购买权</span> </div> <p class="proinfo-memo" id="buyReminder" style="display: none;"><span>由于此商品库存有限，请在下单后15分钟之内支付完成，手慢无哦！</span></p> <div class="divide-line"></div> <dl class="pro-serv-panel"> <dt><span class="w2">服务</span></dt> <dd class="proinfo-serv clearfix" id="proinfo-id"> <span id="returnCate" style="display:none;" name="item_10985347748_basic_7days-hover"> <a rel="nofollow" class="wly no-link" target="_blank"> </a> </span> <span id="zb180" style="display: none;"> <a rel="nofollow" href="//sale.suning.com/ju/b2cfwbz0405/index.html" target="_blank" class="zb-180"> </a> </span> <span id="returnGoods" style="display: none;" forHyjFlag="0"> <a rel="nofollow" href="//help.suning.com/page/channel-376.htm" target="_blank" class="replace"><i class="icon"></i>300天坏就换</a> </span> <span id="yfxian" style="display:none;" name="item_10985347748_basic_carriage-insurance-hover"> <a class="tyfx" rel="nofollow" href="//help.suning.com/page/channel-354.htm" target="_blank"> <i class="icon"></i>退运费险 <span class="s-tooltip"> <i class="s-t-lion"></i>赠送退货运费险 <span class="tri-pointer-up"> <i class="inner-tri"></i> </span> </span> </a> </span> <span > <a rel="nofollow" href="//b.suning.com" target="_blank" class="zqcg blue-bg" name="item_10985347748_basic_purchaser"> <i class="icon"></i>企业采购 <span class="s-tooltip"> <i class="s-t-lion"></i> 针对企业客户采购的专业服务 <span class="tri-pointer-up"> <i class="inner-tri"></i> </span> </span> </a> </span> </dd> </dl> <div class="ng-rec-con lazy-ajax" style="display: none" id="J-slide1" data-type="jsonp"> </div> <script id="noSale-rec-tmpl" type="text/html"> {{if type == "1" || type == "2"}} <div class="ng-rec-con-1 clearfix"> {{else}} <div class="hot-title"> 热销推荐 </div> {{if type == "0"}} <div class="ng-rec-1 ng-rec-2" id="ng_hot_sale_1"> {{else}} <div class="ng-rec-1" id="ng_hot_sale"> {{/if}} {{/if}} {{if type == "1" || type == "2"}} <div class="same-box l" sap-modid="11"> <div class="hot-title"> <a href="//rec.suning.com/show/find/0070094634/10985347748.html" target="_blank">同款推荐</a> </div> <div class="same-pdt"> <div class="img"> <a href="{{identify.eleHref}}" id="{{identify.eleId}}" sa-data="{{identify.saData}}" name="{{identify.eleName}}" target="_blank"><img src="{{identify.eleSrc}}" alt=""></a> <i class="the-same"></i> {{if identify.promotionInfo && identify.promotionInfo!=""}} <label for="" class="com-label">{{identify.promotionInfo}}</label> {{/if}} </div> <div class="p-infos"> <a href="{{identify.eleHref}}" id="{{identify.eleId}}" sa-data="{{identify.saData}}" name="{{identify.eleName}}" target="_blank"><p class="title">{{identify.sugGoodsName}}</p></a> <p class="price"><i>&yen;</i> {{identify.price}}</p> <p class="review" style="display: none" >累计评价 <i></i> </p> <p class="stores" style="display: none" >商家： <strong>苹果店</strong> </p> </div> </div> </div> <div class="rec-box l " sap-modid="12"> <div class="hot-title">热销推荐</div> <div class="ng-rec-1 ng-rec-3" id="ng_hot_sale_2"> {{/if}} {{if type == "2"}} <div class="ng-rec-list"> <div class="scroll-wrapper clearfix"> <ul class="clearfix"> {{each specialSku as value i}} <li> {{if value.identify == "1"}} <i class="the-same"></i> {{/if}} <a href={{if value.adtype == "1" && value.apsClickUrl}}"{{value.apsClickUrl}}"{{else}}"{{value.eleHref}}"{{/if}} id="{{value.eleId}}" sa-data="{{value.saData}}" name="{{value.eleName}}" target="_blank"><img src="{{value.eleSrc}}" alt=""></a> <p class="title"><a href={{if value.adtype == "1" && value.apsClickUrl}}"{{value.apsClickUrl}}"{{else}}"{{value.eleHref}}"{{/if}} sa-data="{{value.saData}}" name="{{value.eleName}} target="_blank">{{value.sugGoodsName}}</a></p> <p class="price"><i>&yen;</i> {{value.price}} {{if (value.adtype == "1")}} <label class="com-label-ad">广告</label> {{else if value.promotionInfo && value.promotionInfo!=""}} <label for="" class="label">{{value.promotionInfo}}</label> {{/if}} </p> </li> {{/each}} </ul> </div> </div> </div> </div> </div> <div class="ng-rec-1" id="ng_hot_sale"> {{/if}} <div class="ng-rec-list"> <div class="scroll-wrapper clearfix"> {{each skus as value i}} {{if (i+1)% skuNum == 1}} <ul class="clearfix"> {{/if}} <li> {{if value.identify == "1"}} <i class="the-same"></i> {{/if}} <a href={{if value.adtype == "1" && value.apsClickUrl}}"{{value.apsClickUrl}}"{{else}}"{{value.eleHref}}"{{/if}} id="{{value.eleId}}" sa-data="{{value.saData}}" name="{{value.eleName}}" target="_blank"><img src="{{value.eleSrc}}" alt=""></a> <p class="title"><a href={{if value.adtype == "1" && value.apsClickUrl}}"{{value.apsClickUrl}}"{{else}}"{{value.eleHref}}"{{/if}} sa-data="{{value.saData}}" name="{{value.eleName}} target="_blank">{{value.sugGoodsName}}</a></p> <p class="price"><i>&yen;</i> {{value.price}} {{if (value.adtype == "1")}} <label class="com-label-ad">广告</label> {{else if value.promotionInfo && value.promotionInfo!=""}} <label for="" class="label">{{value.promotionInfo}}</label> {{/if}} </p> </li> {{if (i+1)% skuNum == 0 || (i+1) == skus.length}} </ul> {{/if}} {{/each}} </div> </div> <a class="com-prev" href="javascript:void(0);"></a> <a class="com-next" href="javascript:void(0);"></a> {{if type == "2"}} </div> {{/if}} {{if type == "1"}} </div> </div> {{/if}} {{if type == "0" || type == "1" || type == "3"}} </div> {{/if}} </script> <div id="cshopBox" class="proinfo-side"> <div class="proinfo-side-inner"> <script type="text/html" id="customer-rec-tmpl"> {{each skus as sku i}} {{if (i+1)%htmlnum == 1}} <ul> {{/if}} {{if sku.alwaysBuyFlag=="0"}} <li class="cgqd" title ="{{sku.sugGoodsName}}"> <img src="{{if sku.elePic!=''}}{{sku.elePic}}{{else}}{{sku.eleSrc}}_120x120.jpg{{/if}}"> <div class="title">常购清单</div> <div class="line"></div> <div class="check">立即查看&nbsp;&gt;</div> {{if (sku.promotionInfo != "")}} <div class="note">{{sku.promotionInfo}}</div> {{/if}} <a class="cgqd-link" href = "{{sku.checkHref}}" name="item_10985347748_shoppinglistright_click"></a> </li> {{else}} <li com-partinfo="{{sku.vendorId}}-{{sku.sugGoodsCode}}" com-name="{{sku.sugGoodsName}}" com-price="{{sku.price}}" com-check="false"> <a class="product-img" sa-data="{'eletp':'prd','prdid':'{{sku.sugGoodsCode}}','shopid':'{{sku.vendorId}}','recvalue':'{{sku.handwork}}','salestatus':'1'}" target="_blank" name="{{sku.eleName}}" href={{if sku.sugType == "3" && sku.apsClickUrl}}"{{sku.apsClickUrl}}"{{else}}"{{sku.eleHref}}"{{/if}} title="{{sku.sugGoodsName}}"> <img alt="{{sku.sugGoodsName}}" src3="{{if sku.elePic!=''}}{{sku.elePic}}{{else}}{{sku.eleSrc}}_120x120.jpg{{/if}}"/> </a> <p> <a class="title" sa-data="{'eletp':'prd','prdid':'{{sku.sugGoodsCode}}','shopid':'{{sku.vendorId}}','recvalue':'{{sku.handwork}}','salestatus':'1'}" target="_blank" id="{{sku.eleId}}" name="{{sku.eleName}}" title="{{sku.sugGoodsName}}" href={{if sku.sugType == "3" && sku.apsClickUrl}}"{{sku.apsClickUrl}}"{{else}}"{{sku.eleHref}}"{{/if}}> {{if sku.zyFlag && sku.zyFlag == "1"}} <span class="zylable">自营</span> {{/if}} {{sku.sugGoodsName}} </a> <span class="price-c"><i>&yen;</i><em>{{sku.price}}</em> {{if (sku.adtype == "1")}} <label class="com-label-ad">广告</label> {{/if}} {{if (sku.promotionInfo != "")}} <label class="com-label ml10">{{sku.promotionInfo}}</label> {{/if}} </span> </p> </li> {{/if}} {{if (i+1)%htmlnum == 0 || (i+1) == skus.length}} </ul> {{/if}} {{/each}} </script> <script type="text/html" id="dot-pages-tmpl"> {{each skus as sku i}} {{if i == 0}} <span class="page-dot current"></span> {{else if (i+1)%htmlnum == 1}} <span class="page-dot"></span> {{/if}} {{/each}} </script> <div class="customer-rec" id="hyjImageTile" style="display:none"> </div> <div class="customer-rec" id="seeAgainTile" sap-modid="07"> <div class="customer-rec-title"> <div class="t-bg"></div> <h3> <span>看了又看</span> </h3> </div> <div class="customer-rec-list" style="display:none;" id="seeAndsee"> <div class="scroll-wrapper clearfix"> </div> <div class="pages-container"> <a href="javascript:;" class="l-arrow"></a> <span class="pages-dot"> <span class="page-dot current"></span> <span class="page-dot"></span> <span class="page-dot"></span> </span> <a href="javascript:;" class="r-arrow"></a> </div> </div> <div class="customer-rec-empty" style="display:none;" id="noAndsee"> <i></i><p>欢迎光临本店铺</p><p><a href="javascript:;" target="_blank">点我可查看更多商品哦~</a></p> </div> </div> </div> </div> <div class="scode-link-box hide" id="scode"> <a name="cprd_10985347748_gmq_smtd" title="请在下单后15分钟之内完成支付" href="javascript:YuShou.checkScode();" class="scode-link"></a> </div> <div class="shopping-guide r-n-store clearfix" id="shopingGuideContent" style="display:none;"></div> <script id="shopingGuideScriptContent" type="text/html"> <div class="sg-summary"> {{if searchStore == 1}} <i class="loc-icon"></i><strong >门店现货</strong><span>门店现货可售，钟爱触手可及</span> <a rel="nofollow" target="_blank" name="{{wuhuoMore}}" href="{{moreStoreUrl}}" class="more-st">更多门店</a> {{/if}} {{if searchStore == 0}} <i class="loc-icon"></i><strong >专业导购</strong><span>家电套装设计，线下全程接待</span> <a rel="nofollow" target="_blank" name="{{wuhuoMore}}" href="{{moreStoreUrl}}" class="more-st">更多门店</a> {{/if}} </div> <div class="sg-l2 clearfix"> {{if searchStore == 1}} <ul class="sg-stores l"> {{each vstore2ndInfos as storeGuide i}} {{if i < 4}} <li class="store l"> <div class="i-loc"></div> <div class="s-info"> <p class="st-name" title="{{storeGuide.storeName}}"> {{storeGuide.storeName}} </p> <p class="st-address"> {{storeGuide.storeAddress}} </p> <a target="_blank" name="{{wuhuo}}" href="{{vbuyDomain}}/vbuyshop.html?shopCode={{storeGuide.storeCode}}&guideId={{storeGuide.guideId}}&channel=10" class="btn-go l">去门店体验</a> </div> </li> {{/if}} {{/each}} </ul> {{/if}} {{if searchStore == 0}} <ul class="sg-girls l"> {{each vstore2ndInfos as storeGuide i}} {{if i < 4}} <li class="sg-item l"> <div class="girl-info"> <div class="g-portrait"> <img lazy-src="{{storeGuide.guidePhoto}}" alt="" /> <i ></i> </div> <div class="girl-r l"> <div class="store-address ">{{storeGuide.storeName}}</div> <p>{{storeGuide.guideName}}<span class="wk-txt">(已接<i class="order-num">{{storeGuide.orderNum}}</i>单)</span> </p> <a target="_blank" name="{{wuhuo}}" href="{{vbuyDomain}}/vbuyshop.html?shopCode={{storeGuide.storeCode}}&guideId={{storeGuide.guideId}}&channel=10" class="btn-go l">去门店找TA</a> </div> </div> </li> {{/if}} {{/each}} </ul> {{/if}} </div> </script> <script id="newShopingGuideScriptContent" type="text/html"> <div class="sg-summary"> <i class="loc-icon"></i><strong >{{tipTitle}}</strong><span>{{tipContent}}</span> {{if isRouteToSntk == 0}} <a rel="nofollow" target="_blank" name="{{wuhuoMore}}" href="{{moreStoreUrl}}" class="more-st">更多门店</a> {{/if}} </div> <div class="sg-l2 clearfix"> <ul class="sg-girls l"> <li class="sg-item l"> <div class="girl-info"> <div class="g-portrait"> <img lazy-src="{{guidePhoto}}" alt="" /> <i ></i> </div> <div class="girl-r l"> <div class="store-address ">{{storeName}}</div> <p>{{guideName}}<span class="wk-txt">(已接<i class="order-num">{{orderNum}}</i>单)</span> </p> <a target="_blank" name="{{wuhuo}}" href="{{vbuyDomain}}/vbuyshop.html?shopCode={{storeCode}}&guideId={{guideId}}&channel=10" class="btn-go l">去门店找TA</a> </div> </div> </li> </ul> </div> </script> </div> </div> <div id="bookProcedure" class="presell-process hide"> <div class="pp-header"> <div class="h-content"> <h3>商品预定流程：</h3> </div> </div> <ul class="clearfix"> <li id="depositTime" class="step-1 current"> <i class="icon-1"></i> <dl> <dt>付定金<span class="deposit-money"></span></dt> <dd></dd> <dd></dd> </dl> </li> <li class="sep">&gt;</li> <li class="step-2"> <i class="icon-2"></i> <dl> <dt>商家备货</dt> </dl> </li> <li class="sep">&gt;</li> <li id="balanceTime" class="step-3"> <i class="icon-3"></i> <dl> <dt>付尾款<span class="deposit-money"></span></dt> <dd></dd> <dd>结束：6月30日23:59</dd> </dl> </li> <li class="sep">&gt;</li> <li id="sendTime" class="step-4"> <i class="icon-4"></i> <dl> <dt>发货</dt> <dd>预计7月1日发货</dd> </dl> </li> <li id="dingJinTuan" class="presell-rule rule-fr" style="display: none;padding-left:0px;"> </li> </ul> </div> <div id="prebuy" class="bespoke-process" style="display:none;"> <div class="pp-header"> <div class="h-content"> <h3>预约抢购流程说明：</h3> </div> <div class="arr-bg"></div> </div> <ul class="clearfix"> <li class="step-1 current"> <i class="icon-1"></i> <dl> <dt>等待预约</dt> </dl> </li> <li class="sep">&gt;</li> <li id="appointTime" class="step-2"> <i class="icon-2"></i> <dl> <dt>预约中</dt> <dd></dd> <dd></dd> </dl> </li> <li class="sep">&gt;</li> <li class="step-3"> <i class="icon-3"></i> <dl> <dt>等待抢购</dt> </dl> </li> <li class="sep">&gt;</li> <li id="buyTime" class="step-4"> <i class="icon-4"></i> <dl> <dt>抢购中</dt> <dd></dd> <dd></dd> <dd></dd> </dl> </li> <li id="yuYueQiangGou" class="presell-rule rule-fr" style="display: none;"> </li> </ul> </div> </div> <div class="product-compare" style="display:none;"> <span class="p-c-close ng-iconfont"></span> <ul class="p-c-tabs clearfix"> <li class="p-t-item l selected" id="tab_prod_compare">商品对比</li> <li class="p-t-item l" id="tab_recent_view">同类别</li> </ul> <div class="p-compare-panel" style="display: block;"> <div class="p-c-pdts"> <ul> <li class="add-prompt clearfix" data-placeholder="1" style="display: none"> <div class="virtual-pic l">1</div> <div class="prom-text">您可以继续添加商品</div> </li> <li class="add-prompt clearfix" data-placeholder="2"> <div class="virtual-pic l">2</div> <div class="prom-text">您可以继续添加商品</div> </li> <li class="add-prompt clearfix" data-placeholder="3"> <div class="virtual-pic l">3</div> <div class="prom-text">您可以继续添加商品</div> </li> <li class="add-prompt clearfix" data-placeholder="4"> <div class="virtual-pic l">4</div> <div class="prom-text">您可以继续添加商品</div> </li> </ul> <a href="javascript:;" class="btn-start-compare" name="item_10985347748_db2_pro">开始对比</a> <a href="javascript:;" class="clear-c-list">清空对比栏</a> </div> </div> <div class="p-c-umaylike" style="display: block;" dataAble="false"> <div class="p-c-header"><span class="u-text">猜你喜欢</span></div> <div class="page-scroll-panel"> <div class="scroll-wrapper clearfix"> </div> <div class="pages-container"> <a href="javascript:;" class="l-arrow"></a> <span class="pages-dot"> <span class="page-dot current"></span> <span class="page-dot"></span> <span class="page-dot"></span> </span> <a href="javascript:;" class="r-arrow"></a> </div> </div> </div> <div class="p-c-recent-view" style="display: none;"> <div class="page-scroll-panel"> <div class="scroll-wrapper clearfix"> <ul class="pdt-list l clearfix"> </ul> </div> <div class="pages-container"> <a href="javascript:;" class="l-arrow"></a> <span class="pages-dot"> <span class="page-dot"></span> <span class="page-dot"></span> <span class="page-dot current"></span> </span> <a href="javascript:;" class="r-arrow"></a> </div> </div> </div> </div> <div class="prod-comp-prompt-dialog" style="display:none;"> 对比栏已满，一次最多可对比4件产品，建议您删除不需要的再添加哦 </div> <div class="imgview"> <div class="imgview-head"> <a href="//www.suning.com/bigimages/10985347748.html" target="_blank">查看大图</a> </div> <div class="imgview-main"> <img onerror="javascript:this.src='//res.suning.cn/project/pdsWeb/images/blank_pic_800.jpg'"/> <div class="mask-l"></div> <div class="mask-r"></div> <div class="imgview-count"><em></em>/<span></span> </div> </div> <div class="imgview-thumb"> <a href="javascript:void(0);" class="btn-dir prev prev-disable"></a> <div class="imgview-thumb-main"> <ul id="bigPic"> <li id="fenwei"> <a name="item_10985347748_sppic_xiaop01" href="javascript:void(0);"><img onerror="javascript:errorMainPicture(this);" alt="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待" src-large="//imgservice.suning.cn/uimg1/b2c/atmosphere/JkoiMX87alhsokZc4hgMIA.jpg_800w_800h_4e" src-medium="//imgservice.suning.cn/uimg1/b2c/atmosphere/JkoiMX87alhsokZc4hgMIA.jpg_800w_800h_4e" src="//imgservice.suning.cn/uimg1/b2c/atmosphere/JkoiMX87alhsokZc4hgMIA.jpg_100w_100h_4e"></a> </li> <li class="current"> <a href="javascript:void(0);"> <img alt="" onerror="javascript:errorMainPicture(this,true);" src-large="//imgservice.suning.cn/uimg1/b2c/image/783X00lIk6NabyNuOdOUbw.jpg_800w_800h_4e" src3="//imgservice.suning.cn/uimg1/b2c/image/783X00lIk6NabyNuOdOUbw.jpg_100w_100h_4e"> </a> </li> <li class="" data-index="2"> <a href="javascript:void(0);"> <img onerror="javascript:$('.imgview-thumb-main li[data-index=2]').remove();" alt="" src-large="//imgservice.suning.cn/uimg1/b2c/image/xB89vZYMlMVYaBKcQ-C2eA.jpg_800w_800h_4e" src3="//imgservice.suning.cn/uimg1/b2c/image/xB89vZYMlMVYaBKcQ-C2eA.jpg_100w_100h_4e"> </a> </li> <li class="" data-index="3"> <a href="javascript:void(0);"> <img onerror="javascript:$('.imgview-thumb-main li[data-index=3]').remove();" alt="" src-large="//imgservice.suning.cn/uimg1/b2c/image/ddzdq5kS5SRwp5Ks1cT1LA.jpg_800w_800h_4e" src3="//imgservice.suning.cn/uimg1/b2c/image/ddzdq5kS5SRwp5Ks1cT1LA.jpg_100w_100h_4e"> </a> </li> <li class="" data-index="4"> <a href="javascript:void(0);"> <img onerror="javascript:$('.imgview-thumb-main li[data-index=4]').remove();" alt="" src-large="//imgservice.suning.cn/uimg1/b2c/image/zNHgh6oIrHum6xRv-QpiKg.jpg_800w_800h_4e" src3="//imgservice.suning.cn/uimg1/b2c/image/zNHgh6oIrHum6xRv-QpiKg.jpg_100w_100h_4e"> </a> </li> <li class="" data-index="5"> <a href="javascript:void(0);"> <img onerror="javascript:$('.imgview-thumb-main li[data-index=5]').remove();" alt="" src-large="//imgservice.suning.cn/uimg1/b2c/image/aVo9V1fSQ7o7tEYbB9yeLw.jpg_800w_800h_4e" src3="//imgservice.suning.cn/uimg1/b2c/image/aVo9V1fSQ7o7tEYbB9yeLw.jpg_100w_100h_4e"> </a> </li> </ul> </div> <a href="javascript:void(0);" class="btn-dir next"></a> </div> <a href="javascript:void(0);" class="close">×</a> </div> <div class="guaCoupon-box" style="display: none;" id="couponBox-id"> <div class="screen-box"> <div class="coupon-box" > <div class="coupon-head"> <h2>云钻刮券</h2> <p class="msg"> 100%刮中券，最高50元无敌券，券有效期7天 </p> <i class="close" onclick="closeCouponBox()"></i> </div> <div class="coupon-info"> <div class="box-p"> <p class='p1 '>亲，今日还有<span class="num" id="coupon-num-id">0</span>次刮奖机会</p> <p class="p2">我的云钻:<span id="pointNum">0</span></p> </div> <div class="coupon-detail coup1 no-can" id="no-can-id" style="display: none"> <p class="p2">您的云钻暂时不足,攒足云钻再来刮</p> <div class="coupon-msg">200云钻刮一次</div> </div> <div class="coupon-detail coup1 can" id="can-id" style="display: none" onclick="executeScrape()"> <p class="p2"></p> <div class="coupon-msg">200云钻刮一次</div> </div> <div class="coupon-detail coup5 congratulate" style="display: none" id="coup5-id"> <p class="p2">恭喜获得1张券！</p> <div class="" onclick="executeScrape()" id="coupon-msg-id"></div> </div> <div class="coupon-detail coup2 no-chance" style="display: none" id="coup2-id"> <p class="p2">今天的机会已经全部用完了，请明天再来</p> </div> <div class="start-gua" id="start-gua-id" style="display: none" data-gua="resultCoupon"> <div class="coupon-detail coup3" id="canvas-box" style="display: none"> <canvas id="cvs" width="338" height="130"></canvas> </div> <div class="coupon-detail coup4" style="display: none" id="coupon-detail-id"> <p class="choice">恭喜刮出<span>两</span>张券，请选择一张领取</p> <div class="content" id="coupon-content-id"> </div> <div class="btn-errMsg"> <a href="javascript:CommonFourPage.ScrapeCoupon.sendScrapeCoupon();" class="receive_btn">立即领取</a> <span class="error-msg" id="getCouponErrorMsg-id"></span> </div> </div> <div class="coupon-detail coup6" style="display: none" id="gend-finish"> <img src="/pds-web/project/pds/csspc2017/images/gend-finish.gif"> <div class="gend-finish-tip">小苏正在为您抽奖<span>.</span><span style="visibility: visible;">.</span><span style="visibility: visible;">.</span></div> </div> </div> <div class="coupon-btn"> <a href="javascript:scrapeRule();" class="btn1">刮券规则&gt;</a> <a href="//quan.suning.com/yhq.do" name="item_10985347748_coupon_blow-mycoupon" target="_blank" class="btn2">我的优惠券&gt;</a> </div> </div> </div> <div class="coupon-box ml255" id="couponBoxRule-id"> <div class="coupon-head"> <h2 class="pb_15">刮券规则</h2> <i class="close" onclick="closeCouponBox()"></i> <i class="return" onclick="returnCouponBox()">&lt;</i> </div> <div class="coupon-info scrol"> <h2>云钻刮券活动规则</h2> <div class="box mt_20"> <h3>活动时间</h3> <p class="msgs"> 活动自2017年6月2日上线，敬请关注云钻刮券活动规则更新。 </p> </div> <div class="box mt_20"> <h3>活动形式</h3> <ul> <li> 会员打开苏宁易购wap端、PC端、苏宁易购APP端方可参与活动。 </li> <li> 活动方式为云钻刮券，每次刮券需要扣除200云钻。奖励分为无敌券和店铺云券两种，100%刮出无敌券，最低2元。店铺券由店铺提供，用户可以根据购物需求，在无敌券和店铺云券之间二选一。如因为网络、用户关闭等原因，造成页面关闭，导致用户没有或无法选择，系统将在5分钟内自动按照获得的无敌券面额发放到用户账户。 </li> <li> 每人每天参与刮券次数上限为3次。活动每日限量，如用户参与时已达到活动最高上限，则不能再继续参与，次日可以继续参与。 </li> <li> 如会员在刮券时选择了店铺云券，券发至账户后则无法再更改为平台的无敌券；如会员在刮券时选择了平台的无敌券，券发至账户后则无法再更改为店铺云券。 </li> <li> 云钻刮券获得的不固定面值的券，会随机获得无敌券：2~2.2元、5元、10元、20元、50元的无敌券或不同面额的店铺云券。 </li> <li> 券是否成功发放，可在“我的优惠券”中查询。 </li> </ul> </div> <div class="box mt_20"> <h3>其他</h3> <p> 如活动受政府机关指令需要停止举办的，或活动遭受严重网络攻击需暂停举办的，或者系统故障导致的其它意外问题，苏宁无需为此承担赔偿或者进行补偿。 </p> </div> <div class="box mt_20"> <h2>券使用规则</h2> <ul class="mt_20"> <li> 不同面额的无敌券有不同的使用门槛，2~2.2元、5元、10元、20元、50元无敌券为无门槛使用，具体以实际发放券说明为准。配送方式仅限选择配送使用，不能抵扣运费部分。 </li> <li> 用户刮券获得的店铺云券可与店铺内领取的店铺易券叠加使用。 </li> <li> 店铺云券使用门槛等具体信息以商家在其店铺内的设置使用说明为准。 </li> <li> 无敌券可用于单件商品的付款，也可用于购物车合并下单付款，同时支持在跨店铺订单中使用。店铺云券仅可使用在指定店铺中，注：部分店铺活动商品不支持用券，以订单实际提交为准。 </li> <li> 云钻刮券获得的无敌券可以购买大聚惠、抢购、团购、手机专享价，但不可购买闪拍、预售、S码、名品特卖、海外购、秒杀、虚拟产品、法律规定限制产品如一段奶粉（包括但不仅限列出的商品）等、云钻加钱兑及云钻全额兑。 </li> <li> 在购物时，点击购买后，页面会提示可使用易购券，只要点击选择易购券即可抵用扣除对应金额。云钻刮券获得无敌券或店铺云券使用时可用于抵扣商品金额，不能抵扣运费、运费险、增值服务等非商品金额。 </li> <li> 云钻刮券获得的无敌券或店铺云券可与店铺页面领取的店铺易券叠加使用，付款时默认优先使用力度较大的店铺优惠券，如使用店铺易券后的订单金额仍然满足云钻刮券所获得店铺云券使用条件，可继续叠加使用店铺云券。（举例：店铺在页面设置满199减50元的店铺易券，同时用户在店铺刮券获得一张满20元减20元的店铺云券，如商品订单金额为200元，会员在用已使用领取的50元店铺易券情况下，仍然可以使用云钻刮券获得20元店铺云券） </li> <li> 云钻刮券获得的无敌券或店铺云券不得提现，不得转赠他人，不得为他人付，不得拆分使用。 </li> <li> 一个订单最多使用6张易购券。 </li> <li> 云钻刮券获得的有效期为：自获得之日起7天内有效（部分活动券可能存在不同有效期，具体详见“我的优惠券”内易购券有效期说明）。 </li> <li> 在获取和使用券过程中，如果出现违规行为（如作弊领取、恶意套现、刷取信誉、虚假交易等），苏宁将取消用户的中奖资格，并有权撤销违规交易、收回易购券（含已使用的易购券及未使用的易购券）,必要时追究法律责任。 </li> <li> 使用易购券的订单若交易未成功或发生退款及售后，在交易所使用的易购券有效期内订单取消完成的，易购券将退回用户账户，退回后的易购券有效期不变。如在使用的易购券有效期之外发生退款，所使用的券退回当天有效，过期不予退还。如发生售后退款，易购券退回当天有效，过期不予退还。 </li> </ul> </div> </div> </div> </div> </div> <div class="wrapper tiein-box mt15" id="listProContent" style="display:none;"> <div class="tabarea" sap-modid="middleSecond"> <ul class="tabarea-items"> <li rel="#J-klyk" style="display:none;" has-data="false"><a href="javascript:void(0);">看了又看</a></li> <li rel="#J-manager-rec" style="display:none;" has-data="false"><a href="javascript:void(0);" name="item_10985347748_rec_shop-tab">店铺热销</a></li> <li rel="#J-holiday" class="" has-data="false" style="display:none;" > <a href="javascript:void(0);">热门推荐</a> </li> <li rel="#J-tieIn" class="" style="display:none;" has-data="false"><a href="javascript:void(0);" name="item_10985347748_rec_collocation">推荐搭配</a></li> </ul> <div class="tiein-tzm-pop"> <div class="title">请选择商品规格</div> <div class="main"></div> <div class="tip"> <span class="normal"></span> <span class="error"></span> </div> <div class="handle"> <a href="javascript:void(0);" class="btn-ok">确 认</a> <a href="javascript:void(0);" class="btn-cancel">取 消</a> </div> <i class="arr"></i> <a class="close" href="javascript:void(0);">&times;</a> </div> <div id="J-holiday" style="" class="tabarea-content holiday-rec-box lazy-ajax" data-type="jsonp" style="display:none;" sap-modid="10"></div> <div class="klyk-middle-list tabarea-content" id="J-klyk" style="display:none;" sap-modid="04"> <a class="btn-dir prev" href="javascript:void(0);"><span class="screen-count"><em class="cur-count">1</em>/<i class="total-count">1</i></span><i class="arr"></i></a> <a class="btn-dir next" href="javascript:void(0);"><span class="screen-count"><em class="cur-count">1</em>/<i class="total-count">1</i></span><i class="arr"></i></a> <div class="klyk-list"></div> </div> <div id="J-manager-rec" class="manager-list tabarea-content lazy-ajax" style="display:none;" data-type="jsonp" sap-modid="06"></div> <div id="J-tieIn" class="tiein tabarea-content lazy-ajax" sap-modid="05" style="display:none;" data-type="function"></div> </div> <script type="text/html" id="special-tmpl"> <div class="ha-cate-list"> <ul> <li class="ha_more"> <a href="{{middlePageUrl}}?partNumber={{partNumber}}" target="_blank" name="item_10985347748_rec_relevant-entrance"> <img lazy-src="{{entranceMapUrl}}" alt=""> </a> </li> {{each skus as sku i}} {{if i < num}} <li> <a href="{{middlePageUrl}}?labelCode={{sku.labelCode}}&partNumber={{partNumber}}" target="_blank" > <img lazy-src="{{sku.labelPic}}" alt="" name="item_{{ninePartNumber}}_rec_entrance-pic{{i+1}}"> </a> </li> {{/if}} {{/each}} </ul> </div> </script> <script type="text/html" id="special-tmpl2"> <div class="ha-rec-list "> <div class="ha_more"> <a href="{{middlePageUrl}}?partNumber={{partNumber}}" sa-data="{'eletp':'cuxiao','prdid':'10985347748'}" target="_blank" name="item_10985347748_rec_irrelevant-entrance"> <img lazy-src="{{entranceMapUrl}}" alt=""> </a> </div> <div class="ha-list"> <ul> {{each skus as sku i}} <li> <a href={{if sku.sugType == "3" && sku.apsClickUrl}}"{{sku.apsClickUrl}}"{{else}}"{{sku.eleHref}}"{{/if}} sa-data="{{sku.saData}}" target="_blank" name="{{sku.eleName}}" id="{{sku.eleId}}"><img src3="{{sku.eleSrc}}" alt=""></a> <p class="price"><i>¥</i> <em>{{sku.price1}}</em>.{{sku.price2}} {{if sku.zyFlag && sku.zyFlag == "1"}} <label class="com-has-border">苏宁自营</label> {{/if}} </p> <p class="p-title"><a href={{if sku.sugType == "3" && sku.apsClickUrl}}"{{sku.apsClickUrl}}"{{else}}"{{sku.eleHref}}"{{/if}} sa-data="{{sku.saData}}" target="_blank">{{sku.sugGoodsName}}</a></p> <p class="p-huodong"> {{if sku.promotionInfo && sku.promotionInfo!=""}} <span>{{sku.promotionInfo}}</span> {{/if}} {{if sku.activityDescriptionList && sku.activityDescriptionList.length > 0}} <span>{{sku.activityDescriptionList[0]}}</span> {{/if}} {{if (sku.adtype == "1")}} <label class="com-label-ad">广告</label> {{/if}} </p> </li> {{/each}} </ul> </div> <div class="pages-container"> <a href="javascript:;" class="l-arrow" name="item_10985347748_rec_qixi-previous"></a> <span class="pages-dot"><span class="page-dot current" data-page="0"></span><span class="page-dot" data-page="1"></span></span> <a href="javascript:;" class="r-arrow" name="item_10985347748_rec_qixi-next"></a> </div> </div> </script> <script type="text/html" id="tmpl_manager_rec_list"> <ul class="clearfix"> {{each skus as sku}} {{if sku.alwaysBuyFlag=="0"}} <li class="cgqd" title ="{{sku.sugGoodsName}}"> <img src="{{if sku.elePic!=""}}{{sku.elePic}}{{else}}{{sku.eleSrc}}_120x120.jpg{{/if}}"> <div class="title">常购清单</div> <div class="line"></div> <div class="check">立即查看&nbsp;&gt;</div> {{if (sku.promotionInfo != "")}} <div class="note">{{sku.promotionInfo}}</div> {{/if}} <a class="cgqd-link" href = "{{sku.checkHref}}" name="item_10985347748_shoppinglistmiddle_click"></a> </li> {{else}} <li class="klyk-middle-item"> <a target="_blank" id="{{sku.eleId}}" sa-data="{{sku.saData}}" name="{{sku.eleName}}" href={{if sku.sugType == "3" && sku.apsClickUrl}}"{{sku.apsClickUrl}}"{{else}}"{{sku.eleHref}}"{{/if}} title="{{sku.sugGoodsName}}"> <img alt="{{sku.sugGoodsName}}" lazy-src="{{if sku.elePic!=""}}{{sku.elePic}}{{else}}{{sku.eleSrc}}_160x160.jpg{{/if}}" /> </a> <p class="price"><i>¥</i> <em>{{sku.price1}}</em>.{{sku.price2}} {{if sku.zyFlag && sku.zyFlag == "1"}} <label class="com-has-border">苏宁自营</label> {{/if}} </p> <p class="p-title"><a target="_blank" sa-data="{{sku.saData}}" href={{if sku.sugType == "3" && sku.apsClickUrl}}"{{sku.apsClickUrl}}"{{else}}"{{sku.eleHref}}"{{/if}} title="{{sku.sugGoodsName}}">{{sku.sugGoodsName}}</a></p> <p class="p-huodong"> {{if sku.promotionInfo !=""}} <span>{{sku.promotionInfo}}</span> {{/if}} {{if sku.activityDescriptionList && sku.activityDescriptionList.length > 0}} <span>{{sku.activityDescriptionList[0]}}</span> {{/if}} {{if (sku.adtype == "1")}} <label class="com-label-ad">广告</label> {{/if}} </p> </li> {{/if}} {{/each}} </ul> </script> <script type="text/html" id="shoptj-sr-tmpl"> <ul class="clearfix"> {{each skus as sku i}} {{if i < 6}} <li> <a href="{{sku.eleHref}}" id="{{sku.eleId}}" sa-data="{{sku.saData}}" name="{{sku.eleName}}" target="_blank"> <img lazy-src="{{sku.eleSrc}}" title="{{sku.sugGoodsName}}"> </a> <p class="p-title"><a href="{{sku.eleHref}}" id="{{sku.eleId}}" sa-data="{{sku.saData}}" name="{{sku.eleName}}" target="_blank">{{sku.sugGoodsName}}</a></p> <p class="price"><i>¥</i>{{sku.price}} {{if sku.promotionInfo !=""}} <label class="com-label">{{sku.promotionInfo}}</label> {{/if}} </p> </li> {{/if}} {{/each}} </ul> </script> <script type="text/html" id="tjdp-sr-tmpl"> <div class="tiein-top"> <a href="{{topUrl}}" target="_blank"><img lazy-src="{{topImg}}" alt="{{topName}}"></a> <p class="title"><a href="{{topUrl}}">{{topName}}</a></p> <p class="price"><i>&yen</i> {{topPrice}}</p> <i class="plus"></i> </div> <div class="tiein-nav"> <a href="javascript:void(0);" class="current" name="item_{{ninePartNumber}}_rectjdpn_1-1_b_none_none_0">精选搭配</a> <span>|</span> {{each accCatgroups as groups i}} <a name="item_{{ninePartNumber}}_rectjdpn_1-{{i+1}}_b_none_none_0" data-type="{{groups.accCatgroupId}}" href="javascript:Recommend.initCatFitting({{i+1}},'{{groups.accCatgroupId}}','{{groups.accCatgroupName}}');" class="">{{groups.accCatgroupName}}</a> {{if (i+1) < accCatgroups.length}} <span>|</span> {{/if}} {{/each}} </div> <div class="tiein-main" id="J-slide-tieIn"> <a name="item_{{ninePartNumber}}_dapei_tabup" class="btn-dir prev" href="javascript:void(0);"><span class="screen-count"><em class="cur-count">1</em>/<i class="total-count">2</i></span><i class="arr"></i></a> <a name="item_{{ninePartNumber}}_dapei_tabdown" class="btn-dir next" href="javascript:void(0);"><span class="screen-count"><em class="cur-count">1</em>/<i class="total-count">2</i></span><i class="arr"></i></a> {{if skus.length > 0}} <div class="tiein-list"> <ul id="dapei_slide" style="left: 0px;"> {{each skus as sku i}} <li data-type="{{sku.catGroupId}}" data-id="{{sku.sugGoodsCode}}" data-rec="true" class=""> <a id="{{sku.eleId}}" sa-data="{{sku.saData}}" name="item_{{ninePartNumber}}_rectjdpn_1-{{i+1}}_p_{{sku.vendorId}}_{{sku.nineCode}}_{{sku.handwork}}" href="{{elecProductDomain}}/{{sku.vendorId}}/{{sku.nineCode}}.html#?src=item_{{ninePartNumber}}_rectjdpn_1-{{i+1}}_p_{{sku.vendorId}}_{{sku.nineCode}}_{{sku.handwork}}" target="_blank"><img src3="{{if sku.elePic!=""}}{{sku.elePic}}{{else}}{{tmImageDomianDir}}/uimg/b2c/newcatentries/{{sku.vendorId}}-{{sku.sugGoodsCode}}_1_100x100.jpg{{/if}}" alt="{{sku.sugGoodsName}}"></a> <p class="title"><a sa-data="{{sku.saData}}" name="item_{{ninePartNumber}}_rectjdpn_1-{{i+1}}_c_{{sku.vendorId}}_{{sku.nineCode}}_{{sku.handwork}}" href="{{elecProductDomain}}/{{sku.vendorId}}/{{sku.nineCode}}.html#?src=item_{{ninePartNumber}}_rectjdpn_1-{{i+1}}_c_{{sku.vendorId}}_{{sku.nineCode}}_{{sku.handwork}}" target="_blank">{{sku.sugGoodsName}}</a></p> <p class="price"><i>¥</i> {{sku.accPrice}} {{if (sku.promotionInfo != "")}} <label class="com-label ml10">{{sku.promotionInfo}}</label> {{/if}} </p> {{if (sku.diffPrice != "") && (sku.diffPrice > 0)}} <span class="label">已优惠 ¥{{sku.diffPrice}}</span> {{/if}} <i class="plus"></i> <input class="fitPartNumber" type="hidden" value="{{sku.sugGoodsCode}}"> <input class="fitVendorCode" type="hidden" value="{{sku.vendorId}}"> <input class="accessoryId" type="hidden" value="{{sku.activityId}}"> <input type="hidden" value="{{sku.highPrice}}" class="high"> <input type="hidden" value="{{sku.accPrice}}" class="low"> <input type="checkbox" class="check"> </li> {{/each}} </ul> </div> <div class="tiein-main-empty" style="display:none;"> <i></i> <span>抱歉，您选择的配件已售完，欢迎您选择其它配件!</span> </div> {{else}} <div class="tiein-main-empty"> <i></i> <span>抱歉，您选择的配件已售完，欢迎您选择其它配件!</span> </div> {{/if}} </div> <div class="tiein-count"> <p class="count">已搭配 <em>0</em> 件</p> <dl> <dt>套餐价：</dt> <dd class="price"><i>¥</i> <span id="yuanjia" class="price-total">{{topPrice}}</span></dd> </dl> <dl style="display:none;"> <dt>已优惠：</dt> <dd class="price"><i>¥</i> <span id="yhj" class="price-diff">0.00</span></dd> </dl> <div class="handle"> <a name="item_10985347748_dapei_buy02-1shouji" href="javascript:Cart.addCartPJ();" class="btn-addcart-mini">加入购物车</a> <a name="item_{{ninePartNumber}}_dapei_delete" href="javascript:void(0);" class="reset">清除全部</a> </div> </div> </script> </div> <div class="activity lazy-ajax" id="cmsActivityBar" data-type="function" style="display:none;"> </div> <div id="win_o2o" class="hide"> <div class="container"> <div class="title"> <h3>门店服务</h3> </div> <a href="javascript:;" class="btn close" title="关闭"><i class="gt">&gt;</i><i class="lt">&lt;</i></a> <div class="content"> <div class="o2o-service"> <dl class="areas"> <dt>区域：</dt> <dd> <ul class="clearfix" id="o2o_service_ul_districtList"> <li class="current" districtId="" name="item_10985347748_mdfw_quanbu" id="o2o_service_clone_li_districtId" > <a href="javascript:void(0);">全部</a> </li> </ul> <a class="more" href="javascript:void(0);">更多<i></i></a> </dd> </dl> <dl class="services"> <dt>服务：</dt> <dd> <ul id="o2o_service_store_service_ul"> <li id="win_o2o_spotGoods" style="display:none"><a href="javascript:void(0);" name="item_10985347748_mdfw_mdxh01">门店现货</a> </li> <li id="win_o2o_guideShop" style="display:none"><a href="javascript:void(0);" name="item_10985347748_mdfw_ddsc01">到店试</a> </li> </ul> </dd> </dl> <div class="o2o-service-main o2o-com-loading"> <ul> <li id="o2o-service-clone-storeList-li" style="display:none"> <div class="handle" style="display:none"><a href="javascript:;" target="_blank">&gt;</a></div> <h5><i class="icon"></i><a href="###" target="_blank"></a></h5> <p title="完整内容">地址：</p> </li> </ul> <div class="watermark"></div> </div> <div class="no-data no-shop hide">很抱歉，该区域暂无门店支持V购服务，正努力开放中•••</div> <div class="no-data no-goods hide">很抱歉，该区域暂无门店有现货，正努力补货中•••</div> </div> </div> </div> </div> <div class="overlay" id="J-overlay"> <div class="overlay-main"></div> <!--[if IE 6]><iframe class="frame" src="about:blank" frameborder="0"></iframe><![endif]--> </div> <div class="fixbar" id="J-fixBar"><div class="wrapper"><div class="fix-store"><div class="fix-store-name" id="fix-store"> <h3 title="华科手机专营店"> <a target="_blank" name="item_10985347748_shop_dianpu02" href="//shop.suning.com/70094634/index.html">华科手机专营店</a> </h3> <a href="javascript:;" class="l-icon contact-me-shop" name="item_zddh_agent" id="itemZddhAgent" ></a> </div> </div> <div class="area"></div> </div> </div> <div id="mini-cart-container" style="display:none;"> <div class="fix-qr-code"> <div class="qrcode-region" id="fixQrcode" style="display: none;" data-time="3"> <span>手机扫码购买</span> <em class="ph-qr-icon"></em> <i class="ng-iconfont down-i"></i> <i class="ng-iconfont up-i"></i> <div class="qrc-wrapper" name="item_10985347748_zddh_QR-hover"> <img onerror="javascript:$('#fixQrcode').hide();" class="b-img"> </div> </div> </div> <div id="tabAddCart" class="handle" style="display: none;"> <a id="addCart2" sa-data="{'eletp':'addtocart','prdid':'10985347748','shopid':'0070094634','salestatus':'1'}" name="item_10985347748_tab_buy03-1shouji" class="btn-orange-mini btn-disabled-mini" href="javascript:void(0);">加入购物车</a> <div class="proinfo-mini"> <p class="pro-img"> <img height="60" width="60" lazy-src="//imgservice.suning.cn/uimg1/b2c/image/783X00lIk6NabyNuOdOUbw.jpg_60w_60h_4e" alt="华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待"/> </p> <p class="pro-name">华为(HUAWEI) 畅享9S 2400万超广角三摄珍珠屏 全网通版 4GB+128GB 幻夜黑 移动联通电信4G手机 双卡双待</p> <p class="pro-price"><span class="price"><i>&yen;</i> <em id="cart2Price"></em></span><span class="count"> ×<em id="cart2Count">1</em></span></p> </div> </div> </div> <script type="text/javascript" src="//res.suning.cn/??/project/pdsWeb/pc2017/template-min.js,/project/pdsWeb/pc2017/iFourth-min.js,/project/pdsWeb/pc2017/itemComDataLoadNew-min.js,/project/pdsWeb/pc2017/inititem-min.js,/project/pdsWeb/pc2017/Mp4player.min20181116141000.js,/project/pdsWeb/pc2017/SFE.city-min.js,/project/crdnode/common/tingyun.js?v=2019071306"> </script> <div id="nogoods-dialog-content" class="hide"> <script id="noGoodsPopBox" type="text/html" > <div class="nogoods-dialog-container"> <div class="nogoods-lion"></div> <div class="nogoods-msg"><span class="nogoods-msg-tick"></span>您选购的商品暂不支持销售，<span class="nogoods-msg-time"></span>秒后为您跳转到同款商品</div> <div class="btn-box"> <a href="{{hrefUrl}}" class="btn1" name="{{onClick}}">立即跳转</a> </div> </div> </script> </div> <script type="text/javascript"> $(function(){ FourPage.initialize(); }); </script> <div class="wrapper mt15"> <div class="procon-side" sap-modid="loverLeft"> <div class="si-intro" sap-modid="03"> <div class="si-intro-head"> <div class="bg"></div> <h4 class="si-intro-head-sj"><i></i><span>苏宁商家</span></h4> </div> <div class="si-intro-list"> <dl> <dt>商家：</dt> <dd> <a target="_blank" name="item_10985347748_shop_dianpu02" href="//shop.suning.com/70094634/index.html">华科手机专营店</a> <script type="text/javascript"> $("#curShopName").attr("title",$("#curShopName").html()); </script> </dd> </dl> <dl id="shopServerExperience" style="display:none;"> <dt>服务体验：</dt> <dd> <span class="star-bg"> <i class="star-val" style="width: 100%;"></i> </span> </dd> </dl> <dl> <dt>联系：</dt> <dd id="onlineTile"> <a href="#" id="callmeTile" name="item_10985347748_shop_agent" class="contact-me contact-me-shop"><i></i>联系客服</a> </dd> </dl> <dl> <dt>电话：</dt> <dd> <p>0755-82624400</p> </dd> </dl> </div> <div class="si-intro-trend lazy-ajax" id="shopScoreTrend" data-type="jsonp"> <ul> <li> <p><span>商品</span></p> <p class="up"><em id="gSatisfy"></em><i></i></p> </li> <li> <p><span>服务</span></p> <p class="up"><em id="sSatisfy"></em><i></i></p> </li> <li> <p><span>物流</span></p> <p class="up"><em id="dSatisfy"></em><i></i></p> </li> </ul> </div> <div class="si-intro-handle2"> <a name="item_10985347748_shop_jinru02" href="//shop.suning.com/70094634/index.html" sa-data="{'eletp':'shop','shopid':'0070094634'}" class="si-entry" target="_blank" title="进入店铺">进入店铺</a> <a name="item_10985347748_shop_shoucang02" class="si-fav" title="关注店铺" href="javascript:FourPage.addShopFavorite();">关注店铺</a> </div> </div> <div class="area mt10"> <div class="area-head"><h3>搜索店内商品</h3></div> <div class="menu-con-new sea-con-new"> <ul> <li> <strong>关键词：</strong> <input id="shopKeyWord" class="inptxt key" type="text" value=""> </li> <li> <strong>价&ensp;&ensp;格：</strong> <input id="slowPrice" class="inptxt inprice" type="text" value=""> <span>-</span> <input id="highPrice" class="inptxt inprice" type="text" value=""> </li> <li> <strong class="l"></strong> <a name="item_10985347748_mingpian_search" class="btn-search" href="javascript:CommonFourPage.FourPage.onShopSubmitSearch();"><span>确定</span></a> </li> </ul> <div class="clear"></div> </div> </div> <div class="area mt10 sfsDIV"> <div class="area-head"><h3>商品分类</h3></div> <div class="menu-con-new type-con-new"> <div class="type-all"> <a class="allType" name="item_10985347748_cata_all" href="//shop.suning.com/70094634/list_all_0.html">全部商品</a> </div> <div class="type-sort"> <a name="item_10985347748_cata_sales" href="//shop.suning.com/70094634/search?keyWord=&price=-&dimension=totalCount-desc" title="按销量" id="assortSalesVolume_n" target="_blank">按销量</a> <a name="item_10985347748_cata_new" href="//shop.suning.com/70094634/search?keyWord=&price=-&dimension=createTime-desc" title="按新品" id="assortNewProduct_n" target="_blank">按新品</a> <a name="item_10985347748_cata_price" href="//shop.suning.com/70094634/search?keyWord=&price=-&dimension=price-asc" title="按价格" id="assortPrice_n" target="_blank">按价格</a> </div> </div> </div> <script type="text/javascript"> CommonFourPage.Recommend.getShopCategory(sn.vendorCode,'processShopCategory'); </script> <div class="area mt10 searchDIV hide" id="shopSort"> <div class="area-head"><h3>商品分类</h3></div> <div class="menu-con-new type-con-new"> <div class="type-all"> <a class="allType" name="item_10985347748_cata_all" href="//shop.suning.com/70094634/list_all_0.html">全部商品</a> </div> <div class="type-sort"> <a name="item_10985347748_cata_sales" href="//shop.suning.com/70094634/search?keyWord=&price=-&dimension=totalCount-desc" title="按销量" id="assortSalesVolume_n" target="_blank">按销量</a> <a name="item_10985347748_cata_new" href="//shop.suning.com/70094634/search?keyWord=&price=-&dimension=createTime-desc" title="按新品" id="assortNewProduct_n" target="_blank">按新品</a> <a name="item_10985347748_cata_price" href="//shop.suning.com/70094634/search?keyWord=&price=-&dimension=price-asc" title="按价格" id="assortPrice_n" target="_blank">按价格</a> </div> <dl class="on"> <dt class="default_title fold_title "><a href="javascript:void(0);" class="folder"></a><a name="item_10985347748_cata_fcata01" target="_blank" href="//shop.suning.com/70094634/list_200137170_1.html">华为（HUAWEI）</a><em></em></dt> </dl> <dl class="on"> <dt class="default_title fold_title "><a href="javascript:void(0);" class="folder"></a><a name="item_10985347748_cata_fcata02" target="_blank" href="//shop.suning.com/70094634/list_200142000_1.html">小米(mi)</a><em></em></dt> </dl> <dl class="on"> <dt class="default_title fold_title "><a href="javascript:void(0);" class="folder"></a><a name="item_10985347748_cata_fcata03" target="_blank" href="//shop.suning.com/70094634/list_200146857_1.html">努比亚（nubia）</a><em></em></dt> </dl> <dl class="on"> <dt class="default_title fold_title "><a href="javascript:void(0);" class="folder"></a><a name="item_10985347748_cata_fcata04" target="_blank" href="//shop.suning.com/70094634/list_200212346_1.html">魅族(MEIZU)</a><em></em></dt> </dl> <dl class="on"> <dt class="default_title fold_title "><a href="javascript:void(0);" class="folder"></a><a name="item_10985347748_cata_fcata05" target="_blank" href="//shop.suning.com/70094634/list_210175477_1.html">荣耀(honor)</a><em></em></dt> </dl> <dl class="on"> <dt class="default_title fold_title "><a href="javascript:void(0);" class="folder"></a><a name="item_10985347748_cata_fcata06" target="_blank" href="//shop.suning.com/70094634/list_210465552_1.html">苹果(Apple)</a><em></em></dt> </dl> <dl class="on"> <dt class="default_title fold_title "><a href="javascript:void(0);" class="folder"></a><a name="item_10985347748_cata_fcata07" target="_blank" href="//shop.suning.com/70094634/list_210471236_1.html">诺基亚(NOKIA)</a><em></em></dt> </dl> <dl class="on"> <dt class="default_title fold_title "><a href="javascript:void(0);" class="folder"></a><a name="item_10985347748_cata_fcata08" target="_blank" href="//shop.suning.com/70094634/list_210471237_1.html">美图手机</a><em></em></dt> </dl> <dl class="on"> <dt class="default_title fold_title "><a href="javascript:void(0);" class="folder"></a><a name="item_10985347748_cata_fcata09" target="_blank" href="//shop.suning.com/70094634/list_210602609_1.html">一加</a><em></em></dt> </dl> </div> <script type="text/javascript"> iFourth.detailSide(); </script> </div> <script id="scoreScript" type="text/html"> <ul> <li> <p><span>商品</span></p> <p class="{{qualitySupClass}}"><em id="gSatisfy">{{qualityStar}}</em><i></i></p> </li> <li> <p><span>服务</span></p> <p class="{{attitudeSupClass}}"><em id="sSatisfy">{{attitudeStar}}</em><i></i></p> </li> <li> <p><span>物流</span></p> <p class="{{deliverySpeedSupClass}}"><em id="dSatisfy">{{deliverySpeedStar}}</em><i></i></p> </li> </ul> </script> <script id="newScoreScript" type="text/html"> <ul> {{each scoreInfo as score i}} <li> <p><span>{{score.name}}</span></p> <p class="{{score.clazz}}"><em id="{{score.code}}">{{score.value}}</em><i></i></p> </li> {{/each}} </ul> </script><div id="viewAndBuyContent" class="lazy-ajax area mt10" sap-modid="15" data-type="jsonp"> </div> <script id="viewAndBuyScriptContent" type="text/html"> <div class="area-head"><h3>看了最终买</h3></div> <ul class="exprec" id="vab"> {{each skus as value i}} {{if i<5 }} <li com-partinfo="{{value.vendorId}}-{{value.sugGoodsCode}}" com-name="{{value.sugGoodsName}}" com-price="{{value.price}}" com-check="false"> <a target="_blank" name="{{value.eleName}}" href={{if value.sugType == "3" && value.apsClickUrl}}"{{value.apsClickUrl}}"{{else}}"{{value.eleHref}}"{{/if}} title="{{value.sugGoodsName}}"> <img class="image" alt="{{value.sugGoodsName}}" lazy-src="{{if value.elePic!=""}}{{value.elePic}}{{else}}{{value.eleSrc}}_120x120.jpg{{/if}}"> </a> <p class="title"> <a target="_blank" id="{{value.eleId}}" name="{{value.eleName}}" title="{{value.sugGoodsName}}" href={{if value.sugType == "3" && value.apsClickUrl}}"{{value.apsClickUrl}}"{{else}}"{{value.eleHref}}"{{/if}}>{{if value.productType==1}}<span class="zylable">自营</span>{{/if}}{{value.sugGoodsName + value.sugGoodsDes}}</a> </p> <p class="price-c"> <span><i>&yen; </i><em>{{value.price}}</em> {{if value.promotionInfo!="" }}<label class="com-label ml10">{{value.promotionInfo}}</label>{{/if}} </span> {{if (value.adtype == "1")}} <label class="com-label-ad">广告</label> {{/if}} </p> <i class="g-sticker-60"><b class="g-s-1"></b></i> </li> {{/if}} {{/each}} </ul> </script><div class="lazy-ajax area mt10" id="hotRank" sap-modid="09" data-type="jsonp"> <div class="area-head hide"><h3><a href="//rec.suning.com/show/rankdetail/20002_2.html" target="_blank">手机通讯排行榜</a></h3></div> <li> <a href="//product.suning.com/0000000000/10973073407.html" title="华为/HUAWEI P30 亮黑色 8GB+128GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机"> <img alt="华为/HUAWEI P30 亮黑色 8GB+128GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机" lazy-src="//image3.suning.cn/uimg/b2c/newcatentries/0000000000-000000010973073407_1_60x60.jpg"> </a> <a href="//www.suning.com/prdCom/0070094634-10985347748_0000000000-10973073407_0-0_0-0.html">华为(HUAWEI)畅享9S手机和华为/HUAWEI P30 亮黑色 8GB+128GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机哪个好</a> <p class="title"> <a title="华为/HUAWEI P30 亮黑色 8GB+128GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机" target="_blank" href="//product.suning.com/0000000000/10973073407.html">华为/HUAWEI P30 亮黑色 8GB+128GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机</a> </p> <p class="price"><i>¥</i></p> <span class="num highlight">0</span> </li> <li> <a href="//product.suning.com/0000000000/10973073658.html" title="华为/HUAWEI P30 Pro 亮黑色 8GB+128GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机"> <img alt="华为/HUAWEI P30 Pro 亮黑色 8GB+128GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机" lazy-src="//image4.suning.cn/uimg/b2c/newcatentries/0000000000-000000010973073658_1_60x60.jpg"> </a> <a href="//www.suning.com/prdCom/0070094634-10985347748_0000000000-10973073658_0-0_0-0.html">华为(HUAWEI)畅享9S手机和华为/HUAWEI P30 Pro 亮黑色 8GB+128GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机哪个好</a> <p class="title"> <a title="华为/HUAWEI P30 Pro 亮黑色 8GB+128GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机" target="_blank" href="//product.suning.com/0000000000/10973073658.html">华为/HUAWEI P30 Pro 亮黑色 8GB+128GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机</a> </p> <p class="price"><i>¥</i></p> <span class="num highlight">1</span> </li> <li> <a href="//product.suning.com/0000000000/11177564390.html" title="华为/HUAWEI nova 5 Pro 前置3200万人像超级夜景 4800万AI四摄 8GB+128GB 绮境森林 移动联通电信4G拍照全网通手机"> <img alt="华为/HUAWEI nova 5 Pro 前置3200万人像超级夜景 4800万AI四摄 8GB+128GB 绮境森林 移动联通电信4G拍照全网通手机" lazy-src="//image1.suning.cn/uimg/b2c/newcatentries/0000000000-000000011177564390_1_60x60.jpg"> </a> <a href="//www.suning.com/prdCom/0070094634-10985347748_0000000000-11177564390_0-0_0-0.html">华为(HUAWEI)畅享9S手机和华为/HUAWEI nova 5 Pro 前置3200万人像超级夜景 4800万AI四摄 8GB+128GB 绮境森林 移动联通电信4G拍照全网通手机哪个好</a> <p class="title"> <a title="华为/HUAWEI nova 5 Pro 前置3200万人像超级夜景 4800万AI四摄 8GB+128GB 绮境森林 移动联通电信4G拍照全网通手机" target="_blank" href="//product.suning.com/0000000000/11177564390.html">华为/HUAWEI nova 5 Pro 前置3200万人像超级夜景 4800万AI四摄 8GB+128GB 绮境森林 移动联通电信4G拍照全网通手机</a> </p> <p class="price"><i>¥</i></p> <span class="num highlight">2</span> </li> <li> <a href="//product.suning.com/0000000000/10973073437.html" title="华为/HUAWEI P30 天空之境 8GB+128GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机"> <img alt="华为/HUAWEI P30 天空之境 8GB+128GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机" lazy-src="//image4.suning.cn/uimg/b2c/newcatentries/0000000000-000000010973073437_1_60x60.jpg"> </a> <a href="//www.suning.com/prdCom/0070094634-10985347748_0000000000-10973073437_0-0_0-0.html">华为(HUAWEI)畅享9S手机和华为/HUAWEI P30 天空之境 8GB+128GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机哪个好</a> <p class="title"> <a title="华为/HUAWEI P30 天空之境 8GB+128GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机" target="_blank" href="//product.suning.com/0000000000/10973073437.html">华为/HUAWEI P30 天空之境 8GB+128GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机</a> </p> <p class="price"><i>¥</i></p> <span class="num highlight">3</span> </li> <li> <a href="//product.suning.com/0000000000/10973073783.html" title="华为/HUAWEI P30 Pro 亮黑色 8GB+256GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机"> <img alt="华为/HUAWEI P30 Pro 亮黑色 8GB+256GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机" lazy-src="//image5.suning.cn/uimg/b2c/newcatentries/0000000000-000000010973073783_1_60x60.jpg"> </a> <a href="//www.suning.com/prdCom/0070094634-10985347748_0000000000-10973073783_0-0_0-0.html">华为(HUAWEI)畅享9S手机和华为/HUAWEI P30 Pro 亮黑色 8GB+256GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机哪个好</a> <p class="title"> <a title="华为/HUAWEI P30 Pro 亮黑色 8GB+256GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机" target="_blank" href="//product.suning.com/0000000000/10973073783.html">华为/HUAWEI P30 Pro 亮黑色 8GB+256GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机</a> </p> <p class="price"><i>¥</i></p> <span class="num highlight">4</span> </li> <li> <a href="//product.suning.com/0000000000/10638773027.html" title="华为/HUAWEI Mate 20 亮黑色 6GB+128GB 麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机"> <img alt="华为/HUAWEI Mate 20 亮黑色 6GB+128GB 麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机" lazy-src="//image1.suning.cn/uimg/b2c/newcatentries/0000000000-000000010638773027_1_60x60.jpg"> </a> <a href="//www.suning.com/prdCom/0070094634-10985347748_0000000000-10638773027_0-0_0-0.html">华为(HUAWEI)畅享9S手机和华为/HUAWEI Mate 20 亮黑色 6GB+128GB 麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机哪个好</a> <p class="title"> <a title="华为/HUAWEI Mate 20 亮黑色 6GB+128GB 麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机" target="_blank" href="//product.suning.com/0000000000/10638773027.html">华为/HUAWEI Mate 20 亮黑色 6GB+128GB 麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机</a> </p> <p class="price"><i>¥</i></p> <span class="num highlight">5</span> </li> <li> <a href="//product.suning.com/0000000000/10973073686.html" title="华为/HUAWEI P30 Pro 天空之境 8GB+128GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机"> <img alt="华为/HUAWEI P30 Pro 天空之境 8GB+128GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机" lazy-src="//image3.suning.cn/uimg/b2c/newcatentries/0000000000-000000010973073686_1_60x60.jpg"> </a> <a href="//www.suning.com/prdCom/0070094634-10985347748_0000000000-10973073686_0-0_0-0.html">华为(HUAWEI)畅享9S手机和华为/HUAWEI P30 Pro 天空之境 8GB+128GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机哪个好</a> <p class="title"> <a title="华为/HUAWEI P30 Pro 天空之境 8GB+128GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机" target="_blank" href="//product.suning.com/0000000000/10973073686.html">华为/HUAWEI P30 Pro 天空之境 8GB+128GB 超感光四摄 未来影像 移动联通电信4G全面屏全网通手机</a> </p> <p class="price"><i>¥</i></p> <span class="num highlight">6</span> </li> <li> <a href="//product.suning.com/0000000000/10924698539.html" title="华为/HUAWEI nova4e AI超广角三摄 4GB+128GB 幻夜黑 移动联通电信4G全网通拍照手机"> <img alt="华为/HUAWEI nova4e AI超广角三摄 4GB+128GB 幻夜黑 移动联通电信4G全网通拍照手机" lazy-src="//image3.suning.cn/uimg/b2c/newcatentries/0000000000-000000010924698539_1_60x60.jpg"> </a> <a href="//www.suning.com/prdCom/0070094634-10985347748_0000000000-10924698539_0-0_0-0.html">华为(HUAWEI)畅享9S手机和华为/HUAWEI nova4e AI超广角三摄 4GB+128GB 幻夜黑 移动联通电信4G全网通拍照手机哪个好</a> <p class="title"> <a title="华为/HUAWEI nova4e AI超广角三摄 4GB+128GB 幻夜黑 移动联通电信4G全网通拍照手机" target="_blank" href="//product.suning.com/0000000000/10924698539.html">华为/HUAWEI nova4e AI超广角三摄 4GB+128GB 幻夜黑 移动联通电信4G全网通拍照手机</a> </p> <p class="price"><i>¥</i></p> <span class="num highlight">7</span> </li> <li> <a href="//product.suning.com/0000000000/10638764316.html" title="华为/HUAWEI Mate 20 Pro 亮黑色 6GB+128GB 麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机"> <img alt="华为/HUAWEI Mate 20 Pro 亮黑色 6GB+128GB 麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机" lazy-src="//image5.suning.cn/uimg/b2c/newcatentries/0000000000-000000010638764316_1_60x60.jpg"> </a> <a href="//www.suning.com/prdCom/0070094634-10985347748_0000000000-10638764316_0-0_0-0.html">华为(HUAWEI)畅享9S手机和华为/HUAWEI Mate 20 Pro 亮黑色 6GB+128GB 麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机哪个好</a> <p class="title"> <a title="华为/HUAWEI Mate 20 Pro 亮黑色 6GB+128GB 麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机" target="_blank" href="//product.suning.com/0000000000/10638764316.html">华为/HUAWEI Mate 20 Pro 亮黑色 6GB+128GB 麒麟980芯片全面屏徕卡三摄移动联通电信4G全网通手机</a> </p> <p class="price"><i>¥</i></p> <span class="num highlight">8</span> </li> <li> <a href="//product.suning.com/0000000000/10973073309.html" title="华为/HUAWEI P30 天空之境 8GB+64GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机"> <img alt="华为/HUAWEI P30 天空之境 8GB+64GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机" lazy-src="//image2.suning.cn/uimg/b2c/newcatentries/0000000000-000000010973073309_1_60x60.jpg"> </a> <a href="//www.suning.com/prdCom/0070094634-10985347748_0000000000-10973073309_0-0_0-0.html">华为(HUAWEI)畅享9S手机和华为/HUAWEI P30 天空之境 8GB+64GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机哪个好</a> <p class="title"> <a title="华为/HUAWEI P30 天空之境 8GB+64GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机" target="_blank" href="//product.suning.com/0000000000/10973073309.html">华为/HUAWEI P30 天空之境 8GB+64GB 徕卡三摄 未来影像 移动联通电信4G全面屏全网通手机</a> </p> <p class="price"><i>¥</i></p> <span class="num highlight">9</span> </li> </ul> <div class="loading-holder"></div> </div> <script id="templateRankScript" type="text/html"> <div class="area-head"> {{if eles && eles.eleHref}} <h3 style="cursor: pointer;"><a href="{{eles.eleHref}}" target="_blank">{{eles.elecontent}}</a></h3> {{else}} <h3 style="cursor: pointer;">{{eles.elecontent}}</h3> {{/if}} </div> <ul class="toppro-tab clearfix " id="hot_sort"> {{each sugGoods as sug i}} {{if sug.showFlag == "Y"}} <li class="no-comparecheck" rel="{{sug.rel}}" name="{{sug.name}}"><a href="javascript:void(0);">{{sug.content}}</a></li> {{/if}} {{/each}} </ul> {{each sugGoods as sug i}} {{if sug.showFlag == "Y"}} <ul class="toppro-list" id="{{sug.id}}" style="display:none;"> {{each sug.skus as suk j}} {{if j <= 5}} <li com-partinfo="{{suk.vendorId}}-{{suk.sugGoodsCode}}" com-name="{{suk.sugGoodsName}}" com-price="{{suk.price}}" com-check="false"> <a id="{{suk.eleId}}" sa-data="{{suk.saData}}" name="{{suk.eleName}}" target="_blank" href={{if suk.sugType == "3" && suk.apsClickUrl}}"{{suk.apsClickUrl}}"{{else}}"{{suk.eleHrefP}}"{{/if}} title="{{suk.sugGoodsName}}"> <img alt="{{suk.sugGoodsName}}" lazy-src="{{if suk.elePic!=""}}{{suk.elePic}}{{else}}{{suk.eleSrc}}_60x60.jpg{{/if}}"/> {{if (suk.adtype == "1")}} <span class="tjw-label-ad"></span> {{/if}} </a> <p class="title"> <a id="" sa-data="{{suk.saData}}" name="{{suk.eleName}}" title="{{suk.sugGoodsName}}" target="_blank" href={{if suk.sugType == "3" && suk.apsClickUrl}}"{{suk.apsClickUrl}}"{{else}}"{{suk.eleHrefC}}"{{/if}}>{{suk.sugGoodsName}}</a> </p> <p class="price"><i>&yen;</i>{{suk.price}}{{if suk.promotionInfo!="" }}<span class="label">{{suk.promotionInfo}}</span>{{/if}}</p> <span class="num highlight">{{j+1}}</span> </li> {{/if}} {{/each}} </ul> {{/if}} {{/each}} </script> <div class="lazy-ajax area mt10" id="relGroup" style="display:none;" data-type="function"> </div> <div class="area mt10" id="relBrand" style="display:none;"> </div> <div class="area mt10" id="searchKeyWord"> <div class="area-head"><h3>为您推荐大家关注的</h3></div> <ul class="procon-relate"> <li> <a target="_blank" href="//search.suning.com/2716x.html" title="育儿卡片">育儿卡片</a> </li> <li> <a target="_blank" href="//search.suning.com/22cov.html" title="舒华抖抖机">舒华抖抖机</a> </li> <li> <a target="_blank" href="//search.suning.com/25ntu.html" title="芯片手机">芯片手机</a> </li> <li> <a target="_blank" href="//search.suning.com/26j5q.html" title="英语口语机">英语口语机</a> </li> <li> <a target="_blank" href="//search.suning.com/1q57j.html" title="博阅1手机">博阅1手机</a> </li> <li> <a target="_blank" href="//search.suning.com/1prg6.html" title="变形机品人">变形机品人</a> </li> <li> <a target="_blank" href="//search.suning.com/1prg5.html" title="变形机甲机木">变形机甲机木</a> </li> <li> <a target="_blank" href="//search.suning.com/1pqqn.html" title="变频2p冷暖机">变频2p冷暖机</a> </li> <li> <a target="_blank" href="//search.suning.com/1pr2m.html" title="变频圆柱机">变频圆柱机</a> </li> <li> <a target="_blank" href="//search.suning.com/1pr1d.html" title="变频式嵌入机">变频式嵌入机</a> </li> </ul> </div> <div id="sideAdvert" class="lazy-ajax" > </div> </div> <div class="procon" sap-modid="loverRight"> <div class="tabarea" id="product-detail" sap-modid="13"> <div class="procon-toolbar" id="pro_detail_tab"> <ul class="tabarea-items detail-tabs"> <li rel="#J-procon-desc" data-type="function" class="current"><a name="item_10985347748_tab_xiangqing" href="javascript:void(0);">商品详情</a></li> <li id="productParTitle" rel="#J-procon-param" data-type="function"><a name="item_10985347748_tab_baozhuang" href="javascript:void(0);">包装及参数</a></li> <li id="tmdy" rel="#J-procon-tmdy" data-type="funtion" style="display:none;"><a name="" href="javascript:void(0);">Outlets答疑</a></li> <li id="productCommTitle" rel="#J-procon-comment" data-type="function"><a name="item_10985347748_tab_pingjia" href="javascript:void(0);">评价（0）</a></li> <li id="answerTitle" rel="#J-procon-answer" data-type="function"><a name="item_10985347748_tab_wenda_click" href="javascript:void(0);">问答（0）</a></li> <li id="productProconSaleTitle" rel="#J-procon-sale" data-type="function"><a name="item_10985347748_tab_shouhou" href="javascript:void(0);">售后保障</a></li> <li id="credential" rel="#J-procon-credential" class="hide" data-type="function"><a href="javascript:void(0);">资质证明</a></li> </ul> </div> <div id="J-procon-desc" class="tabarea-content not-anchor clearfix" > <div class="prod-detail-container not-anchor"> <div class="ccc-auth"><i></i>商品获得<a name="item_10985347748_ccc_xiangqing" href="http://cx.cnca.cn/CertECloud/result/skipResultList" target="_blank">中国强制性产品认证（CCC）证书</a>，符合国家强制性产品认证（CCC）标准</div> <div id = 'commonwealInfo' class="snyp-con"></div> <div class="phone-parameters" id="phoneParameters"> <h4 class="txt-head">核心参数</h4> <ul class="clearfix"> <li class="p-params-node"> <dl class="n-container clearfix" name="item_10985347748_detail_laptop-spec-hover"> <dt class="l-label"> <img class="icon-img" lazy-src="//image.suning.cn/uimg/PCMS/prmtExposition/149308470640601304.png"></img> <p>拍照</p> </dt> <dd class="r-info"> <div class="infos"> <ul> <li><b>前摄像头</b>：800万像素</li> <li><b>后摄像头</b>：2400+1600+200万像素</li> </ul> </div> </dd> </dl> </li> <li class="p-params-node"> <dl class="n-container clearfix" name="item_10985347748_detail_laptop-spec-hover"> <dt class="l-label"> <img class="icon-img" lazy-src="//image.suning.cn/uimg/PCMS/prmtExposition/149308469940875198.png"></img> <p>屏幕</p> </dt> <dd class="r-info"> <div class="infos"> <ul> <li><b>屏幕尺寸</b>：6.21英寸</li> </ul> </div> </dd> </dl> </li> <li class="p-params-node"> <dl class="n-container clearfix" name="item_10985347748_detail_laptop-spec-hover"> <dt class="l-label"> <img class="icon-img" lazy-src="//image.suning.cn/uimg/PCMS/prmtExposition/149308469101161912.png"></img> <p>存储</p> </dt> <dd class="r-info"> <div class="infos"> <ul> <li><b>机身内存</b>：128GB</li> <li><b>运行内存</b>：4GB</li> </ul> </div> </dd> </dl> </li> </ul> </div> <script type="text/javascript"> if($("#phoneParameters").find("li").length>0){ iFourth.bindPhoneParameters(); }else{ $("#phoneParameters").hide(); } </script> <div id = "OptimalProductCertification" class="pro-detail-parameter"></div> <div class="pro-detail-oversea hide"> </div> <div id="phoneDetail" class="pro-detail-pics hide"></div> <div id="productDetail" class="pro-detail-pics"> <p>&nbsp;</p> <p><a title="点击了解" href="https://product.suning.com/0070094634/10576235344.html" target="_blank"><img onload="if(this.width>750){this.height=this.height*(750.0/this.width); this.width = 750;}" src="https://image.suning.cn/uimg/sop/commodity/180991468113013255086857_x.jpg" alt="" /></a></p> <!-- 亲，使用后发个链接帮我们宣传下吧，淘宝代码免费生成网dianshang.gaoding.com --> <p>&nbsp;</p> <!-- 此处注释淘宝会自动过滤 --> <div style="height: 1631px;" data-title="来自淘宝代码生成网www.001daima.com"> <div class="most-footer footer-more-trigger" style="left: auto; right: auto; width: 950px; height: 1631px; top: auto; padding: 0; border: none; z-index: 1; background: none;"> <div class="most-footer footer-more-trigger" style="left: 100px; top: 0px; width: 750px; height: 1631px; border: none; padding: 0; background: none;"><img onload="if(this.width>750){this.height=this.height*(750.0/this.width); this.width = 750;}" src="https://uimgproxy.suning.cn/uimg1/sop/commodity/BaOMybEBzMteBfX4pUlXwQ.jpg" alt="" usemap="#ma102004614" /><map name="ma102004614"> <area style="outline: none;" coords="0,583,746,903" shape="rect" href="https://product.suning.com/0070094634/10989627017.html" target="_blank" /> <area style="outline: none;" coords="5,909,248,1262" shape="rect" href="https://product.suning.com/0070094634/10985141612.html" target="_blank" /> <area style="outline: none;" coords="255,913,496,1264" shape="rect" href="https://product.suning.com/0070094634/10569351024.html" target="_blank" /> <area style="outline: none;" coords="503,911,743,1262" shape="rect" href="https://product.suning.com/0070094634/11178635827.html" target="_blank" /> <area style="outline: none;" coords="6,1271,246,1624" shape="rect" href="https://product.suning.com/0070094634/10985141612.html" target="_blank" /> <area style="outline: none;" coords="253,1270,496,1622" shape="rect" href="https://product.suning.com/0070094634/648528909.html" target="_blank" /> <area style="outline: none;" coords="501,1270,747,1626" shape="rect" href="https://product.suning.com/0070094634/674019357.html" target="_blank" /> </map></div> </div> </div> <div id="pro_detail_vedio" height="420" width="750" style="width: 750px; height: 420px;" data=http://m4.pptvyun.com/pvod/e11a0/DbCyWb50h1oSMYz1oT9DRKD1Pmk/eyJkbCI6MTU2MDY2NjAzNywiZXMiOjYwNDgwMCwiaWQiOiIwYTJkbjZ5ZHFhbWtuSzJMNEsyZG9hZmhvYU9lbjZtYnBxQSIsInYiOiIxLjAifQ/0a2dn6ydqamknK2L4K2doafhoaOen6mbpqA.mp4> </div> <script type="text/javascript"> var vedioUrl = $("#pro_detail_vedio").attr("data"); var playUrl = ""; var playCode = ""; if(vedioUrl != "" && vedioUrl.indexOf(".mp4") > 0){ playUrl = vedioUrl }else if(vedioUrl!="" && vedioUrl.indexOf(".swf") > 0){ vedioUrl=vedioUrl.substring(0,vedioUrl.indexOf(".swf")); vedioUrl=vedioUrl.substring(vedioUrl.lastIndexOf("/")+1); playCode = vedioUrl; } lazyelem.listen('#pro_detail_vedio', 'dom', function(obj) { iFourth.loadVideo('pro_detail_vedio',playCode,playUrl,"30") }); runCustomExpoData("item_"+sn.ninePartNumber+"_vedio_vediopic-expose-more"); </script> <div moduleId='R1901001_3' moduleName='商品详情'><p><img onload="if(this.width>750){this.height=this.height*(750.0/this.width); this.width = 750;}" src2="https://image.suning.cn/uimg/sop/commodity/793004705542972361283158_x.jpg" alt="" /><img onload="if(this.width>750){this.height=this.height*(750.0/this.width); this.width = 750;}" src2="https://image.suning.cn/uimg/sop/commodity/175152915910860652428858_x.jpg" alt="" /><img onload="if(this.width>750){this.height=this.height*(750.0/this.width); this.width = 750;}" src2="https://image.suning.cn/uimg/sop/commodity/136205750618061934181848_x.jpg" alt="" /><img onload="if(this.width>750){this.height=this.height*(750.0/this.width); this.width = 750;}" src2="https://image.suning.cn/uimg/sop/commodity/710346564277350751362742_x.jpg" alt="" /><img onload="if(this.width>750){this.height=this.height*(750.0/this.width); this.width = 750;}" src2="https://image.suning.cn/uimg/sop/commodity/171137539019708031325527_x.jpg" alt="" /><img onload="if(this.width>750){this.height=this.height*(750.0/this.width); this.width = 750;}" src2="https://image.suning.cn/uimg/sop/commodity/275495613175995782630654_x.jpg" alt="" /></p></div><div moduleId='R1901001_5' moduleName='常见问题'><p>&middot;</p></div><div moduleId='R1901001_6' moduleName='售后服务'><p>&middot;</p></div> <p><img onload="if(this.width>750){this.height=this.height*(750.0/this.width); this.width = 750;}" src="https://image.suning.cn/uimg/sop/commodity/108049564317176591407865_x.jpg" alt="" /></p> <p><img onload="if(this.width>750){this.height=this.height*(750.0/this.width); this.width = 750;}" src="https://image.suning.cn/uimg/sop/commodity/205354562450112133391565_x.jpg" alt="" /></p> </div> </div> <div class="d-anchor-panel" style="display:block;"> <div class="vertical-line"></div> <ul class="d-an-list" id="anchorList"> <li class="d-an-item d-select" name="item_10985347748_xqmd0_com" rel="R1901001_3"><i class="d-icon"></i>商品详情</li> <li class="d-an-item" name="item_10985347748_xqmd1_com" rel="R1901001_5"><i class="d-icon"></i>常见问题</li> <li class="d-an-item" name="item_10985347748_xqmd2_com" rel="R1901001_6"><i class="d-icon"></i>售后服务</li> </ul> </div> <script type="text/javascript"> $(".prod-detail-container").removeClass('not-anchor'); iFourth.initDetailScroll(); if($("#anchorList li").length>0){ $("#J-procon-desc").removeClass("not-anchor"); } lazyelem.listen(); </script> </div> <div id="J-procon-param" class="tabarea-content" style="display: none;"> <div class="procon-param"> <table id="bzqd_tag" class="pro-para-tbl"><tbody><tr><th colspan="3">包装清单</th></tr> <tr parameterCode="999998"><td class="name">包装清单</td><td class="val">手机x1、电池（内置）x1、充电器x1、数据线x1、快速指南x1、取卡针x1、三包凭证x1</td> <td class="err"></td> </tr></tbody></table> <table id="itemParameter" class="pro-para-tbl"> <tbody> <tr><th colspan="3">主体</th></tr> <tr parameterCode="000897"><td class="name"> <div class="name-inner"> <span>品牌</span> </div> </td> <td class="val"><a href="//www.suning.com/pinpai/0864-0-0.html" target="_blank">华为(HUAWEI)</a></td> <td class="err"></td> </tr> <tr parameterCode="001360"><td class="name"> <div class="name-inner"> <span>型号</span> </div> </td> <td class="val">畅享9S</td> <td class="err"></td> </tr> <tr parameterCode="001012"><td class="name"> <div class="name-inner"> <span>上市时间</span> </div> </td> <td class="val">2019年</td> <td class="err"></td> </tr> <tr parameterCode="012304"><td class="name"> <div class="name-inner"> <span>入网型号</span> </div> </td> <td class="val">POT-AL00a</td> <td class="err"></td> </tr> <tr parameterCode="015738"><td class="name"> <div class="name-inner"> <span>入网许可证号</span> </div> </td> <td class="val"><a id="entryPermission" isNeedExposure="1" name="item_10985347748_xkzh_click" href="http://jwxk.miit.gov.cn/WSFW/FlagValidate.aspx" target="_blank">02-5043-190113</a></td> <td class="err"></td> </tr> <tr><th colspan="3">系统</th></tr> <tr parameterCode="001921"><td class="name"> <div class="name-inner"> <span>手机操作系统</span> </div> </td> <td class="val">Android</td> <td class="err"></td> </tr> <tr parameterCode="001686"><td class="name"> <div class="name-inner"> <span>系统版本</span> </div> </td> <td class="val">Android 9</td> <td class="err"></td> </tr> <tr><th colspan="3">拍照</th></tr> <tr parameterCode="012059"><td class="name"> <div class="name-inner"> <span>摄像头类型</span> </div> </td> <td class="val">其他</td> <td class="err"></td> </tr> <tr parameterCode="012058"><td class="name"> <div class="name-inner"> <span>前摄像头</span> </div> </td> <td class="val">800万像素</td> <td class="err"></td> </tr> <tr parameterCode="012057"><td class="name"> <div class="name-inner"> <span>后摄像头</span> </div> </td> <td class="val">2400+1600+200万像素</td> <td class="err"></td> </tr> <tr parameterCode="001001"><td class="name"> <div class="name-inner"> <span>闪光灯类型</span> </div> </td> <td class="val">其他</td> <td class="err"></td> </tr> <tr><th colspan="3">屏幕</th></tr> <tr parameterCode="010025"><td class="name"> <div class="name-inner"> <span>屏幕尺寸</span> </div> </td> <td class="val">6.21英寸</td> <td class="err"></td> </tr> <tr parameterCode="014834"><td class="name"> <div class="name-inner"> <span>屏幕分辨率</span> </div> </td> <td class="val">2340*1080</td> <td class="err"></td> </tr> <tr parameterCode="011486"><td class="name"> <div class="name-inner"> <span>屏幕材质</span> </div> </td> <td class="val">TFT</td> <td class="err"></td> </tr> <tr><th colspan="3">基本信息</th></tr> <tr parameterCode="009715"><td class="name"> <div class="name-inner"> <span>颜色</span> </div> </td> <td class="val">黑色</td> <td class="err"></td> </tr> <tr parameterCode="014838"><td class="name"> <div class="name-inner"> <span>机身长度</span> </div> </td> <td class="val">155.2毫米</td> <td class="err"></td> </tr> <tr parameterCode="014837"><td class="name"> <div class="name-inner"> <span>机身宽度</span> </div> </td> <td class="val">73.4毫米</td> <td class="err"></td> </tr> <tr parameterCode="014836"><td class="name"> <div class="name-inner"> <span>机身厚度</span> </div> </td> <td class="val">7.95毫米</td> <td class="err"></td> </tr> <tr parameterCode="006985"><td class="name"> <div class="name-inner"> <span>重量</span> </div> </td> <td class="val">160克</td> <td class="err"></td> </tr> <tr><th colspan="3">CPU</th></tr> <tr parameterCode="008090"><td class="name"> <div class="name-inner"> <span>CPU品牌</span> </div> </td> <td class="val">以官方信息为准</td> <td class="err"></td> </tr> <tr parameterCode="000020"><td class="name"> <div class="name-inner"> <span>CPU型号</span> </div> </td> <td class="val">麒麟710</td> <td class="err"></td> </tr> <tr parameterCode="000017"><td class="name"> <div class="name-inner"> <span>CPU频率</span> </div> </td> <td class="val">4×Cortex A73 2.2GHz +4*Cortex A53 1.7GHz</td> <td class="err"></td> </tr> <tr parameterCode="006141"><td class="name"> <div class="name-inner"> <span>CPU核数</span> </div> </td> <td class="val">八核</td> <td class="err"></td> </tr> <tr><th colspan="3">网络</th></tr> <tr parameterCode="014852"><td class="name"> <div class="name-inner"> <span>双卡机类型</span> </div> </td> <td class="val">双卡双待</td> <td class="err"></td> </tr> <tr parameterCode="014853"><td class="name"> <div class="name-inner"> <span>最大支持SIM卡数量</span> </div> </td> <td class="val">2个</td> <td class="err"></td> </tr> <tr parameterCode="002542"><td class="name"> <div class="name-inner"> <span>SIM卡尺寸</span> </div> </td> <td class="val">Nano SIM卡</td> <td class="err"></td> </tr> <tr parameterCode="011482"><td class="name"> <div class="name-inner"> <span>4G网络制式</span> </div> </td> <td class="val">电信4G,全网通,联通4G,移动4G</td> <td class="err"></td> </tr> <tr parameterCode="011483"><td class="name"> <div class="name-inner"> <span>3G网络制式</span> </div> </td> <td class="val">电信3G,移动3G,联通3G</td> <td class="err"></td> </tr> <tr parameterCode="011484"><td class="name"> <div class="name-inner"> <span>2G网络制式</span> </div> </td> <td class="val">电信2G,移动2G/联通2G</td> <td class="err"></td> </tr> <tr parameterCode="008733"><td class="name"> <div class="name-inner"> <span>待机模式</span> </div> </td> <td class="val">双卡双待</td> <td class="err"></td> </tr> <tr><th colspan="3">存储</th></tr> <tr parameterCode="010664"><td class="name"> <div class="name-inner"> <span>机身内存</span> </div> </td> <td class="val">128GB</td> <td class="err"></td> </tr> <tr parameterCode="009130"><td class="name"> <div class="name-inner"> <span>运行内存</span> </div> </td> <td class="val">4GB</td> <td class="err"></td> </tr> <tr parameterCode="000251"><td class="name"> <div class="name-inner"> <span>存储卡类型</span> </div> </td> <td class="val">支持</td> <td class="err"></td> </tr> <tr parameterCode="011485"><td class="name"> <div class="name-inner"> <span>最大存储扩展</span> </div> </td> <td class="val">512GB</td> <td class="err"></td> </tr> <tr><th colspan="3">电池</th></tr> <tr parameterCode="006788"><td class="name"> <div class="name-inner"> <span>电池容量</span> </div> </td> <td class="val">3400mAh</td> <td class="err"></td> </tr> <tr parameterCode="012071"><td class="name"> <div class="name-inner"> <span>无线充电</span> </div> </td> <td class="val">不支持</td> <td class="err"></td> </tr> <tr parameterCode="008912"><td class="name"> <div class="name-inner"> <span>电池更换</span> </div> </td> <td class="val">不支持</td> <td class="err"></td> </tr> <tr><th colspan="3">接口</th></tr> <tr parameterCode="012008"><td class="name"> <div class="name-inner"> <span>NFC（近场通讯）</span> </div> </td> <td class="val">不支持</td> <td class="err"></td> </tr> <tr parameterCode="007885"><td class="name"> <div class="name-inner"> <span>耳机接口</span> </div> </td> <td class="val">3.5mm</td> <td class="err"></td> </tr> <tr parameterCode="014847"><td class="name"> <div class="name-inner"> <span>充电接口类型</span> </div> </td> <td class="val">Micro USB</td> <td class="err"></td> </tr> <tr><th colspan="3">手机特性</th></tr> <tr parameterCode="001540"><td class="name"> <div class="name-inner"> <span>指纹识别</span> </div> </td> <td class="val">支持</td> <td class="err"></td> </tr> <tr><th colspan="3">其他</th></tr> <tr parameterCode="009949"><td class="name"> <div class="name-inner"> <span>选购热点</span> </div> </td> <td class="val">拍照手机,大容量电池,指纹识别,快速充电,女性手机,大屏手机,双卡双待,国产手机,全面屏手机,游戏手机</td> <td class="err"></td> </tr> <tr><th colspan="3">CCC认证</th></tr> <tr parameterCode="012200"><td class="name"> <div class="name-inner"> <span>CCC认证编号</span> </div> </td> <td class="val"><a name="item_10985347748_ccc_canshu" href="http://cx.cnca.cn/CertECloud/result/skipResultList" target="_blank">2018011606048695</a></td> <td class="err"></td> </tr> <tr parameterCode="012201"><td class="name"> <div class="name-inner"> <span>生产者（制造商）名称</span> </div> </td> <td class="val">鸿富锦精密工业（深圳）有限公司</td> <td class="err"></td> </tr> </tbody> </table> </div> </div> <div id="J-procon-comment" class="tabarea-content" style="display:none;"></div> <div id="J-procon-answer" class="tabarea-content" style="display:none;"></div> <div id="J-procon-tmdy" class="tabarea-content" style="display:none;"> <div id="tmmarket" class="lazy-ajax mt10"> <div class="hwg-newlyBox"> <div class="box mt22"> <h2 class="tit">苏宁Outlets常见问题小贴士</h2> <ul> <li> <p class="content-tit"> <strong>Q</strong><span>商品都是正品吗？</span> </p> <div class="info"> <strong>A</strong> <dl>请你放心，苏宁Outlets上所售卖的商品均确保正品。</dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>衣服图片上搭配的腰带、项链等配件，会连商品一同送货吗？</span> </p> <div class="info"> <strong>A</strong> <dl>这点请注意咯，如非特别说明，服装类商品图片中的腰带、饰品等配件均为拍摄搭配之用，是不包含在所售商品中的。</dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>尺码表上的尺码标准吗？</span> </p> <div class="info"> <strong>A</strong> <dl>苏宁Outlets所售商品尺寸均为人工测量，可能会存在1-2cm的正常误差范围。</dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>图片颜色和实物颜色是否相同？</span> </p> <div class="info"> <strong>A</strong> <dl>苏宁Outlets所有商品均采用专业拍摄，力求将最真实的信息传达至你的视线。但由于个人显示器不同，可能导致实物与图片存在色差，最终颜色以实物为准。</dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>为什么我收到的商品包装和图片显示的不一致？</span> </p> <div class="info"> <strong>A</strong> <dl>由于部分商品生产批次不一，你收到货品的包装有可能与网站上图片不完全一致，但苏宁Outlets保证所售商品均为正品，商品包装请以实物为准。</dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>苏宁Outlets的对比价格？</span> </p> <div class="info"> <strong>A</strong> <dl> <p>苏宁Outlets展示的中间未划横线价格（显示如￥799）为苏宁Outlets销售价，该价格是交易成交价，是您最终决定是否购买商品的依据。</p> <p>苏宁Outlets展示的中间划横线价格（显示如 ￥2899）为参考价，采集自品牌专柜标价、商品吊牌价或由品牌供应商提供的正品零售价；由于地区、时间的差异性和市场行情波动，品牌专柜标价、商品吊牌价可能会与您购物时展示的不一致。该价格仅供您参考。</p> <p>折扣比为苏宁Outlets销售价与参考价的对比（该值四舍五入后采小数点后1位，如￥799/￥2899=0.2756=2.8折），该对比值仅供您参考，不作为结算基数。</p> </dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>所有商品都能退吗多久能退？</span> </p> <div class="info"> <strong>A</strong> <dl> 在你签收商品之日起的15天之内，苏宁Outlets为你提供七天无理由十五天有理由放心退服务，但以下情形将不能退货： <p>1、非苏宁Outlets销售的商品，或有明显使用痕迹影响二次销售的商品；</p> <p>2、法律明确规定不适用七天无理由退货的商品；</p> <p>3、基于安全及健康的考虑，已拆封的贴身用品等；</p> <p>4、未经授权的维修、误用、碰撞、疏忽、滥用、进液、事故、改动、不正确的安装所造成的商品质量问题，或撕毁、涂改标贴、机器序号、防伪标记；</p> <p>5、无法提供商品的发票（如已索要发票）、保修卡等三包凭证或者三包凭证信息与商品不符及被涂改的；</p> <p>6、礼包或套装中的商品不可以部分退货。详见苏宁Outlets退货政策。上述退货规则，客户一经购买视为认可。</p> </dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>验货后不满意能否拒收？</span> </p> <div class="info"> <strong>A</strong> <dl>如果您验货后不满意，您可以不签收该订单，拒收包裹将全额退款并不收取任何运费。部分直发大件商品非质量问题拒收会员可能要承担往返运费，但验货仅支持开箱验货不支持试穿试用。</dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>收到货包装破损怎么办？</span> </p> <div class="info"> <strong>A</strong> <dl> <p>亲爱的会员，您抢购商品不容易，如商品破损轻微且不影响使用，建议您留下商品哦。</p> <p>1、如商品完好不影响使用，建议您签收包裹；</p> <p>2、包装外观出现问题以至于商品出现质量问题或遗失商品问题，请您及时联系客服记录反馈。</p> </dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>能否自己选择物流？</span> </p> <div class="info"> <strong>A</strong> <dl>订单下单成功后，系统会根据您订单中的商品类型和您的联系地址为您自动分配最快的物流公司发出，暂时不提供自选物流的服务，不便之处，请谅解。</dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>苏宁Outlets都用什么物流公司送货？</span> </p> <div class="info"> <strong>A</strong> <dl>我们与顺丰、四通一达等物流公司合作配送商品，会根据您的收货地址和订购商品的种类来选择最合适的物流公司为您配送。</dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>偏远地区能否送到？</span> </p> <div class="info"> <strong>A</strong> <dl>如您的地区超出我们的配送范围，物流会根据具体情况为您转物流配送。如遇特殊情况需自提，可联系客服协商处理，如有不便，敬请谅解。</dl> </div> </li> <li> <p class="content-tit"> <strong>Q</strong><span>退货流程是什么？</span> </p> <div class="info"> <strong>A</strong> <dl> <img width="760" height="140" alt="退换货流程图" class="lazy-loading" src="//res.suning.cn/project/pdsWeb/csspc2017/images/TMreturn-process.jpg?v=2019071306"> </dl> </div> </li> </ul> </div> </div> </div> <script type="text/javascript"> iFourth.hwgDeploy(); </script> </div> <div id="J-procon-sale" class="tabarea-content" style="display:none;"></div> <div id="J-procon-hwgdy" class="tabarea-content" style="display:none;"></div> <div id="J-procon-credential" class="tabarea-content" style="display:none;"> </div> </div> <div id="appraise" class="lazy-ajax mt10" data-type="function"><div class="area loading-holder"></div><a target="_blank" href="//review.suning.com/cmmdty_review/general-000000010985347748-0070094634-1-total.htm">查看全部评论&gt;</a> <div style="display: none;"> <span> 2019-07-11 10:47:53 <a href = "https://review.suning.com/review_detail/613715863-10985347748-0070094634-1.htm">显示清晰，运行快，通信音质好，电池续航真的很赞，拍照效果不错，背后指纹很方便，自动调节亮度灵敏，系统自带商城很方便</a> </span> <span> 2019-07-08 15:06:09 <a href = "https://review.suning.com/review_detail/613321940-10985347748-0070094634-1.htm">手机非常的大气好看，使用起来也很顺畅。这个价格已经堪称完美了，老爸用足够了，非常不错的一次购物</a> </span> <span> 2019-07-19 14:16:19 <a href = "https://review.suning.com/review_detail/616319203-10985347748-0070094634-1.htm">这手机这手机买的超值。后面三个摄像头，拍照都很清晰。手机也很流畅，一点都不会卡顿</a> </span> <span> 2019-07-11 14:12:10 <a href = "https://review.suning.com/review_detail/613743478-10985347748-0070094634-1.htm">秒杀的运行内存杠杠的，反应超迅速，电池再大一点就更完美了，3500毫安一天刚够用，总得来说还是很不错的一款手机，五星好评</a> </span> <span> 2019-07-11 15:25:01 <a href = "https://review.suning.com/review_detail/613754906-10985347748-0070094634-1.htm">全面屏还可以，黑色机身内敛沉稳，手感很好，屏幕分辨率清晰，物流也挺快</a> </span> <span> 2019-07-03 10:01:13 <a href = "https://review.suning.com/review_detail/612567069-10985347748-0070094634-1.htm">手感非常好，手机***功能让使用新手机变得非常便捷，不用再去繁琐的下载软件</a> </span> <span> 2019-07-16 17:47:00 <a href = "https://review.suning.com/review_detail/615029770-10985347748-0070094634-1.htm">使用几天后的感受是手机没有卡顿，屏幕显示细腻，有护眼模式适合孩子玩</a> </span> <span> 2019-07-12 13:13:52 <a href = "https://review.suning.com/review_detail/613898774-10985347748-0070094634-1.htm">特特的验证了一下，是正品，包装的也很严实，手机用起来很流畅</a> </span> <span> 2019-07-16 18:35:56 <a href = "https://review.suning.com/review_detail/615049474-10985347748-0070094634-1.htm">手感超***彩艳丽，性价比高，质量非常扛扛的，音质非常好，给五星好评</a> </span> <span> 2019-07-16 17:46:41 <a href = "https://review.suning.com/review_detail/615029689-10985347748-0070094634-1.htm">这是我在这家买的第3部手机了。很有诚意的一款手机，手机上手第一感觉是轻，做工精致，屏幕没有漏光</a> </span> </div> </div> <div id="appwd" class="lazy-ajax mt10" data-type="function"></div> <div id="appAdv" class="mt10"><a rel="nofollow" name="item_10985347748_mobileAd_01" href="//c.m.suning.com/newPacket_pc.html" target="_blank"><img src2="//image2.suning.cn/uimg/cms/img/154233632056897763.png" onerror="javascript:$('#appAdv').hide()"/></a></div> <div id="serviceArea" class="lazy-ajax area mt10"> <div class="area-head"><h3>售后保障</h3></div> <div class="after-market" id="afterService"> <div id="installService" class="lazy-ajax" data-type="function"></div> <div id="afterServicePic" class="lazy-ajax after-market-img-list" style="display: none"></div> <div id="djh-after-market-container" style="display: none"></div> <div id="snblank" style="display: none"></div> </div> </div> <div class="area history mt15" id="historyListDiv" sap-modid="14"> <div class="area-head"> <h3>最近浏览</h3> </div> <div class="lazy-ajax history-rec" id="J-historyList" data-type="function"> </div> </div> <div class="procon-like mt15 lazy-ajax" id="adDatasDiv" sap-modid="16" style="display: none;"> </div> <div class="area history mt15" id="historyRecDiv" sap-modid="08"> <div class="area-head"> <h3>猜你喜欢</h3> </div> <div class="lazy-ajax history-rec" id="J-historyRec" data-type="jsonp"> </div> </div> <script id="guessScriptContent" type="text/html"> {{if skus.length>5}} <a class="btn-dir prev" href="javascript:void(0);"><span class="screen-count"><em class="cur-count">1</em>/<i class="total-count">3</i></span><i class="arr"></i></a> <a class="btn-dir next" href="javascript:void(0);"><span class="screen-count"><em class="cur-count">1</em>/<i class="total-count">3</i></span><i class="arr"></i></a> {{/if}} <div class="scroll-box"> <ul> {{each skus as value i}} <li com-partinfo="{{value.vendorId}}-{{value.sugGoodsCode}}" com-name="{{value.sugGoodsName}}" com-price="{{value.price}}" com-check="false"> <a name="{{value.eleName}}" sa-data="{{value.saData}}" title="{{value.sugGoodsName}}" target="_blank" href="{{value.eleHref}}"> <img alt="{{value.sugGoodsName}}" src="{{value.eleSrc}}"> </a> <p class="price"> <i>¥</i>{{value.price}}{{if value.productType==1}}<label class="com-has-border">苏宁自营</label>{{/if}} </p> <p class="title"> <a name="{{value.eleName}}" sa-data="{{value.saData}}" id="{{value.eleId}}" target="_blank" href="{{value.eleHref}}">{{value.sugGoodsName}}</a> </p> <p class="p-huodong">{{if value.promotionInfo!="" }}<span>{{value.promotionInfo}}</span>{{/if}}</p> </li> {{/each}} </ul> </div> </script> <div class="pro-statement hide" id="proStatement"> </div> </div> </div> <div id="addCartPop" class="promtip-addcart hide"> <div class="promtip-addcart-title"> <i class="tipInfo4 mr5"></i> <span>该商品在当前城市正在进行</span> <label class="promtip-label">抢购</label> <span>促销</span> </div> <ul class="promtip-addcart-panel clearfix"> <li> <p>抢购价：<span class="price"><i>&yen;</i> <em id="qg_qgprice">38.00</em></span> </p> <a href="javascript:void(0);" id="qg_href" class="btn-view" target="_blank">查看抢购信息</a> </li> <li class="sep"></li> <li> <p>易购价：<span class="price"><i>&yen;</i> <em id="qg_promotionPrice">38.00</em></span> </p> <a href="javascript:void(0);" id="qg_promotion_href" class="btn-buy">以易购价购买</a> </li> </ul> <p class="promtip-addcart-memo">注：参加抢购将不再享受其他优惠活动</p> <a href="javascript:void(0)" class="close"></a> </div> <div id="J-identify-code" style="display: none;"> <div class="identify-code"> <p class="tips">亲，很抱歉，您购买的宝贝销售异常火爆，让小苏措手不及，请稍后再试~</p> <div class="code-input clearfix"> <dl> <dt class="l">验证码</dt> <dd class="l"> <p class="item-ide"><input id="validateCode" autocomplete="off" class="ui-text l" type="text" value="以下字符不区分大小写"><i id="imageVerifytip" class="tip-icon tip-ok-16 tip-ok l" style="display:none;"></i><em class="code-error l" style="display:none;">验证码错误</em></p> <p class="item-ide"><img onclick="fun_getVcode()" name="vcodeimg1" id="vcodeimg1" class="l" src="" alt=""><span class="change l">看不清楚？<a href="javascript:void(0);" onclick="fun_getVcode()">换一张</a></span></p> <p class="item-ide"><a class="lion-btn certain" href="javascript:void(0);" onclick="ajaxCheckVerifyCodeOrSubmit(true);return false;">确定</a><a class="lion-btn close" href="javascript:void(0);">关闭</a></p> </dd> </dl> </div> </div> </div> <div id="J-company-channel" style="display: none;"> <div class="company-channel"> <p class="tips">亲，大宗购物请点击<span><a href="//b.suning.com">企业用户渠道&gt;</a></span>小苏的服务会更贴心！</p> </div> </div> <div id="J-boom" style="display: none;"> <div class="company-channel"> <p class="tips">亲，很抱歉，您购买的宝贝销售<span>异常火爆</span>让小苏措手不及，请稍后再试~</p> </div> </div> <div class="pro-pop gray6 hide" id="proPop"> <div class="pop-up fix"> <a id="proPopCloseBtn" class="close-btn" href="javascript:void(0)" title="关闭">x</a> </div> <div class="pop-main pop-main-normal fix"> <em class="tipIcon"></em> <div class="msg"><strong>您已成功将商品加入收藏夹</strong> <p style="font-size:12px;">查看<a href="#">我的收藏夹</a> </p> </div> </div> <div class="pop-down"> <a id="proPopSubmit" class="pop-btn" href="javascript:;">确定</a> </div> </div> <div id="win_presell" class="hide"> <div class="presell-pay-failed"> <i></i> <p id="psellBookMessage">非常抱歉，您前期未参加预订活动，<br />无法支付尾款哦！</p> <p class="mt20"><a href="javascript:void(0);" class="btn-cancel close">关闭</a></p> </div> </div> <div id="dlg_error_prompt" class="hide"> <div class="d-error-prompt"> <div class="e-img"></div> <p class="d-message">抱歉，您暂无任性付资格</p> </div> </div> <!---super会员预约弹窗--> <div id="super-dialog-tell" class="hide"> <div class="orders-dialog-container"> <div class="orders-msg"> <span class="orders-common super-new-posi"></span> <div class="super-dialog-text"><span id="super-dialog-msg">此时为正式期SUPER会员专享抢购期，普通会员暂不可抢购</span></div> </div> <div class="btn-box"> <a href="javascript:;" name="item_10985347748_supertqqqx_click" id="dialogVipPriceClose" class="btn4 close"> <p>继续等待</p> <p>0小时0分</p> </a> <a href="javascript:;" name="item_10985347748_supertqqkt_click" id="dialogVipPriceLink" class="btn3"> <p>立即开通</p> <p>SUPER会员</p> </a> </div> </div> </div> <div id="o2o_parts_dlg" class="hide"> </div> <div id="car_parts_dlg" class="hide"> </div> <div class="ju-footer-wrapper" id="jufooter" style="display:none;"> </div> <div id="orders-dialog-content" class="hide"> </div> <div id="dialog-vas-quan" style="display: none;"> <script id="ybqDialogImpl" type="text/html"> <!--延保券 弹窗--> <!-- 风控验证 --> <div class="identity-pop-form" id="vasIdentityPopForm" style="display: none"> <div class="idty-container"> <div class="clearfix" id="vasSlideWords" style="display: none"> <div class="lose-img"></div> <div class="idty-prompt"> <p>活动太火爆，请滑动验证！</p> </div> </div> <div class="clearfix" id="vasImgWords" style="display: none"> <div class="lose-img"></div> <div class="idty-prompt"> <p>活动太火爆，请输入验证码验证！</p> </div> </div> <div class="idty-area" id="vasSlideCheck" style="display: none"> <div> <div style="width: 332px;height: 42px; text-align: center;background: #75C72B;" id="vasSlideArea"></div> </div> </div> <div class="idty-area" id="vasImgCheck" style="display: none"> <div class="identity-img "> <div class=" clearfix "> <div class="idty-input check-err check-correct" id="vasChenckInfo"> <input type="text" id="vasImgtext"> <i class="err-i" style="display: none"></i> <i class="correct-i" style="display: none"></i> </div> <img src="" alt="" class="idtycode-img"> <a href="javascript:;" class="idty-change" onclick="yanBaoQuan.fk.imageCheck.changeValidate()">换一张</a> </div> <div class="err-box" style="display: none" id="vasErrbox"></div> <a href="javascript:;" class="btn-idty" id="vasValidateButton">验证领取</a> </div> </div> <div id="vasSMSCheck" style="display: none"> <div class="page1 SMS_security"> <div class="info info-tel"> <p>手机号码:<span class="tel-num" id="vasSmsTel"></span></p> </div> <p class="info info-code"> <input type="tel" class="code" id="vasSmsCode" placeholder="请输入验证码"> <a class="code1" id="vasGetSmsCode" href="javascript:;">获取验证码</a> </p> <p class="error-msg" style="display: none" id="vasSmsErrbox">验证码错误</p> <div class="btn-box"> <a href="javascript:;" class="btn-idty" id="vasSMSButton">确定</a> <a href="javascript:;" class="btn2" id="vasSMSCancel">取消</a> </div> </div> </div> </div> </div> <!-- 券信息 --> <div class="coupons-body vas-quan-pop" id = 'ybqWin'> <!-- 循环领券列表 --> {{if ticketsInfo.bonusList.length == 0 }} <!-- 没有券 展示文案 活动火爆，请稍后再试 --> <div class="none-tickets"> <div class="none-icon"></div> <p class="none-text">活动异常火爆，请稍后再试…</p> </div> {{else}} <!-- 有券循环展示 --> <a class="btn-dir prev" href="javascript:void(0);"> <span class="screen-count"> <em class="cur-count">1</em>/ <i class="total-count">1</i> </span> <i class="arr"></i> </a> <a class="btn-dir next" href="javascript:void(0);"> <span class="screen-count"> <em class="cur-count">1</em>/ <i class="total-count">1</i> </span> <i class="arr"></i> </a> <div class="list-container"> <ul class="clearfix"> <li> {{each ticketsInfo.bonusList as ticket i}} {{if ticket.isReceived == '1'}} <div class="vas-quan" id={{ticket.ticketId}}> {{else}} <div class="vas-quan vas-quan-out" id={{ticket.ticketId}}> {{/if}} <div class="vas-quan-price"> <span class="vas-quan-price-little">&yen;</span> <span class="vas-quan-price-big">{{ticket.priceInteger}}</span> <span class="vas-quan-price-little">{{ticket.priceDecimal}}</span> <span class="vas-quan-price-limit" title={{ticket.ticketDesc}}>{{ticket.ticketDesc}}</span> </div> <div class="vas-quan-price-time" title={{ticket.timeRegion}}>{{ticket.timeRegion}}</div> {{if ticket.isReceived == '1'}} <a class="vas-quan-action" onclick = {{ticket.receiveQuan}}></a> {{/if}} </div> {{if (i+1)%2 == 0 && (i+1) != ticketsInfo.bonusList.length}} </li> <li> {{/if}} {{/each}} </li> </ul> </div> {{/if}} </div> </script> </div> <div id="newcar_Chose" class="hide"> </div> <div id="buySure_Chose" class="hide"> <div class="buySure-text"> <i></i> <span id="tmShowMsg"></span> </div> </div><div class="lazy-ajax" id="pds-footer" data-type="function">
<div style="height:25px;"></div>
</div><script src="//res.suning.cn/public/js/magina-1.0.0-mt-prd.js "></script>
<script type="text/javascript" src="//mmds.suning.com/mmds/mmds.js?v=2019071306"></script> <script type="text/javascript" src="//dfp.suning.com/dfprs-collect/dist/fp.js?v=2019071306"></script> <link rel="stylesheet" type="text/css" href="//res.suning.cn/project/ccf/fourthPage/fourthPopBox.css?v=2019071306"/> <script type="text/javascript" src="//res.suning.cn/project/??/ccf/js/api/cart.js,/myfavorite/js/favorite-api.min.js,/myfavorite/js/favSaleNotice.min.js,/cps/js/remoteService/newFourPageService.min.js,/msIndex/api/js/memberOrgs.min.js,/fct/m/js/page/fctBuyPC-min.js?v=2019071306"></script> <script type="text/javascript" src="https://res.suning.cn/project/??/passport/js/passport.min.js,/asc/style/js/showMobilePop1-min.js?v=2019071306"></script> <script type="text/javascript"> var isArray=function(obj){return Object.prototype.toString.call(obj)==='[object Array]';}; var windowOnLoadEventQueue=[];var scriptOnLoadEventQueue=[];window.onload=function(){for(var i=0;i<windowOnLoadEventQueue.length;i++){windowOnLoadEventQueue[i]();}}; function addOnLoad(func){windowOnLoadEventQueue=windowOnLoadEventQueue.concat(func);} var lazyScriptMap={};function lazyLoadScript(src,callback){if(!lazyScriptMap[src]){lazyScriptMap[src]=callback;var scriptNode=document.createElement("script");if('function'===typeof callback){scriptNode.onload=callback;scriptNode.onreadystatechange=function(){if("loaded"==scriptNode.readyState||"complete"==scriptNode.readyState){callback();}}}else if(isArray(callback)){var callbackSequence=function(){for(var i=0;i<callback.length;i++){(callback[i])();}};scriptNode.onload=callbackSequence;scriptNode.onreadystatechange=function(){if("loaded"==scriptNode.readyState||"complete"==scriptNode.readyState){callbackSequence();}}} scriptNode.type="text/javascript";scriptNode.src=src;var scriptContainer=document.getElementsByTagName("head")[0];scriptContainer.appendChild(scriptNode);}else{}} function lazyLoadScripts(srcs,callback){var srcNum=srcs.length;var loadingProgress=0;if(srcNum>0){for(var i=0;i<srcNum;i++){var currSrc=srcs[i];lazyLoadScript(currSrc,function(){loadingProgress++;if(srcNum==loadingProgress){if('function'===typeof callback){callback();}else if(isArray(callback)){for(var i=0;i<callback.length;i++){(callback[i])();}}}});}}} var isTimeout = false; var lazyLoadFunction = null; var lazyScriptLoaded = false; var lazyScriptTimeout = 2000; /*默认的超时时间2秒，这个数字2是业务部或用户体验部门来提出要求。*/ /*在懒加载方法中对事件响应后绑定*/ lazyloadBindingFuc=function() { $(".mycar, .myhelp, .myweb").bind({ mouseover: function() { addhover(this); }, mouseout: function() { delhover(this); } }); }; lazyLoadFunction = function() { if(lazyScriptLoaded&&isTimeout) { /*一旦已经执行过，并且是在timeout的情况下执行，则需要加载da.js*/ lazyLoadScript( "//res.suning.cn/javascript/sn_da/da_opt.js?v=2019071306", function(){ lazyLoadScript("//res.suning.cn/javascript/sn_da/saSiteDsp.js?v=2019071306" );}); return; } lazyScriptLoaded =true;/*flag置为true*/ if (isTimeout) { lazyLoadScript("//res.suning.cn/javascript/ShoppingArea/V9/ECode.calendar.js?v=2019071306", function(){ lazyLoadScript("//res.suning.cn/javascript/sn_da/saSiteDsp.js?v=2019071306" );}); } else { lazyLoadScript("//res.suning.cn/javascript/ShoppingArea/V9/ECode.calendar.js?v=2019071306", function(){ lazyLoadScript("//res.suning.cn/javascript/sn_da/da_opt.js?v=2019071306", function(){ lazyLoadScript("//res.suning.cn/javascript/sn_da/saSiteDsp.js?v=2019071306" );} );} ); } }; addOnLoad(lazyloadBindingFuc); addOnLoad(lazyLoadFunction); /*对lazyload设置 超时机制*/ function checkLazyScriptTimeout(){ isTimeout = true; if(!lazyScriptLoaded){/*检测lazy script是否已经加载*/ if(!!lazyLoadFunction){/*检测下函数空间，以免servlet还没加载完全*/ lazyLoadFunction(); }else{ setTimeout(checkLazyScriptTimeout, 1000);/*在servlet还没加载完全的情况下，每过1秒，重新检测一次*/ } } } $(document).ready(function(){ $("dl[name^=item_],img[name^=item_],span[name^=item_],a[name^=item_],p[name^=item_],div[name^=item_],i[name^=item_],li[name^=item_],input[name^=item_],a[name^=reviewitem_],input[name^=reviewitem_],p[name^=reviewitem_]").live("click",function(){ sa.click.sendDatasIndex(this); }); /*分享附节点阻止了冒泡，另设分享*/ $('.share a[name^=item_],.share span[name^=item_]').on("click", function(){ sa.click.sendDatasIndex(this); }); bd.init({ 'token':'other', 'system':'PDS', 'url':'//dt.suning.com/detect/dt/portoToken.json' }); var env = "prd"; if(sn.envName){ if(sn.envName == "PROD"){ env = "prd"; }else if(sn.envName == "SIT"){ env = "sit"; }else if(sn.envName == "XGPRE"){ env = "xgpre"; }else if(sn.envName == "PRE"){ env = "pre"; } } _dfp.init({ appCode : "OLSltniYhR1s2xr5", env : env, error : function (e) { } }); }); setTimeout(checkLazyScriptTimeout, lazyScriptTimeout); /*初始化方法*/ FourPage.Ready(); paramRecovery(); </script><script id="shoppingAllowanceDialog" type="text/html">
    <div id="o2o-cjhb">
        <div class="o2o-contain">
            <div id="oto-bgg" class="oto-bgg" style='background: url("//image2.suning.cn/uimg/cms/img/154287473370364143.png")'>
                <p class="o2o-p1" style='background-image: url("//image2.suning.cn/uimg/cms/img/154510130790775531.png")'></p>
                {{if dialogMode == '5'}}
                <p class="o2o-p2">活动太火爆 稍后尝试</p>
                <br/>
                {{else}}
                <p class="o2o-p2"><a name="item_10985347748_gwjtmjhd_click" target="_blank" href="{{ruleUrl}}">{{bountyRulDescribe}} &gt;</a></p>
                {{if startTimeStr && endTimeStr}}
                <p class="o2o-p3">{{startTimeStr}} 至 {{endTimeStr}}</p>
                {{/if}}
                {{/if}}
                <div id="o2oDynamic">
                    <div class={{if dialogMode == '1'}}
                    "o2o-common o2o-avalible">
                    {{else if dialogMode == '4'}}
                    "o2o-common o2o-success">
                    {{else if dialogMode == '5'}}
                    "o2o-common o2o-avalible">
                    {{/if}}
                    {{if dialogMode == '5'}}
                    <div class="o2o-lkbg">刷新</div>
                    {{else}}
                    <div class="o2o-d-con">
                        {{each surplusQuota as quota}}
                        <div class="{{if !point || point < quota.pointQuota}}o2o-d-n{{else}}o2o-d-y{{/if}}{{if dialogMode != '1'}} hide{{/if}}" name='item_10985347748_{{if quota.sendCategory=="0"}}gwjtdh{{else if quota.sendCategory=="1"}}gwjtsjdh{{/if}}_click' sendCategory="{{quota.sendCategory}}">
                            <span class="o2o-zydh">{{if quota.sendCategory=="1"}}抢{{quota.minAllowanceQuota}}-{{quota.maxAllowanceQuota}}元{{else if quota.sendCategory=="0"}}抢{{quota.allowanceQuota}}元{{/if}}</span>
                            <span class="o2o-zyxy">{{if !point || point < quota.pointQuota}}云钻不足{{else}}需{{quota.pointQuota}}云钻{{/if}}</span>
                        </div>
                        {{/each}}
                    </div>
                    <div class="o2o-do-text{{if dialogMode != '4'}} hide{{/if}}"><i>恭喜，兑换成功(</i><i>5</i><i>s)</i></div>
                    <div class="o2o-done{{if dialogMode != '4'}} hide{{/if}}">获得{{if dialogMode == '4'}}{{exchangeAllowanceQuota}}{{/if}}元购物补贴</div>
                    {{/if}}
                </div>
                {{if point >= 0}}
                <div class="o2o-my-money">
                    <span>我的云钻&nbsp;:&nbsp;</span>
                    <i>{{point}}</i>
                </div>
                {{/if}}
                {{if bonusUseAmount >= 0 && shopAllowanceRedPacketLinkSwitch == '1'}}
                <div class="o2o-my-money">
                    <a href="//quan.suning.com/shoppingCoupon/shoppingCoupon_{{activityId}}.htm" target="_blank"><span>我的购物补贴&nbsp;:&nbsp;</span>
                        <i>¥ {{bonusUseAmount}}</i></a>
                </div>
                {{/if}}
            </div>
        </div>
        </div>
    </div>


    <!-- 风控验证 -->
    <div class="identity-pop-form" id="vasIdentityPopForm" style="display: none">
        <div class="idty-container">
            <div class="clearfix" id="vasSlideWords" style="display: none">
                <div class="lose-img"></div>
                <div class="idty-prompt">
                    <p>活动太火爆，请滑动验证！</p>
                </div>
            </div>
            <div class="clearfix" id="vasImgWords" style="display: none">
                <div class="lose-img"></div>
                <div class="idty-prompt">
                    <p>活动太火爆，请输入验证码验证！</p>
                </div>
            </div>
            <div class="idty-area" id="vasSlideCheck" style="display: none">
                <div>
                    <div style="width: 332px;height: 42px; text-align: center;background: #75C72B;"
                         id="vasSlideArea"></div>
                </div>
            </div>
            <div class="idty-area" id="vasImgCheck" style="display: none">
                <div class="identity-img ">
                    <div class=" clearfix ">
                        <div class="idty-input check-err check-correct" id="vasChenckInfo">
                            <input type="text" id="vasImgtext">
                            <i class="err-i" style="display: none"></i>
                            <i class="correct-i" style="display: none"></i>
                        </div>
                        <img src="" alt="" class="idtycode-img">
                        <a href="javascript:;" class="idty-change" onclick="shopAllowance.fk.imageCheck.changeValidate()">换一张</a>
                    </div>
                    <div class="err-box" style="display: none" id="vasErrbox"></div>
                    <a href="javascript:;" class="btn-idty" id="vasValidateButton">验证领取</a>
                </div>
            </div>
            <div id="vasSMSCheck" style="display: none">
                <div class="page1 SMS_security">
                    <div class="info info-tel">
                        <p>手机号码:<span class="tel-num" id="vasSmsTel"></span></p>
                    </div>
                    <p class="info info-code">
                        <input type="tel" class="code" id="vasSmsCode" placeholder="请输入验证码">
                        <a class="code1" id="vasGetSmsCode" href="javascript:;">获取验证码</a>
                    </p>
                    <p class="error-msg" style="display: none" id="vasSmsErrbox">验证码错误</p>
                    <div class="btn-box">
                        <a href="javascript:;" class="btn-idty" id="vasSMSButton">确定</a>
                        <a href="javascript:;" class="btn2" id="vasSMSCancel">取消</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</script></body>
</html>


"""

detail_html_doc = etree.HTML(kkk)

title = detail_html_doc.xpath('//div[@class="proinfo-title"]/h1/text()')
second_title = detail_html_doc.xpath('//div[@class="proinfo-title"]/h2/text()')
system_version = detail_html_doc.xpath('//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="001686"]/td[2]/text()')
back_camera = detail_html_doc.xpath('//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="012057"]/td[2]/text()')
screen_size = detail_html_doc.xpath('//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="010025"]/td[2]/text()')
screen_material = detail_html_doc.xpath('//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="011486"]/td[2]/text()')
color = detail_html_doc.xpath('//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="009715"]/td[2]/text()')
cpu = detail_html_doc.xpath('//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="000020"]/td[2]/text()')
ram = detail_html_doc.xpath('//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="009130"]/td[2]/text()')
save = detail_html_doc.xpath('//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="010664"]/td[2]/text()')
battery = detail_html_doc.xpath('//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="006788"]/td[2]/text()')
model = detail_html_doc.xpath('//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="001360"]/td[2]/text()')
market_time = detail_html_doc.xpath('//div[@class="procon-param"]/table[2]/tbody/tr[@parametercode="001012"]/td[2]/text()')

print(title)
print(second_title)
print(system_version)

# detail_url = 'https://product.suning.com/0000000000/10638755882.html'
# key1 = detail_url.split('/')[-2].zfill(10)
# key2 = detail_url.split('/')[-1].split('.')[0].zfill(18)
# print(key1)
# print(key2)
#
# s = 'pcData({"code":"1","data":{"price":{"cacheMinute":"","saleInfo":[{"vipPrice":"","vendorCode":"0070094634","accountPlace":"","sendCityId":"","refPrice":"","processStat":"","noPriceCausation":"","balanceStartTime":"","onLineStatus":"","netPrice":"3838.00","warrantyList":{},"deptNo":"0001","finalPayment":"","salesOrg":"C","pgPrice":"3828.00","factorySendFlag":"0","plantCode":"Z048","pgNum":"2","businessField1":"","manageInvFlag":"5","promotionPrice":"3838.00","bookPrice":"","pgActionId":"47077787673282886988","bigPromoPrice":"","singlePrice":"","bigPromoTextPrice":"","bigPromoId":"","promoActType":"","promoActId":"","bookActionID":"","bookPriceLabel":"","marketVipPriceType":"","marketVipPrice":"","sendAvalidTime":"1563786957000","serveCodeList":{},"rentPrice":"","bookGoodID":"","usePrice":"","vendorType":"921C店","balanceEndTime":"","invStatus":"1","chargePlantCode":"","bookPriceSwell":"","juId":"","partNumber":"000000010989586988","noPriceCode":"","priceType":"0","ownerPlace":"Z048","vendor":"0070094634","govPrice":"","purChaseType":""}]},"pcMsg":[{"pcNewCouponsFlag":"0","https":"0"}],"marketVipPriceType":"","isnpri":"1","nowTime":1563786956000,"nt":1563786956.978,"isOp":"1","flag":"0","respTime":"priceTime-10,fimsTime-0,solpTime-0,treatyTime-0","freightObj":{"snslt":"0","fare":"-1","freight":"{}"},"deliverableFlag":"Y","isCShop":"Y","invStatus":"0-4"},"api":"pcitemsale"})'
# price = re.findall(r'"promotionPrice": "(.*?)"', s)
# print(price)