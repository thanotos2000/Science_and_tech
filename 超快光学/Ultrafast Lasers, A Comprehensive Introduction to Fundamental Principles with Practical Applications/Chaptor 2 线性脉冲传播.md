

# 2.1 动机

可见激光脉冲永远不可能是单色的，并且必须不同于连续波 (CW) 激光的单色光.

形成脉冲的颜色（即频率）成分越多，<mark style="background: #FFF3A3A6;">其光谱就越宽，脉冲就越短</mark>。

脉冲持续时间和脉冲频率带宽的乘积不能低于最小值，并且取决于脉冲形状。

当我们将不同波长的不同平面波叠加时，我们只能在时间上获得有限的波包（激光脉冲）（见图2.1）。在可见光谱中，不同的波长对应于不同的颜色，因此，可见激光脉冲永远不可能是单色的，并且必然不同于连续波（CW）激光的单色光。

![[超快光学/超快激光相关技术/附件/Pasted image 20231102090827.png]]

激光器是高度非线性系统，只需在激光腔内进行微小的损耗调制（例如，甚至小于 1%）即可产生具有高对比度和非常精确的脉冲重复率的短光脉冲。如今，我们可以直接从激光产生短至几飞秒的可见光和近红外波长范围的脉冲。这比任何电子开关速度都要快得多

超短激光脉冲的应用:
- <mark style="background: #FFF3A3A6;">短脉冲持续时间</mark>
通过使用超短激光脉冲的短时光谱，我们可以检查自然和技术中的快速过程。这通常是通过所谓的泵浦-探测测量来完成的，例如，较强的泵浦脉冲启动快速过程，而延迟的探测脉冲则探测时间的变化。
泵浦脉冲和探测脉冲的脉冲持续时间通常至少长一个数量级。这意味着<mark style="background: #FFF3A3A6;">脉冲持续时间通常是解决快速过程动力学的时间尺度的限制因素</mark>。
- <mark style="background: #FFF3A3A6;">短脉冲&高脉冲重复率</mark>
超快激光器的脉冲重复率理想地由激光腔内脉冲的往返时间设定。每次脉冲到达输出耦合器时，脉冲的一小部分就会传输到外部。因此，我们获得了脉冲串，其脉冲重复率由腔内脉冲的往返频率给出。
未来，光脉冲很可能支持多核微处理器的高速互连和时钟。
- <mark style="background: #FFF3A3A6;">宽的光谱</mark>
短脉冲还具有宽的相干频谱。
(1)应用包括<mark style="background: #FF5582A6;">光学相干断层扫描</mark> (OCT) 或<mark style="background: #FF5582A6;">频率计量</mark>等。
(2)<mark style="background: #FF5582A6;">频率梳</mark>
未来将有可能制造出比当今最好的原子钟更精确的光学钟。我们希望这样的时钟能够测量物理常数随时间的微小变化——如果它们确实存在的话。
- <mark style="background: #FFF3A3A6;">高强度</mark>
在短脉冲中，所有能量都被限制在很短的时间内。因此，可以获得非常高的峰值强度。
这对许多应用都很重要，如非线性光学、材料加工（用于机械加工和医学）、高场物理、聚变、软X射线生成和阿秒脉冲生成。

# 2.2 频域波动方程：亥姆霍兹方程

## 2.2.1 傅里叶变换

$$\begin{aligned}\tilde{E}(z,\omega)&\equiv F\left\{E(z,t)\right\}=\int E(z,t)\mathrm{e}^{-i\omega t}\mathrm{d}t\:,&(2.2)\\E(z,t)&=F^{-1}\left\{\tilde{E}(z,\omega)\right\}=\frac{1}{2\pi}\int\tilde{E}(z,\omega)\mathrm{e}^{+\mathrm{i}\omega t}\mathrm{d}\omega\:.&(2.3)\end{aligned}$$

$$\boxed{\omega\Longleftrightarrow-\mathrm{i}\frac\partial{\partial t},\quad\omega^2\Longleftrightarrow-\frac{\partial^2}{\partial t^2}=\left(-\mathrm{i}\frac\partial{\partial t}\right)^2,\quad\omega^3\Longleftrightarrow\mathrm{i}\frac{\partial^3}{\partial t^3}=\left(-\mathrm{i}\frac\partial{\partial t}\right)^3}\tag{2.4}$$

## 2.2.2 亥姆霍兹方程

波动方程
$$\Delta\mathbf{E}-\frac1{c^2}\frac{\partial^2}{\partial t^2}\mathbf{E}=\mu_0\frac{\partial^2}{\partial t^2}\mathbf{P}$$

傅里叶变换后有: 频域波动方程
$$\frac{\partial^2\tilde{E}(z,\omega)}{\partial z^2}+\frac{\omega^2}{c^2}\tilde{E}(z,\omega)=-\mu_0\omega^2\tilde{P}(z,\omega)\tag{2.6}$$

频域中波矢
$$k_n(\omega)=\frac\omega cn(\omega) \tag{2.8} $$

由于 $c=\dfrac{1}{\sqrt{\varepsilon_0\mu_0}},n(\omega)=\sqrt{\varepsilon(\omega)},$ 我们有<mark style="background: #FF5582A6;">一维亥姆霍兹方程</mark>:
$$\boxed{\frac{\partial^2\tilde{E}(z,\omega)}{\partial z^2}+\left[k_n(\omega)\right]^2\tilde{E}(z,\omega)=0}\tag{2.9}$$
一维亥姆霍兹方程的解:
$$\boxed{\tilde{E}(z,\omega)=\tilde{E}_0^+(\omega)\mathrm{e}^{-\mathrm{i}k_n(\omega)z}+\tilde{E}_0^-(\omega)\mathrm{e}^{\mathrm{i}k_n(\omega)z}}\tag{2.10}$$


# 2.3 线性与非线性波传播

## 2.3.1 叠加原理

如果 $E_i$ 和 $H_i$ 是波动方程的解，那么它们的任何线性组合也将是波动方程的解：
$$\boxed{E_{\mathrm{tot}}=\sum_ia_iE_i\:,\quad\quad H_{\mathrm{tot}}=\sum_ib_iH_i}\tag{2.15}$$
如果电场不满足干涉条件，叠加原理对强度也是有效的.

## 2.3.2 线性系统理论

线性系统:
$$E_{\mathrm{in~}1}\overset{\text{linear system}}{\operatorname*{\longrightarrow}}E_{\mathrm{out~}1}\Longrightarrow aE_{\mathrm{in~}1}\overset{\text{linear system}}{\operatorname*{\longrightarrow}}aE_{\mathrm{out~}1}$$
$$\left.\begin{array}{c}E_{\mathrm{in~1}}\overset{\text{linear system}}{\operatorname*{\longrightarrow}}E_{\mathrm{out~1}}\\E_{\mathrm{in~2}}\overset{\text{linear system}}{\operatorname*{\longrightarrow}}E_{\mathrm{out~2}}\end{array}\right\}\quad\Longrightarrow\quad E_{\mathrm{in~1}}+E_{\mathrm{in~2}}\overset{\text{linear system}}{\operatorname*{\longrightarrow}}E_{\mathrm{out~1}}+E_{\mathrm{out~2}}$$

在线性系统中，可以定义一个<mark style="background: #FF5582A6;">脉冲响应</mark> $h(t)$，它描述了完整的动态演化 $E_{\mathrm{in}}(t)\rightarrow E_{\mathrm{out}}(t)$ ，其中$E_in$ 是输入信号，$E_out$ 是输出信号。如果脉冲响应 $h(t)$ 不依赖于输入信号 $E_{in}$ 的强度，则系统是线性的：
$$E_{\mathrm{out}}(t)=\int h\left(t^{\prime}\right)E_{\mathrm{in}}\left(t-t^{\prime}\right)\mathrm{d}t^{\prime}\equiv h(t)*E_{\mathrm{in}}(t)\tag{2.20}$$
时域上, 输出函数是输入函数与脉冲响应的卷积.
$$\boxed{\tilde{E}_{\mathrm{out}}(\omega)=\tilde{h}(\omega)\tilde{E}_{\mathrm{in}}(\omega)}\tag{2.22}$$

