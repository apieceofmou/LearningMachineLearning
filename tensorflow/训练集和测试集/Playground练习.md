# 训练集和测试集 (Training and Test Sets)：Playground 练习



## 训练集和测试集

让我们回到 Playground，以便使用训练集和测试集进行实验。

在直观图示中：

- 每个蓝点表示一类数据的一个样本（例如，垃圾邮件）。
- 每个橙点表示另一类数据的一个样本（例如，非垃圾邮件）。
- 背景颜色表示该模型对于应该在何处找到相应颜色样本的预测。某个蓝点周围显示蓝色背景表示该模型正确地预测了该样本。相反，某个蓝点周围显示橙色背景则表示该模型错误地预测了该样本。



本练习提供了从同一数据集中抽取的测试集和训练集。默认情况下，直观图示只会显示训练集。如果您还想看到测试集，请点击直观图示正下方的**显示测试数据** (Show test data) 复选框。在直观图示中，请注意以下区别：

- 训练样本具有白色轮廓。
- 测试样本具有黑色轮廓。

**任务 1**：使用指定设置运行 Playground，具体操作如下：

1. 点击“运行/暂停”(Run/Pause) 按钮
2. 观察测试损失值和训练损失值的变化。
3. 当测试损失值和训练损失值停止变化或好一会儿才会变化一次时，请再次按“运行/暂停”(Run/Pause) 按钮，以暂停 Playground。

测试损失与训练损失之间存在显著差异吗？

**任务 2**：执行以下操作：

1. 按“重置”(Reset) 按钮。
2. 修改[学习速率](https://developers.google.com/machine-learning/crash-course/reducing-loss/learning-rate)。
3. 按“运行/暂停”(Run/Pause) 按钮：
4. 让 Playground 运行至少 150 次迭代。



在这种新的学习速率下，测试损失与训练损失之间的差值是降低了还是升高了？如果同时修改了学习速率和[批量大小](https://developers.google.com/machine-learning/glossary#batch_size)，会出现什么情况？

**（可选）任务 3**：您可以通过标签为**训练数据与测试数据之比** (Ratio of training to test data) 的滑块来控制测试数据与训练数据之比。例如，当该滑块设为 90% 时，训练集包含的样本比测试集多很多。当该滑块设为 10% 时，训练集包含的样本比测试集少很多。

执行以下操作：

1. 将“训练数据与测试数据之比”(Ratio of training data to test data) 从 50% 降至 10%。
2. 尝试不同的学习速率和批量大小，记录您的发现。

改变训练数据与测试数据之比是否会更改您在任务 2 中找出的最佳学习设置？如果是，原因是什么？



<iframe scrolling="no" style="width: 970px; height: 700px" class="inherit-locale" frameborder="0" src="https://developers.google.com/machine-learning/crash-course/playground/?utm_source=engedu&amp;utm_medium=ss&amp;utm_campaign=mlcc&amp;hl=zh-cn#activation=linear&amp;batchSize=1&amp;dataset=gauss&amp;regDataset=reg-plane&amp;learningRate=3&amp;regularizationRate=0&amp;noise=80&amp;networkShape=&amp;seed=0.06680&amp;showTestData=false&amp;discretize=false&amp;percTrainData=50&amp;x=true&amp;y=true&amp;xTimesY=false&amp;xSquared=false&amp;ySquared=false&amp;cosX=false&amp;sinX=false&amp;cosY=false&amp;sinY=false&amp;collectStats=true&amp;problem=classification&amp;initZero=false&amp;hideText=true&amp;dataset_hide=true&amp;percTrainData_hide=false&amp;noise_hide=false&amp;batchSize_hide=false&amp;xTimesY_hide=true&amp;xSquared_hide=true&amp;ySquared_hide=true&amp;sinX_hide=true&amp;sinY_hide=true&amp;activation_hide=true&amp;learningRate_hide=false&amp;regularization_hide=true&amp;regularizationRate_hide=true&amp;numHiddenLayers_hide=true&amp;problem_hide=true&amp;tutorial=dp-training-and-test-sets&amp;goalTrainTestDiffMinThresholdFirst=0.02&amp;goalTrainTestDiffMaxThresholdFirst=0.4"></iframe>