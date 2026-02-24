import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import sys
import subprocess
import tempfile
import os

class ContentManager:
    """
    Manages the educational content (Modules, Topics, Examples).
    Acts as the 'Model' in the application.
    """
    def __init__(self):
        self.data = {
            "Introduction": {
                "What is Python?": {
                    "explanation": "Python is a high-level, interpreted programming language known for its readability and versatility.",
                    "learn": "Understand that Python emphasizes code readability and allows you to express concepts in fewer lines of code than languages like C++ or Java.",
                    "real_world": "Web development (Django), Data Science (Pandas), AI (TensorFlow), and Automation scripts.",
                    "code": "print('Hello, World!')\nprint('Welcome to Python!')"
                },
                "Installation & Setup": {
                    "explanation": "Python must be installed on your OS. You usually run python scripts via a terminal or an IDE.",
                    "learn": "How to verify installation using 'python --version'.",
                    "real_world": "Setting up development environments for servers.",
                    "code": "import sys\nprint(f'Python Version: {sys.version}')"
                }
            },
            "Variables": {
                "Creating Variables": {
                    "explanation": "Variables are containers for storing data values. Python has no command for declaring a variable.",
                    "learn": "A variable is created the moment you first assign a value to it.",
                    "real_world": "Storing user names, scores in a game, or bank balances.",
                    "code": "x = 5\ny = 'John'\nprint(x)\nprint(y)"
                },
                "Variable Names": {
                    "explanation": "A variable name must start with a letter or the underscore character. It cannot start with a number.",
                    "learn": "Naming conventions (snake_case) and restrictions.",
                    "real_world": "Writing readable code that other developers can understand.",
                    "code": "my_var = 'Sally'\n_my_var = 'John'\nprint(my_var)\nprint(_my_var)"
                }
            },
            "Data Types": {
                "Numbers": {
                    "explanation": "There are three numeric types in Python: int, float, and complex.",
                    "learn": "Difference between integers (whole numbers) and floats (decimals).",
                    "real_world": "Calculating prices, physics simulations, or counting items.",
                    "code": "x = 1    # int\ny = 2.8  # float\nprint(type(x))\nprint(type(y))"
                },
                "Strings": {
                    "explanation": "Strings in python are surrounded by either single quotation marks, or double quotation marks.",
                    "learn": "String slicing, concatenation, and formatting.",
                    "real_world": "Processing text data, user inputs, and logging.",
                    "code": "a = 'Hello'\nprint(a[1])\nprint(len(a))\nprint(a.upper())"
                }
            },
            "Control Flow": {
                "If...Else": {
                    "explanation": "Python supports the usual logical conditions from mathematics.",
                    "learn": "Indentation is crucial in Python to define blocks of code.",
                    "real_world": "Decision making: If user is logged in, show dashboard, else show login page.",
                    "code": "a = 33\nb = 200\nif b > a:\n    print('b is greater than a')"
                },
                "For Loops": {
                    "explanation": "A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).",
                    "learn": "How to iterate through data structures.",
                    "real_world": "Processing a list of customer orders.",
                    "code": "fruits = ['apple', 'banana', 'cherry']\nfor x in fruits:\n    print(x)"
                }
            },
            "Functions": {
                "Defining Functions": {
                    "explanation": "A function is a block of code which only runs when it is called.",
                    "learn": "Use the 'def' keyword. Information can be passed as arguments.",
                    "real_world": "Reusing logic (e.g., a function to calculate tax) across an application.",
                    "code": "def my_function(fname):\n    print(fname + ' Refsnes')\n\nmy_function('Emil')\nmy_function('Tobias')"
                }
            },
            "OOP Basics": {
                "Classes & Objects": {
                    "explanation": "Python is an object oriented programming language. Almost everything in Python is an object, with its own properties and methods.",
                    "learn": "The difference between a Class (blueprint) and Object (instance).",
                    "real_world": "Modeling real entities like 'User', 'Product', or 'Vehicle' in software.",
                    "code": "class Person:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\np1 = Person('John', 36)\nprint(p1.name)\nprint(p1.age)"
                }
            },
            "Modules & Packages": {
                "Importing": {
                    "explanation": "A module is a file containing a set of functions you want to include in your application.",
                    "learn": "How to use 'import' and 'from ... import ...'.",
                    "real_world": "Using standard libraries like 'math' or 'datetime'.",
                    "code": "import math\nprint(math.pi)\nprint(math.sqrt(64))"
                }
            },
            "File Handling": {
                "Reading/Writing": {
                    "explanation": "The key function for working with files in Python is the open() function.",
                    "learn": "Modes: 'r' (read), 'w' (write), 'a' (append). Always close files or use 'with'.",
                    "real_world": "Saving logs, reading configuration files, or exporting reports.",
                    "code": "# Writing\nwith open('test.txt', 'w') as f:\n    f.write('Hello Python!')\n\n# Reading\nwith open('test.txt', 'r') as f:\n    print(f.read())"
                }
            },
            "Error Handling": {
                "Try...Except": {
                    "explanation": "The try block lets you test a block of code for errors. The except block lets you handle the error.",
                    "learn": "Preventing program crashes when unexpected input occurs.",
                    "real_world": "Handling network failures or missing files gracefully.",
                    "code": "try:\n    print(x)\nexcept NameError:\n    print('Variable x is not defined')\nexcept:\n    print('Something else went wrong')"
                }
            }
        }

    def get_modules(self):
        return list(self.data.keys())

    def get_topics(self, module_name):
        if module_name in self.data:
            return list(self.data[module_name].keys())
        return []

    def get_lesson(self, module_name, topic_name):
        return self.data.get(module_name, {}).get(topic_name, None)


