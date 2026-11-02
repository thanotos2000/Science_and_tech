---
tags:
  - 光学/超快光学/色散补偿
---

# 3.1 介绍与目的

超短脉冲具有非常宽的光谱带宽，并且在传播过程中经历强烈的色散展宽。

仅 1 毫米的熔融石英即可将 5 fs 脉冲展宽至约 20 fs。即使在空气中传播也成为一个需要考虑的问题。因此，我们需要补偿这种脉冲展宽。

- 色散材料总是会展宽变换限制脉冲。
- 这个过程<mark style="background: #FFF3A3A6;">线性</mark>，可让光通过补偿相应色散的材料来再次取消脉冲展宽：瞬时移动的频率分量需要按正确的时间向后移动延迟---<mark style="background: #FFF3A3A6;">负色散</mark>。

- 透明区域的材料具有正色散。如果我们想避免巨大的损失，就必须寻找其他方法获得负色散。这可以通过“<mark style="background: #FFF3A3A6;">几何结构</mark>”实现。
- 利用折射或衍射产生的角色散使某些频率分量沿较长光路长度传播，如<mark style="background: #FF5582A6;">光栅对</mark>和<mark style="background: #FF5582A6;">棱镜对</mark>。条件 ---- 空间相干光束。
- 其他几何结构使用强烈波长依赖的干涉效应，例如 <mark style="background: #FF5582A6;">Gires-Tournois 干涉仪 (GTI)</mark> 和<mark style="background: #FF5582A6;">色散镜</mark>。


介质的折射率由 Sellmeier equation 给出:
$$n^2-1=\sum_k\frac{B_k\lambda^2}{\lambda^2-C_k}\tag{3.4}$$
不同材料具有不同的中心波长和系数.

- GDD是正色散还是负色散取决于 $\dfrac{d^2n}{d\omega ^2}$ 或 $\dfrac{d^2n}{d\lambda ^2}$ 的正负.

在 $600 nm$ 至 $1.1 μm$ 的波长范围内，玻璃、蓝宝石和石英、$CaF_2$ 或 $BaF_2$ 等其他透明介质几乎都表现出正色散。

根据第2章, 初始的变换极限高斯脉冲在二阶色散后获得线性调频的频率啁啾脉冲:
$$\omega(t)\equiv\frac{\mathrm{d}\phi_{\mathrm{tot}}(t)}{\mathrm{d}t}=\omega_0+2\Gamma_2t\tag{3.7}$$
其中, 由 (2.70) 
$$\frac1{\Gamma\left(L_{\mathrm{d}}\right)}=\frac1{\Gamma\left(0\right)}+2\mathrm{i}k_{\mathrm{n}}^{\prime}L_{\mathrm{d}}\mathrm{~,~}\quad\quad\Gamma\equiv\Gamma_{1}-\mathrm{i}\Gamma_{2}$$
因此, 传输一定距离后, 频率线性变化的斜率
$$\Gamma\left(L_{\mathrm{d}}\right)=\frac1{\frac1{\Gamma\left(0\right)}+2\mathrm{i}k_{n}^{\prime\prime}L_{\mathrm{d}}}=\frac{\frac1{\Gamma\left(0\right)}-2\mathrm{i}k_{n}^{\prime\prime}L_{\mathrm{d}}}{\left[\frac1{\Gamma\left(0\right)}\right]^{2}+\left(2k_{n}^{\prime\prime}L_{\mathrm{d}}\right)^{2}}\implies\Gamma_{2}\propto k_{n}^{\prime\prime}L_{\mathrm{d}}\tag{3.9}$$
可见:
- 正啁啾 ---- $k_n''>0$ , $\Gamma _2>0$
- 负啁啾 ---- $k_n''<0$ , $\Gamma _2<0$

脉冲在材料中色散, 会导致脉冲大幅度展宽.


# 3.2 棱镜压缩器 (棱镜对)

## 3.2.1 四棱镜压缩器的二阶色散

为了弥补这一点，我们需要负（反常）色散。



原理: 角色散或几何色散

- 斯涅尔定律中与波长相关的折射率会导致与角度相关的折射，从而导致折射光的角色散。
- 不同的频率分量沿着不同的几何路径传播。
- 由此产生的光路长度的频率依赖性会导致负色散。

器件: 棱镜对, 光栅对

对于棱镜色散补偿, 通常使用一对棱镜

- 第一个棱镜，不同波长频率分量沿不同方向传播：短波部分（“蓝色”）比长波部分（“红色”）折射更强烈。
- 第二个棱镜后，光束再次平行出射，但在横向上在空间上分离。
- 这种空间分离可通过向后反射光束或插入第二对棱镜来逆转（见图 3.4）。

最后，产生的路径长度差加倍，色散加倍。经过双路棱镜对后，实现负色散，即“蓝色比红色快”。

![[Pasted image 20231108002557.png]]

棱镜被切割成入射角为激光脉冲中心波长的布鲁斯特角 $θ_B$
- 布儒斯特角下, p-偏振光的反射损耗降至最低, 且在超短脉冲的光谱带宽内, 任何与中心波长略有不同的偏差会导致微小的损耗。
- 此外，可选择的顶角 $α$ 应适当选取, 从而得到入射角$θ_1$和出射角 $θ_2$ 相等的对称光路。具有相等入射角和出射角的对称光束路径总是确保最小的偏离角。这样我们可较容易获得, 要保持路径对称所需要的棱镜旋转角。

![[Pasted image 20231108004024.png]]

棱镜配置的总 GDD 可以通过移动棱镜来连续调整。在图 3.5 的底部图像中，这相当于向上或向下移动第一或第二棱镜。

注意:  将棱镜加入光路中，会引入正色散，因为光束必须传播通过较长的具有正色散的棱镜材料。

我们忽略棱镜的正色散计算棱镜的负色散.

斯涅尔公式:
$$n(\lambda)\sin\theta_2^{\prime}=\sin\theta_2\tag{3.10}$$
顶角
$$\alpha=180^\circ-\left(90^\circ-\theta_1^{\prime}\right)-\left(90^\circ-\theta_2^{\prime}\right)=\theta_1^{\prime}+\theta_2^{\prime}\tag{3.12}$$
选择入射角为 p-偏振脉冲中心波长 $λ_0$ 的布儒斯特角，反射率 $R_p (θ_B) = 0$，且棱镜布置具有最小偏差角。对于最小偏角 $δ_{min}$，通过棱镜的光束路径是对称的，具有相同的入射角和出射角，即 $θ_1(λ_0) = θ_B = θ_2(λ_0)$，其中 $θ_B$ 对应于中心波长 $λ_0$ 处的布鲁斯特角：
$$\tan\theta _\mathbf{B}=n(\lambda _{0}),\quad \theta _B+\theta_B'=\frac{\pi}{2} \tag{3.13}$$
因此我们得到了经过两倍路径后实现最小损耗的角度.

最小偏离角情形, $\theta _1'=\theta _2'$:
$$\alpha =2(\frac{\pi}{2}-\theta _B)=\pi -2\theta _B=\pi -2\theta _B\tag{3.14}$$

棱镜的出射角是独立于波长的, 因此对于任意波长, 我们都有一个固定的入射角 $\theta _1(\lambda )=\theta _B$ , 因此第一个棱镜的角色散
$$\theta _2(\lambda )=\arcsin(n\sin\theta _2')=\arcsin[n(\lambda )\sin(\pi-2\theta _B-\arcsin\frac{\sin\theta _B}{n(\lambda )})]\tag{3.15}$$

原则上, 我们现在可以通过计算路径长度作为波长的函数来表征光路的负色散. 存在一个更加"优雅"的计算方法:

其依赖于这样的一个事实: <mark style="background: #FFF3A3A6;">光学各向同性材料中的波前 (具有相同相位的点) 总是垂直于传播方向</mark>.

首先，我们考虑一个简单的特殊情况，对特定的参考波长，光束正好在两个棱镜的顶点上传播。此时，我们有纯的几何色散，并且可以忽略两棱镜中的材料色散。这种情况被称为棱镜配置的水平极限，因为它定义了最短波长，也称为水平波长 $λ_h$，它实际上可以穿过棱镜序列（见下图）。

![[Pasted image 20231110170834.png]]

![[Pasted image 20231110171536.png]]

两个顶点间距离 $\overline{CB}=L$ , 如上图, 是角度 $\beta$ 的参考线. 角度 $\beta$ 定义了比水平波长更长的波长的光束通过两个棱镜的传播路径. 

这一波长的相位前沿由 AC , BE 和 GH 给出. 我们无需花力气计算 CDEG 路径的光程, 只需计算 ABH 路径即可. 两次通过棱镜对后, 实际上与波长相关的光程只是 CDE 的两倍, 也就是 AB的两倍:
$$P=2\overline{CDE}|_{opt}=2\overline{AB}=2L\cos\beta \tag{3.16}$$
相应的相移:
$$\phi_P=kP(\lambda )=\frac{2\pi }{\lambda }P(\lambda )\tag{3.17}$$

我们忽略空气的色散, 四棱镜压缩器的二阶色散:
$$\boxed{\frac{\mathrm{d}^2\phi_\mathrm{P}}{\mathrm{d}\omega^2}=\frac{\lambda^3}{2\pi c^2}\frac{\mathrm{d}^2P}{\mathrm{d}\lambda^2}}\tag{3.18}$$

$P=P(\beta (n(\lambda )))$ , 所以
$$\frac{dP}{d\lambda }=\frac{\partial P}{\partial \beta }\frac{\partial \beta }{\partial n}\frac{\partial n}{\partial \lambda }$$ $$\frac{\mathrm{d}^2P}{\mathrm{d}\lambda^2}=\frac{\partial P}{\partial\beta}\left[\frac{\partial^2n}{\partial\lambda^2}\frac{\partial\beta}{\partial n}+\frac{\partial^2\beta}{\partial n^2}\left(\frac{\partial n}{\partial\lambda}\right)^2\right]+\left(\frac{\partial\beta}{\partial n}\frac{\partial n}{\partial\lambda}\right)^2\frac{\mathrm{d}^2P}{\mathrm{d}\beta^2}$$
由 (3.16):
$$\frac{\partial P}{\partial\beta}=-2L\sin\beta\:,\quad\frac{\mathrm{d}^2P}{\mathrm{d}\beta^2}=-2L\cos\beta \tag{3.23}$$
由上图, 明显, $\theta _2(\lambda )$ 与 $\beta$ 呈现负相关, 并且二者的和由棱镜的配置所确定.
$$\frac{\partial \beta }{\partial n}=-\frac{\partial \theta _{2}}{\partial n^{2}},\quad \frac{\partial ^2\beta }{\partial n^2}=-\frac{\partial ^2\theta _2}{\partial n^2}\tag{3.24}$$

对于所有波长和棱镜材料，进入棱镜对的入射角θ1是固定的
$$\frac{\partial }{\partial n}\sin\theta _1=0$$

(3.10) :
$$0=\frac{\partial }{\partial n}\sin\theta _1=\frac{\partial }{\partial n}(n\sin\theta _1')=\sin\theta _1'+n\cos\theta _1'\frac{\partial \theta _1'}{\partial n}\quad\Rightarrow\quad \tan\theta _1'=n\frac{\partial \theta _1'}{\partial n}$$

