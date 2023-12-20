def generate_pcnf(truth_table, num_arguments):
    pcnf = []
    for i, value in enumerate(truth_table):
        if not value:
            literals = [(chr(ord('A') + j) if (i >> j) & i == 0 else '~' + chr(ord('A') + j)) for j in range(num_arguments-1 ,-1, -1)]
            pcnf.append(' or '.join(literals))
    return ' and '.join(pcnf)

def generate_pdnf(truth_table, num_arguments):
    pdnf = []
    for i, value in enumerate(truth_table):
        if value:
            literals = [(chr(ord('A') + j) if (i >> j) & i == 1 else '~' + chr(ord('A') + j)) for j in range(num_arguments-1 ,-1, -1)]
            pdnf.append(' and '.join(literals))
    return ' or '.join(pdnf)

def translate_truth_table(input_sequence, output_format):
    num_arguments = len(input_sequence) // 2
    truth_table = [bool(int(x)) for x in input_sequence]
    if num_arguments == 4:
        num_arguments = num_arguments - 1
    if num_arguments < 2 or num_arguments > 5:
        print('Я НЕ БУДУ РАБОТАТЬ')
    pcnf_expression = generate_pcnf(truth_table, num_arguments)
    pdnf_expression = generate_pdnf(truth_table, num_arguments)
    if output_format.lower() == 'pcnf':
        return pcnf_expression
    elif output_format.lower() == 'pdnf':
        return pdnf_expression
    else:
        return "Invalid output format."

def gleb_snf(inp, pnf: str):
    if pnf.lower() == 'pcnf':
        pcnf_expression = translate_truth_table(inp, pnf)
        for _ in range(0, 100):
            if 'B' in pcnf_expression:
                pcnf_expression = pcnf_expression.replace('B', 'Q2', 1)
            if 'A' in pcnf_expression:
                pcnf_expression = pcnf_expression.replace('A', 'Q3', 1)
            if 'C' in pcnf_expression:
                pcnf_expression = pcnf_expression.replace('C', 'Q1', 1)
        print(f"PCNF: {pcnf_expression}")
    elif pnf.lower() == 'pdnf':
        pdnf_expression = translate_truth_table(inp, pnf)
        for _ in range(0, 100):
            if 'B' in pdnf_expression:
                pdnf_expression = pdnf_expression.replace('B', 'Q2', 1)
            if 'A' in pdnf_expression:
                pdnf_expression = pdnf_expression.replace('A', 'Q3', 1)
            if 'C' in pdnf_expression:
                pdnf_expression = pdnf_expression.replace('C', 'Q1', 1)
        print(f"PDNF: {pdnf_expression}")
    else:
        print('[ERROR]: O#@*&AAAAAA')


# input_sequence = input("Enter the sequence of 0s and 1s: ") #НАШ ИНПУТ КУДЫ ПИХАТЬ ЧИСЛО
# output_format = input("Enter the output format (PCNF / PDNF): ")
#pcnf_expression, pdnf_expression = translate_truth_table(input_sequence)

