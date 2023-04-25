class Student:
    def __init__(self, surname, first_name, student_number):
        self.__surname = surname
        self.__first_name = first_name
        self.__student_number = student_number
        self.__total_credits = 0
        self.__level = self.__studentEval()

    def add_credits(self, credits):
        if credits > 0:
            self.__total_credits += credits
            self.__level = self.__studentEval()
        else:
            print("Error: Number of credits must be greater than zero.")

    def get_total_credits(self):
        return self.__total_credits

    def __studentEval(self):
        if (self.__total_credits >= 90):
            return "Excellent"
        elif (self.__total_credits >= 80):
            return "Very good"
        elif (self.__total_credits >= 70):
            return "Good"
        elif (self.__total_credits >= 60):
            return "Fair"
        else:
            return "Insufficient"

    def studentInfo(self):
        print("Student Information:")
        print(f"Name: {self.__first_name} {self.__surname}")
        print(f"Identifier: {self.__student_number}")
        print(f"Level: {self.__level}")


class Job:
    def __init__(self, job_title, salary):
        self.job_title = job_title
        self.salary = salary
        self.__applicants = []

    def add_applicant(self, applicant):
        self.__applicants.append(applicant)

    def get_applicants(self):
        return self.__applicants


# Example usage
john = Student("Doe", "John", 145)
john.add_credits(5)
john.add_credits(3)
john.add_credits(4)

print(
    f"The student {john._Student__first_name} {john._Student__surname} has {john.get_total_credits()} points.")
print("--------------------")

programmer_job = Job("Programmer", 60000)

jane = Student("Doe", "Jane", 146)
jane.add_credits(2)
jane.add_credits(3)
jane.add_credits(4)

programmer_job.add_applicant(john)
programmer_job.add_applicant(jane)

applicants = programmer_job.get_applicants()

for applicant in applicants:
    applicant.studentInfo()