E(t) 的<mark style="background: #FF5582A6;">功率谱密度</mark> P(ω) 由下式给出:
$$P(\omega)\equiv\left|\tilde{E}(\omega)\right|^2\Longrightarrow\quad P_{\mathrm{in}}(\omega)=\left|\tilde{E}_{\mathrm{in}}(\omega)\right|^2,\quad P_{\mathrm{out}}(\omega)=\left|\tilde{E}_{\mathrm{out}}(\omega)\right|^{2} \tag{2.23}$$
在具有频率相关折射率的色散材料中，脉冲形状可以在线性传播期间显著改变。

## 2.3.3 非线性系统

在非线性系统中，脉冲响应取决于输入强度, 输出信号取决于输入信号的强度。

非线性效应:
- 克尔效应
- 自相位调制
- 倍频
等等

因此，在非线性系统中，检查时域中的动态演化是有利的。频谱会随着时间而变化。

# 2.4 超快脉冲

## 2.4.1 脉冲波包&脉冲包络

光谱通常是具有有限宽度 $\Delta ω_0$ 和中心频率 $ω_0$ 的函数，即 $\omega _0>>\Delta \omega _0$，脉冲持续时间明显长于一个光周期（见图 2.5）。
$$E(t)=\frac1{2\pi}\int\tilde{E}\left(\omega_0+\Delta\omega\right)\mathrm{e}^{\mathrm{i}(\omega_0+\Delta\omega)t}\mathrm{d}\Delta\omega=\frac1{2\pi}\mathrm{e}^{\mathrm{i}\omega_0t}\int\tilde{A}(\Delta\omega)\mathrm{e}^{\mathrm{i}\Delta\omega t}\mathrm{d}\Delta\omega.\tag{2.32}$$
$\tilde{A}( ω)$ 就是频移频谱. 
$$\tilde{A}(\Delta\omega)=\tilde{E}\left(\omega_0+\Delta\omega\right)\tag{2.33}$$
$$\begin{aligned}E(t)=A(t)\mathrm{e}^{\mathbf{i}\omega_0t}\:,&\text{where }A(t)=\frac{1}{2\pi}\int\tilde{A}(\Delta\omega)\mathrm{e}^{\mathbf{i}\Delta\omega t}\mathrm{d}\Delta\omega\end{aligned}\tag{2.34}$$

  ![[超快光学/超快激光相关技术/附件/Pasted image 20231103001538.png]]

## 2.4.2 时间-带宽乘积与海森堡不确定性关系的类比

<mark style="background: #FF5582A6;">激光脉冲持续时间</mark> $τ_p$ : 随时间变化的脉冲强度的半峰全宽 (FWHM) 定义。

<mark style="background: #FF5582A6;">激光脉冲光谱宽度</mark> $ν_p$ 通常由光谱强度的FWHM定义。激光脉冲越短，即 $τ_p$ 值越小，其光谱 $ν_p$ 越宽。

我们在表 2.1 中总结了一些常见脉冲形状的时间带宽积 $ν_p \times  τ_p$ , 以及脉冲持续时间:

![[Pasted image 20231103002112.png]]

考虑啁啾高斯脉冲的示例

![[Pasted image 20231103002342.png]]

<mark style="background: #FF5582A6;">高斯脉冲</mark>:
$$E(t)=A(t)\exp(\mathrm{i}\omega_0t)=\exp\left(-\Gamma t^2\right)\exp(\mathrm{i}\omega_0t)\tag{2.35}$$
$\Gamma$ 是<mark style="background: #FF5582A6;">复高斯参数</mark> $\Gamma \equiv \Gamma _{1}-i\Gamma _{2}$
- 复高斯参数的实部 $\Gamma  _1$ 决定了脉冲长度，复高斯参数的虚部 $\Gamma_ 2$ 决定了高斯脉冲的啁啾
- 啁啾: <mark style="background: #FFF3A3A6;">脉冲的瞬时频率随时间改变</mark>。

高斯脉冲的相位:
$$\phi_{\mathrm{tot}}(t)\equiv\omega_0t+\Gamma_2t^2\tag{2.37}$$
高斯脉冲的瞬时频率 (相位随时间改变)
$$\omega(t)\equiv\frac{\mathrm{d}\phi_{\mathrm{tot}}(t)}{\mathrm{d}t}=\omega_0+2\Gamma_{2}t \tag{2.38}$$
高斯脉冲的脉冲长度 $τ_p$ 由强度 $I (t)$ 的半高宽定义：
$$I(t)\propto|E(t)|^2=\exp\left(-2\Gamma_{1}t^{2}\right)=\exp\left[-(4\ln2)\left(\frac t{\tau_{\mathfrak{p}}}\right)^{2}\right]\tag{2.39}$$
$$\boxed{\tau_{\mathfrak{p}}=\sqrt{\frac{2\ln2}{\Gamma_1}}}\tag{2.40}$$

通过进行傅里叶变换并完成指数平方，可以发现连续频谱为:
$$\tilde{E}(\omega)\propto\exp\left[-\frac{(\omega-\omega_0)^2}{4\Gamma}\right]$$
$$\tilde{l}(\omega)\propto\left|\tilde{E}(\omega)\right|^2\propto\exp\left[-\left(4\ln2\right)\frac{\left(\omega-\omega_0\right)^2}{\Delta\omega_{\mathfrak{p}}^2}\right]\tag{2.42}$$
高斯脉冲的频谱宽度 $\Delta \omega _p$ (光强谱的半高宽): 
$$\Delta\nu_{\mathfrak{p}}\equiv\frac{\Delta\omega_{\mathfrak{p}}}{2\pi}=\frac{\sqrt{2\ln2}}\pi\sqrt{\Gamma_1\left[1+\left(\frac{\Gamma_2}{\Gamma_1}\right)^2\right]}\tag{2.43}$$
给定的脉冲持续时间（相同 $\Gamma _1$ 下），啁啾脉冲 ($\Gamma _2 \neq 0$) 始终比非啁啾脉冲 ($\Gamma _2 = 0$) 具有更宽的频谱带宽, 或者说啁啾使脉冲展宽.

高斯脉冲的时间脉宽积: 
$$\boxed{\tau_\mathrm{p}\Delta\nu_\mathrm{p}=\frac{2\ln2}\pi\sqrt{1+\left(\frac{\Gamma_2}{\Gamma_1}\right)^2}=0.4413\times\sqrt{1+\left(\frac{\Gamma_2}{\Gamma_1}\right)^2}}\tag{2.44}$$
若没有啁啾, 
$$\tau_p \Delta \nu_p=0.4413$$
此时为最小的时间带宽积, 相应光脉冲称为时间带宽受限或<mark style="background: #FF5582A6;">带宽受限脉冲</mark>, 对于给定的频谱, 带宽受限脉冲具有最短的脉冲持续时间对于确定的频谱宽度&脉冲形状.

- <mark style="background: #FFF3A3A6;">频谱中任何额外的啁啾都会导致更长的脉冲持续时间</mark>。

## 2.4.3 产生最短脉冲的光谱相位

实际中的脉冲都表现出复杂或者说不规则的光谱，往往与理想的脉冲形状不一致。

![[Pasted image 20231103014943.png]]

于是，<mark style="background: #FFF3A3A6;">简单地通过 FWHM 值指定脉冲持续时间并不契合实际</mark>。更合适的脉冲宽度测量可由 $rms$ 脉冲持续时间 $τ_{rms}$ 给出：
$$\begin{aligned}\tau_{\mathrm{rms}}^2&=\left\langle(t-\langle t\rangle)^2\right\rangle=\int_{-\infty}^\infty\left(t-\langle t\rangle\right)^2I(t)\mathrm{d}t\\&=\int_{-\infty}^\infty\left|\left(t-\langle t\rangle\right)E(t)\right|^2\mathrm{d}t\end{aligned}$$
其中, $\langle t \rangle$ 对应于<mark style="background: #FF5582A6;">时间脉冲轮廓的重心</mark>. 

对于给定的功率谱$|\tilde{E} (\omega )|^{2}$，可以通过线性谱相位 $φ(ω$) 获得最短的 rms 脉冲持续时间. 

