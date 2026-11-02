
#光学/光子晶体 

# The Macroscopic Maxwell Equations

Maxwell Equations
$$\begin{aligned}
\nabla\cdot\mathbf{B} & = 0,\quad\nabla\times\mathbf{E}+\frac{\partial\mathbf{B}}{\partial t} = 0,\\\nabla\cdot\mathbf{D} &= \rho,\quad\nabla\times\mathbf{H}-\frac{\partial\mathbf{D}}{\partial t} = \mathbf{J}.
\end{aligned}$$
在混合介电介质内的传播, 设$\rho=0,\quad\mathbf{J}=0$

## ELECTROMAGNETISM IN MIXED DIELECTRIC MEDIA

![[Pasted image 20241221183134.png]]
将电场展宽 
$$D_{i}/\varepsilon_{0}=\sum_{j}\varepsilon_{ij}E_{j}+\sum_{j,k}\chi_{ijk}E_{j}E_{k}+O(E^{3}),$$
我们引入假设
- 电场足够小, 只需考虑线性项;
- 材料各向同性
- 忽略材料色散
- 关注透明材料, 只考虑介电常数的实部

于是我们有
$$\mathbf{D}(\mathbf{r})=\varepsilon_0\varepsilon(\mathbf{r})\mathbf{E}(\mathbf{r}),\quad \mathbf{B}(\mathbf{r})=\mu_0\mu(\mathbf{r})\mathbf{H}(\mathbf{r})$$
麦克斯韦方程组化为
$$\begin{aligned}
\nabla\cdot\mathbf{H}(\mathbf{r},t) & = 0,\quad &\nabla\times\mathbf{E}(\mathbf{r},t)+\mu_0\frac{\partial\mathbf{H}(\mathbf{r},t)}{\partial t} = 0\\
\nabla\cdot[\varepsilon(\mathbf{r})\mathbf{E}(\mathbf{r},t)] & = 0,\quad &\nabla\times\mathbf{H}(\mathbf{r},t)-\varepsilon_0\varepsilon(\mathbf{r})\frac{\partial\mathbf{E}(\mathbf{r},t)}{\partial t} = 0.
\end{aligned}\tag{3}$$
## ELECTROMAGNETISM IN MIXED DIELECTRIC MEDIA

由于麦克斯韦方程是线性的，我们可以通过将场扩展为一组谐波模式来将时间依赖性与空间依赖性分开.
$$\begin{aligned}&\mathbf{H}(\mathbf{r},t)=\mathbf{H}(\mathbf{r})e^{-i\omega t}\\&\mathbf{E}(\mathbf{r},t)=\mathbf{E}(\mathbf{r})e^{-i\omega t}.\end{aligned} \tag{4}$$
代入(3)中的散度方程:
$$\nabla\cdot\mathbf{H}(\mathbf{r})=0,\quad\nabla\cdot[\varepsilon(\mathbf{r})\mathbf{E}(\mathbf{r})]=0,\tag{5}$$
- 介质中不存在电场的点源或磁场的位移汇;
- 同样，场结构是由横向电磁波组成的。
亦即，如果有一个平面波 $H(r) =\bf{a} \exp(i\bf{k}\cdot \bf{r})$, 对于某波矢 k, 方程（5）要求 $\bf{a}·\bf{k}=0$.

旋度方程:
$$\begin{align}
\nabla\times\mathbf{E}(\mathbf{r})-i\omega\mu_0\mathbf{H}(\mathbf{r}) & = 0\\\nabla\times\mathbf{H}(\mathbf{r})+i\omega\varepsilon_0\varepsilon(\mathbf{r})\mathbf{E}(\mathbf{r}) & = 0.
\end{align}\tag{6}$$
旋度的旋度, 解耦:
$$\boxed{\nabla\times\left(\frac1{\varepsilon(\mathbf{r})}\nabla\times\mathbf{H}(\mathbf{r})\right)=\left(\frac\omega c\right)^2\mathbf{H}(\mathbf{r}).}\tag{7}$$
其中, 光速 $c=1/\sqrt{\varepsilon_0\mu_0}$.

