
#光学/超快光学

# 回顾

- 两能级系统动力学方程
- 三能级系统
- 四能级系统


- 激光操作的一般描述


- 锁模 
	- 频域 vs 时域, 
	- 主动锁模 vs 被动锁模


- Master equation


# 超快激光 ---- 第四个要素: 锁模器


![[Pasted image 20231115170348.png]]

![[Pasted image 20231115171014.png]]

一些描写激光脉冲的参数:
- 脉冲持续时间 T (fs-ps)


- 脉冲能量 E (pJ-J)


- 峰值功率 $P_P$ (1 kW-10 kW)
$$P_P\approx \frac{E}{T}$$
e.g. 1nJ, 100fs 的脉冲可以产生10kW 的峰值功率.


- (峰值) 光强 I
$$I=\frac{P}{S_{\text{beam area}}}$$
e.g. 如果一个具有1pW 峰值功率的光斑被聚焦在 $1\mu m^2$ 的区域内, 峰值光强为 $10^{23}W/cm^2$ .


- 重复率
$$f_R=\frac{1}{T_R}$$
1kHz-10GHz

- 平均功率 P
$$P=Ef_R$$
e.g. 峰值功率为1nJ, 重复频率为100 MHz的激光产生100 mW的平均功率.


- 中心波长 $\lambda_0$
700-3000nm


# 激光质量的度量


|   |   |
|---|---|
|Physical quantity|Measuring device|
|Average power|Power meter|
|Repetition rate|RF spectrum analyzer|
|Optical spectrum|Optical spectrum analyzer (OSA)|
|Optical pulse|Pulse meter (?)|

![[Pasted image 20231115172726.png]]

![[Pasted image 20231115172739.png]]


# 我们需要什么信息才能完整的表征一个脉冲?

一个激光脉冲具有时域上的电场
$$\mathrm{E}(t)\sim\mathrm{Re}\{\color{red}{\underbrace{I(t)}_{\text{Intensity}}\color{black}^{1/2}\exp[j\omega_0t-j\color{blue}\underbrace{\phi(t)}_{\text{Phase}}\color{black}]}\color{black}\}$$

等价的, 频域上
$$\color{black}\widetilde{\mathsf{E}}(\omega)\thicksim\color{red}\underbrace{{\mathsf{I}}(\omega-\omega_0)}_{\text{Spectrum}}\color{black}^{1/2}\exp{[-j\color{blue}\underbrace{\varphi(\omega-\omega_0)}_{\text{Spectrum Phase}}\color{black}]}$$
其中, 我们忽略了负频率的成分.

我们可以用一个光谱仪测量一个脉冲.

# 频域上光谱测量

![[Pasted image 20231115174412.png]]

光谱仪原理图如下:

![[Pasted image 20231115174403.png]]

- 光纤出射后通过一个凹面镜反射为一束平行光;
- 然后被衍射器件 (一般是光栅) 分光, 不同频率成分以不同的角度出射;
- 从焦面上不同角度出射 (不同频率) 的光被另一个凹面镜聚焦在焦面上的不同位置, 最后光线要通过一个狭缝将这些不同频率的光选择出来;
- 通过分光仪器的转动可以控制不同的频率成分的光通过狭缝并被探测器检测.
- 不同的光栅转动角度标定到光的频率, 具体如何???

Note: 
- 这种测量方法无法测量相位信息.
- 但是这种测量方法可以计算得到变换极限脉冲, 但无法知道真正的脉冲的形状.


# 时域上脉冲测量, 光探测器

光探测器可以响应光子发射电子.

![[Pasted image 20231115180825.png]]

Example: 光电探测器, 光电倍增管

问题: 响应很慢 ~1 ns

光电探测器的反应非常慢, 因此它们只能测量脉冲强度的时间积分：
$$V_{{\text{detector}}}\propto \int_{-\infty}^{\infty}|E(t|^2dt$$
探测器输出电压与脉冲能量成正比.

问题: 超短脉冲的上升沿下降沿至少都在 ns 量级, 光探测器本身不能告诉我们脉冲的信息.

![[Pasted image 20231115181017.png]]









