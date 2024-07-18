import scrapy

class Person(scrapy.Item):
    name = scrapy.Field()
    job = scrapy.Field()
    email = scrapy.Field()

bob = Person(name='bob', job='teacher', email='abc@123.com')
print(bob)
print(bob['job'])
print(bob.keys())
print(bob.items())  # 获取项目视图