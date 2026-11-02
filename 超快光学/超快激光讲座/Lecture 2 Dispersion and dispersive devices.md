
#光学/超快光学

非线性效应: 在洛伦兹模型中引入修正项

# 脉冲的线性传输

![[Pasted image 20231105101147.png]]


脉冲: 载波+包络

传播常数 
$$k(\omega )=\dfrac{\omega n(\omega)}{c_0}$$
零阶
$$k_{0}=\dfrac{\omega _0n(\omega _0)}{c_0}$$


缓变振幅近似
$$\bigg|\frac{d^2A}{dz^2}\bigg|<<\bigg|2k_0\frac{dA}{dz}\bigg|$$

# 对k作泰勒展开, 看前两阶的作用
![[Pasted image 20231105102258.png]]
得到频域上包络的空间演化.

# 作傅里叶逆变换, 变换回时域
![[Pasted image 20231105102842.png]]

- 包络随时间变化, 且时间上发生移动
- 载波相位发生变化


- 群速度 (包络传播速)
$$V_{g}=\frac{1}{k_{1}}=1/\frac{dk}{d\omega}\bigg|_{\omega=\omega_{0}}=\frac{c_{0}}{n(\omega_{0})+\omega_{0}\frac{dn(\omega)}{d\omega}\bigg|_{\omega=\omega_{0}}}$$

- 相速度 (载波传输速度)
$$V_{p}=\frac{\omega_{0}}{k_{0}}=\frac{c_{0}}{n(\omega_{0})}$$

群速度>光速
- 剧烈的吸收和色散, 无法用于光通信
- 并不是能量传输的速度

- 慢光
- 超材料


# 群速度色散

考虑泰勒展开的第三项, (二阶)

![[Pasted image 20231105104437.png]]

- 出现群速度的修正, 群速度发生色散---群速度色散 GVD
$$k_{2}=\frac{d}{d\omega}(\frac{dk}{d\omega})=\frac{d}{d\omega}(\frac{1}{V_{g}})$$

# 时域上?---反傅里叶变换

![[Pasted image 20231105105418.png]]

高斯函数为例
$$A(z,t)=A_0\sqrt{\frac{\tau^2}{\tau^2+jk_2z}}\exp\{-\frac{\tau^2\left(t-\frac{z}{Vg}\right)^2}{2[\tau^4+(k_zz)^2]}+jk_2z\frac{\left(t-\frac{z}{Vg}\right)^2}{2[\tau^4+(k_zz)^2]}\}$$

- 傅里叶变换后还是高斯函数

![[Pasted image 20231105105609.png]]

- 脉冲获得延时 $t \longrightarrow  T=t-\frac{z}{V_g}$
- 抛物型的二阶相位
- 脉冲发生展宽

展宽
$$\tau_{FWHM(z=L)}=2\sqrt{\mathrm{ln}2}\tau\sqrt{1+\left(\frac{k_{2}L}{\tau^{2}}\right)^{2}}=\tau_{FWHM}(z=0)\sqrt{1+\left(\frac{k_{2}L}{\tau^{2}}\right)^{2}}$$
长距离情形
$$\tau_{FWHM(Z=L)}=2\sqrt{\ln2}\left|\frac{k_{2}L}{\tau}\right|$$
- 二阶项 $k_2$ 改变脉冲宽度
- 光谱越宽, 光谱展宽越多

载波相位发生变化

可定义瞬时频率
$$\omega_{inst}(z=L,T)=\frac{\partial}{\partial T}\{\omega_{0}T+k_{2}z\frac{T^{2}}{2[\tau^{4}+(k_{z}z)^{2}]}\}=\omega_{0}+\frac{k_{2}z}{[\tau^{4}+(k_{z}z)^{2}]}\:T$$
载波振荡的快慢随时间变化---啁啾 Chirp , 脉冲前沿开始到脉冲后沿, 
- $k_2>0$, 载波振荡的频率越来越快, 正群速度色散---正啁啾
- $k_2<0$, 载波震荡的频率越来越慢, 负群速度色散---负啁啾

![[Pasted image 20231105112020.png]]

# 总结

![[Pasted image 20231105111603.png]]

脉冲通过一个色散介质后

![[Pasted image 20231105112052.png]]
- 展宽
- 啁啾

# 群延迟&群延迟色散

许多光学器件中, 难以定义 $k(\omega )$ , 因此常用群延迟描述这些过程


$$\phi(\omega)=k(\omega)z=\phi_0+\phi_1(\omega-\omega_0)+\frac12\phi_2(\omega-\omega_0)^2+\frac16\phi_3(\omega-\omega_0)^3+\ldots\quad\quad\phi_m=\left(\frac{d^m\phi}{d\omega^m}\right)_{\omega=\omega_0}$$

