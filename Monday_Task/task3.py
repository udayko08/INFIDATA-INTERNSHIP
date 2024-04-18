def main():
    print("Welcome to the Quiz!\n")
    score = 0
    total_questions = 3

    # Question 1
    print("Question 1: In which year was Mysore renamed Karnataka??")
    print("a) 1971 ")
    print("b) 1973")
    print("c) 1968")
    answer1 = input("Your answer: ").lower()
    if answer1 == "b":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Question 2
    print("\nQuestion 2: which town as the silk town of karnataka?")
    print("a) ramanagara")
    print("b) haveri")
    print("c) davanagere")
    answer2 = input("Your answer: ").lower()
    if answer2 == "a":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Question 3
    print("\nQuestion 3: Who wrote 'Romeo and Juliet'?")
    print("a) William Shakespeare")
    print("b) Charles Dickens")
    print("c) Jane Austen")
    answer3 = input("Your answer: ").lower()
    if answer3 == "a":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    # Calculate score
    wrong_answers = total_questions - score
    print("\nQuiz completed!")
    print("Your score: {}/{}".format(score, total_questions))
    print("You got {} wrong answer(s).".format(wrong_answers))

if __name__ == "__main__":
    main()
