def open_file(f_name, mode='r'):
    print(f'openinig {f_name} file')
    f = open(f_name, mode)
    try:
        yield f
    finally:
        print(f'closing {f_name} file')
        f.close()
