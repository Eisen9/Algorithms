# Highest Common Factor Algorithm

## What is in this document:
  * HCF Algorithm Idea
  * HCF Pseudo Code
  * HCF Python Code (Task)

### Idea

We want to find the HCF for two numbers by using the modulus operator.
I.e. When the two numbers have a modulus of 0 then a common factor is found.

To achieve this, we want to create a counter that is set to the highest common factor value, then decrement this counter until the first instance of (x%i==0 && y%i==0), when this first encounter is found, then, this is going to be our HCF.
Note: if the idea is not clear, you will find it clearer in the pseudo code.

### Pseudo Code Annotated


For simplicity, we will initialise the values of the two numbers for which we are going to find the HCF. In your code, it is better that you take the user inputs and save them to variables.


```
// we set a flag. I.e we loop as long as the HCF isn't found
found = false

// we initialise the variables (two numbers for the HCF)
x = 12
y = 8

// we set the value of i (the counter) to x. This is where we start incrementing from.

// we create a while loop. We loop as long as value is greater than 1, and found is false.

while(i>= 1 && found == false){
    if(x%i == 0 && y%i == 0){
        found = true
    } else {
        i--
    }
}

Print("HCF for ", x, " and ", y, " is ", i )

```

### Python Code (Task)

```

x = int(input())
y = int(input())
i = x
found = False
while i >= 1 and found == False:
    if(x%i==0 and y%i==0):
        found = True
    else:
        i= i -1

print(i)

```
