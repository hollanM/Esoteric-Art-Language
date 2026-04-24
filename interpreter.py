import sys


#parsing strings or lines
def parseLine(line):
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
def cmd_paint(stack, value):
    #value = value.strip()
    if (value.startswith('"') and value.endswith('"')) or \
       (value.startswith("'") and value.endswith("'")):
        stack.append(value[1:-1])
        return
    if value.isdigit() or (value.startswith("-") and value[1:].isdigit()):
        stack.append(int(value))
        return
    stack.append(value)


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
    if line.isdigit() or (line.startswith("-") and line[1:].isdigit()):
        stack.append(int(line))
    else:
        stack.append(line)

def cmd_showoff(stack):
    value = stack.pop()
    print(value)





#Arithmetic
def cmd_blend(stack):
    a = stack.pop()
    b = stack.pop()
    if isinstance(a, str) and isinstance(b, str):
        stack.append(b + a)
        return  
    if isinstance(a, int) and isinstance(b, int):
        stack.append(b + a)
        return
    raise TypeError("BLEND: unsupported types")


def cmd_mix(stack):
    a = stack.pop()
    b = stack.pop()
    if isinstance(a, int) and isinstance(b, int):
        stack.append(b * a)
        return
    if isinstance(a, int) and isinstance(b, str):
        stack.append(b * a)
        return
    if isinstance(a, str) and isinstance(b, int):
        stack.append(a * b)
        return
    raise TypeError("MIX: unsupported types")


def cmd_residue(stack):
    a = stack.pop()
    b = stack.pop()
    if isinstance(a, int) and isinstance(b, int):
        stack.append(b % a)
        return
    raise TypeError("RESIDUE: unsupported types")

def cmd_mirror(stack):
    a = stack.pop()
    b = stack.pop()
    if isinstance(a, int) and isinstance(b, int):
        stack.append(a == b)
        return
    if isinstance(a, str) and isinstance(b, str):
        stack.append(a == b)
        return
    raise TypeError("MIRROR: unsupported types (must be two ints or two strings)")








#Strings
def cmd_merge(stack):
    a = stack.pop()
    b= stack.pop()
    stack.append(str(b) + str(a))

def cmd_invert(stack):
    s = stack.pop()
    stack.append(s[::-1])        
    # sequence[start : stop : step] (slicing syntax) moving in step backwards by starting at the end to the beginning









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
        "MIRROR": cmd_mirror,
        "==": cmd_mirror,

    }
    for rawLine in lines:
        parsed = parseLine(rawLine)
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
    with open (program_path, "r", encoding = "utf-8") as file:
        lines = file.readlines()

    stack = []
    execute_program(lines, stack)

if __name__ == "__main__":
    main()
