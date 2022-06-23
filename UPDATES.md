---
layout: page
title: "Updates"
permalink: /updates/
---

## Week 1: Diving In
Of course, we can't begin our own research until we've at least sampled the current state of research in the field. The concept of a notional machine was first justified by Benedict Du Boulay in 1986. His paper, *Some Difficulties of Learning to Program*, detailed 5 key difficulties encountered by beginner programmers: Orientation, Notation, Structures, Pragmatics, and The Notional Machine. He placed emphasis on this Notional Machine because of its tendency to produce misconceptions in students when designed poorly. He then goes on to explain the most common misconceptions and how best to avoid them based on his experience. This paper was fundamental to the importance of Notional Machines, highlighting the need for more work to be done.
Quote Here: "inventing a consistent story..."

And more work has, indeed, been done. Most notably in Dr. Juha Sorva's doctoral dissertation, titled *Visual Program Simulation in Introductory Programming Education*, where he revisits the difficulties cited by Du Boulay. Using more modern psychological and educational research, he describes his own set of the 5 most pressing challenges for novice programmers:
- citation + quote
Then describes the goals and functions of a Notional Machine:
- quote
Then forms a select group of principles which one should follow closely when designing a Notional Machine:
- quote

I came across several great examples of Notional Machines:

<img src="/pytutor.png" alt="PythonTutor" width="400"> <img src="/uuhistle.png" alt="UUhistle" width="200"> <img src="/novis.png" alt="Novis" width="200">

## Week 2: Making the Machine
My priority this week was understanding what information I can gather about a program before/during/after its execution. All of these together will form a set a tools that I may use to extract critical information about a program that needs to be represented in a Notional Machine. 

There are many modules for Python which I've started playing around with:
- AST (abstract syntax trees)
- StackTrace
- Trace
- PDB/BDB

This week I focused primarily on the AST module, and produced abstract syntax trees for a variety of sample Python programs.
- images of ASTs that we have produced

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
iunciuerniuewnviernvrv

## Week 4: The Debugger

[GitHub Repository](https://github.com/ERoels23/ERoels23.github.io/)
