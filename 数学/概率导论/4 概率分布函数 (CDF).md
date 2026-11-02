
- 描述随机变量"落地"位置累积概率的函数,
- 能够统一描述离散型和连续型随机变量的最通用形式.

```ad-def
**概率分布函数 (Cumulative Distribution Function, CDF)**:

设 $X$ 是一个随机变量 (可以是离散的, 也可以是连续的), $x$ 是任意实数, 则函数:
$$F_X(x)=\mathrm{P}(X\leqslant x)=\left\{\begin{aligned}\sum_{k\leqslant x}p_X(k),&\text{若 }X\text{ 是离散的},\\\int_{-\infty}^xf_X(t)\mathrm{d}t,&\text{若 }X\text{ 是连续的}.\end{aligned}\right.$$
称为随机变量 $X$ 的概率分布函数.
```

- 累积意味着 $F_X (x)$ 将 $X$ 取值的概率由 $−\infty$ 累计到  $x$;
- 随着 $x$ 的增加, 这个概率会不断积累到 1.

性质: 
1. 随 $x$ 增加, $F_X(x)$ 不会减小.
2. 有界性: $0 \le F_X(x) \le 1$
	*   $\lim_{x \to -\infty} F_X(x) = 0$ (不可能取值小于负无穷)
	*   $\lim_{x \to +\infty} F_X(x) = 1$ (必然取值小于正无穷)
3.  右连续性: $F(x) = F(x+0)$.
	- 这是一个数学上的约定, 确保在离散跳跃点上的函数值定义明确. 


离散随机变量的 CDF 呈阶梯状 (是一个阶梯函数).

![[Pasted image 20260109212625.png]]

特征: 
* 在每一个可能的取值点 $x_k$ 处, 函数图像会向上跳跃, 跳跃的高度等于该点的概率 $P(X=x_k)$.
* 在跳跃点上, $F_X (x)$ 取较大的那个值, 即 $F_X (x)$ 保持右连续

连续型随机变量 CDF 是一条连续曲线.

![[Pasted image 20260109212920.png]]


* 特征: 函数是连续的 (没有跳跃). 
* 分布函数的导数就是概率密度函数.
$$f_X(x)=\frac{\mathrm{d}F_X}{\mathrm{d}x}(x)$$
