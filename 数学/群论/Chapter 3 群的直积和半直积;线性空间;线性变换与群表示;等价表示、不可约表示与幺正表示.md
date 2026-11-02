
#数学/群论

# 6 群的直积和半直积

## 6.1 群的直积

### 群的直积

设 $g_{1\alpha }\in G$, $g_{2\beta }\in G$, 则<mark style="background: #FF5582A6;">两个群的直积群</mark> $G_1\otimes G_2=G$ 的元素 $g_{\alpha\beta}$ 为
$$g_{\alpha\beta}=g_{1\alpha}g_{2\beta}=g_{2\beta}g_{1\alpha}$$
由于 $G_{1}$ 和 $G_2$ 间没有乘法规则, 因此在定义直积群时 $g_{1\alpha }$ 和 $g_{2\beta}$ 是<mark style="background: #FFF3A3A6;">可交换</mark>.

- <mark style="background: #FF5582A6;">直积群的元素间乘法</mark>定义为两个子群的元素各自相乘后再组合：
$$g_{\alpha\beta}g_{\alpha'\beta'}=(g_{1\alpha}g_{1\alpha '})(g_{2\beta}g_{2\beta' })=g_{1\alpha ''}g_{2\beta ''}   $$
- 任何一个群乘以其他群的单位元，同构于原来的那个群，因为单位元是恒等变换。
$$\begin{aligned}F_1=\{g_{1\alpha}e_2\}\cong G_1,F_2=\{e_1g_{2\beta}\}\cong G_2\end{aligned}$$
- 两个群的<mark style="background: #FF5582A6;">直积群的单位元</mark>显然是两个单位元的乘积
$$e=e_{1}e_{2}$$
- <mark style="background: #FF5582A6;">直积群的逆元</mark>则是两个子群对应元素的逆元的乘积
$$g_{\alpha \beta }^{-1}=g_{1\alpha }^{-1}g_{2\beta }^{-1}$$

一个群是其两个子群的直积的条件：
(1)每个元素可唯一地<mark style="background: #FFF3A3A6;">分解</mark>为两个子群的分量乘积；
(2)两个子群分量之间的<mark style="background: #FFF3A3A6;">乘积可交换</mark>。

若一个群是其两个子群的直积时:
(1)单位元是两个子群的<mark style="background: #FFF3A3A6;">唯一公共元素</mark>。
(2)两个子群都是<mark style="background: #FFF3A3A6;">不变子群</mark>。

由于<mark style="background: #FFF3A3A6;">直积群各个因子群都是不变子群，故可定义商群</mark> ：
$$G_1\otimes G_2/G_1\cong G_2,G_1\otimes G_2/G_2\cong G_1$$
### 群的半直积

