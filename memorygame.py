import time
import os
import random

# ---------------- LEVELS ---------------- #

levels = {
    1: [
        "cat dog sun tree fish bird sky cloud grass",
        "apple banana mango orange grapes watermelon papaya",
        "red blue green yellow white black purple pink",
        "lion tiger elephant monkey zebra giraffe deer",
        "table chair window door computer keyboard mouse"
    ],

    2: [
        "python coding memory keyboard typing game challenge practice",
        "students learn programming through practice and projects daily",
        "computer science improves problem solving abilities significantly",
        "debugging programs requires patience concentration and logic",
        "software development involves testing coding and maintenance"
    ],

    3: [
        "Artificial intelligence improves human productivity and learning every day",
        "Technology helps people communicate and collaborate efficiently worldwide",
        "Machine learning algorithms can identify complex patterns in data",
        "Data science combines statistics programming and business knowledge",
        "Modern computers process information at extremely high speeds"
    ],

    4: [
        "Success usually comes to those who are too busy to be looking for it",
        "Hard work and consistency are important factors for achieving goals",
        "Discipline often matters more than motivation in the long run",
        "Small daily improvements eventually lead to remarkable results",
        "Confidence grows when preparation and opportunity meet together"
    ],

    5: [
        "The quick brown fox jumps over the lazy dog while programmers debug complex algorithms",
        "Software engineers continuously improve applications through testing and maintenance",
        "Creative thinking combined with technical knowledge produces innovative solutions",
        "Cybersecurity professionals protect systems from threats and vulnerabilities",
        "Successful projects require teamwork communication planning and execution"
    ]
}

# ---------------- TIME LIMITS ---------------- #

level_time_limits = {
    1: 60,
    2: 120,
    3: 180,
    4: 240,
    5: 300
}

# ---------------- FUNCTIONS ---------------- #

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def calculate_accuracy(original, typed):
    original_words = original.split()
    typed_words = typed.split()

    correct = 0

    for i in range(min(len(original_words), len(typed_words))):
        if original_words[i].lower() == typed_words[i].lower():
            correct += 1

    accuracy = (correct / len(original_words)) * 100

    return round(accuracy, 2)


def calculate_wpm(text, time_taken):
    words = len(text.split())

    if time_taken == 0:
        return 0

    return round(words / (time_taken / 60), 2)


# ---------------- GAME START ---------------- #

total_score = 0
current_level = 1

print("=" * 50)
print("              MEMORY TYPING GAME")
print("=" * 50)

input("\nPress ENTER to start...")

# ---------------- MAIN LOOP ---------------- #

while current_level <= 5:

    while True:

        level_scores = []

        selected_sentences = random.sample(
            levels[current_level],
            3
        )

        # ---------- ROUNDS ---------- #

        for round_number in range(1, 4):

            sentence = selected_sentences[round_number - 1]

            clear_screen()

            print("=" * 50)
            print(f"LEVEL {current_level} | ROUND {round_number}/3")
            print("=" * 50)

            print("\nMEMORIZE THIS SENTENCE:\n")
            print(sentence)

            display_time = max(
                5,
                len(sentence.split())
            )

            print(
                f"\nSentence disappears in "
                f"{display_time} seconds"
            )

            for sec in range(display_time, 0, -1):
                print(
                    f"\rCountdown: {sec} ",
                    end=""
                )
                time.sleep(1)

            clear_screen()

            print("=" * 50)
            print(f"LEVEL {current_level} | ROUND {round_number}/3")
            print("=" * 50)

            typing_limit = level_time_limits[current_level]

            print(
                f"\nTyping Time Limit: "
                f"{typing_limit} seconds"
            )

            start_time = time.time()

            typed_text = input(
                "\nType the sentence:\n"
            )

            end_time = time.time()

            time_taken = end_time - start_time

            # ---------- TIME CHECK ---------- #

            if time_taken > typing_limit:

                print("\nTIME LIMIT EXCEEDED!")

                accuracy = 0
                wpm = 0
                score = 0

            else:

                accuracy = calculate_accuracy(
                    sentence,
                    typed_text
                )

                wpm = calculate_wpm(
                    typed_text,
                    time_taken
                )

                score = round(
                    (accuracy + min(wpm, 100)) / 2
                )

            level_scores.append(score)

            print("\n" + "=" * 50)
            print("ROUND RESULT")
            print("=" * 50)

            print(
                f"Original Text : {sentence}"
            )

            print(
                f"Your Text     : {typed_text}"
            )

            print(
                f"Time Taken    : "
                f"{round(time_taken, 2)} sec"
            )

            print(
                f"Accuracy      : {accuracy}%"
            )

            print(
                f"WPM           : {wpm}"
            )

            print(
                f"Round Score   : {score}"
            )

            input(
                "\nPress ENTER for next round..."
            )

        # ---------- LEVEL SUMMARY ---------- #

        clear_screen()

        average_score = round(
            sum(level_scores) / len(level_scores),
            2
        )

        print("=" * 50)
        print(
            f"LEVEL {current_level} SUMMARY"
        )
        print("=" * 50)

        print(
            f"\nRound 1 Score : {level_scores[0]}"
        )

        print(
            f"Round 2 Score : {level_scores[1]}"
        )

        print(
            f"Round 3 Score : {level_scores[2]}"
        )

        print(
            f"\nAverage Score : {average_score}"
        )

        level_passed = average_score >= 50

        if level_passed:
            print("\nSTATUS : PASSED")
        else:
            print("\nSTATUS : FAILED")

        # ---------- MENU ---------- #

        print("\nOPTIONS")
        print("1. Retake Level")

        if level_passed:
            print("2. Move To Next Level")

        print("3. Restart Full Game")
        print("4. Exit Game")

        choice = input(
            "\nEnter choice: "
        )

        if choice == "1":

            print("\nRestarting level...")
            time.sleep(1)

            continue

        elif choice == "2" and level_passed:

            total_score += average_score
            current_level += 1

            break

        elif choice == "3":

            current_level = 1
            total_score = 0

            print("\nRestarting game...")
            time.sleep(1)

            break

        elif choice == "4":

            print("\nThanks for playing!")
            exit()

        else:

            print("\nInvalid choice!")
            time.sleep(1)


# ---------------- GAME COMPLETE ---------------- #

clear_screen()

print("=" * 50)
print("CONGRATULATIONS!")
print("=" * 50)

print("\nYou completed all levels.")

print(
    f"\nTotal Score : "
    f"{round(total_score, 2)}"
)

if total_score >= 450:

    print("\nLEGENDARY MEMORY MASTER")

elif total_score >= 350:

    print("\nMASTER MEMORY PLAYER")

elif total_score >= 250:

    print("\nGREAT PERFORMANCE")

else:

    print("\nGOOD TRY")

print("\nThank you for playing!")