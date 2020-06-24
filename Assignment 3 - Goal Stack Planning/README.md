# Goal Stack Planning

## Actual Algorithm
 
while stack is not empty:<br>
&emsp;if top of stack is predicate:<br>
&emsp;&emsp;if predicate is true:<br>
&emsp;&emsp;&emsp;pop it<br>
&emsp;&emsp;else: <br>
&emsp;&emsp;&emsp;pop it<br>
&emsp;&emsp;&emsp;push corresponding action that will satisfy that predicate onto stack<br>
&emsp;&emsp;&emsp;push preconditions of that action<br>
&emsp;if top of stack is action:<br>
&emsp;&emsp;pop it<br>
&emsp;&emsp;perform the action i.e add and delete it's effects from current state.<br>
&emsp;&emsp;add that action to the actual plan   <br>
