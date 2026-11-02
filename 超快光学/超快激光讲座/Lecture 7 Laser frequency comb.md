
#光学/超快光学 
#光学/超快光学/光学频率梳

# 回顾

- 脉冲测量
- 场自相关 = 光谱测量
- 强度自相关
	- 无背景
	- 干涉型
- 强度与相位测量
	- FROG
	- EO sampling


# 再看频域锁模

谐振腔 ---- 驻波

![[Pasted image 20231119233234.png]]

当有锁模出现后, 产生一串脉冲, 由于非线性, 本来由于色散间隔不均匀的光谱, 此时频域上产生的模式间隔均匀.
 ---- 飞秒激光频率梳



## 时域上图像: 一串相同的脉冲通向频率梳状线

一系列相同脉冲, 间隔相等, 

- 一个脉冲 ---- 频域上脉冲宽度的倒数
- 两个脉冲 ---- 干涉, 产生modulation
- 许多脉冲 ---- 分立谱线 相邻谱线间隔=脉冲重复频率
$$I(\omega)=I_0(\omega)[\frac{\sin(N\omega T_R/2)}{\sin(\omega T_R/2)}]^2$$
![[Pasted image 20231120000730.png]]


脉冲 = 包络 + 载波

包络与载波间出现相移
$$\Delta\phi_{CE}=2\omega_{c}L(\frac{1}{\nu_{g}}-\frac{1}{\nu_{p}})$$

![[Pasted image 20231120000930.png]]

$$\begin{array}{rcl}A(t)&=&\displaystyle\sum_{m=-\infty}^{+\infty}a(T=mT_R,t)e^{j\left[\omega_e\left(t-\frac{1}{v_p}2mL\right)\right]}\\&=&\displaystyle\sum_{m=-\infty}^{+\infty}a(T=mT_R,t)e^{j\left[\omega_e\left(t-mT_R+\left(\frac{1}{v_g}-\frac{1}{v_p}\right)2mL\right)\right]}\end{array}$$
脉冲每在谐振腔中一个往返, 会产生一个相位:
$$\Delta\phi_{CE}=2\omega_{c}L(\frac{1}{\nu_{g}}-\frac{1}{\nu_{p}})$$
脉冲只是包络一样, 实际上载波都存在相位变化.


# 非线性效应对相移产生影响 : 被动锁模

Soliton:
$$a(t,T)=a_s(t)\:e^{-j\phi_0\frac{T}{T_R}}\quad\left\{\quad\begin{aligned}
a_s(t)&=A_0\operatorname{sech}(\frac{t-t_0}{\tau})\\
\phi_0=&\frac{1}{2}\delta A_0^2=\frac{|D|}{\tau^2}:\quad \text{非线性相移}
\end{aligned}\right.$$

脉冲每在谐振腔一个往返就会多产生一个相移.
$$\begin{array}{rcl}\Delta\phi_{CE}&=&\omega_c\left(\dfrac{1}{v_g}-\dfrac{1}{v_p}\right)\bigg|_{\omega_c}2L-\phi_0\\&=&\underbrace{\omega_cT_R\left(1-\dfrac{v_g}{v_p}\right)}_{\text{dispersion}}-\underbrace{\phi_0}_{\text{nonlinearity}}\end{array}$$

# 有载波包络相移的脉冲的光学频率梳

$$A(t)=\sum_{m=-\infty}^{+\infty}a_{s}(t-mT_{R})\:e^{j[\omega_{c}(t-mT_{R})+m\Delta\phi_{CE}]}$$
FT
$$\begin{array}{rcl}\hat A(\omega)&=&\hat a_s(\omega-\omega_c)\sum_{m=-\infty}^{+\infty}e^{j(\Delta\phi_{CE}-\omega T_R)m}\\&=&\hat a_s(\omega-\omega_c)\sum_{m=-\infty}^{+\infty}e^{jmT_R\left(\frac{\Delta\phi_{CE}E}{T_R}-\omega\right)}\\&=&\hat a_s(\omega-\omega_c)\:\frac{2\pi}{T_R}\sum_{n=-\infty}^{+\infty}\delta\left(\omega-\left(\frac{\Delta\phi_{CE}}{T_R}+n\omega_R\right)\right)\end{array}$$
$$\sum_{m=-\infty}^{+\infty}e^{jm2\pi x}=\sum_{n=-\infty}^{+\infty}\delta\left(x-2\pi n\right)$$
comb 产生频移, 每条谱线产生的相位并非整数倍.

![[Pasted image 20231120003444.png]]

载波频移频率
$$f_{CE}=f_{_R}\frac{\Delta\Phi_{CE}}{2\pi}$$

频率梳有两个自由度
$$f_M=Mf_R+f_{CE}$$

![[Pasted image 20231120003702.png]]

- 频率梳有两个自由度
- 锁模激光重复频率决定了频率梳的间隔
- 谐振腔中每个往返的载波频移决定了载波频移

![[Pasted image 20231120004403.png]]

1)每条梳状线都是一个零线宽的无噪声连续激光器。
2)对于脉冲宽度为100 fS、重复频率为100 MHz的锁模激光器，其光谱带宽约为1/(100 FS)=10 THZ，带宽内梳状线数为 (10 THz)/(100 MHz)=100,000。
3)这种频率梳相当于100,000个频率由 $f_M=Mf_R+f_{CE}$ 固定频率的连续激光器。

