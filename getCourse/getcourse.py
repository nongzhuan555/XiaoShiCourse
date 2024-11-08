import requests
from .login import Login
from .getcookie import get_next_cookie
import time
# 思路:
    # 1.通过selenium真正意义上模拟人为操作进入教务网然后输入学号及密码然后一步步点击最终进入课表页面后获取原始HTML
    # 2.通过requests模拟浏览器向后台直接索要课表页面原始HTML，难点在于cookie的来源，最终决定通过从登录到课表页面的多次请求一环一环的要cookie
    # 3.requests到‘超级课程表’后台要他们洗好的数据，无需我来清洗；缺点在于接口分析更难且第三方数据来源不稳定
    ########1，2方法均需清洗数据############

# 链式请求模拟人为操作，一步到位失败
def get_course(user,pwd):
    second_url = "https://jiaowu.sicau.edu.cn/jiaoshi/bangong/main/index1.asp"
    third_url = "https://jiaowu.sicau.edu.cn/jiaoshi/bangong/main/welcome1.asp"
    fourth_url = "https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/bxq.asp"
    fifth_url = "https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/xszhinan.asp?title_id1=9&xueqi=2024-2025-1"
    course_url = "https://jiaowu.sicau.edu.cn/xuesheng/gongxuan/gongxuan/kbbanji.asp"
    login_cookie = Login(user,pwd)
    second_cookie = get_next_cookie(second_url,login_cookie)
    print("开始通过模拟请求获取课表原始HTML，过程稍慢，请稍等......\n")
    print("登录后第一次cookie:\n"+login_cookie)
    print("第二次cookie:\n"+second_cookie)
    third_cookie = get_next_cookie(third_url,second_cookie)
    print("第三次cookie:\n"+third_cookie)
    fourth_cookie = get_next_cookie(fourth_url,third_cookie)
    print("第四次cookie:\n"+fourth_cookie)
    fifth_cookie = get_next_cookie(fifth_url,fourth_cookie)
    print("第五次cookie:\n"+fifth_cookie)
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "user-agent": "Mozilla/5.0 (Windows NT10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0",
        "cookie": fifth_cookie
    }
    response = requests.get(course_url, headers=headers)
    response.encoding = 'gb2312'
    # print("以下是课表信息的原始HTML，等待清洗模块清洗......")
    # print(response.text)
    return response.text

if __name__ == '__main__':
    # 示例
    start_time = time.time()
    get_course('202308596','17318269035TL')
    end_time = time.time()
    print('本次获取课表大约花费：(单位秒)')
    print(end_time - start_time)

