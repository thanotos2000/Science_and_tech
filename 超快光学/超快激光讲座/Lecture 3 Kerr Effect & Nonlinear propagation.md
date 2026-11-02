
#光学/超快光学
#光学/非线性光学

# 回顾

- Phase velocity, group velocity, 
- group-velocity dispersion (GVD), group delay, group-delay dispersion (GDD), 
- third-order dispersion (TOD)

- Instantaneous frequency, chirp

- Dispersive optical devices: 
	- prism pair, 
	- grating pair, 
	- chirped mirror, 
	- chirped fiber Bragg grating (CFBG), 
	- chirped volume Bragg grating (CVBG), 
	- spatial light modulator, 
	- Acousto-Optic Programmable Dispersive Filter (AOPDF, also known as Dazzler)

波数:
$$\begin{aligned}k(\omega)&=n(\omega)\frac{\omega}{c}=k_0+k_1(\omega-\omega_0)+\frac{1}{2}k_2(\omega-\omega_0)^2+\ldots\end{aligned},\quad k_m=\left(\frac{d^mk}{d\omega^m}\right)_{\omega=\omega_0}$$

群速度:
$$k_1=\frac1{V_g}=\frac1c(n+\omega\frac{dn}{d\omega})=\frac1c(n-\lambda\frac{dn}{d\lambda})\quad\quad\quad\text{Unit: s/m}$$

$$k_2=\frac d{d\omega}(\frac1{V_g})=-\frac1{{V_g}^2(\omega_0)}\frac{dV_g}{d\omega}=\frac1c(2\frac{dn}{d\omega}+\omega\frac{d^2n}{d\omega^2})=(\frac\lambda{2\pi c})\frac{\lambda^2}c\frac{d^2n}{d\lambda^2}$$
Note: more often, $β(ω)$, is used to replace k(ω) and $β_2$ is GVD.

![[Pasted image 20231106151736.png]]

![[Pasted image 20231106151642.png]]

群延迟
$$\phi(\omega)=k(\omega)z=\phi_0+\phi_1(\omega-\omega_0)+\frac12\phi_2(\omega-\omega_0)^2+\frac16\phi_3(\omega-\omega_0)^3+\ldots\quad\phi_m=\left(\frac{d^m\phi}{d\omega^m}\right)_{\omega=\omega_0}$$
- 群延迟: $\phi_{1}=\dfrac{z}{V_g}=\tau$ 
- 群延迟色散 GDD:  $\phi_2=\dfrac{d\tau_{g}}{d\omega }$ 
	- GDD>0 正色散
	- GDD<0 负色散
- $\phi_3$ TOD
- $\phi_4$ FOD

# 从波动方程开始

## 时域上描述

![[Pasted image 20231106153232.png]]

![[Pasted image 20231106153239.png]]

正群速度色散

![[媒体1.gif]]

负群速度色散

![[媒体2.gif]]

## 线性系统

![[Pasted image 20231106154623.png]]

## 非线性光学---在极化中引入高阶项

$$P=\varepsilon_0[\chi^{(1)}E+\chi^{(2)}E^2+\chi^{(3)}E^3+...]$$

![[Pasted image 20231106154710.png]]

这里我们只考虑
$$P\:=\:\varepsilon_0\left[\chi^{(1)}E\:+\:\chi^{(3)}|E|^2E\right]\:=\:\varepsilon_0\:\left[\chi^{(1)}\:+\:\chi^{(3)}|E|^2\right]E$$
带回波动方程
$$\frac{\partial^2E}{\partial z^2}~-~\frac{1}{c_0^2}~\frac{\partial^2E}{\partial t^2}~=~\mu_0\varepsilon_0[\chi^{(1)}~+~\chi^{(3)}~|E|^2]~\frac{\partial^2E}{\partial t^2}$$
$$\frac{\partial^2E}{\partial z^2}\:-\:\frac{\left[1+\chi^{(1)}\:+\:\chi^{(3)}\:|E|^2\right]}{c_0^2}\:\frac{\partial^2E}{\partial t^2}\:=\:0$$
# 折射率 --- Kerr Effect

## Kerr Effect
$$n\:=\:\sqrt{1+\chi^{(1)}+\:\chi^{(3)}\left|E\right|^2}$$
折射率是
$$n~\approx~n_0[1+~\chi^{(3)}|E|^2/2n_0^2]\longrightarrow n~\approx~n_0+~\chi^{(3)}|E|^2/2n_0=n_0+n_2I$$
其中, $n_0=\sqrt{1+\chi^{(1)}}$ 为一般线性情形下的折射率.

