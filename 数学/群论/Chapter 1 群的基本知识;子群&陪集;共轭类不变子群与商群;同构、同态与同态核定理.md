
#数学/群论

群论: <mark style="background: #FFF3A3A6;">研究对称性问题的数学基础</mark>. 

具体的说，自然界中或者数学中存在着各种各样地所谓“操作”，比如说坐标变换（空间中的平移，旋转，镜像对称，指标对易等等），比如说加法乘法，等等。数学上讲，操作往往代表着一种乘法运算。我们希望通过某个理论来具体的描述这些乘法运算以及他们所蕴含的对称性（操作或多次操作后的某些不变性）。

# 1 群

定义1.1 G为一些元素的集合 $G=\{\cdots , g , \cdot \}=\{g\}$. 在G中定义了乘法运算满足: 
(1) <mark style="background: #FFF3A3A6;">封闭性</mark>   $fg=h, h\in G$ 
(2) <mark style="background: #FFF3A3A6;">结合律</mark>   $(fg)h=f(gh)$
(3) <mark style="background: #FFF3A3A6;">有幺元</mark>   $e\in G ef=fe=f$
(4) <mark style="background: #FFF3A3A6;">有逆</mark>   $f^{-1}f=ff^{-1}=1$ 
则称 𝐺 为一个<mark style="background: #FF5582A6;">群</mark>。

例子: 
(1) 空间反演群
(2) n阶置换群

(3) <mark style="background: #FFB86CA6;">正三角形对称群</mark> 
𝐷4 又称为6阶二面体群，考虑如下正三角形, 

![[数学/群论/附件-骆禹天的MacBook/Drawing 23-09-07 20.25.34.excalidraw]]

保持三角形不变的转动操作：
<center>𝑒：不转，</center>
<center>𝑑：绕 z 轴逆时针转2𝜋 ∕ 3,</center>
<center>𝑓：绕 z 轴逆时针转4𝜋 ∕ 3,</center>
<center>𝑎：绕 1 轴转𝜋, </center>
<center>𝑏：绕 2 轴转𝜋,</center>
<center>𝑐：绕 3 轴转𝜋</center>

乘法表：

| $g_2 g_1$ | e | d | f | a | b | c |
|:--|:--|:--|:--|:--|:--|:--|
| e    | e | d | f | a | b | c |
| d    | d | f | e | c | a | b |
| f    | f | e | d | b | c | a |
| a    | a | b | c | e | d | f |
| b    | b | c | a | f | e | d |
| c    | c | a | b | d | f | e |  

例(4) 整数加法、实数加法、去0实数乘法
例(5) 𝑇(3), 三维欧式空间的平移群
例(6) 𝑆𝑂(3), 三维欧式空间转动群

<mark style="background: #FFF3A3A6;">群的乘法一般不具备可交换性</mark>，即对 ∀𝑓, 𝑔 ∈ 𝐺，一般𝑓𝑔 ≠ 𝑔𝑓。如果对 ∀𝑓, 𝑔 ∈ 𝐺 都有 𝑓𝑔 = 𝑔𝑓，则称 𝐺 为可交换群或<mark style="background: #FF5582A6;">阿贝尔(abelian)群</mark>。

有限群: 群元素有限
无限群: 群元素无限
有限群G的元素个数称为<mark style="background: #FF5582A6;">群的阶</mark>(order) 记为 n(G) or ord(G)

注意区分: <mark style="background: #FF5582A6;">群元素 𝑔 的阶</mark>：由 𝑔 自作用生成的群的阶。群元素的阶也叫周期(period)。

群元素可以用指标或参数唯一标记, 无论是有限群还是无限群.

定理1.1 <mark style="background: #FFF3A3A6;">重排定理</mark>
设 $𝐺 = \{𝑔_\alpha\} , \mu \in 𝐺$，当 $\alpha$ 取遍所有可能值时，乘积 $\mu g_\alpha$ 给出并且仅仅一次给出𝐺 的所有元素。

重排定理指出: <mark style="background: #FFF3A3A6;">群的每一个元素都在乘法表的每一行和每一列出现一次且只出现一次。</mark>


# 2 子群&陪集

## 2.1 子群

