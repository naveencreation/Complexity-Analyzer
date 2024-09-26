import streamlit as st
import ast


def show_main_page():
   
    class ComplexityAnalyzer(ast.NodeVisitor):
        def __init__(self):
            self.time_complexity = "O(1)"  
            self.space_complexity = "O(1)"
            self.nested_loops = 0
            self.current_loop_depth = 0
            self.is_recursive = False
            self.variables = set()
            self.is_binary_search = False  
            self.has_halving = False       
            self.loop_counter = 0          
            self.recursive_calls = 0       

        def visit_FunctionDef(self, node):
            function_name = node.name
            self.is_recursive = any(isinstance(n, ast.Call) and getattr(n.func, 'id', None) == function_name for n in ast.walk(node))
            if self.is_recursive:
                self.recursive_calls += 1
            self.generic_visit(node)

        def visit_For(self, node):
            self.current_loop_depth += 1
            self.nested_loops = max(self.nested_loops, self.current_loop_depth)
            self.loop_counter += 1
            self.generic_visit(node)
            self.current_loop_depth -= 1

        def visit_While(self, node):
            if isinstance(node.test, ast.Compare) and len(node.body) > 0:
                for stmt in node.body:
                    if isinstance(stmt, ast.Assign):
                        if isinstance(stmt.value, ast.BinOp) and isinstance(stmt.value.op, ast.FloorDiv):
                            self.has_halving = True

            self.current_loop_depth += 1
            self.nested_loops = max(self.nested_loops, self.current_loop_depth)
            self.loop_counter += 1
            self.generic_visit(node)
            self.current_loop_depth -= 1

        def visit_Assign(self, node):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    self.variables.add(target.id)
            self.generic_visit(node)

        def analyze(self):
            if self.is_recursive:
                if self.nested_loops == 1 and self.recursive_calls > 1:
                    self.time_complexity = "O(n log n)"
                elif self.nested_loops == 0 and self.recursive_calls == 1 and self.has_halving:
                    self.time_complexity = "O(log n)"
                elif self.nested_loops == 1:
                    self.time_complexity = "O(n) * T(recursive)"
                elif self.nested_loops == 2:
                    self.time_complexity = "O(n^2) * T(recursive)"
                else:
                    self.time_complexity = f"O(n^{self.nested_loops}) * T(recursive)"
            else:
                if self.has_halving and self.loop_counter == 1:
                    self.time_complexity = "O(log n)"
                elif self.nested_loops == 1:
                    self.time_complexity = "O(n)"
                elif self.nested_loops == 2:
                    self.time_complexity = "O(n^2)"
                elif self.nested_loops > 2:
                    self.time_complexity = f"O(n^{self.nested_loops})"

            num_vars = len(self.variables)
            if num_vars > 0:
                self.space_complexity = f"O({num_vars} variables)"
            
            return self.time_complexity, self.space_complexity

    def wrap_snippet(snippet):
        if "def" not in snippet:
            snippet = f"def wrapped_function():\n    " + "\n    ".join(snippet.splitlines())
        return snippet

    def analyze_code(user_code):
        try:
            wrapped_code = wrap_snippet(user_code)
            tree = ast.parse(wrapped_code)
            analyzer = ComplexityAnalyzer()
            analyzer.visit(tree)
            time_complexity, space_complexity = analyzer.analyze()
            return time_complexity, space_complexity
        except Exception as e:
            return None, str(e)

    st.title(":blue[Time and Space Complexity Analyzer]")
    st.write("""
    ### Enter your Python code snippet or full code below, and this app will analyze the time and space complexity:
    """)

    user_code = st.text_area("Input your Python code snippet here:", height=300)

    if st.button("Analyze"):
        if user_code.strip() == "":
            st.error("Please input some Python code!")
        else:
            time_complexity, space_complexity = analyze_code(user_code)
            if time_complexity and space_complexity:
                st.success(f"**Estimated Time Complexity:** {time_complexity}")
                st.success(f"**Estimated Space Complexity:** {space_complexity}")
            else:
                st.error(f"Error: {space_complexity}")

    st.write("""
    ---
    
    """)
    st.markdown("<h5 style='text-align: center;'>Crafted with passion and a splash of fun! 🎉✨<br>Made with ❤️ by Naveen!</h5>", unsafe_allow_html=True)