设群 $𝐺_{1} = \{𝑔_{1\alpha} , 𝐺 = {𝑔}$，𝐺!的自同构群为 $𝐴𝑢𝑡(𝐺_{1})$，而 $𝜈_\mu ∈ 𝐴𝑢𝑡(𝐺_1)$。若存在一个同态映射 $𝛷: 𝐺_2 → 𝐴𝑢𝑡(𝐺_1)$ ,即 $𝛷(𝑔_{2\beta}) = 𝜈_{g_{2\beta}}$，则可定义 $𝐺_1$ 和 $G_2$ 的半直积群：
$$G=G_{1}\otimes_\mathbf{s}G_2$$
半直积群 𝐺 的元素 $𝑔_{\alpha \beta}$ 可唯一地写为 $𝑔_{\alpha \beta } = \langle g_{1\alpha },g_{2\beta }\rangle$ 但 $g_{1\alpha }$ 和 $g_{2\beta }$ 是有序的，即<mark style="background: #FFF3A3A6;">不可交换</mark>。 𝐺 的乘法定义为
$$g_{\alpha\beta}g_{\alpha^{\prime}\beta^{\prime}}=\langle g_{1\alpha},g_{2\beta}\rangle\langle g_{1\alpha^{\prime}},g_{2\beta^{\prime}}\rangle=\left\langle g_{1\alpha}\nu_{g_{2\beta}}(g_{1\alpha^{\prime}}),g_{2\beta}g_{2\beta^{\prime}}\right\rangle $$
外自同构映射可写为共轭的形式。

逆元形式？

### 外自同构映射的共轭造

在讲外自同构映射时我们提到，外自同构映射也可写成： $\Phi(g)=\tilde{u}g\tilde{u}^{-1}$ 的形式，但 $\tilde{u}\notin G$，而是属于更大的群的元素。 这个更大的群可通过 𝐺 与另一个群的半直积得到。方法如下： 

定义 𝐺 与 𝐹 的半直积 $𝑁 = 𝐺 \otimes_s 𝐹$，因此要求有一个同态映射 $𝛷: 𝐹 \rightarrow 𝐴𝑢𝑡 (𝐺)$ 并定义群乘法
$$\langle g_\alpha,f_\beta\rangle\langle g_{\alpha^{\prime}},f_{\beta^{\prime}}\rangle=\left\langle g_\alpha\nu_{f_\beta}(g_{\alpha^{\prime}}),f_\beta f_{\beta^{\prime}}\right\rangle $$
考虑一个对 𝐺 的元素的共轭操作：
$$\begin{aligned}&\langle e,f_\beta\rangle\langle g_\alpha,e\rangle\langle e,f_\beta\rangle^{-1}=\langle e,f_\beta\rangle\langle g_\alpha,e\rangle\langle e,f_\beta^{-1}\rangle=\langle e,f_\beta\rangle\langle g_\alpha,f_\beta^{-1}\rangle\\=&\left\langle e\nu_{f_\beta}(g_\alpha),f_\beta f_\beta^{-1}\right\rangle=\left\langle\nu_{f_\beta}(g_\alpha),e\right\rangle\end{aligned}$$
这个 𝐹 可以选为 𝐴𝑢𝑡(𝐺)，而 𝛷 可选为恒等映射。

# 7 线性空间、线性变换与群表示

## 7.1 线性空间

### 线性空间

<mark style="background: #FF5582A6;">线性空间</mark>又叫向量空间，它是定义在数域K上向量集合V。V中定义两运算：
- 加法
- 数乘
两运算都满足封闭性且满足：
- 阿贝尔加法群
	- 结合律
	- 交换律
	- 幺元 (0)
	- 逆 (^-1)
- 数乘（用数域中数字乘向量）
	- $1·x=x$
	- $(ab)x=a(bx)$
	- $a(x+y)=ax+by$
	- $(a+b)x=ax+by$

Note：
<mark style="background: #FF5582A6;">环</mark>：集合$X=\{x_{1},x_{2},\cdots,\}$ 
- 加法交换群
- 乘法满足
	- 结合律
	- 不要求单位元

域（Field）：环的基础上
- 乘法
	- 环基础上，去掉0后也构成乘法交换群

### 线性变换

定义2.2 设 𝑉 是数域 𝐾 上的线性空间，<mark style="background: #FF5582A6;"> 线性变换</mark> 𝐴 是 将 𝑉 映入 𝑉 的线性映射，即对𝑥, 𝑦 ∈ 𝑉, 𝑎 ∈ 𝐾。有:
- $A：V\rightarrow V，A(x)\in V$
- $A(ax+y)=aA(x)+A(y)$

可定义线性变换的数乘、加法和乘法:
 - $(aA) (𝑥) = 𝑎 \cdot 𝐴 (𝑥)$
  - $(𝐴+𝐵)(𝑥) =𝐴(𝑥)+𝐵(𝑥)$
  - $(𝐴𝐵)(𝑥) = 𝐴(𝐵(𝑥))$
若<mark style="background: #FFF3A3A6;">线性变换是双射，则存在逆变换</mark>$A^{-1}$. 

### 基矢与坐标

若线性空间 𝑉 中最多只有 𝑛 个线性独立的向量，则称 𝑉 是 𝑛 维线性空间。在 𝑛 维线性空间中，可选 𝑛 个线性独立的向量 $(𝑒_1, 𝑒_2, \cdots , 𝑒_n)$ 作为 𝑉 的<mark style="background: #FF5582A6;">基</mark>或基矢。在这一基下， 任意 $𝑥 \in 𝑉$ 可用基展开，
$$x=x_1e_1+x_2e_2+\cdots+x_ne_n=\sum_{i=1}^nx_ie_i\:,\quad(x_i\in K)$$
基 $(𝑒_1, 𝑒_2, \cdots , 𝑒_n)$ 也称为<mark style="background: #FF5582A6;">坐标系</mark>，有序数组 $(𝑥_1, 𝑥_2, \cdots , 𝑥_n)$ 称为 𝑥 的<mark style="background: #FF5582A6;">坐标</mark>。常用列矩阵表示基和向量：
$$e_1=\begin{pmatrix}1\\0\\\vdots\\0\end{pmatrix},e_2=\begin{pmatrix}0\\1\\\vdots\\0\end{pmatrix},...,e_3=\begin{pmatrix}0\\0\\\vdots\\1\end{pmatrix},\quad x=\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix}.$$

线性空间V中的线性变换A可以用$n\times n$ 矩阵表示:
$$\begin{pmatrix}A_{11}&A_{12}&\cdots&A_{1n}\\A_{21}&A_{22}&\cdots&A_{2n}\\\vdots&\cdots&\cdots&\vdots\\A_{n1}&A_{n2}&\cdots&A_{nn}\end{pmatrix}$$
$$Ae_j=\sum_{i=1}^nA_{ij}e_i\:,(Ax)_i=\sum_{j=1}^nA_{ij}x_j\:.$$
线性变换的数乘、加法和乘法，也用相应矩阵的数乘、 加法和乘法表示。当 $det(A)\neq0$ 时，存在 𝐴 的逆矩阵$A^{-1}$ ，它对应于 𝐴 的逆变换 $A^{-1}$ 。这时称 𝐴 为<mark style="background: #FF5582A6;">非奇异</mark>的。


### 线性变换

设 𝑉 为 𝑛 维复向量空间， 𝑉 上的<mark style="background: #FFF3A3A6;">全部非奇异线性变换构成一个群</mark>，乘法定义为连续两次线性变换。这个群称为 <mark style="background: #FF5582A6;">𝑛 维复一般线性群</mark> ${GL(n,\mathbb{C})}$，有时我们也记为群 $𝐺𝐿(𝑉, \mathbb{C})$。显然 $𝐺𝐿(n, \mathbb{C})$ 有无穷多个元素。

如果在 𝑉 中选一组基 $(e_1,e_2,\cdots,e_n)$ ，则 $𝐺𝐿(𝑛, \mathbb{C})$ 可表示为 $𝑛\times n$ 非奇异复矩阵，群乘法就是矩阵乘法。群单位元就是 $n\times n$ 单位矩阵，互逆的元素则为矩阵和逆矩阵。

如果只是<mark style="background: #FFF3A3A6;">部分非奇异线性变换构成的群</mark>，则记为 $𝐿(𝑉, \mathbb{C})$ ， 显然它是 $𝐺𝐿(𝑉, \mathbb{C})$ 的子群。

Note:
- 矩阵行列式不为零：非奇异，存在逆矩阵（描述逆变换）
- 例：用$1,x^{2},x^{3},\cdots$构成基底，
- 求导：线性变换（没有逆）相当于：在空间中平移操作

### 线性表示

