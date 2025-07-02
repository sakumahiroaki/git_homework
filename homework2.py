import random

def number_guessing_game():
    answer = random.randint(1, 100)  # 正解は1〜100のランダム
    max_attempts = 5

    print("数字当てゲームを始めます！ 1から100の数字を当ててください。")
    print(f"チャンスは {max_attempts} 回です。")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"{attempt} 回目の予想: "))
        except ValueError:
            print("数字を入力してください。")
            continue
        
        if guess == answer:
            print(f"正解です！{attempt} 回目で当たりました！")
            break
        else:
            if guess < answer:
                hint = "もっと大きい数字です。"
            else:
                hint = "もっと小さい数字です。"
            print(f"不正解です。ヒント: {hint}")
    else:
        print(f"残念！正解は {answer} でした。")

if __name__ == "__main__":
    number_guessing_game()
