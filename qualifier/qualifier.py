from typing import Any, List, Optional



def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    if labels:
        newlist = list(zip(*rows,labels))
    else:
        newlist = list(zip(*rows))


    lengthList = []
    for row in newlist:
        longest = max(map(str,row),key=len)
        lengthList.append(len(str(longest)))
    
       
  
    empty_str = ''
    for i in lengthList:
        if centered:
            empty_str += '| {'+':^{}'.format(i)+'} '
        else:
            empty_str += '| {'+':<{}'.format(i)+'} '
    top_str = [('─'*e) for e in lengthList]
    
    print('┌─'+'─┬─'.join(top_str)+'─┐')

    if labels:
        print(empty_str.format(*labels)+'|') 
        print('├─'+'─┼─'.join(top_str)+'─┤')

    for row in rows:
        print(empty_str.format(*row)+'|')
    print('└─'+'─┴─'.join(top_str)+'─┘')

