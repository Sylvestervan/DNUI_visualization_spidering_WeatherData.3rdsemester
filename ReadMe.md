# Crawling the Global Historical Weather Data and Machine Learning

--- By *Sylvester Van* in Dalian Neusoft University of Information

***

### Part 1 --- developing schedule

#### a. 前言

由于爬取天气数据的体量庞大，技术需求质量高。 故为了在有限的时间内完成该项目，列出前期的日程安排和项目愿景非常有利于开发效率的提升和自身水平的提高。</br>

我在 2023-2024 学年第二学期的《数据库原理与应用》这门课上已经做出了由骆晓莉老师所评价的 “只要进一步完善就能媲美毕设”的数据库逻辑。《数据预处理》期末答辩作业选择了更难的Task2，让我初步与国际尖端文本处理的模型接触。可以说，彼时的努力给此时的我带来了课题优势。</br>

这也是我在实践学期选题爬取天气数据的主要原因，有现成的世界范围内的地理数据预设和一些机器学习经验可供我完善和深化此实践学期的技术需求。</br>

对我个人而言，无论是未来继续想做一个更大的项目，比如MacOS，iOS上的ObjectiveC的程序。还是为了升本复习专业课基础知识，此次项目都提供了更多可能性的机会去探索计算机科学知识的机会。</br>

简单描述后，Part1的主要内容将被列出，并将持续更新，后续会公布在Github上。

#### b. 总体计划 --- *update 2024.07.11*

>- [x] 确定选题。 *2024.07.09* </br> 从不严谨的标题修改为《全球天气历史数据爬取与机器学习》--- *2024.07.10*
>- [x] 制作每日汇报的自述文件。 *2024.07.09 onwards* 
>- [x] 基础知识的储备。 *2023-09-17 >>> 2024.07.11\*非常严谨:D*
>- [x] 认识到涉及哪些库。 *2024.07.03 >>> 2024.07.11* </br> 经过考虑(*潜在的得分项)，综合应用了正则表达式和.xpath()
>- [x] 选题内确定爬取范围和网站。 </br> 目前正在爬取数据的网站/www.worldweatheronline.com </br> 仅爬取上学期自建数据库中region_info中中国的部分城市，爬取行为是非恶意的非盈利的且仅是学术性质的。具体城市列表如下：
>- Qiqihar, China
>- Weihai, China
>- Dalian, China
>- Harbin, China
>- Xiamen, China
>- Beijing, China
>- Shanghai, China
>- Suzhou, China </br> --- *2024.07.10*
>- [x] 集中测试网站爬取的可行性。</br> weatherdataonline是可用的，是以提交表单的形式换页 --- *2024.07.11* </br> 
>- [x] 量级数据获取。</br> 目前因为时间原因暂定为下列三个城市2014-01-01 --->> 2024-07-10的数据 </br>*（est.approximately 4000 datas per spider）* </br> Dalian, China </br> Qiqihar, China </br> Weihai, China </br> 大连和威海，齐齐哈尔分别做一个实验组。地理原因带来的气候条件可视化.etc </br> 目前完成度 *20%* --- *2024.07.11*｜预计完成时间*2024.07.14*
>- 爬取完成qiqihar_weather_daily.jsonl, 同时优化爬取文件名（加了时间戳）*2024.07.12 11:40 AM*
>- [x] 确认数据本地存储及格式。</br> 文件格式为jsonline
>- [x] 广泛了解爬取数据的方式。
>- [ ] 将数据存储到MySQL中，同时针对WeatherBroadcastSystem进行真实化。
>- [ ] 数据分析：利用Transformer库进行机器学习。
>- [ ] 数据分析：利用第三方库进行可视化。
>- [ ] 撰写项目报告。
>- [ ] 制作答辩Powerpoint。
>- [ ] 制作文件架构图(Structure Chart)，程序流程图(Flow Chart)，优化MySQL数据库的Entity-Relationship Diagram

### Part 2 --- Introduction of Programme

#### i. How To Run?

for one's terminal

> `scrapy crawl city_weather_daily/hourly -a start_date=yyyy-mm-dd -a end_date=yyyy-mm-dd` </br>

and strictly

> `start_date=yyyy-mm-dd` =< `end_date=yyyy-mm-dd` 

*normally, start_date is no less than 1970-01-01 for most regions

for example:

> `scrapy crawl dalian_weather_daily -a start_date=2023-09-03 -a end_date=2024-06-22 --nolog`

Additionally, if users are used to customizing the path of the data spidered, then

> a. get into the `pipelines` file </br>
> b. find '`output_dir`' by initialization </br>
> c. change the path within the quote </br>
> d. check the accessibility of the root dictionary </br>

-- to be continued --

### Part 3 --- Syntax

-- to be continued --

### Part 4 --- Application of ML

-- to be continued --

### Part 5 --- Conclusion

-- to be continued --

### Part 6 --- Write at the End

-- to be continued --

***

Copyright (c) By Sylvester Van, Dalian Neusoft University of Information, Higher Vocational, Artificial Intelligence and Technology Department, Class 23102. </br>
Contact E-mail: Naringinstudio@outlook.com(Personal, available always), 2323450016@dnui.edu.cn(Public, disabled at 2026.7 onwards). </br>
Discord: cs_sylvester_van