定义1.2 设 𝐻 是群 𝐺 的一个子集，若对于与群 𝐺 同样的乘法运算， 𝐻 也构成一个群，则称 𝐻 为 𝐺 的子群。常记为 $H\subset G$。群 𝐺 的非空子集 𝐻 是 <mark style="background: #FF5582A6;">𝐺 的子群</mark>的充要条件为：
(1) 若 $h_{\alpha}, h_{\beta} \subset H$，则 $h_{\alpha}h_{\beta} \subset H$,
(2) 若 $h_{\alpha}\subset H$，则 $h_{\alpha}^{-1}\subset H$。

对于任意一个群 𝐺 ，单位元构成的群和群 𝐺 本身都是 𝐺 的子群，这两种子群称为显然子群或<mark style="background: #FF5582A6;">平庸子群</mark>。除平庸子群外的子群则称为<mark style="background: #FF5582A6;">固有子群</mark>。若不特别说明，一般说子群是指固有子群。

例: 
- 整数加法群是实数加法群的子群
- 沿𝑥 方向的平移是三维平移群的子群
- 绕固定轴𝑘 的转动是𝑆𝑂(3)的子群

Note:   <mark style="background: #FFF3A3A6;">与任一群元对易的所有群元构成一个子群</mark>
$$H_{(g)}=\{h\in G|hg=gh\} \subset G$$

定义1.3 <mark style="background: #FF5582A6;">𝑛 阶循环群</mark>是由元素 𝑎的幂 $𝑎^k$ 组成的，𝑘 = 1,2,…, 𝑛 并
且 $𝑎^n = 𝑒$，记为
$$Z_{n}=\{a,a^2,a^3,\cdots,a^n=e\}$$
Note: <mark style="background: #FFF3A3A6;">循环群的乘法可以交换，故循环群是阿贝尔群</mark>.

Example: <mark style="background: #FFB86CA6;">完美洗牌法</mark> (perfect shuffles)

- 洗一副2𝑛张牌的扑克牌组的操作属于 2𝑛 阶置换群 $𝑆_{2n}$ 。
- 记一次完美洗牌操作为 $𝑃 \in S_{2n}$，则反复操作 𝑃 可生成一个𝑘阶循环子群 $𝑍_k$，即完美洗牌 𝑘 次后牌组会回到初始的状态。

![[数学/群论/附件-骆禹天的MacBook/Pasted image 20230907234936.png]]  ![[数学/群论/附件-骆禹天的MacBook/Pasted image 20230907234946.png]]
<center>外洗法(左)-顶牌在上;   内洗法(右)-顶牌在下</center>

对于2𝑛 = 52 (去掉两张joker)的牌组，采用外洗则 $𝑘 = 8$，采用内洗则 $𝑘 = 52$。

思考：如何证明？
提示：从上往下以0,1,…, 2𝑛 − 1 为牌的位置编号，则经过1次外洗操作后原本在 𝑝位置的牌变到了 2𝑝 𝑚𝑜𝑑 2𝑛 − 1 的位置(若𝑝 < 2𝑛 − 1)。

证明:  

见文件: [[完美洗牌法 推导]]

## 2.2 陪集

定义1.4 设 𝐻 是群 𝐺 的子群，$H = \{h_{\alpha}\}$ 。由固定 𝑔 ∈ 𝐺 ，可生成子群 𝐻 的<mark style="background: #FF5582A6;">左陪集</mark>(left coset)
$$𝑔𝐻 = \{𝑔ℎ_{\alpha}|ℎ_\alpha\in 𝐻 \}$$
同样也可生成<mark style="background: #FF5582A6;">右陪集</mark>(right coset)
$$Hg = \{ℎ_{\alpha}g|ℎ_\alpha\in 𝐻 \}$$
当𝐻 是有限子群时，陪集元素的个数等于 𝐻 的阶.

定理1.2 (<mark style="background: #FFF3A3A6;">陪集定理</mark>)  $𝐻 \subset 𝐺$，则 $g_{1}𝐻$ 和 $g_{2}H$ 要么完全重合，要么没有任何公共元素。(右陪集同理)