- 当脉冲很小, 则可以忽略非线性效应. 但脉冲很强时不能忽略, 折射率和光强成正比 --- Kerr Effect.
$$n=n_0+n_2I$$

|   |   |   |
|---|---|---|
|Material|Refractive index n|n_2 [[cm]^2/W]|
|Sapphire (Al2O3)|1.76 @ 850 nm|3∙10^(-16)|
|Fused Quarz|1.45 @ 1064 nm|2.46∙10^(-16)|
|Glass (LG-760)|1.5 @ 1064 nm|2.9∙10^(-16)|
|YAG (Y3Al5O12)|1.82 @ 1064 nm|6.2∙10^(-16)|
|YLF (LiYF4), ne|1.47 @ 1047 nm|1.72∙10^(-16)|
|Si|3.3 @ 1550 nm|4∙10^(-14)|

## 自聚焦

![[Pasted image 20231106160255.png]]

高斯光束,  光强中间强, 两边弱, 发生克尔效应, 中心部分的折射率大, 边缘的折射率小. 光束在其中传输时, 中心部分的传输慢, 就像一个透镜.

光强越高, 聚焦越明显, 聚焦越明显, 光束强度随之增加从而聚焦能力更加显著, 就像一个雪崩现象, 使得聚焦的现象越来越快. 就像图中由红颜色逐渐变为绿色最后到蓝色线条一样.

自聚焦的阈值:
$$P_{cr}=\frac{\pi(0.61)^2\lambda_0^2}{8n_0n_2}$$

波长越长, 材料 $n_0$ 和 $n_2$ 折射率越小, 自聚焦阈值越大.

对熔融石英而言, 
$$\begin{aligned}\lambda_0&=1.03\mu m\:n_0=1.45\\n_2&=2.7\times10^{-20}m^2/W\end{aligned}\quad\longrightarrow\quad P_{cr}=4MW$$

做光放大的时候, 能量不能超过自聚焦阈值, 否则自聚焦现象会产生雪崩, 最后损害仪器.

光斑更大并不能避免自聚焦, 只会延缓自聚焦的发生.

解决方法: 啁啾脉冲放大.

## Kerr 效应对脉冲的影响 ---- 自相位调制 (Self-Phase Modulation)

传输方程:
$$\frac{\partial A(z,t)}{\partial z}=-jk_0n_2|A|^2A=-j\delta|A|^2A\quad\quad\delta=k_0\:n_2$$
解:
$$\begin{array}{rl}A(z,t)=A(0,t)e^{j\phi_{NL}}&=A(0,t)e^{-j\delta|A(z,t)|^{2}z}\end{array}$$
- 输入输出脉冲形状上没有变化
- 只是在时间上获得了一个的相位, 来自强度很高下的 Kerr Effect (非线性效应).
- 相位与脉冲自己的强度成正比 ---- <mark style="background: #FF5582A6;">自相位调制</mark>
$$\begin{aligned}|A(z,t)|&=|A(0,t)|\\\phi_{NL}&=-\delta|A(z,t)|^2z\end{aligned}$$

![[Pasted image 20231106232922.png]]

- <mark style="background: #FFF3A3A6;">在脉冲中心附近产生一个正啁啾, 其他地方产生负啁啾</mark>
$$\Delta\omega=\frac{d\phi_{NL}}{dt}=-\delta z\frac{d|A(z,t)|^2}{dt}$$

自相位调制不改变脉冲的形状, 但会改变脉冲的光谱:

![[Pasted image 20231106233255.png]]

![[媒体3.gif]]

- 光谱越来越宽, 出现越来越多的旁瓣
- 旁瓣的数量与非线性相移有定量关系
$$\varphi_{NL}\approx(M-\frac12)\times\pi $$
光谱上的极值点恰好对应时域上最外侧的的旁瓣, 可用滤波将其提取出来.
 
对比脉冲色散&自相位调制

色散:
$$j\frac{\partial A(z,t)}{\partial z}=-\frac{\beta_2}2\frac{\partial^2A}{\partial t^2}$$
- 脉冲频域上获得相位
- 频谱不会改变
- 时域上, 脉冲被拉长或压缩 (正色散或负色散) , 取决于初始的啁啾

自相位调制
$$j\frac{\partial A(z,t)}{\partial z}=\delta|A|^2A$$
- 时域上获得相位
- 脉冲形状不变
- 频域上光谱变宽或变窄, 取决于初始啁啾.

Q: 变窄?

二者就像在一个在时域上一个在频域上, 相互对偶的操作. 

# 既有色散又有非线性效应 ---- 非线性薛定谔方程 (NLSE)

## NLSE 的讨论, 孤子的概念