(3.12)
$$\alpha =\theta _1'+\theta _2'\quad\Rightarrow\quad \frac{\partial \theta _2'}{\partial n}=\frac{\partial }{\partial n}(\alpha -\theta _1')=-\frac{\partial \theta _1'}{\partial n}$$
(3.11) 斯涅耳公式
$$\sin\theta _2=n\sin\theta _2'\quad\Rightarrow\quad \cos\theta _2\frac{\partial \theta _2}{\partial n}=\sin\theta _2'+n\cos\theta _2'\frac{\partial \theta _2'}{\partial n}$$
联立上面三式可以解出.
$$\cos\theta_2\frac{\partial\theta_2}{\partial n}=\sin\theta_2'+\tan\theta_1'\cos\theta_2'$$

多数时候, 我们在$\beta$ 很小的情形下运行, 
$$\frac{\partial\theta_2}{\partial n}=\frac1{\cos\theta_2}\left(\sin\theta_2^{\prime}+\tan\theta_1^{\prime}\cos\theta_2^{\prime}\right)\tag{3.25}$$
$$\frac{\partial^2\theta_2}{\partial^2n}=\tan\theta_2\bigg(\frac{\partial\theta_2}{\partial n}\bigg)^2-\frac{\tan^2\theta_1'}n\bigg(\frac{\partial\theta_2}{\partial n}\bigg)\tag{3.26}$$

假设对于所有波长都有近似对称的光束路径, $\theta _1'(\lambda )\approx \theta _2'(\lambda )$ , 并且布儒斯特角 $\tan\theta _2=n$ , 上面两式可以化简:
$$\frac{\partial\beta}{\partial n}=-\frac{\partial\theta_2}{\partial n}\approx-2\:,\quad\frac{\partial^2\beta}{\partial n^2}=-\frac{\partial^2\theta_2}{\partial n^2}\approx-4n+\frac2{n^3}\tag{3.27}$$
这个近似值一般情形下可以很好地对应现实情形，但对于低于 20fs 的超短脉冲产生，应该使用精确的解.

综上, 代入P 的式子中, 我们最后得到:
$$\boxed{\begin{aligned}\frac{\mathrm{d}^2P}{\mathrm{d}\lambda^2}&=2\left[\frac{\partial^2n}{\partial\lambda^2}\left(\frac{\partial\theta_2}{\partial n}\right)+\left(\frac{\partial^2\theta_2}{\partial n^2}\right)\left(\frac{\partial n}{\partial\lambda}\right)^2\right]L\sin\beta-2\left(\frac{\partial\theta_2}{\partial n}\frac{\partial n}{\partial\lambda}\right)^2L\cos\beta\\&\approx4\left[\frac{\mathrm{d}^2n}{\mathrm{d}\lambda^2}+\left(2n-\frac{1}{n^3}\right)\left(\frac{\mathrm{d}n}{\mathrm{d}\lambda}\right)^2\right]L\sin\beta-8\left(\frac{\mathrm{d}n}{\mathrm{d}\lambda}\right)^2L\cos\beta\end{aligned}}\tag{3.19}$$
下面的约等于后对应了上面提到的近似, 第一行右边是精确解.

- 目前为止，该计算对于参考光束穿过棱镜顶点的情况是有效的。
- 当然，在实践中，所有光束都必须与顶点保持一定的距离，以最大限度地减少衍射损失。
- 事实上，图3.6中的h必须至少是光谱加宽光束半径的1.5倍，这样高斯光束中大约99%的功率才能通过棱镜（见以下注释）。

在z方向上传播的高斯光束可以用傍轴近似中的抛物线来近似。高斯脉冲的强度
$$I\left(\rho,z\right)=I_0\left[\frac{w_0}{w(z)}\right]^2\exp\left[-\frac{2\rho^2}{w^2(z)}\right]$$
其中,
- $\rho ^2=x^2+y^2$ ;
- $\omega _0$ : 束腰;
- $\omega (z)$ : 光束半径

高斯光束的功率 (空间上对截面积求积分):
$$P=\int_0^\infty I\left(\rho,z\right)2\pi\rho\mathrm{d}\rho=\frac12\pi w_0^2I_0\implies I_0=\frac{2P}{\pi w_0^2}$$
换掉 $I_0$
$$I\left(\rho,z\right)=\frac{2P}{\pi w^2(z)}\exp\left[-\frac{2\rho^2}{w^2(z)}\right]$$
半径为 $ρ_0$ 的圆形区域内的功率与总功率的比值由下式给出
$$\frac{P\left(\rho\leq\rho_0\right)}P=\frac1P\int_0^{\rho_0}I\left(\rho,z\right)2\pi\rho\mathrm{d}\rho=1-\exp\left[-\frac{2\rho_0^2}{w^2(z)}\right]$$
如此,
$$\frac{P\left(\rho\leq1.5w(z)\right)}P\approx99\%$$

四棱镜系统的二阶色散随距离 L 成线性下降:

![[Pasted image 20231110183452.png]]

## 3.2.2 四棱镜压缩器的三阶色散

四棱镜压缩器的三阶色散:
$$\boxed{\frac{\mathrm{d}^3\phi_\mathrm{P}}{\mathrm{d}\omega^3}=\frac{-\lambda^4}{4\pi^2c^3}\left(3\frac{\mathrm{d}^2P}{\mathrm{d}\lambda^2}+\lambda\frac{\mathrm{d}^3P}{\mathrm{d}\lambda^3}\right)}\tag{3.28}$$

同样地, 类似上一节我们可以做近似:
$$\boxed{\frac{\mathrm{d}^3P}{\mathrm{d}\lambda^3}\approx4\frac{\mathrm{d}^3n}{\mathrm{d}\lambda^3}L\sin\beta-24\frac{\mathrm{d}n}{\mathrm{d}\lambda}\frac{\mathrm{d}^2n}{\mathrm{d}\lambda^2}L\cos\beta}\tag{3.29}$$

四棱镜系统的三阶色散如下图:

![[Pasted image 20231110184203.png]]

## 四棱镜系色散的连续调节

棱镜压缩器的最大优点: 可以连续调节色散，不引入光束的空间偏移。

为此，让棱镜沿着x轴方向移动一段距离 $\Delta x$ 的距离，这决定了通过棱镜的光束路径，如图3.9所示。

![[Pasted image 20231110185221.png]]

还是从下面这幅图可以看出，在棱镜配置为最小偏差的情况下，当我们垂直于直线DE平移第二棱镜时，我们可以在不改变角度的情况下获得更大的“插入”到第二棱镜中（即，更大的距离 $h=\overline{BE}$ ）。因此，可以添加一定量额外的正色散材料并且这可以通过插入棱镜来调节（参见下面的推导）：

![[Pasted image 20231110171536.png]]

还是由图 (3.9)

![[Pasted image 20231110185221.png]]

由 (3.14):
$$\frac{\alpha }{2}=90°-\theta _B=\xi\Longrightarrow a=\Delta x$$
角 $\gamma$ 有:
$$\gamma =90 ^{\circ}-\theta _B'-\xi=2\theta_\mathrm{B}-90^\circ $$
$$ \Rightarrow  \sin \gamma = \sin (2\theta _B-90^\circ)= -\cos  (2\theta _B)=-1+2 \sin ^{2}\theta _B$$
又由上图
$$ \sin \gamma= \frac{h-\Delta x}{a}=\frac{h-\Delta x}{\Delta x}$$
所以:
$$-\Delta x+2\Delta x  \sin ^{2}\theta _{B}=h-\Delta  x$$
所以最后有:
$$\boxed{h(\Delta x)=2\Delta x\sin^2\theta} \tag{3.30}$$


对第一个棱镜也同样适用. 

这样做, 两棱镜之间的距离就会发生变化. 不过这通常可以忽略, 因为棱镜间的距离往往大于10cm, 而棱镜只在 mm 量级上发生小的位移.

相对于角度 $\alpha$ 而言, h 可以很容易地在实验上改变. h和α有关系:
$$\cos \frac{\alpha }{2}=\frac{h}{s}$$
 其中, $s=\overline{DB}$ .

再由几何原理, 考虑三角形 $\triangle BCD$ 内, 
$$\frac{\sin\angle BDC}{\overline{BC}}=\frac{\sin\angle BCD}{\overline{BD}} \Rightarrow \frac{L}{\sin(\theta _2+\pi/2)}=\frac{s}{\sin \beta } \Rightarrow s=L\frac{\sin \beta }{\cos \theta _2}$$

代入前面, 有:
$$ \boxed{\sin \beta =\frac{h}{L}\frac{ \cos \theta_{2}}{ \cos (\alpha /2)}}\tag{3.33}$$

超快激光器中，棱镜压缩器常用于色散补偿。
- 在环形腔中，可使用四棱镜压缩器，如图 3.10a ，用于碰撞脉冲锁模（CPM）染料激光器（详见第9章）。
- 在线性腔中，常使用两棱镜压缩器，如果可能的话，在线性腔的相对端选择输出耦合器。否则，必须使用附加的棱镜对序列来获得空间相干光束。

![[Pasted image 20231129164523.png]]

图 3.10b 展现了这样一种激光器，其中棱镜用于补偿钛宝石激光晶体中的正色散。为了最小化在 800nm 的中心波长处的三阶色散，通常用熔融石英为棱镜材料。对长于 20 到 30fs 的脉冲的脉冲生成，通常使用 SF10 玻璃，因为这种玻璃具有更强的色散，并且棱镜间隔可以选择得更小。这导致了更紧凑的激光腔。稍后我们将看到，原则上，人们总是使用小的负二阶色散来满足稳定孤子脉冲的条件。

通常只能补偿一种阶次的色散，如二阶色散。对于超短脉冲生成，未补偿的高阶色散导致脉冲加宽, 限制了脉冲长度。图 3.11 显示了具有不同第二棱镜插入 h（如图3.9所示）的 50 cm 顶点间距的熔融二氧化硅-布鲁斯特对的 GDD 。

![[Pasted image 20231129170105.png]]

假设切割棱镜，并根据设计波长 $λ_B=800  \text{nm}$ 的布鲁斯特条件选择入射角。顶点的位置是为特定水平波长 $λ_h$ 的无限细光线确定的。任何波长 $λ<λ_h$ 都不会被第二个棱镜折射，并且在通过棱镜对的传播过程中会丢失。插入第二个棱镜越大，即图 3.9 中的 h 越大，地平线波长 $λ_h$ 越短。但代价是，随着地平线波长的缩短，引入了更多的正色散（见图 3.11 和 3.12）。请注意，对于 $λ>λ_h$ ，较大直径的光束已经被剪裁，这通常必须考虑在内。图3.11和3.12显示了不同材料单次通过棱镜对的波长相关 GDD。对称四棱镜压缩器的色散加倍，或者等效地，通过两棱镜序列的往返。

![[Pasted image 20231129170637.png]]


# 3.3 光栅压缩器, 拉伸器和脉冲整形

## 3.3.1 色散光栅压缩器

### 光栅压缩器原理

可以使用<mark style="background: #FF5582A6;">光栅对</mark>引入角色散, <mark style="background: #FFF3A3A6;">长波 (红光) 成份相较短波 (蓝紫光) 走的距离更长, 从而引入负 GDD</mark>. <mark style="background: #FFF3A3A6;">通过调节光栅对的间距可以轻易调节色散大小.</mark>

![[Pasted image 20231129195252.png]]

光栅衍射的角色散:
$$\nu_{x,m}=m\frac1\Lambda\iff\theta_{x,m}\approx m\frac\lambda\Lambda \tag{3.34}$$
其中, $\Lambda$ 为光栅周期, $\lambda$ 为波长, $m$ 为衍射级次, $v_{x,m}$ 为空间频率, $\theta _{x,m}$ 为衍射角.

<mark style="background: #FFF3A3A6;">当我们通过这样的光栅, 棱镜等角色散元件传播短脉冲时，我们也会在脉冲前沿引入倾斜</mark>（见图3.14）。

![[Pasted image 20231129201942.png]]

因此，是脉冲前沿而不是相位前沿, 为脉冲峰值处恒定强度的轮廓。注意，相位前沿仍然垂直于脉冲传播方向。该脉冲前沿倾斜
$$\tan\alpha _{t}=\lambda _{0}\left.\frac{d\phi}{d\lambda }\right|_{\lambda_{0}}$$

在Littrow配置中，衍射光束沿着与入射光束相同的方向传播，光栅可以被设计为具有一阶（水平偏振）的最大衍射效率。因此，第一衍射级的光栅方程简化为
$$ \sin \phi =\frac{\lambda }{\Lambda }$$
其中, $\phi =\theta$ 为衍射角, 它是波长的函数, 这里使用了图3.14和注释 [99Pre] 的标记.

这种脉冲前沿倾斜对非线性频率转换中的群速度匹配非常有用。在和频生成中使用这种倾斜的脉冲前沿与非共线几何结构相结合，产生了新的世界纪录的深紫外生成，例如[20Wil]。

光栅压缩器对相位具有一个与位置相关的贡献。
- 这种贡献在第一光栅上可忽略，因为光束没在光谱上分散，所有频率分量经历相同的相移，因此对GDD可忽略。
- 但第二个光栅不同，这时, 光束按光谱分散 ---- 脉冲不同频率成分在光栅不同位置衍射 ---- 位置相关的光栅相位 ---- 频率相关的相位 ---- GDD。

根据惠更斯原理, 衍射波前的结构见图 3.15。

![[Pasted image 20231129204429.png]]

在图3.15中，<mark style="background: #FFF3A3A6;">第一光栅阶波前是由来自每条光栅线的所有二次波的相长干涉产生的。我们获得了与光栅线距离的相长干涉，与相邻的光栅线相比，该干涉导致 2π 位移的二次波前。</mark>因此, 当在相位图中评估两个光栅配置时，必须考虑这种光栅产生的相位。

有一种方法可避免这种复杂性。考虑到, 光栅相位对光栅序列中的群延迟没有影响。如果将光栅压缩器中的光路长度解释为群延迟，而不是相位延迟，那么仅使用ω中的一阶导数就可以更容易地计算相关的二阶色散。

设光束的入射角为 $θi$，被光栅衍射，光栅周期为 $\Lambda$。得到的反射和衍射光束（ $m$ 级）由衍射角 $θ_m$ 确定，如图 3.17 ，由(3.34) ：
$$\sin\theta _m=m\frac{\lambda }{\Lambda }+ \sin \theta _{i},\quad \text{where}\quad m=0,\pm1,\pm2,\cdots \tag{3.36}$$

![[Pasted image 20231129205500.png]]

- 考虑 $m = 0$ ， $θ_m = θ_i$，这对应平面上反射的情形，这时 $θ_m$ 对于所有波长都相同。
- 说明: 若衍射角 $θ_m$ 与入射角 $θ_i$ 位于 z 轴的同一侧，我们将其定义为负值。

对二阶色散，无论使用正一阶还是负一阶来操作光栅都没有任何区别，但<mark style="background: #FFF3A3A6;">实践中总是使用负一阶, 因为可以使用更高的衍射角，从而允许具有更大线数的光栅</mark>。

![[Pasted image 20231129195252.png]]

如图 3.13 ，例如，选择 $θ_i$ 为 45°时，正一阶的最大可能衍射角也仅为 45°。衍射光束是切向的。然而，在向后方向上，在光束变为相切之前，可能会形成 135° 的角度。

- 光栅压缩器通常采用近似 Littrow 配置。即，光束被衍射回其发出的方向。这样可制造非常高效的光栅，且通常闪耀光栅针对这种情况进行了精确优化。
- 一般, 为了光栅中的损耗最低，通常用<mark style="background: #FF5582A6;">闪耀光栅</mark>，因为这种光栅可优化一特定衍射级的衍射效率。由前面, 通常选择衍射级 $m=-1$ 的闪耀光栅。
- 低衍射损耗至关重要，因为光要在光栅衍射四次才能再次获得与波长无关的光束轮廓 (空间相干光束)（见图 3.16）。

![[Pasted image 20231129211022.png]]

我们可得出由于光栅对而导致的频率相关相移。该相移由两部分组成：
- 第一部分是几何色散 (3.37)
- 第二部分是光栅相位 $φ_g(x)$（3.38）

![[Pasted image 20231129205500.png]]

(1) 根据图 3.17，光通过光栅对的路径
$$L=\overline{PABQ}=\overline{P'A}+b=b\Big[1+\cos{(\theta_m+\theta_i)}\Big]=\frac{L_g}{\cos{\theta_m}}\Big[1+\cos{(\theta_m+\theta_i)}\Big]\tag{3.37}$$

(2) 平面 $z = L_g$ 中第二个光栅的衍射会产生与位置 $x$ 和波长 $λ$ 相关的相移 $\phi_g(x)$（见图 3.17）：
$$\phi_{g}(x)=\pi-m\frac{2\pi}\Lambda x \tag{3.38}$$
其中, $x$ 由于衍射角 $θ_m$ (3.36) 与 $λ$ 相关，因此 $x$ 与 $λ$ 相关。

这两个部分对光栅对处的总波长相关相移做出贡献：
$$\phi =\frac{\omega }{c}L+\phi _g(x),\quad x=L_{g}\tan \theta _{m}\tag{3.39}$$

这里我们忽略了棱镜间的所有材料色散，即群速度 $v_g=c$ 。这通常合理因为光栅对一般在空气乃至真空中运行。对四光栅压缩器的二阶色散, $m =−1$，
$$\boxed{\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}=-\frac{m^{2}\lambda^3L_\mathrm{g}}{2\pi c^2\Lambda^2}\left[1-\left(-m\frac\lambda\Lambda-\sin\theta_\mathrm{i}\right)^2\right]^{-3/2}}\tag{3.40}$$

![[Pasted image 20231129221325.png]]

如果脉冲最初已被色散材料展宽（GDD > 0），则四光栅压缩器可以再次压缩脉冲。色散可以通过两个平行光栅之间的距离 $Lg$ 连续调节，如式（3.40）所示（见图3.18）：
$$\frac{d^2\phi }{d\omega ^{2}}\propto L_{g}\tag{3.41}$$
光栅对的三阶色散, 考虑衍射级次 $m=-1$:
$$\boxed{\frac{\mathrm{d}^3\phi}{\mathrm{d}\omega^3}=-\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}\dfrac{3\lambda}{\pi c}\frac{1+\dfrac\lambda\Lambda\sin\theta_\mathrm{i}-\sin^2\theta_\mathrm{i}}{1-\left(\dfrac\lambda\Lambda-\sin\theta_\mathrm{i}\right)^2}}\tag{3.42}$$

