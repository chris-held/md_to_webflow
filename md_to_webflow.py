
import sys

def validate_args():
    if len(sys.argv) < 2:
        raise Exception("Include file argument")

def get_language(line):
    return line[3:].rstrip('\n')

def convert_start_code_to_webflow(line):
    language = get_language(line)
    return f'    -- CODE line-numbers language-{language} --\n'


def main():
    validate_args();
    file = sys.argv[1]
    with open(file) as f:
        lines_to_write = []
        is_start = True
        is_in_code_block = False
        for line in f:
            if(line.startswith('```')):
                if is_start:
                    line = convert_start_code_to_webflow(line)
                    lines_to_write.append(line);
                    lines_to_write.append("    <!--\n")
                    is_start = False
                    is_in_code_block = True
                else:
                    lines_to_write.append("    -->\n")
                    is_start = True
                    is_in_code_block = False
            else:
                if is_in_code_block:
                    lines_to_write.append("      " + line)
                else:
                    lines_to_write.append(line)
    
    with open(file + "-webflow.md", "w") as f:
        f.writelines(lines_to_write)

main()