非线性效应将强度噪声变成相位噪声.

# 现实中, 激光中存在噪声

![[Pasted image 20231120004807.png]]

统计学手段描述噪声?

平均值

方差

自相关函数

频谱

功率谱

![[Pasted image 20231120005233.png]]


噪声来源:
- 技术噪声
	- 泵浦功率
	- 振动
- 量子噪声
	- 放大的自发辐射

描述噪声的模型

![[Pasted image 20231120010120.png]]

脉冲动力学方程
$$T_{R}\frac{\partial u(t,T)}{\partial T}\:=\:\left\{-l+g\left(1+\frac{1}{\Omega_{g}^{2}}\frac{\partial^{2}}{\partial t^{2}}\right)+\frac{1}{\Omega_{f}^{2}}\frac{\partial^{2}}{\partial t^{2}}+jD\frac{\partial^{2}}{\partial t^{2}}\:\frac{M_{AM}+jM_{PM}}{4}(\omega_{M}t)^{2}+(\gamma-j\delta)|a(t,T)|^{2}\right\}a(t,T)+T_{R}S(t,T).$$

T：短期变量T：多腔往返时间尺度上的时间变量。

1.找到描述激光腔的正确主方程。
2.在没有噪声的情况下求主方程的解
3.在试解中加入噪声项作为扰动；
4.推导出不同噪声波动的方程：幅度、定时、频率、相位等。
5.计算不同噪声波动的功率谱密度和相关性。

解
$$a_s(t,T)\to a_s(t,T)+\Delta A(t,T)$$
噪声修正
$$\Delta A(t,T)=\Delta E_p(T)f_{E_p}(t)+\Delta\varphi(T)f_\varphi(t)+\Delta f_c(T)f_{f_c}(t)+\Delta t(T)f_t(t)+a_{c}(T,t)$$
- 能量
- 高阶相位
- 中心频率
- 时间抖动
- 连续背景

![[Pasted image 20231120010528.png]]

几种改变相互耦合.

如何产生更少的噪声?

- 低损耗 ---- 少的增益 ---- 少的量子噪声
- 降低色散 ---- 中心波长改变更小
- 功率高, 脉冲强
- 脉冲窄
- 腔长长, 重复频率低, 每次经过增益介质所需距离或时间少.

$f_R$ ---- RF specture analyzer

如何测量 $f_{CE}$ ?

1f-2f Interferometer

倍频层

![[Pasted image 20231120011457.png]]

如何获得这么宽的光谱?  ---- Kerr 效应

![[Pasted image 20231120012551.png]]

应用:

频率是可以精准测量的物理量.

物理量 --?-- 频率

精确测量光学频率 ---- 拍频

![[Pasted image 20231120013852.png]]

$$f_{unknown}=f_{known}+M\times f_{R}\pm f_{beat,1}\pm f_{beat,2}$$

- 光钟

![[Pasted image 20231120014339.png]]

![[Pasted image 20231120014529.png]]


低噪声微波信号

![[Pasted image 20231120014612.png]]

$$f_R=\frac{f_M-f_{CE}}{M}$$

## 任意波形发生器

![[Pasted image 20231120014912.png]]





![[Pasted image 20231120015141.png]]







