print("请输入学生数量：")
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