电场
$$\mathbf{E}(\mathbf{r})=\frac i{\omega\varepsilon_0\varepsilon(\mathbf{r})}\nabla\times\mathbf{H}(\mathbf{r}).\tag{8}$$
## Electromagnetism as an Eigenvalue Problem

上一节中我们得到了一个特征值问题.
$$\hat{\Theta}\mathbf{H}(\mathbf{r})=\left(\frac\omega c\right)^2\mathbf{H}(\mathbf{r}).\tag{10}$$
其中, 
$$\hat{\Theta}\mathbf{H}(\mathbf{r})\triangleq\nabla\times\left(\frac1{\varepsilon(\mathbf{r})}\nabla\times\mathbf{H}(\mathbf{r})\right)\tag{11}$$
注意, $\hat{\Theta}$ 是线性算符.

可类比量子力学中的哈密顿量本征值问题.
- 正交;
- 可以通过变分原理获得;
- 可通过对称性分类;
- 主算符为厄米算符.

厄米算符

两个向量场 $\bf{F(r)}$ 和 $\bf{G(r)}$ 的内积
$$(\mathbf{F},\mathbf{G})\triangleq\int d^3\mathbf{r}\mathbf{F}^*(\mathbf{r})\cdot\mathbf{G}(\mathbf{r}),$$
其中, "\*" 表示复共轭。
厄米算符 $\hat{\Xi}$ 满足:
$$(\mathbf{F},\hat{\Xi}\mathbf{G})=(\hat{\Xi}\mathbf{F},\mathbf{G})$$

## General Properties of the Harmonic Modes

- 特征值一定为实数
$$\begin{align}
\hat{\Theta}\mathbf{H}(\mathbf{r}) & = (\omega^2/c^2)\mathbf{H}(\mathbf{r})\\\Longrightarrow(\mathbf{H},\hat{\Theta}\mathbf{H}) & = (\omega^2/c^2)(\mathbf{H},\mathbf{H})\\\Longrightarrow(\mathbf{H},\hat{\Theta}\mathbf{H})^* & = (\omega^2/c^2)^*(\mathbf{H},\mathbf{H}).
\end{align}$$
厄米算符: $(\mathbf{H},\hat{\Theta}\mathbf{H})=(\hat{\Theta}\mathbf{H},\mathbf{H})$
由内积定义: $(\mathbf{H},\hat{\Xi}\mathbf{H})=(\hat{\Xi}\mathbf{H},\mathbf{H})^*$
所以,
$$\begin{aligned}(\mathbf{H},\hat{\Theta}\mathbf{H})^*=(\omega^2/c^2)^*(\mathbf{H},\mathbf{H})&=(\hat{\Theta}\mathbf{H},\mathbf{H})=(\omega^2/c^2)(\mathbf{H},\mathbf{H})\\&\implies(\omega^2/c^2)^*=(\omega^2/c^2).\end{aligned}$$
于是, $\omega^2=(\omega^2)^*$, $\omega^2$ 为实数. 

- 当 $ε >0$ 时 $ω^2$ 总是非负的. 

设 $\bf{F}=\bf{G}=\bf{H}$
$$(\mathbf{H},\mathbf{H})\left(\frac\omega c\right)^2=(\mathbf{H},\hat{\Theta}\mathbf{H})=\int d^3\mathbf{r}\frac1\varepsilon|\nabla\times\mathbf{H}|^2.\tag{17}$$
由于 $ε(r)$ 处处 > 0，因此右侧的被积函数处处非负。算子 $\hat{\Theta}$ 被认为是半正定的。因此，所有特征值 $ω^2$ 都是非负的，并且 $ω$ 是实数。

- $\hat{\Theta}$ 的厄米性迫使不同频率 $ω_1$ 和 $ω_2$ 的任意两个谐波模式 $\bf{H}_1(\bf{r})$ 和 $\bf{H}_2(\bf{r})$ 具有零内积。

说明: 如果两个谐波模式具有相等的频率 $ω_1=ω_2$，称它们是简并的，并且它们不一定是正交的。
- 要使两种模式简并，从表面上看似乎是惊人的巧合：两种不同的场模式恰好具有完全相同的频率。
- <mark style="background: #FFF3A3A6;">通常是一种对称性导致了这种 "巧合"</mark>. 例如, 如果介电结构在 120° 旋转下保持不变，则仅 120° 旋转不同的模式预计将具有相同的频率。