使用傅里叶分析的<mark style="background: #FF5582A6;"> Parseval 定理</mark>, 上式可化为
$$\tau_\mathrm{rms}^2=\int_{-\infty}^\infty\left|\frac{\partial\left[\tilde{E}(\omega)\exp\left(-\mathrm{i}\omega\left\langle t\right\rangle\right)\right]}{\partial\omega}\right|^2\mathrm{d}\omega $$
我们定义 $φ(ω)= φ(ω) − ω t$，因此它是没有线性项的谱相位。根据这个定义和关系$\tilde{E}(ω) =|\tilde{E} (ω)| exp (iφ(ω))$，我们有:
$$\begin{aligned}\tau_\mathrm{rms}^2&=\int_{-\infty}^\infty\left|\frac{\partial\left|\tilde{E}\left(\omega\right)\right| .}{\partial\omega}+\mathrm{i}\left|\tilde{E}\left(\omega\right)\right|\frac{\partial\phi\left(\omega\right)}{\partial\omega}\right|^2\mathrm{d}\omega\\&=\int_{-\infty}^\infty\left|\frac{\partial\left|\tilde{E}\left(\omega\right)\right|}{\partial\omega}\right|^2\mathrm{d}\omega+\int_{-\infty}^\infty\left|\left|\tilde{E}\left(\omega\right)\right|\frac{\partial\phi\left(\omega\right)}{\partial\omega}\right|^2\mathrm{d}\omega\end{aligned}$$
最后右侧第二项大于等于零. 因此, 给定脉冲频谱 $|\tilde{E} (ω) |^2$ 的光脉冲的最短均方根持续时间在相位 $\phi(ω)$ 为<mark style="background: #FFF3A3A6;">常数</mark>时出现。

根据上述定义，我们可以直接得出结论: 
- 在这种情况下，谱相位 $\phi(ω)$ 仅由常数和线性项组成。
- 所有其他频谱相位函数都会产生更长的均方根脉冲持续时间。


# 2.5 色散材料中的线性脉冲传播

## 2.5.1 线性脉冲传播与线性色散

Sect. 2.3.2 中讲到: 对于<mark style="background: #FFF3A3A6;">色散介质中的线性脉冲传播，频谱不会改变</mark>. 对于任何可能表现出非线性频率依赖性的任意色散关系都是这种情况。
- 线性脉冲传播意味着不考虑强度相关的材料特性。
- 然而，折射率 $n(ω)$ 可以具有任何非线性频率依赖性。
- 我们将证明线性脉冲传播可以完全由频率相关的折射率 $n(ω)$ 和吸收系数 $α(ω)$ 来描述。
- 色散和吸收是脉冲传播中的线性效应。另一方面，在非线性脉冲传播中，还考虑强度相关效应，例如吸收或放大的饱和、自聚焦、孤子等。

## 2.5.2 缓变包络近似

为了检查线性脉冲的传播, 我们需要<mark style="background: #FFF3A3A6;">分离复电场中快速变化的部分</mark> (我们对此并不关心) , 我们只关心包络 $A(z,t)$ 的动力学机制.
$$E(z,t)=A(z,t)\mathrm{e}^{\mathrm{i}[\omega_0t-k_n(\omega_0)z]},\quad k_n(\omega _0)=\frac{n\omega _0}{c}$$
  ![[超快光学/超快激光相关技术/附件/Pasted image 20231103001538.png]]

我们可以直接用 A 通过某些因子(略去)确定脉冲的强度&功率:
$$I(z,t)=|A(z,t)|^2,\quad P(z,t)=|A(z,t)|^2$$
频域上,
$$\tilde{E}\left(z,\omega_0+\Delta\omega\right)=\tilde{A}\left(z,\Delta\omega\right)\mathrm{e}^{-\mathrm{i}k_n(\omega_0)z},\quad\tilde{A}\left(z,\Delta\omega\right)=\int A(z,t)\mathrm{e}^{-\mathrm{i}\Delta\omega t}\mathrm{d}t$$
频域上波动方程:
$$\frac{\partial^2\tilde{E}(z,\omega)}{\partial z^2}+[k_n(\omega)]^2\tilde{E}(z,\omega)=0\mathrm{~,}$$
写成A的形式
$$\begin{aligned}&\frac{\partial^2}{\partial z^2}\tilde{A}\left(z,\Delta\omega\right)-2\mathrm{i}k_n(\omega_0)\frac\partial{\partial z}\tilde{A}\left(z,\Delta\omega\right)-\left[k_n(\omega_0)\right]^2\tilde{A}\left(z,\Delta\omega\right)\\&+\left[k_n\left(\omega_0+\Delta\omega\right)\right]^2\tilde{A}\left(z,\Delta\omega\right)=0\end{aligned}$$
我们作<mark style="background: #FF5582A6;">缓变包络近似</mark> (slowly varying-envelope approximation, <mark style="background: #FF5582A6;">SVEA</mark>)
$$\boxed{\left|\frac{\partial^2\tilde{A}}{\partial z^2}\right|\ll\left|k_n(\omega_0)\frac{\partial\tilde{A}}{\partial z}\right|}\tag{2.57}$$
SVEA意味着: 包络线在一个波长$λ_{n0}  = λ_{0}/n$ 的距离内变化不大。

<mark style="background: #FFF3A3A6;">通过上面近似, 我们可以忽略频域波动方程中二阶的高阶项</mark>
$$\frac\partial{\partial z}\tilde{A}\left(z,\Delta\omega\right)+\mathrm{i}\frac12\left[\frac{k_n^2\left(\omega_0+\Delta\omega\right)}{k_n(\omega_0)}-k_n(\omega_0)\right]\tilde{A}\left(z,\Delta\omega\right)=0$$
将 $k_{n}$ 在中心频率附近展开到一阶
$$k_n(\omega_0+\Delta\omega)\approx k_n(\omega_0)+\Delta k_n$$
代入到i后面的中括号内, 有:
$$\begin{aligned}\frac12\left[\frac{k_n^2\left(\omega_0+\Delta\omega\right)}{k_n(\omega_0)}-k_n(\omega_0)\right]&=\frac12\left[\frac{k_n^2(\omega_0)+2\Delta k_nk_n(\omega_0)+\Delta k_n^2-k_n^2(\omega_0)}{k_n(\omega_0)}\right]\\&=\frac12\left[\frac{2\Delta k_nk_n(\omega_0)+\Delta k_n^2}{k_n(\omega_0)}\right],\end{aligned}$$
由于 $\Delta k_n<<k_n$, 舍去平方项并相消
$$\frac12\left[\frac{k_n^2\left(\omega_0+\Delta\omega\right)}{k_n(\omega_0)}-k_n(\omega_0)\right]=\Delta k_{n}$$
波动方程化为:
$$\boxed{\frac\partial{\partial z}\tilde{A}\left(z,\Delta\omega\right)+\mathrm{i}\Delta k_n\tilde{A}\left(z,\Delta\omega\right)=0}\tag{2.60}$$
上式就是<mark style="background: #FF5582A6;">脉冲包络线的等效波动方程</mark>。这个微分方程的解很简单：
$$\boxed{\tilde{A}\left(z,\Delta\omega\right)=\tilde{A}\left(0,\Delta\omega\right)\mathrm{e}^{-\mathrm{i}\Delta k_nz}=\tilde{A}\left(0,\Delta\omega\right)\mathrm{e}^{-\mathrm{i}[k_n(\omega_0+\Delta\omega)-k_n(\omega_0)]z}}\tag{2.61}$$

## 2.5.3 一阶&二阶色散

- 光脉冲由单色平面波的连续叠加组成，其傅里叶频谱的分量围绕中心频率 $ω_0$ 分组。
- 对于给定的介质，光谱的每个部分都有自己的相速度，这导致在传播过程中各个光谱分量之间的相移.
- 脉冲加宽的原因是群速度的色散，而不是相速度的色散.

<mark style="background: #FFF3A3A6;">脉冲越短，其光谱带宽越宽，色散对脉冲的影响越强。</mark>

如果脉冲的谱宽远小于其载波频率，由于载波频率巨大，即使对于超短光脉冲，这在光学区域也能满足，我们只需将波数$k_n(ω)$ 围绕载波频率 $ω_0$ 展开到二阶：
$$k_n(\omega)\approx k_n(\omega_0)+k_n^{\prime}\Delta\omega+\frac12k_n^{\prime\prime}\Delta\omega^2$$
- 一阶色散 $k_n'=\dfrac{dk_n}{d\omega }$
- 二阶色散 $k_n''=\dfrac{d^2k_n}{d\omega ^2}$

## 2.5.4 相速度与群速度

对于高斯脉冲，可以在考虑高达二阶色散的色散介质中解析求解线性脉冲传播。

