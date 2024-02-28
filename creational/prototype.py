from abc import ABCMeta, abstractmethod
import copy 

"""
ABCMeta: Abstract Base Class Meta, is a metaclass for defining abstract base classes.
abstractmethod: A decorator indicating abstract methods.
"""
class CoursesGFG(metaclass=ABCMeta):
    # constructor 
    def __init__(self):
        self.id = None 
        self.type = None 
    
    @abstractmethod 
    def course(self):
        pass    
    def get_tpye(self):
        return self.type 

    def get_id(self):
        return self.id 

    def set_id(self, sid):
        self.id = sid
    
    def clone(self):
        return copy.copy(self)

# class DSA Course    
class DSA(CoursesGFG):
    def __init__(self):
        super().__init__()
        self.type = "Data Structures and Algorithms"
    
    def course(self):
        print(f"Inside DSA::course() method")


# class SDE Course
class SDE(CoursesGFG):
    def __init__(self):
        super().__init__()
        self.type = "Software Development Engineer"
    
    def course(self):
        print(f"Inside SDE::course() method")

# class STL Course
class STL(CoursesGFG):
    def __init__(self):
        super().__init__()
        self.type = "Standard Template Library"
    
    def course(self):
        print(f"Inside STL::course() method")


# class- Course GFG Cache
class CourseGFGCache:
    cache = {}

    @staticmethod
    def get_course(sid):
        COURSE = CourseGFGCache.cache.get(sid, None)
        return COURSE.clone() 

    @staticmethod
    def load():
        sde = SDE()
        sde.set_id("1")
        CourseGFGCache.cache[sde.get_id()] = sde

        dsa = DSA()
        dsa.set_id("2")
        CourseGFGCache.cache[dsa.get_id()] = dsa

        stl = STL()
        stl.set_id("3")
        CourseGFGCache.cache[stl.get_id()] = stl

if __name__ == "__main__":
    CourseGFGCache.load()

    sde = CourseGFGCache.get_course("1")
    print(f"Course: {sde.get_tpye()}")

    dsa = CourseGFGCache.get_course("2")
    print(f"Course: {dsa.get_tpye()}")

    stl = CourseGFGCache.get_course("3")
    print(f"Course: {stl.get_tpye()}")





