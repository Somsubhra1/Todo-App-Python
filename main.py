import db_helper


def main():
    run = 1
    db_helper.create_table()

    while run:
        print()
        print("1: Insert new task\n2:View Todo List\n3:Delete Todo\n0:Exit")
        x = int(input("Enter choice: "))
        if x == 1:
            task = input("Enter task: ")
            db_helper.data_entry(task)

        elif x == 2:
            db_helper.printData()

        elif x == 3:
            index = int(input("Enter Todo Index to delete: "))
            db_helper.deleteTask(index)

        elif x == 0:
            run = 0

        else:
            print("Wrong choice...")

    db_helper.closeCursor()


if __name__ == '__main__':
    main()