$$j\frac{\partial A(z,t)}{\partial z}=-\frac{\beta_2}2\frac{\partial^2A}{\partial t^2}+\delta|A|^2A$$
- $\delta|A|^2A$ : 非线性项

NLSE 分为两种情形:
- positive GVD + SPM
正色散让脉冲正啁啾, 自相位调制也让脉冲产生正啁啾, 因此<mark style="background: #FFF3A3A6;">脉冲的传播越来越快</mark>.


- Negative GVD + SPM
负色散让脉冲产生负啁啾, 自相位调制让脉冲产生正啁啾, 二者可以达到平衡, 使得脉冲处于没有啁啾的状态 ---- 变换极限状态. 虽然脉冲传输中又有非线性又有色散, 但脉冲一直不变. 
<p align="right">---- <mark style="background: #FF5582A6;">光孤子</mark>解 (Soliton) </p>

#光学/非线性光学/光孤子

Soliton (孤子) : 对应某一类非线性偏微分方程, 最早在水波中观察到.

- 两个孤子相互靠近，它们逐渐碰撞并合并为一个波包。
- 这个波包在“碰撞”之后, 又很快分裂成两个形状和速度相同的孤子。
- 非线性薛定谔方程可预言光孤子的存在.


## 光纤概述

![[Pasted image 20231107171809.png]]

光纤结构
- 高折射率芯层
- 低折射率包层

光纤色散:
- 来自材料本身的色散 ---- 熔融石英的色散
- 光纤的几何结构 ---- 波导色散 waveguide dispersion
入射的角度不同, 使得入射的光波感受的限制不同, 光波有不同的色散. 

![[Pasted image 20231107172231.png]]

可通过改变光纤几何结构灵活地改变光纤的色散.

光纤中的Kerr effect
$$n(I)=n+n_2I$$

非线性相移
$$\phi_{NL}=\frac{2\pi}{\lambda }N_{2}iz=\frac{2\pi}{\lambda }n_{2}\frac{P}{A_eff}z=\gamma Pz$$

非线性参数
$$\gamma=\frac{2\pi}{\lambda}\frac{n_{2}}{A_{eff}}$$
$\gamma$ 表征了光纤的非线性大小. 

- 材料的 $n_{2}$, 空心光纤


- 光纤块越小, 模长面积越小, 非线性越弱


![[Pasted image 20231107173044.png]]

![[Pasted image 20231107173147.png]]

问题: 光纤粗了后会出现高阶模? - 设计光纤结构.

- 光的波长 ---- 长波长

## 非线性薛定谔方程 孤子解

$$j\:\frac{\partial A(z,t)}{\partial z}=-D_{2}\frac{\partial^{2}A(z,t)}{\partial t^{2}}+\delta|A(z,t)|^{2}A(z,t),\quad D_{2}=\frac{\beta _2}{2}$$
$\beta _2$ 描述了GVD.


Soliton solution:
$$A_s(z,t)=A_0\mathrm{sech}(x(z,t))e^{-j\theta(z,t)}$$
一个双曲正割函数 $\mathrm{sech}(x)=\dfrac{2}{e^{x}+e^{-x}}$

