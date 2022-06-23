---
layout: page
title: "Home"
permalink: /
order: 1
---

Welcome to my website! As a part of the [DREAM Research Program](https://tech.mines.edu/dream/), I'm spending this summer investigating Notional Machines.

### What is a Notional Machine?
If you've studied Computer Science even a little bit, it's more than likely that you've come across several already, as they are excellent educational tools, especially for beginner CS students.
A notional machine is a visual representation of program execution. In essence, a Notional Machine seeks to capture the general gist (or notion, if you will) of what a computer is doing while executing a program.
One fantastic and popular example comes from [Python Tutor](https://pythontutor.com/) 

### Why Study Them?
There are several reasons for continuing the work on Notional Machines. Although a site like PythonTutor functions well and has surely helped countless CS students, its visual design still has more potential. The way we choose to represent a part of a program has long-reaching consequences. For example, a variable might be displayed as a box which holds a value. Most students might assume that each box can hold only one value, which is correct, but some students might get the wrong impression that a variable can hold more than one value, simply because of the way that we chose to represent it visually.

The translation of a program into a notional machine is also of interest. There are many ways to obtain information about how a program is running. The simplest example is a stacktrace, which is typically printed out when a program hits an error. Efficient and targetted translation would help build educational tools and make notional machines for accessible to the beginner CS student.

### My Goals
Computers do a LOT of work behind-the-scenes to make things happen. Sometimes this behind-the-scenes work can give meaningful insight into how a program runs, and other times it introduces unecessary complexity which would only serve to confuse a novice programmer. Because of this discrepency, every notional model MUST "lie" to students on some level. 

For example, all objects in Python are actually stored on the heap, with references placed in the relevant stack frames where they're a "local variable". In a notional representation, it would be most accurate to show these objects stored in the heap with references inside stack frames, but this would not be helpful to beginner programmers because we treat objects as if they are stored in stack frames. This notion of stack frames is also a fundamental principle of programming, so novices would be robbed of valuable concepts simply because of an implementation choice made by Python.

My ideal notional machine would be open and honest about how and when it was lying to the user, giving them options to adjust the level of accuracy/complexity. This will prioritize understanding while still allowing students to dig deeper if they so choose!


[GitHub Repository](https://github.com/ERoels23/ERoels23.github.io/)
