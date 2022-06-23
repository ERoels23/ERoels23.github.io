---
layout: page
title: "Updates"
permalink: /updates/
---

## Week 1: Diving In
Of course, we can't begin our own research until we've at least sampled the current state of research in the field. The concept of a notional machine was first justified by Benedict Du Boulay in 1986. His paper, [*Some Difficulties of Learning to Program*](https://www.bibsonomy.org/bibtex/2e63b8419af16b225d3ef00fe08c12a1b/ji), detailed 5 key difficulties encountered by beginner programmers: Orientation, Notation, Structures, Pragmatics, and The Notional Machine. He placed emphasis on this Notional Machine because of its tendency to produce misconceptions in students when designed poorly. He then goes on to explain the most common misconceptions and how best to avoid them based on his experience. This paper was fundamental to the importance of Notional Machines, highlighting the need for more work to be done.

"...inventing a consistent story that describes events at the right level of detail is not easy. Very often an analogy introduced at one point does not fit later on, so producing extra confusion in addition to any misapplication of the analogy at the point where it was appropriate"
-- Benedict Du Boulay, 1986

And more work has, indeed, been done. Most notably in Dr. Juha Sorva's doctoral dissertation, titled [*Visual Program Simulation in Introductory Programming Education*](https://aaltodoc.aalto.fi/handle/123456789/3534), where he revisits the difficulties cited by Du Boulay. Using more modern psychological and educational research, he describes his own set of the 5 most pressing challenges for novice programmers:

1. Creating programs imposes a great cognitive load on novice programmers
2. Programmers need plan schemas which represent generic solutions to common problems, but novices have few
3. Novices have misconceptions about basic programming concepts, which give them trouble when reading and writing programs
4. Many creative and unexpected programming tasks require mental tracing of programs, something that novices are not always capable of
5. Novices need to form a viable mental model of a notional machine to be able to understand program execution

Then describes the goals and functions of a Notional Machine:
- is an idealized abstraction of computer hardware and other aspects of the runtime environment of programs
- serves the purpose of understanding what happens during program execution
- is associated with one or more programming paradigms or languages (or subsets thereof) to be described
- gives a particular perspective to the execution of programs
- correctly reflects what programs do when executed

Then forms a select group of principles which one should follow closely when designing a Notional Machine:
- No-Function-In-Structure: system components are context-free (specific components work independently of the overall system)
- Locality: component behavior is not defined by higher levels of abstraction
- Weak Causality: there is a clear cause and effect relationship between events in the system and on the model
- Deletion: if a vital part of the system is removed, the mental model should predict a disfunctional system

I came across several great examples of Notional Machines:

<img src="/pytutor.png" alt="PythonTutor" height="200"> <img src="/uuhistle.png" alt="UUhistle" height="200"> <img src="/novis.png" alt="Novis" height="200">

1. [PythonTutor.com](PythonTutor.com) is a fantastic resource for learning Python and several other languages, it's the most popular Notional Machine around today!
2. UUhistle (pronounced "Whistle") was a project produced as a part of Juha Sorva's Dissertation
3. Novis is a notional machine produced to work within BlueJ to help visualize Java programs. Produced by Michael Berry and Michael Kolling [link here](https://www.researchgate.net/publication/266657026_The_state_of_play_A_notional_machine_for_learning_programming)


## Week 2: Making the Machine
My priority this week was understanding what information I can gather about a program before/during/after its execution. All of these together will form a set a tools that I may use to extract critical information about a program that needs to be represented in a Notional Machine. 

There are many modules for Python which I've started playing around with:
- AST (abstract syntax trees)
- StackTrace
- Trace
- PDB/BDB

This week I focused primarily on the AST module, and produced abstract syntax trees for a variety of sample Python programs.

<img src="/ast.png" alt="AST" height="300">

These trees do a fantastic job of showing the operations done by the computer to do something as simple as assigning a variable. 
They are also useful for understanding the relationships between entities in the program, which functions are called, etc.
However, when trying to adapt this information into Notional Machine, we run into some problems:
- ASTs do nothing to show the order in which operations occur. This is critical for a good NM.
- Even taking a snapshot of the AST after each line of code could still lead to misorderings.

This week is also when this website was born! It has gone through several changes since it's initial conception.
At first, I wanted to write the website nearly from scratch, but that quickly became too much work.
Instead, I installed a Jeckyll theme that worked with GitHub Pages by default, and then edited a Markdown file for each of the pages on the website.
After installing a bunch of dependencies and fiddling around with HTML, my site was born!

## Week 3: Program Parsing
With goals in mind as to how I should construct my Notional Model, it's now time to start constructing it.
To do this, I started by identifying the key parts of program execution and noted how they were represented in various notional machines.
Take a look at this example from PythonTutor showing several stack frames and object instantiations:

<img src="/pytutor2.png" alt="pytutorEx1" height="300">

- Variables are denoted as a yellow box with space for the value inside, with a label for the variable's name
- Objects are included in a separate "Objects" column with room for both definitions and instances
- Stack Frames are denoted in the left column, labeled "Frames". The current active frame is saturated while the others are not
There are tons of tiny little decisions that went into how this notional machine looks, and each one is important if we are aiming for maximum student understanding.
There are also many animated aspects of PythonTutor that are not displayed with a static image. Important program transitions are displayed with brief animations, aiding the student in understanding program execution.

After getting a good idea of what I should be looking for, I returned to the modules I introduced in Week 2 and started hunting.
Abstract Syntax Trees, StackTrace, and PDB all represent the program's execution in different ways. 

In the coming weeks, I will be isolating specific program events with the help of these modules, and then using them to write a program which can translate a Python program into its occompanying notional machine!

## Week 4: The Debugger
(coming soon!)

[GitHub Repository](https://github.com/ERoels23/ERoels23.github.io/)
