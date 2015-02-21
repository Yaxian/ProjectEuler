#encoding:utf-8
__metaclass__=type
"""
1900年1月1日是星期1
1901年1月1日是星期2
"""
from datetime import date
#从datatime模块导入date “type”
s = 0
for year in range(1901, 2001):
	for month in range(1, 13):
		if date(year, month, 1).isoweekday() == 7:
        		"""
        		.isoweekday():返回data()代表的星期几
        		Monday==1……Sunday==7
        		"""
        		s += 1
print (s)

"""
1901~2000一共有100年，100年中共有12个月。
1星期共有7天。
12个月中肯定有12//7个月是以星期日开始的。
"""
print 100*12//7