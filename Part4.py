
progress_count = 0
trailer_count = 0
retriever_count = 0
excluded_count = 0
out_come = ""


def is_in_range(credit):
    if credit not in range(0,121,20):
        print("Out of range")
        return False
    else:
        return True


# function to print inputs from file
def print_input_list_from_file():
    file = open('file.txt', 'r')
    inputs = file.read().splitlines()
    for i in inputs:
        print(i)


def print_vertical_histogram(p_count, t_count, r_count, e_count ):
    print("Progress Trailing Retriever Excluded")
    lines = max(p_count,t_count,r_count,e_count)
    for i in range(lines):
        print("   *   " if p_count>0 else "       ",
              "    *   " if t_count>0 else "        ",
              "     *   " if r_count>0 else "         ",
              "     *   " if e_count>0 else "         ",)
        p_count -= 1
        t_count -= 1
        r_count -= 1
        e_count -= 1


print("Staff version with Histogram")
file = open('file.txt', 'w').close()
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
        if(pass_credits + defer_credits + fail_credits) == 120:
            if pass_credits == 120:
                out_come = "Progress"
                progress_count += 1

            elif pass_credits == 100 and (0 <= defer_credits <= 20 and 0 <= fail_credits <= 20):
                out_come = "Progress (module trailer)"
                trailer_count += 1

            elif 80 <= fail_credits <= 120:
                out_come = "Exclude"
                excluded_count += 1
                
            else:
                out_come = "Module retriever"
                retriever_count += 1

            # print correct output after conditional check
            print(out_come)

            # append a new line to file
            file = open('file.txt', 'a')
            line = out_come + " - " + str(pass_credits) + ", " + str(defer_credits) + ", " + str(fail_credits) + "\n"
            file.write(line)
            file.close()

            print("\nWould you like to enter another set of data?")
            is_continue = input("Enter 'y' for yes or 'q' to quit and view results:")

            if is_continue == 'y':
                continue
            elif is_continue == 'q':
                print_vertical_histogram(progress_count, trailer_count, retriever_count, excluded_count)
                # print user inputs from file
                print_input_list_from_file()
                break
            else:
                print("Invalid input!")
                break
            
        else:
            print("Total incorrect")
            continue

    except ValueError:
        print("Integer required")



