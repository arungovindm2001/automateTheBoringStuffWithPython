#### You can see the execution of the program here:<br />

[The Collatz Sequence with Input Validation.py](http://pythontutor.com/visualize.html#code=def%20collatz%28number%29%3A%0A%20%20%20%20if%20number%20%25%202%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20number//2%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%203*number%2B1%0A%20%20%20%20%0Atry%3A%0A%20%20%20%20print%28'Enter%20number%3A'%29%0A%20%20%20%20number%20%3D%20int%28input%28%29%29%0A%20%20%20%20n%3Dcollatz%28number%29%0A%20%20%20%20print%28n%29%0A%0A%20%20%20%20while%20n-1%20!%3D%200%3A%20%20%20%20%0A%20%20%20%20%20%20%20%20n%3Dcollatz%28n%29%0A%20%20%20%20%20%20%20%20print%28n%29%0A%0Aexcept%20ValueError%3A%0A%20%20%20%20print%28'You%20must%20enter%20an%20integer'%29&cumulative=false&curInstr=46&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%2210%22%5D&textReferences=false)<br />
<br />
[The Collatz Sequence.py](http://pythontutor.com/visualize.html#code=def%20collatz%28number%29%3A%0A%20%20%20%20if%20number%20%25%202%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20return%20number//2%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%203*number%2B1%0A%0Aprint%28'Enter%20number%3A'%29%0Anumber%20%3D%20int%28input%28%29%29%0A%0An%3Dcollatz%28number%29%0Aprint%28n%29%0A%0Awhile%20n-1%20!%3D%200%3A%20%20%20%20%0A%20%20%20%20n%3Dcollatz%28n%29%0A%20%20%20%20print%28n%29%0A&cumulative=false&curInstr=45&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%2210%22%5D&textReferences=false)