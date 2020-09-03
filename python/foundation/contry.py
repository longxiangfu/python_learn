"""
用户输入国家名称,打印出所输入国家名称和首都
"""

d = {"中国": "北京", "朝鲜": "平壤", "美国": "纽约"}
country_name = input("请输入国家名称:")
country_capture = d.get(country_name, "北京")
print("国名:", country_name, "首都:", country_capture)