class CodeRunner:
    """
    Handles the execution of Python code safely using subprocess.
    """
    @staticmethod
    def run_code(code_string):
        if not code_string.strip():
            return "No code to run."

        # Create a temporary file to execute the code
        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as tmp_file:
                tmp_file.write(code_string)
                tmp_file_path = tmp_file.name

            # Run the subprocess
            # We set a timeout to prevent infinite loops freezing the app
            result = subprocess.run(
                [sys.executable, tmp_file_path],
                capture_output=True,
                text=True,
                timeout=5
            )
            
            output = result.stdout
            if result.stderr:
                output += "\n[ERROR]\n" + result.stderr

        except subprocess.TimeoutExpired:
            output = "Error: Code execution timed out (Infinite loop?)."
        except Exception as e:
            output = f"System Error: {str(e)}"
        finally:
            # Clean up temp file
            if 'tmp_file_path' in locals() and os.path.exists(tmp_file_path):
                os.remove(tmp_file_path)
        
        return output


class NavigationPanel(tk.Frame):
    """
    Left sidebar for selecting Modules and Topics.
    """
    def __init__(self, parent, content_manager, on_topic_select):
        super().__init__(parent, width=200, bg="#f0f0f0")
        self.content_manager = content_manager
        self.on_topic_select = on_topic_select
        self.pack_propagate(False) # Enforce width

        # Header
        lbl = tk.Label(self, text="Course Modules", font=("Arial", 12, "bold"), bg="#f0f0f0")
        lbl.pack(pady=10)

        # Treeview for Modules -> Topics
        self.tree = ttk.Treeview(self, show="tree")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbar for tree
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.populate_tree()
        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def populate_tree(self):
        modules = self.content_manager.get_modules()
        for mod in modules:
            mod_id = self.tree.insert("", "end", text=mod, open=False)
            topics = self.content_manager.get_topics(mod)
            for topic in topics:
                self.tree.insert(mod_id, "end", text=topic)

    def on_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            item_text = self.tree.item(selected_item[0], "text")
            parent_id = self.tree.parent(selected_item[0])
            
            # If parent_id exists, it means a topic was clicked (not a module)
            if parent_id:
                module_text = self.tree.item(parent_id, "text")
                self.on_topic_select(module_text, item_text)


class LessonPanel(tk.Frame):
    """
    Displays the educational content (Explanation, Real World Use, etc).
    """
    def __init__(self, parent):
        super().__init__(parent, bg="white")
        
        # Title
        self.title_lbl = tk.Label(self, text="Select a Topic", font=("Arial", 16, "bold"), bg="white", anchor="w")
        self.title_lbl.pack(fill=tk.X, padx=10, pady=10)

        # Scrollable Text Area for content
        self.text_area = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("Segoe UI", 10), state=tk.DISABLED, padx=10, pady=10)
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Tag configurations for formatting
        self.text_area.tag_config("header", font=("Segoe UI", 11, "bold"), foreground="#2c3e50")
        self.text_area.tag_config("normal", font=("Segoe UI", 10))
        self.text_area.tag_config("highlight", background="#e8f6f3", font=("Consolas", 10))

    def update_content(self, topic_name, data):
        self.title_lbl.config(text=topic_name)
        
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        
        if not data:
            self.text_area.insert(tk.END, "No content available.")
            self.text_area.config(state=tk.DISABLED)
            return

        # 1. Explanation
        self.text_area.insert(tk.END, "Explanation:\n", "header")
        self.text_area.insert(tk.END, f"{data['explanation']}\n\n", "normal")

        # 2. What to learn
        self.text_area.insert(tk.END, "Key Concepts:\n", "header")
        self.text_area.insert(tk.END, f"{data['learn']}\n\n", "normal")

        # 3. Real World
        self.text_area.insert(tk.END, "Real World Application:\n", "header")
        self.text_area.insert(tk.END, f"{data['real_world']}\n\n", "normal")

        self.text_area.config(state=tk.DISABLED)


