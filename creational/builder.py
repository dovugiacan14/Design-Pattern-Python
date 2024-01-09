class Course: 
    def __init__(self):
        self.Fee()
        self.available_batches()

    def Fee(self):
        raise NotImplementedError
    
    def available_batches(self): 
        raise NotImplementedError 
    
    # provide a way to control the creation of the object under string representation
    def __repr__(self):
        return 'Fee : {0.fee} | Batches : {0.batches}'.format(self)


class DSA(Course):
    def Fee(self):
        self.fee = 8000
    
    def available_batches(self):
        self.batches = 5
    
    def __str__(self):
        return "DSA"


class STL(Course):
    def Fee(self):
        self.fee = 9000
    
    def available_batches(self):
        self.batches = 4
    
    def __str__(self):
        return "STL"
    

class SDE(Course):
    def Fee(self):
        self.fee = 10000
    
    def available_batches(self):
        self.batches = 3
    
    def __str__(self):
        return "SDE"

# ==============================================================
class ComplexCourse:
    def __repr__(self):
        return 'Fee : {0.fee} | Batches : {0.batches}'.format(self)


class Complexcourse(ComplexCourse):
    def Fee(self):
        self.fee = 7000
    
    def available_batches(self):
        self.batches = 6

def construct_complex(cls):
    course = cls()
    course.Fee()
    course.available_batches()
    return course

if __name__=="__main__":
    dsa = DSA()
    sde = SDE()
    stl = STL()

    complex_course = construct_complex(Complexcourse) 
    print(complex_course)
    
    




    

