from collections import Counter

# https://en.wikipedia.org/wiki/Machine_learning
ml_wikipedia_text = """
Machine learning (ML) is an umbrella term for solving problems for which development of algorithms by human programmers would be cost-prohibitive, and instead the problems are solved by helping machines 'discover' their 'own' algorithms,[1] without needing to be explicitly told what to do by any human-developed algorithms.[2] Recently, generative artificial neural networks have been able to surpass results of many previous approaches.[3][4] Machine learning approaches have been applied to large language models, computer vision, speech recognition, email filtering, agriculture and medicine, where it is too costly to develop algorithms to perform the needed tasks.[5][6]

The mathematical foundations of ML are provided by mathematical optimization (mathematical programming) methods. Data mining is a related (parallel) field of study, focusing on exploratory data analysis through unsupervised learning.[8][9]

ML is known in its application across business problems under the name predictive analytics. Although not all machine learning is statistically-based, computational statistics is an important source of the field's methods.
The term machine learning was coined in 1959 by Arthur Samuel, an IBM employee and pioneer in the field of computer gaming and artificial intelligence.[10][11] The synonym self-teaching computers was also used in this time period.[12][13]

By the early 1960s an experimental "learning machine" with punched tape memory, called Cybertron, had been developed by Raytheon Company to analyze sonar signals, electrocardiograms, and speech patterns using rudimentary reinforcement learning. It was repetitively "trained" by a human operator/teacher to recognize patterns and equipped with a "goof" button to cause it to re-evaluate incorrect decisions.[14] A representative book on research into machine learning during the 1960s was Nilsson's book on Learning Machines, dealing mostly with machine learning for pattern classification.[15] Interest related to pattern recognition continued into the 1970s, as described by Duda and Hart in 1973.[16] In 1981 a report was given on using teaching strategies so that a neural network learns to recognize 40 characters (26 letters, 10 digits, and 4 special symbols) from a computer terminal.[17]

Tom M. Mitchell provided a widely quoted, more formal definition of the algorithms studied in the machine learning field: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P if its performance at tasks in T, as measured by P, improves with experience E."[18] This definition of the tasks in which machine learning is concerned offers a fundamentally operational definition rather than defining the field in cognitive terms. This follows Alan Turing's proposal in his paper "Computing Machinery and Intelligence", in which the question "Can machines think?" is replaced with the question "Can machines do what we (as thinking entities) can do?".[19]

Modern-day machine learning has two objectives, one is to classify data based on models which have been developed, the other purpose is to make predictions for future outcomes based on these models. A hypothetical algorithm specific to classifying data may use computer vision of moles coupled with supervised learning in order to train it to classify the cancerous moles. A machine learning algorithm for stock trading may inform the trader of future potential predictions.[20]

As a scientific endeavor, machine learning grew out of the quest for artificial intelligence (AI). In the early days of AI as an academic discipline, some researchers were interested in having machines learn from data. They attempted to approach the problem with various symbolic methods, as well as what were then termed "neural networks"; these were mostly perceptrons and other models that were later found to be reinventions of the generalized linear models of statistics.[22] Probabilistic reasoning was also employed, especially in automated medical diagnosis.[23]: 488 

However, an increasing emphasis on the logical, knowledge-based approach caused a rift between AI and machine learning. Probabilistic systems were plagued by theoretical and practical problems of data acquisition and representation.[23]: 488  By 1980, expert systems had come to dominate AI, and statistics was out of favor.[24] Work on symbolic/knowledge-based learning did continue within AI, leading to inductive logic programming, but the more statistical line of research was now outside the field of AI proper, in pattern recognition and information retrieval.[23]: 708–710, 755  Neural networks research had been abandoned by AI and computer science around the same time. This line, too, was continued outside the AI/CS field, as "connectionism", by researchers from other disciplines including Hopfield, Rumelhart, and Hinton. Their main success came in the mid-1980s with the reinvention of backpropagation.[23]: 25 

Machine learning (ML), reorganized and recognized as its own field, started to flourish in the 1990s. The field changed its goal from achieving artificial intelligence to tackling solvable problems of a practical nature. It shifted focus away from the symbolic approaches it had inherited from AI, and toward methods and models borrowed from statistics, fuzzy logic, and probability theory.[24]
"""

