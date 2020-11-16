# evaluator.py

"""
"""

class Student:
    """
    """

    def __init__(self, name):
        """
        Initialiser
        Args:
            name : Name of the Student
        """
        self.level = 1
        self.name = name
        self.top_level = 4
        self.bottom_level = 0
        
       

    def reset(self, subject):
        """
        Resets the Evaluator state to the Beginning

        Args:
            subject(str): Subject Name

        """
        self._level = 1
        self._subject = subject

    def begin_course(self, subject):
        """
        Creates an Evaluator for the course

        Args:
            subject = Name of the Subject

        """
        self.subject = subject
        self.evaluator = Evaluator()

    def answer_correctly_firstattempt(self, question):
        """
        Simulates the behavior of the student responding with correct answer
        in first attempt.

        Args:
            question: Question for which the behavior is observed and metrics collected

        Returns:
            metrics object of type Answer.  
        """
        metrics = Answer()
        metrics.sample_answer_metrics(question, True, 1, True, 70.9)
        return metrics
        
    def answer_correctly_with_iteration(self, question):
        """
        Simulates the behavior of the student responding with correct answer
        with iteration.

        Args:
            question: Question for which the behavior is observed and metrics collected

        Returns:
            metrics object of type Answer.  
        """
        metrics = Answer()
        metrics.sample_answer_metrics(question, True, 1, False, 100)
        return metrics

    def answer_partly(self, question):
        """
        Simulates the behavior of the student responding with partly correct
        answer.
        
        Args:
            question: Question for which the behavior is observed and metrics collected

        Returns:
            metrics object of type Answer.  
        """
        metrics = Answer()
        metrics.sample_answer_metrics(question, True, 2, False, 200)
        return metrics

    def answer_wrongly(self, question):
        """
        Simulates the behavior of the student responding with wrong answer.
        
        Args:
            question: Question for which the behavior is observed and metrics collected

        Returns:
            metrics object of type Answer.  
        """
        metrics = Answer()
        metrics.sample_answer_metrics(question, True, 0, False, 100)
        return metrics   

    def did_not_answer(self, question):
        """
        Simulates the behavior of the student did not answer.
        Args:
            question: Question for which the behavior is observed and metrics collected

        Returns:
            metrics object of type Answer.  
        """
        metrics = Answer()
        metrics.sample_answer_metrics(question, False, 0, False, 100)
        return metrics



class Question:
    """
    This class is created to test the Evaluator Class 
    """

    def __init__(self, expected_answer_time, max_no_appearances,
                 interval_between_appearances, visibility_time):
        """
        Initialiser to intialise attributes of the question
        """
# The following attributes are initialised while the question object is created
        self._expected_answer_time = expected_answer_time
        self._max_no_appearances = max_no_appearances
        self._interval_between_appearances = interval_between_appearances
        self._visibility_time = visibility_time

# The following attributes are updated everytime after the question is answered
        self.no_of_appearances = 0;
        self.no_correctly_answered = 0
        self.no_of_first_attempted_correct_answers = 0
        self.no_of_partly_answered = 0
        self.no_of_wrongly_answered = 0
        self.no_of_unattempted = 0
        self.visibility_time = visibility_time
        
        self.list_of_answer_times = [expected_answer_time] #  time taken to answer correctly by students

    def present_question(self):
        """
        Presents the question and collect answer

        """
        #Presenting the question is out of our scope

        
        


class Answer:
    """
    This class is created to test the logic used in
    the Evaluator Class
    """

    def __init__(self):
        """
        Initialise to set default values for an answer.
        """
        self.answered = False
        self.correct_answer = 0
        self.first_attempt = False
        self.answer_time = 0

    def sample_answer_metrics(self, question, answered, correct_answer, first_attempt,
                                answer_time):
        """
        To create a metrics based on the response from the student given as arguements
        and update the dynamic attributes of the question
        

        Args:
            question;  The question being answered
            answered: True if answered or False
            Corrrect_answer: 0 for wrong answer, 1 for correct answer, 2 for part correct answer
            first_attempt: True if first ateempt, False for Iterated
            answer_time: time taken to answer
        """
            
        self._question_answered = question
        self.answered = answered
        self.correct_answer = correct_answer
        self.first_attempt = first_attempt
        self.answer_time = answer_time
        question.no_of_appearances +=1
        question.list_of_answer_times.append(answer_time)
        if answered:
            if correct_answer == 1:
                if first_attempt:
                    question.no_of_first_attempted_correct_answers += 1
                      
                elif correct_answer == 2:
                    question.no_of_partly_answered += 1 
                elif correct_answer == 0:
                    question.no_of_wrongly_answered = +1

        else:
            question.no_of_unattempted +=1
        
        

class Evaluator:
    """
    A simple evalautor to implement the MDP 
    """

    def __init__(self):
        """
        Constructor for the Evaluator Class

        """

        
        self._state = 1
        self._lower_state = 0
        self._upper_state = 4

    def evaluate(self, student, metrics):
        """
        This function evaluate and update of the state of the Evaluator.
        Also updates the level of the student as a feedabck to the content
        delivery
        Args:
            answered:  Boolean.  TRUE if answered or FALSE
            correct_answer: Integer 0 for Not Correct, 1 for all correct,
            2 for partial correctness
            first_attempt: Boolean.  True for answered without iteration or False
            answer_time: in Seconds 

        Returns:
            Return the Performance score after evalauting the student
            based on the input arguments.

        """
        if metrics.answered:
            if metrics.correct_answer == 1 and metrics.first_attempt:
                if self._state != self._upper_state:
                    self._state += 1
                if student.level != student.top_level:
                    student.level +=1
            elif metrics.correct_answer == 1 and metrics.first_attempt== False:
                if student.level == self._state:
                    if self._state != self._lower_state:
                        self._state -= 1
                    if student.level != student.bottom_level:
                        student.level -=1
            elif metrics.correct_answer == 2:
                if student.level != student.bottom_level:
                    student.level -= 1
            elif metrics.correct_answer == 0:
                if self._state != self._lower_state:
                    self._state -= 1
                if student.level != student.bottom_level:
                        student.level -=1
        else:
            if self._state != self._lower_state:
                self._state -= 1
                
        # print("The Evaluator State is {} and the Student {} Level is {} ".
        #          format(self._state, student.name, student.level))
        return (self._state + student.level)
                  

                    
                    
                
            

        
