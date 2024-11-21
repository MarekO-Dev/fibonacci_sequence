### Description:

A tool that has various different features related to fibonacci sequence.

### Features:

- Viewing fibonacci sequence given 2 starting values and limit of how many items in the sequence should there be
- Returning the actual sequence values as a list
- Various visualisation options of fibonacci sequence or ratios

### Guide how to get all to work:

#### $${\color{orange}Linux}$$

1. Create a new folder "FOLDER_NAME":
    
    ```bash

        mkdir PATH/TO/YOUR/FOLDER_NAME

    ```
    
2. Navigate "FOLDER_NAME" this folder in terminal:
    
    ```bash
    
    cd PATH/TO/YOUR/FOLDER_NAME

    ```

3. Clone repository to this above folder and cd into it

    ```bash

    git clone https://github.com/MarekO-Dev/fibonacci_sequence
    cd fibonacci_sequence


    ```
    -   If you don't have git installed visit: 

    ```
    https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

    ```

4. Create virtual enviroment using venv (It comes as standard with python)

    ```bash

    python3 -m venv NAME_OF_YOUR_VENV

    ```

5. Enter your venv

    ```bash

    source NAME_OF_YOUR_VENV/bin/activate

    ```

6. Install requirements:

    ```bash

    python3 -m pip install -r requirements.txt

    ```

7. And it should all be ready now. Run example in __main__.py

    ```bash

    # Will run __main__.py inside src folder
    python3 src

    ```

#### $${\color{orange}Windows}$$

    TODO:

#### $${\color{orange}MacOS}$$

    TODO:


### How to use

1. Firstly you have to create a sequence object(s) and you do it this way:

```python

FibonacciSequence(**{
    "starts_with": (0.0, 1),
    "length": 10
})

```

And if you would like to create multiple for example for some cool visualisations you can do it by calling multiples of the above like this:

```python

FibonacciSequence(**{
    "starts_with": (0.0, 1),
    "length": 10
})

FibonacciSequence(**{
    "starts_with": (0.0, 1),
    "length": 10
})


```

*Note: You don't have to assign these to variables, it is simply not needed

Or you can chain it like this:

```python

FibonacciSequence(**{
    "starts_with": (0.0, 1),
    "length": 10
})(**{
    "starts_with": (0.1, 1),
    "length": 10
})

FibonacciSequence(**{
    "starts_with": (0.0, 1),
    "length": 10
})(**{
    "starts_with": (0.1, 1),
    "length": 10
})(**{
    "starts_with": (0.1, 1),
    "length": 10
})(**{
    "starts_with": (0.1, 1),
    "length": 10
})



# Or mixture of both :)

```

2. Now you can do various things like viewing some ratios or actual sequence or you can head straight to visualisations. You do this by:

    a) Viewing various stats in the terminal
        To be continued...
    b) Visualising some plots
        To be continued...