# https://wiki.python.org/moin/BeginnersGuide
python_beginner_guide_text = """
Beginner's Guide to Python
New to programming? Python is free and easy to learn if you know where to start! This guide will help you to get started quickly.

Chinese Translation/中文版入门

New to Python?
Read BeginnersGuide/Overview for a short explanation of what Python is.

Getting Python
Next, install the Python 3 interpreter on your computer. This is the program that reads Python programs and carries out their instructions; you need it before you can do any Python programming. Mac and Linux distributions may include an outdated version of Python (Python 2), but you should install an updated one (Python 3). See BeginnersGuide/Download for instructions to download the correct version of Python.

There are also Python interpreter and IDE bundles available, such as Thonny. Other options can be found at IntegratedDevelopmentEnvironments.

At some stage, you'll want to edit and save your program code. Take a look at HowToEditPythonCode for some advice and recommendations.

Learning Python
Next, read a tutorial and try some simple experiments with your new Python interpreter.

If you have never programmed before, see BeginnersGuide/NonProgrammers for a list of suitable tutorials.

If you have previous programming experience, consult BeginnersGuide/Programmers, which lists more advanced tutorials.

If English isn't your first language, you might be more comfortable with a tutorial that's been translated into your language. Consult python.org's list of Non-English resources.

Most tutorials assume that you know how to run a program on your computer. If you are using Windows and need help with this, see How do I Run a Program Under Windows.

Some sites offer in-browser coding for those who want to learn Python:


Codédex

Codecademy

Coding Bootcamps

DataCamp

Dataquest for Python for data science.

HackInScience free and open source platform.

High School Technology Services for general Python

Python Land: A completely free beginners tutorial with interactive, editable code examples

Print a cheat sheet of the most important Python features and post it to your office wall until you know the basics well.

Once you have read a tutorial, you can browse through Python's online documentation. It includes a tutorial that might come in handy, a Library Reference that lists all of the modules that come standard with Python, and the Language Reference for a complete (if rather dry) explanation of Python's syntax.

When you are ready to write your first program, you will need a text editor or an IDE. If you don't want to use Thonny or something more advanced, then you can use IDLE, which is bundled with Python and supports extensions.

This Python wiki also contains a page about Python One-Liners -- an obscure but interesting subculture in Python.

Need Help?
Need help with any of this? Read BeginnersGuide/Help for mailing lists and newsgroups.

Most Python books will include an introduction to the language; see IntroductoryBooks for suggested titles.

Consult BeginnersGuide/Examples for small programs and little snippets of code that can help you learn.

Or, if you prefer to learn Python through listening to a lecture, you can attend a training course or even hire a trainer to come to your company. Consult the PythonEvents page to see if any training courses are scheduled in your area and the PythonTraining page for a list of trainers.

Teachers can join the EDU-SIG, a mailing list for discussion of Python's use in teaching at any level ranging from K-12 up to university.

Complete list of Beginner's Guide pages
BeginnersGuide/Download
BeginnersGuide/Examples
BeginnersGuide/Help
BeginnersGuide/Mathematics
BeginnersGuide/NonProgrammers
BeginnersGuide/NonProgrammersChinese
BeginnersGuide/Overview
BeginnersGuide/OverviewChinese
BeginnersGuide/Programmers
BeginnersGuide/Programmers (Cpp2Python.pdf)
BeginnersGuide/Programmers/SimpleExamples
Quiz and Exercises
Finxter - How good are your Python skills? Test and Training with a Daily Python Puzzle

CheckIO - Online learning, testing and improving your python skills

After Hours Programming - Python Quiz

PyGUI - Collection of python quiz answers, Examples And GUI Tkinter Tutorials For Beginners

Pythonspot - Python Quiz

Python Challenge - A Python Quiz App on Android Platform

CS Circles - online lessons and graded exercises

Python Style Checker
Pythonchecker.com - An educative online tool to rate your Python style (with dynamic score computation and hints)

Looking for a particular Python module or application?
The first place to look is the Python Package Index.

If you can't find anything relevant in the Package Index,
try searching python.org - you can find anything mentioned on the Python site, in the FAQs, or in the newsgroup. More info: where to search.

You may also try our external guest project, pydoc.net, for advanced package and module search.

Next, try Google or another search engine of your choice. Searching for "python" and some relevant keywords will usually find something helpful.

Finally, you can try posting a query to the comp.lang.python Usenet group.
Python-Related Cheat Sheets
Python: Collection of 11 Best Python Cheat Sheets

NumPy: Collection of 10 Best NumPy Cheat Sheets

Pandas: Collection of 7 Beautiful Pandas Cheat Sheets

Machine Learning: Collection of 15 Machine Learning Cheat Sheets

Want to contribute?
Python is a product of the Python Software Foundation, a non-profit organization that holds the copyright. Donations to the PSF are tax-deductible in the USA, and you can donate via credit card or PayPal.

To report a bug in the Python core, use the Python Bug Tracker.

To contribute a bug fix or other patch to the Python core, read the Python Developer's Guide for more information about Python's development process.

To contribute to the official Python documentation, join the Documentation SIG, write to docs@python.org , or use the Issue Tracker to contribute a documentation patch.

To announce your module or application to the Python community, use comp.lang.python.announce. See the guide to Python mailing lists for more information.

To propose changes to the Python core, post your thoughts to comp.lang.python. If you have an implementation, follow the Python Patch Guidelines.

If you have a question are not sure where to report it, check out the WhereDoIReportThis? page.
"""


def find_ten_most_common_letters(text_counter):
    letter_frequency_tuple = [(letter, count / ml_total_chars) for letter, count in text_counter.items()]
    letter_frequency_dict = dict(letter_frequency_tuple)
    letter_frequency_counter = Counter(letter_frequency_dict)
    return letter_frequency_counter.most_common(10)


def print_most_common(most_common):
    for character, frequency in most_common:
        print("{} => {:.2f}%".format(character, frequency * 100))


if __name__ == '__main__':
    ml_text_counter = Counter(ml_wikipedia_text.strip().lower())
    ml_total_chars = sum(ml_text_counter.values())
    print(ml_total_chars)

    python_text_counter = Counter(python_beginner_guide_text.strip().lower())
    python_total_chars = sum(python_text_counter.values())
    print(python_total_chars)

    ml_most_common = find_ten_most_common_letters(ml_text_counter)
    python_most_common = find_ten_most_common_letters(python_text_counter)

    print("Machine Learning top 10 letters used:")
    print_most_common(ml_most_common)
    print("Python top 10 letters used:")
    print_most_common(python_most_common)