$$\frac{d^{3}\phi}{d\omega ^3}\propto L_g$$

### 相关计算 1 

光栅对压缩器的相位和光线路径长度 L 的群延迟色散之间存在有用的关系

群延迟定义:
$$T_g\equiv \frac{L}{c}$$
其中, $L$ 是光线路径长度.

因此群延迟色散 $D_2$ (i.e. 二阶色散) 为
$$D_{2}=\frac{dT_{g}}{d\omega }=\frac{d}{d\omega }(\frac{L}{c}) =\frac{1}{c}\dfrac{dL}{d\omega}$$
我们可以证明: 
$$\boxed{-\frac{\omega }{c}\dfrac{dL}{d\omega}=\dfrac{d\phi _{g}}{d\omega}}\tag{3.44}$$
其中, $\phi _g$ 为光栅相位.

证明如下:

光学路径长度由 (3.37) , 
$$L=\frac{L_g}{\cos{\theta_m}}\Big[1+\cos{(\theta_m+\theta_i)}\Big]\tag{3.37}$$
由图 (3.17), 注意到:  $b=\dfrac{L_{g}}{ \cos \theta _{m}}$ 

![[Pasted image 20231129205500.png]]

所以有
$$\frac{\mathrm{d}}{\mathrm{d}\omega}b=\frac{L_\mathrm{g}}{\cos^2\theta_m}\sin\theta_m\frac{\mathrm{d}}{\mathrm{d}\omega}\theta_m=b\tan\theta_m\frac{\mathrm{d}}{\mathrm{d}\omega}\theta_m$$
$$\begin{aligned}\frac{\mathrm{d}}{\mathrm{d}\omega}L&=\frac{\mathrm{d}b}{\mathrm{d}\omega}\big[1+\cos\left(\theta_m+\theta_\mathrm{i}\right)\big]-b\bigg[\sin\left(\theta_m+\theta_\mathrm{i}\right)\frac{\mathrm{d}\theta_m}{\mathrm{d}\omega}\bigg]\\&=b\tan\theta_m\frac{\mathrm{d}\theta_m}{\mathrm{d}\omega}\bigg[1+\cos\left(\theta_m+\theta_\mathrm{i}\right)\bigg]-b\sin\left(\theta_m+\theta_\mathrm{i}\right)\frac{\mathrm{d}\theta_m}{\mathrm{d}\omega}\\&=b\frac{\mathrm{d}\theta_m}{\mathrm{d}\omega}\bigg[\tan\theta_m\big[1+\cos\left(\theta_m+\theta_\mathrm{i}\right)\bigg]-\sin\left(\theta_m+\theta_\mathrm{i}\right)\bigg]\end{aligned} \tag{3.45}$$

