# lets have some fun with dictionaries
qa_dict = {
    "First Question": "First Answer",
    "Second Question": "Second Answer",
    "Third Question": "Third Answer"
}
print(qa_dict["First Question"])

# may actually have to do it as a list
# of tuples
qa_list = [
    ("first qestion", "first answer"),
    ("second question", "second answer"),
    ("third question", "third answer")]
q2 = (qa_list[0])
print(q2[0])
print(q2[1])