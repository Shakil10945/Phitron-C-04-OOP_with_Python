def difference_update(set1,set2):
    st = set1.copy()
    for item in set1:
        if (item in set2):
            st.remove(item)
    return st

    

set1 = {10, 20, 30}
set2 = {20, 40, 50}


print(difference_update(set1,set2))