高斯脉冲包络
$$\begin{aligned}A\left(z=0,t\right)&=\exp\left[-\Gamma(0)t^2\right]\:,\\E\left(z=0,t\right)&\propto\exp\left[-\Gamma(0)t^2\right]\mathrm{e}^{\mathrm{i}\left[\omega_0t-k_n(\omega_0)z\right]}\end{aligned}$$
傅里叶变换后, 高斯脉冲包络的频谱为
$$\tilde{A}\left(z=0,\Delta\omega\right)=\int A\left(0,t\right)\mathrm{e}^{-\mathrm{i}\Delta\omega t}\mathrm{d}t=\sqrt{\frac{\pi}{\Gamma\left(0\right)}}\exp\left[-\frac{\left(\omega-\omega_0\right)^2}{4\Gamma\left(0\right)}\right]$$
通过长度为 $L_d$ 的色散介质后, 高斯脉冲的频谱
$$\tilde{A}\left(L_{\mathbf{d}},\omega\right)=\tilde{A}\left(0,\omega\right)\mathrm{e}^{-\mathrm{i}[k_{n}(\omega)-k_{n}(\omega_{0})]L_{\mathbf{d}}}$$
考虑<mark style="background: #FFF3A3A6;">二阶色散</mark>, 将波数展开到二阶 $k_n(\omega)\approx k_n(\omega_0)+k_n^{\prime}\Delta\omega+\frac12k_n^{\prime\prime}\Delta\omega^2$ ,有:
$$\tilde{A}\left(L_{\mathsf{d}},\omega\right)=\sqrt{\frac{\pi}{\Gamma\left(0\right)}}\exp{\left[-\frac{\left(\omega-\omega_{0}\right)^{2}}{4\Gamma\left(0\right)}\right]}\exp{\left[-\mathrm{i}k_{n}^{\prime}L_{\mathsf{d}}\left(\omega-\omega_{0}\right)-\mathrm{i}\frac{k_{n}^{\prime\prime}L_{\mathsf{d}}}2\left(\omega-\omega_{0}\right)^{2}\right]}$$
作傅里叶逆变换, 即可得到经过色散介质后的输出脉冲 $A(L_{d},t)$ :
$$A\left(L_{\mathbf{d}},t\right)=\frac1{2\pi}\sqrt{\frac\pi{\Gamma(0)}}\int\exp\left[-\frac{\left(\omega-\omega_0\right)^2}{4\Gamma\left(L_{\mathbf{d}}\right)}+\mathrm{i}\left(\omega-\omega_0\right)\left(t-k_n^{\prime}L_{\mathbf{d}}\right)\right]\mathrm{d}\left(\omega-\omega_0\right)\tag{2.68}$$
其中, k''合并到前面一个指数函数内改变 $\Gamma$ 函数的相位.

我们不考虑比例因子, 电场可表示为:
$$\begin{aligned}E\left(L_{\mathrm{d}},t\right)&=\exp\left[\mathrm{i}\omega t-\mathrm{i}k_{n}(\omega_{0})L_{\mathrm{d}}\right]\\&\times\int\exp\left[-\frac{\left(\omega-\omega_{0}\right)^{2}}{4\Gamma\left(L_{\mathrm{d}}\right)}+\mathrm{i}\left(\omega-\omega_{0}\right)\left(t-k_{n}^{\prime}L_{\mathrm{d}}\right)\right]\mathrm{d}\left(\omega-\omega_{0}\right)\end{aligned}\tag{2.69}$$
方程（2.69）对应于时间偏移为 $(t − k_ nL_d )$ 的高斯脉冲 $exp(\Gamma  t^2)$ 的傅立叶变换。在这个方程中，我们可以将<mark style="background: #FF5582A6;">传播后的复高斯参数</mark> $\Gamma (L_d)$ 写为
$$\boxed{\frac1{\Gamma(L_\mathsf{d})}=\frac1{\Gamma(0)}+2\mathrm{i}k_n^{\prime\prime}L_\mathsf{d}}\tag{2.70}$$
该式对应于得到 (2.68) 式时我们所做的合并处理.

我们看到只有二阶色散项 $(k''_n )$ 影响复高斯参数。这表明
- <mark style="background: #FFF3A3A6;">只有二阶和更高阶色散才导致脉冲展宽</mark>。
- 因此这是<mark style="background: #FFF3A3A6;">群速度的色散，而不是相速度的色散</mark>，这最初是违反直觉的。

为了计算 (2.69) 中的积分，以下关系式很有用
$$\int\mathrm{e}^{-Ay^2-2By}\mathrm{d}y=\sqrt{\frac\pi A}\mathrm{e}^{B^2/A},\quad\mathrm{Re}(A)>0$$
积分结果为:
$$E\left(L_{\mathsf{d}},t\right)\propto\exp\left[\mathrm{i}\omega_0\left(t-\frac{L_{\mathsf{d}}}{\upsilon_{\mathsf{p}}(\omega_0)}\right)\right]\exp\left[-\Gamma(L_{\mathsf{d}})\left(t-\frac{L_{\mathsf{d}}}{\upsilon_{\mathsf{g}}(\omega_0)}\right)^2\right]$$
其中,
- <mark style="background: #FF5582A6;">相速度</mark> 
$$\boxed{\upsilon_{\mathfrak{p}}(\omega_0)\equiv c_n=\left.\frac\omega{k_n}\right|_{\omega=\omega_0}}\tag{2.73}$$
- <mark style="background: #FF5582A6;">群速度</mark> (脉冲包络的传播速度)
$$\boxed{\left.\upsilon_{\mathfrak{g}}(\omega_0)\equiv\frac1{k_n^{\prime}(\omega_0)}=\frac1{\left.\frac{\mathrm{d}k_n}{\mathrm{d}\omega}\right|_{\omega=\omega_0}}=\frac{\mathrm{d}\omega}{\mathrm{d}k_n}\right|_{\omega=\omega_0}}\tag{2.74}$$
真空中，适用色散关系 $k(ω) = ω/c$ , 群速度与相速度相等.

一阶色散决定了<mark style="background: #FFF3A3A6;">脉冲的时间偏移</mark>，称为<mark style="background: #FF5582A6;">群延迟</mark>，记为 Tg。
$$\boxed{T_\mathfrak{g}\equiv\frac z{\upsilon_\mathfrak{g}}=k_n^{\prime}z}\tag{2.75}$$

![[Pasted image 20231103024544.png]]

## 2.5.5 色散脉冲展宽 $\star\star\star\star\star$

<mark style="background: #FF5582A6;">色散脉冲展宽</mark>: 脉冲通过色散介质传播而变宽.

![[Pasted image 20231103024905.png]]

### 色散介质中的脉冲展宽

在色散介质中传播 $L_d$ 距离后, 半高宽或者说脉冲长度可由前文计算:
$$\tau_{p}\left(L_{d}\right)=\sqrt{\frac{2\ln2}{\operatorname{Re}\left[\Gamma\left(L_{d}\right)\right]}}\tag{2.76}$$
- 线性色散本身对脉冲增宽没有贡献，而仅对二阶和更高阶色散有贡献。
- 三阶与更高阶色散对于非常短的脉冲或可忽略的小的低阶色散变得重要。

对于<mark style="background: #FFF3A3A6;">不存在啁啾</mark>的<mark style="background: #FFF3A3A6;">变换受限</mark>输入脉冲, 这样的特殊情况，(2.70) 化简为
$$\tau_{p}=\sqrt{\frac{2\ln2}{\Gamma_1}},\quad \frac1{\Gamma(L_\mathsf{d})}=\frac1{\Gamma(0)}+2\mathrm{i}k_n^{\prime\prime}L_\mathsf{d}\quad \Rightarrow \quad \frac1{\Gamma(L_\mathrm{d})}=\frac{\tau_\mathrm{p}^2(0)}{2\ln2}+2\mathrm{i}k_\mathrm{n}^{\prime\prime}L_\mathrm{d}\mathrm{~.}$$
代入 (2.76) 中, 
$$\tau_{p}\left(L_{d}\right)=\frac{\sqrt{\tau_{p}^4(0)+\left(4\ln2k_{\mathfrak{n}}^{\prime\prime}L_{d}\right)^2}}{\tau_{p}(0)}$$
或者可写为
$$\boxed{\frac{\tau_{\mathbf{p}}\left(L_{\mathbf{d}}\right)}{\tau_{\mathbf{p}}(0)}=\sqrt{1+\frac{\left(4\ln2k_{\mathbf{n}}^{\prime\prime}L_{\mathbf{d}}\right)^2}{\tau_{\mathbf{p}}^4(0)}}=\sqrt{1+\left(\frac{4\ln2\dfrac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}}{\tau_{\mathbf{p}}^2(0)}\right)^2}}\tag{2.79}$$
其中 $\phi = k_n L_d$ , 是厚度为 $L_d$ 的<mark style="background: #FF5582A6;">色散介质中平面波的累积相移</mark>。 
- (2.79) 描述了变换限制输入脉冲持续时间 $τ_p(0)$ 的二阶色散引起的脉冲展宽。
- <mark style="background: #FFF3A3A6;">原始脉冲越短，脉冲被色散介质拉伸得越多</mark>。
- 这里，脉冲保持高斯分布。但<mark style="background: #FFF3A3A6;">一般来说，脉冲形状可能会发生显着变化</mark>. 

