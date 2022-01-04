## Get data from web page with Javascript

I can't get the data from the downloaded page content as there was Javascript to load the data according to users operation (can search `v-for="(item,index) in list` to confirm about this). using the "requests" I only get the below content:

```
[<div :style="{height: (list.length*60)/16 + 'rem'}" class="out-row">
	<div :class="'bg-' + item.eva_type" :key="item.id" :style="{top: index*(60/16) + 'rem'}" @click="trackUserClick(item)" class="name" v-for="(item,index) in list">
		<div class="con"><h1>{{item.name}}</h1>
			<div class="color-bar-content"><span :class="item.eva_type" class="color-bar"></span><small>{{item.index_code}}</small></div>
		</div>
	</div>
	<div @scroll="handleScrollHoriz" class="in-row">
		<div :class="'bg-' + item.eva_type" :key="item.id" @click="trackUserClick(item)" class="row normal" v-for="item in list">
			<div class="ttype">{{renderTtype(item.ttype)}}</div>
			<div class="pe">{{numeral(item.pe).format('0,00.00')}}</div>
			<div class="pe-per">{{numeral(item.pe_percentile * 100).format('0,00.00') + '%'}}</div>
			<div class="pb">{{numeral(item.pb).format('0,00.00')}}</div>
			<div class="pb-per">{{numeral(item.pb_percentile * 100).format('0,00.00') + '%'}}</div>
			<div class="dyr">{{numeral(item.yeild * 100).format('0,00.00') + '%'}}</div>
			<div class="roe">{{numeral(item.roe * 100).format('0,00.00') + '%'}}</div>
			<div class="begin">{{item.peg?numeral(item.peg).format('0,00.00'):'--'}}</div>
		</div>
	</div>
</div>]
```

There are 3 ways to tackle this problem:

- Using `selenium` with Firefox web driver
- Using `phantomJS`
- Making an API using a REST client or python `request`

According to the guide [Data Science Skills: Web scraping javascript using python](https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f) I can found the responds as below:

![](find-respond-with-javascript-loaded.png)

Then when check 


reference:

- [vue.js中v-for的使用及索引获取](https://www.cnblogs.com/xulei1992/p/6015416.html)
- [Data Science Skills: Web scraping javascript using python](https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f)
