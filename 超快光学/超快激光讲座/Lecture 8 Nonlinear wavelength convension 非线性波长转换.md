
#光学/超快光学 
#光学/非线性光学 

# 回顾

- 飞秒激光的频谱由等间隔的谱线构成, 谱线间隔严格等于飞秒激光的重复频率, 重复频率由腔长决定+
	- ++++
- 激光频率梳由两个自由度: $f_R$ & $f_{ce}$
- 1f-2f 干涉仪可以实现 $f_{R}$ & $f_{ce}$ 的测量&控制
- 频率梳在 RF 和 光波波段之间建立了桥梁, 构成了一种有效的技术, 用于频率测量, 光学钟&光谱测量.


# 锁模超快激光器, 固体激光器 vs 光纤激光器

![[Pasted image 20231120232111.png]]

脉冲中心波长都在近红外波段

![[Pasted image 20231120232241.png]]

激光产生的光谱只占非常少的一个范围, 需要非线性光学的方法拓展光谱范围.



![[Pasted image 20231120234210.png]]

线性光学: 入射光强比较小, 电场比较弱, 辐射出来的电磁波与入射光场的频率是一样的.

非线性: 入射强, 材料的响应不再是线性的, 产生新的频率分量.

![[Pasted image 20231120234342.png]]

材料的极化 (响应)
$$P=\varepsilon_0[\chi^{(1)}E+\chi^{(2)}E^2+\chi^{(3)}E^3+...]$$

三阶非线性
$$P\:=\:\varepsilon_0\left[\chi^{(1)}E\:+\:\chi^{(3)}|E|^2E\right]\:=\:\varepsilon_0\left[\chi^{(1)}\:+\:\chi^{(3)}|E|^2\right]\:E$$

Kerr 效应
$$n=\sqrt{1+\chi^{(1)}+2\chi^{(3)}\left|E\right|^2}=n_0+n_2I$$
折射率随光强改变.

非线性现象: 自相位调制
$$\frac{\partial A(z,t)}{\partial z}=-jk_0n_2|A|^2A=-j\delta|A|^2A$$
解
$$\boxed{A(z,t)=A(0,t)e^{j\phi_{NL}}=A(0,t)e^{-j\delta|A(z,t)|^2z}}$$
额外的相移, 相移正比于光强.
$$\begin{aligned}|A(z,t)|&=|A(0,t)|\\\\\phi_{NL}&=-\delta|A(z,t)|^2z\end{aligned}$$
- 脉冲的形状&宽度不变, 只是发生相移.
- 脉冲中心部分产生正啁啾.

光纤中常用, 聚焦在空间或者晶体中由于存在衍射会很快发散, 非线性相移很小, 而光纤的波导结构能克服衍射, 光能长距离传输, 所以能积累很强的非线性作用.

$$\varphi_{NL}=\frac{2\pi}{\lambda_0}\cdot n_2\cdot l\cdot z=\frac{2\pi}{\lambda_0}\cdot n_2\cdot\frac P{A_{eff}}\cdot z=\gamma Pz$$
非线性系数
$$\gamma=\frac{2\pi}{\lambda_0}\frac{n_2}{A_{eff}}$$

![[Pasted image 20231120235002.png]]

自相位调制中, 光谱在传输过程中会展宽. 

可利用这种效应进行波长转换 ---- SPM-enabled spectral selection (SESS)

![[Pasted image 20231120235411.png]]

- 滤除最左边&最右边的旁瓣, 非常接近变换极限脉冲.

![[Pasted image 20231120235505.png]]

可实现一定范围内 (800nm-1700nm) 的中心波长连续可调.

通过增加模长面积或者增加光纤长度的方法可以增加脉冲能量.

# 非线性薛定谔方程 NLSE

非线性自相位调制 (正啁啾) =负色散 (负啁啾) ---- 孤子解 Soliton


# 光纤高阶色散

![[Pasted image 20231120235931.png]]

脉冲光谱很宽的时候需要包含更高阶色散. 

广义薛定谔方程 Generalized Nonlinear Schrodinger Equation (GNLSE)
$$j\frac{\partial A}{\partial z}+\frac{\beta_2}2\frac{\partial^2A}{\partial t^2}-j\frac{\beta_3}6\frac{\partial^3A}{\partial t^3}=\gamma|A|^2A$$
- 第二项: GVD
- 第三项: TOD 三阶色散
- Right: SPM