证明：设 $𝑢, 𝑣 \in 𝐺, 𝑢, 𝑣 \notin 𝐻$，考虑由 u,v 生成的 𝐻 的两个左陪集，
$$\quad\begin{aligned}
𝑢𝐻 &= \{𝑢ℎ_\alpha  |ℎ_\alpha  \in 𝐻\}\\
vH &= \{vℎ_\alpha  |ℎ_\alpha  \in 𝐻\}
\end{aligned}$$
若 $𝑢𝐻$ 和 $𝑣𝐻$ 有一个公共元素, 
$$𝑢ℎ_\alpha  = 𝑣ℎ_\beta \quad \Rightarrow \quad 𝑣^{-1}𝑢 = ℎ_{\beta }ℎ^{-1}_{\alpha }\in H$$
根据重排定理，在 $\gamma$ 遍历所有可能值时$𝑣^{-1}𝑢ℎ_{\gamma}$ 给出群 𝐻 的所有元素一次且仅一次。故 $𝑣(𝑣^{-1}𝑢ℎ_{\gamma}) =𝑢ℎ_{\gamma}$ 与左陪集 $𝑣ℎ_{\gamma }$ 重合。因此<mark style="background: #FFF3A3A6;">两个陪集只要有1个公共元素，就一定重合</mark>。


定理1.3 (<mark style="background: #FFF3A3A6;">拉格朗日定理</mark>) 有限群的子群的阶，等于该有限群阶的因子。

Note:
- 群的阶? ---- 群的元素个数
- 因子? ----代数上因式分解的因子, 如: $6=1\times6=2\times3$, 所以6的因子有 1,2,3,6.
- 所以表述翻译为: 有限群的子群的元素个数应为这个有限群的元素总数的一个因子.

证明, 或者说, 说明该定理的实质:
- 用有限群(n个元素)中不属于该子群的元素 (左或右) 乘上该子群即可生成一个 (左或右) 陪集, 陪集的元素都是相同的, 比如说m. 
- 由陪集定理: 两个陪集间的元素要么完全相同, 要么完全不同.
- 由上可见: 由于有限群元素有限, 我们总能找到j个拥有相同元素数量(m)的陪集, 这些陪集的元素穷尽了整个有限群. 即 $n=j\times m$. 

推论：<mark style="background: #FFF3A3A6;">阶为素数的有限群没有非平庸子群</mark>。

例12: $D_3$ 的子群与陪集
$D_3$ 的非平庸子群：
$$H_1=\{e,a\},𝐻_2=\{𝑒, 𝑏 \},𝐻_3=\{𝑒, 𝑐\},𝐻_{4} =\{𝑒, 𝑓, 𝑑\}$$
$D_3$ 可按子群$H_1$和它的左陪集分割为：
$$𝐻_1=\{𝑒,𝑎\},b𝐻_1 = \{𝑏, 𝑓\},c𝐻_1 =\{ 𝑐, 𝑑\}$$
也可按子群 $𝐻_4$ 和它的右陪集分割为：
$$𝐻_4 =\{𝑒, 𝑓, 𝑑 \},𝐻_4𝑎 =\{𝑎, 𝑏, 𝑐\}$$

# 3 共轭类、不变子群与商群

## 3.1 共轭类

定义1.5 群 G 中, 元素 f, h <mark style="background: #FF5582A6;">共轭</mark> ($f\sim h$): 
$$\exists g\in G\quad s.t. \quad 𝑔𝑓𝑔^{-1} = ℎ$$
- <mark style="background: #FFF3A3A6;">对称性</mark>: $h\sim f \Rightarrow f\sim h$
- <mark style="background: #FFF3A3A6;">传递性</mark>: $f_{1}\sim h, f_{2}\sim h\Rightarrow f_{1}\sim f_{2}$ 

定义1.6 群 𝐺 的所有互相共轭的元素集合组成 𝐺 的一个类，称为<mark style="background: #FF5582A6;">共轭类</mark>。对于元素 𝑓 所在的类记为: $𝐶𝑙(𝑓)$。

Note: 
- 一个共轭类可用其中任意一个元素作为它的代表，<mark style="background: #FFF3A3A6;">只要给出类中任意一个元素就可求出该类的所有元素</mark>;
$$𝐶𝑙(𝑓)=\{𝑓'|𝑓'= 𝑔_\alpha 𝑓𝑔^{-1}_{\alpha }, 𝑔_\alpha  ∈ 𝐺\} .$$
- e自成一个共轭类;
- 阿贝尔群的每个元素也自成一个共轭类.  $𝑓'= 𝑔_\alpha 𝑓𝑔^{-1}_{\alpha }=𝑔_\alpha 𝑔^{-1}_{\alpha }𝑓=f$
- <mark style="background: #FFF3A3A6;">在一个共轭类中，所有元素的阶相同</mark>，即若某元素有 $𝑓^m = 𝑒$ ，则与 𝑓 共轭的所有元素 𝑓′也满足$𝑓'^{m}= 𝑒$。
$$f'^{m}=(g_{\alpha}fg_{\alpha }^{-1})^{m}=(g_{\alpha}f\underbrace{g_{\alpha }^{-1})(g_{\alpha}}_{e}fg_{\alpha }^{-1})\cdots=g_{\alpha }f^{m}g_{\alpha }^{-1}$$
- 不同共轭类没有公共元素。因此群可以按共轭类分割。

