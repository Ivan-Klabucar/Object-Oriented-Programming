import ast
import re

def eval_expression(exp, variables={}):
    def _eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Name):
            return variables[node.id]
        elif isinstance(node, ast.BinOp):
            return _eval(node.left) + _eval(node.right)
        else:
            raise Exception('Unsupported type {}'.format(node))

    node = ast.parse(exp, mode='eval')
    return _eval(node.body)

class Cell:
    def __init__(self, exp, name):
        self.exp = exp
        self.value = None
        self.dependees = []
        self.name = name

class Sheet:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = dict()
    
    def check_if_in_bounds(self, coordinates):
        if not len(coordinates) == 2 or \
           ord(coordinates[0]) - ord('A') >= self.rows or \
           ord(coordinates[1]) - ord('1') >= self.cols: raise Exception('Cell out of bounds!')

    def check_if_cycle_in_refs(self, ref):
        open = set([ref])
        closed = set()
        while open:
            curr_ref = open.pop()
            closed.add(curr_ref)
            for r in self.getrefs(self.cell(curr_ref)):
                if r.name == ref: raise Exception('Circular definition!')
                if r.name not in closed: open.add(r.name)

    def update_cell(self, cell):
        cell.value = self.evaluate(cell)
        for c in cell.dependees:
            self.update_cell(c)

    def set(self, ref, content):
        coordinates = list(ref)
        self.check_if_in_bounds(coordinates)
        old_cell = None
        if ref in self.table: old_cell = self.table[ref]
        self.table[ref] = Cell(content, ref)
        try:
            self.check_if_cycle_in_refs(ref)
        except Exception as e:
            del self.table[ref]
            if old_cell: self.table[ref] = old_cell
            raise e
        if old_cell: self.table[ref].dependees = old_cell.dependees
        for r in self.getrefs(self.table[ref]): r.dependees.append(self.table[ref])
        self.update_cell(self.table[ref])
    
    def cell(self, ref):
        return self.table[ref]
        
    
    def getrefs(self, cell):
        matcher = re.compile('[A-Z][0-9][0-9]*')
        matches = matcher.findall(cell.exp)
        return [self.cell(r) for r in matches]
    
    def evaluate(self, cell):
        refs = self.getrefs(cell)
        vars = dict()
        for ref in refs: vars[ref.name] = ref.value
        return eval_expression(cell.exp, vars)
    
    def print(self):
        cells = [x for x in self.table]
        cells.sort()
        for x in cells:
            print(f'{x}: {self.cell(x).value}')


s=Sheet(5,5)
print()

s.set('A1','2')
s.set('A2','5')
s.set('A3','A1+A2')
s.print()
print()

s.set('A1','4')
s.set('A4','A1+A3')
s.print()
print()

try:
    s.set('A1','A3')
except Exception as e:
    print("Caught exception:",e)
    s.print()
    print()