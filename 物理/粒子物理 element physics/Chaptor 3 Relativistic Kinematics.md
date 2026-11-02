#物理/粒子物理
# 3.1 Lorentz Transformation

![[物理/粒子物理 element physics/附件/Pasted image 20231122104501.png]]

<mark style="background: #FF5582A6;">Lorentz Trans</mark>:
$$\begin{aligned}&x'=\gamma\:(x-\imath t)\\&y'=y\\&z'=z\\&t'=y\:(t-\frac{v}{c^2}x)\end{aligned}$$
where
$$\gamma \equiv \frac{1}{\sqrt{1-\dfrac{v^2}{c^2}}}$$
inverse trans:

$$\begin{aligned}x&=\gamma(x^{\prime}+vt^{\prime})\\y&=y^{\prime}\\z&=z^{\prime}\\t&=\gamma\left(t^{\prime}+\frac v{c^2}x^{\prime}\right)\end{aligned}$$

- <mark style="background: #FF5582A6;">The relativity of simultaneity</mark>:

Two events occur at the same time ($t_A=t_B$) in S, but at different locations, then they do not occur at the same time in S
$$t_{A}^{\prime}=t_{B}^{\prime}+\frac{\gamma v}{c^{2}}(x_{B}-x_{A})$$


- <mark style="background: #FF5582A6;">Lorentz contraction</mark>

A moving object is shortened by a factor of $\gamma$, as compared with its length in the system in which it is at rest.
$$L'=\gamma L$$

- <mark style="background: #FF5582A6;">Time dilation</mark>

Moving clock run slow.
$$T=\gamma T'$$
- <mark style="background: #FF5582A6;">Velocity addition</mark>

Suppose a particle is moving in the x diretion at speed $u'$ , with respect to S'. 

With respect to S, it travels a distance
$$\Delta x=\gamma (\Delta x'+v \Delta t')$$
in a time
$$\Delta t=\gamma [\Delta  t'+(v/c^2)\Delta x']$$
$$\Rightarrow \quad \frac{\Delta x}{\Delta t}=\frac{\Delta x'+v\:\Delta t'}{\Delta t'+(v/c^2)\Delta x'}=\frac{(\Delta x'/\Delta t')+v}{1+(v/c^2)(\Delta x'/\Delta t')}.$$
$\Delta x/\Delta t=u,\quad \Delta x'/\Delta t'=u'$ , so
$$u=\frac{u^{\prime}+v}{1+(u^{\prime}v/c^{2})}$$

The speed of light is the same in all internal systems:
$$u'=c,\quad \longrightarrow \quad u=c$$ 
# Four-vectors

Position-time four-vector $x^{\mu },\mu =0,1,2,3$ :
$$x^{0}=ct,\quad x^{1}=x,\quad x^{2}=y,\quad x^{3}=z$$

Lorentz trans:
$$\begin{aligned}x^{0\prime}&=\gamma(x^0-\beta x^1)\\x^{1\prime}&=\gamma(x^1-\beta x^0)\\x^{2\prime}&=x^2\\x^{3\prime}&=x^3\end{aligned}$$
where $\beta \equiv \dfrac{v}{c}$

Lorentz transformation:
$$\boxed{x^{\mu^{\prime}}=\sum\limits_{\nu=0}^{3}\Lambda_{\nu}^{\mu}x^{\nu}\quad(\mu=0,1,2,3)}$$
$\Lambda _\nu ^\mu$ is the elements of a matrix $\Lambda$
$$\Lambda=\left(\begin{array}{cccc}\gamma&-\gamma\beta&0&0\\-\gamma\beta&\gamma&0&0\\0&0&1&0\\0&0&0&1\end{array}\right)$$
i.e.
$$\Lambda =\begin{pmatrix} 1&0&0&0\\0&-1&0&0 \\  0&0&-1&0 \\0&0&0&-1 \end{pmatrix}$$

Einstein's summation convention:
$$x^{\mu^{\prime}}=\Lambda_{\nu}^{\mu}x^{\nu}$$

Under the change of coordinates, there is a combination remains the same 
---- invariant:
$$I\equiv(x^{0})^{2}-(x^{1})^{2}-(x^{2})^{2}-(x^{3})^{2}=(x^{0'})^{2}-(x^{1'})^{2}-(x^{2'})^{2}-(x^{3'})^{2}$$

Now, I would like to write this invariant in the form of a sum: $\sum\limits_{\mu =0}^{3}x^\mu x^\mu$ , but there are those three irritating minus signs.

To keep track of them, we introduce the <mark style="background: #FF5582A6;">metric</mark> $g_{\mu \nu }$
$$g=\left(\begin{array}{cccc}1&0&0&0\\0&-1&0&0\\0&0&-1&0\\0&0&0&-1\end{array}\right)$$

Thus, the invariant I
$$I=\sum_{\mu=0}^{3}\sum_{\nu=0}^{3}g_{\mu\nu}x^{\mu}x^{\nu}=g_{\mu\nu}x^{\mu}x^{\nu}$$

We define the covariant four-vector $x_\mu$ (index down)
$$x_{\mu }\equiv g_{\mu \nu }x^{\nu }$$
$$I=x_\mu x^\mu $$

We can define a four-vector, $a^\mu$, as a four-component object :
$$a^{\mu'}=\Lambda _\nu ^\mu a^\nu $$
$$a_\mu =g^{\mu \nu }a_\nu $$
We can go back from covariant to contravariant by reversing the signs again:
$$a^{\mu}=g^{\mu\nu}a_{\nu}$$
where $g^{\mu \nu }$ are the elements in the matrix $g^{-1}$.

For any four-vectors $a^\mu$ and $b^\mu$ , we have
$$a^{\mu}b_{\mu}=a_{\mu}b^{\mu}=a^{0}b^{0}-a^{1}b^{1}-a^{2}b^{2}-a^{3}b^{3}$$
is invariant. 

- We shall refer to it as the scalar product of a and b; it is the four-dimensional analog to the dot product of two three-vectors
- Note: there is no four-vector analog to the cross product.
$$a\cdot b \equiv  a_\mu b^\mu =a^{0}b^{0}-\bf{a}\cdot \bf{b}$$

We can classify all four-vectors by
- $a^2>0$ : $a^\mu$ is timelike;
- $a^2<0$ : $a^\mu$ is spacelike;
- $a^2=0$ : $a^\mu$ is light like.









