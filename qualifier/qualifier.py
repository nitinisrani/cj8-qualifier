from typing import Any, List, Optional, final



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
    top_str = [('─'*(e+2)) for e in lengthList]
    final_str = ""
    final_str += '┌'+'┬'.join(top_str)+'┐ \n'

    if labels:
        final_str += empty_str.format(str(l)for l in labels )+'| \n'
        final_str += '├'+'┼'.join(top_str)+'┤ \n'

    for row in rows:
        final_str += empty_str.format(*row)+'| \n' 

    final_str += '└'+'┴'.join(top_str)+'┘ \n' 

    return(final_str)

print(make_table( rows=[
                    [None, 1, 2.5, None, 32j, '123'],
                ],
                labels=[3, None, 12, "A", 12.6, 12j],
                centered=True))