TOD 可看做光孤子的扰动, Soliton 本身非常稳定, 可以自我调节, 会在时域上产生另一个非常弱的脉冲
$$A(z,t)=A_s(z,t)+A_D(z,t)$$
扰动解以由相位匹配条件确定的频率发射色散波：
$$\omega_{D}\approx\omega_{s}-\frac{3\beta_{2}}{\beta_{3}}+\frac{\gamma P_{s}\beta_{3}}{3{\beta_{2}}^{2}}\:\left\{\quad \begin{array}{ll}\beta_{3}(\omega_{s})>0&\implies\omega_{d}>\omega_{s}\\\\\beta_{3}(\omega_{s})<0&\implies\omega_{d}<\omega_{s}\end{array}\right.$$
- 正三阶色散 ---- 中心频率>入射光
- 负三阶色散 ---- 中心频率<入射光

![[Pasted image 20231121000419.png]]

<mark style="background: #FFF3A3A6;">soliton 在传输中出现小的尖峰</mark>, 对应色散波.

---- dispersion wave generation 

# Dispersion wave generation

![[Pasted image 20231121001148.png]]

用这种方法可以得到可见光范围的脉冲, 但他的能量很小. 不适合强场应用.

如何产生能量更高的脉冲?

$$\gamma =\frac{2\pi}{{\lambda}}\frac{n_2}{A_{eff}}$$
- 增加波长
- 减小模场面积 ---- 空心光纤
- 增大非线性项系数

![[Pasted image 20231121001459.png]]

- 利用钛宝石激光( 38fs 脉冲) 射入空心光子晶体光纤, 中间充满惰性气体.
- 通过调节惰性气体气压调节色散与非线性效应, 从而调整色散波的位置

![[Pasted image 20231121001702.png]]

- 产生中心波长 550nm-180nm 的脉冲
- 可以突破一般晶体的波长限制, 可产生波长更短的飞秒脉冲.
- 缺陷: 脉冲能量还是不够高 (几十nJ-百nJ)


![[Pasted image 20231121001901.png]]

- 用充气毛细管 (脉冲压缩中常用) 
- 充气光纤的半径更大, 毛细管直径是大概十倍, 模场面积增大到约100倍
- 同样选择气体&气压使内部波导中处于负色散, 产生高阶估值压缩效应, 输入脉冲从10fs 接近压缩至 1fs, 并产生很强的色散波.

![[Pasted image 20231121002157.png]]

波长可以达到紫外范围.


# 受激拉曼

GNLSE:
$$j\frac{\partial A}{\partial z}+\frac{\beta_2}2\frac{\partial^2A}{\partial t^2}-j\frac{\beta_3}6\frac{\partial^3A}{\partial t^3}=\gamma(1-\frac j{\omega_0}\frac\partial{\partial t})\int_{-\infty}^tR(t^{\prime})|A(z,t-t^{\prime})|^2dt^{\prime}$$
- $-\dfrac{i}{\omega _0}\dfrac{\partial }{\partial t}$ : Self-steepening 

$$R(t)=(1-f_R)\delta(t)+f_Rh_R(t)$$
- $(1-f_R)\delta (t)$ : 瞬时响应 Instantaneous response
- $f_{R}h_R(t)$ : 延时响应 e.g. Raman scattering

熔融石英中, 拉曼散射效应在Kerr 效应中约占20%, 
$$f_{R}=0.18 \quad \text{For fused silica fiber}$$

- 短波部分放大长波部分 ---- 孤子自频移
- 仍然可以理解为对孤子的扰动, 孤子调整自己, 
- 方式为孤子损失一部分能量, 让自己的中心波长红移, 可作为一种连续调整中心波长的方式.
 
![[Pasted image 20231121003006.png]]

![[Pasted image 20231121003245.png]]

- 熔融石英光纤中存在氢氧根的吸收, 长波吸收越来越严重, 在2微米以上损耗非常大.
- 可以使用其它材料的光纤, 如氟化物 (100fs, 中心波长最远可超过4.3微米)

# 两个输入下, 克尔非线性效应

输入 两个频率成分
$$E=E_{01}\cos(\omega_1t)+E_{02}\cos(\omega_2t)$$
极化强度
$$P^{(3)}=\varepsilon_0\chi^{(3)}E^3=\varepsilon_0\chi^{(3)}[E_{01}\cos(\omega_1t)+E_{02}\cos(\omega_2t)]^3]$$

可展开为8项

![[Pasted image 20231121003655.png]]

- <mark style="background: #FF5582A6;">四波混频</mark> (FWM) 是一种由<mark style="background: #FFF3A3A6;">三阶</mark>光学非线性引起的非线性效应，用 $\chi(3)$ 系数来描述。
- 如果至少两个不同的光学频率分量在光纤等非线性介质中一起传播，就会发生四波混频。
- 二阶 ---- 三波混频

