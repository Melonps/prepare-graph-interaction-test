import argparse
import random


def add_random_list(current_list: list):
    current_list = current_list + current_list
    random.shuffle(current_list)
    return current_list


def get_question_id_list():
    group_num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, "yomiage"]
    result_group_list = add_random_list(group_num_list)
    print(result_group_list)
    print(len(result_group_list))
    question_id_list = []
    for group_num in result_group_list:

        if group_num == "yomiage":
            val = 9 * 100 - 1
            next_val = 10 * 100 - 1
        else:
            val = (group_num - 2) * 100 - 1
            next_val = (group_num - 1) * 100 - 1
        index = random.randint(val, next_val)
        question_id_list.append(index)
    print("label: ", question_id_list)
    return question_id_list


if __name__ == "__main__":
    random.seed(42)
    parser = argparse.ArgumentParser(description="質問データを処理します。")
    args = parser.parse_args()
    get_question_id_list()
