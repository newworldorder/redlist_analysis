import re 

def export_csv(rows, filename):
    """Export RedList Data to CSV format."""
    p1 = 'position'
    r1 = 'response'
    c1 = 'category'
    with open(filename, 'w') as f:
        for r in rows:
            f.write('%s|%s|%s\n' % (r.get(p1),r.get(r1),str(r.get(c1))))

if __name__ == '__main__':
    raw_data = 'data/RedList_Table_Dump.txt'
    removals = set(['2015 Security "Red List"',
                    'www.somaini.net','6/2015'])
    new_lines = []
    with open(raw_data) as f:
        # extract the lines with responses 
        lines = [line.strip() for line in f.readlines()]
        num_lines = len(lines)
        index = 0
        while index < num_lines:
            if len(lines[index]) == 0 or lines[index] in removals:
                index += 1
                continue 
            term = []
            inc = True
            while re.search('\w|\-', lines[index]) != None:
                term.append(lines[index])
                index += 1
                inc = False
                if index >= num_lines:
                    break 
            if(inc):
                index += 1
            else:
                new_lines.append(' '.join(term))
    
    # organize the position, reponse, and sometimes category
    base = 3
    entry = {}
    labels = ['position', 'response', 'category']
    final_rows = []
    for index, new_line in enumerate(new_lines):
        if 'security dashboards' in new_line:
            base = 2 
        key = labels[index % base]
        entry[key] = new_line 
        if len(entry) == base:
            final_rows.append(entry)
            entry = dict() 


    # print the resulting data set
    export_csv(final_rows, 'data/tidy_redlist.csv')
    print "The number of respondents: ", len(final_rows)