class EditorPanel(tk.Frame):
    """
    Code Editor and Output Console.
    """
    def __init__(self, parent):
        super().__init__(parent)
        
        # Toolbar
        toolbar = tk.Frame(self, bg="#ddd", height=30)
        toolbar.pack(fill=tk.X, side=tk.TOP)
        
        lbl = tk.Label(toolbar, text="Code Editor", bg="#ddd", font=("Arial", 9, "bold"))
        lbl.pack(side=tk.LEFT, padx=5)

        self.run_btn = tk.Button(toolbar, text="▶ Run Code", command=self.execute_code, bg="#2ecc71", fg="white", font=("Arial", 9, "bold"))
        self.run_btn.pack(side=tk.RIGHT, padx=5, pady=2)

        # Split Editor and Console
        self.paned = tk.PanedWindow(self, orient=tk.VERTICAL)
        self.paned.pack(fill=tk.BOTH, expand=True)

        # Input Area
        self.code_input = scrolledtext.ScrolledText(self.paned, wrap=tk.NONE, font=("Consolas", 11), bg="#282c34", fg="#abb2bf", insertbackground="white")
        self.paned.add(self.code_input, height=200)

        # Output Area
        output_frame = tk.Frame(self.paned)
        output_lbl = tk.Label(output_frame, text="Console Output:", font=("Arial", 8, "bold"))
        output_lbl.pack(anchor="w")
        
        self.console_output = scrolledtext.ScrolledText(output_frame, wrap=tk.WORD, font=("Consolas", 10), bg="#000000", fg="#00ff00", state=tk.DISABLED)
        self.console_output.pack(fill=tk.BOTH, expand=True)
        
        self.paned.add(output_frame, height=100)

    def set_code(self, code):
        self.code_input.delete(1.0, tk.END)
        self.code_input.insert(tk.END, code)

    def execute_code(self):
        code = self.code_input.get(1.0, tk.END)
        self.console_output.config(state=tk.NORMAL)
        self.console_output.delete(1.0, tk.END)
        self.console_output.insert(tk.END, "Running...\n")
        self.console_output.update()

        # Run via CodeRunner class
        result = CodeRunner.run_code(code)
        
        self.console_output.delete(1.0, tk.END)
        self.console_output.insert(tk.END, result)
        self.console_output.config(state=tk.DISABLED)


class PythonTutorApp(tk.Tk):
    """
    Main Application Window.
    """
    def __init__(self):
        super().__init__()
        self.title("Python Tutor - Learn by Doing")
        self.geometry("1000x700")
        
        # Initialize Data Manager
        self.content_manager = ContentManager()

        # Main Layout (PanedWindow for resizing)
        self.main_pane = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.main_pane.pack(fill=tk.BOTH, expand=True)

        # 1. Navigation Panel (Left)
        self.nav_panel = NavigationPanel(self.main_pane, self.content_manager, self.load_topic)
        self.main_pane.add(self.nav_panel, width=220)

        # Right Side (Content + Editor)
        self.right_pane = tk.PanedWindow(self.main_pane, orient=tk.VERTICAL)
        self.main_pane.add(self.right_pane)

        # 2. Lesson Panel (Top Right)
        self.lesson_panel = LessonPanel(self.right_pane)
        self.right_pane.add(self.lesson_panel, height=300)

        # 3. Editor Panel (Bottom Right)
        self.editor_panel = EditorPanel(self.right_pane)
        self.right_pane.add(self.editor_panel)

        # Load initial welcome message
        self.show_welcome()

    def show_welcome(self):
        welcome_data = {
            "explanation": "Welcome to the Python Tutor App!",
            "learn": "Select a module from the left sidebar to begin your journey.",
            "real_world": "This application itself is built using Python and Tkinter!",
            "code": "# Try modifying this code and click Run!\nname = 'Student'\nprint(f'Welcome, {name}!')"
        }
        self.lesson_panel.update_content("Welcome", welcome_data)
        self.editor_panel.set_code(welcome_data['code'])

    def load_topic(self, module_name, topic_name):
        data = self.content_manager.get_lesson(module_name, topic_name)
        if data:
            self.lesson_panel.update_content(topic_name, data)
            self.editor_panel.set_code(data['code'])
            # Clear console on new topic load
            self.editor_panel.console_output.config(state=tk.NORMAL)
            self.editor_panel.console_output.delete(1.0, tk.END)
            self.editor_panel.console_output.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = PythonTutorApp()
    app.mainloop()