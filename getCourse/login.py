import requests
def Login(user,pwd):
    # 登录接口,成功登录后跳转到个人页面的首页（index1.asp）
    login_url = "https://jiaowu.sicau.edu.cn/jiaoshi/bangong/check.asp"
    sign = "c534ba46ed6b2abf2a7f222fecfee48"
    hour_key = "97212289813344038199293481995674813304738995971181334403906095788930461688655555813737238995971188657505813411038930337689961391880036548199695486681192"
    data =  {
    "user": user,
    "pwd": pwd,
    "lb": "S", # 身份label，s代表student
    "sign": sign, # 相对固定
    "hour_key": hour_key # 相对固定，看名字感觉是一小时刷新一次
    }
    response = requests.post(login_url, data)
    # response.encoding = "utf-8" # 换编码
    cookie_str = "ASPSESSIONIDSETCQSQS=DAOHGFFCJGMCBIMLHGJILELO;" # 存cookie
    for cookie in response.cookies:
        cookie_str += cookie.name + '=' + cookie.value + ';'
    return cookie_str

# 仅作为主程序运行时可用
if __name__ == '__main__':
    cookie_sample = Login()
    # 展示cookie样例
    print(cookie_sample)

# 所得cookie样例
##############
# jcrj%5Fbanhao=%E7%89%A9%E8%81%94%E7%BD%91202301;
# jcrj%5Fgzbh=202308596;
# jcrj%5Fnj=2023;
# jcrj%5Fpwd=89959711893774168996797181335133906246988930461690627938972820799726950990671198813470539066333888683905;
# jcrj%5Fsession=xt%5Ffb%2Cxt%5Fxxq%2Cgzbh%2Cuser%2Cuser2%2Csf%2Cxueqi%2Csf%5Fpj%2Ctemp%2Cpwd%2Cxm%2Cnj%2Cbanhao%2Cxibie%2Czy%2Cxiaoqu%2Cxzy%2C;
# jcrj%5Fsf=%E5%AD%A6%E7%94%9F;
# jcrj%5Fsf%5Fpj=%E5%90%A6;
# jcrj%5Ftemp=9301416277;
# jcrj%5Fuser=202308596;
# jcrj%5Fuser2=819929349067365886025327972136198133440381345043899646518603449789370776;
# jcrj%5Fxiaoqu=%E9%9B%85%E5%AE%89;
# jcrj%5Fxibie=%E4%BF%A1%E6%81%AF%E5%B7%A5%E7%A8%8B%E5%AD%A6%E9%99%A2;
# jcrj%5Fxm=%E5%94%90%E7%A3%8A;
# jcrj%5Fxt%5Ffb=%E9%9B%85%E5%AE%89;
# jcrj%5Fxt%5Fxxq=%E9%9B%85%E5%AE%89;
# jcrj%5Fxueqi=2024%2D2025%2D1;
# jcrj%5Fxzy=%E7%89%A9%E8%81%94%E7%BD%91%E5%B7%A5%E7%A8%8B;
# jcrj%5Fzy=%E7%89%A9%E8%81%94%E7%BD%91%E5%B7%A5%E7%A8%8B;
##############

