# Please enter the letters like this: rgyb
# Please enter the given questions like this: 1234
# Please enter the question to be solved like this: 1234,2341,3412
# Please enter the answer at the end and the the program will end automatically: ygrb

# Setting variable for initial ones
start_colour = list(input("Enter: "))
end_colour = []

questions = []
test_case = []
question_req = []

# Getting the inputs of the users
letter_counter = 1
input_counter = 0

while letter_counter > 0:
    user_input = input("Enter: ")
    if user_input[0].isalpha() and letter_counter == 1:
        end_colour = list(user_input)
        letter_counter -= 1
    else:
        if ',' in user_input:
            temp = user_input.split(',')
            questions.append([list(map(int,i)) for i in temp])
            question_req.append(input_counter)
        else:
            questions.append([[int(j) for j in list(user_input)]])
        input_counter += 1

    
# Testing a matrix for a set of matrix
def test_answer(start_colour,test_questions):
    for i, start_letter in enumerate(start_colour):
        temp = i + 1
        for j in test_questions:
            temp = j.index(temp) + 1
        if start_letter != end_colour[temp-1]:
            return False
    return True

# Iterator in Switch
iter_length = len(question_req)
process_queue = []
found_answer = False

while question_req:
    current_iter = [0 for _ in range(len(questions))]
    if question_req:
        process_queue.append(question_req.pop(0))
    else:
        process_queue.pop(0)
    for _ in range(3):
        testing_answer = [questions[i][v] for i,v in enumerate(current_iter)]
        if test_answer(start_colour,testing_answer):
            print("Answer:" + str(testing_answer))
            found_answer = True
        for layer in process_queue:
            current_iter[layer] += 1

if not found_answer:
    print("Cannot find answer")


