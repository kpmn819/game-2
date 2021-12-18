# lets have some fun with dictionaries
import json
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
# convert into a json list to store
j_list = json.dumps(qa_list)
print(j_list[0])
with open('q-and-a.json', 'w') as outfile: #save the json file
        json.dump(qa_list, outfile)
        print("json Data encoded and saved to file")