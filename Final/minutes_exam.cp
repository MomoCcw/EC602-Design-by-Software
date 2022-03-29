// Midterm Two: C++

// EXAM TIMING: please read
//
// You have until 4:15pm to finish the exam
//
// Late submissions will be accepted until 4:30pm
// with a penalty of 1 point per minute.
// 
// Emailed submissions will be penalized at 2 points
// per minute after 4:30pm.


// EXAM DESCRIPTION

// Your copyright notice is required. Please do that
// now and not when you are about to submit.

// This exam is all about the minutes in a day
// The first minute is 00:00 and the last one is 23:59
//
// We use 24-hour format throughout (NOT the 12-hour am/pm
// format)

// There are 24*60 = 1440 minutes in each day

// We label these minutes from 0 to 1439.

// Please read the entire exam before beginning part 1.

// PART 1: write a function "get_minute" that returns 
// a string. It has one integer argument. The argument 
// is the label of the minute to retrieve within a day.
// 
// So, get_minute(0) should return "00:00" and get_minute(1439)
// should return "23:59". 
// get_minute(89) should return "01:29"

// get_minute should raise an exception if the label is out
// of range

// it is important that all minutes have exactly 5 characters
// as they would be displayed by a clock.







// PART 2: write a class "Minute" that models the minutes
// of a day.
// 
// Your class should have these three methods and whatever
// else is necessary to make the methods work:
// 
// 1. "all_minutes" should return a vector of strings with
// the all the minutes of the day in the correct order,
// first to last.
//
// 2."get_minute" which works the same way as the function
// in part 1 (but it is a method of the Minute class).
// What happens for out of range should be configurable 
// in the constructor
//
// 3. A constructor with a boolean argument "enable_exception" that allows
// the behavior of the method "get_minute" to be modified.
//  - if "enable_exception" is True, then an exception should be
//    raised when the label of "get_minute" is out of range
//  - if "enable_exception" is False, then get_minute should return
//    the string "??:??"







// PART 3:
//
// Write a main() program that performs tests
// of the code you wrote for parts 1 and 2, including
// the out of range behaviors.
//
// Your program should not use `stdin`, i.e. when compiled
// and run, it should finish without any user input
// required.

// Grading
// -------
// Your program will be evaluated based on these factors:
// 
// - successfully compiling 
// - correctness of part 1 and 2
// - test code in main() 
// - program simplicity, program structure and readability
//

// Additionally, some bonus points will be awarded for
//
//  - never using brackets
//  - never using the push_back method
//  - avoiding magic numbers
//  - program brevity (words + lines not counting comments)

