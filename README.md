# My-Python-Learning-Journey
The repository is created by a Shenzhen university student to finish his Python homework. In this repository, you will see the most satisfied code in my term！
## 我将结合if条件语句、多个函数（str、len等）设计一个班级智能成绩分析。

## 设计思路：使用元组存储成绩，并结合if条件语句进行循环判断批量输入的成绩概况（成绩等级及对应人数），分析并成列成绩后给予用户鼓励，我认为创新点在于：1.能输入多个值进行运算。2.运用len对不同等级在总人数中的占比进行班级总体评价以及个性化建议。

## 功能特性： *1.可以根据提示词“请输入学生数量”的提示词，个性化的填写不同数量的成绩  *2.运用len对不同等级在总人数中的占比进行班级总体评价以及个性化建议。

## 使用指南：首先根据提示词输入学生数量，然后输入对应数量的成绩后即可输出成绩不同等级在总人数中的占比进行班级总体评价以及个性化建议。

## 代码预览
```print("请输入学生数量：")
student_count = int(input("学生人数："))
scores = []
for i in range(student_count):
    score = int(input("请输入第" + str(i+1) + "个学生的成绩："))
    scores.append(score)
scores_tuple = tuple(scores)
# 成绩等级统计
grades = {"优": 0, "良": 0, "中": 0, "差": 0}
for score in scores_tuple:
    if score >= 90:
        grades["优"] += 1
    elif score >= 75:
        grades["良"] += 1
    elif score >= 60:
        grades["中"] += 1
    else:
        grades["差"] += 1
# 显示结果
print("分析结果：")
print("成绩元组：" + str(scores_tuple))
print("等级分布：" + str(grades))
# 简单建议
if grades["差"] > len(scores_tuple) * 0.3:
    print("建议：需要加强学习！")
elif grades["优"] >= len(scores_tuple) * 0.5:
    print("建议：表现优秀！")
else:
    print("建议：继续努力！")
```

# 学习心得与规划：首先我第一次了解在网上有这么全面且面向全世界的一个巨大代码数据库，在浏览的过程中看到了各式各样的代码（只有想不到，没有找不到），感觉是一个非常好可以自学的平台。在完成本次作业的过程中，首先第一个困难就是GitHub网站非常不稳定需要梯子或者修改ip才能让网站稳定运行（纯个人摸索出来的太难了），但在这个网站中，我认为这是一个很好与他人学习交流的机会，并且自己也能在上面公布自己库中代码，分享自己的一些心得与发现，更有可能收获指导与建议，简直就是一个代码人自己的贴吧。我将在上面查找借鉴自己所需要的代码，并虚心学习他人在代码中的巧思。
