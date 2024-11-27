# NOTE : NPI Calculator is a really known leetcode problem that you can find here : https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

# src/calculator.py

def calculate_npi(expression: str) -> float:
    """
    Calculate result of NPI expression
    
    Args:
        expression: Space-separated numbers and operators (e.g. "3 4 +")
    Returns:
        Result of the calculation
    """

    stack = []
    tokens = expression.split()
    operators = ["+", "-", "/", "*"]
    
    for tok in tokens:
        if tok not in operators:
            try:
                stack.append(float(tok))
            except ValueError:
                raise ValueError(f"Invalid number: {tok}")
        else:
            if len(stack) < 2:
                raise ValueError("Not enough operands")
                
            v1 = stack.pop()
            v2 = stack.pop()
            
            if tok == "+":
                v3 = v2 + v1
            elif tok == "-":
                v3 = v2 - v1
            elif tok == "/":
                if v1 == 0:
                    v3 = float('inf')  # Handle division by zero
                else:
                    v3 = v2 / v1
            elif tok == "*":
                v3 = v2 * v1
                
            stack.append(v3)
    
    if not stack:
        raise ValueError("Empty expression")
        
    return stack[0]