定义2.4 群 𝐺 到线性空间 𝑉 上线性变换群 𝐿(𝑉, ℂ) 的<mark style="background: #FFF3A3A6;">同态</mark>映射 𝑅 称为 𝐺 的一个<mark style="background: #FF5582A6;">线性表示</mark>，有时也简称表示 (representation)， 𝑉 称为表示空间。当 𝑉 的维数是 𝑛 时， 表示 𝑅 的维数也是 𝑛 。𝑅 的作用可写为
$$𝑅: 𝐺 → 𝐿 (𝑉, \mathbb{C})$$
对 $\forall 𝑔 ∈ 𝐺$，都有 $𝑅(g_\alpha) ∈ 𝐿(𝑉, ℂ)$ 与之对应，而且<mark style="background: #FFF3A3A6;">保持 𝐺 的乘法不变</mark>。即对 $g_{\alpha}, 𝑔_\beta \in 𝐺$，有
$$R(g_{\alpha},g_{\beta}) = 𝑅 (g_{\alpha}) 𝑅 (𝑔_\beta ) $$
显然 𝐺 的单位元素 $g_{0}$ 对应于 𝑉 上的恒等变换，即 $R(g_{0}) = 𝐸_{n\times n}$   , 而互逆群元素对应于互逆变换 $R(g^{-1})= R(g)^{-1}$。

定义2.5 如果群 𝐺 到群 𝐿(𝑉, ℂ) 的映射不仅同态，而且是<mark style="background: #FFF3A3A6;">同构</mark>，即对 $∀g_{\alpha} ∈ 𝐺$，有<mark style="background: #FFF3A3A6;">唯一</mark>的 $𝑅 (g_{\alpha}) ∈ 𝐿(𝑉, ℂ)$ 与之对应，反之任一 $𝑅 (g_{\alpha}) ∈ 𝐿(𝑉, ℂ)$，也唯一对应 $g_{\alpha} ∈ 𝐺$，则称该表示 𝑅 为<mark style="background: #FF5582A6;">忠实表示</mark>。

对于两个同构的群 $𝐺 ≅ 𝐺^′$，若 𝑅 是 𝐺 的一个表示，则 𝑅 也必是 𝐺′ 的一个表示. 当然，两个群可能代表完全不同的物理意义，表示 𝑅 在 𝐺 中和在 𝐺′ 代表的意义也可能完全不同。

### 表示的例子

- 一维平庸表示：1，无论群元什么都映射到1

- <mark style="background: #FFF3A3A6;">矩阵群是自己的忠实表示</mark>. $GL(n,\mathbb{C}),SL(n,\mathbb{C}),O(n,\mathbb{C}),Sp(n,\mathbb{C})$

- 反射群的表示

(1) 恒等变换
$$E:\begin{pmatrix}x\\y\\z\end{pmatrix}=R(E)\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix}\binom xz,$$
(2) 关于xy平面的反射
$$\sigma_k:\quad\begin{pmatrix}x\\y\\-z\end{pmatrix}=R(\sigma_k)\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&-1\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix},$$
(3) 转动子群
$$C_k(\pi)\colon\begin{pmatrix}-x\\-y\\z\end{pmatrix}=R(C_k(\pi))\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}-1&0&0\\0&-1&0\\0&0&1\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix},$$

(4) 空间反演
$$I:\:\begin{pmatrix}-x\\-y\\-z\end{pmatrix}=R(I)\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}-1&0&0\\0&-1&0\\0&0&-1\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}$$
关于原点的反射 𝐼 也有其他三维表示，如: 球坐标下
$$R(I)=\begin{pmatrix}1&0&0\\0&1&0\\0&0&-1\end{pmatrix}$$
但此时它作用的空间并不是坐标 $\overrightarrow{r} (𝑥, 𝑦, 𝑧)$，而是坐标的函数，如有三个函数 $\phi_{i}(\overrightarrow{r}) , 𝑖 = 1,2,3$。其中 i=1,2 是坐标的偶 函数，而 i=3 为坐标的奇函数，则在这三个函数构成的线性空间在对坐标反射的作用下：
$$\begin{pmatrix}\psi_1(\vec{r})\\\psi_2(\vec{r})\\\psi_3(\vec{r})\end{pmatrix}\to\begin{pmatrix}\psi_1(-\vec{r})\\\psi_2(-\vec{r})\\\psi_3(-\vec{r})\end{pmatrix}=\begin{pmatrix}\psi_1(\vec{r})\\\psi_2(\vec{r})\\-\psi_3(\vec{r})\end{pmatrix}=\begin{pmatrix}1&0&0\\0&1&0\\0&0&-1\end{pmatrix}\begin{pmatrix}\psi_1(\vec{r})\\\psi_2(\vec{r})\\\psi_3(\vec{r})\end{pmatrix}$$

(5) 𝑆𝑂(2) 群的表示
二维欧氏空间中选取笛卡尔坐标系 (𝑖, 𝑗)， 则转动群 𝑆𝑂(2) 的二 维表示为：
$$R(C_k(\psi))=\begin{pmatrix}\cos\psi&-\sin\psi\\\sin\psi&\cos\psi\end{pmatrix}.$$
在三维空间中，绕 𝑘 轴的转动群也是 𝑆𝑂(2)，此时在笛卡尔坐标系 (𝑖, 𝑗, 𝑘)下的三维表示为：
$$R\big(C_k(\psi)\big)==\begin{pmatrix}\cos\psi&-\sin\psi&0\\\sin\psi&\cos\psi&0\\0&0&1\end{pmatrix}.$$
这是一个可约表示。

(6) $D_3$ 群 

- $D_3$ 一维表示

$D_3$ 群除了有一个平庸的一维恒等表示, 还有一个非平庸的一维表示.

