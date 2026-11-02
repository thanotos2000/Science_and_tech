
#物理/经典力学

# 1.1 Mechanics of a Particle

Velocity
$$
	\mathbf{v}=\frac{d\mathbf{r}}{dt} \tag{1.1.1}
$$

Linear momentum
$$
\mathbf{p}=m\mathbf{v}\tag{1.1.2}
$$

Newton's second law
$$
\mathbf{F}=\frac{d\mathbf{p}}{dt}=\frac{d}{dt}(m\mathbf{v})=m\mathbf{a}\tag{1.1.3}
$$

Acceleration
$$
\mathbf{a}=\frac{d^2\mathbf{r}}{dt^2}\tag{1.1.4}
$$

> **Conservation Theorem for the Linear Momentum of a Particle**:
> If the total force $\mathbf{F}$ is zero, then $\dot{p}=0$, and the linear momentum $\mathbf{p}$ is conserved.
> 	$$\mathbf{p}=const \tag{1.1.5}$$

Angular momentum
$$
\mathbf{L}=\mathbf{r}\times\mathbf{p}\tag{1.1.6}
$$

Torque
$$
\mathbf{N}=\mathbf{r}\times\mathbf{F}\tag{1.1.7}
$$

$$
\mathbf{N}=\mathbf{r}\times\mathbf{F}=\mathbf{r}\times\frac{d}{dt}(mv)=\frac{d}{dt}(\mathbf{r}\times m\mathbf{v})=\frac{d}{dt}\mathbf{L}\tag{1.1.8}
$$

> **Conservation Theorem of the Angular Momentum of a Particle**:
> If the total torque is zero then the angular momentum is conserved.
> 
> $$\mathbf{N}=0\quad \Rightarrow \quad \mathbf{L}=const \tag{1.1.9}$$

Next we consider the work done by the external force F upon the particle in going from point 1 to the point 2. By definition, this work is 
$$
W_{12}=\int_1^{2}\mathbf{F}\cdot ds=\frac{m}{2}(v_2^2-v_1^2)\tag{1.1.10}
$$

Kinetic energy
$$
T=\frac{1}{2}mv^2\tag{1.1.11}
$$

If the force field is such that the work $W_{12}$ is the same for any physically possibly path between points 1 and 2, then the force field (and the system) is said to be **conservative**. Imagining the particle taken from point 1 to point 2 by one path and then being returned by another path, the work down around such a closed circuit is 0.
$$
\oint\mathbf{F}\cdot ds=0\tag{1.1.12}
$$

^6ae1e0

A necessary and sufficient condition that the work be independent of the path is that $\mathbf{F}$ be the gradient of some scalar function of position:
$$
\mathbf{F}=-\nabla V(\mathbf{r})\tag{1.1.13}
$$
where $V$ is called **potential** .

If $W_{12}$ is independent of the path, it should be possible to express $W_{12}$ as the change in a quantity that depends only upon the position of the end points. This quantity may be designated by $-V$, so that for a differential path length we have the relation
$$
\mathbf{F}\cdot ds=-dV\quad \text{or}\quad F_s=-\frac{\partial V}{\partial s}\tag{1.1.14}
$$

For a conservative system, the work done by the force is
$$
W_{12}=V_1-V_2\quad\Rightarrow\quad T_1+V_1=T_2+V_2\tag{1.1.15}
$$

> **Energy conservative Theorem for a Particle**:
> If the forces acting on a particle are conservative, then the total energy of the particle, $T+V$ is conserved.
> $$E=T+V=const\tag{1.1.16}$$

Note: The force applied to a particle may in some circumstances be given by the gradient function that depends explicitly on both the position of the particle and the time. However, the work done on the particle when it travels a distance is then no longer the total change in $-V$. Hence, the work done as the particle is no longer the difference in the function $V$. While the total energy may still be defined, it is not conserved during the course of the particle's motion. 

# 1.2 Mechanics of a System of Particles

Newton's second law:
$$
\sum\limits_j\underbrace{\mathbf{F}_{ji}}_{\text{internal force}}+\underbrace{\mathbf{F}_i^{(e)}}_{\text{external force}}=\dot{\mathbf{p}}
_i\tag{1.2.1}$$

