
#物理/辐射剂量学

# 2.1 带电粒子与物质相互作用类型

带电粒子和物质相互作用包括:
- 电离
	- $\alpha$ 粒子电离从原子吸引电子
	- $\beta$ 粒子电离从原子排斥电子
- 激发
	- 电子获得能量不足以摆脱原子束缚成为自由电子
	- 激发态的原子是不稳定的, 退激时释放出来的能量以光子的形式发射出来 -- 受激原子发光现象

辐射损失
- 带电粒子和原子核非弹性碰撞
- 重带电粒子, 辐射损失可忽略

# 2.2 带电粒子库伦相互作用类型

由经典碰撞参数和原子半径 a 的相对大小分类:
- 软碰撞 ($b \gg a$)
	- 粒子的库伦场影响整个原子, 将原子激发到较高的能态, 且有时会逐出价电子而将原子电离
- 硬碰撞 ($b\sim a$)
	- 和原子的一个电子相互作用, 逐出电子, $\delta$ 射线
- 原子核相互作用 ($b\ll a$)
	- 弹性散射: 电子路径曲折的原因
	- 轫致辐射

# 2.3 阻止本领

<mark style="background: #FF5582A6;">阻止本领</mark>: 带电粒子在物质中穿过单位长度路程时由于电离、激发过程所损失的能量
$$S=-\frac{dE}{dx}$$
- 单位: $J/m$

Bethe-Block公式：利用量子理论, 并考虑了相对论修正
$$\left(-\frac{dE}{dx}\right)_{ion}=\frac{4\pi z^2e^4}{m_0v^2}NB$$
其中, 
$$B=Z\left[\ln\frac{2m_0v^2}{I}-\ln(1-\beta^2)-\beta^2-\frac{C}{Z}\right]$$
在非相对论条件下：
$$\left(-\frac{dE}{dx}\right)_{ion}\propto\frac{z^2}{v^2}NZ$$
其中, 
- $𝑧$ 为入射带电粒子的荷电荷数
- $𝑣$ 为入射带电粒子的速度
- $𝑁$ 为物质的原子密度 $N=\rho/\mathsf{M}(\text{摩尔质量)*Avo}$
- $𝑍$ 为物质的原子序数

Q: 为什么会有Bragg曲线 (能量损失和穿透深度的关系)？

![[Pasted image 20240625185656.png]]

A: 布拉格峰的来源: 因为 $dE/dx$ 在低能区快速增长

相互作用系数
- 线性阻止本领: $S=-\frac{dE}{dx}$ 
	- 单位: $J/m$
- 质量阻止本领: $\frac{s}{\rho}=-\frac{dE}{\rho dx}$
	- 单位: $J\cdot m^2/kg$

# 2.4 带电粒子的射程

射程 R: 带电粒子在物质中沿初始入射方向行进的最大距离

路程: 带电粒子在物质中实际经过的轨迹

- 对重带电粒子, 射程=路程
- 对轻带电粒子, 射程<路程

![[Pasted image 20240625193427.png]]

1.CSDA 射程 (连续慢化近似射程): 

相当于粒子的慢化近于连续情形下的射程, 借助质量阻止本领, <mark style="background: #FF5582A6;">CSDA 射程</mark>定义为:
$$\Re_{CSDA}=\int_0^{E_0}\frac{dE}{(-dE/dx)}$$
- 单位: $cm$

代入阻止本领
$$\Re=\int_0^{E_0}\frac{dE}{(-dE/dx)}=\frac{m}{z^2}\frac{A}{\rho Z}\frac{m_0}{4\pi e^4N_A}\int_0^{v_0}\frac{v^3}{\ln\frac{2m_ev^2}{I}}dv$$
在相同的入射速度时,
$$\Re\propto\frac m{z^2}\frac A{\rho Z}$$
同种粒子以相同速度, 入射在不同物质中, 如果Z比较接近
$$R\rho\propto\frac AZ\thicksim\text{常数}$$
重要结论:  Z 相近的物质，带电粒子在其中的质量射程近似常数

2.投影射程

粒子在其运行方向上穿过的最远穿透深度 $𝑡_𝑓$ 的期望值
$$<t>=-\frac1{N_0}\int_0^\infty t\cdot t_f(t)dt$$

3.<mark style="background: #FF5582A6;">最大穿透深度</mark> $t_{max}$


# 2.5 $\alpha$ 粒子在标准状态空气中的射程—经验公式

对于 $3\;\rm{MeV} \leq E \leq 7\;\rm{MeV}$ 的 $\alpha$ 粒子
$$R_0 = 0.318 𝐸^{3/2}$$
在不同物质中, 有经验公式:
$$\frac{R\rho }{\sqrt{A}}=\rm{const}$$
相对于空气而言, 有
$$R=\frac{\rho_0\sqrt{A}}{\rho\sqrt{A_0}}R_0=3.2\times10^{-4}\frac{\sqrt{A}}\rho R_0$$


# $\beta$ 射线与物质相互作用

- 电离损失
- 辐射损失

# 2.6 快速电子的电离损失率

$$\left(-\frac{dE}{dx}\right)_{ion}=\frac{2\pi e^4NZ}{m_0v^2}B$$
其中,
$$B=\ln\frac{m_0v^2E}{2I^2(1-\beta^2)}-\ln2\left(2\sqrt{1-\beta^2}-1+\beta^2\right)+(1-\beta^2)+\frac18\Big(1-\sqrt{1-\beta^2}\Big)^2$$
快速电子在物质中穿透本领比重带电粒子大得多!


# 2.7 辐射损失

在单位路程上通过辐射损失的能量叫做<mark style="background: #FF5582A6;">辐射损失率</mark>
$$\left(-\frac{dE}{dx}\right)_{rad}\propto\frac{\mathrm{z}^2E}{m^2}N\mathrm{Z}^2$$
Note: 
- 辐射损失率与入射粒子质量平方成反比, 重带电粒子的辐射损失可以忽略不计.
- 辐射损失率与靶物质 $NZ^2$ 成正比；----打在重元素上韧致辐射更强，屏蔽 $\beta$ 射线的原则

# 2.8 描述韧致辐射的另一个特征参数 ---- 辐射长度



