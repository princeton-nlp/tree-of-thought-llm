python run.py \
    --task text \
    --task_file_path data_100_random_text.txt \
    --task_start_index 0 \
    --task_end_index 1 \
    --method_generate sample \
    --method_evaluate vote \
    --method_select greedy \
    --n_generate_sample 5 \
    --n_evaluate_sample 5 \
    --n_select_sample 1 \
    --prompt_sample cot \
    --temperature 1.0 \
    ${@}


# 0.3 dollars per line ->  30 dollars for 100 lines