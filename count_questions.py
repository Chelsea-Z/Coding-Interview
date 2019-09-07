import os
import sys
import collections




"""
usage: python count_questions.py <folder_name>
sample: python count_question.py ./LintCode
"""
def count_number_of_questions(dir):

    q = collections.deque()
    q.append(dir)

    completed = set()
    catagories = {}

    while q:
        curr_dir = q.popleft()
        catagories[curr_dir] = []
        for item in os.listdir(curr_dir):
            if os.path.isdir(os.path.join(curr_dir, item)):
                q.append(os.path.join(curr_dir, item))
                continue

            filename_parts = item.split('_')
            if len(filename_parts) <= 1 or not filename_parts[0].isdigit():
                continue
            completed.add(int(filename_parts[0]))
            catagories[curr_dir].append(int(filename_parts[0]))

    print("Number of questions completed: ", len(completed))
    print(sorted(completed))

    sorted_cate = sorted([(k.split('/')[-1], len(v)) for k, v in catagories.items()],
                            key=lambda x: x[1], reverse=True)
    for cate, value in sorted_cate:
        print(cate + ": ", value)


if __name__ == '__main__':
    count_number_of_questions(sys.argv[1])