> **Newton's third law**:
> The forces two particles exert on each other are equal and opposite.

(1.2.1) takes the form
$$
\frac{d^2}{dt^2}\sum\limits_im_i\mathbf{r}_i=\underbrace{\sum\limits_i\mathbf{F}_i^{(e)}}_{\text{external force }\mathbf{F}^{(e)}}+\underbrace{\sum\limits_{
i,j
\atop
i\neq j}\mathbf{F}_{ji}}_{\text{vanishes}}\tag{1.2.2}
$$

We define a vector $\mathbf{R}$: center of mass
$$
	\mathbf{R}=\frac{\sum\limits m_i\mathbf{r}_i}{\sum\limits m_i}=\frac{\sum\limits m_i\mathbf{r}_i}{M}\tag{1.2.3}
$$

(1.2.3) reduces to
$$
M\frac{d^2}{dt^2}\mathbf{R}=\sum\limits_i\mathbf{F}_i^{(e)}\equiv\mathbf{F}^{(e)}\tag{1.2.4}
$$
The center of mass moves as if the total external force were acting on the entire mass of the system concentrated at the center of mass.

total linear momentum of the system
$$
\mathbf{P}=\sum\limits m_{i}\frac{d\mathbf{r}_i}{dt}=\mathbf{M}\frac{d\mathbf{R}}{dt}\tag{1.2.5}
$$

> **Conservation Theorem for the Linear Momentum of a System of Particles**:
> If the total external force is zero, the total linear momentum is conserved.
> $$\mathbf{P}=const \tag{1.2.6}$$


Total angular momentum
$$
\begin{align} 
 \sum\limits_i(\mathbf{r}_i\times\dot{\mathbf{p}_i})&=\sum\limits_i\frac{d}{dt}(\mathbf{r}_i\times\mathbf{p}_i)=\dot{\mathbf{L}}\\
 &=\sum\limits_i\mathbf{r}_i\times\mathbf{F}_i^{(e)}+\sum\limits_{i,j\atop i\neq j}\mathbf{r}_i\times\mathbf{F}_{ji}
\end{align}\tag{1.2.7}
$$
The last term can be considered a sum of the pairs of the form
$$
\mathbf{r}_i\times\mathbf{F}_{ij}+\mathbf{r}_i\times\mathbf{F}_{ij}=(\mathbf{r}_{i}-\mathbf{r}_{j})\times\mathbf{F}_{ji}=\mathbf{r}_{ij}\times\mathbf{F}_{ji}\tag{1.2.8}
$$
If the internal forces between two particles in addition to be equal and opposite, also lie along the line joining the particles, $\mathbf{r}_{ij}\times\mathbf{F}_{ji}=0$
$$
\begin{align}
\mathbf{r}_i\times\mathbf{F}_{ij}+\mathbf{r}_i\times\mathbf{F}_{ij}&=\mathbf{r}_{ij}\times\mathbf{F}_{ji}=0\\
\Rightarrow \quad\quad\quad\sum\limits_{i,j\atop i\neq j}\mathbf{r}_i\times\mathbf{F}_{ji}&=0
\end{align}
\tag{1.2.9}
$$
(1.2.7) can be written in the form
$$
\frac{d\mathbf{L}}{dt}=\mathbf{N}^{(e)}
$$
> **Conservation Theorem for Total Angular Momentum**:
> $\mathbf{L}$ is constant in time if the applied (external) torque is zero.
> $$\mathbf{L}=const\tag{1.2.10}$$

Note:
it is a vector theorem; i.e., $L_z$ will be conserved if $N_z^{(2)}$ is zero, even if $N_x^(e)$, $N_y^{(e)}$ are not zero.

The total angular momentum of a system is
$$\mathbf{L}=\sum\limits_i\mathbf{r}_i\times\mathbf{p}_{i}\tag{1.2.11}$$
Let $\mathbf{R}$ be the radius from O to the center of mass and $\mathbf{r}_i'$ be the radius vector from center of mass to the ith particle (cf. Fig. 1.2.1)
![[物理/经典力学/附件-骆禹天的MacBook/Fig 1.2.1.excalidraw]]
<center>Fig 1.2.1</center>