通过 $D_3$ 的不变子群 $Z_3=\{e,d,f\}$ ,我们知道有一个 $D_3$ 到 $Z_2$ 的同态映射. 而 $Z_2$ 有一维表示
$$Z_2:\{e,d,f\}\rightarrow 1,\{a,b,c\}\rightarrow -1$$
所以 $D_3$ 的非恒等一维表示
$$\begin{align}
&R(e)=R(d)=R(f)=1\\
&R(a)=R(b)=R(c)=-1
\end{align}$$
利用商群求群表示.

- $D_3$ 二维表示

$D_3$ 群本身是对二维平面上三角形进行操作, 所以很自然的应当有二维的忠实表示.
![[数学/群论/附件-骆禹天的MacBook/Pasted image 20231028105422.png]]

$${\begin{array}{c}R(e)=\left(\begin{array}{ll}1 & 0 \\ 0 & 1\end{array}\right), R(a)=\left(\begin{array}{cc}-1 & 0 \\ 0 & 1\end{array}\right) \\ R(d)=\left(\begin{array}{cc}-1 / 2 & -\sqrt{3} / 2 \\ \sqrt{3} / 2 & -1 / 2\end{array}\right), R(b)=\left(\begin{array}{cc}1 / 2 & \sqrt{3} / 2 \\ \sqrt{3} / 2 & -1 / 2\end{array}\right) \\ R(f)=\left(\begin{array}{cc}-1 / 2 & \sqrt{3} / 2 \\ -\sqrt{3} / 2 & -1 / 2\end{array}\right), R(c)=\left(\begin{array}{cc}1 / 2 & -\sqrt{3} / 2 \\ -\sqrt{3} / 2 & -1 / 2\end{array}\right) .\end{array}}$$

- $D_3$ 三维表示

$3=2\otimes 1$

$${\begin{array}{c}R(e)=\left(\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right), R(a)=\left(\begin{array}{ccc}-1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right) \\ R(d)=\left(\begin{array}{ccc}-1 / 2 & -\sqrt{3} / 2 & 0 \\ \sqrt{3} / 2 & -1 / 2 & 0 \\ 0 & 0 & 1\end{array}\right), R(b)=\left(\begin{array}{ccc}1 / 2 & \sqrt{3} / 2 & 0 \\ \sqrt{3} / 2 & -1 / 2 & 0 \\ 0 & 0 & 1\end{array}\right) \\ R(f)=\left(\begin{array}{ccc}-1 / 2 & \sqrt{3} / 2 & 0 \\ -\sqrt{3} / 2 & -1 / 2 & 0 \\ 0 & 0 & 1\end{array}\right), R(c)=\left(\begin{array}{ccc}1 / 2 & -\sqrt{3} / 2 & 0 \\ -\sqrt{3} / 2 & -1 / 2 & 0 \\ 0 & 0 & 1\end{array}\right)\end{array}}$$

$3'=2\otimes 1'$

$${\begin{array}{l}R(e)=\left(\begin{array}{lll}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{array}\right), R(a)=\left(\begin{array}{ccc}-1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1\end{array}\right) \\ R(d)=\left(\begin{array}{ccc}-1 / 2 & -\sqrt{3} / 2 & 0 \\ \sqrt{3} / 2 & -1 / 2 & 0 \\ 0 & 0 & 1\end{array}\right), R(b)=\left(\begin{array}{ccc}1 / 2 & \sqrt{3} / 2 & 0 \\ \sqrt{3} / 2 & -1 / 2 & 0 \\ 0 & 0 & -1\end{array}\right)  \\ R(f)=\left(\begin{array}{ccc}-1 / 2 & \sqrt{3} / 2 & 0 \\ -\sqrt{3} / 2 & -1 / 2 & 0 \\ 0 & 0 & 1\end{array}\right), R(c)=\left(\begin{array}{ccc}1 / 2 & -\sqrt{3} / 2 & 0 \\ -\sqrt{3} / 2 & -1 / 2 & 0 \\ 0 & 0 & -1\end{array}\right) \\\end{array}}$$

- $D_3$ 的六维表示




### 简并子空间展开

量子力学中, 粒子的哈密顿量 H 的对称群 $G=\{g_\alpha \}$ 即
$$\left\langle r'|H| r'\right\rangle=\left\langle g_{\alpha}^{-1} r|H| g_{\alpha}^{-1} r\right\rangle=\left\langle r\left|R\left(g_{\alpha}\right) H R\left(g_{\alpha}\right)^{-1}\right| r\right\rangle=\langle r|H| r\rangle \Rightarrow [R(g _{\alpha}),H]=0$$
$R(g_{\alpha })$ 和 H 有共同的本征态.

设 $|n,\mu\rangle$  为H的本征态, 即:
$$H|n,u\rangle=E_{n}|n,\mu \rangle ,\quad R(g_\alpha )H|n,\mu \rangle=E_{n}R(g_\alpha )|n,\mu \rangle$$
$R(g_\alpha )$ 可用<mark style="background: #FF5582A6;">简并子空间</mark>表示:
$$R(g_{\alpha })|n,\mu \rangle=\sum_{\nu }|n,\nu \rangle \langle n,\nu |R(g_\alpha )|n,\mu \rangle =\sum_{\nu }R_{\nu \mu }|n,\nu \rangle $$
或者坐标表象下
$${\begin{array}{c}\psi_{n \mu}\left(g_{\alpha}^{-1} r\right)=\left\langle r\left|R\left(g_{\alpha}\right)\right| n, \mu\right\rangle=\left\langle r\left|\sum_{v} R_{v \mu}\right| n, v\right\rangle \\ =\sum_{v} R_{v \mu}\langle r | n, v\rangle=\sum_{v} R_{v \mu} \psi_{n \mu}(r)\end{array}}$$



# 8 等价表示, 不可约表示与幺正表示

