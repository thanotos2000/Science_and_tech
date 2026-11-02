---
tags:
  - 光学/非线性光学/光孤子
---


# 1 历史

1834年, Russell 观察到了孤子现象:
> 1. 他观察到孤立波，这是一种长而浅的永久形式的水波，因此他推断出它们的存在；这是他最重要的成果； 
> 2. 孤立波在深度 $h$ 均匀的通道中的传播速度 $c$ 由以下公式给出：$c^2 = g(h +\eta )$，其中, $\eta$ 是波的振幅，$g$ 是重力。


Korteweg-de Vries (KdV) 方程

控制在浅水通道中传播的长一维、小振幅、表面重力波的非线性演化方程
$$\frac{\partial\eta}{\partial\tau}=\frac32\sqrt{\frac gh}\frac\partial{\partial\xi}\left(\frac12\eta^2+\frac23\alpha\eta+\frac13\sigma\frac{\partial^2\eta}{\partial\xi^2}\right),\quad\sigma=\frac13h^3-Th/(\rho g)\tag{1.1.1}$$
其中,
- $\eta$ 是波在平衡水平 $h$ 之上的表面高度，
- $a$ 是与液体匀速运动相关的任意小常数，
- $g$ 是引力常数，
- $T$ 是表面张力，
- $\rho$ 是密度
- （术语“长”和“小”是指与通道的深度相比）。

方程（1.1.1）可以通过变换
$$t=\frac{\mathrm{l}}2\sqrt{g/(h\sigma)}\:\tau,\quad x=-\sigma^{-1/2}\xi,\quad u=\frac{\mathrm{l}}2\eta+\frac{\mathrm{l}}3\alpha  \tag{1.1.2}$$
转化为无量纲形式
$$u_t+6uu_x+u_{xxx}=0$$
其中, 下标表示偏微分.

KdV 方程具有孤立波解:
$$u(x,t)=2\kappa^2\sinh^2\left\{\kappa(x-4\kappa^2t-x_0)\right\}\tag{1.1.3}$$