例13: $D_3$ 群的共轭类
$$\begin{align}
&𝐶𝑙(𝑒)= 𝑒 \\
&𝐶𝑙(𝑑)= 𝑑, 𝑓 \\
&𝐶𝑙(𝑎)= 𝑎, 𝑏, 𝑐
\end{align}$$

定理1.4.1 共轭类 𝑔 的元素数目=$𝐻_{(g)}$ 的陪集数目。

Note:
- 共轭类 $Cl(g)=\{g_\alpha gg_\alpha ^{-1}|\forall g_\alpha \in G\}$
- $𝐻_{(g)}$ 表示与 𝑔 对易的所有群元构成的子群。$H_{(g)}=\{h|\forall h\in G, gh=hg\}\subset G$

证明:
- 我们首先尝试论证:  $𝐶𝑙(𝑔)$ 中的元素与 $𝐻_{g}$ 的陪集是一一对应的.

具体地讲, 对于共轭类中的一个元素 $g_{1}gg_{1}^{-1}$ , 有
$$g_1 \in g_{1}H_{(g)}$$ 即 $g_{1}$ 属于 $H_{(g)}$ 的一个陪集. 

并且, 需要考虑到共轭类中, 有可能一个元素的表示不唯一, 即 $g_{2}gg_{2}^{-1}=g_{1}gg_{1}^{-1}$ , 但是仍然有
$$g_2 \in g_{1}H_{(g)}$$
即 $g_{\beta}$ 也属于 $H_{(g)}$ 的同一个陪集. 证明如下:
$$g_{2}gg_{2}^{-1}=g_{1}gg_{1}^{-1}\Rightarrow g(g_{1}^{-1}g_{2})=(g_{1}^{-1}g_{2})g$$
$g$ 与 $(g_{1}^{-1}g_{2})$ 的乘法满足交换律, 即 $(g_{1}^{-1}g_{2})\in H_{(g)}$, 因此,
$$g_{1}(g_{1}^{-1}g_{2})\in g_{1}H_{(g)} \quad \text{即}\quad g_{2}\in g_{1}H_{(g)}$$
综上, 共轭类中每一个元素都与 $H_{(g)}$ 中的一个并且仅仅一个陪集相互对应. 

接着, 反过来, $g_{1}H_{(g)}$ 中, 明显有 $g_{1}$ 对应 $g_{1}gg_{1}^{-1}$, 那么 $g_{1}H_{(g)}$ 中是否有别的元素能对应其他共轭类的元素? 比如说, $g_{2}$ 对应 $g_{2}gg_{2}^{-1}$ . 我们考虑一元素 $h\in g_{1}H_{(g)}$ , $g_{2}=g_{1}h$ ,由于 $h$ 与 $g$ 存在交换律(对易关系), 我们有:
$$g_{2}gg_{2}^{-1}=hg_{1}g(hg_{1})^{-1}=g_{1}gg_{1}^{-1}$$
所以说,  $g_{1}H_{(g)}$ 中只有一个元素 $g_{1}$ 对应共轭类中的仅一个元素 $g_{1}gg_{1}^{-1}$ .
综上, 
$$g_{2}gg_{2}^{-1}=g_{1}gg_{1}^{-1}\iff g_{2}\in g_{1}H_{(g)}$$
最终得证: 共轭类 𝑔 ( $Cl(g)$ ) 的元素数目 (满足 $g_{2}gg_{2}^{-1}\neq g_{1}gg_{1}^{-1}$ 才算不同元素)=$𝐻_{(g)}$ 的左陪集数目。

Note: 根据拉格朗日定理, 有限群的子群的阶，等于该有限群阶的因子. $H_{(g)}$ 的左陪集数目为 $G$ 的阶除以 $H_{(g)}$ 的阶.
$$\frac{ord(G)}{ord(H_{(g)})}$$

