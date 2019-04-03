from db_controller.Definition import Definition
from db_controller.Manipulation import Manipulation

if __name__ == '__main__':
    # Usage examples
    table = 'Location'
    d2 = Definition('db1')
    s = d2.create_table(table)
    if s:
        s += d2.add_column('address', 'string', is_next=False)
        d2.cursor.execute(s)
    else:
        print('Table {} exists'.format(table))

    t = d2.show_tables()
    for x in t:
        print(x)

    s = d2.show_schema()
    for x in s:
        print(x)

    d2.commit_close()

    m2 = Manipulation('db1')
    template = m2.insert_record(table, 'address')
    print(template)
    v = m2.insert_values('Hamilton St.')
    print(v)
    m2.cursor.execute(template, m2.insert_values("Academy St."))

    q = m2.cursor.execute('SELECT * FROM address;').fetchall()
    print(q)

    m2.commit_close()