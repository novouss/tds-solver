
def host_portfolio(html_tag: str) -> str:
    
    static_index = "./index.html"
    
    with open(static_index, "r") as file:
        lines = file.readlines()
        
    for idx, line in enumerate(line):
        if "<!---Add Content Here--->" in line:
            lines.insert(idx + 1, html_tag + "\n")
    
    with open(static_index, "w") as file:
        file.writelines(lines)
    
    return "https://novouss.github.io/tds-solver/"
        