由 (3.36) $\sin\theta _m=m\dfrac{\lambda }{\Lambda }+ \sin \theta _i$ , 利用 $\lambda =\dfrac{2\pi c}{\omega }$ , 我们有:
$$\dfrac{d}{d\omega }( \sin \theta _m)=\dfrac{d}{d\omega}( \sin \theta _{m}- \sin \theta _{i})=\dfrac{d}{d\omega}(m\dfrac{\lambda }{\Lambda })=\dfrac{d}{d\omega}\left(\dfrac{2\pi mc}{\omega \Lambda }\right)=-\dfrac{2\pi mc}{\omega^2 \Lambda }$$
其中, $\sin \theta_i$ 是入射角与频率无关, 因此,
$$\dfrac{d}{d\omega}( \sin \theta _m)= \cos \theta _m\dfrac{d\theta _m}{d\omega }=-\dfrac{2\pi mc}{\omega ^2\Lambda }$$
所以,
$$\dfrac{d\theta _m}{d\omega}=-\dfrac{2\pi mc}{\omega ^{2}\Lambda  \cos \theta _{m}}\tag{3.46}$$
将其代入 (3.45)
$$\begin{aligned}\frac{\mathrm{d}}{\mathrm{d}\omega}L&=-\frac{2\pi mc}{\omega^2A\cos\theta_m}b\bigg[\frac{\sin\theta_m}{\cos\theta_m}\bigg[1+(\cos\theta_m\cos\theta_i-\sin\theta_m\sin\theta_i)\bigg]\\&\quad-(\sin\theta_i\cos\theta_m+\sin\theta_m\cos\theta_i)\bigg]\\&=-\frac{2\pi mc}{\omega^2A\cos\theta_m}b\frac{\sin\theta_m-\sin^2\theta_m\sin\theta_i-\sin\theta_i\cos^2\theta_m}{\cos\theta_m}\\&=-\frac{2\pi mc}{\omega^2A\cos^2\theta_m}b(\sin\theta_m-\sin\theta_i)\\&=-\frac{2\pi mc}{\omega^2A\cos^2\theta_m}\frac{L_\mathrm{g}}{\cos\theta_m}\frac{2\pi mc}{\omega A}=-\frac{(2\pi mc)^2}{\omega^3A^2\cos^3\theta_m}L_\mathrm{g}\:.\end{aligned}\tag{3.47}$$

光栅相位 $\phi _{g}$ 为
$$\phi _g=\pi -2\pi Nm =\pi -2\pi \frac{x}{\Lambda }m=\pi -2\pi m\frac{L_g}{\Lambda }\tan \theta _m $$

它的微分
$$\dfrac{d}{d\omega}\phi _g=-\frac{2\pi m}{\Lambda  \cos ^2\theta _m}L_g\frac{d\theta _m}{d\omega }$$
代入 (3.46), 有:
$$\dfrac{d}{d\omega}\phi _g=\frac{1}{c}\frac{(2\pi mc)^2}{\omega ^2\Lambda ^2 \cos ^3\theta _m}L_{g}\tag{3.48}$$
与 (3.47) 对比, 有:
$$-\frac{\omega }{c}\dfrac{d}{d\omega}L=\dfrac{d}{d\omega}\phi _g$$

有两种方式得到二阶色散是等价的.

### 相关计算2 光栅对压缩器的二阶色散推导

光学相位:
$$\phi =\frac{\omega }{c}L+\phi _g$$
 一阶色散:
 $$\dfrac{d}{d\omega}\phi =\frac{1}{c}L+\frac{\omega }{c}\frac{dL}{d\omega }+\dfrac{d\phi _g}{d\omega}\tag{3.49}$$
(3.44) 
$$\boxed{-\frac{\omega }{c}\dfrac{dL}{d\omega}=\dfrac{d\phi _{g}}{d\omega}}\tag{3.44}$$ 所以, 一阶色散
$$\dfrac{d}{d\omega}\phi =\frac{L}{c}$$
 二阶色散
$$\frac{\mathrm{d}^2}{\mathrm{d}\omega^2}\phi=\frac2c\frac{\mathrm{d}L}{\mathrm{d}\omega}+\frac\omega c\frac{\mathrm{d}^2L}{\mathrm{d}\omega^2}+\frac{\mathrm{d}^2\phi_\mathrm{g}}{\mathrm{d}\omega^2}\tag{3.50}$$
由 (3.47)
$$\frac{\mathrm{d}}{\mathrm{d}\omega}L=-\frac{(2\pi mc)^2}{\omega^3A^2\cos^3\theta_m}L_\mathrm{g}\tag{3.47}$$
再求导,
$$\frac{\mathrm{d}^2}{\mathrm{d}\omega^2}L=\frac{3\left(2\pi mc\right)^2L_\mathrm{g}}{\omega^4\Lambda^2\cos^3\theta_m}-\frac{3\left(2\pi mc\right)^2L_\mathrm{g}}{\omega^3\Lambda^2\cos^4\theta_m}\sin\theta_m\frac{\mathrm{d}\theta_m}{\mathrm{d}\omega}\tag{3.51}$$

对 (3.48) 式:  $\dfrac{d}{d\omega}\phi _g=\dfrac{1}{c}\dfrac{(2\pi mc)^2}{\omega ^2\Lambda ^2 \cos ^3\theta _m}L_{g}\tag{3.48}$  再求导,
$$\frac{\mathrm{d}^2}{\mathrm{d}\omega^2}\phi_\mathrm{g}=-\frac1c\frac{2\left(2\pi mc\right)^2L_\mathrm{g}}{\omega^3\Lambda^2\cos^3\theta_m}+\frac1c\frac{3\left(2\pi mc\right)^2L_\mathrm{g}}{\omega^2\Lambda^2\cos^4\theta_m}\sin\theta_m\frac{\mathrm{d}\theta_m}{\mathrm{d}\omega}\tag{3.52}$$

将 (3.47), (3.51), (3.52) 代入 (3.50) 中, 有:
$$\begin{aligned}\frac{\mathrm{d}^2}{\mathrm{d}\omega^2}\phi&=\frac{2}{c}\left[-\frac{(2\pi mc)^2L_\mathrm{g}}{\omega^3\Lambda^2\cos^3\theta_m}\right]+\frac{\omega}{c}\left[\frac{3\left(2\pi mc\right)^2L_\mathrm{g}}{\omega^4\Lambda^2\cos^3\theta_m}-\frac{3\left(2\pi mc\right)^2L_\mathrm{g}}{\omega^3\Lambda^2\cos^4\theta_m}\sin\theta_m\frac{\mathrm{d}\theta_m}{\mathrm{d}\omega}\right]\\&\quad -\frac{1}{c}\frac{2\left(2\pi mc\right)^2L_\mathrm{g}}{\omega^3\Lambda^2\cos^3\theta_m}+\frac{1}{c}\frac{3\left(2\pi mc\right)^2L_\mathrm{g}}{\omega^2\Lambda^2\cos^4\theta_m}\sin\theta_m\frac{\mathrm{d}\theta_m}{\mathrm{d}\omega}\\&=-\frac{1}{c}\frac{\left(2\pi mc\right)^2L_\mathrm{g}}{\omega^3\Lambda^2\cos^3\theta_m}\:.\end{aligned}\tag{3.53}$$
将式子 (3.53) 中的 $\cos \theta _m$ 换掉, 由 $\sin\theta _m=m\dfrac{\lambda }{\Lambda }+ \sin \theta _i$ ,
$$\cos\theta _m=\sqrt{1- \sin^2 \theta _m}
=\sqrt{1-(m\dfrac{\lambda }{\Lambda }+ \sin \theta _i)^2}$$
代入 (3.53) , 并用 $\omega  =\dfrac{2\pi c}{\lambda }$ 换掉 $\omega$, 最后
$$\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}=-\frac{m^2\lambda^3L_\mathrm{g}}{2\pi c^2\Lambda^2}\left[1-\left(-m\frac\lambda\Lambda-\sin\theta_\mathrm{i}\right)^2\right]^{-3/2}\tag{3.54}$$
这是光线单次通过光栅对发生的群延迟色散, 对于通过两次光栅对, 我们可以对上式乘2. 最终我们得到了 (3.40) 式.

