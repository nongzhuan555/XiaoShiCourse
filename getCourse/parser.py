import re
def parser_raw_html(raw_html):
    final_info = []  # 最终课程信息的字典列表
    # 先把课程按照一行一行拆出来，第一行代表第一大节，以此类推，一天一共五大节课
    row_matches = re.findall(r'(<td width="2%" align="center".*?</tr>)', raw_html, re.DOTALL)  # 匹配换行符
    course_order = 0  # 代表课程序号，即某天的第几节
    for row_str in row_matches:
        course_order += 1
        # 第一次匹配，把每行内容的单元格逐个分出来
        week_order = 0  # 代表星期几
        first_matches = re.findall("<td width='13.5%' valign=top align=center height=50>(.*?)</td>",
                                   row_str)  # 第一次清洗返回的数组
        second_matches = []  # 存放第二次清洗的数据
        for match in first_matches:
            week_order += 1
            # 如果该单元格是空的说明没课，舍去
            if not match.startswith('&nbsp;'):
                total_order = f'星期{week_order}-第{course_order}大节------'
                second_matches.append(total_order + match)
        third_matches = []  # 存放第三次清洗的数据，也是所有课程数据
        for match in second_matches:
            sub_string = '<br>--------------------<br>'
            # 通过观察，发现分隔符数量等于该单元格中课程数量
            if sub_string in match:
                course_num_in_this_td = match.count(sub_string)
                class_order = re.search('(.*?)------', match)
                if course_num_in_this_td == 1:
                    pattern_1 = '(.*?)<br>--------------------<br>'
                    result_1 = re.search(pattern_1, match)
                    if result_1.group(1) != '&nbsp;' and result_1.group(1):
                        third_matches.append(result_1.group(1))
                elif course_num_in_this_td == 2:
                    pattern_2 = '(.*?)<br>--------------------<br>(.*?)<br>--------------------<br>&nbsp;'
                    result_2 = re.search(pattern_2, match)
                    if result_2.group(1) != '&nbsp;' and result_2.group(1):
                        third_matches.append(class_order.group(1) + '------' + result_2.group(1))
                    if result_2.group(2) != '&nbsp;' and result_2.group(2):
                        third_matches.append(class_order.group(1) + '------' + result_2.group(2))
                else:
                    # 默认一个单元格中最多只可能有三节课
                    pattern_3 = '(.*?)<br>--------------------<br>(.*?)<br>--------------------<br>(.*?)<br>--------------------<br>&nbsp;'
                    result_3 = re.search(pattern_3, match)
                    if result_3.group(1) != '&nbsp;' and result_3.group(1):
                        third_matches.append(class_order.group(1) + '------' + result_3.group(1))
                    if result_3.group(2) != '&nbsp;' and result_3.group(2):
                        third_matches.append(class_order.group(1) + '------' + result_3.group(2))
                    if result_3.group(3) != '&nbsp;' and result_3.group(3):
                        third_matches.append(class_order.group(1) + '------' + result_3.group(3))
        for match in third_matches:
            # 修复前面代码中的瑕疵，统一格式
            if match.count('------') == 2:
                match = match[14:]
            # 判断是否为单双周
            isEvenOrOdd = re.search('<font color=red>(.*?)</font>', match)
            if isEvenOrOdd:
                isEvenOrOdd = isEvenOrOdd.group(1)
            week_range = re.search('<br>(.*?)周', match).group(1)
            week_range = re.search(r'<br>(.*)', week_range).group(1)
            if isEvenOrOdd and isEvenOrOdd == '(单周)':
                range_start = int(re.search('(.*)-(.*)', week_range).group(1))
                range_end = int(re.search('(.*)-(.*)', week_range).group(2)) + 1
                week_range = [num for num in range(range_start, range_end) if num % 2 == 1]
            elif isEvenOrOdd and isEvenOrOdd == '(双周)':
                range_start = int(re.search('(.*)-(.*)', week_range).group(1))
                range_end = int(re.search('(.*)-(.*)', week_range).group(2)) + 1
                week_range = [num for num in range(range_start, range_end) if num % 2 == 0]
                # print(week_range)
            elif not re.search('(.*)-(.*)', week_range):
                # 离散周，直接提取数字即可
                week_range = re.findall(r'\d+', week_range)
            else:
                # 否则就是连续周
                range_start = int(re.search('(.*)-(.*)', week_range).group(1))
                range_end = int(re.search('(.*)-(.*)', week_range).group(2)) + 1
                week_range = [num for num in range(range_start, range_end)]
            detail_time = re.search('(.*?)------', match)
            detail_time = detail_time.group(1)
            detail_time = re.search('星期(.*?)-第(.*?)大节', detail_time)
            detail_time = detail_time.group(1) + "-" + detail_time.group(2)
            course_name = re.search('------(.*?)：', match)
            teacher = re.search('：(.*?)<br>', match)
            classroom = (re.search('<br>雅安校区：(.*?)<br>', match)
                         or re.search('<br>温江校区：(.*?)<br>', match)
                         or re.search('<br>都江堰校区：(.*?)<br>', match))
            course_dict = {
                "detail_time": detail_time,
                "course_name": course_name.group(1),
                "teacher": teacher.group(1),
                "classroom": classroom.group(1),
                "render_week": week_range
            }
            final_info.append(course_dict)
    return final_info