定义1.7 设 𝐻 和 𝐾 是群 𝐺 的两个子群，若 $\exists 𝑔\in𝐺, s.t.$
$$𝐾 = 𝑔𝐻𝑔^{-1} = \{𝑘 = 𝑔ℎ𝑔^{-1}|ℎ \in 𝐻\}$$
则称 H 是 K 的<mark style="background: #FF5582A6;">共轭子群</mark>。

- 每个元素都共轭的两个子群;
- 共轭子群也具有<mark style="background: #FFF3A3A6;">对称性</mark>、<mark style="background: #FFF3A3A6;">传递性</mark>。
- 𝐺的每个子群可被当作某个集合的元素，这个“群 𝐺的子群集合”可以分割为不同的<mark style="background: #FF5582A6;">共轭子群类</mark>。

Example: $𝐷_4$ 的非平庸子群
$$𝐻_{1} = \{𝑒, 𝑎\} ,𝐻_2 = \{𝑒, 𝑏\} ,𝐻_{3} = \{𝑒, 𝑐\} ,𝐻_{4} = \{𝑒, 𝑓, 𝑑\}$$
由
$$𝑏𝐻_{1}𝑏^{-1} = \{𝑒, 𝑐\} = 𝐻_{3},\quad  𝑐𝐻_{1}𝑐^{-1} = \{𝑒, 𝑏\} = 𝐻_{2}$$
可得 $\{𝐻_{1},𝐻_{2},𝐻_{3}\}$ 为共轭子群类。
而 $𝐻_{4}$ 则为自共轭子群：
$$𝑔𝐻_{4}𝑔^{-1} = 𝐻_{4}$$

## 3.2 不变子群

定义1.8 设 H 是 G 的子群，若对 $\forall 𝑔 \in 𝐺$，都有 $𝑔𝐻𝑔^{-1} = 𝐻$ ，则称 𝐻 是 𝐺 的<mark style="background: #FF5582A6;">不变子群</mark>，也叫<mark style="background: #FF5582A6;">正规子群</mark>。

- 不变子群自成一个共轭子群类。
- <mark style="background: #FFF3A3A6;">不变子群完整地包含了它每个元素的共轭类的所有元素</mark>。如 $𝐷_{3}$ 的子群 $𝐻_{4} = \{𝑒, 𝑓, 𝑑\}$ 中包含了 $𝐶𝑙 (e) = \{𝑒\}$ 和 $𝐶𝑙(𝑑)= \{𝑑, 𝑓\}$ 的所有元素。

定理1.5 设 H 是 G 的不变子群，对任一固定的$𝑓 \in 𝐺$，在$ℎ_{\alpha }$ 取遍 𝐻 的所有群元时，乘积$𝑓ℎ_{\alpha }𝑓^{-1}$ 一次且仅一次给出 𝐻 的所有元素。

相当于, <mark style="background: #FFF3A3A6;">对不变子群的某一个元素一直做共轭操作, 便能够得到且仅一次得到每一个群元</mark>.

<mark style="background: #FFF3A3A6;">不变子群的左陪集等于右陪集</mark>：
$$𝑔𝐻 = 𝐻𝑔$$
- 亦可由上面结论定义不变子群. 
- 不变子群不区分左右陪集，只说陪集。

Example <mark style="background: #FFB86CA6;">整数加法群是实数加法群的一个不变子群</mark>.

- 事实上, <mark style="background: #FFF3A3A6;">阿贝尔群的任意子群都是不变子群</mark>. 

设 H 是 G 的不变子群。考虑没有公共元素的 H 的陪集串, $𝐻, 𝑔_{1}𝐻, 𝑔_{2}𝐻,\cdots, 𝑔_{i}𝐻,\cdots$ ，假定陪集串穷尽了群 𝐺 ，那么两个陪集 $𝑔_{i}𝐻$ 与 $𝑔_{j}𝐻$ 中元素的乘积，必属于某一个陪集。
$$𝑔_{i}ℎ_{\alpha }𝑔_{j}ℎ_{\beta} = 𝑔_{i}g_{j}\underbrace{g_{j}^{-1}ℎ_{\alpha }𝑔_{j}}_{h_{\gamma }}ℎ_{\beta} = 𝑔_{i}ℎ_{\gamma }ℎ_{\beta}  = 𝑔_{k}ℎ_{\delta } \in 𝑔_{k}𝐻$$
我们也可以此定义<mark style="background: #FF5582A6;">不变子群陪集的乘法</mark>:
$$(g_iH)(g_jH)=g_ig_jH=g_kH$$