![[Pasted image 20231121003947.png]]

- 掺铒光纤产生1.5微米飞秒脉冲, 分出一部分通过非线性光纤产生中心波长在1400nm的光谱, 
- 再叠加, 打到色散位移光纤 (选择色散在一定合适位置, 满足合适相位匹配条件) , 
- 在1700nm的地方产生新的光谱, 滤出压缩得到宽度450fs的脉冲.

$$1550nm+1550nm-1400nm=1700nm$$

转换效率达到 20%

问题: 脉冲能量不会太高, 能量约为40nJ.

如何让能量更高? ---- 使用空心充气光纤!

![[Pasted image 20231121004415.png]]

掺镱光纤激光器, 经过BBO二倍频产生1035nm的光与517nm的光, 再做四波混频, 通过级联空心光纤可产生丰富波长.

![[Pasted image 20231121004626.png]]

- 可达到15级次, 波长69nm. 光子能量更高, 波长更短.
- 不能连续调节


# 二阶非线性效应

$$P=\varepsilon_0[\chi^{(1)}E+\boxed{\chi^{(2)}E^2}+\chi^{(3)}E^3+...]$$
输入
$$E=E_0\cos(\omega t)$$
$$P=\varepsilon_0[\chi^{(1)}E+\boxed{\chi^{(2)}E^2}+\chi^{(3)}E^3+...]$$
$$\color{balck}\cos^2(\omega t){\operatorname*{=}}\frac12[1+\color
{red}\boxed{\color
{black}\cos(2\omega t)}]\quad \longrightarrow\quad\color{black}\text{Second harmonic!}$$


# 相位匹配条件 SHG




- 晶体中任意位置都产生二倍频, 最后在边界处叠加, 我们希望这些子波相长叠加, 这要求相位与z长度无关, 各个子波具有相同的相位.

![[Pasted image 20231121010715.png]]

相位匹配条件:
$$\boxed{\begin{array}{c}\Delta k\equiv k_2-2k_1=0\\k_1=\omega_1c/n(\omega_1)\\k_2=\omega_2c/n(\omega_2)\end{array}}\longrightarrow n(\omega_1)=n(\omega_2)$$
- 要求二倍频的光与基频光对应的折射率是相同的. 
- 但是对于远离吸收共振的频率(波长)，折射率随频率的增加而增加，导致 $n(\omega _1)<n(\omega _2)$，色散作用下无法实现相位匹配。
- 怎么办? ---- 双折射!

有些晶体中存在双折射现象, 如方解石.

![[Pasted image 20231121011050.png]]

![[Pasted image 20231121011059.png]]

光分为:
- o光 与晶体角度&偏振无关
- e光 与晶体角度有关
- 二者偏振垂直

可以调节使得基频光&二倍频分别对应o光&e光, 这样调节特定入射角度就能使晶体中二者的折射率相同从而实现相位匹配条件.

## BBO晶体 对于 o - e SHG


![[Pasted image 20231121011428.png]]

- 负单轴晶体 ---- $n_o>n_e$
- 调节晶体角度, 蓝线向红线靠近

![[Pasted image 20231121011508.png]]

绿色激光笔就是通过二倍频产生的.

![[Pasted image 20231121011723.png]]


## 入射光包含两个频率 ---- 三波混频

$$\begin{aligned}\mathsf{P}^{(2)}&=\varepsilon_0\chi^{(2)}\mathsf{E}^2\\\mathsf{E}&=\mathsf{E}_{01}\cos(\omega_1\mathsf{t})+\mathsf{E}_{02}\cos(\omega_2\mathsf{t})\end{aligned}$$
结果:
$$\cos(\omega_1t)\cos(\omega_2t)=\frac12[\cos(\omega_1+\omega_2)t+\cos(\omega_1-\omega_2)t]$$
- 和频 ---- 中心波长更短
- 差频 ---- 中心波长更长

![[Pasted image 20231121012005.png]]

- 能量守恒
- 动量守恒 ---- 相位匹配条件

## I类匹配与II类匹配

$$\omega _1+\omega _2=\omega _3$$

![[Pasted image 20231121012139.png]]

一类相位匹配条件 ---- $\omega _1$ 与 $\omega _2$ 偏振一样
$$o+o\rightarrow e \quad or \quad   e+e\rightarrow o$$