## 8.1 等价表示

设群$G=\{g_{\alpha }\}$ 在表示空间 V 的表示为 $R=R(g_{\alpha })$ , 即对每一个 $g_{\alpha }$ , 有唯一非奇异线性变换 $R(g_{\alpha })$ 与之对应. 在一组基 $(e_1,e_2,\cdots,e_n)$ 下, $R(g_{\alpha })$ 就是与 $g_\alpha$ 对应的非奇异矩阵.

设 X 是 V 上非奇异矩阵, $det(x)\neq 0$ , 则相似矩阵集合 $\{XR(g_{\alpha })X^{-1}\}$ , 也给出 G 的一个表示.
- 每个群元与相似变换后的矩阵也唯一对应
- 相似变换后的矩阵非奇异
- 相似变换后仍保持 G 的乘法不变
$$XR(g_\alpha g_{\beta })X^{-1}=(XR(g_\alpha )X^{-1})(XR(g_{\beta })X^{-1})$$

$\{XR(g)X^{-1}\}$ 称为 $\{R(g_{\alpha })\}$ 的<mark style="background: #FF5582A6;">等价表示</mark>. 

- 实质：<mark style="background: #FFF3A3A6;">选取线性空间不同基底之间的变换</mark>。

在实际的数学和物理问题中，基的选取是任意的，因此它们对 应的表示矩阵也是等价的。

- 显然, 等价表示的维数相同, 但反之相同维数的表示不一定等价.


## 8.2 不可约表示

### 可约表示

定义 2.7 设 R 是群 G 在表示空间 V 上的一个表示, 若V 存在一个 G 不变的真子空间 W, 则称表示 R 是<mark style="background: #FF5582A6;">可约表示</mark>. 

即群作用 $R(g_\alpha )$ <mark style="background: #FFF3A3A6;">不会将某个真子空间 W 中的向量变到 W 外面</mark>.

当存在不变真子空间 W 时, 总可以选取恰当的基底 $e_{i}(i=1,2,\cdots ,n)$ , s.t. 前m (m<n) 个基底描述 W, 此时 $R(g_{\alpha })$ 和W中的向量具有下面形式:
$$R\left(g_{\alpha}\right)=\left(\begin{array}{cc}C_{\alpha}{} & N_{\alpha} \\ 0 & B_{\alpha}\end{array}\right)\begin{aligned}&\text{m 行}\\&\text{n-m 行}\end{aligned},\quad   Y=\left(\begin{array}{c}
Y \\ 
0
\end{array}\right)\begin{aligned}&\text{m 行}\\&\text{n-m 行}\end{aligned}$$
根据表示的等价性，只要有一个表示是可约的，则它通过相似变换后得到的等价表示也是可约的。


### 线性空间的直和

设 W 和 W' 是线性空间V 的子空间, 若对 $\forall x\in V$ , 可找到 $y\in W, z\in  W'$  , 并<mark style="background: #FFF3A3A6;">唯一</mark>的将 x 表示为
$$x=y+z$$
或者
$$V=W+W',\quad W\cap W'=\{{\varnothing\}}$$
则称 V 是线性空间 W 和 W'的<mark style="background: #FF5582A6;">直和</mark>, 记为
$$V=W\oplus W'$$
若 x 的分解不唯一, 即$x=y+z=y'+z'$, 且$y\neq y',z\neq z'$ 则:
$$y'-y=z'-z\neq0$$
这与 $W \cap W'=\{\varnothing\}$ 矛盾.

所以<mark style="background: #FFF3A3A6;">直和的分解一定是唯一的</mark>.


### 完全可约表示

定义2.8 设群 G 的表示空间 V 可分解为 W 和 W'的直和, $V=W\oplus W'$, 且W和 W' 都是G 不变的, 即对 $\forall y\in W,z\in W'$, V上的表示 R 有:
$$R(g_{\alpha })y\in W,\quad R(g_{\alpha })z\in W'$$
则称: R是<mark style="background: #FF5582A6;">完全可约表示</mark>.

相应, 如果一个表示是可约的, 但不是完全可约的, 称为<mark style="background: #FF5582A6;">可约而不完全可约表示</mark>.

<mark style="background: #FFF3A3A6;">对于完全可约表示，总可以选取一组恰当的基底，使得所有群元的表示矩阵都是对角块状矩阵，即对角子矩阵的直和</mark>。

具体地, 考虑所选取的基底为 $(e_1,e_2,\cdots,e_m,e_{m+1},\cdots,e_n)$ , 其所长空间可以分解为W和W'的直和，其中W的基为 $(e_1,e_2,\cdots,e_m)$ 和 $(e_m,e_{m+1},\cdots,e_n)$ , 于是W&W'中的向量有形式
$$y=\binom Y0,\quad z=\binom0Z$$
表示矩阵 $R(g_\alpha )$ 具有下面形式:
$$R(g_\alpha)=\begin{pmatrix}C(g_\alpha)&0\\0&B(g_\alpha)\end{pmatrix}=C(g_\alpha)\oplus B(g_\alpha)$$
$R(g_\alpha )$ 是矩阵 $C(g_{\alpha }), B(g_{\alpha })$ 的直和.

一般地, <mark style="background: #FFF3A3A6;">一个完全可约表示可能可以写成多个不可约表示的直和, 对于重复出现的不可约表示还可以用其倍数来表示</mark>.
$$R(g_\alpha)=\sum_p\oplus m_pR^p(g_\alpha)$$
其中 $m_p$ 称为<mark style="background: #FF5582A6;">重复度</mark>. 例如:
$$R(g)=\begin{pmatrix}R^1(g)&&&\\&R^1(g)&&\\&&R^2(g)&\\&&&R^3(g)\end{pmatrix}\\=[2R^1(g)]\oplus R^2(g)R^3(g)$$


