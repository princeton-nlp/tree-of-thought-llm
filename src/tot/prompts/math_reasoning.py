standard_prompt = '''Solve the following math problem.

<Example>
Question: Let \[f(x) = \left\{\n\begin{array}{cl} ax+3, &\text{ if }x>2, \\\nx-5 &\text{ if } -2 \le x \le 2, \\\n2x-b &\text{ if } x <-2.\n\end{array}\n\right.\]Find $a+b$ if the piecewise function is continuous (which means that its graph can be drawn without lifting your pencil from the paper).
Answer: 0.
</Example>

<Task>
Question: {question}
Answer: 
</Task>
'''

cot_prompt = r'''Solve the following math problem. Perform the solution by going step by step, and write down each step.

<Example>
Question: Let \[f(x) = \left\{\n\begin{array}{cl} ax+3, &\text{ if }x>2, \\\nx-5 &\text{ if } -2 \le x \le 2, \\\n2x-b &\text{ if } x <-2.\n\end{array}\n\right.\]Find $a+b$ if the piecewise function is continuous (which means that its graph can be drawn without lifting your pencil from the paper). Let's think step by step.
Solution: For the piecewise function to be continuous, the cases must "meet" at $2$ and $-2$. For example, $ax+3$ and $x-5$ must be equal when $x=2$. This implies $a(2)+3=2-5$, which we solve to get $2a=-6 \Rightarrow a=-3$. Similarly, $x-5$ and $2x-b$ must be equal when $x=-2$. Substituting, we get $-2-5=2(-2)-b$, which implies $b=3$. So $a+b=-3+3=\boxed{0}$.
</Example>

<Example>
Question: Sixteen is 64$\%$ of what number? Let's think step by step.
Solution: If the number is $x$, we can set up the equation $\frac{16}{x}=\frac{64}{100}$. We divide both sides by $4$ to get $\frac{1}{x}=\frac{4}{100}=\frac{1}{25}$, so $x=\boxed{25}$.
</Example>

<Example>
Question: There are 3 complex numbers $a+bi$, $c+di$, and $e+fi$. If $b=1$, $e=-a-c$, and the sum of the numbers is $-i$, find $d+f$. Let's think step by step.
Solution: We know that $a+bi+c+di+e+fi=-i$. Thus, the real parts add up to 0 and the imaginary parts add up to -1. We then have  \begin{align}\na+c+e&=0\\\nb+d+f&=-1\\\n\end{align}We know that $b=1$, therefore $d+f=\boxed{-2}$
</Example>

<Task>
Question: {question} Let's think step by step.
Solution: 
</Task>
'''

propose_first_step_prompt = '''Write the first step to solve the following math problem. Only write down the first step. Do not write down the answer. Do not write down the question. Do not continue the solution. Do not write down the second step.
<Example>
Question: Let \[f(x) = \left\{\n\begin{array}{cl} ax+3, &\text{ if }x>2, \\\nx-5 &\text{ if } -2 \le x \le 2, \\\n2x-b &\text{ if } x <-2.\n\end{array}\n\right.\]Find $a+b$ if the piecewise function is continuous (which means that its graph can be drawn without lifting your pencil from the paper).
First step: For the piecewise function to be continuous, the cases must "meet" at $2$ and $-2$.
</Example>

<Example>
Question: Sixteen is 64$\%$ of what number? 
First step: If the number is $x$, we can set up the equation $\frac{16}{x}=\frac{64}{100}$.
</Example>

<Example>
Question: There are 3 complex numbers $a+bi$, $c+di$, and $e+fi$. If $b=1$, $e=-a-c$, and the sum of the numbers is $-i$, find $d+f$.
First step:We know that $a+bi+c+di+e+fi=-i$. Thus, the real parts add up to 0 and the imaginary parts add up to -1.
</Example>

<Task>
Question: {question}
First step: 
</Task>
'''