二类相位匹配条件 ---- $\omega _1$ 与 $\omega _2$ 偏振不同
$$o+e\rightarrow o \quad    e+o\rightarrow e  \quad e+o\rightarrow o \quad   o+e\rightarrow e$$

不同频率产生: 光学参量生成, 光学参量放大, 光学参量振动

![[Pasted image 20231121012607.png]]

- 两个输入 ---- 差频产生 DFG
- 单个输入 ---- 参量下转换 OPG
- 两个输入两个输出 ---- 一个频率放大另一个频率 ---- 光学参量放大 OPA
- 放大装置放入谐振腔中, 就像一个激光一样 ---- 光参量振荡 OPO ---- 中心波长可调的飞秒脉冲

三波混频
$$\begin{aligned}\frac{\partial A_1(z,\tau)}{\partial z}+\left(\frac{1}{v_{g,1}}-\frac{1}{v_{g,3}}\right)\frac{\partial A_1(z,\tau)}{\partial\tau}+\frac{i\beta_{z,1}}{2}\frac{\partial^2A_1(z,\tau)}{\partial\tau^2}&=i\frac{\omega_1d_{eff}}{n_1c}A_3A_2^*e^{-i\Delta kz}\\\frac{\partial A_2(z,\tau)}{\partial z}+\left(\frac{1}{v_{g,2}}-\frac{1}{v_{g,3}}\right)\frac{\partial A_2(z,\tau)}{\partial\tau}+\frac{i\beta_{z,2}}{2}\frac{\partial^2A_2(z,\tau)}{\partial\tau^2}&=i\frac{\omega_2d_{eff}}{n_2c}A_3A_1^*e^{-i\Delta kz}\\\frac{\partial A_3(z,\tau)}{\partial z}+\frac{i\beta_{z,3}}{2}\frac{\partial^2A_3(z,\tau)}{\partial\tau^2}&=i\frac{\omega_3d_{eff}}{n_3c}A_1A_2^*e^{+i\Delta kz}\end{aligned}$$

利用二阶非线性过程得到长波长

基于DFG的中红外飞秒信号源原理图 DFG-based mid-IR fs source
![[Pasted image 20231121013255.png]]

- 分束
	- 泵浦
	- 非线性转换为长波
- 差频
- 产生长波中红外

![[Pasted image 20231121013459.png]]


更长如何获得? 太赫兹波段? ---- <mark style="background: #FF5582A6;">光学整流</mark>
输入 $E=E_0\cos(\omega t)$
$$P^{(2)}=\varepsilon_0\chi^{(2)}E^2=\varepsilon_0\chi^{(2)}[E_0\cos(\omega t)]^2$$
$$\cos^2(\omega t){=}\frac{1}{2}[1+\cos(2\omega t)]$$
- 产生直流项
- 如果输入一个脉冲, 脉冲有一定光谱宽度, <mark style="background: #FFF3A3A6;">光谱内部会产生自我差频</mark>, 产生频率非常低, 几乎为一个<mark style="background: #FFF3A3A6;">直流项</mark>.
<p align="right">---- <mark style="background: #FF5582A6;">光学整流</mark></p>

- 可以产生太赫兹波段脉冲.

![[Pasted image 20231121014003.png]]

太赫兹 ---- 光学和电子学的交界处

通过光整流产生太赫兹

$$E_{THz}(z,\Omega)=-\frac{d_{eff}I_{pump}(\Omega)}{2n_{THz}}\frac{e^{i\frac{\Omega}{c}z(n_{THz}-n_{group})}-1}{n_{group}-n_{THz}}e^{i\frac{\Omega}{c}n_{group}z}$$
- $I_{pump}(\Omega )$ 是脉冲的强度的FT

![[Pasted image 20231121014252.png]]


# 总结

![[Pasted image 20231121014340.png]]

- 二阶非线性
	- 二倍频&和频 ---- 可见光
	- 差频 ---- 中红外
	- 光整流 ---- 太赫兹

- 三阶非线性
	- 自相位调制, 旁瓣滤波 ---- 800-1700 近红外连续可调
	- 色散波 ---- 110nm UV 
	- 受激拉曼散射 ---- 4.3微米 
	- 四波混频 70, 80nm
	- 超连续谱 可见到中红外 时域上不是飞秒脉冲

其他波段  X-ray
- 自由电子激光
- 高次谐波产生 
	- 超快激光与气体相互作用, 产生更高阶次谐波 
	- 可产生阿秒脉冲
- 逆康普顿散射
	- 光子与电子散射, 从电子中获得能量


# Q

拉曼延时的物理图像?



