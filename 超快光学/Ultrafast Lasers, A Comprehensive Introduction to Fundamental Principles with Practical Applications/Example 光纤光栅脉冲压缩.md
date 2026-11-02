
一束通过光纤传播的高斯脉冲经历自相位调制 (SPM) 并啁啾。因此，脉冲的相位与频率相关。我们可将高斯脉冲写为 (2.35) 式的形式:
$$A(t)=e^{-\Gamma _1t^2}e^{i\Gamma _{2}t^{2}}e^{i\omega _0t}=e^{-\Gamma t^2}e^{i\omega _0t}$$
其中, $\Gamma \equiv \Gamma _1-i\Gamma _2$ . 这里, $\Gamma _1$ 决定了脉冲宽度, $\Gamma _2$ 决定了脉冲的啁啾.

(a) 将脉冲转换到频域并将频谱归一化

(b) 现在我们在脉冲中引入二阶色散, 比如使用一个光栅对压缩器. 这一二阶色散可表示为频域上在脉冲上乘上一个相位因子. 如果 $A(\omega )$ 为 (a) 中获得的脉冲频域上的表达式, 我们可写为
$$A'(\omega )=A(\omega )e^{-iD_2(\omega _0-\omega )^2}$$
将新的 $\Gamma$ 表示为 $\Gamma _1$ , $\Gamma _2$ 和 $D_2$ 的函数

(c) 代入 $d=\dfrac{D_2}{\tau _0^2}$ , 以及 $\gamma =\dfrac{\Gamma _2}{\tau _0^2}$ , 求出并作出 $\dfrac{\tau _{\text{new}}^2}{\tau _0^2}$ 作为$d$ 和 $\gamma$ 的函数. 您期望使用哪种参数组合来实现脉冲压缩？

解:

(a)

自相位调制 SPM 可用一个非线性相移描述
$$\varphi_2(t)=-\delta |A(t)|^2$$
其中, $\delta$ 为 SPM 系数, 由 (4.5) 式给出. 脉冲
$$A(t)=e^{-\Gamma _1t^2}e^{i\Gamma _2t^2}e^{i\omega  _0t}=e^{-\Gamma _1t^2}e^{i\omega _0t}$$
FT:
$$\begin{align}
A(\omega )&= C\int_{-\infty}^{+\infty} e^{-\Gamma t^{2}}e^{-i\omega_{0} t} e^{-i\omega t} \mathrm{d}t\\
&=C\int_{-\infty}^{+\infty} \exp \left\{ -\Gamma \left[t^2-i\frac{\omega_{0} -\omega }{\Gamma }t+\left( 
 i\frac{\omega_{0} -\omega }{2\Gamma }\right)^2-\left(  i\frac{\omega_{0} -\omega }{2\Gamma }\right)^2\right] \right\}    \mathrm{d} t \\
 &=C\times \exp \left[ -\frac{(\omega_{0} -\omega )^{2}}{4\Gamma } \right]\int_{-\infty}^{+\infty} \exp \left[ -\Gamma \left( t-i\frac{\omega_{0} -\omega }{2\Gamma } \right)^2 \right] \mathrm{d} t\\ 
 &=C\times \exp \left[ -\frac{(\omega_{0} -\omega)^2 }{4\Gamma } \right]\sqrt{\frac{\pi }{\Gamma }}
\end{align}
 $$
其中, $C$ 为待确定常数, 作归一化:
$$A(\omega_{0} )=C\sqrt{\frac{\pi }{\Gamma }}=1 \implies C=\sqrt{\Gamma /\pi } , \quad A(\omega_{0} )=e^{(-\omega_{0} -\omega)^2/4\Gamma  }$$

(b) 我们有
$$A'(\omega )=A(\omega )e^{{-iD_2(\omega _0-\omega )^2}}e^{-(\omega_{0} -\omega )^{2}}e^{iD_{2}+1/4\Gamma }$$
因此, $\Gamma '$ 可由下式给出:
$$\dfrac{1}{4\Gamma '}=\dfrac{1}{4\Gamma }+iD_{2}$$
最后有:
$$\Gamma '=\dfrac{\Gamma }{1+i4\Gamma D_{2}}=\dfrac{\Gamma _{1}-i\Gamma _{2}}{1+i4\Gamma _{1}D_{2}+4\Gamma _{2}D_{2}}$$

(c) $\Gamma$ 的实部, 这里为 $\Gamma _1$ 由 (2.40) 定义了脉冲持续时间
$$\tau _{0}^{2}=\dfrac{2\ln 2}{\Gamma _1}$$
因此, 新的持续时间和 $\Gamma '$ 的实部相关, 此处表示为 $\Gamma _{1}$ , 由下式
$$\Gamma _{1}'=\dfrac{\Gamma _{1}}{(1+4\Gamma _{2}D_{2})^{2}+16\Gamma _{1}^{2}D
_{2}^{2}}$$
因此, 
$$\dfrac{\tau _{\text{new}}^{2}}{\tau _{0}^{2}}=(1+4\Gamma _{2}D_{2})^{2}+16\Gamma _{1}^{2}D_{2}^{2}=(1+4\gamma d)^{2}+(8d\ln 2)^{2}$$
这里我们使用了 $D_{2}=d\tau _{0}^{2}$ 以及 $\Gamma _2=\gamma /\tau _0^2$ . 对于确定的参数, 我们可以确定脉冲的压缩, 由 $\tau _{\text{new}}^{2}/\tau _{0}^{2}<1$ . 比如, 对于 $\gamma =-3$ 以及 $d\approx0.1$.