一个更快速的推导是使用 (3.44) 代入 (3.49), 
$$\frac{\mathrm{d}\phi}{\mathrm{d}\omega}=\frac Lc,\quad\quad\quad\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}=\frac1c\frac{\mathrm{d}L}{\mathrm{d}\omega}\tag{3.55}$$
由 (3.47):  $\dfrac{d}{d\omega}L=-\dfrac{(2\pi mc)^2}{\omega ^3\Lambda ^2 \cos ^3\theta _m}L_g$ 
$$\dfrac{d^{2}}{d\omega^{2}}\phi=\frac{1}{c}\dfrac{dL}{d\omega}=-\dfrac{1}{c}\dfrac{(2\pi mc)^2}{\omega ^3\Lambda ^2 \cos ^3\theta _m}L_g$$

### 相关计算3 光栅对的三阶色散推导

此处略.


## 3.3.2 将光栅对转换为一个拉伸器

图 3.19 显示了一个更加复杂的光栅对配置, 其中<mark style="background: #FFF3A3A6;">引入了一对共焦系统</mark>. 凸透镜之间距离为 $2f$ , 并且相距两个光栅的距离都为 $L$ .

![[Pasted image 20231201164738.png]]

- $L<f$，该系统为正色散拉伸器；
- $L>f$，该系统为负色散拉伸器.
- $L=f$ 情形用于脉冲整形器.（见图3.21和下一节的讨论)[92Wei2]。

说明: 对于具有宽光谱的超短脉冲，聚焦元件是球面或柱面镜而不是透镜，以避免引入额外的正色散。

四光栅压缩器的 GDD 由 (3.40) 为
$$\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}=-\frac{m^2\lambda^3L_\mathrm{g}}{2\pi c^2\Lambda^2}\left[1-\left(-m\frac\lambda\Lambda-\sin\theta_\mathrm{i}\right)^2\right]^{-3/2}$$
显然前面的系数 $\lambda$ 等都是正的

考虑 (3.36) 式 : 
$$\sin\theta _m=m\frac{\lambda }{\Lambda }+ \sin \theta _{i},\quad \text{where}\quad m=0,\pm1,\pm2,\cdots \tag{3.36}$$
可化为
$$\left[1-\left(\frac{\lambda }{\Lambda} - \sin \theta _{i}\right)^{2}\right]^{1/2}= \cos \theta _{m},\quad \theta _{m}\in[-\pi /2,\pi /2]$$
 (3.40) 右边中阔内也为正, 所以四光栅压缩器的二阶色散 GDD 为负.

同理由 (3.42) 
$$\frac{\mathrm{d}^3\phi}{\mathrm{d}\omega^3}=-\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}\dfrac{3\lambda}{\pi c}\frac{1+\dfrac\lambda\Lambda\sin\theta_\mathrm{i}-\sin^2\theta_\mathrm{i}}{1-\left(\dfrac\lambda\Lambda-\sin\theta_\mathrm{i}\right)^2}$$
可见, 对于四光栅对的三阶色散为正.

接下来我们将看到如何<mark style="background: #FFF3A3A6;">从光栅排列中实现负光栅分离，从而翻转GDD的符号获得正GDD</mark>。这对啁啾脉冲放大十分重要，因为放大前需要大量可调节的正色散展宽脉冲，以防止任何材料损坏。

我们参考Martinez的论文，他推导了考虑衍射和折射的光栅压缩器的GDD。我们只需要对双光栅进行计算，由图 (3.17)
$$\frac{\mathrm{d}^2P}{\mathrm{d}\lambda^2}=\left[\frac{\mathrm{d}^2n}{\mathrm{d}\lambda^2}-n\left(\frac{\mathrm{d}\theta}{\mathrm{d}\lambda}\right)^2\right]L$$

![[Pasted image 20231129205500.png]]

在这里, $L=\overline{AB}$ 而不是前面的 $\overline{PABQ}$ .

在图 3.17 的配置中, 因为只存在在空气或真空中的衍射，在该系统中不存在材料色散, 上式可化为:
$$\dfrac{d^2P}{d\lambda ^2}=-\left(\frac{d\theta }{d\lambda }\right)^2L$$

现在，我们想修改一照上面所述的情况下的方程. 我们将一对共焦透镜放置在两个光栅之间, 如图3.19所示。

![[Pasted image 20231201164738.png]]

考虑到光束路径中额外的共焦系统，只需进行两次修改：

(1) 光栅的角色散被透镜的角放大率放大。透镜的角放大率由下式给出
$$M=\dfrac{f_1}{f_2}\tag{3.61}$$

(2) 由于所有光线的光程在透镜的两个焦平面间是相同的，所以这部分几何路径对GDD没有贡献。这导致通过压缩器在加入透镜对后的有效路径长度要减去两个焦平面的长度
$$L_{\text{eff}}=L-2(f_1+f_2)\tag{3.62}$$
最后修正得到二阶色散为
$$\frac{\mathrm{d}^2\phi}{\mathrm{d}\omega^2}=-\frac{m^2\lambda^3M^2L_\mathrm{eff}}{2\pi c^2\Lambda^2}\left[1-\left(-m\frac{\lambda}{\Lambda}-\sin\theta_\mathrm{i}\right)^2\right]^{-3/2}\tag{3.63}$$
- 当 $L<2(f_1+f_2)$ , 即光栅与透镜的间距小于焦距时, $L_{\text{eff}}<0$ , 这时GDD 被翻转. 

紧接着有两个问题：
(1) 在这种脉冲展宽器情形中，如何选择透镜的放大率？
(2) 为了实现光脉冲整形器，将光栅放在哪里？

- 虽然这种“放大率”可使光路更加紧凑. 
- 但问题是第二个光栅的选择需要使其之后所有不同的光谱分量平行传播。因此，第二光栅的每毫米凹槽的数量也必须通过放大因子来校正。而在实践中，很难获得如此完美匹配的第二光栅（制造两个相同的光栅要容易得多）。
- 那么，为什么不使用每毫米凹槽加倍的相同光栅作为第一个光栅呢？
	- 这将首先直接提供更大的角色散。
	- 此外，在光栅压缩器的输出端，我们希望所有光谱分量在空间上再次重叠, 所以往往使用四光栅压缩器。<mark style="background: #FFF3A3A6;">如果第一次通过时放大M，那么返回时将缩小为1/M，从而完全消除了最初的放大效果。</mark>
- 因此，在实践中往往选择<mark style="background: #FFF3A3A6;">放大倍数M=1</mark>（即<mark style="background: #FFF3A3A6;">两个透镜具有相同的焦距</mark>）.

在光脉冲整形器中，人们希望光栅的净GDD为零。因此，将光栅放置在望远镜的焦平面上（ $L_{\text{eff}}=0$ ）

基于光栅的脉冲整形器、压缩器和拉伸器是超快激光物理中非常重要的工具。它们被用于推进脉冲放大的前沿。最重要的突破是<mark style="background: #FF5582A6;">啁啾脉冲放大（CPA）技术</mark>（见图3.23），<mark style="background: #FFF3A3A6;">通过首先拉伸脉冲并降低峰值强度来防止放大器材料的损坏，从而也减少了光学损坏。在放大之后，不同的频率分量被另一个光栅脉冲压缩器及时重组</mark>。CPA技术能够将峰值功率缩放许多数量级，因此得到2018年诺贝尔物理学奖。

![[Pasted image 20231205153957.png]]

## 3.3.3 基于光栅的脉冲整形

- 透镜对焦平面中的入射波进行 FT（图3.20）。

![[Pasted image 20231205153413.png]]

- <mark style="background: #FFF3A3A6;">光栅引入角色散，入射光束的每个频率分量在空间中被衍射到特定的方向</mark>。
- 透镜将具有特定入射角的每个入射平面波成像到其焦平面中与透镜相隔距离f的特定位置。因此，我们<mark style="background: #FFF3A3A6;">可在透镜的焦平面中使用特殊的相位和振幅掩模分别处理每个单独的频率分量</mark>。如图3.21所示。

![[Pasted image 20231205153548.png]]

- 不同脉冲形状的示例如图3.22所示。

![[Pasted image 20231205153612.png]]


# 3.4 Gires–Tournois干涉仪（GTI）

<mark style="background: #FF5582A6;">Gires-Tournois 标准具</mark> (或干涉仪) 是一种具有两个反射表面的非吸收反射器, 其中一个反射表面有很高的反射率 (理想接近 100%). 

两个反射表面组成了一个 <mark style="background: #FF5582A6;">Fabry-Perot 标准具</mark>, 理想情况下, 它能反射 100% 的入射光，但在使用100%反射率的背反射镜而不引入其他损耗的情形下, 由于产生仅在相位中引起剧烈谐振的多光束干涉从而会造成<mark style="background: #FFF3A3A6;">与波长相关的相移</mark>。

一般, 我们忽略所有材料色散, GTI 如图 3.24 所示:

![[Pasted image 20231205154830.png]]

当GTI 左边的反射镜具有 100% 的反射率时, 所有的光强都被反射, 并且GTI 的内部没有吸收. 于是 GTI 能够实现 100% 的反射并不引入损耗:
$$|R_\mathrm{GTI}|=1,\quad R_\mathrm{GTI}=\exp{(i2\phi _\mathrm{GTI})}\tag{3.64}$$
唯一变化的参数是相位 $\phi_\mathrm{GTI}$，由于 Fabry–Pérot 结构，它变得<mark style="background: #FFF3A3A6;">十分依赖于频率</mark>。

这种频率依赖性比相关于层厚度 $d$ 的材料色散强得多 (比如, 不使用气隙或基板情形下)。通常，可忽略GTI中的材料色散。

两反射镜间距离可使用压电元件调节 ---- <mark style="background: #FFF3A3A6;">GTI也可以用于调节色散</mark>。

