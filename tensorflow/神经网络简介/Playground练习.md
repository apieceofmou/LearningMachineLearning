# 神经网络简介 (Introduction to Neural Networks)：Playground 练习



## 首个神经网络

在本练习中，我们将训练首个小型神经网络。借助神经网络，我们无需使用显式特征组合，便可学习非线性模型。

**任务 1**：给定模型将两个输入特征合并为一个神经元。此模型会学习任何非线性规律吗？运行该模型，以确认您的猜测是否正确。

**任务 2**：尝试将隐藏层中神经元的数量从 1 增加到 2，此外，尝试将线性激活更改为非线性激活（例如 ReLU）。您能否创建可以学习非线性的模型？

**任务 3**：通过添加或移除隐藏层和每层的神经元，继续进行实验。此外，您可以随时更改学习速率、正则化和其他学习设置。要使测试损失不超过 0.177，您可以使用的最少节点和层数是多少？



<iframe scrolling="no" style="width: 960px; height: 700px" class="inherit-locale" frameborder="0" src="https://developers.google.com/machine-learning/crash-course/playground/?utm_source=engedu&amp;utm_medium=ss&amp;utm_campaign=mlcc&amp;hl=zh-cn#activation=linear&amp;regularization=L2&amp;batchSize=10&amp;dataset=xor&amp;regDataset=reg-plane&amp;learningRate=0.01&amp;regularizationRate=0&amp;noise=35&amp;networkShape=1&amp;seed=0.50819&amp;showTestData=false&amp;discretize=false&amp;percTrainData=50&amp;x=true&amp;y=true&amp;xTimesY=true&amp;xSquared=true&amp;ySquared=true&amp;cosX=false&amp;sinX=false&amp;cosY=false&amp;sinY=false&amp;collectStats=true&amp;problem=classification&amp;initZero=false&amp;hideText=true&amp;dataset_hide=true&amp;percTrainData_hide=false&amp;noise_hide=false&amp;batchSize_hide=false&amp;xTimesY_hide=true&amp;xSquared_hide=true&amp;ySquared_hide=true&amp;sinX_hide=true&amp;sinY_hide=true&amp;activation_hide=false&amp;learningRate_hide=false&amp;regularization_hide=false&amp;regularizationRate_hide=false&amp;numHiddenLayers_hide=false&amp;problem_hide=true&amp;tutorial=dp-neural-net-intro-first&amp;goalTestLossMinThresholdFirst=0.35&amp;goalTestLossMinThresholdSecond=0.2&amp;goalTestLossMinThresholdThird=0.177"></iframe>



## 神经网络初始化

本练习将再次使用 XOR 数据，但这次用于研究训练神经网络的重复性以及初始化的重要性。

**任务 1**：运行给定模型四到五次。在每次试验开始之前，请点击**重置网络**按钮，以获取新的随机初始化数据。（**重置网络**按钮是一个圆形重置箭头，位于“播放”按钮左侧）。让每次试验至少运行 500 步，以确保图形能收敛。每个模型输出会收敛为何种形状？对于初始化在非凸优化中发挥的作用，这说明了什么？

**任务 2**：尝试添加一层和几个额外节点，让模型变得稍微复杂点。重复任务 1 的试验。这是否可以提高结果的稳定性？



<iframe scrolling="no" style="width: 960px; height: 700px" class="inherit-locale" frameborder="0" src="https://developers.google.com/machine-learning/crash-course/playground/?utm_source=engedu&amp;utm_medium=ss&amp;utm_campaign=mlcc&amp;hl=zh-cn#activation=relu&amp;regularization=L2&amp;batchSize=10&amp;dataset=xor&amp;regDataset=reg-plane&amp;learningRate=0.01&amp;regularizationRate=0&amp;noise=35&amp;networkShape=3&amp;seed=0.50819&amp;showTestData=false&amp;discretize=false&amp;percTrainData=50&amp;x=true&amp;y=true&amp;xTimesY=true&amp;xSquared=true&amp;ySquared=true&amp;cosX=false&amp;sinX=false&amp;cosY=false&amp;sinY=false&amp;collectStats=true&amp;problem=classification&amp;initZero=false&amp;hideText=true&amp;dataset_hide=true&amp;percTrainData_hide=false&amp;noise_hide=false&amp;batchSize_hide=false&amp;xTimesY_hide=true&amp;xSquared_hide=true&amp;ySquared_hide=true&amp;sinX_hide=true&amp;sinY_hide=true&amp;activation_hide=false&amp;learningRate_hide=false&amp;regularization_hide=false&amp;regularizationRate_hide=false&amp;numHiddenLayers_hide=false&amp;problem_hide=true&amp;tutorial=dp-neural-net-intro-initialization&amp;goalTestLossMinThresholdFirst=0.2"></iframe>

## 神经网络螺旋

此数据集是一种混乱的螺旋。显然，线性模型不适用于此处，但即使手动定义的特征组合可能也很难构建。

**任务 1**：只使用 X1 和 X2 训练您可以获得的最佳模型。您可以随时添加或移除层和神经元，以及更改学习速率、正则化率和批量大小等学习设置。您可以获得的最佳测试损失是多少？此模型输出表面的平滑程度如何？

**任务 2**：即使使用神经网络，通常也需要一些特征工程，才能获得最佳性能。尝试添加额外向量积特征或 sin(X1) 和 sin(X2) 等其他转换。您是否获得了更好的模型？模型输出表面是否更平滑？



<iframe scrolling="no" style="width: 960px; height: 700px" class="inherit-locale" frameborder="0" src="https://developers.google.com/machine-learning/crash-course/playground/?utm_source=engedu&amp;utm_medium=ss&amp;utm_campaign=mlcc&amp;hl=zh-cn#activation=relu&amp;batchSize=10&amp;dataset=spiral&amp;regDataset=reg-plane&amp;learningRate=0.1&amp;regularizationRate=0.01&amp;noise=80&amp;networkShape=3,2&amp;seed=0.38953&amp;showTestData=false&amp;discretize=false&amp;percTrainData=50&amp;x=true&amp;y=true&amp;xTimesY=false&amp;xSquared=false&amp;ySquared=false&amp;cosX=false&amp;sinX=false&amp;cosY=false&amp;sinY=false&amp;collectStats=false&amp;problem=classification&amp;initZero=false&amp;hideText=true&amp;problem_hide=true&amp;tutorial=dp-neural-net-intro-spiral&amp;goalTestLossMinThresholdFirst=0.4&amp;goalTestLossMinThresholdSecond=0.25"></iframe>

