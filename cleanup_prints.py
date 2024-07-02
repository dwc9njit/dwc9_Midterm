import os

def comment_out_prints(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                
                with open(file_path, 'w') as f:
                    in_multiline_string = False
                    for line in lines:
                        stripped_line = line.strip()

                        # Check if entering or leaving a multi-line string
                        if stripped_line.startswith('"""') or stripped_line.startswith("'''"):
                            in_multiline_string = not in_multiline_string
                        
                        # Comment out print statements if not in a multi-line string
                        if not in_multiline_string and stripped_line.startswith("print("):
                            f.write("# " + line)
                        else:
                            f.write(line)

comment_out_prints('.')