Ps: 文献中, 常用<mark style="background: #FF5582A6;">相移</mark> $\phi(\omega )=k_nL_d$ 而不是频率相关的折射率 $n(\omega )$ 或波数 $k(\omega )$ 描述色散.

图 2.11 描绘了中心波长为 800 nm 的高斯脉冲通过 1 cm 厚的熔融石英透镜后的脉冲展宽，使用（2.79）计算。

![[Pasted image 20231103030750.png]]

- 在<mark style="background: #FFF3A3A6;">线性状态下，脉冲展宽因子与脉冲的谱宽成正比</mark>。
- 对于低于 100 fs 的脉冲长度，利用透镜、分束器等光学元件进行的脉冲展宽变得非常重要。因此，在需要短时间分辨率的测量中，必须补偿所有透镜和光学元件，或者必须用反射光学元件替换它们。


### **强脉冲展宽近似** 下输出的脉冲长度计算

在脉冲展宽效应很强烈的情形下,
$$\frac{d^2\phi}{d\omega ^{2}}>>\tau^2_p(0)$$
脉冲展宽因子化简为
$$\frac{\tau_{\mathrm{p}}\left(L_{\mathrm{d}}\right)}{\tau_{\mathrm{p}}(0)}=\sqrt{1+\left(\frac{4\ln2\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}}{\tau_{\mathrm{p}}^2(0)}\right)^2}\approx\frac{4\ln2\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}}{\tau_{\mathrm{p}}^2(0)}\mathrm{~,~for~}\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}\gg\tau_{\mathrm{p}}^2(0)$$

由 (2.44) , 假设 $\tau _p(0)$ 没有啁啾, 时间带宽积:
$$\tau_p(0)\Delta \nu_p=\frac{2\ln 2}{\pi}\sqrt{1+(\frac{\Gamma _2}{\Gamma _1})^2}=\frac{2\ln 2}{\pi }$$
代入上式, 
$$\tau_p(L_{d})\approx \frac{4\ln 2\dfrac{d^{2}\phi}{d\omega ^2}}{\tau _p(0)}=2\pi\Delta \nu _p\frac{d^2\phi}{d\omega ^2}=\frac{d^2\phi}{d\omega ^2}\Delta \omega _p$$
因此, 对于十分强烈的脉冲展宽, 输出脉冲长度近似为
$$\boxed{\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}\gg\tau_{p}^2(0)\implies\tau_{p}\left(L_{d}\right)\approx\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}\Delta\omega_{p}}\tag{2.80}$$

表2.2列出了不同材料在800 nm中心波长处的一阶至三阶色散。这些值来自于第 1.4.2 节中讨论和给出的 Sellmeier 方程。
$$n^2=1+\frac{A\lambda^2}{\lambda^2-\lambda_1^2}+\frac{B\lambda^2}{\lambda^2-\lambda_2^2}+\frac{C\lambda^2}{\lambda^2-\lambda_3^2}$$

![[Pasted image 20231104004336.png]]

与上表相关的公式:

波数与折射率关系, (2.8) 式, (两种色散关系的表示间的联系)
$$k_n(\omega)=\frac\omega cn(\omega) \tag{2.8} $$
波长与角频率关系
$$\omega =\frac{2\pi c}{\lambda }$$
相移 (联系与相移相关的色散关系)
$$\phi(\omega )=k_nL_d$$

> **Example** 中心波长为 800 nm 的, 带宽限制为 10 fs 的高斯脉冲通过 1 cm 厚的熔融石英材料, 发生脉冲展宽多少?  (Important!)
>
> 计算 $\dfrac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}$
> $$\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}=L_\mathrm{d}\frac{\mathrm{d}^2k_n}{\mathrm{d}\omega^2}=361\mathrm{~fs}^2$$
> 时间带宽积
> $$\Delta \nu_p\tau_p=\frac{2\ln2}{\pi}=0.4413$$
> $$\Delta \omega _p=2\pi \Delta \nu _p=2\pi \frac{0.4413}{10 fs}=2.77 fs^{-1}$$
> 所以可由 (2.80) 求脉冲宽度:
> $$\tau_{p}\left(L_{d}\right)\approx\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}\Delta\omega_{p}=361*2.77fs=100.046fs$$
> 脉宽展宽约10倍. ||

正色散下的脉冲展宽如图 2.12 所示。
- 脉冲变得更长并且啁啾. 
- 具有较长波长的光谱分量比具有较短波长的分量传播得更快，即$\lambda_{1}>\lambda_{2}\Rightarrow\upsilon_{\mathfrak{g}}\left(\lambda_{1}\right)>\upsilon_{\mathfrak{g}}\left(\lambda_{2}\right)$ 。

![[Pasted image 20231104010834.png]]

需要注意: 

- 线性色散脉冲展宽仅发生在二阶和更高阶色散中。这意味着相关的不是与频率相关的相速度差异，而是群速度。
- <mark style="background: #FFF3A3A6;">脉冲的频谱在传播过程中并不会改变</mark>, 如图 2.13 所示.

![[Pasted image 20231104011350.png]]

Q: 脉冲展宽过程中, 更加细节地看, 或者从时域上看, 究竟发生了什么?

可以将短脉冲分成中心波长稍有偏移的较长子脉冲（图 2.14）。
- <mark style="background: #FFF3A3A6;">较长子脉冲的叠加会产生较短的脉冲</mark>，因为子脉冲肩部的电场会产生破坏性干扰。
- <mark style="background: #FFF3A3A6;">各个子脉冲不会展宽，但它们将具有不同的群延迟</mark>，因为对于不同的中心波长，$dφ/dω$ 不同。
- 这种<mark style="background: #FFF3A3A6;">不同的群延迟会导致脉冲展宽</mark>，如图 2.14 所示。

![[Pasted image 20231104011716.png]]

## 2.5.6 色散与频率和波长的关系

结果总结如下表:

![[Pasted image 20231104012657.png]]

<mark style="background: #FF5582A6;">群延迟</mark> $T_g=\dfrac{z}{v_g}$ 


群速度
$$\frac1{\upsilon_\mathrm{g}}=\frac{\mathrm{d}k_n(\omega)}{\mathrm{d}\omega}=\frac{\mathrm{d}}{\mathrm{d}\omega}\left[\frac{n(\omega)\omega}c\right]=\frac{\mathrm{d}n(\omega)}{\mathrm{d}\omega}\frac\omega c+\frac nc$$

