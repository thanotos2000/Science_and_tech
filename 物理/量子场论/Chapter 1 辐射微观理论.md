---
tags:
  - 物理/量子场论
---

# 1 黑体辐射

经典地，尺寸为 L 的盒子可支持具有特定角频率的驻波
$$\omega =\dfrac{2\pi}{L}|\overrightarrow{n}|c \tag{1.1}$$
1900年之前，物理学家相信每种模式的能量可任意大。

根据（经典）均分定理，黑体应该在所有模式下均等地发光，且强度随着相空间的微分体积而增长：
$$I(\omega)\equiv\frac1V\frac d{d\omega}E(\omega)=\mathrm{const}\times c^{-3}\omega^2k_BT\quad\text{(classical)}$$
这一结果来自量纲分析：量纲为 $\text{能量}\times \text{时间}\times \text{距离}^{-3}$ ，由 $\omega$, $k_BT$ , 和 $c$。

经典光谱每单位频率发射的辐射量应该随着频率的增加而增加，这一结果被称为紫外灾难。

![[物理/量子场论/附件/Pasted image 20240205234317.png]]

显然，均分定理对黑体辐射不起作用。

观测结果与经典预测不同，普朗克假设：空腔中每个电磁模式的能量都是以频率量子化的：
$$E_n=\hbar\omega_n=\frac{2\pi}L\hbar|\vec{n}|=|\vec{p}_n|$$
爱因斯坦解释，光是粒子（光子）组成的。注意，如果激发是粒子，则它们是无质量的：
$$m_n^2=E_n^2-|\vec{p_n}|^2=0$$
如果普朗克和爱因斯坦是对的，光实际上是无质量光子的集合。这一假设有许多实验结果：
- 光的量子化解决了黑体辐射难题；
- 具有能量的光导致了光电效应；
- 具有动量的光导致康普顿散射。

并且，能量假说是导致量子场论发展的关键见解。

根据普朗克假设，对应每种模式频率 $\omega_n$ ，可激发整数 j 次，产生能量 $jE_n=j(\hbar\omega )$. 在模式中找到那么多能量的概率与在任何事物中找到能量的概率相同，正比于与玻尔兹曼 $exp（−\text{energy}/k_BT）$。因此，每个模式下的能量期望为
$$\langle E_n\rangle=\frac{\sum_{j=0}^\infty(jE_n)e^{-jE_n\beta}}{\sum_{j=0}^\infty e^{-jE_n\beta}}=\frac{-\frac d{d\beta}\frac1{1-e^{-\hbar\omega_n\beta}}}{\frac1{1-e^{-\hbar\omega_n\beta}}=\frac{\hbar\omega_n}{e^{\hbar\omega_n\beta}-1}}=\dfrac{\hbar \omega _n}{e^{\hbar\omega _n\beta }-1}$$
其中，$\beta =1/k_BT$ 。取连续极限 $L→∞$. 黑体中频率ω的平均总能量是
$$\begin{aligned}E(\omega)&=\int^\omega d^3\vec{n}\frac{\hbar\omega_n}{e^{\hbar\omega_n\beta}-1}=\int_{-1}^1d\cos\theta\int_0^{2\pi}d\phi\int_0^\omega d|\vec{n}|\frac{|\vec{n}|^2\hbar\omega_n}{e^{\hbar\omega_n\beta}-1}\\&=4\pi\hbar\frac{L^3}{8\pi^3}\int_0^\omega d\omega^{\prime}\frac{\omega^{\prime3}}{e^{\hbar\omega^{\prime}\beta}-1}.\end{aligned}$$
因此，光的强度作为频率的函数是（对光的两个偏振加上因子2）
$$I(\omega)=\frac{1}{V}\frac{dE(\omega)}{d\omega}=\frac{\hbar}{\pi^2}\frac{\omega^3}{e^{\hbar\omega\beta}-1}$$
这与量子场论有什么关系？为了使这种使用平衡统计力学的推导有意义，<mark style="background: #FFF3A3A6;">光必须能够平衡</mark>。例如，如果我们用单色光加热一个盒子，最终所有的频率都必须被激发。然而，如果不同的频率是不同的粒子，则<mark style="background: #FFF3A3A6;">平衡必须涉及一种粒子转变为另一种粒子</mark>。因此，<mark style="background: #FFF3A3A6;">粒子必须被创造和摧毁</mark>。量子场论告诉我们这是怎么发生的。

