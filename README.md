### Description:

A tool that has various features related to fibonacci sequence.

### Features:

- Viewing fibonacci sequence given 2 starting values and limit of how many items in the sequence should there be
- Returning the actual sequence values as a list
- Returning sequence as list or dict
- Returning sequence ratios and reversed ratios as pandas dataframe

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

    # Or the following to avoid pycache folder being created

    python3 -B src 

    ```

#### $${\color{orange}Windows}$$

1. Create a new folder "FOLDER_NAME":

    ```powershell
    mkdir PATH\TO\YOUR\FOLDER_NAME
    ```

2. Navigate to "FOLDER_NAME" in Command Prompt or PowerShell:

    ```powershell
    cd PATH\TO\YOUR\FOLDER_NAME
    ```

3. Clone the repository into this folder and navigate into it:

    ```powershell
    git clone https://github.com/MarekO-Dev/fibonacci_sequence
    cd fibonacci_sequence
    ```

    - If you don't have Git installed, visit:

    ```
    https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
    ```

4. Create a virtual environment using `venv` (comes standard with Python):

    ```powershell
    python -m venv NAME_OF_YOUR_VENV
    ```

5. Activate your virtual environment:

    ```powershell
    .\NAME_OF_YOUR_VENV\Scripts\activate
    ```

6. Install the required dependencies:

    ```powershell
    python -m pip install -r requirements.txt
    ```

7. Everything should now be set up. Run the example in `__main__.py`:

    ```powershell
    # Will run __main__.py inside src folder
    python src

    # Or the following to avoid pycache folder being created
    python -B src
    ```

#### $${\color{orange}MacOS}$$
1. Create a new folder "FOLDER_NAME":

    ```bash
    mkdir PATH/TO/YOUR/FOLDER_NAME
    ```

2. Navigate to "FOLDER_NAME" in Terminal:

    ```bash
    cd PATH/TO/YOUR/FOLDER_NAME
    ```

3. Clone the repository into this folder and navigate into it:

    ```bash
    git clone https://github.com/MarekO-Dev/fibonacci_sequence
    cd fibonacci_sequence
    ```

    - If you don't have Git installed, visit:

    ```
    https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
    ```

4. Create a virtual environment using `venv` (comes standard with Python):

    ```bash
    python3 -m venv NAME_OF_YOUR_VENV
    ```

5. Activate your virtual environment:

    ```bash
    source NAME_OF_YOUR_VENV/bin/activate
    ```

6. Install the required dependencies:

    ```bash
    python3 -m pip install -r requirements.txt
    ```

7. Everything should now be set up. Run the example in `__main__.py`:

    ```bash
    # Will run __main__.py inside src folder
    python3 src

    # Or the following to avoid pycache folder being created
    python3 -B src
    ```