### 不可约表示

定义2.9 若群 𝐺 的表示 𝑅 的表示空间 𝑉 <mark style="background: #FFF3A3A6;">不存在 𝐺 不变的真子空间</mark>，则 𝑅 是 𝐺 的<mark style="background: #FF5582A6;">不可约表示</mark>，或称为<mark style="background: #FF5582A6;">既约表示</mark>。 

显然如果 𝑅 是不可约的，则: <mark style="background: #FFF3A3A6;">𝑅 的任何一个等价表示都不具有上三角或上三角的形式，当然更不具备准对角的形式</mark>。 

要注意的是，这里说的 $𝑅(g_{\alpha})$的形式是对所有 $g_{\alpha} \in  𝐺$ 而言的， 即如果仅某几个 $g_{\alpha}$ 具有上(下)三角或准对角形式并不代表可约， 而是要<mark style="background: #FFF3A3A6;">所有</mark>的 $g_{\alpha}$ 都满足可约，而且<mark style="background: #FFF3A3A6;">具有同样的可约形式</mark>，才算是可约的。

## 8.3 幺正表示

### 内积

设 𝑉 是数域 𝐾 上的线性空间，将 𝑉 中两个有序向量 𝑥, 𝑦 映为数 $\langle 𝑥| 𝑦\rangle  \in 𝐾$ ，对 $𝑥, 𝑦, 𝑧 \in 𝑉, 𝑎 \in 𝐾$，如满足:
1. $\langle x+y|z> =\langle x|z \rangle  +\langle y|z \rangle$ ,
2. $\langle x|ay \rangle  =a \langle x|y \rangle$
3. $\langle x|y \rangle =\langle y|\mathbf{x}\rangle ^*$
4. $\langle x|\mathbf{x}\rangle >0$ 当 $x\neq 0$
则数 $\langle x|y \rangle$ 称为 x 和 y的<mark style="background: #FF5582A6;">内积</mark>.

由此也可推出：$\langle 𝑥| 𝑦  + 𝑧 \rangle = \langle 𝑥 |𝑦 \rangle +\langle  𝑥 |𝑧 \rangle$ 和 $\langle 𝑎𝑥| 𝑦 \rangle  = a^*\langle  𝑥| 𝑦 \rangle$ 。
### 内积空间

<mark style="background: #FFF3A3A6;">内积空间是定义有内积的线性空间</mark>.

在内积空间中，可定义向量 𝑥 的<mark style="background: #FF5582A6;">长度</mark> $|x|$ 为 $|𝑥| =\sqrt{\langle x|x \rangle }$ 。

若两个向量 𝑥, 𝑦 的内积 $\langle 𝑥| 𝑦 \rangle = 0$ ， 则称两个向量垂直或<mark style="background: #FF5582A6;">正交</mark>。

于是我们总可以选择一组正交归一的基 $𝑒_i$，即 $\langle 𝑒_i| 𝑒_{j}\rangle \delta_{ij}$

我们用的欧式空间是有限维实空间，而酉空间则是有限维复空间，<mark style="background: #FFF3A3A6;">希尔伯特空间则是无限维复空间</mark>。

### 幺正变换

定义2.10 U是内积空间V上的线性变换, 若对 $\forall x,y\in V,U$ 保持x和y的<mark style="background: #FFF3A3A6;">内积不变</mark>, 即
$$\langle Ux|Uy \rangle =\langle x|y \rangle,\forall x,y\in V$$
则称: U为V上的<mark style="background: #FF5582A6;">幺正变换</mark>. 

我们在那内积空间中可以定义某一线性变换A的<mark style="background: #FF5582A6;">厄米共轭变换</mark> $A^\dagger$ : 对 $\forall x,y\in V$ 有
$$\langle Ax|y \rangle =\langle x|A^{\dagger} y \rangle $$
因此, 对 $\forall x,y\in V$ 幺正变换U满足: $\langle Ux|Uy \rangle =\langle x|U^{\dagger }Uy \rangle =\langle x|y \rangle$ . 这意味着:
$$U^{\dagger}U=UU^{\dagger}=E,U^{\dagger}=U^{-1}$$
其中 E 为恒等变换。在选取一组基底后，U 可以用幺正矩阵表示, $U_{ij}$ ，它满足 $𝑈^{∗\dagger }𝑈 = 1$，或者写成 $𝑈_{ji} ^{∗} 𝑈_{jk} = \delta _{ik}$.

### 幺正表示

定义2.11 设 𝑅 是群 𝐺 在内积空间 𝑉 上的表示，且 𝑅 是 𝑉 上幺正变换，则 𝑅 称为 𝐺 的酉表示或<mark style="background: #FF5582A6;">幺正表示</mark>。亦即对 $\forall 𝑔_{\alpha},g_{\beta } \in 𝐺$，有 $𝑅(g_{\alpha }) , 𝑅(g_{\beta })$ 与之对应，而且有:
- 保持群的乘法
$$R(g_\alpha g_\beta)=R(g_\alpha)R(g_\beta),$$
- 保群的逆元
$$R(g_\alpha)^\dagger=R(g_\alpha)^{-1}=R(g_\alpha^{-1})$$

在一组正交归一的基下， $𝑅(g_{\alpha })$ 可用矩阵表示，则: <mark style="background: #FFF3A3A6;">矩阵的复共轭等于逆元的矩阵</mark>
$$R(g_{\alpha})_{ji}^{*}=[R(g_{\alpha})^{-1}]_{ij}=R(g_{\alpha}^{-1})_{ij}$$

定理2.1 <mark style="background: #FFF3A3A6;">幺正表示可约，则完全可约</mark>. 即如果群 𝐺 的表示 𝑅 是可约幺正表示, 则 𝑅 是完全可约的. 

