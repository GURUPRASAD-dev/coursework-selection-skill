from mycroft import MycroftSkill, intent_file_handler


class CourseworkSelection(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('selection.coursework1.intent')
    def handle_coursework1(self, message):
        self.speak(' A programming language - Is a formal language, which comprises a set of instructions that produce various kinds of output. Programming languages are used in computer programming to implement specific algorithms. Most programming languages consist of instructions for computers. A computer program - Is a collection of instructions that performs a specific task when executed by a computer. Most computer devices require programs to function properly. A computer program is usually written by a computer programmer and can be can be written in either high or low-level languages, depending on the task and the hardware being used.When we think about computer programmers, we probably think about people who write in high-level language. Most computer programming languages are written in a high-level programming language. They use the common English language to help make the code more understandable and to speed up the process of writing and debugging programs. Computers, however, use their own language written using binary called Machine code. This is known as a low-level language.')
    
    @intent_file_handler('selection.coursework2.intent')
    def handle_coursework2(self, message):
        self.speak(' High-level Languages – Python, Visual Basic, Java, C, C++, SQL and many more Low-level Languages – Hardware/Processor-specific assembly languages and machine code.')
    
    @intent_file_handler('selection.coursework3.intent')
    def handle_coursework3(self, message):
        self.speak(' high-level languages Independeent of hardware, translated using either a compiler or   interpreter. one statement translates into many machine code instructions.  Low-level language - classified into 1 assembly language , which translated using an assembler. one statement translates into one machine code instruction. 2 machine code, the executable binary code produced either by a compilet, interpreter or assembler.')
        
    @intent_file_handler('selection.coursework4.intent')
    def handle_coursework4(self, message):
        self.speak('advanced computer programming courses we offered are 1 python for everybody, 2 introduction to science and programming,3 HTML CSS and javascripts for webdevelopers, 4 java programming and software engineering fundamentals,5 web design for everybody, 6 basics of web development and coding,7 learn to program the fundamentals, 8 google IT automation with python, 9 microsoft word,excel,powerpoint, 10 codeyourself! an introduction to programming,11 fundamentals of computing, 12 fundamentals of excel,13 IBM data science, 14 software testing &automation,15 Genome assembly programming challenge and other basics.')
     
    @intent_file_handler('selection.coursework5.intent')
    def handle_coursework5(self, message):
        self.speak(' This Specialization builds on the success of the Python for Everybody course and will introduce fundamental programming concepts including data structures, networked application program interfaces, and databases, using the Python programming language.  ')
        
     @intent_file_handler('selection.coursework6.intent')
    def handle_coursework6(self, message):
        self.speak('Introduction to Computer Science and Programming in Python is intended for students with little or no programming experience. It aims to provide students with an understanding of the role computation can play in solving problems and to help students, regardless of their major, feel justifiably confident of their ability to write small programs that allow them to accomplish useful goals. ')   
        
     @intent_file_handler('selection.coursework7.intent')
    def handle_coursework7(self, message):
        self.speak('  Do you realize that the only functionality of a web application that the user directly interacts with is through the web page? Implement it poorly and, to the user, the server-side becomes irrelevant! Today’s user expects a lot out of the web page: it has to load fast, expose the desired service, and be comfortable to view on all devices: from a desktop computers to tablets and mobile phones.')
     
    @intent_file_handler('selection.coursework8.intent')
    def handle_coursework8(self, message):
        self.speak('Take your first step towards a career in software development with this introduction to Java—one of the most in-demand programming languages and the foundation of the Android operating system. Designed for beginners, this Specialization will teach you core programming concepts and equip you to write programs to solve complex problems. In addition, you will gain the foundational skills a software engineer needs to solve real-world problems, from designing algorithms to testing and debugging your programs. ')
        
    @intent_file_handler('selection.coursework9.intent')
    def handle_coursework9(self, message):
        self.speak(' This Specialization covers how to write syntactically correct HTML5 and CSS3, and how to create interactive web experiences with JavaScript. Mastering this range of technologies will allow you to develop high quality web sites that, work seamlessly on mobile, tablet, and large screen browsers accessible. During the capstone you will develop a professional-quality web portfolio demonstrating your growth as a web developer and your knowledge of accessible web design. This will include your ability to design and implement a responsive site that utilizes tools to create a site that is accessible to a wide audience, including those with visual, audial, physical, and cognitive impairments.')
    
    @intent_file_handler('selection.coursework10.intent')
    def handle_coursework10(self, message):
        self.speak('Behind every mouse click and touch-screen tap, there is a computer program that makes things happen. This course introduces the fundamental building blocks of programming and teaches you how to write fun and useful programs using the Python language. ')
        
    @intent_file_handler('selection.coursework11.intent')
    def handle_coursework11(self, message):
        self.speak(' This new beginner-level, six-course certificate, developed by Google, is designed to provide IT professionals with in-demand skills -- including Python, Git, and IT automation -- that can help you advance your career.Knowing how to write code to solve problems and automate solutions is a crucial skill for anybody in IT. Python, in particular, is now the most in-demand programming language by employers.')
       
    @intent_file_handler('selection.coursework12.intent')
    def handle_coursework12(self, message):
        self.speak('Excel is the most popular program for managing and reporting data.This is largely due to its availability. All computers with windows have MS Excel installed in them.It is also available on Mac OS, on different mobile devices.With the latest version of Office, Office 365, Excel has become available onlne.This means that users have access to the program from a range of devices, from almost any location.MS Excel is used by over 1.2 billion people on the planet and if you dont know how to use it yet, then youre missing out big time. ')
        
    @intent_file_handler('selection.coursework13.intent')
    def handle_coursework13(self, message):
        self.speak('Have you ever wished you knew how to program, but had no idea where to start from? This course will teach you how to program in Scratch, an easy to use visual programming language. More importantly, it will introduce you to the fundamental principles of computing and it will help you think like a software engineer. ')
        
    @intent_file_handler('selection.coursework14.intent')
    def handle_coursework14(self, message):
        self.speak('QTR 1 Fundamentals of Computing is designed to introduce students to the field of computer science through an exploration of engaging and accessible topics. Through creativity and innovation, students will use critical thinking and problem solving skills to implement projects that are relevant to students lives. ')
        
    @intent_file_handler('selection.coursework15.intent')
    def handle_coursework15(self, message):
        self.speak('Data science is one of the hottest professions of the decade, and the demand for data scientists who can analyze data and communicate results to inform data driven decisions has never been greater. This Professional Certificate from IBM will help anyone interested in pursuing a career in data science or machine learning develop career-relevant skills and experience.It’s a myth that to become a data scientist you need a Ph.D. Anyone with a passion for learning can take this Professional Certificate – no prior knowledge of computer science or programming languages required – and develop the skills, tools, and portfolio to have a competitive edge in the job market as an entry level data scientist. ')
        
    @intent_file_handler('selection.coursework16.intent')
    def handle_coursework16(self, message):
        self.speak('This Specialization is intented for beginning to intermediate software developers seeking to develop knowledge and skill in implementing testing techniques and tools in the development of their projects. Through four courses, you will cover black-box and white-box testing, automated testing, web & mobile testing, and formal testing theory and techniques, which will prepare to you to plan and perform effective testing of your software. ')
    
    @intent_file_handler('selection.coursework17.intent')
    def handle_coursework17(self, message):
        self.speak('In Spring 2011, thousands of people in Germany were hospitalized with a deadly disease that started as food poisoning with bloody diarrhea and often led to kidney failure. It was the beginning of the deadliest outbreak in recent history, caused by a mysterious bacterial strain that we will refer to as E. coli X. Soon, German officials linked the outbreak to a restaurant in Lübeck, where nearly 20% of the patrons had developed bloody diarrhea in a single week. At this point, biologists knew that they were facing a previously unknown pathogen and that traditional methods would not suffice – computational biologists would be needed to assemble and analyze the genome of the newly emerged pathogen. ')
        
    @intent_file_handler('selection.coursework18.intent')
    def handle_coursework18(self, message):
        self.speak(' Access to lectures and assignments depends on your type of enrollment. If you take a course in audit mode, you will be able to see most course materials for free. To access graded assignments and to earn a Certificate, you will need to purchase the Certificate experience, during or after your audit. If you dont see the audit option:The course may not offer an audit option. You can try a Free Trial instead, or apply for Financial Aid.The course may offer Full Course, No Certificate instead. This option lets you see all course materials, submit required assessments, and get a final grade. This also means that you will not be able to purchase a Certificate experience.')    
    
    @intent_file_handler('selection.coursework19.intent')
    def handle_coursework19(self, message):
        self.speak(' Yes! To get started, click the course card that interests you and enroll. You can enroll and complete the course to earn a shareable certificate, or you can audit it to view the course materials for free. When you subscribe to a course that is part of a Specialization, you’re automatically subscribed to the full Specialization. Visit your learner dashboard to track your progress. ')
        
    @intent_file_handler('selection.coursework20.intent')
    def handle_coursework20(self, message):
        self.speak('This Specialization doesnt carry university credit, but some universities may choose to accept Specialization Certificates for credit. Check with your institution to learn more. ')    
        
    @intent_file_handler('selection.coursework21.intent')
    def handle_coursework21(self, message):
        self.speak('When you enroll in the course, you get access to all of the courses in the Specialization, and you earn a certificate when you complete the work. If you only want to read and view the course content, you can audit the course for free. If you cannot afford the fee, you can apply for financial aid. ')
        
    @intent_file_handler('selection.coursework22.intent')
    def handle_coursework22(self, message):
        self.speak('Yes! To get started, click the course card that interests you and enroll. You can enroll and complete the course to earn a shareable certificate, or you can audit it to view the course materials for free. When you subscribe to a course that is part of a Certificate, you’re automatically subscribed to the full Certificate. Visit your learner dashboard to track your progress.')
        
    @intent_file_handler('selection.coursework23.intent')
    def handle_coursework23(self, message):
        self.speak('Data science is the process of collecting, storing, and analyzing data. Data scientists use data to tell compelling stories to inform business decisions. Learn more about what data science is and what data scientists do in the first course of this Professional Certificate, "What is Data Science?" ')
        
    @intent_file_handler('selection.coursework24.intent')
    def handle_coursework24(self, message):
        self.speak(' An understanding of data science and the ability to make data driven decisions is useful in any career, but some careers specifically require a data science background. Some examples of careers in data science include:- Business Intelligence Analyst- Data Analyst- Data Architect- Data Engineer- Data Scientist- Machine Learning Engineer- Marketing Analyst- Operations Analyst- Quantitative Analyst')
        
    @intent_file_handler('selection.coursework25.intent')
    def handle_coursework25(self, message):
        self.speak('This Professional Certificate is open for anyone with any job and academic background. No prior computer programming experience is necessary, but is an asset, as are familiarity working with computers, high school math, and communication and presentation skills. For the last few courses, knowledge of calculus and linear algebra is an asset but not an absolute requirement. ')
        
    @intent_file_handler('selection.coursework26.intent')
    def handle_coursework26(self, message):
        self.speak('Yes, it is highly recommended to take the courses in the order they are listed, as they progressively build on concepts taught in previous courses. For example the Data Analysis, Data Visualization, and Machine Learning courses require knowledge of Python covered earlier in the program. ')    
    
    @intent_file_handler('selection.coursework27.intent')
    def handle_coursework27(self, message):
        self.speak(' Become job ready for a career in Data Science. Develop practical skills using hands-on labs in Cloud environments, projects and captsones.')
                   
    @intent_file_handler('selection.coursework28.intent')
    def handle_coursework28(self, message):
        self.speak('Yes, absolutely. Any courses that you have already completed as part of that Specialization will be marked as "Complete". You do not have to take those courses again and will be able to finish this Professional Certificate more quickly. ')
      
    @intent_file_handler('selectcion.coursework29.intent')
    def handle_coursework29(self, message):
        self.speak('This Specialization is designed to serve as an on-ramp for programming, and has no pre-requisites. The pace of the first two courses is aimed at those with no programming experience at all.')
        
def create_skill():
    return CourseworkSelection()

