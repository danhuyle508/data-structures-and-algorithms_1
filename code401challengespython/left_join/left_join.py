from hashtable import HashTable

def left_join(table1,table2):
    output = []

    def add_first_table(table):

        for i in range(len(table.table)-1):
            if table.table[i] is not None:
                linked_list = table.table[i]
                curr = linked_list.head
                while curr:
                    output.append([curr.value[0],curr.value[1]])
                    curr = curr._next

        return output

    def join(list, table):

        for value in list:
            if table.contains(value[0]):
                value.append(table.get(value[0]))
            else:
                value.append(None)
    join(add_first_table(table1),table2)
    return output                