## 3.3 商群

定义1.9 设群 𝐺 不变子群 𝐻 生成的陪集串为 $H,g_1H,g_2H,...,g_iH,...$ ，把其中每一个陪集看成一个集合的元素：
$$H\to q_0,g_1H\to q_1,g_2H\to q_2,...,g_iH\to q_i$$
并由不变子群陪集的乘法定义元素之间的乘法规则: $(g_iH)(g_jH)=g_kH\to q_iq_j=q_k$ 则这个集合 $\{q_0,q_1,q_2,...,q_i\}$ 构成了一个群，称为<mark style="background: #FF5582A6;">不变子群的商群</mark>，记为 <mark style="background: #FF5582A6;">𝐺⁄𝐻</mark> 。而 $q_{0}$ 为该该群的单位元。

Example: 商群 $𝐷_{3} ∕ 𝐻_{4}$
𝐷4 的不变子群 $𝐻_{4} = \{𝑒, 𝑓, 𝑑\}$ ，于是商群 $D_{3}∕ 𝐻_{4}$ 的元素：
$$\begin{aligned}H_4\to q_0,aH_4=\{a,b,c\}\to q_1\end{aligned}$$
我们可以验证
$$(aH_4)(aH_4)=a^2H_4=H_4\rightarrow q_1q_1=q_0$$
因此，$𝐷_{3}⁄𝐻_{4} =Z_{2}$ 。

# 4 同构、同态与同态核定理

## 4.1 同构

定义1.10 若从群 G 到群 F 上，存在一个一一对应的满映射(双射) $\Phi$，而且 $\Phi$ 保持群的基本运算规则(乘法)不变; 即群 G 中两个元素乘积的映射，等于两个元素映射的乘积，则称群 G 和群 G <mark style="background: #FF5582A6;">同构</mark>，记为 $𝐺 ≅ 𝐹$。映射 $\Phi$ 称为<mark style="background: #FF5582A6;">同构映射</mark>。

![[数学/群论/附件-骆禹天的MacBook/Pasted image 20230918153344.png]]

- 两个同构的群在数学上可以看成完全相同的一个群。

关于映射:
![[数学/群论/附件-骆禹天的MacBook/Pasted image 20230918230923.png]]

Example 
- 置换群 $S_{3}$ 与 $𝐷_{3}$ 同构
- 互为共轭的两个子群同构
- 正实数乘法群与实数加法群同构

## 4.2 同态

### 同态映射

设存在一个从群 G 到群 F 上的满映射 $\Phi$， $\Phi$ 保持群的基本运算规则(乘法)不变；即群 G 中两个元素乘积的映射，等于两个元素映射的乘积，则称群 G 和群 F  <mark style="background: #FF5582A6;">同态</mark>，记为 $G\sim F$。映射 $\Phi$ 称为<mark style="background: #FF5582A6;">同态映射</mark>。

![[数学/群论/附件-骆禹天的MacBook/Pasted image 20230918231505.png]]

### 同态核

定义1.12 设群 G 与群 F 同态，G 中与 F 的单位元素 $f_{0}$ 对应的元素集合 $𝐻 = \{ℎ_{\alpha }\}$ ，称为<mark style="background: #FF5582A6;">同态核</mark>，也记为 $𝐾𝑒𝑟(\Phi)$ 。

- 即为<mark style="background: #FFF3A3A6;">同态映射中映射到单位元 e 上的元素组成的集合</mark>.

![[数学/群论/附件-骆禹天的MacBook/Pasted image 20230918231752.png]]
### 同态核定理

定理1.6 (<mark style="background: #FFF3A3A6;">同态核定理</mark>) 设群 G 与群 F 同态，则有:
1. 同态核 H 是 G 的不变子群；
2. 商群 $𝐺/𝐻$ 与 F 同构

证明:

思路:
- 结论一 (不变子群)
	- 子群 --- 1
		- 封闭性 --- 2
		- 逆 --- 3
		- 幺元 --- 4
	- 不变
- 结论二 (同构)
	- 乘法规则
	- 单射


证明见:   [[同态核定理证明]]

Example:

- $D_{3}$ 群与 $Z_{2}$ 群
 $D_{3}$ 群与 $Z_{2}$ 群同态，同态核为 $𝐻 = \{𝑒, 𝑑, 𝑓\}$，陪集 $𝐻 = \{𝑎, 𝑏, 𝑐\}$