Then we have
$$\left\{\quad\begin{align}
	\mathbf{r}_i&=\mathbf{r}_i'+\mathbf{R}\\
	\mathbf{v}_i&=\mathbf{v}_i'+\mathbf{v}\\
	\mathbf{v}&=\frac{d\mathbf{R}}{dt}\\
	\mathbf{v}_i&=\frac{d\mathbf{r}_i'}{dt}
\end{align}\right.\tag{1.2.12}$$

Total angular momentum
$$\begin{align}
\mathbf{L}&=\sum\limits_i\mathbf{r}_i\times\mathbf{p}_{i}\\
&=\sum\limits_i\mathbf{R}\times m_i\mathbf{v}\tag{1.2.13}+\sum\limits_{i}\mathbf{r}_i'\times m_i\mathbf{v}_i'\\
&+\underbrace{(\sum\limits_im_i\mathbf{r}_i')}_{\text{0}}\times \mathbf{v}+\mathbf{R}\times \frac{d}{dt}\underbrace{\sum\limits_im_{i}\mathbf{r}_i'}_{\text{0}}\\
&=\mathbf{R}\times M\mathbf{v}+\sum\limits_i\mathbf{r}_i'\times \mathbf{p}_i'
\end{align}
$$
The total angular momentum about a point O is
- the angular momentum of motion concentrated at the center of mass;
- angular momentum of motion about the center of mass.

The work down by all forces
$$W_{12}=\sum\limits_{i} \int_1^2\mathbf{F}_i\cdot d\mathbf{s}_i=\sum\limits_i\mathbf{F}_i^{(e)}\cdot d\mathbf{s}_i+\sum\limits_{i,j \atop i\neq j}\int_1^2\mathbf{F}_{ji}\cdot d\mathbf{s}_{i}\tag{1.2.14}$$
Left-hand side is
$$\sum\limits_{i}\int_1^2\mathbf{F}_i\cdot d\mathbf{s}_i=\sum\limits_i\int_1^2m_i\dot{\mathbf{v}}_i\cdot \mathbf{v}_idt=\sum\limits_i\int_1^2d\left(\frac{1}{2}m_iv_i^2\right)$$
$$W_{12}=T_2-T_{1}\tag{1.2.15}$$
Total kinetic energy
$$T=\frac{1}{2}\sum\limits_{i}m_iv_i^2=\frac{1}{2}Mv^2+\frac{1}{2}\sum\limits_im_iv_i'^2\tag{1.2.16}$$

Consider the right-hand side, in special case that the external forces are derivable in terms of the gradient of a potential,  the first term can be written as
$$\sum\limits_i\int_1^2\mathbf{F}i^{(e)}\cdot d\mathbf{s}_i=-\sum\limits_i\int_1^2\nabla _iV_i\cdot d\mathbf{s}_i=-\sum\limits_iV_i\bigg|_{1}^2\tag{1.2.17}$$

If the internal forces are also conservative, then the mutual forces between two particles $\mathbf{F}_{ij}$ can be obtained from a potential function $V_{ij}$.
To satisfy the strong law of action and reaction $V_{ij}$ can be a function only of the distance between the particles:
$$\mathbf{F}_{ij}=-\nabla _iV_{ij}=+\nabla _jV_{ji}=-\mathbf{F}_{ji}\tag{1.2.18}$$
$$V_{ij}=V_{ij}(|\mathbf{r}_i-\mathbf{r}_j|),\quad \nabla V_{ij}(|\mathbf{r}_i-\mathbf{r}_j|)=(\mathbf{r}_i-\mathbf{r}_{j})f\tag{1.2.19}$$
where f is some scalar function.

When the forces are all conservative, the second term in Eq (1.2.14) can be rewritten as a sum over pairs of particles.
$$\sum\limits_{i,j \atop i\neq j}\int_1^2\mathbf{F}_{ji}\cdot d\mathbf{s}_i=-\int_1^2(\nabla _iV_{ij}\cdot d\mathbf{s}_i+\nabla _jV_{ji}\cdot d\mathbf{s}_{j)}\tag{1.2.20}$$

If the difference vector $\mathbf{r}_i-\mathbf{r}_j$ is denoted by $\mathbf{r}_{ij}$, and if $\nabla _{ij}$ stands for the gradient with respect to $\mathbf{r}_{ij}$, then 
$$\nabla _iV_{ij}=\nabla _{ij}V_{ij}=-\nabla _jV_{ij} \tag{1.2.21}$$
and 
$$d\mathbf{s}_i-d\mathbf{s}_j=d\mathbf{r}_i-d\mathbf{r}_j=d\mathbf{r}_{ij} \tag{1.2.22}$$
so
	$$\sum\limits_{i,j \atop i\neq j}\int_1^2\mathbf{F}_{ji}\cdot d\mathbf{s}_i=-\int_1^2\nabla _{ij}V_{ij}\cdot d\mathbf{r}_{ij}\tag{1.2.23}$$
The total work arising from internal forces then reduces to
$$-1/2 \sum\limits_{i,j\atop i\neq j}\int_1^2\nabla _{ij}V_{ij}\cdot d\mathbf{r}_{ij}=-\frac{1}{2}\left.\sum\limits_{i,j\atop i\neq j}V_{ij}\right|_1^2\tag{1.2.24}$$
From these considerations, it is clear that if the external and internal forces are both derivable from potentials it is possible to define a **total potential energy V** of the system
$$V=\sum\limits_iV_i+\frac{1}{2}\sum\limits_{i,j\atop i\neq j}V_{ij}\tag{1.2.25}$$
such that the total energy $T+V$ is conserved. 

# 1.3 Constraints

If the conditions of constraint can be expressed as equations connecting the coordinates of the particles (and possibly the time) having the form
$$f(\mathbf{r}_1,\mathbf{r}_2,\mathbf{r}_3,\cdots ,t)=0\tag{1.3.1}$$
then the constraints are said to be **holonomic**.

A system of $N$ particles, free from constraints, has $3N$ independent coordinates or degrees of freedom. If there exist holonomic constraints, expressed in k equations, then we are left $3N-k$ independent coordinates. This elimination of the dependent coordinates can be expressed by equations of the form
$$
\begin{align}
\mathbf{r}&=\mathbf{r}_1(q_1,q_2,q_3,\cdots,q_{3N-k},t)\\
&\vdots\\
\mathbf{r}_N&=\mathbf{r}_N(q_1,q_2,q_3,\cdots ,q_{3N-k},t)
\end{align}\tag{1.3.2}
$$

# 1.4 D' Alembert's Principle and Lagrange's Equation

A **virtual** (infinitesimal) displacement of a system refers to a change in the configuration of the system as the result of any arbitrary infinitesimal change of the coordinate $\delta \mathbf{r}_i$, consistent with the forces and constraints imposed on the system at the given instant $t$. 

The displacement is called virtual to distinguish it from an actual displacement of the system occurring in a time interval dt, during which the forces and constraints may be changing.

Suppose the system is in equilibrium ($\mathbf{F}_i=0$):
$$\sum\limits_i\mathbf{F}_i\cdot \delta \mathbf{r}_i=0\tag{1.4.1}$$
As yet nothing has new physical content. Decompose $\mathbf{F}_i$ into the applied force $\mathbf{F}_i^{(a)}$ , and the force of constraint, $\mathbf{f}_i$ ,
$$\mathbf{F}_i=\mathbf{F}_i^{(a)}+\mathbf{f}_i\tag{1.4.2}$$

(1.3.1) becomes
$$\sum\limits_i\mathbf{F}_i^{(a)}\cdot \delta \mathbf{r}_i+\sum\limits_i\mathbf{f}_i\cdot \delta \mathbf{r}_{i}=0\tag{1.4.3}$$

We now restrict ourselves to systems for which **the net virtual work of the forces of constraints is zero** (this condition holds true for rigid bodies and it is valid for a large number of other conditions). 

We therefore have 

> **The principle of virtual work**: 
> The condition for equilibrium of a system that the virtual work of the applied forces vanishes:
> $$\sum\limits_i\mathbf{F}_i^{(a)}\cdot \delta \mathbf{r}_i=0\tag{1.4.4}$$

Note: 

The coefficients of $\delta r_i$ can be no longer be set equal to zero; i.e., in general $\mathbf{F}_i^{(a)}\neq 0$ , since the $\delta \mathbf{r}_i$ are not completely independent but are connected by the constraints. In order to equate the coefficients to zero, we must transform the principle into a form involving the virtual displacements of the $q_i$ , which are independent. Equation (1.3.4) satisfied our needs in that it does not contain the $\mathbf{f}_i$ , but it deals only with statics; we want a condition involving the general motion of the system. 

To obtain such a principle, we use a device first thought by James Bernoulli and developed by D' Alembert. The equation motion,
$$\mathbf{F}_i=\dot{\mathbf{p}}_{i}\quad\Rightarrow\quad\mathbf{F}_i-\dot{\mathbf{p}}_i=0\tag{1.4.5}$$
states that the particles in the system will be in equilibrium under a force equal to the actual force plus a "reversed effective force" $-\dot{\mathbf{p}}_i$ . Instead of (1.3.1), (1.3.3) we can immediately write
$$\sum\limits_i(\mathbf{F}_i-\dot{\mathbf{p}}_i)\cdot \delta \mathbf{r}_{i}=0 \tag{1.4.6}$$
and 
$$\sum\limits_i(\mathbf{F}_i^{(a)}-\dot{\mathbf{p}}_i)\cdot \delta \mathbf{r}_i+\underbrace{\sum\limits_i\mathbf{f}_i\cdot \delta \mathbf{r}_i}_{\text{vanishes}}=0\tag{1.4.7}$$

> **D' Alembert's Principle**: 
> $$\sum\limits_i(\mathbf{F}_i^{(a)}-\dot{\mathbf{p}}_i)\cdot \delta \mathbf{r}_i=0\tag{1.4.8}$$

We now transform the principle into an expression involving virtual displacements of the **generalized coordinates**, which are then independent of each other (for holonomic), so that the coefficients of the $\delta q_i$ can be set separately equal to zero.
$$\mathbf{r}_i=\mathbf{r}_i(q_1,q_2,q_3,\cdots,q_n,t)\tag{1.4.9}$$
Thus,
$$\mathbf{v}_i\equiv \frac{d\mathbf{r}_i}{dt}=\sum\limits_k\frac{\partial  \mathbf{r}_i}{\partial q_k}\dot{q}_{k} +\frac{\partial \mathbf{r}_i}{\partial t}\tag{1.4.10}$$
Similarly, the arbitrary virtual displacement $\delta \mathbf{r}_i$ can be connected with the virtual displacement $\delta q_i$
$$\delta \mathbf{r}_i=\sum\limits_j\frac{\partial \mathbf{r}_i}{\partial q_j}\delta q_{j}\tag{1.4.11}$$
virtual work of $\mathbf{F}_i$
$$\sum\limits_i\mathbf{F}_i\cdot \delta \mathbf{r}_i=\sum\limits_{i,j}\mathbf{F}_i\frac{\partial \mathbf{r}_i}{\partial q_j}\delta q_j=\sum\limits_{j}Q_{j}\delta q_{j}\tag{1.4.12}$$
> $Q_j$: Generalized force
> $$Q_j=\sum\limits_{i}\mathbf{F}_i\cdot \frac{\partial \mathbf{r}_i}{\partial q_{i}}\tag{1.4.13}$$

And in (1.3.8)
$$\sum\limits_{i}\dot{\mathbf{p}}_i\cdot \delta \mathbf{r}_{i}=\sum\limits_{i}m_i\ddot{\mathbf{r}}_{i}\cdot \delta \mathbf{r}_{i}=\sum\limits_{i,j}m_i\ddot{\mathbf{r}}_i\cdot \frac{\partial \mathbf{r}_i}{\partial q_{j}}\delta q_j\tag{1.4.14}$$

consider
$$\sum\limits_im_i\ddot{\mathbf{r}}_i\cdot \frac{\partial \mathbf{r}_i}{\partial q_j}=\sum\limits_i[\frac{d}{dt}(m_i\dot{\mathbf{r}}_i\cdot \frac{\partial \mathbf{r}_i}{\partial q_j})-m_i\dot{\mathbf{r}_i}\cdot \frac{d}{dt}(\frac{\partial \mathbf{r}_i}{\partial q_j})]\tag{1.4.15}$$
And,
$$\left\{\quad\begin{align}

& \frac{d}{dt}(\frac{\partial \mathbf{r}_i}{\partial q_j})=\frac{\partial \mathbf{v}_i}{\partial q_j}\\
	&\frac{\partial  \mathbf{v}_i}{\partial \dot{q}_j}=\frac{\partial \mathbf{r}_i}{\partial q_j}
\end{align}\right.\tag{1.4.16}
$$
(1.3.15) becomes
$$\sum\limits_im_i\ddot{\mathbf{r}}_i\cdot \frac{\partial \mathbf{r}_i}{\partial q_j}=\sum\limits[\frac{d}{dt}(m_i\mathbf{v}_i\cdot \frac{\partial \mathbf{v}_i}{\partial \dot{q}_{j}})-m_{i}\mathbf{v}_{i}\cdot \frac{\partial 
 \mathbf{v}_i}{\partial q_{j}}]\tag{1.4.17}$$

So, the principle (1.3.8) becomes
$$\begin{align}
\sum\limits_i(\mathbf{F}_i^{(a)}-\dot{\mathbf{p}}_i)\cdot \delta \mathbf{r}_i&=\sum\limits_j\left\{\frac{d}{dt}[\frac{\partial }{\partial \dot{q}_j}(\sum\limits_{i}\frac{1}{2}m_iv_{i}^{2} ) ]-\frac{\partial }{\partial q_j}(\sum\limits_{i}\frac{1}{2}m_{i}v_{i}^{2})-Q_{j}\right\}\\
&=\sum\limits\left\{[\frac{d}{dt}(\frac{\partial T}{\partial \dot{q}_{j}})-\frac{\partial T}{\partial q_{j}}]-Q_{j}\right\}\delta q_{j}=0
\end{align}
\tag{1.4.18}$$
So
$$\frac{d}{dt}(\frac{\partial T}{\partial \dot{q}_j})-\frac{\partial  T}{\partial q_{j}}=Q_{j}\tag{1.4.19}$$
There are n such equations at all.

When the forces are derivable from a scalar potential function V,
$$\mathbf{F}_{i}=-\nabla _{i}V \tag{1.4.20}$$
The generalized forces 
$$Q_{j}=\sum\limits_{i}\mathbf{F}_{i}\cdot \frac{\partial \mathbf{r}_i}{\partial q_{j}}=-\sum\limits_i\nabla _iV\cdot \frac{\partial \mathbf{r}_i}{\partial q_j}=-\frac{\partial V}{\partial q_{j}}\tag{1.4.21}$$
So (1.3.18) becomes
$$\frac{d}{dt}(\frac{\partial T}{\partial \dot{q}_j})-\frac{\partial  (T-V)}{\partial q_{j}}=0$$

Potential V does not depend on $\dot{q}_{j}$ , so $\dfrac{\partial V}{\partial \dot{q}_{j}}=0$ .
$$\frac{d}{dt}(\frac{\partial (T-V)}{\partial \dot{q}_j})-\frac{\partial  (T-V)}{\partial q_{j}}=0\tag{1.4.22}$$

We define a new function
> **Lagrangian L** 
> $$L=T-V \tag{1.4.23}$$

Finally we have
> **Lagrange's equation**
> $$\frac{d}{dt}(\frac{\partial L}{\partial \dot{q}_j})-\frac{\partial  L}{\partial q_{j}}=0\tag{1.4.24}$$

# 1.5 Velocity-dependent Potential and the Dissipation Function

Providing the general force are obtained from a function $U(q_{j},\dot{q}_{i})$ by the prescription
	$$Q_{j}=-\frac{\partial U}{\partial q_{j}}+\frac{d}{dt}(\frac{\partial U}{\partial \dot{q}_j})\tag{1.5.1}$$

So,
> **Lagrangian**
> $$ L=T-U \tag{1.5.2} $$
> which U is called **generalized potential**.

consider Lorentz force
$$\mathbf{F}=q[\mathbf{E}+(\mathbf{v}\times \mathbf{B})] \tag{1.5.3}$$
Both E and B are continuous functions of time and position derivable from a scalar potential $\phi (t,x,y,z)$ and a vector potential $\mathbf{A}(t,x,y,z)$.
$$\left\{\quad\begin{aligned}
\mathbf{E}&=-\nabla \phi -\frac{\partial \mathbf{A}}{\partial t}\\
\mathbf{B}&=\nabla \times \mathbf{A}
\end{aligned}\right.\tag{1.5.4}$$

Velocity-dependent potential energy
$$U=q\phi -q\mathbf{A}\cdot \mathbf{v}\tag{1.5.5}$$
So, Lagrangian
$$L=\frac{1}{2}mv^2-q\phi+q\mathbf{A}\cdot \mathbf{v}\tag{1.5.6}$$
X-component of Lagrange's equation:
$$\begin{align}
m\ddot{x}&=q(v_x\frac{\partial A_x}{\partial x}+v_y\frac{\partial A_y}{\partial x}+v_z\frac{\partial A_z}{\partial x})-q(\frac{\partial \phi }{\partial x}+\underbrace{\frac{dA_{x}}{dt}}_{\frac{\partial A_{x}}{\partial t}+\mathbf{v}\cdot \nabla A_{x}})\\
\\
&=q[\underbrace{-\frac{\partial \phi }{\partial x}-\frac{\partial A_x}{\partial t}}_{E_x}+\underbrace{v_y(\frac{\partial A_y}{\partial x}-\frac{\partial A_{x}}{\partial y})+v_z(\frac{\partial A_z}{\partial x}-\frac{\partial A_{x}}{\partial z})}_{(\mathbf{v}\times \mathbf{B})_x}]
\end{align}
$$
$$m\ddot{x}=q[E_x+(\mathbf{v}\times \mathbf{B})_{x}]\tag{1.5.7}$$
(1.5.7) and (1.5.3) are identical, showing that the Lorentz force equation is derivable from Eqs. (1.5.4) and (1.5.5). 

> **Note**: If not all the forces acting on the system are derivable from a potential, then Lagrange's equations can be always written in the form
> $$\frac{d}{dt}(\frac{\partial L}{\partial \dot{q}_{j}})-\frac{\partial L}{\partial q_{j}}=Q_{j}\tag{1.5.8}$$
- $Q_j$ represent the forces not arising from a potential;
- Such a situation often occurs when frictional forces are present.

Frictional force is proportional to the velocity of the particle.
$$F_{fx}=-k_xv_x$$
Frictional force can be derived in terms of a function $F$
> **Rayleigh's Dissipation Function**:
> $$\mathcal{F}=\frac{1}{2}\sum\limits_i(k_xv_{ix}^{2}+k_yv_{iy}^{2}+k_zv_{iz}^{2})\tag{1.5.9}$$

Frictional force
$$F_{fx}=-\frac{\partial  \mathcal{F}}{\partial v_{x}}\quad or\quad \mathbf{F}_f=-\nabla _v\mathcal{F}\tag{1.5.10}$$
The work done by system against friction
$$dW_f=-\mathbf{F}_f\cdot d\mathbf{r}=-\mathbf{F}_f\cdot \mathbf{v}dt=(k_xv_x^2+k_yv_y^2+k_zv_z^2)dt\tag{1.5.11}$$
hence, $2\mathcal{F}$ is the rate of energy dissipation due to friction. The generalized force resulting from force of friction is
$$
\begin{align}
Q_j&=\sum\limits_{i}\mathbf{F}_{fi}\cdot \frac{\partial \mathbf{r}_i}{\partial q_i}=-\sum\limits\nabla _v\mathcal{F}\cdot \frac{\partial \mathbf{r}_{i}}{\partial q_j}\\
&=-\sum\limits\nabla _v\mathcal{F\cdot \frac{\partial \dot{\mathbf{r}}_{i}}{\partial \dot{q}_j}}\\
&=-\frac{\partial \mathcal{F}}{\partial \dot{q}_{j}}
\end{align}\tag{1.5.12}
$$

