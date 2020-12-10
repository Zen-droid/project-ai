import json

def commit(data):
    json_object = json.dumps(data, indent=4)

    with open("employee_data.json", "w") as outfile:
        outfile.write(json_object)


def get_data():
    with open("employee_data.json", "r") as openfile:
        data = json.load(openfile)
        return data


def add_data():
    n = int(input("Number of data: "))

    for x in range(n):
        temp = {}
        print(f"\nEmployee {index+x+1}")

        name = str(input("Enter name: "))
        position = str(input('Enter position: '))
        division = str(input("Enter division: "))

        temp["id"] = index+x+1
        temp["name"] = name
        temp["position"] = position
        temp["division"] = division

        original_data.append(temp)

    commit(original_data)


def view_data():
    print("-- Employee List --")
    print("| Employee ID | Employee Name        | Employee Position | Employee Division |")
    print("+=============+======================+===================+===================+")
    for data in original_data:
        print("| %-11d | %-20s | %-17s | %-17s |" 
                %(data["id"], data["name"], data["position"], data["division"]))


def delete_data():
    view_data()

    choice = -1
    while choice < 0 or choice > index:
        choice = int(input("Choose employee ID to delete: "))

    for i in range(index):
        if original_data[i]["id"] == choice:
            del original_data[i]
            break

    commit(original_data)

original_data = get_data()
index = len(original_data)

if __name__ == "__main__":
    choice = -1
    
    while choice != 4:
        print("(1) Add Data")
        print("(2) View Data")
        print("(3) Delete Data")
        print("(4) Exit")

        choice = int(input("Choose >> "))

        if choice == 1:
            add_data()
        elif choice == 2:
            view_data()
        elif choice == 3:
            delete_data()
        else:
            pass

        print("Press enter to continue...")
        input()