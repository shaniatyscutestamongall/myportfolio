#Define the biueprint(class)
class student:
    def __int__(self, name, score):
        self.name = name 
        self.score  = score

def display(self):    #method 
    print(f"{self.name:  {self.score}")

def get_grades(self):   #method
    if self.score >= 90
        return "a"
    elif self.score >= 80
        return "b"
    elif self.score >= 70:
        return "c"
        else:
    return "d"

#system state = a list of objects
students = []

def add_student():
    name = input("name:")
    score =float( input("score: "))
    students.append(student(name, score,))
    print ("student added!")
    
def display_all():
    print ("\n--- all records ---")
    
#compute class average using object data
total = sum(s.score for s in students)
average = total /len(students)
print(f"\n class average: {average: .2f} ")

def find_student():
    name = input("name to find: ")
    for s in students:
        if s.name == name: 
            s.display()
            print (fr"grade: {s.get_grades()}")
            return
    print ("Student not found.")
    
def get_average():
    if not student:
        print ("no records.")
        return 
    return sum(s.score for s in students) / len(students)
    
def main_menu():
    wile true:
        print("\n ====== student Info system ======")
        print("1. add student")
        print("2. display students")
        print("3. find students")
        print("4. class average")
        print("5. exit")
        choice =input("choice: ")
        
        if choice =='1':
            add_student()
        elif choice == '2':
            display_all()
        elif choice == '3':
            find_student()
        elif choice == '4':
            print(f"average: {get_average():.2f}")
        elif choice == '5':
            break
            
main_menu()