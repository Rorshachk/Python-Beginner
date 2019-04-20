# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urllib.parse import quote
from taobao.items import ProductItem
from scrapy_splash import SplashRequest
from urllib.parse import quote

script = """
function main(splash, args)
  splash:init_cookies({
      {
name="l",
value="bBEc3eEqvl9Id1wUBOCN5uI8Yj_9IIRfguPRwh0wi_5Z-6L_sa7OlNb2hFp6Vj5PtZ8Q4R15R8etZFqT5Pef.",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="_tb_token_",
value="5e76eeeb38366",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="t",
value="4845798dd5f2512b4d510bb833d9d6fe",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="sg",
value="25a",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="cna",
value="XPdBFXq9EEACATyiUIYiRYk+",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="cookie2",
value="13eac6a7718ced4597073aaca2359b66",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=True},
{
name="v",
value="0",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="uc1",
value="cookie16=URm48syIJ1yk0MX2J7mAAEhTuw%3D%3D&cookie21=URm48syIYB3rzvI4Dim4&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTZ4SKyj2dMPw%3D%3D&lng=zh_CN",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="unb",
value="3330702905",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=True},
{
name="_l_g_",
value="Ug%3D%3D",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="skt",
value="698db491729887e6",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=True},
{
name="cookie1",
value="BxvEgaAehE8yB0hc2t7eQe%2F3stOCBPisIcQfdrdTLcU%3D",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=True},
{
name="csg",
value="b99f3b76",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="uc3",
value="vt3=F8dByEfI1OP9ujOVvi0%3D&id2=UNN%2BxtrxfuPO5Q%3D%3D&nk2=F6k3HMtynvpgmy4rUUdTvF1Va5Q%3D&lg2=W5iHLLyFOGW7aA%3D%3D",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=True},
{
name="existShop",
value="MTU1NTc2MTUxMA%3D%3D",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="tracknick",
value="t_1497968676242_0732",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="lgc",
value="t_1497968676242_0732",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="_cc_",
value="VFC%2FuZ9ajQ%3D%3D",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="mt",
value="np=",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="dnk",
value="t_1497968676242_0732",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="_nk_",
value="t_1497968676242_0732",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="cookie17",
value="UNN%2BxtrxfuPO5Q%3D%3D",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=True},
{
name="tg",
value="0",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="thw",
value="cn",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
{
name="isg",
value="BEhIITpVgNA3I-xUu7JGSQtcGbaaWa_jqokaPAL5lUO23ehHqgF8i95fUbWtbWTT",
path="/",
domain=".taobao.com",
secure=False,
httpOnly=False},
    })
  args = {
    url="https://s.taobao.com/search?q=ipad",
    wait=5,
    page=5,
  }
  splash.images_enabled = false
  assert(splash:go(args.url))
  assert(splash:wait(args.wait))
  js = string.format("document.querySelector('#mainsrp-pager > div > div > div > div.form > input').value=%d;document.querySelector('#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit').click()", args.page)
  splash:evaljs(js)
  assert(splash:wait(args.wait))
  return splash:html()
end
"""


class TaobaoSpider(Spider):
    name = 'Taobao'
    allowed_domains = ['www.taobao.com']
    base_url = 'https://s.taobao.com/search?q='

    def start_request(self):
        for keyword in self.settings.get('KEYWORDS'):
            for page in range(1, self.settings.get('MAX_PAGE') + 1):
                url = self.base_url + quote(keyword)
                yield SplashRequest(url, callback=self.parse, endpoint='execute', args={'lua_source': script, 'page': page, 'wait': 7})

    def parse(self, response):
        products = response.xpath(
            '//div[@id="mainsrp-itemlist"]//div[@class="items"][1]//div[contains(@class, "item")]')
        for product in products:
            item = ProductItem()
            item['price'] = ''.join(product.xpath(
                './/div[contains(@class, "price")]//text()').extract()).strip()
            item['title'] = ''.join(product.xpath(
                './/div[contains(@class, "title")]//text()').extract()).strip()
            item['shop'] = ''.join(product.xpath(
                './/div[contains(@class, "shop")]//text()').extract()).strip()
            item['image'] = ''.join(
                product.xpath('.//div[@class="pic"]//img[contains(@class, "img")]/@data-src').extract()).strip()
            item['deal'] = product.xpath(
                './/div[contains(@class, "deal-cnt")]//text()').extract_first()
            item['location'] = product.xpath(
                './/div[contains(@class, "location")]//text()').extract_first()
            yield item