群延迟, 单位 $fs$ :
$$\phi_{1}=\frac{z}{V_{g}}=\tau_{g}$$
包络的延迟: 由于群速度的存在导致脉冲包络在时域上产生延迟.

群延迟色散 (GDD, $fs^2$):
$$\phi_2=\frac{d\tau_g}{d\omega}$$
- GDD>0---正色散
- GDD<0---负色散

三阶---TOD

四阶---FOD

![[Pasted image 20231105112649.png]]

- 零阶下不改变包络
- 群延迟 (一阶) 反映了包络的延迟


![[Pasted image 20231105113044.png]]

- 群延迟色散 (二阶) 使包络展宽并啁啾
- 四阶色散 脉冲的中间变化不大, 但是脉冲的前沿和后沿产生了很大的拖尾. 四阶色散越大, 拖尾越长.
- 推广: 若色散是偶数阶, 脉冲的包络的改变是对称的.


![[Pasted image 20231105113340.png]]
- 三阶可分为: 正三阶色散和负三阶色散
- 也产生拖尾
- 奇数阶色散, 并不对称
- 正的色散拖尾在脉冲后沿, 负的色散拖尾在前沿


# 变换极限脉冲

脉冲可用时域表示也可用频域表示:
$$\tilde{E}(\omega)=\int\limits_{-\infty}^{\infty}E(t)\exp(-j\omega t)dt,\quad E(t)=\frac{1}{2\pi}\int\limits_{-\infty}^{\infty}\tilde{E}(\omega)\exp(j\omega t)d\omega $$
- 频域上有光谱宽度 $\Delta \omega$
- 时域上有脉冲宽度 $\Delta t$
(均由半高全宽定义)

于是有, 类似于不确定原理的时间带宽积 (TBP)
$$\Delta \nu \Delta t \geq K$$
- 给定光谱, 存在一个脉冲持续时间的最小限制. 若达到最小持续时间, 我们称这种脉冲为<mark style="background: #FF5582A6;">变换极限脉冲</mark>.
- <mark style="background: #FFF3A3A6;">要获得更小的变换极限脉冲, 就需要更宽的光谱</mark>.


# 色散补偿器件

#光学/超快光学/色散补偿

## 角色散

折射的角度随频率发生变化.

![[Pasted image 20231105114649.png]]

白光打到棱镜上, 不同颜色的光沿着不同的角度出射.

相位出现延迟:

![[Pasted image 20231105114722.png]]

利用棱镜对可以将角色散变为群延迟色散

![[Pasted image 20231105115956.png]]

- 棱镜对可以产生负色散, 可以补偿材料中的正色散

## 光栅对

光栅: 多个狭缝发生干涉

![[Pasted image 20231105120212.png]]

通过控制周期可以控制干涉的条纹集中的位置.
$$\sin\alpha +\sin \beta _{m}=\frac{m\lambda }{d}$$
利用光栅对也能产生负群延迟色散:


![[Pasted image 20231105120402.png]]

![[Pasted image 20231105120526.png]]

- 色散效果远好于棱镜对
- 具有更小的损失

![[Pasted image 20231105120654.png]]


## 啁啾镜

高折射率与低折射率的材料以镀膜的方式周期重复, 组成类似布拉格晶面的结构, 可以实现高反射率

![[Pasted image 20231105121158.png]]

我们对上面结构进行改造, 调节厚度, 使得越深处镀膜厚度越厚 --- 啁啾镜

![[Pasted image 20231105121430.png]]

- 短波长在浅的地方反射, 长波长在更深的地方反射, 从而实现负群延迟色散.

![[Pasted image 20231105121557.png]]

上述结构也能在光纤中实现---啁啾光纤布拉格光栅

![[Pasted image 20231105121742.png]]

上述结构放在体材料中 --- 啁啾体布拉格光栅 (CVBG)

![[Pasted image 20231105121816.png]]

- 非常紧凑

## 激励色散补偿

Spatial light modulator

![[Pasted image 20231105122023.png]]

- 用液晶片上电流调制通过光的振幅&相位, 实现对脉冲的任意操作.

还可用声光调制器 --- AOPDF (Dazzler)

![[Pasted image 20231105122206.png]]

利用声光晶体, 加入声波, 挤压材料导致折射率周期变化.

双折射晶体有快轴和慢轴, 对快轴操作可将入射光有选择性地让其中某个成分变到另一个轴上. 
- 通过声波在晶体中传输, 产生折射率变化, 相当于一个光栅, 光栅发生衍射, 将快轴上的光有选择的传播到慢轴上. 
- 频率选择由声波频率决定, 选择多少由声波强度决定. 通过声波变成衍射光栅, 从而对光的光谱&强度进行选择.

Q: CPA 

展宽---正色散 
压缩---负色散

足够的色散---空间中传播足够距离---夫琅禾费衍射---FT

光谱越宽, 高阶色散的作用越明显.