由图 3.24 , GTI 的反射率
$$r_\mathrm{GTI}\equiv \exp{(-i\phi_\mathrm{GTI})}=\frac{r_{12}+r_{23}e^{-i2\varphi}}{1+r_{12}r_{23}e^{-i2\varphi}}=\frac{\sqrt{R_t}-e^{-i2\varphi}}{1-\sqrt{R_{t}}e^{-i2\varphi}}\tag{3.65}$$
其中, $r_{12}=\sqrt{R_t}$ , $r_{23}=-1$ , 我们假设 $R_{t}$ 是一个正实数 $R_t=|R_t|$ , 相移
$$\varphi=nkd \tag{3.66}$$
GTI 的群延迟色散 $T_g$
$$T_g=\frac{d\phi_\mathrm{GTI}}{d\omega }\tag{3.67}$$
二阶色散
$$\frac{dT_g}{d\omega }=\dfrac{d^{2}\phi_\mathrm{GTI}}{d\omega^{2}}\tag{3.68}$$
其中相位
$$\tan\phi_{GTI}=-\frac{\mathrm{Im}(r_\mathrm{GTI})}{\mathrm{Re}(r_\mathrm{GTI})}=-\frac{(1-R_{t}) \sin 2\varphi}{2\sqrt{R_t}-(1+R_t) \cos 2\varphi}\tag{3.69}$$
对于边界情况, $R_t=0$ , 相位 $\phi_{GTI}$ 由 $2\varphi$ 给出, 其对应于通过镜面间距的往返相位.

为了计算色散, (3.66) 中的相位还可写为下面形式:
$$\varphi=nkd=n\frac{\omega }{c}d\equiv \frac{\omega 
 t_{0}}{2}\tag{3.70}$$
其中, $t_0=\dfrac{2nd}{c}$ 表示 F-P 腔中的往返时间.

下面我们忽略材料色散, 
$$\dfrac{d\varphi }{d\omega}\approx\frac{t_0}{2}\tag{3.72}$$
由 (3.67), (3.69) 并使用如下关系:
$$\dfrac{d\tan\phi}{d\omega}=(1+\tan ^2\phi )\dfrac{d\phi }{d\omega}$$
我们有:
$$T_\mathrm{g}=\frac{\mathrm{d}\phi_\mathrm{GTI}}{\mathrm{d}\omega}=\frac{t_0\left(1-R_\mathrm{t}\right)}{1+R_\mathrm{t}-2\sqrt{R_\mathrm{t}}\cos\omega t_0}\tag{3.73}$$
群延迟色散
$$\frac{\mathrm{d}T_\mathrm{g}}{\mathrm{d}\omega}=\frac{\mathrm{d}^2\phi_\mathrm{GTI}}{\mathrm{d}\omega^2}=-\frac{2t_0^2\left(1-R_\mathrm{t}\right)\sqrt{R_\mathrm{t}}\sin\omega t_0}{\left(1+R_\mathrm{t}-2\sqrt{R_\mathrm{t}}\cos\omega t_0\right)^2}\tag{3.74}$$
由上可见，<mark style="background: #FFF3A3A6;">Fabry–Pérot结构（非材料色散）产生了随波长改变正负周期性变化的GDD群延迟和二阶色散</mark>（图3.25和3.26）。

由于对 $t_0$ 的依赖性，（3.73）和（3.74）表明: <mark style="background: #FFF3A3A6;">群延迟和GDD都随着层厚度d的增加而增加</mark>。对于GDD，它甚至呈二次方增长
$$\frac{dT_g}{d\omega }\propto d^2\tag{3.75}$$

![[Pasted image 20231205173911.png]]

我们需要权衡, GTI的带宽随着层厚度d的增加而减小.
$$\text{bandwidth of }\frac{dT_{g}}{d\omega }\propto \frac{1}{d}\tag{3.76}$$

对大的负色散，d得足够大，但这会极大地限制可用带宽，从而无法支持短脉冲。通常，空气间隔的GTI不用于短于约100fs的脉冲. 

另一方面, GTI的可用带宽也受到快速增长的高阶色散的限制。


# 3.5 基于角色散与 GTI 的色散补偿器总结

![[Pasted image 20231205180818.png]]

# 3.6 相控反射镜

## 3.6.1 Bragg 镜

一种基本的高反射镜是 <mark style="background: #FF5582A6;">Bragg 镜</mark>, Bragg 镜<mark style="background: #FFF3A3A6;">由高, 低折射率的四分之一波层交替堆叠组成</mark>, 如图 3.27 所示.

一个 Bragg 镜在 Bragg 波长 $\lambda _B$ 处表现出最大反射率, 一般用该波长来定义四分之一波长结构, 每一个独立的层的厚度为布拉格波长的 1/4倍 $\lambda _B/4$ . 

![[Pasted image 20231206104253.png]]

Bragg 镜的反射率在一系列波长 (称为<mark style="background: #FF5582A6;">阻带</mark>) 下表现出高反射率, 在边缘急剧下降, 见图 3.28 . 

![[Pasted image 20231206104328.png]]

在角频率
$$\omega _{B}=\frac{2\pi c}{\lambda _B}$$
附近的阻带, 有如下关系:
$$\frac{ \cos \phi -r^{2}}{1-r^2}\leq-1$$
其中, $\phi =\dfrac{\pi \omega }{\omega  _B}$ 是在一对四分之一波层传播后获得的相位, $r$ 描述了由不同层间折射率阶跃导致的菲涅尔反射系数, 由下式给出:
$$r=\frac{n_H-n_L}{n_H+n_L}\tag{3.77}$$
假如我们忽略折射率的波长依赖性, 反射带将覆盖波长范围
$$[\lambda _{S1},\lambda _{S2}]=[\dfrac{\pi \lambda _B}{2\pi-2\arccos r},\dfrac{\pi\lambda _B}{2\arccos r}]$$
因此, 其分数宽度 $\dfrac{\Delta \omega }{\omega _B}$ 仅取决于高低折射率材料的折射率之比
$$\frac{\Delta \omega }{\omega _B}=\frac{4}{\pi }\arcsin r \tag{3.78}$$

对于外延生长的半导体四分之一波镜，所有折射率通常都在 3.0 到 3.6 之间，因此它们的最大分数带宽约为 10%。对于非晶涂层，低折射率的几种典型材料介于 $\mathrm{MgF_2}$ (n = 1.37) 和 $\mathrm{SiO_2}$ (n = 1.45) 之间，典型的高折射率材料为 $\mathrm{Ta_2O_5}$ (n = 2.1) 和 $\mathrm{TiO_2}$ (n = 2.35)，这会导致分数带宽达到约30%。外延生长的 $\mathrm{CaF_2/Al_{1−x} Ga_x}$ 多层结构甚至具有高达 55% 的分数带宽。

对于无损四分之一波镜，可精确计算具有图 3.27 所示结构的四分之一波镜的最大反射率，计算公式为
$$R_0(\lambda_\mathrm{B})=\left(\frac{1-aqp^{m-1}}{1+aqp^{m-1}}\right)^2\tag{3.79}$$
其中, $m=2N$ 为对于 N 个层对的层数, 参数 a, p 和 q 分别为三种界面上的折射率比值
$$p=\frac{n_1}{n_\mathrm{H}}\:,\quad q=\frac{n_\mathrm{L}}{n_\mathrm{H}}\:,\quad a=\frac{n_\mathrm{L}}{n_\mathrm{S}}\tag{3.80}$$
布拉格镜的波长相关反射率如图 3.28 所示。

在<mark style="background: #FFF3A3A6;">布拉格镜的阻带内，即高反射率带宽内，我们有一个线性相移，因此没有二阶色散</mark>。这意味着，<mark style="background: #FFF3A3A6;">在阻带内，脉冲将被反射而没有任何失真</mark>。然而，阻带也对 Bragg 镜的应用构成限制, <mark style="background: #FFF3A3A6;">一旦超短脉冲的带宽超出高反射阻带，这种情况就会发生巨大变化</mark>。

对最早的低于 100 fs 的染料激光器，棱镜压缩器尚不能用于色散补偿。为获得负色散，往往将布拉格波长比激光器中心波长短的高反射布拉格镜插入激光器中。图 3.28 描绘了布拉格波长为 630 nm 的布拉格镜的示例：对于约 750 nm 的较长波长，镜子<mark style="background: #FFF3A3A6;">产生负色散</mark>，即 $dT_g/dλ>0$，因此 $dT_g/dω<0$，而不引入太多损失。


## 3.6.2 电介质 GTI 型镜

我们需要大量的负群延迟色散（GDD）才能在高脉冲能量下实现孤子锁模。因此，通常使用在多层结构中具有显著场增强的电介质 GTI 型反射镜。

优势:
- 使用介电多层涂层代替空气间隔的法布里-珀罗（参见第 3.4 节），并通过调整层厚度可以获得 "增强的" 法布里-珀罗场。
- 但是如此虽然可以实现相对大量的 GDD，但通常带宽有限。
- 相对，只要脉冲持续时间足够长（即，中心波长为 $1.030 μm$ 时 > 500 fs），<mark style="background: #FFF3A3A6;">平坦的负 GDD 的带宽要求</mark>可以通过商用色散 GTI 型反射镜来满足，该反射镜具有<mark style="background: #FFF3A3A6;">很高的单次反射产生的色散</mark>（通常约每次反射 -500 $fs^2$)。
- 也可以考虑使用低损耗线性调频反射镜（参见第 3.6.3 节），但每次反射可实现的最大色散较低，对于所需的总体色散而言仍然不切实际，因此 GTI 型反射镜仍然是这样的激光器的首选。

不足:
在<mark style="background: #FFF3A3A6;">高功率</mark>超快固态激光器中，与标准高反射多层堆叠相比，电介质 GTI 型反射镜结构中的大场增强可直接导致更高的寄生<mark style="background: #FFF3A3A6;">非线性吸收</mark>，这会导致<mark style="background: #FFF3A3A6;">热性能恶化</mark>，引入<mark style="background: #FFF3A3A6;">较低的损伤阈值</mark>并<mark style="background: #FFF3A3A6;">增加损耗</mark>。

基于半导体的 GTI 提供了另一个机会。例如，使用多层半导体 GTI 镜（除了色散补偿之外还包含可饱和吸收器），可以通过二极管泵浦 Cr:LiSAF 激光器生成 160 fs 脉冲。


## 3.6.3 啁啾镜

