---
日期: 2026-01-26
时间: 2026-01-26T11:42:44
---
激光的线性传输


 #光学/超快光学 


# 激光产生

激光三要素:
- 增益介质 Gain medium
	- enable stimulated emission to produce identical copies of photons
	- determin the light wavelength
- 泵浦 Pump
	- inject power into the gain medium
	- achieve population inversion
- 谐振腔 Resonator cavity
	- make light wave oscillating to efficiently extract stored in the gain medium
	- Improve directionally and color purity of the light

连续激光: 
- 功率随时间不变
- 非常窄的谱线, 良好的单色性

超快激光, 引入第四个元素, 锁模器, 产生序列脉冲
- 脉冲具有光谱宽度

![[Pasted image 20231103154720.png]]

脉冲间隔 $T_R$ , 脉冲在谐振腔中走一个来回所需时间
脉冲宽度 $T$ , 半高全宽?
![[Pasted image 20231103154759.png]]

时间宽度与频谱宽度之间由傅里叶变换联系, 二者类似于测不准原理, 一个越短另一个则越宽.

![[Pasted image 20231103155329.png]]

用越丰富的颜色能得到越来越窄的脉冲.

为什么白炽灯具有非常丰富的频率成分但却没有很短的脉冲?
需要相位关系. 因此需要锁模技术.

# 描述激光的一些参数

- 脉冲宽度(半高全宽) T (fs-ps)

- 脉冲的能量 pulse energy (脉冲的面积)E (pJ-J)

- 脉冲的幅度 peak power  (峰值功率) $P_P\approx E/T$ (1kW-10PW)

激光能被聚焦到非常小的光斑 : 衍射极限, 约为波长的尺度.
- <mark style="background: #FF5582A6;">光强</mark> peak intensity $I=P_P/( S_{\text{光斑面积}})$
光强越来越强, 便能研究光与物质的非线性相互作用.

- <mark style="background: #FF5582A6;">重复频率</mark> repetition rate $f_R=1/T_R$ (1kHz-10GHz)
脉冲序列的频率

- <mark style="background: #FF5582A6;">平均功率</mark> average power $P$ (10mW-1kW)
$$P=E\times f_R$$

- <mark style="background: #FF5582A6;">中心波长</mark> center wavelength $\lambda _0$ (700-3000nm)
	- 由增益介质所决定. 
	- 常见在近红外波段
	- 通过选择合适增益介质向更长的波段推进, 短红外中红外波段 (2um-3um)

# 超短脉冲应用

## "快门"

研究短的物理过程, 我们需要更短的事件来研究. 飞秒脉冲: 人为制造的非常短的事件, 要研究更短的事件就要制作更短的脉冲. 越小的尺度发生的事情, 对应的速度就越快.

![[Pasted image 20231103161347.png]]

改变两个脉冲之间的延迟(相位差), 从而可以研究各种过程.


## 时间同步

飞秒脉冲时间上严格地重复自己. 可以控制相邻脉冲间的间隔控制保持不变, 从而使得大装置上实现时间同步.


## 光学频率梳

对脉冲序列作 FT, 在频域上也是对应间隔严格相同的谱线, 像一把梳子. 每个梳齿对应一个频率, 于是可用于做非常精确的频率测量.

## 高光强: 非线性相互作用, 飞秒脉冲激光加工

![[Pasted image 20231103162324.png]]

- 脉冲越短, 加工效果更好. 可实现高精度加工.
- 光镊, 慢光
- 从狄拉克海中激发正负电子对, 能量不确定关系


钛宝石激光器

![[Pasted image 20231103163340.png]]

脉冲实际上包含了: 包络以及包络中快速振荡的载波:

![[Pasted image 20231103163431.png]]

一个脉冲实际上可以具有任意形状. 数学上, 一个脉冲由下面式子描述:
$${E(t) \propto \frac{1}{2} \sqrt{I(t)} \exp \left\{j\left[\omega_{0} t-\varphi(t)\right]\right\}+c . c}$$
- 强度
- 载波
- 相位

多数时候我们不关心快速变化的载波的中心频率, 只关心包络的情况
$$E(t)\propto \sqrt{I(t)}exp[-j\phi(t)]$$

高斯脉冲
$$\begin{align}
E(t)&=E_{0}exp[-(t/\tau_{HW1/e})^{2}]\\
&=E_0exp[-2\ln 2(t/\tau_{FWHM})^2]
\end{align}$$
- $\tau_{FWHM}$ : 半高全宽