考虑 
$$\nu=\frac c\lambda\implies\frac{\mathrm{d}\nu}{\mathrm{d}\lambda}=-\frac c{\lambda^2}=-\frac\nu\lambda\implies\frac{\mathrm{d}\nu}\nu=-\frac{\mathrm{d}\lambda}\lambda $$
所以
$$\frac{d\omega }{\omega }=-\frac{d\lambda }{\lambda }$$
因此,
$$\frac{\mathrm{d}n(\omega)}{\mathrm{d}\omega}\omega=-\frac{\mathrm{d}n(\lambda)}{\mathrm{d}\lambda}\lambda $$
代入, 最後有
$$\frac1{\upsilon_\mathrm{g}}=-\frac{\mathrm{d}n(\lambda)}{\mathrm{d}\lambda}\frac\lambda c+\frac nc=\frac nc\left[1-\frac{\mathrm{d}n(\lambda)}{\mathrm{d}\lambda}\frac\lambda n\right]$$
二阶和三阶色散的类似关系
$$\begin{aligned}\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}&=\frac{\mathrm{d}}{\mathrm{d}\omega}\left(\frac{\mathrm{d}\phi}{\mathrm{d}\omega}\right)=\frac{\mathrm{d}}{\mathrm{d}\omega}\left[\frac{nL_{\mathrm{d}}}c\left(1-\frac{n^{\prime}}n\lambda\right)\right]=\frac{\mathrm{d}\lambda}{\mathrm{d}\omega}\frac{\mathrm{d}}{\mathrm{d}\lambda}\left[\frac{nL_{\mathrm{d}}}c\left(1-\frac{n^{\prime}}n\lambda\right)\right]\\&=-\frac{2\pi c}{\omega^2}\frac{L_{\mathrm{d}}}c\left[n^{\prime}\left(1-\frac{n^{\prime}}n\lambda\right)+n\left(-\frac{n^{\prime\prime}}n\lambda-\frac{n^{\prime}}n+\left(\frac{n^{\prime}}n\right)^2\lambda\right)\right]\\&=-\frac{\lambda^2}{2\pi c}\frac{L_{\mathrm{d}}}c\left(n^{\prime}-\frac{n^{\prime2}}n\lambda-n^{\prime\prime}\lambda-n^{\prime}+\frac{n^{\prime2}}n\lambda\right)=\frac{\lambda^3L_{\mathrm{d}}}{2\pi c^2}n^{\prime\prime}.\end{aligned}$$
并且,
$$\begin{aligned}\frac{\mathrm{d}^3\phi}{\mathrm{d}\omega^3}&=\frac{\mathrm{d}}{\mathrm{d}\omega}\left(\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}\right)=\frac{\mathrm{d}\lambda}{\mathrm{d}\omega}\frac{\mathrm{d}}{\mathrm{d}\lambda}\left(\frac{\lambda^3L_\mathrm{d}}{2\pi c^2}n^{\prime\prime}\right)\\&=-\frac{\lambda^2}{2\pi c}\frac{L_\mathrm{d}}{2\pi c^2}\left(3\lambda^2n^{\prime\prime}+\lambda^3n^{\prime\prime\prime}\right)=-\frac{\lambda^4L_\mathrm{d}}{4\pi^2c^3}\left(3n^{\prime\prime}+\lambda n^{\prime\prime\prime}\right)\end{aligned}$$

二阶色散，即<mark style="background: #FF5582A6;">群速度色散</mark>（GVD）或<mark style="background: #FF5582A6;">群延迟色散</mark>（GDD）, 根据应用，通常使用不同的算式和单位
$$GVD:\frac{dv_g}{d\omega }\tag{2.81}$$
$$GDD:\frac{dT_{g}}{d\omega }=\frac{d^2\phi}{d\omega ^2}\quad [fs^2]\tag{2.82}$$
$$GDD:\frac{dT_{g}}{d\lambda } \quad \left[\frac{fs}{nm}\right]\tag{2.83}$$
表格中, GDD 的计算:
$$\begin{aligned}\frac{\mathrm{d}T_\mathrm{g}}{\mathrm{d}\lambda}&=\frac{\mathrm{d}T_\mathrm{g}}{\mathrm{d}\omega}\frac{\mathrm{d}\omega}{\mathrm{d}\lambda}\\&=-\frac{2\pi c}{\lambda^2}\frac{\mathrm{d}T_\mathrm{g}}{\mathrm{d}\omega}=-\frac{2\pi c}{\lambda^2}\frac{\lambda^3L_\mathrm{d}}{2\pi c^2}n^{\prime\prime}\\&=-\frac{\lambda L_\mathrm{d}}cn^{\prime\prime}.\end{aligned}$$

请注意，(2.82) 和 (2.83) 还会导致 GDD 的代数符号不同（除了单位不同之外）。

对于光纤，通常使用以下符号：
$$\mathrm{GDD}:\begin{array}{rr}\dfrac{\mathrm{d}^2k_n}{\mathrm{d}\omega^2}&\left[\dfrac{\mathrm{ps}^2}{\mathrm{km}}\right]\end{array}\tag{2.84}$$
给定<mark style="background: #FF5582A6;">光纤长度</mark> $L_F$ , 上式可化为:
$$\frac{\mathrm{d}^2k_n}{\mathrm{d}\omega^2}L_\mathrm{F}=\frac{\mathrm{d}^2\boldsymbol{\phi}}{\mathrm{d}\omega^2}=\frac{\mathrm{d}T_\mathrm{g}}{\mathrm{d}\omega}$$
此外，在光通信中，人们给出了对二阶色散的另一种描述, 即<mark style="background: #FF5582A6;">色散系数</mark>：
$$\mathrm{GDD}:\:D_\lambda\equiv-\frac1{L_\mathrm{F}}\frac{\mathrm{d}T_\mathrm{g}}{\mathrm{d}\lambda}=\frac{\omega^2}{2\pi cL_\mathrm{F}}\frac{\mathrm{d}T_\mathrm{g}}{\mathrm{d}\omega}\quad\left[\frac{\mathrm{ps}}{\mathrm{km}\cdot\mathrm{nm}}\right]\tag{2.85}$$

我们使用前面推导的一个简单的关系（2.80），用于计算强脉冲展宽近似中高斯脉冲的色散脉冲展宽，即：
$$\tau_{\mathfrak{p}}\left(L_{d}\right)\approx\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}\Delta\omega_{\mathfrak{p}}$$
首先, $\dfrac{d^2\phi}{d\omega ^2}$ 与 $D_{\lambda}$ 有如下关系:
$$D_\lambda:=-\frac1{L_\mathrm{d}}\frac{\mathrm{d}T_\mathrm{g}}{\mathrm{d}\lambda}=\frac{\omega^2}{2\pi cL_\mathrm{d}}\frac{\mathrm{d}T_\mathrm{g}}{\mathrm{d}\omega}\:,\quad\quad T_\mathrm{g}:=\frac{\mathrm{d}\phi}{\mathrm{d}\omega}$$
$$\quad\Rightarrow\quad D_\lambda=\frac{\omega^2}{2\pi cL_\mathbf{d}}\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}$$
因此,
$$\tau_{\mathrm{p}}\left(L_{\mathrm{d}}\right)\approx\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}\Delta\omega=\frac{2\pi cL_{\mathrm{d}}D_{\lambda}}{\omega^2}\Delta\omega=D_{\lambda}L_{\mathrm{d}}\Delta\lambda \tag{2.86}$$
最后一个等式, 我们使用了
$$\frac{\Delta \omega }{\omega }=\frac{\Delta \lambda }{\lambda },\quad  \Delta \omega =\frac{\omega }{\lambda }\Delta \lambda=\frac{2\pi c}{\lambda ^{2}}\Delta \lambda $$
光纤末端的脉冲持续时间是色散系数 $D_λ$、光纤长度和脉冲光谱带宽的乘积。


脉冲展宽与色散系数

## 2.5.7 光通信

大多数长距离通信都是通过<mark style="background: #FF5582A6;">光纤</mark>传输的。玻璃光纤包含<mark style="background: #FFF3A3A6;">高折射率</mark>的<mark style="background: #FF5582A6;">纤芯</mark>以及<mark style="background: #FFF3A3A6;">低折射率</mark>的<mark style="background: #FF5582A6;">包层</mark>（见图 2.15）。因为由于包层上的<mark style="background: #FFF3A3A6;">全内反射</mark>，光停留在纤芯中,  光可以以低损耗在纤芯中传播。如果光纤中只能引导一种可能的横向场分布，则称为单模光纤。

![[Pasted image 20231104232451.png]]

信息的传输可以是数字的，即信息以一定的比特率以比特为单位进行传输。

由于传输距离可以超过1000公里，因此要选择玻璃光纤损耗最小的光载波频率, 对应波长约为 1.55 μm.

然而，在一定距离之后，额外的光放大器是必要的. 在1.55μm波长处，玻璃纤维具有二阶色散（见图2.16）。波导中的色散取决于材料，还取决于波导的几何形状。

考虑特殊情况，我们通过长度 LF = 5000 km 的光纤发送中心波长为 λ0 = 1.55 μm 且脉冲重复率为 5 GHz 的 20 ps 脉冲。我们想知道，在这个距离之后脉冲将如何变化以及数字信息是否能够保存。目前我们忽略损耗和所有非线性过程，仅考虑色散的影响。

