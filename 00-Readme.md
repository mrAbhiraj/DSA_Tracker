# DSA Repo Organization Guide

This repository is designed for easy revision and consistent tracking of coding questions.

## Main Goal

Keep every question in a structured, searchable, and memorable layout so you can:

- find the topic quickly
- understand the pattern easily
- revise without confusion
- keep progress visible

## Recommended Folder Structure

```text
DSA/
├── 00-Readme.md
├── Study-Tracker.md
├── templates/
│   └── Question-Template.md
├── 01-Arrays/
│   ├── 01-LinearSearch/
│   │   ├── Problem.md
│   │   ├── solution.py
│   │   └── Notes.md
│   └── 02-BinarySearch/
│       ├── Problem.md
│       ├── solution.py
│       └── Notes.md
├── 02-Strings/
│   ├── 01-ReverseString/
│   └── 02-Anagram/
├── 03-LinkedList/
├── 04-StacksQueues/
├── 05-Trees/
├── 06-Graphs/
└── 07-RecursionBacktracking/
```

## Naming Convention

Use this format for every question folder:

```text
<chapter-number>-<ChapterName>/
    <question-number>-<QuestionName>/
        Problem.md
        solution.py
        Notes.md
```

Examples:

- 01-Arrays/01-LinearSearch/
- 02-Strings/02-ValidPalindrome/
- 05-Trees/01-BinaryTreeTraversal/

## What to Keep in Every Question Folder

Each question should contain:

1. Problem.md
   - problem statement
   - examples
   - constraints
   - hints

2. solution.py
   - final working solution
   - comments

3. Notes.md
   - approach
   - complexity
   - edge cases
   - mistakes to avoid

## Best Revision Pattern

After solving a question, always write:

- the idea in one line
- time complexity
- space complexity
- 2 tricky edge cases
- why this pattern matters

This is the easiest way to recall the question later during interviews or revisions.

## How to Track Progress

Keep a central tracker in Study-Tracker.md and update it after every problem:

- question name
- topic
- status
- difficulty
- date completed
- notes

## Smart Recall Rule

Use the format:

- What was the problem?
- Which pattern did it use?
- What was the key trick?
- What are the edge cases?
- What is the complexity?

If you can answer those 5 questions in under 30 seconds, you know the topic well.

## Suggested Daily Routine

- Solve 1 new problem
- Review 3 old problems
- Update Study-Tracker.md
- Write one-line recall summary
- Refactor code if needed

## Example of a Good Recall Line

"Linear Search checks each element from left to right and returns the first matching index, with O(n) time and O(1) space."

This structure keeps your repo clean, searchable, and interview-ready.
