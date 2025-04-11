
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取结果数据
file_path = '../outcome/adult/adult_results.csv'
data = pd.read_csv(file_path)

# 设置可视化库
sns.set(style="whitegrid")

# 绘制柱状图对比不同折叠的准确率
sns.barplot(x='fold', y='accuracy', data=data)
plt.xlabel('Fold')
plt.ylabel('Accuracy')
plt.title('Accuracy across 5 Folds for Adult Dataset')

# 保存可视化结果
plt.savefig('accuracy_across_folds.png')

# 显示图表
plt.show()    