证明: 若幺正表示 𝑅 可约，则<mark style="background: #FFF3A3A6;">可以选取恰当的基使得它具有上三角形式</mark>:
$$R(g_\alpha)=\begin{pmatrix}C_\alpha&N_\alpha\\0&B_\alpha\end{pmatrix}\Longrightarrow R(g_\alpha)^\dagger=\begin{pmatrix}C_\alpha^\dagger&0\\N_\alpha^\dagger&B_\alpha^\dagger\end{pmatrix}$$
由幺正表示矩阵与自己的厄米共轭矩阵互逆: $𝑅(g_{\alpha })R(g_{\alpha})^{\dagger } = 𝑅(g_{\alpha })^{\dagger }R(g_{\alpha }) = 1$，有:
$$\begin{aligned}&1=\begin{pmatrix}C_\alpha&N_\alpha\\0&B_\alpha\end{pmatrix}\begin{pmatrix}C_\alpha^\dagger&0\\N_\alpha^\dagger&B_\alpha^\dagger\end{pmatrix}=\begin{pmatrix}C_\alpha C_\alpha^\dagger+N_\alpha N_\alpha^\dagger&N_\alpha B_\alpha^\dagger\\B_\alpha N_\alpha^\dagger&B_\alpha B_\alpha^\dagger\end{pmatrix}\\&\Longrightarrow{C_\alpha C_\alpha^\dagger+N_\alpha N_\alpha^\dagger=1,N_\alpha B_\alpha^\dagger=0,B_\alpha N_\alpha^\dagger=0,B_\alpha B_\alpha^\dagger=1}\end{aligned}$$
以及
$$\begin{array}{c}
1 = \begin{pmatrix}C_\alpha^\dagger&0\\N_\alpha^\dagger&B_\alpha^\dagger\end{pmatrix}\begin{pmatrix}C_\alpha&N_\alpha\\0&B_\alpha\end{pmatrix} = \begin{pmatrix}C_\alpha^\dagger C_\alpha&C_\alpha^\dagger N_\alpha\\N_\alpha^\dagger C_\alpha&N_\alpha^\dagger N_\alpha+B_\alpha^\dagger B_\alpha\end{pmatrix}\\\implies{N_\alpha^\dagger N_\alpha+B_\alpha^\dagger B_\alpha = 1,C_\alpha^\dagger N_\alpha = 0,N_\alpha^\dagger C_\alpha = 0,C_\alpha^\dagger C_\alpha = 1}
\end{array}$$
由于 $B_\alpha B_{\alpha }^{\dagger }=1\Rightarrow B_{\alpha }^{\dagger }B_{\alpha }=1$ , 可得: $N_{\alpha }^{\dagger }N_{\alpha }=0\Rightarrow N_{\alpha }N_{\alpha }^{\dagger }=0$ .

同理: $C_{\alpha }^{\dagger }C_{\alpha }=C_{\alpha }C_{\alpha }^{\dagger }=1$ . 由于 $B_{\alpha }, C_{\alpha }$ 都是非奇异的.

所以由 $\begin{aligned}C_\alpha^\dagger N_\alpha=0,N_\alpha^\dagger C_\alpha=0,N_\alpha B_\alpha^\dagger=0,B_\alpha N_\alpha^\dagger=0\end{aligned}$ 可得: $N_{\alpha }=0$. 因此 $R(g_{\alpha })$ 具有完全可约的形式:
$$R(g_\alpha)=\begin{pmatrix}C_\alpha&0\\0&B_\alpha\end{pmatrix}$$

量子力学中，表示空间是复内积的希尔伯特空间. <mark style="background: #FFF3A3A6;">群表示保持矢量内积模方不变 (归一性)，因而都是幺正或反幺正表示</mark>.

### 量子力学中的时间反演

考虑一个波函数 $\psi(\overrightarrow{x},t)$ 是薛定谔方程的解:
$${i \hbar \frac{\partial \psi(\vec{x}, t)}{\partial t}=\left(-\frac{\hbar^{2}}{2 m} \nabla^{2}+V(\vec{x})\right) \psi(\vec{x}, t)}$$
在时间反演后 $\psi (\overrightarrow{x},t)$ 并不是薛定谔方程的解. 但确是薛定谔方程求复共轭后的解:
$${-i \hbar \frac{\partial \psi^{*}(\vec{x}, t)}{\partial t}=\left(-\frac{\hbar^{2}}{2 m} \nabla^{2}+V(\vec{x})\right) \psi^{*}(\vec{x}, t)}$$
原方程的解是一个能量的本征态: $\psi (\overrightarrow{x},t)=u_n(\overrightarrow{x})e^{-iE_nt/\hbar}$

考虑: <mark style="background: #FFF3A3A6;">能量本征态的共轭后再作时间反演后则是原薛定谔方程的解</mark>
$$\psi^{*}(\overrightarrow{x},-t)=u^*_n(\overrightarrow{x})e^{-\dfrac{iE_nt}{\hbar}}$$
因此, 我们猜测: <mark style="background: #FFF3A3A6;">时间反演操作对波函数的作用应该和复共轭有关</mark>.

### 反幺正变换

定义2.1sp 考虑量子态 $| \alpha \rangle$ 和 $|\beta \rangle$ , 在变换 𝜃 的作用下变为
$${|\alpha\rangle \rightarrow|\tilde{\alpha}\rangle=\theta|\alpha\rangle,|\beta\rangle \rightarrow|\tilde{\beta}\rangle=\theta|\beta\rangle}$$
并且满足:
- 振幅取复共轭 $\langle \tilde{\beta  }|\tilde{\alpha }\rangle =\langle \beta| \alpha  \rangle^{*}=\langle \alpha |\beta \rangle$
- 反线性变换 $\theta (c_{1}|\alpha \rangle +c_{2}|\beta \rangle )=c_1^*\theta |\alpha \rangle +c_2^*\theta |\beta \rangle$
则称: 变换 $\theta$ 为<mark style="background: #FF5582A6;">反幺正变换</mark>.

