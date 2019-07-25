# 稀疏性正则化 (Regularization for Sparsity)：Playground 练习



## L1 正则化练习

本练习包含一个有些混乱的小型训练数据集。在这种情况下，过拟合问题比较令人担忧。 正则化可能会有所帮助，但采用哪种形式的正则化呢？

本练习包含 5 个相关的任务。为了简化这 5 个任务之间的比较，请在单独的标签中运行每个任务。 请注意，连接 FEATURES 和 OUTPUT 的线的厚度表示每个特征的相对权重。

| 任务 | 正则化类型 | 正则化率 (lambda) |
| ---- | ---------- | ----------------- |
| 1    | L2         | 0.1               |
| 2    | L2         | 0.3               |
| 3    | L1         | 0.1               |
| 4    | L1         | 0.3               |
| 5    | L1         | 实验              |

问题：

1. 从 L2 正则化转换到 L1 正则化对测试损失与训练损失之间的差值有何影响？
2. 从 L2 正则化转换到 L1 正则化对已知权重有何影响？
3. 增加 L1 正则化率 (lambda) 对已知权重有何影响？



<iframe scrolling="no" style="width: 970px; height: 700px" class="inherit-locale" frameborder="0" src="https://developers.google.com/machine-learning/crash-course/playground/?utm_source=engedu&amp;utm_medium=ss&amp;utm_campaign=mlcc&amp;hl=zh-cn#activation=linear&amp;regularization=L2&amp;batchSize=7&amp;dataset=xor&amp;regDataset=reg-plane&amp;learningRate=0.01&amp;regularizationRate=0.1&amp;noise=30&amp;networkShape=&amp;seed=0.57899&amp;showTestData=false&amp;discretize=false&amp;percTrainData=20&amp;x=true&amp;y=true&amp;xTimesY=true&amp;xSquared=true&amp;ySquared=true&amp;cosX=false&amp;sinX=false&amp;cosY=false&amp;sinY=false&amp;collectStats=true&amp;problem=classification&amp;initZero=false&amp;hideText=true&amp;dataset_hide=true&amp;percTrainData_hide=false&amp;noise_hide=false&amp;batchSize_hide=false&amp;xTimesY_hide=false&amp;xSquared_hide=false&amp;ySquared_hide=false&amp;sinX_hide=true&amp;sinY_hide=true&amp;activation_hide=true&amp;learningRate_hide=false&amp;regularization_hide=false&amp;regularizationRate_hide=false&amp;numHiddenLayers_hide=true&amp;problem_hide=true&amp;tutorial=dp-regularization-for-sparsity&amp;goalTrainTestDiffMaxThresholdFirst=0.135&amp;goalTestLossMinThresholdFirst=0.205&amp;goalTrainTestDiffMinThresholdFirst=0.1&amp;goalTrainTestDiffMinThresholdSecond=0.05"></iframe>