傅立叶变换
$$\begin{align}
{\tilde{E}(\omega)=\int_{-\infty}^{\infty} E(t) e^{-j \omega t} d t}\\
{E(t)=\frac{1}{2 \pi} \int_{-\infty}^{\infty} \tilde{E}(\omega) e^{j \omega t} d \omega}
\end{align}$$

上面作 FT
$${\tilde{E}(\omega)=\frac{1}{2} \sqrt{S\left(\omega-\omega_{0}\right)} \exp \left\{-j\left[\phi\left(\omega-\omega_{0}\right)\right]\right\}+\frac{1}{2} \sqrt{S\left(-\omega-\omega_{0}\right)} \exp \left\{+j\left[\phi\left(-\omega-\omega_{0}\right)\right]\right\}}$$
- FT后, 频率上的0是相对于中心频率而言的
- 时域与频域上都具有一个相位
- 高斯脉冲变换后还是高斯型

常用的一些脉冲形状

![[Pasted image 20231103165246.png]]

- 高斯型和双曲正割型比较常见
- 光孤子往往对应双曲正割型
- 锁模后产生一个脉冲, 脉冲形状一般由锁模的机制决定.

时间带宽积有最小值.


# 麦克斯韦方程与波动方程

Maxwel eqs

.......

波动方程
$${\left(\nabla^{2}-\frac{1}{c_{0}^{2}} \frac{\partial^{2}}{\partial t^{2}}\right) E=\mu_{0} \frac{\partial^{2} P}{\partial t^{2}}}$$
- 电极化P 中包含了光与物质相互作用的信息.

真空中光速
$$c_0=\sqrt{\frac{1}{\mu_0\epsilon_0}}$$

无磁性材料物质方程:
$$\mathbf{P}=\epsilon _0\chi\mathbf{E}$$
$$ \epsilon =\epsilon _{0}(1+\chi)$$
$$\mu=\mu _0$$
材料的折射率
$$n=\sqrt{\frac{\epsilon \mu}{\epsilon _{0}\mu_{0}}}=\sqrt{1+\chi}$$
我们可以直接用折射率描述光对物质的响应.

## 洛伦兹模型

洛伦兹模型: 简谐振子
$${m \frac{d^{2} x}{d t^{2}}+2 m \gamma \frac{d x}{d t}+m \omega_{0}^{2} x=-e E(t)}$$
$${E(t)=\mathrm{E} e^{j \omega t} \Rightarrow x(t)=x e^{j \omega t} \Rightarrow p(t)=-e x(t)=\mathrm{p} e^{j \omega t}}$$
 最后有色散关系:
$$
\begin{align}
{\mathrm{p}=\frac{e^{2} / m}{\omega_{0}^{2}-\omega^{2}+2 j \omega \gamma} \mathrm{E}}\\
{\chi(\omega)=\frac{N e^{2} /\left(m \varepsilon_{0}\right)}{\omega_{0}^{2}-\omega^{2}+2 j \omega \gamma}}
\end{align}
$$

出射光应当是受迫振荡的光与入射光之间的叠加, 应当考虑二者的干涉情形:
- 相位同步---光放大---激光
- 差了π/2个相位---吸收
- 既不放大也不吸收, π/2的相移

多数情况, 入射光频率应远离吸收峰(本征频率), $|\omega _{0}^{2}-\omega ^{2}|>>2\omega \gamma$
$${\chi(\omega)=\frac{\omega_{p}^{2}}{\left(\omega_{0}^{2}-\omega^{2}\right)},\quad   \omega_{p}^{2}=N e^{2} /\left(m \varepsilon_{0}\right)}$$
假设有多个本征频率, 可简单的作线性叠加:
$${n^{2}(\omega)=1+\chi(\omega)=1+\sum_{i} A_{i} \frac{\omega_{p}^{2}}{\omega_{i}^{2}-\omega^{2}}=1+\sum_{i} a_{i} \frac{\lambda^{2}}{\lambda^{2}-\lambda_{i}^{2}}}$$
实际中, 多数材料实验上满足上面方程, 表现为具有不同的系数与本征频率组成.
- 背后的实质就是洛伦兹模型.
- 描述光在物质中线性传输时所发生的事情
	- 色散
	- 脉冲增宽


