$$\left\{\quad \begin{aligned}
&x=\frac{1}{\tau}(t-2|D_2|p_0z-t_0)\\
&\theta=p_0(t-t_0)+|D_2|\left(\frac{1}{\tau^2}-p_0^2\right)z+\theta_0\\
&\frac{\delta A_0^2}{2}=\frac{|D_2|}{\tau^2}
\end{aligned}\right.$$

可用4个参数进行描述
- 能量频率 $\omega$ 或振幅 $A_{0}$
- 载波频率 $p_{0}$
- 相位 $\theta _0$
- 初始时间 $t_0$



双曲正割脉冲与高斯脉冲对比:

![[Pasted image 20231107174450.png]]

高斯脉冲下降会略快.

光孤子要满足条件:
$$\frac{\delta A_{0}^{2}}{2}=\frac{|D_{2}|}{\tau^{2}}$$
描述了<mark style="background: #FFF3A3A6;">色散效应与非线性效应达到平衡.</mark>

孤子在光纤中传输, 不会发生任何变化.

![[媒体1 1.gif]]

- 不变化的孤子称为基阶孤子
- 还存在高阶孤子, 传输过程中周期震荡.
$$A_0\tau=N\sqrt{\frac{2|D_2|}{\delta}},N=1,2,3...\quad A_s(z,t)=NA_0\mathrm{sech}(\frac{t}{\tau})e^{-j\theta}$$

![[Pasted image 20231107175258.png]]

- N=1, 基阶孤子, 孤子双曲正割函数脉冲不变
- $N\neq 1$ , 高阶孤子, 会发生变化. 左边2阶, 右边3阶.

若有两个孤子, 会相遇, 碰撞然后分开, 没有任何能量交换. 如下图所示:

![[Pasted image 20231107195432.png]]

若有两个孤子相距很近, 二者可能会相互吸引, 也有可能相互排斥.

![[媒体2 1.gif]]

Soliton 还是一个吸引子, 一开始输入不是一个严格的soliton 但在演化的过程中会慢慢演化成一个soliton.

下图是一个高斯脉冲演化为一个soliton的过程:

![[媒体3 1.gif]]

高斯脉冲在一个负色散的 Kerr 介质中传输, 会慢慢演化为一个 soliton 的一个双曲正割函数脉冲.

假设输入高斯脉冲能量高, 会演化为一个高阶的孤子, 表现出一个周期性的振荡.

![[媒体4.gif]]

超高斯脉冲演化为 soliton

![[媒体5.gif]]




如果我们已有一个soliton 但我们的系统并不完美, 具有各种噪声和扰动. 这样的情况下, soliton 是否还能保持稳定?

$$\frac{\partial A(z,t)}{\partial z}=-j\left[|D_2|\frac{\partial^2A}{\partial t^2}+\delta|A|^2A\right]+F(A,A^*,z)$$

最右边一项描述现实中的扰动.

解:
$$A(z,t)=\left[a(\frac t\tau)+\Delta A(z,t)\right]e^{-jk_sz},\quad \text{with}\quad a(\frac{t}{\tau})=A_{0}\:\mathrm{sech}(\frac{t}{\tau})\quad k_{s}=\frac{1}{2}\delta A_{0}^{2}$$

完美的孤子解+多出了一项小的噪声 $\Delta A$
$$\Delta A(z)=\Delta w(z)f_{w}+\Delta\theta(z)f_{\theta}+\Delta p(z)f_{p}+\Delta t(z)f_{t}+a_{c}(z)$$
其中, $f_w=\dfrac{\partial A}{\partial w},f_\theta=\dfrac{\partial A}{\partial\theta},f_p=\dfrac{\partial A}{\partial p},f_t=\dfrac{\partial A}{\partial t}$

- $\Delta \omega (z)$ : 能量起伏 ---- 强度噪声
- $\Delta \theta (z)$ : 相位起伏 ---- 谱线加宽
- $\Delta p(z)$ : 中心频率起伏 ---- 光谱左右抖动
- $\Delta t(z)$ : 时间起伏 ---- 脉冲时域上的抖动
- $a_{c}(z)$ : 连续背景

如下图, 通过放大器引入干扰

![[Pasted image 20231107202341.png]]

下图中可以看到脉冲出现不完美的抖动

![[Pasted image 20231107202347.png]]

Soliton 的应用:

完美的cw光并不是一个脉冲, 并不会被影响. cw输入cw输出.

但是, 不可能有完美的功率没有任何抖动, 一单cw光的光强有一点变化, 就会在负色散&自相位调制的作用下被放大 ---- 调制不稳定性 (modulation instability) , 就会产生一系列的基阶孤子, 这些基阶孤子有的很强有的很弱, 并有一定概率产生非常强的soliton 
<p align="right">---- <mark style="background: #FF5582A6;">Rogue wave</mark></p>

这种现象就像大海上突然产生一个巨大的海浪一样.

![[Pasted image 20231107203147.png]]

![[Pasted image 20231107203152.png]]

这种海浪的形成的机制与光学中非线性孤子解相类似.



Question:

1.Kerr效应中 Taylor 展开的合理性?

尤其在强场下, Taylor 展开可能要考虑高阶项. 但是Kerr效应要求只去 $n_{2}$ . 更高阶项可能是其他的更高阶的效应.

2.自聚焦 和峰值的光功率有关而跟光功率密度无关, 更大的光斑无法避免雪崩. 实际中, 固定长度的window, 光斑变大是不是可以看不到光斑的大小.

还需要考虑光束的衍射, 衍射会使得光斑发散, 光斑变大但是衍射变小的. 

薄片压缩, 用多个薄片来扩展光谱, 避免自聚焦. 通过一个薄版后让光束衍射再使得光束发散, 然后再透过薄片. 

Q: 能否直接使用透镜?

3.孤子传播过程中, 孤子时域上所有的东西几乎都不变, 除了发生一个随距离线性增加的一个常数相移.

4.孤子间相互作用, 相互之间有一个振荡. 相互作用, 有可能弹开, 也有可能交换?




