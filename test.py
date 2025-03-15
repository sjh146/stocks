from urllib.parse import urljoin
from urllib.robotparser import RobotFileParser

url="https://wwww.inflearn.com/course/실습-파이썬-웹크롤링-웹페이지-자동화"
robot_url=urljoin(url,"/robots.txt")
print(robot_url)
robot_parser=RobotFileParser()
robot_parser.set_url(robot_url)
robot_parser.read()
print (robot_parser)
print()
if robot_parser.can_fetch("Mybot",url):
    print("Allow")
else:
    print("Disallow")