propose_next_step_prompt = '''Write the next step to solve the following math problem. If the solution is reached, write "Problem solved" at the end. If final answer is not yet reached, write down the next step. 
<Example>
Question: Let \[f(x) = \left\{\n\begin{array}{cl} ax+3, &\text{ if }x>2, \\\nx-5 &\text{ if } -2 \le x \le 2, \\\n2x-b &\text{ if } x <-2.\n\end{array}\n\right.\]Find $a+b$ if the piecewise function is continuous (which means that its graph can be drawn without lifting your pencil from the paper).
Steps until now: For the piecewise function to be continuous, the cases must "meet" at $2$ and $-2$.
Next step: For example, $ax+3$ and $x-5$ must be equal when $x=2$. This implies $a(2)+3=2-5$, which we solve to get $2a=-6 \Rightarrow a=-3$.
</Example>

<Example>
Question: Sixteen is 64$\%$ of what number? 
Steps until now: If the number is $x$, we can set up the equation $\frac{16}{x}=\frac{64}{100}$.
Next step: We divide both sides by $4$ to get $\frac{1}{x}=\frac{4}{100}=\frac{1}{25}$, so $x=\boxed{25}$. Problem solved.
</Example>

<Example>
Question: There are 3 complex numbers $a+bi$, $c+di$, and $e+fi$. If $b=1$, $e=-a-c$, and the sum of the numbers is $-i$, find $d+f$.
Steps until now: We know that $a+bi+c+di+e+fi=-i$. Thus, the real parts add up to 0 and the imaginary parts add up to -1.
Next step: We then have  \begin{align}\na+c+e&=0\\\nb+d+f&=-1\\\n\end{align}We know that $b=1$, therefore $d+f=\boxed{-2}$. Problem solved.
</Example>

<Task>
Question: {question}
Steps until now: {steps}
Next step: 
</Task>
'''

propose_final_step_prompt = ''' Extract the final answer given the question and solution steps.
<Example>
Question: Let \[f(x) = \left\{\n\begin{array}{cl} ax+3, &\text{ if }x>2, \\\nx-5 &\text{ if } -2 \le x \le 2, \\\n2x-b &\text{ if } x <-2.\n\end{array}\n\right.\]Find $a+b$ if the piecewise function is continuous (which means that its graph can be drawn without lifting your pencil from the paper). Let's think step by step.
Solution: For the piecewise function to be continuous, the cases must "meet" at $2$ and $-2$. For example, $ax+3$ and $x-5$ must be equal when $x=2$. This implies $a(2)+3=2-5$, which we solve to get $2a=-6 \Rightarrow a=-3$. Similarly, $x-5$ and $2x-b$ must be equal when $x=-2$. Substituting, we get $-2-5=2(-2)-b$, which implies $b=3$. So $a+b=-3+3=\boxed{0}$.
Final answer: 0
</Example>

<Example>
Question: Sixteen is 64$\%$ of what number? Let's think step by step.
Solution: If the number is $x$, we can set up the equation $\frac{16}{x}=\frac{64}{100}$. We divide both sides by $4$ to get $\frac{1}{x}=\frac{4}{100}=\frac{1}{25}$, so $x=\boxed{25}$.
Final answer: 25
</Example>

<Example>
Question: There are 3 complex numbers $a+bi$, $c+di$, and $e+fi$. If $b=1$, $e=-a-c$, and the sum of the numbers is $-i$, find $d+f$. Let's think step by step.
Solution: We know that $a+bi+c+di+e+fi=-i$. Thus, the real parts add up to 0 and the imaginary parts add up to -1. We then have  \begin{align}\na+c+e&=0\\\nb+d+f&=-1\\\n\end{align}We know that $b=1$, therefore $d+f=\boxed{-2}$
Final answer: -2
</Example>

<Task>
Question: {question}
Solution: {solution}
Final answer: 
</Task>
'''

value_prompt = ''' Evaluate if given steps are likely to solve the question. (likely, unlikely, or unsure)
<Example>
Question: Let \[f(x) = \left\{\n\begin{array}{cl} ax+3, &\text{ if }x>2, \\\nx-5 &\text{ if } -2 \le x \le 2, \\\n2x-b &\text{ if } x <-2.\n\end{array}\n\right.\]Find $a+b$ if the piecewise function is continuous (which means that its graph can be drawn without lifting your pencil from the paper).
Steps: For the piecewise function to be continuous, the cases must "meet" at $2$ and $-2$.
Reasoning: criteria to make piecewise function is correct.
Evaluation: likely
</Example>

<Example>
Question: Sixteen is 64$\%$ of what number? 
Steps: If the number is $x$, we can set up the equation $\frac{16}{x}=\frac{64}{100}$.
Reasoning: equation is correct
Evaluation: likely
</Example>

<Example>
Question: There are 3 complex numbers $a+bi$, $c+di$, and $e+fi$. If $b=1$, $e=-a-c$, and the sum of the numbers is $-i$, find $d+f$.
Steps:We know that $a+bi+c+di+e+fi=-i$. Thus, the real parts add up to 1 and the imaginary parts add up to 0.
Reasoning: equation is incorrect
Evaluation: unlikely
</Example>

<Task>
Question: {question}
Steps: {steps}
Reasoning: 
Evaluation: 
</Task>
'''

