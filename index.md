LOF-BOT
======
作者：[**refraction-ray**](https://github.com/refraction-ray/)

项目地址：[**lof-bot**](https://github.com/refraction-ray/lof-bot)

🎉 You need a 🤖, not a 👻.

## 净值预测基金列表：

<p align="center">
<a href="https://github.com/refraction-ray/lof-bot/actions"><img alt="Actions Status" src="https://github.com/refraction-ray/lof-bot/workflows/gh/badge.svg"></a>
</p>

#### 原油类基金

* [南方原油](/lof-bot/SH501018.html) (501018)
* [华宝油气](/lof-bot/SZ162411.html) (162411)
* [国泰商品](/lof-bot/SZ160216.html) (160216)
* [嘉实原油](/lof-bot/SZ160723.html) (160723)
* [诺安油气](/lof-bot/SZ163208.html) (163208)
* [易方达原油](/lof-bot/SZ161129.html) (161129)
* [广发道琼斯石油](/lof-bot/SZ162719.html) (162719)
* [华安标普石油](/lof-bot/SZ160416.html) (160416)
* [信诚商品](/lof-bot/SZ165513.html) (165513)
* [银华通胀](/lof-bot/SZ161815.html) (161815)

#### 其他 QDII 基金

* [华安德国30](/lof-bot/SH513030.html) (513030/000614)
* [博时标普500](/lof-bot/SH513500.html) (513500/050025)
* [易方达标普500](/lof-bot/SZ161125.html) (161125)
* [易方达标普科技](/lof-bot/SZ161128.html) (161128)
* [易方达纳斯达克100](/lof-bot/SZ161130.html) (161130)
* [国泰纳斯达克100](/lof-bot/SH513100.html) (513100)
* [交银中国互联](/lof-bot/SZ164906.html) (164906)
* [易方达中概互联](/lof-bot/SH513050.html) (513050)
* [华宝香港中小](/lof-bot/SH501021.html) (501021)
* 日经225:
  * [513880](/lof-bot/SH513880.html)
  * [513520](/lof-bot/SH513520.html)
  * [513000](/lof-bot/SH513000.html)

More funds are coming soon.

*净值预估的页面更新机制可能还存在问题，数据仅供参考，如果预测数据过于离谱，可能是有 bug 待捉。*

*附带仓位预计栏的，为滑动平均预估。每日仓位数字不变的，则说明未启动仓位预估调整，很多指数跟踪不启动仓位调整预测效果更佳。*

## 场内实时溢价提醒

<p align="center">
<a href="https://github.com/refraction-ray/lof-bot/actions"><img alt="Actions Status" src="https://github.com/refraction-ray/lof-bot/workflows/pb/badge.svg"></a>
</p>

场内跟踪基金溢价阈值超过一定限度，自动通过 pushbullet 通知。如果你也想获取该提醒通知功能，请 fork 该项目，并且在 forked 项目 setting 中 secrets 添加自己 pushbullet 的 token 作为 ``PB_TOKEN`` 即可。

## 基金相关研究

比起 [xalpha](https://github.com/refraction-ray/xalpha) 项目，这里的研究更侧重于基金溢价行为和净值预测等。

亮点研究：

* [不同 QDII 基金净值可预测性](https://github.com/refraction-ray/lof-bot/blob/master/studies/qdii_lof_prediction.ipynb)
* [不同 QDII 基金对基准的追踪情况和购买建议分析](https://github.com/refraction-ray/lof-bot/blob/master/studies/compwithbenchmark.ipynb)
* [末日QDII拯救计划：主流 QDII 额度耗尽时的替代品分析](https://github.com/refraction-ray/lof-bot/blob/master/studies/alternatives.ipynb)

Stay tuned for more.