中心波长 λ0 = 1.55 μm 的 20 ps 脉冲的光谱宽度 λp 由以下时间带宽积给出
$$\Delta \nu_{p}\tau_{p}=0.315$$
假设脉冲形状对应于双曲正割（参见表 2.1）。对于 $\Delta λ_p$ 使用 (2.45)，
$$\frac{\Delta\lambda_{\mathrm{p}}}{\lambda_0}=\frac{\Delta\nu_{\mathrm{p}}}{\nu_0}\quad\Rightarrow\quad \Delta\lambda_{\mathbf{p}}=\frac{\lambda_0}{\nu_0}\Delta\nu_{\mathbf{p}}=\frac{\lambda_0}{\nu_0}\frac{0.315}{\tau_{\mathbf{p}}}=0.315\frac{\lambda_0^2}c\frac1{\tau_{\mathbf{p}}}=0.13\mathrm{~nm}$$
由(2.86),
$$\tau_{\mathrm{p}}\left(L_{\mathrm{F}}\right)\approx D_{\lambda}L_{\mathrm{F}}\Delta\lambda_\mathrm{p} $$
中心波长为 1.55 um 情形, 色散系数 $D_\lambda =17\mathrm{\dfrac{ps}{km\cdot nm}}$

脉冲展宽近似为
$$\tau_{\mathrm{p}}\left(L_{\mathrm{F}}=5000\mathrm{~km}\right)\approx17\frac{\mathrm{p}\mathrm{s}}{\mathrm{km}\cdot\mathrm{nm}}\times5000\mathrm{~km}\times0.13\mathrm{~nm}\approx10.6\mathrm{~ns}$$

这意味着，<mark style="background: #FFF3A3A6;">在5000公里之后，脉冲展宽到远超过200 ps的脉冲长度，这比脉冲间隔还要长，即数字信息将完全丢失</mark>。

非线性过程尤其重要，因为<mark style="background: #FFF3A3A6;">非线性效应低强度时也会在长距离下累积</mark>。非线性效应会导致<mark style="background: #FF5582A6;">光谱展宽</mark>、<mark style="background: #FF5582A6;">脉冲群延迟波动</mark>等，并且相比线性色散, <mark style="background: #FFF3A3A6;">非线性效应下脉冲更快地发生扭曲</mark>。

现实中，传播大约 50-100 km 的距离后，光信号通常会通过电子手段在所谓中继器中检测提取出来, 并由激光二极管重新发射. 
- 中继器复杂、昂贵，且会随时间退化。
- 而且，比特率受到中继器的限制

孤子脉冲, 存在一些基本问题

扩大时分复用 (TDM) 也越来越具有挑战性，因为较高数据速率下的较短脉冲需要较窄的接收器时间窗口和较大的光带宽。

更长脉冲和相干通信的<mark style="background: #FF5582A6;">波分复用</mark>（WDM）
- 在 WDM 中，多个载波波长并行传输多个数据流，同时保持更长的脉冲持续时间和更适中的光带宽。 
- 信号基于相位而不是幅度调制，这也称为<mark style="background: #FF5582A6;">相干光通信</mark>。


## 2.5.8 脉冲在真空中的传播速度可以超过光速吗？

波动方程
$$\left(\frac\partial{\partial z^2}-\frac1{c^2}\frac\partial{\partial t^2}\right)E(z,t)=\mu_0\frac\partial{\partial t^2}P(z,t)$$

介质中极化强度
$$P(z,t)=\int_{-\infty}^t\chi\left(t-t^{\prime}\right)\varepsilon_0E\left(t^{\prime}\right)\mathrm{d}t^{\prime}$$
其中介电磁化率 $χ(t)$ 是因果函数，即 $t < 0$ 时 $χ(t) = 0$。

我们通过傅里叶变换求解（2.87），将其转化为一维亥姆霍兹方程，如第三节中所讨论的。
$$\tilde{E}(z,\omega)\equiv F\left\{E(z,t)\right\}=\int E(z,t)\mathrm{e}^{-\mathrm{i}\omega t}\mathrm{d}t$$
使用复的磁导率
$$\tilde{\chi}\left(\omega\right)=\int_0^\infty\chi\left(t\right)\mathrm{e}^{-\mathrm{i}\omega t}\mathrm{d}t$$
在频域中, 波数
$$k_n(\omega)=\pm\frac\omega cn(\omega)$$

复折射率 $\tilde{n}(ω)$ , 虚数的部分反映了介质对光的吸收.
$$\tilde{n}(\omega)=\sqrt{1+\tilde{\chi}(\omega)}\mathrm{~,~where~}\tilde{n}(\omega)\equiv\eta(\omega)-i\alpha(\omega)$$
如此, 亥姆霍兹方程的解为:
$$\tilde{E}(z,\omega)=\tilde{E}(0,\omega)\mathrm{e}^{-\mathrm{i}\boldsymbol{k}\tilde{\boldsymbol{n}}(\omega)z}=\tilde{E}(0,\omega)\mathrm{e}^{-\mathrm{i}\boldsymbol{k}\eta(\omega)z}\mathrm{e}^{-\boldsymbol{k}\boldsymbol{\alpha}(\omega)z}$$

考虑以下配置。电磁脉冲从半空间 z < 0 发送到厚度为 L 的介质上。该脉冲的一部分在第一个真空介质界面处反射。一部分渗透到介质中并穿过介质，直到到达第二介质-真空界面。一部分再次被反射，一部分最终离开介质。由于我们处理的是线性介质，我们当然可以确定每个频率分量的整个配置的传递函数并计算发射的脉冲。该传递函数考虑结构内的所有多重反射。这里，我们考虑一个简化的问题，我们考虑介质引起的折射率变化很小的情况忽略多次反射。通过这种近似，我们可以简化复折射率 (2.92)：

![[Pasted image 20231105002841.png]]
$$|\tilde{\chi}(\omega)|\ll1\Longrightarrow\tilde{n}(\omega)\approx1+\frac{\tilde{\chi}(\omega)}2 \tag{2.94}$$
高斯脉冲的最大值以群速度传播
$$\frac1{\upsilon_\mathrm{g}}=\frac{\mathrm{d}k_{\tilde{n}}}{\mathrm{d}\omega}=\frac{\mathrm{d}}{\mathrm{d}\omega}\left[\frac\omega c\tilde{n}(\omega)\right]\tag{2.95}$$

从经典色散理论 (洛伦兹模型) 中，我们还知道吸收线附近正频率的复磁化率的典型曲线：
$$\tilde{\chi}(\omega)=-2\mathrm{i\alpha}\frac1{1+\mathrm{i}(\omega-\omega_0)/\Delta\omega_\mathrm{a}}$$
其中 $α$ 与共振时每个波数的振幅衰减成正比，而 $ω_a$ 是吸收线的半高全宽。

图 2.18 和 2.19 显示了磁化率的实部和虚部随频率变化的曲线

![[Pasted image 20231105201557.png]]

图 2.18 描绘了给定吸收线宽的复数磁化率 $χ_r$ 的实部。

图 2.18 和 2.19 中的虚线显示了具有与吸收线相对应中心频率的高斯脉冲频谱。我们选择足够长的脉冲，频谱足够窄，使磁化率的实部近似为频率线性，虚部视为常数。通过上述近似并由 $ω − ω_0<< \Delta ω_\alpha$，我们得到式子(2.96)中的磁化率为
$$\boxed{\tilde{\chi}(\omega)\approx-2\mathrm{i}\alpha\left(1-\mathrm{i}\frac{\omega-\omega_0}{\Delta\omega_\mathrm{a}}\right)=-2\alpha\frac{\omega-\omega_0}{\Delta\omega_\mathrm{a}}-2\mathrm{i}\alpha}\tag{2.97}$$

通过 (2.94) 的近似，折射率的实部由 $n(\omega ) ≈ 1 + χ_r(ω)/2$ 确定，因此反群速度由 $χ_r(ω)$ (2.95) 的导数确定。

![[Pasted image 20231105203802.png]]

图 2.20 清楚地表明，我们可以轻松获得群速度的每个任意值，而不会违反我们所做的任何近似。群速度甚至可以变为负值。

由(2.94)
$$\tilde{n}(\omega)\approx1-\alpha\left(\frac{\omega-\omega_0}{\Delta\omega_a}\right)-\mathrm{i\alpha}$$