# Electromagnetic Energy and the Variational Principle

尽管介电介质中的谐波模式可能非常复杂, 但有一种简单的方法可以理解它们的一些定性特征: <mark style="background: #FFF3A3A6;">电磁场的模式倾向于将其电场能量集中在高介电常数区域中, 同时保持正交于频率更低模式</mark>. 

这个有用但有些模糊的概念可以通过电磁变分定理精确地表达, 该定理类似于量子力学的变分原理. 具体地, 最小特征值 $ω_0^2/c^2$ 以及相应最低频率模式应当对应于一个电磁场模式能够最小化如下泛函: 
$$U_f(\mathbf{H})\triangleq\frac{(\mathbf{H},\hat{\Theta}\mathbf{H})}{(\mathbf{H},\mathbf{H})}.\tag{20}$$
也就是说, $ω_0^2/c^2$ 是所有场模式 $\bf{H}$ 上 $U_f(\bf{H})$ 的最小值（受横向约束 $∇·\bf{H} = 0$）. 

- 泛函 $U_f$ 有时称为<mark style="background: #FF5582A6;">瑞利商</mark>，并且出现在任何厄米算子的类似变分定理中。
- 我们将 $U_f$ 称为电磁“能量”泛函，以强调与量子力学和经典力学中最小化物理能量的类似变分定理的类比。
- 量子力学中, 瑞利商指某个观察矩阵的期望值, 对于上述电磁场系统代表哈密顿量的期望值最小, 因此上述表述实际上就是最小作用量原理?

为验证最低频率模式下 $U_f$ 最小化的说法，我们考虑 $\bf{H}(r)$ 的微小变化如何影响能量泛函。

假设我们通过添加微扰函数 $δ\bf{H}(r)$ 来扰动场 $\bf{H}(r)$。能量泛函中产生的微扰变化 $δU_f$ 是多少？

如果能量泛函确实处于最小值，则它应该为零，就像函数的普通导数在极值处消失一样。为了找到答案，我们评估 $\bf{H}(r) + δ\bf{H}(r)$ 和 $\bf{H}(r)$ 处的能量泛函，然后计算差值 $δU_f$ ：
$$\begin{aligned}U_f(\mathbf{H}+\delta\mathbf{H})&=\frac{(\mathbf{H}+\delta\mathbf{H},\hat{\Theta}\mathbf{H}+\hat{\Theta}\delta\mathbf{H})}{(\mathbf{H}+\delta\mathbf{H},\mathbf{H}+\delta\mathbf{H})}\\
U_f(\mathbf{H})&=\frac{(\mathbf{H},\hat{\Theta}\mathbf{H})}{(\mathbf{H},\mathbf{H})}\\
\delta U_f(\mathbf{H})&\triangleq U_f(\mathbf{H}+\delta\mathbf{H})-U_f(\mathbf{H})\end{aligned}\tag{21}$$


忽略 $δ\bf{H}$ 中高于一阶的项，我们可以将 $δU_f$ 写成
$$δU_f \approx [(δH, G) + (G, δH)]/2$$
其中, 
$$\mathbf{G}(\mathbf{H})=\frac2{(\mathbf{H},\mathbf{H})}\left(\hat{\Theta}\mathbf{H}-\left[\frac{(\mathbf{H},\hat{\Theta}\mathbf{H})}{(\mathbf{H},\mathbf{H})}\right]\mathbf{H}\right)\tag{22}$$
该 $\bf{G}$ 可以解释为函数 $U_f$ 相对于 $\bf{H}$ 的梯度. 

在极值处，对于所有可能的变化 $δ\bf{H}$，$δU_f$ 必须消失，这意味着 $G = 0$。这意味着 (22) 中括号中的量为零，相当于说 $\bf{H}$ 是 $\hat{\Theta}$ 的特征向量。因此，当且仅当 $\bf{H}$ 是谐波模式时，$U_f$ 才处于极值。更仔细的考虑表明，最低 $ω$ 电磁本征模 $\bf{H}_0$ 使 $U_f$ 最小化。次低 $ω$ 本征模将最小化与 H0 正交的函数子空间内的 Uf，依此类推。

