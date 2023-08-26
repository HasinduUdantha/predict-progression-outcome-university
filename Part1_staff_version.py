# initiate separate variables for keep the output counts
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0


# function for check credit range
def is_in_range(credit):
    if credit not in range(0, 121, 20):
        print("Out of range")
        return False
    else:
        return True


# access output counts and prepare histogram
def print_horizontal_histogram():
    total = progress_count + trailer_count + retriever_count + excluded_count
    print("Horizontal Histogram")
    print("Progress", progress_count, "  :", "*" * progress_count)
    print("Trailer", trailer_count, "   :", "*" * trailer_count)
    print("Retriever", retriever_count, " :", "*" * retriever_count)
    print("Exclude", excluded_count, "   :", "*" * excluded_count)
    print(total, " outcomes in total")


print("Staff version with Histogram")

while True:
    try:
        pass_credits = int(input("Please enter your credits at pass: "))
        if not is_in_range(pass_credits):
            continue

        defer_credits = int(input("Please enter your credits at defer: "))
        if not is_in_range(defer_credits):
            continue

        fail_credits = int(input("Please enter your credits at fail: "))
        if not is_in_range(fail_credits):
            continue

        # check total validity
        if (pass_credits + defer_credits + fail_credits) == 120:
            if pass_credits == 120:
                print("Progress")
                progress_count += 1  # increase progress outcomes count by one

            elif pass_credits == 100 and (0 <= defer_credits <= 20 and 0 <= fail_credits <= 20):
                print("Progress (module trailer)")
                trailer_count += 1  # increase trailer outcomes count by one

            elif 80 <= fail_credits <= 120:
                print("Exclude")
                excluded_count += 1  # increase excluded outcomes count by one

            else:
                print("Module retriever")
                retriever_count += 1  # increase retriever outcomes count by one

            # ask for continue the inputs
            print("\nWould you like to enter another set of data?")
            is_continue = input("Enter 'y' for yes or 'q' to quit and view results:")

            if is_continue == "y":
                continue  # continue asking for inputs

            elif is_continue == "q":
                print_horizontal_histogram()
                break  # break multiple input taking
            else:
                print("Invalid input!")
                continue

        else:
            print("Total incorrect")
            continue

    except ValueError:
        print("Integer required")