由 (2.95) 脉冲中心频率处的群速度由下式给出
$$\frac1{\upsilon_\mathrm{g}(\omega_0)}=\frac{\tilde{n}(\omega_0)}c+k\left.\frac{\mathrm{d}\tilde{n}}{\mathrm{d}\omega}\right|_{\omega=\omega_0}=\frac1c\left[\tilde{n}(\omega_0)-\alpha\frac{\omega_0}{\Delta\omega_\mathrm{a}}\right]\approx\frac1c\left(1-\alpha\frac{\omega_0}{\Delta\omega_\mathrm{a}}\right)$$
即
$$\upsilon_\mathrm{g}(\omega_0)\approx\frac c{1-\alpha\omega_0/\Delta\omega_\mathrm{a}}\tag{2.99}$$
对于(2.99)中的某些参数，我们可以得到 $υ_g(ω_0) > c$。

这是否意味着违反相对论？现在可以以超光速传输信息吗？答案是否定的，因为<mark style="background: #FFF3A3A6;">高斯脉冲是解析信号，即高斯脉冲的信息在空间的任何时刻都已经存在，并且已经可以通过泰勒级数展开在空间的任何地方完全重构</mark>。在传播期间，仅脉冲最大值发生偏移。为了更现实地处理传输速度，必须考虑因果电磁脉冲的传播，当 $t < 0$ 时，初始边界值 $E (z = 0, t) = 0$ 以及其他任意行为。该脉冲边缘不能以超光速传播。这个问题的数学处理比较复杂，这里就不展示了。


## 2.5.9 群系数的定义

我们希望定义一个有关群速度的参数---群系数, 类似于相速度与折射率的关系
$$v_p=\frac{c}{n(\omega )}$$
群系数与群速度的关系应有
$$v_g(\omega )\equiv \frac{c}{n_g}$$
于是
$$\frac{n_\mathrm{g}}c=\frac1{\upsilon_\mathrm{g}}=\frac{\mathrm{d}k_n}{\mathrm{d}\omega}=\frac{\mathrm{d}}{\mathrm{d}\omega}\left(\frac\omega cn(\omega)\right)=\frac{n(\omega)}c+\frac\omega c\frac{\mathrm{d}}{\mathrm{d}\omega}n(\omega)$$
所以群系数:
$$\boxed{n_\mathrm{g}=n+\omega\frac{\mathrm{d}n}{\mathrm{d}\omega}}\tag{2.101}$$
从群指数的定义和图 2.18 可以看出，共振吸收频率周围的群速度可以变得强烈依赖于频率，正或负，并且大于或小于光速。这允许在传播过程中用损失控制群速度的工程。用增益谐振代替吸收谐振解决了这个问题。这个例子表明我们可以将脉冲传播速度减慢到非常低的速度---慢光。

![[Pasted image 20231105201557.png]]

## 2.5.10 更高阶色散

超短脉冲的产生需要精确控制激光谐振腔以及后续系统中的色散和光谱带宽。虽然可以直接生成长度为 10-30 fs 的脉冲，但较短的脉冲会产生越来越多的困难。高阶色散的精确知识变得更加重要。因此，必须考虑泰勒展开式中的更高阶。

为了表征高阶色散，引入色散长度 $L_D$ 和 $L_D'$ 
$$L_\mathrm{D}\equiv\frac{\tau^2}{\left|k_n^{\prime\prime}\right|},\quad L_\mathrm{D}^{\prime}\equiv\frac{\tau^3}{\left|k_n^{\prime\prime\prime}\right|}\tag{2.102}$$
其中, $k_{n}''=\dfrac{\partial ^{2}k_{n}}{\partial \omega ^2}$, $k_{n}'''=\dfrac{\partial ^{3}k_{n}}{\partial \omega ^{3}}$. 更高阶的色散长度可类似的定义。

高斯脉冲的脉冲宽度 $\tau$ 为
$$E(t)\propto\exp\left(-\frac{t^2}{2\tau^2}\right)\Longrightarrow\tau_{\mathrm{p}}=2\sqrt{\ln2}\tau=1.665\tau $$
双曲正割函数脉冲 (sech pulse) 的脉冲宽度为
$$E(t)\propto\operatorname{sech}\left(\frac t\tau\right)\Longrightarrow\tau_{\mathrm{p}}=2\ln\left(1+\sqrt{2}\right)\tau=1.763\tau $$

如果我们比较由二阶色散引起的高斯脉冲的脉冲展宽，如（2.79）所示：
$$\frac{\tau_{\mathbf{p}}\left(L_{\mathbf{d}}\right)}{\tau_{\mathbf{p}}(0)}=\sqrt{1+\frac{\left(4\ln2k_{\mathbf{n}}^{\prime\prime}L_{\mathbf{d}}\right)^2}{\tau_{\mathbf{p}}^4(0)}}=\sqrt{1+\left(\frac{4\ln2\dfrac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}}{\tau_{\mathbf{p}}^2(0)}\right)^2}$$
代入二阶色散的色散长度, 我们有:
$$\frac{\tau_{\mathbf{p}}(z)}{\tau_{\mathbf{p}}(0)}=\sqrt{1+\left(\frac z{L_{\mathbf{D}}}\right)^2}$$
传播了色散长度 $L_D$ 后，带宽受限的高斯脉冲将展宽 $\sqrt{2}$ 倍

- 大多数情况下，与二阶色散相比，三阶色散可以忽略不计，即 $k_n(ω)$ 中泰勒展开式中的高阶项可以忽略不计。
- 三阶色散仅在 $L_D' ≤ L_D$ 或 $L_D'$ 与 $L_D$ 相当时才起作用。类似的论点也适用于更高阶的色散。
- 稍后将证明，即使对于 $≤ 30 fs$ 的脉冲生成，激光谐振腔内的三阶色散通常也开始发挥不可忽视的作用，并成为近红外光谱范围内亚 10 飞秒脉冲生成的主要限制。
- 三阶色散在光纤中也很重要，例如，当中心波长为 $1.32 μm$ 的光具有消失的二阶色散时，即 $|k_n''| \approx 0$。

对于 $z>>L_D$，以下近似对于高斯脉冲十分有效
$$\frac{\tau_{\mathfrak{p}}(z)}{\tau_{\mathfrak{p}}(0)}\approx z\sqrt{1+\frac1{L_{\mathrm{D}}^2}+\frac1{4{L_{\mathrm{D}}^{\prime}}^2}}$$
这描述了由于二阶和三阶色散引起的脉冲展宽。为了计算三阶色散，我们可以利用色散关系 $n(λ)$ 来数值计算得到三阶导数（见表2.3）。发现三阶色散为
$$\frac{\mathrm{d}^3\phi}{\mathrm{d}\omega^3}=-\frac{\lambda^4z}{4\pi^2c^3}\left(3\frac{\mathrm{d}^2n}{\mathrm{d}\lambda^2}+\lambda\frac{\mathrm{d}^3n}{\mathrm{d}\lambda^3}\right)$$
对于 1 cm 厚的熔融石英透镜，
$$\left.\frac{\mathrm{d}^3\boldsymbol{\phi}}{\mathrm{d}\omega^3}\right|_{\lambda_0=800\mathrm{~nm}}=2.74\times10^{-43}\mathrm{~s}^3=274\mathrm{~fs}^3$$

## 2.5.11 慢演化波近似

2.5.2 我们证明，在线性脉冲传播中，使用缓慢变化的包络近似（2.57）仅考虑脉冲包络 A(z, t) 的动力学是有用的。缓慢变化的包络近似在少周期状态下通常仍然有效，其中脉冲仅包含电磁波的几个周期。但是对于持续时间在一个或两个光周期范围内的脉冲会发生什么？对于如此短的脉冲，一阶包络方程 (2.60) 仍然有效吗？
$$\left|\frac{\partial^2\tilde{A}}{\partial z^2}\right|\ll\left|k_n(\omega_0)\frac{\partial\tilde{A}}{\partial z}\right|\quad\Rightarrow\quad \frac\partial{\partial z}\tilde{A}\left(z,\Delta\omega\right)+\mathrm{i}\Delta k_n\tilde{A}\left(z,\Delta\omega\right)=0$$

包络方程可以扩展到等于载波振荡周期 T 的脉冲持续时间，并且修改后的一阶包络方程的有效性也扩展到短至一个光周期 T 的脉冲持续时间。

<mark style="background: #FF5582A6;">缓慢演化波近似</mark>
$$\left|\partial_\xi E\right|\ll\beta_0\left|E\right|$$
- 它没有明确地对脉冲宽度施加限制

- 在缓慢演化波近似的框架中，非线性包络方程准确地描述了单周期状态下的光脉冲传播。



