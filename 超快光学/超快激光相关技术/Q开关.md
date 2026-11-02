# Q开关（Q Switches）

分类: **[光子器件](https://www.oe1.com/encyclopedia/category/6962598421545242627.html)**

定义: 通常用于<mark style="background: #FFF3A3A6;">在激光器中产生纳秒脉冲的光开关</mark>.


## Q开关（Q Switches） 详述

Q开关（或Q开关装置）是一种快速的光开关，即一种可以在不同状态之间快速切换的装置，它对通过它的激光束分别造成非常低或相当高的功率<mark style="background: #FFF3A3A6;">损失</mark>。Q开关被用于激光谐振器内，目的是对激光进行主动Q开关；这是一种用于产生短的强[光脉冲](https://www.oe1.com/encyclopedia/7026070768548532224.html)的技术，其中[脉冲持续时间](https://www.oe1.com/encyclopedia/7032228553084665856.html)通常在纳秒范围内。

类似的装置也可用于产生带有空[腔](https://www.oe1.com/encyclopedia/7025306920576462848.html)倾倒的脉冲，但在这种情况下对光开关的详细要求实际上有些不同。


## Q开关的类型

### 1. 声光式Q开关

![[Pasted image 20231031225740.png]]

图1：非共振[声光调制器](https://www.oe1.com/product/category/6988033364354932736.html)的设置示意图。一个换能器产生一个声波，在这个声波上，光束被部分地[衍射](https://www.oe1.com/encyclopedia/7053975485007351808.html)出来。

最常见的类型是声光调制器。<mark style="background: #FFF3A3A6;">只要声波关闭，通过一些水晶或玻璃片的传输损失就很小，而在声波开启时，会发生强烈的布拉格反射，因此，损失通常为每次50%，相当于线性激光谐振器中每次双通道的75%。</mark>

为了<mark style="background: #FFF3A3A6;">产生声波，需要一个电子驱动器，其射频功率为1瓦</mark>（或大孔径设备为几瓦），无线电频率（RF）为100MHz。

开关速度（或调制[带宽](https://www.oe1.com/encyclopedia/7025373368956706816.html)）最终不是由声光转换器本身限制，而是<mark style="background: #FFF3A3A6;">由声速和光束直径限制</mark>。后者意味着<mark style="background: #FFF3A3A6;">开关速度对于具有较大光束的高功率激光器来说暂且变得较低</mark>。

更多的细节，请参见声光Q开关的文章. [[声光Q开关]]。



### 2. 电光Q开关

对于特别<mark style="background: #FFF3A3A6;">高的开关速度</mark>，例如在Q开关的[微芯片激光器](https://www.oe1.com/encyclopedia/7026809458466099200.html)中的要求，可以使用[电光调制器](https://www.oe1.com/encyclopedia/7047449691290173440.html)（Pockels电池）。在这里，光的偏振状态可以通过<mark style="background: #FF5582A6;">电光效应</mark>（或波克尔斯效应）来改变，这可以<mark style="background: #FFF3A3A6;">通过使用一个偏振器变成损失的调制</mark>。

与声光器件相比，需要<mark style="background: #FFF3A3A6;">更高的电压</mark>（需要<mark style="background: #FFF3A3A6;">以纳秒级的速度进行切换</mark>），但另一方面，<mark style="background: #FFF3A3A6;">没有射频信号</mark>。

电光Q开关的一个典型应用领域是在具有相当高[增益](https://www.oe1.com/encyclopedia/7027172850834804736.html)的激光器中，而AOM的衍射效率是不够的。为了实现短脉冲，需要一个高的激光增益。如果需要高的[脉冲能量](https://www.oe1.com/encyclopedia/7032227456492273664.html)，但又想限制[模式](https://www.oe1.com/encyclopedia/7059774521176780800.html)面积，例如由于[谐振器设计](https://www.oe1.com/encyclopedia/7025309784484982784.html)的限制，激光增益也可能变得很高。

### 3. 机械式Q开关

特别是在Q开关激光器的早期，机械Q开关经常被使用--主要是以<mark style="background: #FF5582A6;">旋转镜</mark>的形式。这里，一个小的激光镜被安装在一个快速旋转的装置上。该镜子被用作线性激光谐振器的端面镜。当镜子处于关闭激光谐振器的位置时，一个脉冲就会建立起来。这种方法很简单，适用于广泛的光谱区域，不需要特殊的部件，而且相当坚固（例如在损坏阈值方面），特别适合于脉冲持续时间相对较长的高功率激光器。它仍然在<mark style="background: #FFF3A3A6;">少数情况</mark>下被使用。

### 4. 无源Q开关

无源Q开关是由激光本身触发的可[饱和吸收器](https://www.oe1.com/encyclopedia/7044198424656928768.html)。在这里，<mark style="background: #FFF3A3A6;">一旦有足够的能量储存在增益介质中，Q开关引入的损失必须小到足以被激光增益所克服, 否则，激光就无法开始工作</mark>。然后，<mark style="background: #FFF3A3A6;">激光功率首先相对缓慢地上升，一旦达到一定水平，吸收器就会饱和，这样损失就会下降，净增益就会增加，激光功率就可以急剧上升，形成一个短脉冲</mark>。

对于工作在1μm光谱区的被动Q开关[YAG激光器](https://www.oe1.com/encyclopedia/7068841425938821120.html)，Cr4+:YAG晶体通常作为被动Q开关。还有其他可能的材料，如各种掺杂的晶体和玻璃，半导体可饱和吸收镜特别适用于小脉冲能量。


## 关键特性

为了选择一个合适的Q开关，必须考虑以下方面:

- 工作波长，这影响到例如所需的[抗反射涂层](https://www.oe1.com/encyclopedia/7043469725607321600.html)
- 开放的孔径
- 高损耗状态（特别是对于高增益激光器）和低损耗状态（影响功率效率）的损耗
- 开关速度（特别是对于短[脉冲激光器](https://www.oe1.com/encyclopedia/7025741554810052608.html)）。
- 损伤阈值强度
- 所需的射频功率
- 冷却要求
- 设置的尺寸（特别是对于紧凑型激光器来说）。
- 当然，必须选择电子驱动器，以便在各方面与Q开关相适应。