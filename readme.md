# Tree of Thoughts (ToT)

Code for paper [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601). 
Also check [its tweet thread](https://twitter.com/ShunyuYao12/status/1659357547474681857) in 1min.


## Setup
You need to first have an OpenAI API key and store it in the environment variable ``OPENAI_API_KEY`` (see [here](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)).

Package requirement: ``openai``, ``backoff``, ``sympy``, ``numpy``. 


## Experiments

Run experiments via ``sh scripts/{game24, text, crosswords}/{standard_sampling, cot_sampling, bfs}.sh``, except in crosswords we use a DFS algorithm for ToT, which can be run via ``scripts/crosswords/search_crosswords-dfs.ipynb``.

The very simple ``run.py`` implements the ToT + BFS algorithm, as well as the naive IO/CoT sampling. Some key arguments:

- ``--naive_run``: if True, run naive IO/CoT sampling instead of ToT + BFS.
-  ``--prompt_sample`` (choices=[``standard``, ``cot``]): sampling prompt
- ``--method_generate`` (choices=[``sample``, ``propose``]): thought generator, whether to sample independent thoughts (used in Creative Writing) or propose sequential thoughts (used in Game of 24)
- ``--method_evaluate`` (choices=[``value``, ``vote``]): state evaluator, whether to use the value states independently (used in Game of 24) or vote on states together (used in Creative Writing)
- ``--n_generate_sample``: number of times to prompt for thought generation
- ``--n_evaluate_sample``: number of times to prompt for state evaluation
- ``--n_select_sample``: number of states to keep from each step (i.e. ``b`` in the paper's ToT + BFS algorithm)



## Trajectories
``logs/`` contains trajectories from paper experiments, except ``logs/game24/gpt-4_0.7_propose1_value3_greedy5_start900_end1000.json`` is reproduced after the paper (as the original experiment was in a notebook) and achieved 69\% instead of original 74\% due to the randomness in GPT decoding. We hope to aggregate multiple runs in the future to account for sampling randomness and update the paper, but it shouldn't affect the main conclusions of the paper.



## Questions
Feel free to contact shunyuyao.cs@gmail.com or open an issue if you have any questions.


## Citation

```bibtex
@misc{yao2023tree,
      title={{Tree of Thoughts}: Deliberate Problem Solving with Large Language Models}, 
      author={Shunyu Yao and Dian Yu and Jeffrey Zhao and Izhak Shafran and Thomas L. Griffiths and Yuan Cao and Karthik Narasimhan},
      year={2023},
      eprint={2305.10601},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```