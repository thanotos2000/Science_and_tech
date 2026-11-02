
#物理/辐射剂量学

# 1 重要的国际组织:


ICRP (International Commission on Radiological Protection): 国际辐射防护委员会

ICRU (International Commission on Radiation Units and Measurements): 国际辐射单位和测量委员会

IAEA (International Atomic Energy Agency): 国际原子能机构

UNSCEAR (United Nations Scientific Committee on the Effects of Atomic Radiation): 联合国原子辐射影响科学委员会




电离辐射
- 电离辐射：以其激发和电离物质的能力为表征
- 最常见的电离辐射是α、β或γ，重带电粒子以及中子。
	- γ射线:原子核发生的，或者正负电子湮灭
	- X射线：带电粒子发生的（通常电子），X射线机
	- 快电子：核里发出来的，β射线；带电粒子碰撞过程，δ射线
	- 重带电粒子：质子、氘、氚、α粒子、π介子
	- 中子

![[Pasted image 20240420165310.png]]

电离：带电粒子或者非带电粒子获得动能足以克服原子的束缚.
- 电子挣脱束缚，入射粒子最小能量，电离能
- 在电离过程中产生的负离子和正离子形成离子对

Note: 电离是一个能量传递的过程

直接致电离辐射: 快速带电粒子 (β射线，质子，α粒子)
- 沿着粒子轨迹，通过多次小的库仑力相互作用将能量授予物质

间接致电离辐射: X,  $\gamma$ 射线光子 (光电效应, 康普顿散射) 或中子 (反冲核, 次级质子, 氘核, $\alpha$粒子)
- 分两个阶段能量沉积
	- 在少数几次不连续的相对较强的相互作用中先将能量传递给物质中的带电粒子, 
	- 然后快速带电粒子再将能量传递给物质.
- 光子: 光电效应, 康普顿散射 --- 电子
- 中子: 反冲核, 次级质子, 氘核, $\alpha$粒子

# 2 辐射来源

天然辐射&人工辐射

人工辐射:
- 消费品
- 航空旅行
- 大气核试验
- 核能设施
- 医疗照射

# 3 随机量

随机量
- 值随机出现
- 进针对有限的区域范围定义. 其值随空间和时间的变化不连续.
- 原则上其值可全部测得
- 测量次数足够大下, 随机量的期望值为其测量值的平均值

# 4 电离辐射场

电离辐射场: 无论在空间还是介质内部, 凡电离辐射在其中<mark style="background: #FFF3A3A6;">通过, 传播以致经由相互作用发生能量传递</mark>的整个空间范围, 称为电离辐射场.

# 5 注量

注量: 一个大圆面积 $𝑑𝑎$ 为无限小球，一段时间 $t$ 内入射到这个球内的粒子数为 $𝑑𝑁$ ，注量为
$$\Phi=\frac{dN_e}{da}$$
- 单位: $m^{-2}$

![[Pasted image 20240625152135.png]]

为何要定义球体积元?

![[Pasted image 20240625152219.png]]


注量率 (或通量密度): 单位时间内注量
$$\varphi=\frac{\mathrm{d}\Phi}{\mathrm{d}t}=\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\mathrm{d}N_{e}}{\mathrm{d}a}\right)$$
- 单位: $m^{-2}\cdot s^{-1}$

能注量: 将带电粒子的能量考虑进来, 一个圆面积 $𝑑𝑎$ 的无限小球，一段时间 $t$ 内入射到这个球内的粒子数为 $𝑑𝑁$ , 这些粒子的总能量为 $dR$， 能注量为
$$\psi=\frac{\mathrm{d}R}{\mathrm{d}a}$$
- 单位: $J\cdot m^{-2}$, or $erg\cdot m^{-2}$
- 对单一能量 $E$ 的射线, $R=EN$, $\Psi=E\Phi$

同样地, 能通量密度
$$\psi=\frac{\mathrm{d}\Psi}{\mathrm{d}t}=\frac{\mathrm{d}}{\mathrm{d}t}\left(\frac{\mathrm{d}R}{\mathrm{d}a}\right)$$
- 单位: $J·m^{-2}·s^{-1}$  或 $erg^{-2}·cm^{-2}·s^{-1}$ .

微分通量密度: 任一时刻, P点处的通量密度实际上是入射粒子能量 $E$, 入射立体角度$\theta$ 和 $\beta$ 的函数
$$\varphi^{\prime}\left(\theta,\beta,E\right)$$
因而通过立体角元 $d\Omega$, 能量在 $E$ 到 $dE$ 之间的粒子入射到该球单位大圆面积上的数目为
$$\varphi^{\prime}\left(\theta,\beta,E\right)\mathrm{d}\Omega\mathrm{d}E$$
因而通量密度 $\varphi$
$$\varphi=\int_{\theta=0}^{\pi}\int_{\beta=0}^{2\pi}\int_{E=0}^{E_{\max}}\varphi^{\prime}(\theta,\beta,E)\mathrm{sin}\theta\mathrm{d}\theta\mathrm{d}\beta\mathrm{d}E$$

当选定 E 为变量下的微分分布称为能谱.

注量另一个定义:
$$\phi=\frac{\overline{L}dN}{dV}$$
- 二者是等价的 
$$\Phi=\frac{dN}{da}=\frac{4dN}{dS}=\frac{4\overline{L}dN}{4dV}=\frac{\overline{L}dN}{dV}$$
