target_problem_name = input()

num_submissions = int(input())

max_score_for_target = 0

for _ in range(num_submissions):
    line_parts = input().split()

    problem_name = line_parts[1]
    
    score = int(line_parts[2])
    
    if problem_name == target_problem_name:
        if score > max_score_for_target:
            max_score_for_target = score

print(max_score_for_target)