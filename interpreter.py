import sys


#parsing strings or lines
def parse_line(line):
    line = line.strip()
    if not line or line.startswith("#"):
        return None
    
    if '"' in line:
        cmd, rest = line.split(" ", 1)
        first_quote = rest.find('"')
        last_quote = rest.rfind('"')
        string_value = rest[first_quote + 1: last_quote]
        return cmd, [string_value]
    else:
        parts = line.split()
        cmd = parts[0]
        args = parts[1:]
        return cmd, args
        



#Stack Literals
def cmd_paint(stack, text):
    stack.append(text)

def cmd_brush_weight(stack, value):
    stack.append(int(value))

def cmd_trace(stack):
    stack.append(stack[-1])

def cmd_flip(stack):
    stack[-1], stack[-2] = stack[-2], stack[-1]

def cmd_erase(stack):
    stack.pop()






#Input/Output
def cmd_sketch(stack):
    line = input()
    stack.append(line)

def cmd_showoff(stack):
    value = stack.pop()
    print(value)





#Arithmetic
def cmd_blend(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b + a)

def cmd_mix(stack):
    a = int(stack.pop())
    b = int(stack.pop())
    stack.append(b * a)

def cmd_residue(stack):
    a = stack.pop()
    b = stack.pop()
    stack.append(b % a)





#Strings
def cmd_merge(stack):
    a = stack.pop()
    b= stack.pop()
    stack.append(str(b) + str(a))

def cmd_invert(stack):
    s = stack.pop()
    stack.append(s[::-1])        
    # sequence[start : stop : step] (slicing syntax) moving in step backwards by starting at the end to the beginning

def cmd_stipple(stack):
    count = stack.pop()
    char = stack.pop()
    stack.append(char * int(count))







#Logic You can choose to print booleans as True/False or convert them to "yes"/"no" in your programs.
def cmd_steady_hand(stack):
    n = int(stack.pop())
    stack.append(n % 2 ==0)

def cmd_mirror(stack):
    s = stack.pop()
    stack.append(s == s[::-1])






#Dictionary
def execute_program(lines, stack):
    commands ={
        "PAINT": cmd_paint,
        "BRUSHWEIGHT": cmd_brush_weight,
        "TRACE": cmd_trace,
        "FLIP": cmd_flip,
        "ERASE": cmd_erase,
        "SKETCH": cmd_sketch,
        "SHOWOFF": cmd_showoff,
        "+": cmd_blend,
        "BLEND": cmd_blend,
        "*": cmd_mix,
        "MIX": cmd_mix,
        "%": cmd_residue,
        "RESIDUE": cmd_residue,
        "MERGE": cmd_merge,
        "INVERT": cmd_invert,
        "STIPPLE": cmd_stipple,
        "STEADYHAND": cmd_steady_hand,
        "MIRROR": cmd_mirror,
    }
    for raw_line in lines:
        parsed = parse_line(raw_line)
        if parsed is None:
            continue
        cmd, args = parsed
        if cmd not in commands:
            raise ValueError(f"Unknown command: {cmd}")
        commands[cmd](stack, *args)
                






def main():
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <program_file>")
        return

    program_path = sys.argv[1]
    with open (program_path, "r", encoding = "utf-8") as f:
        lines = f.readlines()

    stack = []
    execute_program(lines, stack)

if __name__ == "__main__":
    main()