要产生非常短的脉冲需要在很宽的光谱上使用色散补偿技术. 棱镜对是色散补偿技术的标准组件, 但其缺点是会产生大量的高阶色散. 而啁啾镜能克服这一限制.

虽然超宽带的反射镜所覆盖的阻带超出了简单的 $\mathrm{TiO_2/SiO_2}$ 布拉格反射镜, 涉及多个具有重叠组带连续四分之一波长部分, 但其引入了强烈依赖于波长的 GDD, 导致非常大的相位变化, 且它不能应用于飞秒应用. 

而啁啾镜中, 布拉格波长在沉积过程中逐渐减小 ( 至少在初始设计中必须通过后续计算机优化进行更改以防止寄生 GDD 振荡 ) 。因此，<mark style="background: #FFF3A3A6;">波长越长的成分就能越深地穿透镀层，产生负的 GDD</mark>. 相较四分之一波镜，啁啾镜扩大了高反射率范围, 如图3.29b。啁啾镜是宽带色散补偿的理想紧凑元件。

![[Pasted image 20231206163346.png]]

啁啾镜一次反射的总色散不是很大，因此仅用于近红外的 10 fs 以下区域。并且多次反射通常也用于线性调频镜像压缩器中。通过计算反射镜材料中的光程差，可以获得最大负色散的简单估计，如图 3.29a 所示。简单地从多层镜结构的总厚度就可以清楚地看出我们需要多次反射来补偿至少几毫米长的激光晶体的色散.

啁啾反射镜有一个重要缺点：计算出的色散特性显示出围绕理想色散补偿所需目标函数的不必要的振荡（图 3.30）。

![[Pasted image 20231210152155.png]]

1994 年，还没有令人满意的理论来正确描述此类镜子的光谱特性。特别是，对于群延迟和 GDD 中出现的振荡，不存在任何分析解释。尽管与所需的平滑色散曲线存在偏差，但此类结构最初被用作计算机优化的起始设计，旨在减少群延迟和 GDD 中不需要的振荡。通过这种方式，啁啾反射镜被设计用于无棱​​镜谐振器中的腔内色散补偿以及混合反射镜和棱镜方案。用这种啁啾镜获得的最短脉冲是在无棱镜环形谐振器中产生的。这些脉冲的持续时间约为 7.5 fs 。

1997年，在精确耦合模式方程和传输线理论的基础上，提出了啁啾镜的综合理论。据此，我们引入一种经过分析设计的<mark style="background: #FFF3A3A6;">多层反射镜堆叠</mark>，称为<mark style="background: #FF5582A6;">双啁啾反射镜 (DCM)</mark>，<mark style="background: #FFF3A3A6;">以避免不良振荡</mark>。 DCM 的原理基于以下事实：<mark style="background: #FFF3A3A6;">除局部布拉格波长的啁啾之外，还必须减少镜子开始处的初始部分反射，以避免强烈的 GDD 型振荡</mark>（见图 3.30） ）。这可通过阻抗匹配方法解决，其中<mark style="background: #FFF3A3A6;">高折射率层厚度中的啁啾会缓慢减小阻抗，从而减少部分反射</mark>（见图 3.29c 和 3.31）。

![[Pasted image 20231210152411.png]]

阻抗匹配方法减少了啁啾镜结构初始部分的部分反射（图3.31顶部），这对于长波长组件尤其重要。附加的宽带抗反射 (AR) 涂层解决了从空气进入啁啾镜结构的第一个界面的阻抗匹配问题（图 3.31c 底部）。我们通常需要将该增透膜的残余反射率降低到优于 $10^{−4}$。然而不幸的是，这限制了 DCM 的带宽，我们无法同时获得任意低的反射率和任意宽的带宽。在中心波长为 800 nm 时，我们通常可以获得约 230 nm 的反射率带宽，残余反射率小于 $10^{−4}$ 。

![[Pasted image 20231210155011.png]]

减少的色散振荡如图 3.32 所示。这比较了单啁啾反射镜和双啁啾反射镜的反射率和群延迟。对于 1050 至 700 nm 范围内的单啁啾镜，平均群延迟的斜率为负。然而，<mark style="background: #FFF3A3A6;">±25 fs 的强群延迟振荡会极大地扭曲任何超短脉冲，这阻碍了使用此类单啁啾镜来生成超短脉冲</mark>。之所以产生这些振荡，是因为<mark style="background: #FFF3A3A6;">深入反射镜的长波长在穿过镀层前部的过程中也被部分反射</mark>。与单啁啾反射镜相比，DCM 可以抑制不需要的色散振荡，如上所述。图3.32进一步表明，<mark style="background: #FFF3A3A6;">与单啁啾镜相比，DCM的高反射率带宽在短波长侧有所减小</mark>。然而，单线性调频镜的额外带宽并未显示出所需的负色散，因此在色散补偿范围内没有带宽损失。

![[Pasted image 20231210164402.png]]

图 3.33 显示了 DCM 中与波长相关的渗透。该 DCM 还设计用于对钛蓝宝石激光器中的绿色泵浦光具有高透射率。

![[Pasted image 20231210164307.png]]

增透膜的带宽限制可以通过进一步扩展 DCM 的设计来解决。<mark style="background: #FFF3A3A6;">当来自 AR 涂层的最大可接受残余反射不干扰多层 DCM 叠层时，可以充分放宽这些残余反射的限制</mark>。这可以通过<mark style="background: #FF5582A6;">楔形基板</mark>来实现，如图 3.34 所示，其中<mark style="background: #FFF3A3A6;">来自基板的前反射不会干扰镜组的其余部分</mark>。如果我们选择衬底 $n_{\text{substrate}}$ 的折射率等于 DCM 部分的第一层 $n_{\text{first}}$ 层的折射率，则可以完美地获得从衬底内部到 DCM 结构的阻抗匹配。在这种情况下，基材上的增透膜只需减少损耗，通常应为 1% 的一小部分。因此，可以生产更广泛的增透膜。这个概念被称为<mark style="background: #FF5582A6;">背面涂层双啁啾镜（BASIC DCM）</mark>。

![[Pasted image 20231210164801.png]]

使用这样的 BASIC DCM，可以大幅扩展反射率带宽，同时将残余色散振荡保持在小于 3.8 fs2 rms（图 3.35）[00Mat]。 BASIC DCM 设计的缺点是我们<mark style="background: #FFF3A3A6;">必须引入额外的正色散</mark>，因为<mark style="background: #FFF3A3A6;">脉冲现在必须通过基板传播</mark>。然而，这<mark style="background: #FFF3A3A6;">可以通过啁啾镜的更多反射次数来补偿</mark>。更严重的缺点是，<mark style="background: #FFF3A3A6;">由于楔形基底处与波长相关的折射引入的角色散，光束不再在空间上相干</mark>。 这必须通过另一个匹配的反射来补偿。对于曲面镜来说，这不是问题，因为我们可以在第一界面选择平坦的基板，而 DCM 结构将在基板的第二界面处经历曲率半径。

目前，啁啾反射镜色散补偿的主要限制是这种<mark style="background: #FFF3A3A6;">反射镜的制造</mark>。我们可以获得对于一个光循环状态来说足够好的设计，但是<mark style="background: #FFF3A3A6;">制造过程中的层沉积误差通常太大并且再次引入GDD振荡</mark>。对于高达 50 fs2 峰值的 GDD 误差，仅 0.2 nm rms 的层沉积误差就足够了（图 3.36）。因此，我们通常使用在不同时间制造并仔细选择的许多不同的啁啾镜来补偿它们的色散振荡。因此，<mark style="background: #FFF3A3A6;">通过使用一组不同的啁啾反射镜，可以平均化诱导层沉积误差，从而这些配置最终证明来自激光振荡器的最短脉冲</mark>。然而，很明显，更准确、更经济的涂层沉积技术将对超快激光界非常有利。


## 3.6.4 啁啾镜的设计

标准耦合模式理论适用于小折射率阶跃，通常用于光纤光栅的计算.

<mark style="background: #FFF3A3A6;">高频传输线中阻抗匹配等概念转移到涂层设计中，而不仅仅是用于小折射率调制的结构</mark>。耦合模式理论根据耦合一阶微分方程将向后和向前传播模式 A 和 B 的缓慢变化的场振幅联系起来
$$\frac{\mathrm{d}}{\mathrm{d}m}\begin{pmatrix}A\\B\end{pmatrix}=\mathrm{i}\begin{bmatrix}-\delta&-\kappa\\\kappa&\delta\end{bmatrix}\begin{pmatrix}A\\B\end{pmatrix}\tag{3.81}$$
其中, 失谐系数 $\delta$ , 耦合系数 $\kappa$ , 归一化传输距离 $m$ 的函数, 如图 3.37 . 这里 m 是一个连续变量，用于计算索引步长，定义为
$$m\equiv\int_0^m\mathrm{d}\bar{m}\equiv\int_0^z\frac{\mathrm{d}\bar{z}}{d_\mathrm{H}\left(\bar{z}\right)+d_\mathrm{L}\left(\bar{z}\right)}\tag{3.82}$$

![[Pasted image 20231210231625.png]]

通过适当的替换，耦合模式方程解耦，产生两个独立的波动方程。利用精确的耦合模式方程，可以证明<mark style="background: #FFF3A3A6;">单线性调频结构中不需要的色散振荡是由阻抗失配引起的</mark>。 （复数）阻抗取决于通过耦合和失谐系数的归一化位置 m。不仅可通过对布拉格波长 $λ_B$ 进行啁啾，还可以通过对<mark style="background: #FF5582A6;">占空比</mark>（<mark style="background: #FFF3A3A6;">对布拉格波长有贡献的高折射率材料部分</mark>，见图 3.29）来避免失配。

![[Pasted image 20231206163346.png]]

由于晶胞高折射率部分和低折射率部分的传播而产生的相位差异会影响耦合系数 $κ$，并且缓慢的占空比上升减少了阻抗不连续处的内部反射。我们将 $λ_B$ 和 κ 都系统变化的啁啾镜称为<mark style="background: #FF5582A6;">双啁啾镜 (DCM) </mark>。<mark style="background: #FFF3A3A6;">为了获得最佳阻抗匹配，耦合系数根据幂律从零上升到最大值</mark>。