- 反幺正变换依然保持概率密度, 或者说模不变.

反幺正变换 $𝜃$ 总可以写成
$$𝜃 = 𝑈𝐾$$
其中, 𝑈 是一个<mark style="background: #FF5582A6;">幺正变换</mark>，而 𝐾 是一个<mark style="background: #FF5582A6;">复共轭变换</mark>，它<mark style="background: #FFF3A3A6;">把态的复系数变为其复共轭</mark>
$$K(c|\alpha \rangle )=c^*K|\alpha \rangle$$
对于选定的正交基, 可作正交基展开: $|\alpha >=\sum_{\alpha }|\alpha  \rangle \langle \alpha |\alpha \rangle$ , $K$ 的作用下, 
$${K|\alpha\rangle=K \sum_{a}|a\rangle\langle a | \alpha\rangle=\sum_{a}\langle a | \alpha\rangle^{*} K|a\rangle=\sum_{a}\langle a | \alpha\rangle^{*}|a\rangle}$$

于是, $\theta$ 的作用下, 
$$\begin{aligned}|\tilde{\alpha}\rangle&=\sum_a\langle a|\alpha\rangle^*U|a\rangle,|\tilde{\beta}\rangle=\sum_b\langle b|\beta\rangle^*U|b\rangle\Longrightarrow\langle\tilde{\beta}|=\sum_b\langle b|\beta\rangle\langle b|U^\dagger\\\Longrightarrow\langle\tilde{\beta}|\tilde{\alpha}\rangle&=\sum_{a,b}\langle a|\alpha\rangle^*\langle b|\beta\rangle\langle b|U^\dagger U|a\rangle=\sum_{a,b}\langle\alpha|a\rangle\langle b|\beta\rangle\delta_{ab}=\langle\alpha|\beta\rangle\end{aligned}$$

- <mark style="background: #FFF3A3A6;">反幺正变换=幺正变换+复共轭变换</mark>


### 时间反演算符

时间反演算符 $\Theta$ 的性质应具有哪些性质?

对动量本征态, 时间反演下, 本征值变为负数并且乘上一个相位因子.
$$\Theta |p \rangle =e^{i\xi}|-p \rangle $$
对角动量和自旋也类似.

考虑在 $t=t_0=0$ 时刻, 某一个态时间演化 $\delta t$ 时间后,
$$|\alpha ,t=t_{0};t=\delta t \rangle \approx(1-i\frac{H}{\hbar}\delta t)|\alpha \rangle $$
先对一个态作用时间反演 $\Theta$, 再经过 $\delta t$ 时间的演化
$$\left(1-i\frac{H}{\hbar}\delta t\right)\Theta |\alpha \rangle $$
- 那么这种情况下的结果应该相当于将动量反转后演化 $\delta t$ 时间, 或者说反向运动了 $\delta t$ 时间.
- 如果时间反演对称性存在, 这相当于先把态演化回 $-\delta t$ 的状态在反转动
$$\Theta \left(1-i\frac{H}{\hbar}(-\delta t)\right)|\alpha \rangle $$
$$\Rightarrow -iH\Theta | \quad \rangle =\Theta (iH)|\quad \rangle $$

假定 $\Theta$ 为幺正, 其没有反线性变换, 可以直接把 i 提出来消去
$$-H\Theta =\Theta H$$
考虑能量本征函数
$$H\Theta |n \rangle =-\Theta H|n \rangle =-E_{n}\Theta |n \rangle $$
- $\Theta |n \rangle$ 是负能态, 且越高的能级负的越多, 这是违反现实的, 
- 再考虑自由粒子的哈密顿量: $H=\dfrac{p^2}{2m}$ , 时间反演下 $p\longrightarrow -p$ , 无法得到: $\Theta ^{-1} H \Theta =-H$ ;

所以时间反演不应当是幺正的.

那么考虑时间反演算符 $\Theta$ 是反幺正的如何?

$$\Theta (iH)=-i\Theta   H,\quad H\Theta =\Theta H$$
作用在能量本征态上 $|n \rangle$,  它的时间反演的能量本征态 $\Theta |n \rangle$ 为
$$H\Theta |n \rangle =\Theta H|n \rangle =E_{n}\Theta  |n \rangle $$
我们得到了一个正能量态, 这是贴合现实的.

因此我们得到结论: <mark style="background: #FFF3A3A6;">时间反演算符是反幺正算符</mark>.

### 算符的时间反演

算符在时间反演下如何变化?

考虑算符 A, $|\gamma \rangle =A^{\dagger} |\beta \rangle ,\langle \gamma |=\langle \beta |A$ , 于是
$$\langle \beta |A|\alpha \rangle =\langle \gamma |\alpha \rangle =\langle \tilde{\alpha }|\tilde{\gamma }\rangle =\langle \tilde{\alpha }|\Theta A^\dagger|\beta \rangle =\langle \tilde{\alpha }|\Theta A^{\dagger}\Theta ^{-1}|\tilde{\beta }\rangle $$

综上, 对于厄米算符:
$$\langle \beta |A|\alpha \rangle =\langle \tilde{\alpha }|\Theta A\Theta ^{-1}|\tilde{\beta }\rangle $$

厄米算符在时间反演下, 定义:
$$\Theta A\Theta ^{-1}=\pm A$$
$$\langle \beta |A|\alpha \rangle =\pm \langle \tilde{\beta }|A|\tilde{\alpha }\rangle^* $$
其中,
- 取+ : 偶变换
- 取- : 奇变换

















