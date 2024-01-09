import random 
class DSA: 
    def __init__(self):
        pass 

    def fee(self):
        return 11000
    
    def __str__(self):
        return "DSA"


class STL: 
    def __init__(self):
        pass

    def fee(self):
        return 12000
    
    def __str__(self):
        return "STL"


class SDE: 
    def __init__(self):
        pass

    def fee(self):
        return 13000
    
    def __str__(self):
        return "SDE"
    

class CourseFactory:
    def __init__(self, courses_list):
        self.courses_list = courses_list
    
    def show_course(self):
        course = self.courses_list()

        print(f"we have a course {course}")
        print(f"it's price is {course.fee()}")


if __name__ == "__main__":
    for i in range(5):
        course = CourseFactory(random.choice([DSA, STL, SDE]))
        course.show_course()
        print("\n")
    