啁啾镜理论提供了一个近似解析公式，显示如何对布拉格波长进行啁啾以调整色散涂层性能。下面给出的线性调频定律的解析公式依赖于简化的 <mark style="background: #FF5582A6;">WKB 解决方案</mark>，该解决方案使用标准失谐和恒定耦合系数，从而忽略任何双线性调频. 它允许我们计算布拉格波数值为 $k_B \equiv  \dfrac{2π}{λ_{B}}$ 的晶胞位置 m，以实现作为 $k_B$ 函数给出的目标 GDD。第 m 个晶胞的光学厚度与布拉格波长的关系为 $d_{\text{opt}} = n_Hd_H + n_Ld_L = \dfrac{π}{k_{B}}$。当 m 定义为 (3.82) 时，逆线性调频定律为
$$m\left(k_\mathrm{B}\right)=\frac{c^2}{2\pi}\left(1-\frac{2r}\pi\right)\int_{k_\mathrm{B}}^{k_\mathrm{B}^\mathrm{max}}\bar{k}_\mathrm{B}\operatorname{GDD}\left(\bar{k}_\mathrm{B}\right)\mathrm{d}\bar{k}_\mathrm{B}\tag{3.83}$$

如果所需的 GDD 服从幂律，那么求解这个方程就很简单。例如，为了实现恒定的负 GDD，必须根据平方根定律线性调频 $k_B$。相反，如果我们在沉积过程中线性减小 $k_B$，$k_B(m) = k^ {max} _{B} − a|m|，a > 0$，则所得 GDD 将与 $λ$ 成正比，因此 TOD 将为正（见图 3.32）。 DCM 理论的一项显着成果是，<mark style="background: #FFF3A3A6;">设计具有负 GDD 和正 TOD 的宽带啁啾镜比设计同时具有负 GDD 和负 TOD 的宽带啁啾镜更容易</mark>。

(3.83) 中给出的解析啁啾定律对于数值细化也有好处：典型的啁啾反射镜由大约 50 层组成，因此计算机优化程序必须搜索 50 维的参数空间才能找到良好的最小值函数（取决于 GDD 振荡和高反射阻带）。如果层数进一步增加，则分析起始设计的存在变得更加有利，半导体啁啾镜就是这种情况[99Pas]，相对折射率差要小得多。实际上，解析啁啾定律给出了如何改变布拉格波长的信息，但双啁啾不能包含在封闭形式的解中。在 DCM 的设计中（图 3.38），我们在涂层的第一部分中加入了双啁啾。与该双线性调频部分一样，后续的单线性调频部分也遵循分析线性调频定律。然后可以添加可选的非啁啾四分之一波长部分，以便进一步扩展长波长侧的高反射率范围。最后，在镜子顶部添加了单独设计的增透膜，以提供与空气的阻抗匹配。由于所进行的近似、折射率的色散、有限的层数、层所需的最小厚度以及不完美的增透膜，该结构确实需要进一步的计算机优化。尽管如此，DCM 理论使得开始设计比任何其他方法都更接近预期目标。计算机优化的细节远远超出了本章的范围，读者可以参考[99Mat2]以获取对此问题的更详细说明。

![[Pasted image 20231210233429.png]]

# 3.7 Dazzlers

能够在大光谱带宽上自适应补偿大量色散的可编程器件。尽管<mark style="background: #FF5582A6;">空间光调制器（SLM）</mark>和<mark style="background: #FF5582A6;">可变形镜</mark>也已被成功使用，但我们将在本节中将讨论限制为<mark style="background: #FF5582A6;">声光可编程色散滤波器（ AOPDF 或所谓“dazzler”）</mark>。

与 SLM 和可变形镜相比，Dazzler
-  不需要高质量的光学元件;
- 结构紧凑，易于在现有激光放大器系统中实现.

图 3.39 显示了 AOPDF 的示意图。使用由射频时间信号激励的换能器将声波发射到声光装置中。声波以速度 υ 沿 z 轴传播，以这种方式在空间上再现射频信号的时间形状。如果两个光学模式和声波相位匹配，则两个光学模式只能通过声光相互作用有效耦合。由于声光栅局部只有一种空间频率，因此在位置z处只能衍射一种光频率。传入的光脉冲最初处于模式 1。每个频率 $ω$ 在遇到声光栅中的相位匹配空间频率之前都会传播一定的距离。在该位置 $z(ω)$ 处，部分能量被衍射至模式 2，并随后沿该模式传播。在模式 2 下离开设备的脉冲将由在各个位置衍射的所有光谱分量组成。如果两种模式的速度不同，则每个频率将经历不同的时间延迟。这通常是通过通过双折射晶体传播声波和光脉冲来实现的。光最初沿着快寻常轴偏振，但被衍射到慢速非常轴。衍射效率，即输出脉冲的幅度，由位置 $z(ω)$ 处的声功率控制。

![[Pasted image 20231210233918.png]]

AOPDF 的光输出是光输入和电信号的函数。因此，<mark style="background: #FFF3A3A6;">通过正确选择射频信号的时间形状以及声波的空间形状，可以创建作为频率函数的几乎任意的群延迟分布</mark>。通过耦合波理论可以获得 AOPDF 输出端群延迟与输入声信号的解析表达式.

# 3.8 色散测量

测量 GDD 的标准方法是通过白光干涉测量法。这里，宽带光源的输出被馈送到干涉仪（通常是迈克尔逊型干涉仪）。被测设备 (DUT) 放置在样品臂中，而参考臂包含具有已知色散的光学器件。使用光电二极管（时域采样、光谱集成检测）或使用光谱干涉测量法来监测所得的干涉图案。

光谱积分方法的明显优点
- 可以同时评估所有频率分量的相位，因此即使是低功率谱密度的光源也可以使用。
- 与光谱分辨检测相比，光谱积分方法不需要单色仪、光谱仪或探测器阵列；因此无需对这些设备进行其他必要的校准。
- 低设备成本以及实时倾斜对准和零延迟监测的可能性。

两个白光迈克尔逊干涉仪用于测量包含待测试组件的样本臂和已知色散的参考臂之间与波长相关的相位差。

第一种方案如图 3.40 所示，利用一个干涉仪臂中的电动镜台和基于 HeNe 激光的距离校准。

![[Pasted image 20231210234937.png]]

实验轨迹的示例如图 3.41 所示。互相关中的边缘项表示为
$$S\left(\Delta t\right)=\mathrm{Re}\int_{-\infty}^{+\infty}E_{\mathbf{S}}^{*}(t)E_{\mathbf{R}}\left(t+\Delta t\right)\mathrm{d}t \tag{3.84}$$
其中 $E_S$ 和 $E_R$ 分别是来自样本臂和参考臂的场，我们假设准无限积分时间，比白光的相干时间长得多。每当光程差改变单色氦氖触发激光器波长的一半时，就会对条纹进行采样。

![[Pasted image 20231210235406.png]]

干涉图的快速傅立叶变换（图 3.41）产生样本和参考臂的振幅谱的乘积。傅里叶变换信号的参数是两个臂之间的相位差，而其相对于频率的导数给出了相对群延迟。

首先在没有样品的情况下表征两个臂的相对分散。然后测量样本引起的频谱相位 φ 作为频率的函数。根据相位，我们以数字方式计算群延迟，并计算许多单独干扰迹线的平均值。测量的光谱分辨率由 $ω = 2π c/N λ_{HeNe} \approx 0.006 fs^{−1}$ 给出，通常每条干涉迹线有 $N = 512$ 个条纹数据点。当中心波长为 $λ_c ≈ 800 nm$ 时，结果为 $λ = λ2/N λ_{HeNe} ≈ 2\text{nm}$。典型傅里叶变换光谱仪中使用的干涉图的光谱幅度在色散测量中被忽略，但决定了检索相位中的误差。

在第二个白光干涉仪设置中，我们稍微倾斜其中一个干涉仪臂，如图 3.42 所示。这导致<mark style="background: #FFF3A3A6;">离开干涉仪的两个平面波之间存在依赖于高度的几何路径长度差异</mark>。在它们的叠加中，干涉仪后面的垂直狭缝处<mark style="background: #FFF3A3A6;">产生彩色干涉条纹</mark>。这种白光干涉图案相当于上述动态干涉仪中记录的<mark style="background: #FFF3A3A6;">一小部分与延迟相关的干涉信号</mark>。该信号不是通过数值傅里叶变换，而是通过成像光谱仪进行波长解析，然后通过 CCD 相机进行观察。记录的图像显示了作为高度和波长函数的二维干涉图样（<mark style="background: #FF5582A6;">穆勒条纹</mark>，见图 3.43）。<mark style="background: #FFF3A3A6;">在固定波长下，干涉图作为高度的函数振荡，频率与波长成反比</mark>。样品和参考臂之间的色散差异引起该振荡的相移 $φ$，该相移被记录为光频率的函数。


![[Pasted image 20231210234919.png]]

在每个干涉仪中，我们测量两个干涉仪臂之间的相对相移 $φ$ 作为频率 $ω$ 或波长 $λ$ 的函数。双重数值微分最终给出 GDD。由于微分对检索阶段中的实验噪声敏感，因此我们通常使用低通傅立叶滤波器（二项式平滑）来平滑结果曲线。

第二种技术的缺点
- 依赖于进入和离开干涉仪的平面波, 因此曲面镜的测量很复杂
- 尽管两个干涉仪臂的不同光斑尺寸会降低条纹水平，但这一要求对于动态测量并不重要。

对于使用动态白光干涉仪来表征中心波长约为 800 nm 的啁啾镜的 GDD 测量，在波长分辨率下，GDD 的精度通常优于 $±5fs^2$，群延迟的精度优于 $±0.1 fs$ 约 $±5nm$ ( 图 3.44 ) 。这足以解决啁啾反射镜的色散变化，并且对于具有更平滑色散特征的组件来说绰绰有余。如果需要更好的信噪比，我们可以用飞秒激光器产生的超连续谱代替白光源，这是迄今为止最亮的空间相干宽带光源。为了将可表征的光谱范围扩展到更短的波长，我们可以使用更短波长的触发激光器，或者我们可以折叠触发激光器的光束，使其两次击中移动镜。对于窄折叠角度，这将使触发信号的有效频率大约加倍。