![[数学/群论/附件-骆禹天的MacBook/Pasted image 20230919002540.png]]

### 自同构映射

定义1.13 群 $𝐺$ 到自身的同构映射 $v$，称为 $𝐺$ 的<mark style="background: #FF5582A6;">自同构映射</mark>. 
$$𝜈: 𝐺 \rightarrow  𝐺$$
-  $\forall g_{\alpha }\in G$ 有 $v(g_{\alpha })=g_{\beta }\in G$ 
- 保持群的乘法规则不变 $v(g_{\alpha }g_{\beta })=v(g_{\alpha  })v(g_{\beta })$
- 单位元映射到单位元 $v(f_{0})\rightarrow f_{0}$
- 互逆的元素映射为互逆的元素

### 自同构群

定义1.14 自同构群
- <mark style="background: #FF5582A6;">自同构映射的乘积</mark>: 定义群 G 的两个自同构 $𝜈_{1}$ 和 $v_{2}$ 的乘积 $𝜈_{1}𝜈_{2}$ 为先实行 $v_{1}$ 再实行 $v_2$ 。
- 恒等映射 $v_{0}$ 指定为单位元，而每个 $v_{i}$ 的逆映射 $v_{i}^{-1}$ 为逆元，则<mark style="background: #FFF3A3A6;">群 𝐺 的所有自同构映射 𝜈 构成一个群</mark>，称为群 G 的<mark style="background: #FF5582A6;">自同构群</mark>，记为 $𝐴(𝐺)$ 或 $𝐴𝑢𝑡(𝐺)$。
- $𝐴𝑢𝑡(𝐺)$ 的子群也称为 $𝐺$ 的一个自同构群。

### 内自同构映射

如果群 𝐺 的自同构映射 $𝜇$ 是群 𝐺 本身某个固定元素 𝑢诱导的共轭变换，则这个映射称为群 𝐺 的<mark style="background: #FF5582A6;">内自同构映射</mark>，
$$g_{\alpha}\rightarrow\mu(g_{\alpha})=ug_{\alpha}u^{-1}$$
一个群 𝐺 的所有内自同构映射的集合构成一个群，称为群 𝐺 的<mark style="background: #FF5582A6;">内自同构群</mark>，记为𝐼𝑛𝑛(𝐺)。

内自同构群的证明。

Example：$Z_{3}$的自同构群和内自同构群

$Z_{3}=\{e,a,a^{2}\}$ 的自同构映射
$$v_{0}:\left\{\quad\begin{aligned}
&e\rightarrow e\\
&a\rightarrow a\\
&a^2\rightarrow a^2
\end{aligned}\right.,\quad v_{1}:\left\{\quad\begin{aligned}
&e\rightarrow e\\
&a\rightarrow a^{2}\\
&a^{2}\rightarrow a
\end{aligned}\right.
$$
自同构群为$Aut(Z_3)=\{v_{0},v_{1}\}≅Z_{2}$

$Z_{3}$ 的内自同构映射为恒等映射，因为是阿贝尔的：
$$ag_{\alpha }a^{-1}=a^{2}g_{\alpha }(a^{2})^{-1}=g_{\alpha }$$
则：$Inn(Z_{3})=\{v_{0}\}$ , 即 $Z_{3}$ 的内自同构群是平庸的。

### 群的中心（center）

群G的<mark style="background: #FF5582A6;">中心</mark>：与G所有元素都对易的元素集合：
$$Z(G)=\{z\in G|\forall g\in G,zg=gz\}$$
- $Z(G)$ 群是G的不变子群；
- 商群 $G/Z(G)$ 与内自同构群 $Inn(G)$ 同构，
$$G/Z(G)≅Inn(G)$$

### 外自同构映射与外同构群

凡事不属于内自同构映射的自同构映射都称为<mark style="background: #FF5582A6;">外自同构映射</mark>。

内自同构映射通常可表示为：$\Phi(g)=ugu^{-1}$ ，其中 $u\in G$，

外自同构映射则也可表示为：$\Phi(g)=\widetilde{u}g\widetilde{u}^{-1}$ ，但 $\widetilde{u}\notin G$ 。不过，$\widetilde{u}$ 可以属于更大的群的元素。

外自同构群：$Out(G)=Aut(G)/Inn(G)$ 。




